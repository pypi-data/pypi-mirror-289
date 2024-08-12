use crate::{issue::Issue, shell_utils::shell_out};

pub enum MergeMethod {
    Merge,
    Rebase,
    Squash,
}

pub trait Forge {
    fn setup(&self);
    fn begin(&self, issue: Issue, start_as_draft: bool) -> Result<(), std::io::Error>;
    fn ready(&self, automerge: bool, merge_method: MergeMethod, mark_as_ready: bool);
}

// Implement for GitHub
pub struct GitHub {}

impl Forge for GitHub {
    fn setup(&self) {
        let _ = shell_out("gh", &[""]);
    }

    fn begin(
        &self,
        issue: Issue,
        start_as_draft: bool,
        // TODO: title_formatter: impl Fn(&Issue) -> String,
    ) -> Result<(), std::io::Error> {
        let title = issue.title.content;
        let mut args = vec!["pr", "create", "--title", &title, "--body", ""];

        if start_as_draft {
            args.push("--draft");
        }
        shell_out("gh", &args)
    }

    fn ready(&self, automerge: bool, merge_method: MergeMethod, mark_as_ready: bool) {
        if mark_as_ready {
            let _ = shell_out("gh", &["pr", "ready"]);
        }

        let mut merge_cmd = vec!["pr", "merge"];
        if automerge {
            merge_cmd.push("--auto");
        }
        match merge_method {
            MergeMethod::Merge => merge_cmd.push("--merge"),
            MergeMethod::Rebase => merge_cmd.push("--rebase"),
            MergeMethod::Squash => merge_cmd.push("--squash"),
        }

        let _ = shell_out("gh", &merge_cmd);
    }
}
