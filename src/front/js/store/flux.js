const getState = ({ getStore, getActions, setStore }) => {
  return {
    store: {
      message: null,
      demo: [
        {
          title: "FIRST",
          background: "white",
          initial: "white",
        },
        {
          title: "SECOND",
          background: "white",
          initial: "white",
        },
      ],
      people: [],
      planets: [],
      vehicles: [],
      favorites: [],
    },
    actions: {
      // Use getActions to call a function within a fuction
      exampleFunction: () => {
        getActions().changeColor(0, "green");
      },

      getMessage: async () => {
        try {
          // fetching data from the backend
          const resp = await fetch(
            process.env.BACKEND_URL + "https://swapi.dev/api/"
          );
          const data = await resp.json();
          setStore({ message: data.message });
          // don't forget to return something, that is how the async resolves
          return data;
        } catch (error) {
          console.log("Error loading message from backend", error);
        }
      },
      changeColor: (index, color) => {
        //get the store
        const store = getStore();

        //we have to loop the entire demo array to look for the respective index
        //and change its color
        const demo = store.demo.map((elm, i) => {
          if (i === index) elm.background = color;
          return elm;
        });

        //reset the global store
        setStore({ demo: demo });
      },
      getPeople: (data) => {
        const store = getStore();
        const endpoint = process.env.BACKEND_URL + "/api/person";
        const config = {
          method: "GET",
        };
        fetch(endpoint, config)
          .then((res) => res.json())
          .then((data) => setStore({ people: data.all_characters }))
          .catch((err) => err);
      },
      getPlanets: (data) => {
        const store = getStore();
        const endpoint = process.env.BACKEND_URL + "/api/planet/";
        const config = {
          method: "GET",
        };
        fetch(endpoint, config)
          .then((res) => res.json())
          .then((data) => setStore({ planets: data.all_planets }))
          .catch((err) => err);
      },
      getVehicles: (data) => {
        const store = getStore();
        const endpoint = process.env.BACKEND_URL + "/api/vehicle/";
        const config = {
          method: "GET",
        };
        fetch(endpoint, config)
          .then((res) => res.json())
          .then((data) => setStore({ vehicles: data.all_vehicles }))
          .catch((err) => err);
      },
      setFavorites: (favorite) => {
        const store = getStore();
        setStore({ favorites: [...store.favorites, favorite] });
      },
      deleteFavorites: (favorite) => {
        const store = getStore();
        const del = store.favorites.filter((item) => item != favorite);
        setStore({ favorites: del });
      },
    },
  };
};

export default getState;
