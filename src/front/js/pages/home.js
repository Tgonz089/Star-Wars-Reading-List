import React, { useContext } from "react";
import { Context } from "../store/appContext";
import { Card } from "../component/card.js";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <div className="container">
        <div className="charctersRow">
          <Card />
        </div>
        &nbsp;
        <div className="planets">
          <div className="planetsRow">
            <Card />
          </div>
        </div>
        &nbsp;
        <div className="vehicles">
          <div className="vehiclesRow">
            <Card />
          </div>
        </div>
      </div>
    </>
  );
};
