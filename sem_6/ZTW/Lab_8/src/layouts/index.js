import React from "react"
import "bootstrap/dist/css/bootstrap.min.css"
import { Helmet } from "react-helmet"
import Header from "../components/header"

export default function Layout({ children }) {
  return (
    <>
      <Header />
      <Helmet
        title="Static Blog"
        meta={[
          { name: "description", content: "Simple Blog for Lab_8" },
          { name: "keywords", content: "pwr, blog" },
        ]}
      />
      <div className="container mt-3">{children}</div>
    </>
  )
}
