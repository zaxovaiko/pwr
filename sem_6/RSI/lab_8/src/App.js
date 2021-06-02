import { Switch, Route } from "react-router";
import CountryPage from "./pages/Country";
import Home from "./pages/Home";

function App() {
  return (
    <div className="container py-5">
      <Switch>
        <Route exact path="/countries/:id" component={CountryPage} />
        <Route component={Home} />
      </Switch>
    </div>
  );
}

export default App;
