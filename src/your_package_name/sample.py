"""Sample module demonstrating typical Python patterns."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Person:
    """Class representing a person."""

    name: str
    age: int
    email: Optional[str] = None
    skills: List[str] = None

    def __post_init__(self) -> None:
        """Initialize default values for optional fields."""
        if self.skills is None:
            self.skills = []

    def add_skill(self, skill: str) -> None:
        """Add a new skill to the person.

        Args:
            skill: The skill to add
        """
        if skill not in self.skills:
            self.skills.append(skill)
            print(f"Added skill '{skill}' to {self.name}")


class Team:
    """A team of people working together."""

    def __init__(self, name: str) -> None:
        """Initialize a team with a name.

        Args:
            name: The team name
        """
        self.name = name
        self.members: Dict[str, Person] = {}

    def add_member(self, person: Person) -> None:
        """Add a person to the team.

        Args:
            person: The person to add
        """
        if person.name not in self.members:
            self.members[person.name] = person
            print(f"{person.name} was added to team {self.name}")
        else:
            print(f"{person.name} is already in team {self.name}")

    def list_skills(self) -> Dict[str, List[str]]:
        """List all skills of team members.

        Returns:
            A dictionary mapping each team member's name to their skills
        """
        return {name: person.skills for name, person in self.members.items()}


def build_team(team_name: str, members: List[Person]) -> Team:
    """Create a new team and add members to it.

    Args:
        team_name: The name of the team
        members: List of people to add to the team

    Returns:
        The newly created team
    """
    team = Team(team_name)
    for person in members:
        team.add_member(person)
    return team


def main() -> None:
    """Run a demonstration of the Team and Person classes."""
    # Create some people
    alice = Person("Alice", 30, "alice@example.com", ["Python", "ML"])
    bob = Person("Bob", 25, "bob@example.com", ["JavaScript", "React"])
    charlie = Person("Charlie", 35)
    charlie.add_skill("Project Management")

    # Build a team
    dev_team = build_team("Development", [alice, bob, charlie])

    # Show team skills
    skills = dev_team.list_skills()
    print("\nTeam Skills:")
    for name, person_skills in skills.items():
        skill_list = ", ".join(person_skills) if person_skills else "No skills listed"
        print(f"- {name}: {skill_list}")


if __name__ == "__main__":
    main()