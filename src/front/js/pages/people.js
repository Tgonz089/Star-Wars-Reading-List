import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";
import { Context } from "../store/appContext";
import { Cards } from "../component/card.js";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import { Card } from "react-bootstrap";
import Button from "react-bootstrap/Button";


export const People = () => {
	//const { store, actions } = useContext(Context);

	return (
		<div className="text-center mt-5">
			<h1>People</h1>
		</div>
	);
};