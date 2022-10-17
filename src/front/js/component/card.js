import React, { useState, useEffect, useContext } from "react";
import Card from "react-bootstrap/Card";
import PropTypes from "prop-types";
import { Context } from "../store/appContext";

export const Cards = (props) => {
  const { store, actions } = useContext(Context);

  return (
    <>
      <Card style={{ width: "18rem" }}>
        <Card.Img variant="top" src="https://fakeimg.pl/400x200/" />
        <Card.Body>
          <Card.Title>{props.Title}</Card.Title>
          <Card.Text>{props.children}</Card.Text>
        </Card.Body>
      </Card>
    </>
  );
};

Cards.propTypes = {
  title: PropTypes.string,
  children: PropTypes.string,
};
