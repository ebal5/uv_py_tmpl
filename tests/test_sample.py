"""Tests for the sample module."""

from your_package_name.sample import Person, Team, build_team


def test_person_initialization() -> None:
    """Test that Person objects are initialized correctly."""
    person = Person("Test Person", 30, "test@example.com", ["Python"])
    
    assert person.name == "Test Person"
    assert person.age == 30
    assert person.email == "test@example.com"
    assert person.skills == ["Python"]


def test_person_default_skills() -> None:
    """Test that Person objects have empty skills list by default."""
    person = Person("Test Person", 30)
    
    assert person.skills == []


def test_add_skill() -> None:
    """Test that skills can be added to a Person."""
    person = Person("Test Person", 30)
    person.add_skill("Python")
    
    assert "Python" in person.skills
    assert len(person.skills) == 1
    
    # Adding the same skill twice should not duplicate it
    person.add_skill("Python")
    assert len(person.skills) == 1


def test_team_initialization() -> None:
    """Test that Team objects are initialized correctly."""
    team = Team("Test Team")
    
    assert team.name == "Test Team"
    assert team.members == {}


def test_add_member() -> None:
    """Test that members can be added to a Team."""
    team = Team("Test Team")
    person = Person("Test Person", 30)
    
    team.add_member(person)
    assert "Test Person" in team.members
    assert team.members["Test Person"] == person


def test_list_skills() -> None:
    """Test that Team can list skills of all members."""
    alice = Person("Alice", 30, skills=["Python"])
    bob = Person("Bob", 25, skills=["JavaScript"])
    
    team = Team("Test Team")
    team.add_member(alice)
    team.add_member(bob)
    
    skills = team.list_skills()
    assert skills == {"Alice": ["Python"], "Bob": ["JavaScript"]}


def test_build_team() -> None:
    """Test that a team can be built with multiple members."""
    alice = Person("Alice", 30, skills=["Python"])
    bob = Person("Bob", 25, skills=["JavaScript"])
    
    team = build_team("Test Team", [alice, bob])
    
    assert team.name == "Test Team"
    assert len(team.members) == 2
    assert "Alice" in team.members
    assert "Bob" in team.members