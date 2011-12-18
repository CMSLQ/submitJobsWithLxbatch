# Auto generated configuration file
# using: 
# Revision: 1.303.2.7 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: Reco --step RAW2DIGI,RECO --conditions START42_V14B::All --eventcontent AODSIM --no_exec --mc --filein root://eoscms//eos/cms/store/cmst3/user/mgouzevi/CMG/QstarToJJ_M-500_TuneD6T_7TeV_pythia6/Fall11-PU_S6_START42_V14B-v1/GEN-RAW/Francesco/E07762FA-28EA-E011-8D2A-E41F13181A48.root --fileout MC_AODSIM_Test.root --python_filename=Reco_RAW2DIGI_RECO_AOD.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_10_1_pnw.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_11_1_Vhj.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_12_1_sjr.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_13_1_k2v.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_14_1_mcl.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_15_1_VC9.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_16_1_lGp.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_17_1_cqw.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_18_1_SSW.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_19_1_mjv.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_1_1_CfA.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_20_1_745.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_21_1_pmJ.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_22_1_cjp.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_23_1_I49.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_24_1_dFU.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_25_1_QVO.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_26_1_o94.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_27_1_ahz.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_28_1_Xie.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_29_1_qAp.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_2_1_nUu.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_30_1_UjK.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_31_1_QYU.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_32_1_m3R.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_33_1_FlM.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_34_1_knx.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_35_1_28g.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_36_1_MCf.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_37_1_fjJ.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_38_1_mgw.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_39_1_ArD.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_3_1_LN6.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_40_1_gKY.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_41_1_mP2.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_42_1_WoA.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_43_1_0HM.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_44_1_yRt.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_45_1_B9L.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_46_1_wzu.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_47_1_UKU.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_48_1_Ev8.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_49_1_SMI.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_4_1_uQq.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_50_1_IqZ.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_5_1_Neh.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_6_1_7Zq.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_7_1_KFy.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_8_1_lKE.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_9_1_IyQ.root'
    #'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_145650/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_10_1_pnw.root'
    #'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/Fall11MCPhysicsDSTGenInfoRAW/PhysicsDSTGenInfoRAW-MC-Fall11-QstarToJJ_20111218_105652/QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__GEN-RAW_9_1_ATW.root'
    #'root://eoscms//eos/cms/store/cmst3/user/mgouzevi/CMG/QstarToJJ_M-500_TuneD6T_7TeV_pythia6/Fall11-PU_S6_START42_V14B-v1/GEN-RAW/Francesco/E07762FA-28EA-E011-8D2A-E41F13181A48.root'
    )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    annotation = cms.untracked.string('Reco nevts:1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODSIMEventContent.outputCommands,
    fileName = cms.untracked.string('QstarToJJ_M-500_TuneD6T_7TeV_pythia6__Fall11-PU_S6_START42_V14B-v1__AODSIM_PhysicsDST.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

process.AODSIMoutput.outputCommands.extend(
    cms.untracked.vstring(
    'keep *_hltAntiKT5CaloJetsSelected_*_*',
    'keep *_hltAntiKT5PFJets_*_*',
    'keep *_hltCaloJetCorrectedSelected_*_*',
    'keep *_hltMuons_*_*',
    'keep *_hltPixelVertices_*_*',
    'keep edmTriggerResults_*_*_*'
    )
    )

# Additional output definition

# Other statements
process.GlobalTag.globaltag = 'START42_V14B::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)
