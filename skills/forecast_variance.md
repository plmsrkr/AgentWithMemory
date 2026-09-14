# Forecast Variance Skill

When comparing actual performance with forecast:

1. Retrieve actual value.

2. Retrieve forecast value.

3. Calculate:

   absolute_variance = actual - forecast

   variance_pct = (actual - forecast) / forecast * 100

4. Determine whether actual:
   - exceeded forecast
   - matched forecast
   - missed forecast

5. If asked why the variance occurred, request supporting business
   data rather than inventing causes.