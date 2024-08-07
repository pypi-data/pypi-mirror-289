CREATE TABLE gaiadr3_astrophysical_parameters (
    solution_id bigint,
    source_id bigint,
    classprob_dsc_combmod_quasar real,
    classprob_dsc_combmod_galaxy real,
    classprob_dsc_combmod_star real,
    classprob_dsc_combmod_whitedwarf real,
    classprob_dsc_combmod_binarystar real,
    classprob_dsc_specmod_quasar real, 
    classprob_dsc_specmod_galaxy real,
    classprob_dsc_specmod_star real,
    classprob_dsc_specmod_whitedwarf real,
    classprob_dsc_specmod_binarystar real,
    classprob_dsc_allosmod_quasar real,
    classprob_dsc_allosmod_galaxy real,
    classprob_dsc_allosmod_star real,
    teff_gspphot real,
    teff_gspphot_lower real,
    teff_gspphot_upper real,
    logg_gspphot real,
    logg_gspphot_lower real,
    logg_gspphot_upper real,
    mh_gspphot real,
    mh_gspphot_lower real,
    mh_gspphot_upper real,
    distance_gspphot real,
    distance_gspphot_lower real,
    distance_gspphot_upper real,
    azero_gspphot real,
    azero_gspphot_lower real,
    azero_gspphot_upper real,
    ag_gspphot real,
    ag_gspphot_lower real,
    ag_gspphot_upper real,
    abp_gspphot real,
    abp_gspphot_lower real,
    abp_gspphot_upper real,
    arp_gspphot real,
    arp_gspphot_lower real,
    arp_gspphot_upper real,
    ebpminrp_gspphot real,
    ebpminrp_gspphot_lower real,
    ebpminrp_gspphot_upper real,
    mg_gspphot real,
    mg_gspphot_lower real,
    mg_gspphot_upper real,
    radius_gspphot real,
    radius_gspphot_lower real,
    radius_gspphot_upper real,
    logposterior_gspphot real,
    mcmcaccept_gspphot real,
    libname_gspphot varchar,
    teff_gspspec real,
    teff_gspspec_lower real,
    teff_gspspec_upper real,
    logg_gspspec real,
    logg_gspspec_lower real,
    logg_gspspec_upper real,
    mh_gspspec real,
    mh_gspspec_lower real,
    mh_gspspec_upper real,
    alphafe_gspspec real,
    alphafe_gspspec_lower real,
    alphafe_gspspec_upper real,
    fem_gspspec real,
    fem_gspspec_lower real,
    fem_gspspec_upper real,
    fem_gspspec_nlines int,
    fem_gspspec_linescatter real,
    sife_gspspec real,
    sife_gspspec_lower real,
    sife_gspspec_upper real,
    sife_gspspec_nlines int,
    sife_gspspec_linescatter real,
    cafe_gspspec real,
    cafe_gspspec_lower real,
    cafe_gspspec_upper real,
    cafe_gspspec_nlines int,
    cafe_gspspec_linescatter real,
    tife_gspspec real,
    tife_gspspec_lower real,
    tife_gspspec_upper real,
    tife_gspspec_nlines int,
    tife_gspspec_linescatter real,
    mgfe_gspspec real,
    mgfe_gspspec_lower real,
    mgfe_gspspec_upper real,
    mgfe_gspspec_nlines int,
    mgfe_gspspec_linescatter real,
    ndfe_gspspec real,
    ndfe_gspspec_lower real,
    ndfe_gspspec_upper real,
    ndfe_gspspec_nlines int,
    ndfe_gspspec_linescatter real,
    feiim_gspspec real,
    feiim_gspspec_lower real,
    feiim_gspspec_upper real,
    feiim_gspspec_nlines int,
    feiim_gspspec_linescatter real,
    sfe_gspspec real,
    sfe_gspspec_lower real,
    sfe_gspspec_upper real,
    sfe_gspspec_nlines int,
    sfe_gspspec_linescatter real,
    zrfe_gspspec real,
    zrfe_gspspec_lower real,
    zrfe_gspspec_upper real,
    zrfe_gspspec_nlines int,
    zrfe_gspspec_linescatter real,
    nfe_gspspec real,
    nfe_gspspec_lower real,
    nfe_gspspec_upper real,
    nfe_gspspec_nlines int,
    nfe_gspspec_linescatter real,
    crfe_gspspec real,
    crfe_gspspec_lower real,
    crfe_gspspec_upper real,
    crfe_gspspec_nlines int,
    crfe_gspspec_linescatter real,
    cefe_gspspec real,
    cefe_gspspec_lower real,
    cefe_gspspec_upper real,
    cefe_gspspec_nlines int,
    cefe_gspspec_linescatter real,
    nife_gspspec real,
    nife_gspspec_lower real,
    nife_gspspec_upper real,
    nife_gspspec_nlines int,
    nife_gspspec_linescatter real,
    cn0ew_gspspec real,
    cn0ew_gspspec_uncertainty real,
    cn0_gspspec_centralline real,
    cn0_gspspec_width real,
    dib_gspspec_lambda real,
    dib_gspspec_lambda_uncertainty real,
    dibew_gspspec real,
    dibew_gspspec_uncertainty real,
    dibewnoise_gspspec_uncertainty real,
    dibp0_gspspec real,
    dibp2_gspspec real,
    dibp2_gspspec_uncertainty real,
    dibqf_gspspec real,
    flags_gspspec varchar,
    logchisq_gspspec real,
    ew_espels_halpha real,
    ew_espels_halpha_uncertainty real,
    ew_espels_halpha_flag varchar,
    ew_espels_halpha_model real,
    classlabel_espels varchar,
    classlabel_espels_flag varchar,
    classprob_espels_wcstar real,
    classprob_espels_wnstar real,
    classprob_espels_bestar real,
    classprob_espels_ttauristar real,
    classprob_espels_herbigstar real,
    classprob_espels_dmestar real,
    classprob_espels_pne real,
    azero_esphs real,
    azero_esphs_uncertainty real,
    ag_esphs real,
    ag_esphs_uncertainty real,
    ebpminrp_esphs real,
    ebpminrp_esphs_uncertainty real,
    teff_esphs real,
    teff_esphs_uncertainty real,
    logg_esphs real,
    logg_esphs_uncertainty real,
    vsini_esphs real,
    vsini_esphs_uncertainty real,
    flags_esphs varchar,
    spectraltype_esphs varchar,
    activityindex_espcs real,
    activityindex_espcs_uncertainty real,
    activityindex_espcs_input varchar,
    teff_espucd real,
    teff_espucd_uncertainty real,
    flags_espucd varchar,
    radius_flame real,
    radius_flame_lower real,
    radius_flame_upper real,
    lum_flame real,
    lum_flame_lower real,
    lum_flame_upper real,
    mass_flame real,
    mass_flame_lower real,
    mass_flame_upper real,
    age_flame real,
    age_flame_lower real,
    age_flame_upper real,
    flags_flame varchar,
    evolstage_flame int,
    gravredshift_flame real,
    gravredshift_flame_lower real,
    gravredshift_flame_upper real,
    bc_flame real,
    mh_msc real,
    mh_msc_upper real,
    mh_msc_lower real,
    azero_msc real,
    azero_msc_upper real,
    azero_msc_lower real,
    distance_msc real,
    distance_msc_upper real,
    distance_msc_lower real,
    teff_msc1 real,
    teff_msc1_upper real,
    teff_msc1_lower real,
    teff_msc2 real,
    teff_msc2_upper real,
    teff_msc2_lower real,
    logg_msc1 real,
    logg_msc1_upper real,
    logg_msc1_lower real,
    logg_msc2 real,
    logg_msc2_upper real,
    logg_msc2_lower real,
    ag_msc real,
    ag_msc_upper real,
    ag_msc_lower real,
    logposterior_msc real,
    mcmcaccept_msc real,
    mcmcdrift_msc real,
    flags_msc varchar,
    neuron_oa_id bigint,
    neuron_oa_dist real,
    neuron_oa_dist_percentile_rank int,
    flags_oa varchar,
    PRIMARY KEY (source_id)
);
