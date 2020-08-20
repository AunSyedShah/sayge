import React from 'react'
import { makeStyles } from '@material-ui/core/styles'
import Container from '@material-ui/core/Container'
import Grid from '@material-ui/core/Grid'
import Paper from '@material-ui/core/Paper'
import Admin from './Admin'
import Chart from './Chart'
import SalesSection from './SalesSection'
import { useCompanySnapshotData } from './company-snapshot'
import ActiveDate from './ActiveDate'

const useStyles = makeStyles((theme) => ({
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
    height: 350,
  },
}))

const Home = () => {
  const { data, error, isLoading } = useCompanySnapshotData()
  const classes = useStyles()

  if (isLoading) return <div>loading...</div>
  if (error) return <div>failed to load: {error}</div>

  return (
    <Container maxWidth="lg" className={classes.container}>
      <Grid container spacing={3}>

        <ActiveDate />

        <SalesSection data={data} />

        <Paper style={{ width: '100%', margin: '1rem 0 0 0' }}>
          <Chart data={data}></Chart>
        </Paper>

      </Grid>
    </Container>
  )
}

export default () => {
  return (
    <Admin component={Home} />
  )
}
