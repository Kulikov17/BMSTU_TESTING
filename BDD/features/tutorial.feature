Feature: Create

  Scenario Outline: Create users
     Given I put user <login> <name> <password> parameters
     When I make create request
     Then I should be user with <login> <name>

    Examples:
        | login         | name            |  password   |
        | dkul          | dima            |  12         |
        | dkul1         | dima1           |  13         |

  Scenario Outline: Create subject
     Given I put subject <ownerId> <private> <name> <description> parameters
     When I make create subject request
     Then I should be subject with <ownerId> <private> <name> <description>

    Examples:
        | ownerId         | private            |  name   | description |
        | 1          | True            |  OOP         | like |
        | 2         | False           |  Testing         | like |