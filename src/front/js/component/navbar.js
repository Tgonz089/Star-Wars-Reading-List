import React from "react";
import { Link } from "react-router-dom";
import { FavortitesButton } from "./favorites.js";
//https://freepngimg.com/download/star_wars/23290-8-star-wars-logo-file.png
export const Navbar = () => {
  return (
    <nav className="navbar navbar-light bg-light">
      <div className="container">
        <Link to="/">
            <img
              className="StarWarsLogo"
              style={{ width: "5%" }}
              src="https://freepngimg.com/download/star_wars/23290-8-star-wars-logo-file.png"
            />
        </Link>
        <div className="ml-auto">
          <FavortitesButton />
        </div>
      </div>
    </nav>
  );
};
