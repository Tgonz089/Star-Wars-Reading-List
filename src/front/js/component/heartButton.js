import React, { useState, useEffect, useContext } from "react";
import ReactDOM from "react-dom";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";
import PropTypes from "prop-types";

export const HeartButton = (props) => {
  const { store, actions } = useContext(Context);

  return (
    <button
      type="button"
      className="btn btn-outline-danger HeartBtn"
      onClick={() => actions.setFavorites(props.name)}
    >
      <i className="far fa-heart" />
    </button>
  );
};
