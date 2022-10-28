import React, { useState, useEffect, useContext } from "react";
import ReactDOM from "react-dom";
import { Context } from "../store/appContext";
import Button from "react-bootstrap/Button";

export const HeartButton = (props) => {
  const { store, actions } = useContext(Context);

  return (
    <Button className="ButtonFav" onClick={() => actions.setFavorites(props.name)}>
      <i className={"far fa-heart Heart"} />
    </Button>
  );
};
