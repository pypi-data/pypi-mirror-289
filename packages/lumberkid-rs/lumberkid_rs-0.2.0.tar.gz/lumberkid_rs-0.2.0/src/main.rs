use clap::Parser;
use commands::{rapid_add, ready, Commands};
mod commands;
mod shell_utils;

#[derive(Parser)]
#[command(version, about, long_about = None)]
struct LumberkidCLI {
    /// Turn debugging information on
    #[arg(short, long, action = clap::ArgAction::Count)]
    debug: u8,

    #[command(subcommand)]
    command: Option<Commands>,
}

fn main() {
    let cli = LumberkidCLI::parse();

    // You can check for the existence of subcommands, and if found use their
    // matches just as you would the top level cmd
    match &cli.command {
        Some(Commands::RapidAdd { name }) => rapid_add(name).unwrap(),
        Some(Commands::Ready) => ready().unwrap(),
        None => {}
    }
}
