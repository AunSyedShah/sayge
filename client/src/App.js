import React from 'react'
import { RecoilRoot } from 'recoil'
import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom"
import Home from './Home'
import './App.css'
import ThemeOverview from './ThemeOverview'
import { ThemeProvider } from './theme'


const App = () => {
  return (
    <RecoilRoot>
      <ThemeProvider>
        <Router>
          <div>
            <Switch>
              <Route path="/theme">
                <ThemeOverview />
              </Route>
              <Route path="/">
                <Home />
              </Route>
            </Switch>
          </div>
        </Router>
      </ThemeProvider>
    </RecoilRoot>
  )
}

export default App
