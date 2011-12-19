# Auto generated configuration file
# using: 
# Revision: 1.303.2.7 
# Source: /cvs/CMSSW/CMSSW/Configuration/PyReleaseValidation/python/ConfigBuilder.py,v 
# with command line options: promptReco --step RAW2DIGI,RECO --conditions GR_P_V22::All --eventcontent AOD --no_exec --data --filein file:/data/santanas/Data/HT-Run2011B-RAW-v1-180072-4E95B756-EE00-E111-8FB6-485B3962633D-20399events.root --fileout HT-Run2011B-AOD-test.root --python_filename=promptReco_RAW2DIGI_RECO_AOD.py
import FWCore.ParameterSet.Config as cms

process = cms.Process('RECO')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_0.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_1.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_10.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_11.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_12.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_13.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_14.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_15.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_16.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_17.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_18.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_19.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_2.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_20.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_21.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_22.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_23.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_24.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_25.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_26.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_27.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_3.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_4.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_5.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_6.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_7.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_8.root',
    'root://eoscms//eos/cms/store/cmst3/user/santanas/DiJets/2011DataPhysicsDSTplusRAW/PhysicsDSTplusRAW-DATA-2011B-HT-180250_20111219/HT__Run2011B-v1-180250__RAWplusPhysicsDST_9.root'
    #'file:/data/santanas/Releases/CMSSW_4_2_9_HLT3_hltpatch3/src/RunHLT_KeepRAW/outputPhysicsDST-RAW_180072_1kevents.root'
    )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.303.2.7 $'),
    annotation = cms.untracked.string('promptReco nevts:-1'),
    name = cms.untracked.string('PyReleaseValidation')
)

# Output definition

process.AODoutput = cms.OutputModule("PoolOutputModule",
    eventAutoFlushCompressedSize = cms.untracked.int32(15728640),
    outputCommands = process.AODEventContent.outputCommands,
    fileName = cms.untracked.string('HT__Run2011B-v1-180250__AODplusPhysicsDST.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('')
    )
)

process.AODoutput.outputCommands.extend(
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
process.GlobalTag.globaltag = 'GR_P_V22::All'

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODoutput_step = cms.EndPath(process.AODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.endjob_step,process.AODoutput_step)
