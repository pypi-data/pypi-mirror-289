#[derive(Debug)]
pub struct IssueTitle {
    pub prefix: Option<String>,
    pub content: String,
}

pub struct Issue {
    pub title: IssueTitle,
}

pub struct RemoteIssue {
    pub title: IssueTitle,
    pub entity_id: String,
    pub description: String,
}
