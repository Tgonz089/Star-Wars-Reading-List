import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Cards } from "../component/card.js";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <div className="container">
        <h1>Characters</h1>
        <div className="charctersRow">
          <Cards />
          <Cards />
          <Cards />
          <Cards />
          <Cards/>
          <Cards />
        </div>
        &nbsp;
        <div className="planets">
          <h1>Planets</h1>
          <div className="planetsRow">
            <Cards />
            <Cards />
            <Cards />
            <Cards />
            <Cards />
            <Cards />
          </div>
        </div>
        &nbsp;
        <div className="vehicles">
          <h1>Vehicles</h1>
          <div className="vehiclesRow">
            <Cards />
            <Cards />
            <Cards />
            <Cards />
            <Cards />
            <Cards />
          </div>
        </div>
      </div>
    </>
  );
};
