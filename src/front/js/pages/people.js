import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import { Cards } from "../component/card.js";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import { Card } from "react-bootstrap";
import Button from "react-bootstrap/Button";

export const People = (props) => {
  const { store, actions } = useContext(Context);

  return (
    <>
	            {store.people.map((person, index) => {
            return (
              <Cards key={index+1}>
                <Card.Title>{person.name}</Card.Title>
                <Card.Text>Gender: {person.gender}</Card.Text>
                <Card.Text>Eye Color: {person.eye_color}</Card.Text>
                <Card.Text>Hair Color: {person.hair_color}</Card.Text>
              </Cards>
            );
          })}
          ;
    </>
  );
};
