use clap::Subcommand;

use crate::shell_utils::shell_out;

#[derive(Subcommand)]
pub enum Commands {
    /// Add a new item without querying the issue provider
    RapidAdd { name: String },
    /// Mark a change as ready, based on the config
    Ready,
}

pub fn ready() -> Result<(), std::io::Error> {
    shell_out("gh", &["pr", "merge"])
}

pub fn rapid_add(name: &String) -> Result<(), std::io::Error> {
    let migrate_changes = true; // Assume this is set somewhere
    let default_branch = "main"; // Assume this is set somewhere

    let needs_migration = migrate_changes && !repo_is_clean()?;

    if needs_migration {
        shell_out(
            "git",
            &[
                "stash",
                "save",
                "--include-untracked",
                "--no-track",
                &format!("origin/{}", &default_branch),
            ],
        )?;
    }

    shell_out("git", &["fetch", "origin"])?;
    shell_out("git", &["checkout", "-b", &branch_title(name)])?;

    if needs_migration {
        shell_out("git", &["stash", "pop"])?;
    }

    shell_out(
        "git",
        &["commit", "--allow-empty", "-m", &branch_title(name)],
    )?;

    shell_out("git", &["push"])?;

    Ok(())
}

fn branch_title(issue: &str) -> String {
    return format!("feature/{}", issue);
}

use std::process::Command;

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
