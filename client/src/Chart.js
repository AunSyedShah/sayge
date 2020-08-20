import React, {useEffect} from 'react'
import {bb, bar, area, zoom} from "billboard.js"
import "billboard.js/dist/billboard.css"
import "billboard.js/dist/theme/insight.css"

export default ({ data }) => {
  useEffect(() => {
    bb.generate({
      bindto: "#last_costs",
      data: {
        columns: [
          ['Food Variance', ...data.map(item => item.food_variance)],
          ['Labor Variance', ...data.map(item => item.labor_variance)],
        ],
        type: area()
      },
      zoom: {
        enabled: zoom()
      }
    })

    bb.generate({
      bindto: "#bad_orders",
      data: {
        x: 'x',
        columns: [
          ["x", ...data.map(item => item.store)],
          ["Bad Orders", ...data.map(item => item.bad_orders )],
        ],
        type: bar(),
        colors: {
          'Bad Orders': "#4562F6",
        },
      },
      axis: {
        x: {
          type: "category",
        }
      },
      zoom: {
        enabled: zoom()
      }
    })

    bb.generate({
      bindto: "#chart1",
      data: {
        columns: [
          ["Actual Food", ...data.map(item => item.actual_food)],
          ["Food Variance", ...data.map(item => item.food_variance)],
        ],
        type: bar(),
        colors: {
          'Actual Food': "#4562F6",
        },
      },
      zoom: {
        enabled: zoom()
      }
    })

    bb.generate({
      bindto: "#chart2",
      data: {
        columns: [
          ['Actual Food', ...data.map(item => item.actual_food)],
          ['Food Variance', ...data.map(item => item.food_variance)],
        ],
        groups: [
          ['Actual Food', 'Food Variance'],
        ],
        type: bar(),
        colors: {
          'Actual Food': "#4562F6",
          'Food Variance': "#FF4141",
        },
      },
      bar: {
        width: {
          max: 10,
        }
      },
      zoom: {
        enabled: zoom()
      }
    })
  }, [data])

  return (
    <>
    <div id="last_costs">Last Costs</div>
    <div id="bad_orders">Bad Orders</div>
    <div id="chart1">Chart</div>
    <div id="chart2">Chart</div>
    <div id="chart3">Chart</div>
    </>
  )
}
