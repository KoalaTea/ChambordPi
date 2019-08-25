import React from "react";

interface Drink {
  id: number;
}

interface MenuProps {
  drinks?: Drink;
}

const Menu: React.FC<MenuProps> = ({ drinks = { id: 1 } }) => {
  return (
    <div className="Menu">
      <p>Menu</p>
      <p>{drinks.id}</p>
    </div>
  );
};

export default Menu;
