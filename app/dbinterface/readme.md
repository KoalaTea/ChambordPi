Orders
{
    _id: objectID("..."),
    user: "username",
    stats: "queued|complete|ready",
    cost: int(cost),
    name: "Drink Name",
    recipe: DrinkObject,
    image: "image file.png",
    instructions: "user input",
    type: "beer|mixed|shot",
    timeOrdered: 1488908888
}

Drinks
{
    _id: objectID("..."),
    available: true|false,
    cost: int(cost),
    name: "Drink Name",
    times_ordered: int(times_ordered),
    recipe: [
        {
            flavor: "flavor",
            type: "Rum|Vodka|Liqueuer|...."
            amount: "how much"
        },
        {
            ...
        }
    ],
    image: "image file.png",
    type: "mixed|shot|beer",
    id: int(Do I Need This?)
}

Ingredients
{
    _id: objectID("...."),
    available: true|false,
    cost: int(cost), <---- Do I need costs? Custom drinks are the only place this makes sense. It's a static cost... Might remove

    bottles: int(number of bottles),
        Change to stock and measure
        amount different word? to not conflict with recipe

    stock: int(number of measure),
    measure: "Measure Word, bottles|bushels|fruits(for lemons/limes)"

    name: "name of ingredient",
    class: "mixer|alchohol",
    type: "rum|vodka|water|soda|...|jager"
    flavor: "null|coconut|lemon-lime|...."

    times_ordered: int(#ordered) <------------- is this removable? If so restructure it out

    TODO NEEDS WORK
        Restructure?
        what about non liquid mixers
}

PastOrders
{
}


Users
{
    _id: objectID("..."),
    username: "username",
    password: "hash",
    roles: [
        "role1",
        "role2"
    ],
    drinksOrdered: int(number of orders currently open),
    credits: int(credits)
}
