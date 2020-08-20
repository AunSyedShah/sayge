import React, { useState } from 'react'
import CssBaseline from '@material-ui/core/CssBaseline'
import clsx from 'clsx'
import { makeStyles } from '@material-ui/core/styles'
import Toolbar from './Toolbar'
import Drawer from '@material-ui/core/Drawer'
import IconButton from '@material-ui/core/IconButton'
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft'
import Divider from '@material-ui/core/Divider'
import Navigation from './Navigation'
import { drawerWidth } from './constants'
import Logo from './assets/logo.svg'
import RecoilData from './RecoilData'

const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  logo: {
    width: 110,
    height: 25,
    float: 'right',
  },
  toolbarIcon: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: '0 8px',
    ...theme.mixins.toolbar,
  },
  drawerPaper: {
    position: 'relative',
    whiteSpace: 'nowrap',
    width: drawerWidth,
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  },
  drawerPaperClose: {
    overflowX: 'hidden',
    transition: theme.transitions.create('width', {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.leavingScreen,
    }),
    width: theme.spacing(7),
    [theme.breakpoints.up('sm')]: {
      width: theme.spacing(9),
    },
  },
  appBarSpacer: theme.mixins.toolbar,
  content: {
    flexGrow: 1,
    height: '100vh',
    overflow: 'auto',
  },
  container: {
    paddingTop: theme.spacing(4),
    paddingBottom: theme.spacing(4),
  },
  paper: {
    padding: theme.spacing(2),
    display: 'flex',
    overflow: 'auto',
    flexDirection: 'column',
  },
  fixedHeight: {
    height: 240,
  },
}))

export default ({ component: Component }) => {
  const classes = useStyles()
  const [open, setOpen] = useState(true)
  const handleDrawerOpen = () => {
    setOpen(true)
  }
  const handleDrawerClose = () => {
    setOpen(false)
  }

  return (
    <div className={classes.root}>
      <CssBaseline />
      <Toolbar openDrawer={handleDrawerOpen} drawerIsOpen={open}></Toolbar>
      <Drawer
        variant="permanent"
        open={open}
        classes={{
          paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
        }}
      >
        <div className={classes.toolbarIcon}>
          <img alt="Sayge AI" className={classes.logo} src={Logo} />
          <IconButton onClick={handleDrawerClose}>
            <ChevronLeftIcon />
          </IconButton>
        </div>
        <Divider />
        <Navigation />
      </Drawer>
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <RecoilData />
        {<Component />}
      </main>
    </div>
  )
}

