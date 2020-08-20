import React from 'react'
import List from '@material-ui/core/List'
import ListItem from '@material-ui/core/ListItem'
import ListItemIcon from '@material-ui/core/ListItemIcon'
import ListItemText from '@material-ui/core/ListItemText'
import HomeWorkIcon from '@material-ui/icons/HomeWork'
import Brightness4Icon from '@material-ui/icons/Brightness4'
import { Link } from "react-router-dom"
import ThemeSwitcher from './ThemeSwitcher'

export default () => {
  return (
    <>
    <List>
      <ListItem button component={Link} to="/">
        <ListItemIcon>
          <HomeWorkIcon />
        </ListItemIcon>
        <ListItemText primary="Home" />
      </ListItem>
      <ListItem button component={Link} to="/theme">
        <ListItemIcon>
          <Brightness4Icon />
        </ListItemIcon>
        <ListItemText primary="Theme" />
      </ListItem>
    </List>
    <ThemeSwitcher />
    </>
  )
}
