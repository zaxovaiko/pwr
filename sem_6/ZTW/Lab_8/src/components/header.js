import * as React from "react"
import { Link } from "gatsby"

const Header = () => (
  <nav class="navbar navbar-dark bg-primary">
    <div class="container">
      <Link to="/" className="navbar-brand">
        Blog Lab_8
      </Link>
      <form class="d-flex">
        <div class="input-group">
          <input
            class="form-control"
            type="search"
            placeholder="Search"
          />
          <button class="btn btn-dark">
            Search
          </button>
        </div>
      </form>
    </div>
  </nav>
)

export default Header
