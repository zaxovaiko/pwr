import * as React from "react"
import { Link } from "gatsby"

const Header = () => (
  <nav className="navbar navbar-dark bg-primary">
    <div className="container">
      <Link to="/" className="navbar-brand">
        Blog Lab_8
      </Link>
    </div>
  </nav>
)

export default Header
