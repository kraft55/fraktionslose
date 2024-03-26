SELECT nachname, vorname, 
SUM(CASE WHEN wie_spd = True THEN 1 ELSE 0 END) AS wie_spd_count,
SUM(CASE WHEN wie_cducsu = True THEN 1 ELSE 0 END) AS wie_cducsu_count,
SUM(CASE WHEN wie_gruene = True THEN 1 ELSE 0 END) AS wie_gruene_count,
SUM(CASE WHEN wie_fdp = True THEN 1 ELSE 0 END) AS wie_fdp_count,
SUM(CASE WHEN wie_afd = True THEN 1 ELSE 0 END) AS wie_afd_count,
SUM(CASE WHEN wie_linke = True THEN 1 ELSE 0 END) AS wie_linke_count,
COUNT(stimme) AS abgegebene_stimmen_count

FROM fraktionslose
GROUP BY nachname, vorname
ORDER BY abgegebene_stimmen_count DESC, nachname ASC, vorname ASC;