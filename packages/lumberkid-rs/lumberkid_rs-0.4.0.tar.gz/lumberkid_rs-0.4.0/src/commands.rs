use crate::{
    forge::{self, Forge, MergeMethod},
    issue::{Issue, IssueTitle},
    shell_utils::shell_out,
};

use inquire::Text;
use regex::Regex;
use std::process::Command;

pub fn ready(forge: &dyn Forge) -> Result<(), std::io::Error> {
    let merge_method = MergeMethod::Squash;
    let automerge = true;

    println!(
        "Marking as ready with \n\tAuto-merge: {}\n\tMerge-method: {}",
        match automerge {
            true => "true",
            false => "false",
        },
        format!("{:?}", merge_method)
    );
    forge.ready(true, forge::MergeMethod::Squash, false); // TODO: Get this from the config
    println!("Marked as ready.");
    Ok(())
}

pub fn rapid_add(
    migrate_changes: bool,
    default_branch: &str,
    start_as_draft: bool,
    forge: &dyn Forge,
) -> Result<(), std::io::Error> {
    let input_str = Text::new("Title of the new change:").prompt().unwrap();
    let issue_title = semver_issue_parser(&input_str);

    let needs_migration = migrate_changes && !repo_is_clean()?;
    if needs_migration {
        shell_out("git", &["stash", "save", "--include-untracked"])?;
    }

    shell_out("git", &["fetch", "origin"])?;
    shell_out(
        "git",
        &[
            "checkout",
            "-b",
            &branch_title(&issue_title),
            "--no-track",
            &format!("origin/{}", &default_branch),
        ],
    )?;

    if needs_migration {
        shell_out("git", &["stash", "pop"])?;
    }

    shell_out(
        "git",
        &["commit", "--allow-empty", "-m", &branch_title(&issue_title)],
    )?;
    shell_out("git", &["push"])?;

    forge.begin(Issue { title: issue_title }, start_as_draft)?;

    Ok(())
}

fn branch_title(issue: &IssueTitle) -> String {
    return issue.content.replace(" ", "_").replace(":", "");
}

fn repo_is_clean() -> Result<bool, std::io::Error> {
    let output = Command::new("git")
        .args(["status", "--porcelain"])
        .output()?;

    if !output.status.success() {
        // Git command failed, assume there are changes
        return Ok(false);
    }

    let git_status = String::from_utf8_lossy(&output.stdout);
    Ok(git_status.trim().is_empty())
}

fn semver_issue_parser(input_str: &str) -> IssueTitle {
    let prefix = Regex::new(r"^(.+?)[:].*").unwrap().captures(input_str);

    match prefix {
        Some(prefix) => IssueTitle {
            prefix: Some(prefix.get(1).unwrap().as_str().to_string()),
            content: input_str.to_string(),
        },
        None => IssueTitle {
            prefix: None,
            content: input_str.to_string(),
        },
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_semver_issue_parser_with_prefix() {
        let issue = "feat: Implement new feature";
        let expected = IssueTitle {
            prefix: Some("feat".to_string()),
            content: "feat: Implement new feature".to_string(),
        };
        assert_eq!(semver_issue_parser(issue), expected);
    }

    #[test]
    fn test_semver_issue_parser_without_prefix() {
        let issue = "Implement new feature";
        let expected = IssueTitle {
            prefix: None,
            content: "Implement new feature".to_string(),
        };
        assert_eq!(semver_issue_parser(issue), expected);
    }
}
