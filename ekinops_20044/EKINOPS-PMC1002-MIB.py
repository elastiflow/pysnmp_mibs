# SNMP MIB module (EKINOPS-PMC1002-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-PMC1002-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:46 2025
# On host e-ws1-mac.muc.elastiflow.net platform Darwin version 24.3.0 by user rob
# Using Python version 3.13.3 (main, Apr  8 2025, 13:54:08) [Clang 16.0.0 (clang-1600.0.26.6)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(EkiApiState,
 EkiMeasureType,
 EkiMode,
 EkiOnOff,
 EkiProtocol,
 EkiState,
 EkiSynchroMode,
 ekinops) = mibBuilder.importSymbols(
    "EKINOPS-MIB",
    "EkiApiState",
    "EkiMeasureType",
    "EkiMode",
    "EkiOnOff",
    "EkiProtocol",
    "EkiState",
    "EkiSynchroMode",
    "ekinops")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

modulepmc1002 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50)
)
if mibBuilder.loadTexts:
    modulepmc1002.setRevisions(
        ("2011-01-04 00:00",
         "2011-02-02 00:00",
         "2012-07-03 00:00",
         "2013-04-03 00:00",
         "2014-03-26 00:00",
         "2015-01-20 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pmc1002OtxMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("otx80mode", 1),
          ("otx60mode", 2),
          ("otxadjustmode", 4))
    )



class Pmc1002OtxGrid(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(50,
              100,
              200)
        )
    )
    namedValues = NamedValues(
        *(("otxgrid50", 50),
          ("otxgrid100", 100),
          ("otxgrid200", 200))
    )



class Pmc1002AdjustValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("otxadjustvalue0", 0),
          ("otxadjustvalue1", 1),
          ("otxadjustvalue2", 2),
          ("otxadjustvalue3", 3),
          ("otxadjustvalue4", 4),
          ("otxadjustvalue5", 5),
          ("otxadjustvalue6", 6),
          ("otxadjustvalue7", 7),
          ("otxadjustvalue8", 8),
          ("otxadjustvalue9", 9),
          ("otxadjustvalue10", 10))
    )



class Pmc1002OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pmc1002DccMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dccNo", 0),
          ("dcctermLine1", 1),
          ("dcctermLine2", 2),
          ("dcctermLines12", 3),
          ("dccmaster", 4),
          ("dccslaveLine12", 7))
    )



class Pmc1002Mode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modedual", 0),
          ("modeprotect", 1),
          ("moderegen", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pmc1002alarms_ObjectIdentity = ObjectIdentity
pmc1002alarms = _Pmc1002alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2)
)
_Pmc1002AlmOther_ObjectIdentity = ObjectIdentity
pmc1002AlmOther = _Pmc1002AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1)
)
_Pmc1002AlmOtherNurg_ObjectIdentity = ObjectIdentity
pmc1002AlmOtherNurg = _Pmc1002AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1)
)
_Pmc1002AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pmc1002AlmsynthAlm2 = _Pmc1002AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1, 2)
)
_Pmc1002AlmConfTableSave_Type = EkiOnOff
_Pmc1002AlmConfTableSave_Object = MibScalar
pmc1002AlmConfTableSave = _Pmc1002AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1, 2, 1),
    _Pmc1002AlmConfTableSave_Type()
)
pmc1002AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmConfTableSave.setStatus("current")
_Pmc1002AlmInvUpload_Type = EkiOnOff
_Pmc1002AlmInvUpload_Object = MibScalar
pmc1002AlmInvUpload = _Pmc1002AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1, 2, 2),
    _Pmc1002AlmInvUpload_Type()
)
pmc1002AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmInvUpload.setStatus("current")
_Pmc1002AlmConfTableLoad_Type = EkiOnOff
_Pmc1002AlmConfTableLoad_Object = MibScalar
pmc1002AlmConfTableLoad = _Pmc1002AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1, 2, 3),
    _Pmc1002AlmConfTableLoad_Type()
)
pmc1002AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmConfTableLoad.setStatus("current")
_Pmc1002AlmCorrelatOff_Type = EkiOnOff
_Pmc1002AlmCorrelatOff_Object = MibScalar
pmc1002AlmCorrelatOff = _Pmc1002AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1, 2, 4),
    _Pmc1002AlmCorrelatOff_Type()
)
pmc1002AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmCorrelatOff.setStatus("current")
_Pmc1002AlmMaintenanceOn_Type = EkiOnOff
_Pmc1002AlmMaintenanceOn_Object = MibScalar
pmc1002AlmMaintenanceOn = _Pmc1002AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 1, 2, 5),
    _Pmc1002AlmMaintenanceOn_Type()
)
pmc1002AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmMaintenanceOn.setStatus("current")
_Pmc1002AlmOtherUrg_ObjectIdentity = ObjectIdentity
pmc1002AlmOtherUrg = _Pmc1002AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2)
)
_Pmc1002AlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pmc1002AlmmodInitFailLevel2 = _Pmc1002AlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 194)
)
_Pmc1002AlmLedFail_Type = EkiOnOff
_Pmc1002AlmLedFail_Object = MibScalar
pmc1002AlmLedFail = _Pmc1002AlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 194, 1),
    _Pmc1002AlmLedFail_Type()
)
pmc1002AlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLedFail.setStatus("current")
_Pmc1002AlmNextColdBootForced_Type = EkiOnOff
_Pmc1002AlmNextColdBootForced_Object = MibScalar
pmc1002AlmNextColdBootForced = _Pmc1002AlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 194, 2),
    _Pmc1002AlmNextColdBootForced_Type()
)
pmc1002AlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmNextColdBootForced.setStatus("current")
_Pmc1002AlmBootUndone_Type = EkiOnOff
_Pmc1002AlmBootUndone_Object = MibScalar
pmc1002AlmBootUndone = _Pmc1002AlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 194, 3),
    _Pmc1002AlmBootUndone_Type()
)
pmc1002AlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmBootUndone.setStatus("current")
_Pmc1002AlmResetHwInitFail_Type = EkiOnOff
_Pmc1002AlmResetHwInitFail_Object = MibScalar
pmc1002AlmResetHwInitFail = _Pmc1002AlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 194, 4),
    _Pmc1002AlmResetHwInitFail_Type()
)
pmc1002AlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmResetHwInitFail.setStatus("current")
_Pmc1002AlmSwInitFail_Type = EkiOnOff
_Pmc1002AlmSwInitFail_Object = MibScalar
pmc1002AlmSwInitFail = _Pmc1002AlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 194, 5),
    _Pmc1002AlmSwInitFail_Type()
)
pmc1002AlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmSwInitFail.setStatus("current")
_Pmc1002AlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pmc1002AlmmodInitFailLevel3 = _Pmc1002AlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195)
)
_Pmc1002AlmGwIdentFail_Type = EkiOnOff
_Pmc1002AlmGwIdentFail_Object = MibScalar
pmc1002AlmGwIdentFail = _Pmc1002AlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 1),
    _Pmc1002AlmGwIdentFail_Type()
)
pmc1002AlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmGwIdentFail.setStatus("current")
_Pmc1002AlmObmTypeReadFail_Type = EkiOnOff
_Pmc1002AlmObmTypeReadFail_Object = MibScalar
pmc1002AlmObmTypeReadFail = _Pmc1002AlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 2),
    _Pmc1002AlmObmTypeReadFail_Type()
)
pmc1002AlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmObmTypeReadFail.setStatus("current")
_Pmc1002AlmInitModuleFail_Type = EkiOnOff
_Pmc1002AlmInitModuleFail_Object = MibScalar
pmc1002AlmInitModuleFail = _Pmc1002AlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 3),
    _Pmc1002AlmInitModuleFail_Type()
)
pmc1002AlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmInitModuleFail.setStatus("current")
_Pmc1002AlmXfp1InitFail_Type = EkiOnOff
_Pmc1002AlmXfp1InitFail_Object = MibScalar
pmc1002AlmXfp1InitFail = _Pmc1002AlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 5),
    _Pmc1002AlmXfp1InitFail_Type()
)
pmc1002AlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmXfp1InitFail.setStatus("current")
_Pmc1002AlmXfp2InitFail_Type = EkiOnOff
_Pmc1002AlmXfp2InitFail_Object = MibScalar
pmc1002AlmXfp2InitFail = _Pmc1002AlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 6),
    _Pmc1002AlmXfp2InitFail_Type()
)
pmc1002AlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmXfp2InitFail.setStatus("current")
_Pmc1002AlmLine1InitFail_Type = EkiOnOff
_Pmc1002AlmLine1InitFail_Object = MibScalar
pmc1002AlmLine1InitFail = _Pmc1002AlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 7),
    _Pmc1002AlmLine1InitFail_Type()
)
pmc1002AlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLine1InitFail.setStatus("current")
_Pmc1002AlmClient1InitFail_Type = EkiOnOff
_Pmc1002AlmClient1InitFail_Object = MibScalar
pmc1002AlmClient1InitFail = _Pmc1002AlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 2, 195, 9),
    _Pmc1002AlmClient1InitFail_Type()
)
pmc1002AlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClient1InitFail.setStatus("current")
_Pmc1002AlmOtherCrit_ObjectIdentity = ObjectIdentity
pmc1002AlmOtherCrit = _Pmc1002AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 3)
)
_Pmc1002AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pmc1002AlmsynthAlm0 = _Pmc1002AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 3, 0)
)
_Pmc1002AlmModGlobFail_Type = EkiOnOff
_Pmc1002AlmModGlobFail_Object = MibScalar
pmc1002AlmModGlobFail = _Pmc1002AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 3, 0, 9),
    _Pmc1002AlmModGlobFail_Type()
)
pmc1002AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmModGlobFail.setStatus("current")
_Pmc1002AlmDefFuseA_Type = EkiOnOff
_Pmc1002AlmDefFuseA_Object = MibScalar
pmc1002AlmDefFuseA = _Pmc1002AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 3, 0, 15),
    _Pmc1002AlmDefFuseA_Type()
)
pmc1002AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmDefFuseA.setStatus("current")
_Pmc1002AlmDefFuseB_Type = EkiOnOff
_Pmc1002AlmDefFuseB_Object = MibScalar
pmc1002AlmDefFuseB = _Pmc1002AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 1, 3, 0, 16),
    _Pmc1002AlmDefFuseB_Type()
)
pmc1002AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmDefFuseB.setStatus("current")
_Pmc1002AlmClient_ObjectIdentity = ObjectIdentity
pmc1002AlmClient = _Pmc1002AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2)
)
_Pmc1002AlmClientNurg_ObjectIdentity = ObjectIdentity
pmc1002AlmClientNurg = _Pmc1002AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1)
)
_Pmc1002AlmclientXfpWarningsTable_Object = MibTable
pmc1002AlmclientXfpWarningsTable = _Pmc1002AlmclientXfpWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpWarningsTable.setStatus("current")
_Pmc1002AlmclientXfpWarningsEntry_Object = MibTableRow
pmc1002AlmclientXfpWarningsEntry = _Pmc1002AlmclientXfpWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1)
)
pmc1002AlmclientXfpWarningsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmclientXfpWarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpWarningsEntry.setStatus("current")


class _Pmc1002AlmclientXfpWarningsIndex_Type(Integer32):
    """Custom type pmc1002AlmclientXfpWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmclientXfpWarningsIndex_Type.__name__ = "Integer32"
_Pmc1002AlmclientXfpWarningsIndex_Object = MibTableColumn
pmc1002AlmclientXfpWarningsIndex = _Pmc1002AlmclientXfpWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 1),
    _Pmc1002AlmclientXfpWarningsIndex_Type()
)
pmc1002AlmclientXfpWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpWarningsIndex.setStatus("current")
_Pmc1002AlmClientTxPowerLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientTxPowerLowWarningPortn_Object = MibTableColumn
pmc1002AlmClientTxPowerLowWarningPortn = _Pmc1002AlmClientTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 2),
    _Pmc1002AlmClientTxPowerLowWarningPortn_Type()
)
pmc1002AlmClientTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxPowerLowWarningPortn.setStatus("current")
_Pmc1002AlmClientTxPowerHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientTxPowerHighWarningPortn_Object = MibTableColumn
pmc1002AlmClientTxPowerHighWarningPortn = _Pmc1002AlmClientTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 3),
    _Pmc1002AlmClientTxPowerHighWarningPortn_Type()
)
pmc1002AlmClientTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxPowerHighWarningPortn.setStatus("current")
_Pmc1002AlmClientTxBiasLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientTxBiasLowWarningPortn_Object = MibTableColumn
pmc1002AlmClientTxBiasLowWarningPortn = _Pmc1002AlmClientTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 4),
    _Pmc1002AlmClientTxBiasLowWarningPortn_Type()
)
pmc1002AlmClientTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxBiasLowWarningPortn.setStatus("current")
_Pmc1002AlmClientTxBiasHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientTxBiasHighWarningPortn_Object = MibTableColumn
pmc1002AlmClientTxBiasHighWarningPortn = _Pmc1002AlmClientTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 5),
    _Pmc1002AlmClientTxBiasHighWarningPortn_Type()
)
pmc1002AlmClientTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxBiasHighWarningPortn.setStatus("current")
_Pmc1002AlmClientTempLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientTempLowWarningPortn_Object = MibTableColumn
pmc1002AlmClientTempLowWarningPortn = _Pmc1002AlmClientTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 8),
    _Pmc1002AlmClientTempLowWarningPortn_Type()
)
pmc1002AlmClientTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTempLowWarningPortn.setStatus("current")
_Pmc1002AlmClientTempHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientTempHighWarningPortn_Object = MibTableColumn
pmc1002AlmClientTempHighWarningPortn = _Pmc1002AlmClientTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 9),
    _Pmc1002AlmClientTempHighWarningPortn_Type()
)
pmc1002AlmClientTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTempHighWarningPortn.setStatus("current")
_Pmc1002AlmClientRxPowerLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientRxPowerLowWarningPortn_Object = MibTableColumn
pmc1002AlmClientRxPowerLowWarningPortn = _Pmc1002AlmClientRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 16),
    _Pmc1002AlmClientRxPowerLowWarningPortn_Type()
)
pmc1002AlmClientRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientRxPowerLowWarningPortn.setStatus("current")
_Pmc1002AlmClientRxPowerHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientRxPowerHighWarningPortn_Object = MibTableColumn
pmc1002AlmClientRxPowerHighWarningPortn = _Pmc1002AlmClientRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 1, 48, 1, 17),
    _Pmc1002AlmClientRxPowerHighWarningPortn_Type()
)
pmc1002AlmClientRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientRxPowerHighWarningPortn.setStatus("current")
_Pmc1002AlmClientUrg_ObjectIdentity = ObjectIdentity
pmc1002AlmClientUrg = _Pmc1002AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2)
)
_Pmc1002AlmclientXfpAlarm1Table_Object = MibTable
pmc1002AlmclientXfpAlarm1Table = _Pmc1002AlmclientXfpAlarm1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpAlarm1Table.setStatus("current")
_Pmc1002AlmclientXfpAlarm1Entry_Object = MibTableRow
pmc1002AlmclientXfpAlarm1Entry = _Pmc1002AlmclientXfpAlarm1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1)
)
pmc1002AlmclientXfpAlarm1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmclientXfpAlarm1Index"),
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpAlarm1Entry.setStatus("current")


class _Pmc1002AlmclientXfpAlarm1Index_Type(Integer32):
    """Custom type pmc1002AlmclientXfpAlarm1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmclientXfpAlarm1Index_Type.__name__ = "Integer32"
_Pmc1002AlmclientXfpAlarm1Index_Object = MibTableColumn
pmc1002AlmclientXfpAlarm1Index = _Pmc1002AlmclientXfpAlarm1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 1),
    _Pmc1002AlmclientXfpAlarm1Index_Type()
)
pmc1002AlmclientXfpAlarm1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpAlarm1Index.setStatus("current")
_Pmc1002AlmClientTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientTxPowerLowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientTxPowerLowAlarmPortn = _Pmc1002AlmClientTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 2),
    _Pmc1002AlmClientTxPowerLowAlarmPortn_Type()
)
pmc1002AlmClientTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxPowerLowAlarmPortn.setStatus("current")
_Pmc1002AlmClientTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientTxPowerHighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientTxPowerHighAlarmPortn = _Pmc1002AlmClientTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 3),
    _Pmc1002AlmClientTxPowerHighAlarmPortn_Type()
)
pmc1002AlmClientTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxPowerHighAlarmPortn.setStatus("current")
_Pmc1002AlmClientTxBiasLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientTxBiasLowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientTxBiasLowAlarmPortn = _Pmc1002AlmClientTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 4),
    _Pmc1002AlmClientTxBiasLowAlarmPortn_Type()
)
pmc1002AlmClientTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxBiasLowAlarmPortn.setStatus("current")
_Pmc1002AlmClientTxBiasHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientTxBiasHighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientTxBiasHighAlarmPortn = _Pmc1002AlmClientTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 5),
    _Pmc1002AlmClientTxBiasHighAlarmPortn_Type()
)
pmc1002AlmClientTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxBiasHighAlarmPortn.setStatus("current")
_Pmc1002AlmClientTempLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientTempLowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientTempLowAlarmPortn = _Pmc1002AlmClientTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 8),
    _Pmc1002AlmClientTempLowAlarmPortn_Type()
)
pmc1002AlmClientTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTempLowAlarmPortn.setStatus("current")
_Pmc1002AlmClientTempHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientTempHighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientTempHighAlarmPortn = _Pmc1002AlmClientTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 9),
    _Pmc1002AlmClientTempHighAlarmPortn_Type()
)
pmc1002AlmClientTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTempHighAlarmPortn.setStatus("current")
_Pmc1002AlmClientRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientRxPowerLowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientRxPowerLowAlarmPortn = _Pmc1002AlmClientRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 16),
    _Pmc1002AlmClientRxPowerLowAlarmPortn_Type()
)
pmc1002AlmClientRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientRxPowerLowAlarmPortn.setStatus("current")
_Pmc1002AlmClientRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientRxPowerHighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientRxPowerHighAlarmPortn = _Pmc1002AlmClientRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 32, 1, 17),
    _Pmc1002AlmClientRxPowerHighAlarmPortn_Type()
)
pmc1002AlmClientRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientRxPowerHighAlarmPortn.setStatus("current")
_Pmc1002AlmclientXfpSupplyAlarmTable_Object = MibTable
pmc1002AlmclientXfpSupplyAlarmTable = _Pmc1002AlmclientXfpSupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64)
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpSupplyAlarmTable.setStatus("current")
_Pmc1002AlmclientXfpSupplyAlarmEntry_Object = MibTableRow
pmc1002AlmclientXfpSupplyAlarmEntry = _Pmc1002AlmclientXfpSupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1)
)
pmc1002AlmclientXfpSupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmclientXfpSupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpSupplyAlarmEntry.setStatus("current")


class _Pmc1002AlmclientXfpSupplyAlarmIndex_Type(Integer32):
    """Custom type pmc1002AlmclientXfpSupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmclientXfpSupplyAlarmIndex_Type.__name__ = "Integer32"
_Pmc1002AlmclientXfpSupplyAlarmIndex_Object = MibTableColumn
pmc1002AlmclientXfpSupplyAlarmIndex = _Pmc1002AlmclientXfpSupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 1),
    _Pmc1002AlmclientXfpSupplyAlarmIndex_Type()
)
pmc1002AlmclientXfpSupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpSupplyAlarmIndex.setStatus("current")
_Pmc1002AlmClientVee5LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVee5LowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVee5LowAlarmPortn = _Pmc1002AlmClientVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 2),
    _Pmc1002AlmClientVee5LowAlarmPortn_Type()
)
pmc1002AlmClientVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVee5LowAlarmPortn.setStatus("current")
_Pmc1002AlmClientVee5HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVee5HighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVee5HighAlarmPortn = _Pmc1002AlmClientVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 3),
    _Pmc1002AlmClientVee5HighAlarmPortn_Type()
)
pmc1002AlmClientVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVee5HighAlarmPortn.setStatus("current")
_Pmc1002AlmClientVcc2LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc2LowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVcc2LowAlarmPortn = _Pmc1002AlmClientVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 4),
    _Pmc1002AlmClientVcc2LowAlarmPortn_Type()
)
pmc1002AlmClientVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc2LowAlarmPortn.setStatus("current")
_Pmc1002AlmClientVcc2HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc2HighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVcc2HighAlarmPortn = _Pmc1002AlmClientVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 5),
    _Pmc1002AlmClientVcc2HighAlarmPortn_Type()
)
pmc1002AlmClientVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc2HighAlarmPortn.setStatus("current")
_Pmc1002AlmClientVcc3LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc3LowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVcc3LowAlarmPortn = _Pmc1002AlmClientVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 6),
    _Pmc1002AlmClientVcc3LowAlarmPortn_Type()
)
pmc1002AlmClientVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc3LowAlarmPortn.setStatus("current")
_Pmc1002AlmClientVcc3HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc3HighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVcc3HighAlarmPortn = _Pmc1002AlmClientVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 7),
    _Pmc1002AlmClientVcc3HighAlarmPortn_Type()
)
pmc1002AlmClientVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc3HighAlarmPortn.setStatus("current")
_Pmc1002AlmClientVcc5LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc5LowAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVcc5LowAlarmPortn = _Pmc1002AlmClientVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 8),
    _Pmc1002AlmClientVcc5LowAlarmPortn_Type()
)
pmc1002AlmClientVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc5LowAlarmPortn.setStatus("current")
_Pmc1002AlmClientVcc5HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc5HighAlarmPortn_Object = MibTableColumn
pmc1002AlmClientVcc5HighAlarmPortn = _Pmc1002AlmClientVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 9),
    _Pmc1002AlmClientVcc5HighAlarmPortn_Type()
)
pmc1002AlmClientVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc5HighAlarmPortn.setStatus("current")
_Pmc1002AlmClientVee5LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVee5LowWarningPortn_Object = MibTableColumn
pmc1002AlmClientVee5LowWarningPortn = _Pmc1002AlmClientVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 10),
    _Pmc1002AlmClientVee5LowWarningPortn_Type()
)
pmc1002AlmClientVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVee5LowWarningPortn.setStatus("current")
_Pmc1002AlmClientVee5HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVee5HighWarningPortn_Object = MibTableColumn
pmc1002AlmClientVee5HighWarningPortn = _Pmc1002AlmClientVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 11),
    _Pmc1002AlmClientVee5HighWarningPortn_Type()
)
pmc1002AlmClientVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVee5HighWarningPortn.setStatus("current")
_Pmc1002AlmClientVcc2LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc2LowWarningPortn_Object = MibTableColumn
pmc1002AlmClientVcc2LowWarningPortn = _Pmc1002AlmClientVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 12),
    _Pmc1002AlmClientVcc2LowWarningPortn_Type()
)
pmc1002AlmClientVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc2LowWarningPortn.setStatus("current")
_Pmc1002AlmClientVcc2HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc2HighWarningPortn_Object = MibTableColumn
pmc1002AlmClientVcc2HighWarningPortn = _Pmc1002AlmClientVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 13),
    _Pmc1002AlmClientVcc2HighWarningPortn_Type()
)
pmc1002AlmClientVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc2HighWarningPortn.setStatus("current")
_Pmc1002AlmClientVcc3LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc3LowWarningPortn_Object = MibTableColumn
pmc1002AlmClientVcc3LowWarningPortn = _Pmc1002AlmClientVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 14),
    _Pmc1002AlmClientVcc3LowWarningPortn_Type()
)
pmc1002AlmClientVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc3LowWarningPortn.setStatus("current")
_Pmc1002AlmClientVcc3HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc3HighWarningPortn_Object = MibTableColumn
pmc1002AlmClientVcc3HighWarningPortn = _Pmc1002AlmClientVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 15),
    _Pmc1002AlmClientVcc3HighWarningPortn_Type()
)
pmc1002AlmClientVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc3HighWarningPortn.setStatus("current")
_Pmc1002AlmClientVcc5LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc5LowWarningPortn_Object = MibTableColumn
pmc1002AlmClientVcc5LowWarningPortn = _Pmc1002AlmClientVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 16),
    _Pmc1002AlmClientVcc5LowWarningPortn_Type()
)
pmc1002AlmClientVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc5LowWarningPortn.setStatus("current")
_Pmc1002AlmClientVcc5HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientVcc5HighWarningPortn_Object = MibTableColumn
pmc1002AlmClientVcc5HighWarningPortn = _Pmc1002AlmClientVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 2, 64, 1, 17),
    _Pmc1002AlmClientVcc5HighWarningPortn_Type()
)
pmc1002AlmClientVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientVcc5HighWarningPortn.setStatus("current")
_Pmc1002AlmClientCrit_ObjectIdentity = ObjectIdentity
pmc1002AlmClientCrit = _Pmc1002AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3)
)
_Pmc1002AlmsynthAlmPortTable_Object = MibTable
pmc1002AlmsynthAlmPortTable = _Pmc1002AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pmc1002AlmsynthAlmPortTable.setStatus("current")
_Pmc1002AlmsynthAlmPortEntry_Object = MibTableRow
pmc1002AlmsynthAlmPortEntry = _Pmc1002AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1)
)
pmc1002AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmsynthAlmPortEntry.setStatus("current")


class _Pmc1002AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pmc1002AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pmc1002AlmsynthAlmPortIndex_Object = MibTableColumn
pmc1002AlmsynthAlmPortIndex = _Pmc1002AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 1),
    _Pmc1002AlmsynthAlmPortIndex_Type()
)
pmc1002AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmsynthAlmPortIndex.setStatus("current")
_Pmc1002AlmClientSfpAbsentPortn_Type = EkiOnOff
_Pmc1002AlmClientSfpAbsentPortn_Object = MibTableColumn
pmc1002AlmClientSfpAbsentPortn = _Pmc1002AlmClientSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 2),
    _Pmc1002AlmClientSfpAbsentPortn_Type()
)
pmc1002AlmClientSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientSfpAbsentPortn.setStatus("current")
_Pmc1002AlmClientDdmAbsentPortn_Type = EkiOnOff
_Pmc1002AlmClientDdmAbsentPortn_Object = MibTableColumn
pmc1002AlmClientDdmAbsentPortn = _Pmc1002AlmClientDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 3),
    _Pmc1002AlmClientDdmAbsentPortn_Type()
)
pmc1002AlmClientDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientDdmAbsentPortn.setStatus("current")
_Pmc1002AlmClientHwFailPortn_Type = EkiOnOff
_Pmc1002AlmClientHwFailPortn_Object = MibTableColumn
pmc1002AlmClientHwFailPortn = _Pmc1002AlmClientHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 5),
    _Pmc1002AlmClientHwFailPortn_Type()
)
pmc1002AlmClientHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientHwFailPortn.setStatus("current")
_Pmc1002AlmClientDwLsdPortn_Type = EkiOnOff
_Pmc1002AlmClientDwLsdPortn_Object = MibTableColumn
pmc1002AlmClientDwLsdPortn = _Pmc1002AlmClientDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 6),
    _Pmc1002AlmClientDwLsdPortn_Type()
)
pmc1002AlmClientDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientDwLsdPortn.setStatus("current")
_Pmc1002AlmClientLocalOosPortn_Type = EkiOnOff
_Pmc1002AlmClientLocalOosPortn_Object = MibTableColumn
pmc1002AlmClientLocalOosPortn = _Pmc1002AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 7),
    _Pmc1002AlmClientLocalOosPortn_Type()
)
pmc1002AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientLocalOosPortn.setStatus("current")
_Pmc1002AlmClientDwCaisPortn_Type = EkiOnOff
_Pmc1002AlmClientDwCaisPortn_Object = MibTableColumn
pmc1002AlmClientDwCaisPortn = _Pmc1002AlmClientDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 9),
    _Pmc1002AlmClientDwCaisPortn_Type()
)
pmc1002AlmClientDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientDwCaisPortn.setStatus("current")
_Pmc1002AlmClientSfpDdmWarningPortn_Type = EkiOnOff
_Pmc1002AlmClientSfpDdmWarningPortn_Object = MibTableColumn
pmc1002AlmClientSfpDdmWarningPortn = _Pmc1002AlmClientSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 10),
    _Pmc1002AlmClientSfpDdmWarningPortn_Type()
)
pmc1002AlmClientSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientSfpDdmWarningPortn.setStatus("current")
_Pmc1002AlmClientSfpDdmAlmPortn_Type = EkiOnOff
_Pmc1002AlmClientSfpDdmAlmPortn_Object = MibTableColumn
pmc1002AlmClientSfpDdmAlmPortn = _Pmc1002AlmClientSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 11),
    _Pmc1002AlmClientSfpDdmAlmPortn_Type()
)
pmc1002AlmClientSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientSfpDdmAlmPortn.setStatus("current")
_Pmc1002AlmClientFailPortn_Type = EkiOnOff
_Pmc1002AlmClientFailPortn_Object = MibTableColumn
pmc1002AlmClientFailPortn = _Pmc1002AlmClientFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 13),
    _Pmc1002AlmClientFailPortn_Type()
)
pmc1002AlmClientFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientFailPortn.setStatus("current")
_Pmc1002AlmClientUpCsfPortn_Type = EkiOnOff
_Pmc1002AlmClientUpCsfPortn_Object = MibTableColumn
pmc1002AlmClientUpCsfPortn = _Pmc1002AlmClientUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 8, 1, 17),
    _Pmc1002AlmClientUpCsfPortn_Type()
)
pmc1002AlmClientUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientUpCsfPortn.setStatus("current")
_Pmc1002AlmclientAccessioAlmTable_Object = MibTable
pmc1002AlmclientAccessioAlmTable = _Pmc1002AlmclientAccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pmc1002AlmclientAccessioAlmTable.setStatus("current")
_Pmc1002AlmclientAccessioAlmEntry_Object = MibTableRow
pmc1002AlmclientAccessioAlmEntry = _Pmc1002AlmclientAccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 16, 1)
)
pmc1002AlmclientAccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmclientAccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmclientAccessioAlmEntry.setStatus("current")


class _Pmc1002AlmclientAccessioAlmIndex_Type(Integer32):
    """Custom type pmc1002AlmclientAccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmclientAccessioAlmIndex_Type.__name__ = "Integer32"
_Pmc1002AlmclientAccessioAlmIndex_Object = MibTableColumn
pmc1002AlmclientAccessioAlmIndex = _Pmc1002AlmclientAccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 16, 1, 1),
    _Pmc1002AlmclientAccessioAlmIndex_Type()
)
pmc1002AlmclientAccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmclientAccessioAlmIndex.setStatus("current")
_Pmc1002AlmClientDwLasFailPortn_Type = EkiOnOff
_Pmc1002AlmClientDwLasFailPortn_Object = MibTableColumn
pmc1002AlmClientDwLasFailPortn = _Pmc1002AlmClientDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 16, 1, 2),
    _Pmc1002AlmClientDwLasFailPortn_Type()
)
pmc1002AlmClientDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientDwLasFailPortn.setStatus("current")
_Pmc1002AlmClientUpLosPortn_Type = EkiOnOff
_Pmc1002AlmClientUpLosPortn_Object = MibTableColumn
pmc1002AlmClientUpLosPortn = _Pmc1002AlmClientUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 16, 1, 5),
    _Pmc1002AlmClientUpLosPortn_Type()
)
pmc1002AlmClientUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientUpLosPortn.setStatus("current")
_Pmc1002AlmclientXfpAlarm2Table_Object = MibTable
pmc1002AlmclientXfpAlarm2Table = _Pmc1002AlmclientXfpAlarm2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40)
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpAlarm2Table.setStatus("current")
_Pmc1002AlmclientXfpAlarm2Entry_Object = MibTableRow
pmc1002AlmclientXfpAlarm2Entry = _Pmc1002AlmclientXfpAlarm2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1)
)
pmc1002AlmclientXfpAlarm2Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmclientXfpAlarm2Index"),
)
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpAlarm2Entry.setStatus("current")


class _Pmc1002AlmclientXfpAlarm2Index_Type(Integer32):
    """Custom type pmc1002AlmclientXfpAlarm2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmclientXfpAlarm2Index_Type.__name__ = "Integer32"
_Pmc1002AlmclientXfpAlarm2Index_Object = MibTableColumn
pmc1002AlmclientXfpAlarm2Index = _Pmc1002AlmclientXfpAlarm2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 1),
    _Pmc1002AlmclientXfpAlarm2Index_Type()
)
pmc1002AlmclientXfpAlarm2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmclientXfpAlarm2Index.setStatus("current")
_Pmc1002AlmClientModNrPortn_Type = EkiOnOff
_Pmc1002AlmClientModNrPortn_Object = MibTableColumn
pmc1002AlmClientModNrPortn = _Pmc1002AlmClientModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 3),
    _Pmc1002AlmClientModNrPortn_Type()
)
pmc1002AlmClientModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientModNrPortn.setStatus("current")
_Pmc1002AlmClientRxCdrNotLockedPortn_Type = EkiOnOff
_Pmc1002AlmClientRxCdrNotLockedPortn_Object = MibTableColumn
pmc1002AlmClientRxCdrNotLockedPortn = _Pmc1002AlmClientRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 4),
    _Pmc1002AlmClientRxCdrNotLockedPortn_Type()
)
pmc1002AlmClientRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientRxCdrNotLockedPortn.setStatus("current")
_Pmc1002AlmClientRxNrPortn_Type = EkiOnOff
_Pmc1002AlmClientRxNrPortn_Object = MibTableColumn
pmc1002AlmClientRxNrPortn = _Pmc1002AlmClientRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 6),
    _Pmc1002AlmClientRxNrPortn_Type()
)
pmc1002AlmClientRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientRxNrPortn.setStatus("current")
_Pmc1002AlmClientTxCdrNotLockedPortn_Type = EkiOnOff
_Pmc1002AlmClientTxCdrNotLockedPortn_Object = MibTableColumn
pmc1002AlmClientTxCdrNotLockedPortn = _Pmc1002AlmClientTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 7),
    _Pmc1002AlmClientTxCdrNotLockedPortn_Type()
)
pmc1002AlmClientTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxCdrNotLockedPortn.setStatus("current")
_Pmc1002AlmClientTxFaultPortn_Type = EkiOnOff
_Pmc1002AlmClientTxFaultPortn_Object = MibTableColumn
pmc1002AlmClientTxFaultPortn = _Pmc1002AlmClientTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 8),
    _Pmc1002AlmClientTxFaultPortn_Type()
)
pmc1002AlmClientTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxFaultPortn.setStatus("current")
_Pmc1002AlmClientTxNrPortn_Type = EkiOnOff
_Pmc1002AlmClientTxNrPortn_Object = MibTableColumn
pmc1002AlmClientTxNrPortn = _Pmc1002AlmClientTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 9),
    _Pmc1002AlmClientTxNrPortn_Type()
)
pmc1002AlmClientTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTxNrPortn.setStatus("current")
_Pmc1002AlmClientWavelengthUnlockedPortn_Type = EkiOnOff
_Pmc1002AlmClientWavelengthUnlockedPortn_Object = MibTableColumn
pmc1002AlmClientWavelengthUnlockedPortn = _Pmc1002AlmClientWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 15),
    _Pmc1002AlmClientWavelengthUnlockedPortn_Type()
)
pmc1002AlmClientWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientWavelengthUnlockedPortn.setStatus("current")
_Pmc1002AlmClientTecFaultPortn_Type = EkiOnOff
_Pmc1002AlmClientTecFaultPortn_Object = MibTableColumn
pmc1002AlmClientTecFaultPortn = _Pmc1002AlmClientTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 16),
    _Pmc1002AlmClientTecFaultPortn_Type()
)
pmc1002AlmClientTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientTecFaultPortn.setStatus("current")
_Pmc1002AlmClientApdSupplyFaultPortn_Type = EkiOnOff
_Pmc1002AlmClientApdSupplyFaultPortn_Object = MibTableColumn
pmc1002AlmClientApdSupplyFaultPortn = _Pmc1002AlmClientApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 40, 1, 17),
    _Pmc1002AlmClientApdSupplyFaultPortn_Type()
)
pmc1002AlmClientApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientApdSupplyFaultPortn.setStatus("current")
_Pmc1002AlmclientMapperDeAlmTable_Object = MibTable
pmc1002AlmclientMapperDeAlmTable = _Pmc1002AlmclientMapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pmc1002AlmclientMapperDeAlmTable.setStatus("current")
_Pmc1002AlmclientMapperDeAlmEntry_Object = MibTableRow
pmc1002AlmclientMapperDeAlmEntry = _Pmc1002AlmclientMapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72, 1)
)
pmc1002AlmclientMapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmclientMapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmclientMapperDeAlmEntry.setStatus("current")


class _Pmc1002AlmclientMapperDeAlmIndex_Type(Integer32):
    """Custom type pmc1002AlmclientMapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmclientMapperDeAlmIndex_Type.__name__ = "Integer32"
_Pmc1002AlmclientMapperDeAlmIndex_Object = MibTableColumn
pmc1002AlmclientMapperDeAlmIndex = _Pmc1002AlmclientMapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72, 1, 1),
    _Pmc1002AlmclientMapperDeAlmIndex_Type()
)
pmc1002AlmclientMapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmclientMapperDeAlmIndex.setStatus("current")
_Pmc1002AlmClientUpAccOosPortn_Type = EkiOnOff
_Pmc1002AlmClientUpAccOosPortn_Object = MibTableColumn
pmc1002AlmClientUpAccOosPortn = _Pmc1002AlmClientUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72, 1, 2),
    _Pmc1002AlmClientUpAccOosPortn_Type()
)
pmc1002AlmClientUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientUpAccOosPortn.setStatus("current")
_Pmc1002AlmClientUpBufferOvlPortn_Type = EkiOnOff
_Pmc1002AlmClientUpBufferOvlPortn_Object = MibTableColumn
pmc1002AlmClientUpBufferOvlPortn = _Pmc1002AlmClientUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72, 1, 11),
    _Pmc1002AlmClientUpBufferOvlPortn_Type()
)
pmc1002AlmClientUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientUpBufferOvlPortn.setStatus("current")
_Pmc1002AlmClientDwCsfDetPortn_Type = EkiOnOff
_Pmc1002AlmClientDwCsfDetPortn_Object = MibTableColumn
pmc1002AlmClientDwCsfDetPortn = _Pmc1002AlmClientDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72, 1, 12),
    _Pmc1002AlmClientDwCsfDetPortn_Type()
)
pmc1002AlmClientDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientDwCsfDetPortn.setStatus("current")
_Pmc1002AlmClientDwBufferOvlPortn_Type = EkiOnOff
_Pmc1002AlmClientDwBufferOvlPortn_Object = MibTableColumn
pmc1002AlmClientDwBufferOvlPortn = _Pmc1002AlmClientDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 2, 3, 72, 1, 15),
    _Pmc1002AlmClientDwBufferOvlPortn_Type()
)
pmc1002AlmClientDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmClientDwBufferOvlPortn.setStatus("current")
_Pmc1002AlmLine_ObjectIdentity = ObjectIdentity
pmc1002AlmLine = _Pmc1002AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3)
)
_Pmc1002AlmLineNurg_ObjectIdentity = ObjectIdentity
pmc1002AlmLineNurg = _Pmc1002AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1)
)
_Pmc1002AlmlineXfp1WarningsTable_Object = MibTable
pmc1002AlmlineXfp1WarningsTable = _Pmc1002AlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1WarningsTable.setStatus("current")
_Pmc1002AlmlineXfp1WarningsEntry_Object = MibTableRow
pmc1002AlmlineXfp1WarningsEntry = _Pmc1002AlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1)
)
pmc1002AlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1WarningsEntry.setStatus("current")


class _Pmc1002AlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pmc1002AlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineXfp1WarningsIndex_Object = MibTableColumn
pmc1002AlmlineXfp1WarningsIndex = _Pmc1002AlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 1),
    _Pmc1002AlmlineXfp1WarningsIndex_Type()
)
pmc1002AlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1WarningsIndex.setStatus("current")
_Pmc1002AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pmc1002AlmLineTxPowerLowWarningPortn = _Pmc1002AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 2),
    _Pmc1002AlmLineTxPowerLowWarningPortn_Type()
)
pmc1002AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxPowerLowWarningPortn.setStatus("current")
_Pmc1002AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineTxPowerHighWarningPortn = _Pmc1002AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 3),
    _Pmc1002AlmLineTxPowerHighWarningPortn_Type()
)
pmc1002AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxPowerHighWarningPortn.setStatus("current")
_Pmc1002AlmLineTxBiasLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineTxBiasLowWarningPortn_Object = MibTableColumn
pmc1002AlmLineTxBiasLowWarningPortn = _Pmc1002AlmLineTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 4),
    _Pmc1002AlmLineTxBiasLowWarningPortn_Type()
)
pmc1002AlmLineTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxBiasLowWarningPortn.setStatus("current")
_Pmc1002AlmLineTxBiasHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineTxBiasHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineTxBiasHighWarningPortn = _Pmc1002AlmLineTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 5),
    _Pmc1002AlmLineTxBiasHighWarningPortn_Type()
)
pmc1002AlmLineTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxBiasHighWarningPortn.setStatus("current")
_Pmc1002AlmLineTempLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineTempLowWarningPortn_Object = MibTableColumn
pmc1002AlmLineTempLowWarningPortn = _Pmc1002AlmLineTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 8),
    _Pmc1002AlmLineTempLowWarningPortn_Type()
)
pmc1002AlmLineTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTempLowWarningPortn.setStatus("current")
_Pmc1002AlmLineTempHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineTempHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineTempHighWarningPortn = _Pmc1002AlmLineTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 9),
    _Pmc1002AlmLineTempHighWarningPortn_Type()
)
pmc1002AlmLineTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTempHighWarningPortn.setStatus("current")
_Pmc1002AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pmc1002AlmLineRxPowerLowWarningPortn = _Pmc1002AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 16),
    _Pmc1002AlmLineRxPowerLowWarningPortn_Type()
)
pmc1002AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineRxPowerLowWarningPortn.setStatus("current")
_Pmc1002AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineRxPowerHighWarningPortn = _Pmc1002AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 209, 1, 17),
    _Pmc1002AlmLineRxPowerHighWarningPortn_Type()
)
pmc1002AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineRxPowerHighWarningPortn.setStatus("current")
_Pmc1002AlmlineOtx1TlhWarningsTable_Object = MibTable
pmc1002AlmlineOtx1TlhWarningsTable = _Pmc1002AlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineOtx1TlhWarningsTable.setStatus("current")
_Pmc1002AlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pmc1002AlmlineOtx1TlhWarningsEntry = _Pmc1002AlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225, 1)
)
pmc1002AlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pmc1002AlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pmc1002AlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pmc1002AlmlineOtx1TlhWarningsIndex = _Pmc1002AlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225, 1, 1),
    _Pmc1002AlmlineOtx1TlhWarningsIndex_Type()
)
pmc1002AlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pmc1002AlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineModulatorAgingHighWarningPortn = _Pmc1002AlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225, 1, 6),
    _Pmc1002AlmLineModulatorAgingHighWarningPortn_Type()
)
pmc1002AlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pmc1002AlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineAgingHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineAgingHighWarningPortn = _Pmc1002AlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225, 1, 7),
    _Pmc1002AlmLineAgingHighWarningPortn_Type()
)
pmc1002AlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineAgingHighWarningPortn.setStatus("current")
_Pmc1002AlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineFreqDevHighWarningPortn = _Pmc1002AlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225, 1, 13),
    _Pmc1002AlmLineFreqDevHighWarningPortn_Type()
)
pmc1002AlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineFreqDevHighWarningPortn.setStatus("current")
_Pmc1002AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pmc1002AlmLineLaserTempHighWarningPortn = _Pmc1002AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 1, 225, 1, 15),
    _Pmc1002AlmLineLaserTempHighWarningPortn_Type()
)
pmc1002AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineLaserTempHighWarningPortn.setStatus("current")
_Pmc1002AlmLineUrg_ObjectIdentity = ObjectIdentity
pmc1002AlmLineUrg = _Pmc1002AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2)
)
_Pmc1002AlmdfrmBerTable_Object = MibTable
pmc1002AlmdfrmBerTable = _Pmc1002AlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pmc1002AlmdfrmBerTable.setStatus("current")
_Pmc1002AlmdfrmBerEntry_Object = MibTableRow
pmc1002AlmdfrmBerEntry = _Pmc1002AlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 129, 1)
)
pmc1002AlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmdfrmBerEntry.setStatus("current")


class _Pmc1002AlmdfrmBerIndex_Type(Integer32):
    """Custom type pmc1002AlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pmc1002AlmdfrmBerIndex_Object = MibTableColumn
pmc1002AlmdfrmBerIndex = _Pmc1002AlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 129, 1, 1),
    _Pmc1002AlmdfrmBerIndex_Type()
)
pmc1002AlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmdfrmBerIndex.setStatus("current")
_Pmc1002AlmLineSignalDegradePortn_Type = EkiOnOff
_Pmc1002AlmLineSignalDegradePortn_Object = MibTableColumn
pmc1002AlmLineSignalDegradePortn = _Pmc1002AlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 129, 1, 2),
    _Pmc1002AlmLineSignalDegradePortn_Type()
)
pmc1002AlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineSignalDegradePortn.setStatus("current")
_Pmc1002AlmLineSignalFailPortn_Type = EkiOnOff
_Pmc1002AlmLineSignalFailPortn_Object = MibTableColumn
pmc1002AlmLineSignalFailPortn = _Pmc1002AlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 129, 1, 3),
    _Pmc1002AlmLineSignalFailPortn_Type()
)
pmc1002AlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineSignalFailPortn.setStatus("current")
_Pmc1002AlmLineDegradePortn_Type = EkiOnOff
_Pmc1002AlmLineDegradePortn_Object = MibTableColumn
pmc1002AlmLineDegradePortn = _Pmc1002AlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 129, 1, 6),
    _Pmc1002AlmLineDegradePortn_Type()
)
pmc1002AlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDegradePortn.setStatus("current")
_Pmc1002AlmlineXfp1AlarmTable_Object = MibTable
pmc1002AlmlineXfp1AlarmTable = _Pmc1002AlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1AlarmTable.setStatus("current")
_Pmc1002AlmlineXfp1AlarmEntry_Object = MibTableRow
pmc1002AlmlineXfp1AlarmEntry = _Pmc1002AlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1)
)
pmc1002AlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1AlarmEntry.setStatus("current")


class _Pmc1002AlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pmc1002AlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineXfp1AlarmIndex_Object = MibTableColumn
pmc1002AlmlineXfp1AlarmIndex = _Pmc1002AlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 1),
    _Pmc1002AlmlineXfp1AlarmIndex_Type()
)
pmc1002AlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1AlarmIndex.setStatus("current")
_Pmc1002AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineTxPowerLowAlarmPortn = _Pmc1002AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 2),
    _Pmc1002AlmLineTxPowerLowAlarmPortn_Type()
)
pmc1002AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pmc1002AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineTxPowerHighAlarmPortn = _Pmc1002AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 3),
    _Pmc1002AlmLineTxPowerHighAlarmPortn_Type()
)
pmc1002AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pmc1002AlmLineTxBiasLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineTxBiasLowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineTxBiasLowAlarmPortn = _Pmc1002AlmLineTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 4),
    _Pmc1002AlmLineTxBiasLowAlarmPortn_Type()
)
pmc1002AlmLineTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxBiasLowAlarmPortn.setStatus("current")
_Pmc1002AlmLineTxBiasHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineTxBiasHighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineTxBiasHighAlarmPortn = _Pmc1002AlmLineTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 5),
    _Pmc1002AlmLineTxBiasHighAlarmPortn_Type()
)
pmc1002AlmLineTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxBiasHighAlarmPortn.setStatus("current")
_Pmc1002AlmLineTempLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineTempLowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineTempLowAlarmPortn = _Pmc1002AlmLineTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 8),
    _Pmc1002AlmLineTempLowAlarmPortn_Type()
)
pmc1002AlmLineTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTempLowAlarmPortn.setStatus("current")
_Pmc1002AlmLineTempHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineTempHighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineTempHighAlarmPortn = _Pmc1002AlmLineTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 9),
    _Pmc1002AlmLineTempHighAlarmPortn_Type()
)
pmc1002AlmLineTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTempHighAlarmPortn.setStatus("current")
_Pmc1002AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineRxPowerLowAlarmPortn = _Pmc1002AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 16),
    _Pmc1002AlmLineRxPowerLowAlarmPortn_Type()
)
pmc1002AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pmc1002AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineRxPowerHighAlarmPortn = _Pmc1002AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 208, 1, 17),
    _Pmc1002AlmLineRxPowerHighAlarmPortn_Type()
)
pmc1002AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pmc1002AlmlineXfp1SupplyAlarmTable_Object = MibTable
pmc1002AlmlineXfp1SupplyAlarmTable = _Pmc1002AlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pmc1002AlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pmc1002AlmlineXfp1SupplyAlarmEntry = _Pmc1002AlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1)
)
pmc1002AlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pmc1002AlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pmc1002AlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pmc1002AlmlineXfp1SupplyAlarmIndex = _Pmc1002AlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 1),
    _Pmc1002AlmlineXfp1SupplyAlarmIndex_Type()
)
pmc1002AlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pmc1002AlmLineVee5LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVee5LowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVee5LowAlarmPortn = _Pmc1002AlmLineVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 2),
    _Pmc1002AlmLineVee5LowAlarmPortn_Type()
)
pmc1002AlmLineVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVee5LowAlarmPortn.setStatus("current")
_Pmc1002AlmLineVee5HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVee5HighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVee5HighAlarmPortn = _Pmc1002AlmLineVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 3),
    _Pmc1002AlmLineVee5HighAlarmPortn_Type()
)
pmc1002AlmLineVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVee5HighAlarmPortn.setStatus("current")
_Pmc1002AlmLineVcc2LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc2LowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVcc2LowAlarmPortn = _Pmc1002AlmLineVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 4),
    _Pmc1002AlmLineVcc2LowAlarmPortn_Type()
)
pmc1002AlmLineVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc2LowAlarmPortn.setStatus("current")
_Pmc1002AlmLineVcc2HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc2HighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVcc2HighAlarmPortn = _Pmc1002AlmLineVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 5),
    _Pmc1002AlmLineVcc2HighAlarmPortn_Type()
)
pmc1002AlmLineVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc2HighAlarmPortn.setStatus("current")
_Pmc1002AlmLineVcc3LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc3LowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVcc3LowAlarmPortn = _Pmc1002AlmLineVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 6),
    _Pmc1002AlmLineVcc3LowAlarmPortn_Type()
)
pmc1002AlmLineVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc3LowAlarmPortn.setStatus("current")
_Pmc1002AlmLineVcc3HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc3HighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVcc3HighAlarmPortn = _Pmc1002AlmLineVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 7),
    _Pmc1002AlmLineVcc3HighAlarmPortn_Type()
)
pmc1002AlmLineVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc3HighAlarmPortn.setStatus("current")
_Pmc1002AlmLineVcc5LowAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc5LowAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVcc5LowAlarmPortn = _Pmc1002AlmLineVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 8),
    _Pmc1002AlmLineVcc5LowAlarmPortn_Type()
)
pmc1002AlmLineVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc5LowAlarmPortn.setStatus("current")
_Pmc1002AlmLineVcc5HighAlarmPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc5HighAlarmPortn_Object = MibTableColumn
pmc1002AlmLineVcc5HighAlarmPortn = _Pmc1002AlmLineVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 9),
    _Pmc1002AlmLineVcc5HighAlarmPortn_Type()
)
pmc1002AlmLineVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc5HighAlarmPortn.setStatus("current")
_Pmc1002AlmLineVee5LowLineWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVee5LowLineWarningPortn_Object = MibTableColumn
pmc1002AlmLineVee5LowLineWarningPortn = _Pmc1002AlmLineVee5LowLineWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 10),
    _Pmc1002AlmLineVee5LowLineWarningPortn_Type()
)
pmc1002AlmLineVee5LowLineWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVee5LowLineWarningPortn.setStatus("current")
_Pmc1002AlmLineVee5HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVee5HighWarningPortn_Object = MibTableColumn
pmc1002AlmLineVee5HighWarningPortn = _Pmc1002AlmLineVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 11),
    _Pmc1002AlmLineVee5HighWarningPortn_Type()
)
pmc1002AlmLineVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVee5HighWarningPortn.setStatus("current")
_Pmc1002AlmLineVcc2LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc2LowWarningPortn_Object = MibTableColumn
pmc1002AlmLineVcc2LowWarningPortn = _Pmc1002AlmLineVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 12),
    _Pmc1002AlmLineVcc2LowWarningPortn_Type()
)
pmc1002AlmLineVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc2LowWarningPortn.setStatus("current")
_Pmc1002AlmLineVcc2HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc2HighWarningPortn_Object = MibTableColumn
pmc1002AlmLineVcc2HighWarningPortn = _Pmc1002AlmLineVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 13),
    _Pmc1002AlmLineVcc2HighWarningPortn_Type()
)
pmc1002AlmLineVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc2HighWarningPortn.setStatus("current")
_Pmc1002AlmLineVcc3LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc3LowWarningPortn_Object = MibTableColumn
pmc1002AlmLineVcc3LowWarningPortn = _Pmc1002AlmLineVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 14),
    _Pmc1002AlmLineVcc3LowWarningPortn_Type()
)
pmc1002AlmLineVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc3LowWarningPortn.setStatus("current")
_Pmc1002AlmLineVcc3HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc3HighWarningPortn_Object = MibTableColumn
pmc1002AlmLineVcc3HighWarningPortn = _Pmc1002AlmLineVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 15),
    _Pmc1002AlmLineVcc3HighWarningPortn_Type()
)
pmc1002AlmLineVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc3HighWarningPortn.setStatus("current")
_Pmc1002AlmLineVcc5LowWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc5LowWarningPortn_Object = MibTableColumn
pmc1002AlmLineVcc5LowWarningPortn = _Pmc1002AlmLineVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 16),
    _Pmc1002AlmLineVcc5LowWarningPortn_Type()
)
pmc1002AlmLineVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc5LowWarningPortn.setStatus("current")
_Pmc1002AlmLineVcc5HighWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineVcc5HighWarningPortn_Object = MibTableColumn
pmc1002AlmLineVcc5HighWarningPortn = _Pmc1002AlmLineVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 212, 1, 17),
    _Pmc1002AlmLineVcc5HighWarningPortn_Type()
)
pmc1002AlmLineVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineVcc5HighWarningPortn.setStatus("current")
_Pmc1002AlmlineOtx1TlhAlarmsTable_Object = MibTable
pmc1002AlmlineOtx1TlhAlarmsTable = _Pmc1002AlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pmc1002AlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pmc1002AlmlineOtx1TlhAlarmsEntry = _Pmc1002AlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1)
)
pmc1002AlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pmc1002AlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pmc1002AlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pmc1002AlmlineOtx1TlhAlarmsIndex = _Pmc1002AlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1, 1),
    _Pmc1002AlmlineOtx1TlhAlarmsIndex_Type()
)
pmc1002AlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pmc1002AlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pmc1002AlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pmc1002AlmLineModulatorAgingHighAlaPortn = _Pmc1002AlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1, 6),
    _Pmc1002AlmLineModulatorAgingHighAlaPortn_Type()
)
pmc1002AlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pmc1002AlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pmc1002AlmLineAgingHighAlaPortn_Object = MibTableColumn
pmc1002AlmLineAgingHighAlaPortn = _Pmc1002AlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1, 7),
    _Pmc1002AlmLineAgingHighAlaPortn_Type()
)
pmc1002AlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineAgingHighAlaPortn.setStatus("current")
_Pmc1002AlmLineCdrNotReadyPortn_Type = EkiOnOff
_Pmc1002AlmLineCdrNotReadyPortn_Object = MibTableColumn
pmc1002AlmLineCdrNotReadyPortn = _Pmc1002AlmLineCdrNotReadyPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1, 10),
    _Pmc1002AlmLineCdrNotReadyPortn_Type()
)
pmc1002AlmLineCdrNotReadyPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineCdrNotReadyPortn.setStatus("current")
_Pmc1002AlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pmc1002AlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pmc1002AlmLineFreqDevHighAlaPortn = _Pmc1002AlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1, 13),
    _Pmc1002AlmLineFreqDevHighAlaPortn_Type()
)
pmc1002AlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineFreqDevHighAlaPortn.setStatus("current")
_Pmc1002AlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pmc1002AlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pmc1002AlmLineLaserTempHighAlaPortn = _Pmc1002AlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 2, 224, 1, 15),
    _Pmc1002AlmLineLaserTempHighAlaPortn_Type()
)
pmc1002AlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineLaserTempHighAlaPortn.setStatus("current")
_Pmc1002AlmLineCrit_ObjectIdentity = ObjectIdentity
pmc1002AlmLineCrit = _Pmc1002AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3)
)
_Pmc1002AlmsynthAlmLineTable_Object = MibTable
pmc1002AlmsynthAlmLineTable = _Pmc1002AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pmc1002AlmsynthAlmLineTable.setStatus("current")
_Pmc1002AlmsynthAlmLineEntry_Object = MibTableRow
pmc1002AlmsynthAlmLineEntry = _Pmc1002AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1)
)
pmc1002AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmsynthAlmLineEntry.setStatus("current")


class _Pmc1002AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pmc1002AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pmc1002AlmsynthAlmLineIndex_Object = MibTableColumn
pmc1002AlmsynthAlmLineIndex = _Pmc1002AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 1),
    _Pmc1002AlmsynthAlmLineIndex_Type()
)
pmc1002AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmsynthAlmLineIndex.setStatus("current")
_Pmc1002AlmLineXfpAbsentPortn_Type = EkiOnOff
_Pmc1002AlmLineXfpAbsentPortn_Object = MibTableColumn
pmc1002AlmLineXfpAbsentPortn = _Pmc1002AlmLineXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 2),
    _Pmc1002AlmLineXfpAbsentPortn_Type()
)
pmc1002AlmLineXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineXfpAbsentPortn.setStatus("current")
_Pmc1002AlmLineXfpInitNotComplPortn_Type = EkiOnOff
_Pmc1002AlmLineXfpInitNotComplPortn_Object = MibTableColumn
pmc1002AlmLineXfpInitNotComplPortn = _Pmc1002AlmLineXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 3),
    _Pmc1002AlmLineXfpInitNotComplPortn_Type()
)
pmc1002AlmLineXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineXfpInitNotComplPortn.setStatus("current")
_Pmc1002AlmLineHwFailPortn_Type = EkiOnOff
_Pmc1002AlmLineHwFailPortn_Object = MibTableColumn
pmc1002AlmLineHwFailPortn = _Pmc1002AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 5),
    _Pmc1002AlmLineHwFailPortn_Type()
)
pmc1002AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineHwFailPortn.setStatus("current")
_Pmc1002AlmLineXfpTxOffPortn_Type = EkiOnOff
_Pmc1002AlmLineXfpTxOffPortn_Object = MibTableColumn
pmc1002AlmLineXfpTxOffPortn = _Pmc1002AlmLineXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 6),
    _Pmc1002AlmLineXfpTxOffPortn_Type()
)
pmc1002AlmLineXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineXfpTxOffPortn.setStatus("current")
_Pmc1002AlmLineLocalOosPortn_Type = EkiOnOff
_Pmc1002AlmLineLocalOosPortn_Object = MibTableColumn
pmc1002AlmLineLocalOosPortn = _Pmc1002AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 7),
    _Pmc1002AlmLineLocalOosPortn_Type()
)
pmc1002AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineLocalOosPortn.setStatus("current")
_Pmc1002AlmLineUpRdiInsPortn_Type = EkiOnOff
_Pmc1002AlmLineUpRdiInsPortn_Object = MibTableColumn
pmc1002AlmLineUpRdiInsPortn = _Pmc1002AlmLineUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 9),
    _Pmc1002AlmLineUpRdiInsPortn_Type()
)
pmc1002AlmLineUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineUpRdiInsPortn.setStatus("current")
_Pmc1002AlmLineDdmWarningPortn_Type = EkiOnOff
_Pmc1002AlmLineDdmWarningPortn_Object = MibTableColumn
pmc1002AlmLineDdmWarningPortn = _Pmc1002AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 10),
    _Pmc1002AlmLineDdmWarningPortn_Type()
)
pmc1002AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDdmWarningPortn.setStatus("current")
_Pmc1002AlmLineDdmAlmPortn_Type = EkiOnOff
_Pmc1002AlmLineDdmAlmPortn_Object = MibTableColumn
pmc1002AlmLineDdmAlmPortn = _Pmc1002AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 11),
    _Pmc1002AlmLineDdmAlmPortn_Type()
)
pmc1002AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDdmAlmPortn.setStatus("current")
_Pmc1002AlmLineFailPortn_Type = EkiOnOff
_Pmc1002AlmLineFailPortn_Object = MibTableColumn
pmc1002AlmLineFailPortn = _Pmc1002AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 13),
    _Pmc1002AlmLineFailPortn_Type()
)
pmc1002AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineFailPortn.setStatus("current")
_Pmc1002AlmLineActivePortn_Type = EkiOnOff
_Pmc1002AlmLineActivePortn_Object = MibTableColumn
pmc1002AlmLineActivePortn = _Pmc1002AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 7, 1, 17),
    _Pmc1002AlmLineActivePortn_Type()
)
pmc1002AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineActivePortn.setStatus("current")
_Pmc1002AlmdfrmAlmTable_Object = MibTable
pmc1002AlmdfrmAlmTable = _Pmc1002AlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pmc1002AlmdfrmAlmTable.setStatus("current")
_Pmc1002AlmdfrmAlmEntry_Object = MibTableRow
pmc1002AlmdfrmAlmEntry = _Pmc1002AlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1)
)
pmc1002AlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmdfrmAlmEntry.setStatus("current")


class _Pmc1002AlmdfrmAlmIndex_Type(Integer32):
    """Custom type pmc1002AlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pmc1002AlmdfrmAlmIndex_Object = MibTableColumn
pmc1002AlmdfrmAlmIndex = _Pmc1002AlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1, 1),
    _Pmc1002AlmdfrmAlmIndex_Type()
)
pmc1002AlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmdfrmAlmIndex.setStatus("current")
_Pmc1002AlmLineDwAisDetPortn_Type = EkiOnOff
_Pmc1002AlmLineDwAisDetPortn_Object = MibTableColumn
pmc1002AlmLineDwAisDetPortn = _Pmc1002AlmLineDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1, 2),
    _Pmc1002AlmLineDwAisDetPortn_Type()
)
pmc1002AlmLineDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDwAisDetPortn.setStatus("current")
_Pmc1002AlmLineDwRdiDetPortn_Type = EkiOnOff
_Pmc1002AlmLineDwRdiDetPortn_Object = MibTableColumn
pmc1002AlmLineDwRdiDetPortn = _Pmc1002AlmLineDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1, 3),
    _Pmc1002AlmLineDwRdiDetPortn_Type()
)
pmc1002AlmLineDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDwRdiDetPortn.setStatus("current")
_Pmc1002AlmLineDwOofPortn_Type = EkiOnOff
_Pmc1002AlmLineDwOofPortn_Object = MibTableColumn
pmc1002AlmLineDwOofPortn = _Pmc1002AlmLineDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1, 4),
    _Pmc1002AlmLineDwOofPortn_Type()
)
pmc1002AlmLineDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDwOofPortn.setStatus("current")
_Pmc1002AlmLineDwLofPortn_Type = EkiOnOff
_Pmc1002AlmLineDwLofPortn_Object = MibTableColumn
pmc1002AlmLineDwLofPortn = _Pmc1002AlmLineDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1, 5),
    _Pmc1002AlmLineDwLofPortn_Type()
)
pmc1002AlmLineDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDwLofPortn.setStatus("current")
_Pmc1002AlmLineFecFailPortn_Type = EkiOnOff
_Pmc1002AlmLineFecFailPortn_Object = MibTableColumn
pmc1002AlmLineFecFailPortn = _Pmc1002AlmLineFecFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 128, 1, 6),
    _Pmc1002AlmLineFecFailPortn_Type()
)
pmc1002AlmLineFecFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineFecFailPortn.setStatus("current")
_Pmc1002AlmlineSyncAlarmsTable_Object = MibTable
pmc1002AlmlineSyncAlarmsTable = _Pmc1002AlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineSyncAlarmsTable.setStatus("current")
_Pmc1002AlmlineSyncAlarmsEntry_Object = MibTableRow
pmc1002AlmlineSyncAlarmsEntry = _Pmc1002AlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 133, 1)
)
pmc1002AlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineSyncAlarmsEntry.setStatus("current")


class _Pmc1002AlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pmc1002AlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineSyncAlarmsIndex_Object = MibTableColumn
pmc1002AlmlineSyncAlarmsIndex = _Pmc1002AlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 133, 1, 1),
    _Pmc1002AlmlineSyncAlarmsIndex_Type()
)
pmc1002AlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineSyncAlarmsIndex.setStatus("current")
_Pmc1002AlmLineDwLockerrPortn_Type = EkiOnOff
_Pmc1002AlmLineDwLockerrPortn_Object = MibTableColumn
pmc1002AlmLineDwLockerrPortn = _Pmc1002AlmLineDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 133, 1, 13),
    _Pmc1002AlmLineDwLockerrPortn_Type()
)
pmc1002AlmLineDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDwLockerrPortn.setStatus("current")
_Pmc1002AlmLineUpLockerrPortn_Type = EkiOnOff
_Pmc1002AlmLineUpLockerrPortn_Object = MibTableColumn
pmc1002AlmLineUpLockerrPortn = _Pmc1002AlmLineUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 133, 1, 14),
    _Pmc1002AlmLineUpLockerrPortn_Type()
)
pmc1002AlmLineUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineUpLockerrPortn.setStatus("current")
_Pmc1002AlmLineDwLosPortn_Type = EkiOnOff
_Pmc1002AlmLineDwLosPortn_Object = MibTableColumn
pmc1002AlmLineDwLosPortn = _Pmc1002AlmLineDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 133, 1, 17),
    _Pmc1002AlmLineDwLosPortn_Type()
)
pmc1002AlmLineDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineDwLosPortn.setStatus("current")
_Pmc1002AlmlineXfp1AlarmsTable_Object = MibTable
pmc1002AlmlineXfp1AlarmsTable = _Pmc1002AlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1AlarmsTable.setStatus("current")
_Pmc1002AlmlineXfp1AlarmsEntry_Object = MibTableRow
pmc1002AlmlineXfp1AlarmsEntry = _Pmc1002AlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1)
)
pmc1002AlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002AlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1AlarmsEntry.setStatus("current")


class _Pmc1002AlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pmc1002AlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002AlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pmc1002AlmlineXfp1AlarmsIndex_Object = MibTableColumn
pmc1002AlmlineXfp1AlarmsIndex = _Pmc1002AlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 1),
    _Pmc1002AlmlineXfp1AlarmsIndex_Type()
)
pmc1002AlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmlineXfp1AlarmsIndex.setStatus("current")
_Pmc1002AlmLineModNrPortn_Type = EkiOnOff
_Pmc1002AlmLineModNrPortn_Object = MibTableColumn
pmc1002AlmLineModNrPortn = _Pmc1002AlmLineModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 3),
    _Pmc1002AlmLineModNrPortn_Type()
)
pmc1002AlmLineModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineModNrPortn.setStatus("current")
_Pmc1002AlmLineRxCdrNotLockedPortn_Type = EkiOnOff
_Pmc1002AlmLineRxCdrNotLockedPortn_Object = MibTableColumn
pmc1002AlmLineRxCdrNotLockedPortn = _Pmc1002AlmLineRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 4),
    _Pmc1002AlmLineRxCdrNotLockedPortn_Type()
)
pmc1002AlmLineRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineRxCdrNotLockedPortn.setStatus("current")
_Pmc1002AlmLineRxNrPortn_Type = EkiOnOff
_Pmc1002AlmLineRxNrPortn_Object = MibTableColumn
pmc1002AlmLineRxNrPortn = _Pmc1002AlmLineRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 6),
    _Pmc1002AlmLineRxNrPortn_Type()
)
pmc1002AlmLineRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineRxNrPortn.setStatus("current")
_Pmc1002AlmLineTxCdrNotLockedPortn_Type = EkiOnOff
_Pmc1002AlmLineTxCdrNotLockedPortn_Object = MibTableColumn
pmc1002AlmLineTxCdrNotLockedPortn = _Pmc1002AlmLineTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 7),
    _Pmc1002AlmLineTxCdrNotLockedPortn_Type()
)
pmc1002AlmLineTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxCdrNotLockedPortn.setStatus("current")
_Pmc1002AlmLineTxFaultPortn_Type = EkiOnOff
_Pmc1002AlmLineTxFaultPortn_Object = MibTableColumn
pmc1002AlmLineTxFaultPortn = _Pmc1002AlmLineTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 8),
    _Pmc1002AlmLineTxFaultPortn_Type()
)
pmc1002AlmLineTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxFaultPortn.setStatus("current")
_Pmc1002AlmLineTxNrPortn_Type = EkiOnOff
_Pmc1002AlmLineTxNrPortn_Object = MibTableColumn
pmc1002AlmLineTxNrPortn = _Pmc1002AlmLineTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 9),
    _Pmc1002AlmLineTxNrPortn_Type()
)
pmc1002AlmLineTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTxNrPortn.setStatus("current")
_Pmc1002AlmLineChannelNotAcquiredPortn_Type = EkiOnOff
_Pmc1002AlmLineChannelNotAcquiredPortn_Object = MibTableColumn
pmc1002AlmLineChannelNotAcquiredPortn = _Pmc1002AlmLineChannelNotAcquiredPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 11),
    _Pmc1002AlmLineChannelNotAcquiredPortn_Type()
)
pmc1002AlmLineChannelNotAcquiredPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineChannelNotAcquiredPortn.setStatus("current")
_Pmc1002AlmLineWavelengthUnlockedPortn_Type = EkiOnOff
_Pmc1002AlmLineWavelengthUnlockedPortn_Object = MibTableColumn
pmc1002AlmLineWavelengthUnlockedPortn = _Pmc1002AlmLineWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 15),
    _Pmc1002AlmLineWavelengthUnlockedPortn_Type()
)
pmc1002AlmLineWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineWavelengthUnlockedPortn.setStatus("current")
_Pmc1002AlmLineTecFaultPortn_Type = EkiOnOff
_Pmc1002AlmLineTecFaultPortn_Object = MibTableColumn
pmc1002AlmLineTecFaultPortn = _Pmc1002AlmLineTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 16),
    _Pmc1002AlmLineTecFaultPortn_Type()
)
pmc1002AlmLineTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineTecFaultPortn.setStatus("current")
_Pmc1002AlmLineApdSupplyFaultPortn_Type = EkiOnOff
_Pmc1002AlmLineApdSupplyFaultPortn_Object = MibTableColumn
pmc1002AlmLineApdSupplyFaultPortn = _Pmc1002AlmLineApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 2, 3, 3, 211, 1, 17),
    _Pmc1002AlmLineApdSupplyFaultPortn_Type()
)
pmc1002AlmLineApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002AlmLineApdSupplyFaultPortn.setStatus("current")
_Pmc1002measures_ObjectIdentity = ObjectIdentity
pmc1002measures = _Pmc1002measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3)
)
_Pmc1002MesrOther_ObjectIdentity = ObjectIdentity
pmc1002MesrOther = _Pmc1002MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 1)
)
_Pmc1002Mesrsynth0_Type = EkiMeasureType
_Pmc1002Mesrsynth0_Object = MibScalar
pmc1002Mesrsynth0 = _Pmc1002Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 1, 0),
    _Pmc1002Mesrsynth0_Type()
)
pmc1002Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrsynth0.setStatus("deprecated")
_Pmc1002Mesrsynth1_Type = EkiMeasureType
_Pmc1002Mesrsynth1_Object = MibScalar
pmc1002Mesrsynth1 = _Pmc1002Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 1, 1),
    _Pmc1002Mesrsynth1_Type()
)
pmc1002Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrsynth1.setStatus("deprecated")
_Pmc1002MesrClient_ObjectIdentity = ObjectIdentity
pmc1002MesrClient = _Pmc1002MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2)
)
_Pmc1002MesrclientModTempMeasTable_Object = MibTable
pmc1002MesrclientModTempMeasTable = _Pmc1002MesrclientModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1002MesrclientModTempMeasTable.setStatus("current")
_Pmc1002MesrclientModTempMeasEntry_Object = MibTableRow
pmc1002MesrclientModTempMeasEntry = _Pmc1002MesrclientModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 16, 1)
)
pmc1002MesrclientModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MesrclientModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MesrclientModTempMeasEntry.setStatus("current")


class _Pmc1002MesrclientModTempMeasIndex_Type(Integer32):
    """Custom type pmc1002MesrclientModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MesrclientModTempMeasIndex_Type.__name__ = "Integer32"
_Pmc1002MesrclientModTempMeasIndex_Object = MibTableColumn
pmc1002MesrclientModTempMeasIndex = _Pmc1002MesrclientModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 16, 1, 1),
    _Pmc1002MesrclientModTempMeasIndex_Type()
)
pmc1002MesrclientModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientModTempMeasIndex.setStatus("current")


class _Pmc1002MesrclientModTempMeasPortn_Type(Integer32):
    """Custom type pmc1002MesrclientModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002MesrclientModTempMeasPortn_Type.__name__ = "Integer32"
_Pmc1002MesrclientModTempMeasPortn_Object = MibTableColumn
pmc1002MesrclientModTempMeasPortn = _Pmc1002MesrclientModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 16, 1, 2),
    _Pmc1002MesrclientModTempMeasPortn_Type()
)
pmc1002MesrclientModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientModTempMeasPortn.setStatus("current")
_Pmc1002MesrclientBiasCurrentMeasTable_Object = MibTable
pmc1002MesrclientBiasCurrentMeasTable = _Pmc1002MesrclientBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1002MesrclientBiasCurrentMeasTable.setStatus("current")
_Pmc1002MesrclientBiasCurrentMeasEntry_Object = MibTableRow
pmc1002MesrclientBiasCurrentMeasEntry = _Pmc1002MesrclientBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 32, 1)
)
pmc1002MesrclientBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MesrclientBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MesrclientBiasCurrentMeasEntry.setStatus("current")


class _Pmc1002MesrclientBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pmc1002MesrclientBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MesrclientBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pmc1002MesrclientBiasCurrentMeasIndex_Object = MibTableColumn
pmc1002MesrclientBiasCurrentMeasIndex = _Pmc1002MesrclientBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 32, 1, 1),
    _Pmc1002MesrclientBiasCurrentMeasIndex_Type()
)
pmc1002MesrclientBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientBiasCurrentMeasIndex.setStatus("current")


class _Pmc1002MesrclientBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pmc1002MesrclientBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002MesrclientBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pmc1002MesrclientBiasCurrentMeasPortn_Object = MibTableColumn
pmc1002MesrclientBiasCurrentMeasPortn = _Pmc1002MesrclientBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 32, 1, 2),
    _Pmc1002MesrclientBiasCurrentMeasPortn_Type()
)
pmc1002MesrclientBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientBiasCurrentMeasPortn.setStatus("current")
_Pmc1002MesrclientTxPowerMeasTable_Object = MibTable
pmc1002MesrclientTxPowerMeasTable = _Pmc1002MesrclientTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pmc1002MesrclientTxPowerMeasTable.setStatus("current")
_Pmc1002MesrclientTxPowerMeasEntry_Object = MibTableRow
pmc1002MesrclientTxPowerMeasEntry = _Pmc1002MesrclientTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 40, 1)
)
pmc1002MesrclientTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MesrclientTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MesrclientTxPowerMeasEntry.setStatus("current")


class _Pmc1002MesrclientTxPowerMeasIndex_Type(Integer32):
    """Custom type pmc1002MesrclientTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MesrclientTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc1002MesrclientTxPowerMeasIndex_Object = MibTableColumn
pmc1002MesrclientTxPowerMeasIndex = _Pmc1002MesrclientTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 40, 1, 1),
    _Pmc1002MesrclientTxPowerMeasIndex_Type()
)
pmc1002MesrclientTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientTxPowerMeasIndex.setStatus("current")


class _Pmc1002MesrclientTxPowerMeasPortn_Type(Integer32):
    """Custom type pmc1002MesrclientTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002MesrclientTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc1002MesrclientTxPowerMeasPortn_Object = MibTableColumn
pmc1002MesrclientTxPowerMeasPortn = _Pmc1002MesrclientTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 40, 1, 2),
    _Pmc1002MesrclientTxPowerMeasPortn_Type()
)
pmc1002MesrclientTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientTxPowerMeasPortn.setStatus("current")
_Pmc1002MesrclientRxPowerMeasTable_Object = MibTable
pmc1002MesrclientRxPowerMeasTable = _Pmc1002MesrclientRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pmc1002MesrclientRxPowerMeasTable.setStatus("current")
_Pmc1002MesrclientRxPowerMeasEntry_Object = MibTableRow
pmc1002MesrclientRxPowerMeasEntry = _Pmc1002MesrclientRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 48, 1)
)
pmc1002MesrclientRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MesrclientRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MesrclientRxPowerMeasEntry.setStatus("current")


class _Pmc1002MesrclientRxPowerMeasIndex_Type(Integer32):
    """Custom type pmc1002MesrclientRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MesrclientRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc1002MesrclientRxPowerMeasIndex_Object = MibTableColumn
pmc1002MesrclientRxPowerMeasIndex = _Pmc1002MesrclientRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 48, 1, 1),
    _Pmc1002MesrclientRxPowerMeasIndex_Type()
)
pmc1002MesrclientRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientRxPowerMeasIndex.setStatus("current")


class _Pmc1002MesrclientRxPowerMeasPortn_Type(Integer32):
    """Custom type pmc1002MesrclientRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002MesrclientRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc1002MesrclientRxPowerMeasPortn_Object = MibTableColumn
pmc1002MesrclientRxPowerMeasPortn = _Pmc1002MesrclientRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 2, 48, 1, 2),
    _Pmc1002MesrclientRxPowerMeasPortn_Type()
)
pmc1002MesrclientRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MesrclientRxPowerMeasPortn.setStatus("current")
_Pmc1002MesrLine_ObjectIdentity = ObjectIdentity
pmc1002MesrLine = _Pmc1002MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3)
)
_Pmc1002Mesrline1ModTempMeasTable_Object = MibTable
pmc1002Mesrline1ModTempMeasTable = _Pmc1002Mesrline1ModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1ModTempMeasTable.setStatus("current")
_Pmc1002Mesrline1ModTempMeasEntry_Object = MibTableRow
pmc1002Mesrline1ModTempMeasEntry = _Pmc1002Mesrline1ModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 208, 1)
)
pmc1002Mesrline1ModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1ModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1ModTempMeasEntry.setStatus("current")


class _Pmc1002Mesrline1ModTempMeasIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1ModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1ModTempMeasIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1ModTempMeasIndex_Object = MibTableColumn
pmc1002Mesrline1ModTempMeasIndex = _Pmc1002Mesrline1ModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 208, 1, 1),
    _Pmc1002Mesrline1ModTempMeasIndex_Type()
)
pmc1002Mesrline1ModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1ModTempMeasIndex.setStatus("current")


class _Pmc1002Mesrline1ModTempMeasPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1ModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1ModTempMeasPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1ModTempMeasPortn_Object = MibTableColumn
pmc1002Mesrline1ModTempMeasPortn = _Pmc1002Mesrline1ModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 208, 1, 2),
    _Pmc1002Mesrline1ModTempMeasPortn_Type()
)
pmc1002Mesrline1ModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1ModTempMeasPortn.setStatus("current")
_Pmc1002Mesrline1ReservedTable_Object = MibTable
pmc1002Mesrline1ReservedTable = _Pmc1002Mesrline1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1ReservedTable.setStatus("deprecated")
_Pmc1002Mesrline1ReservedEntry_Object = MibTableRow
pmc1002Mesrline1ReservedEntry = _Pmc1002Mesrline1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 209, 1)
)
pmc1002Mesrline1ReservedEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1ReservedEntry.setStatus("deprecated")


class _Pmc1002Mesrline1ReservedIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1ReservedIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1ReservedIndex_Object = MibTableColumn
pmc1002Mesrline1ReservedIndex = _Pmc1002Mesrline1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 209, 1, 1),
    _Pmc1002Mesrline1ReservedIndex_Type()
)
pmc1002Mesrline1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1ReservedIndex.setStatus("deprecated")


class _Pmc1002Mesrline1ReservedPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1ReservedPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1ReservedPortn_Object = MibTableColumn
pmc1002Mesrline1ReservedPortn = _Pmc1002Mesrline1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 209, 1, 2),
    _Pmc1002Mesrline1ReservedPortn_Type()
)
pmc1002Mesrline1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1ReservedPortn.setStatus("deprecated")
_Pmc1002Mesrline1BiasCurrentMeasTable_Object = MibTable
pmc1002Mesrline1BiasCurrentMeasTable = _Pmc1002Mesrline1BiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1BiasCurrentMeasTable.setStatus("current")
_Pmc1002Mesrline1BiasCurrentMeasEntry_Object = MibTableRow
pmc1002Mesrline1BiasCurrentMeasEntry = _Pmc1002Mesrline1BiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 210, 1)
)
pmc1002Mesrline1BiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1BiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1BiasCurrentMeasEntry.setStatus("current")


class _Pmc1002Mesrline1BiasCurrentMeasIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1BiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1BiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1BiasCurrentMeasIndex_Object = MibTableColumn
pmc1002Mesrline1BiasCurrentMeasIndex = _Pmc1002Mesrline1BiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 210, 1, 1),
    _Pmc1002Mesrline1BiasCurrentMeasIndex_Type()
)
pmc1002Mesrline1BiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1BiasCurrentMeasIndex.setStatus("current")


class _Pmc1002Mesrline1BiasCurrentMeasPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1BiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1BiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1BiasCurrentMeasPortn_Object = MibTableColumn
pmc1002Mesrline1BiasCurrentMeasPortn = _Pmc1002Mesrline1BiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 210, 1, 2),
    _Pmc1002Mesrline1BiasCurrentMeasPortn_Type()
)
pmc1002Mesrline1BiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1BiasCurrentMeasPortn.setStatus("current")
_Pmc1002Mesrline1TxPowerMeasTable_Object = MibTable
pmc1002Mesrline1TxPowerMeasTable = _Pmc1002Mesrline1TxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1TxPowerMeasTable.setStatus("current")
_Pmc1002Mesrline1TxPowerMeasEntry_Object = MibTableRow
pmc1002Mesrline1TxPowerMeasEntry = _Pmc1002Mesrline1TxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 211, 1)
)
pmc1002Mesrline1TxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1TxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1TxPowerMeasEntry.setStatus("current")


class _Pmc1002Mesrline1TxPowerMeasIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1TxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1TxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1TxPowerMeasIndex_Object = MibTableColumn
pmc1002Mesrline1TxPowerMeasIndex = _Pmc1002Mesrline1TxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 211, 1, 1),
    _Pmc1002Mesrline1TxPowerMeasIndex_Type()
)
pmc1002Mesrline1TxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1TxPowerMeasIndex.setStatus("current")


class _Pmc1002Mesrline1TxPowerMeasPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1TxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1TxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1TxPowerMeasPortn_Object = MibTableColumn
pmc1002Mesrline1TxPowerMeasPortn = _Pmc1002Mesrline1TxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 211, 1, 2),
    _Pmc1002Mesrline1TxPowerMeasPortn_Type()
)
pmc1002Mesrline1TxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1TxPowerMeasPortn.setStatus("current")
_Pmc1002Mesrline1RxPowerMeasTable_Object = MibTable
pmc1002Mesrline1RxPowerMeasTable = _Pmc1002Mesrline1RxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1RxPowerMeasTable.setStatus("current")
_Pmc1002Mesrline1RxPowerMeasEntry_Object = MibTableRow
pmc1002Mesrline1RxPowerMeasEntry = _Pmc1002Mesrline1RxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 212, 1)
)
pmc1002Mesrline1RxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1RxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1RxPowerMeasEntry.setStatus("current")


class _Pmc1002Mesrline1RxPowerMeasIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1RxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1RxPowerMeasIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1RxPowerMeasIndex_Object = MibTableColumn
pmc1002Mesrline1RxPowerMeasIndex = _Pmc1002Mesrline1RxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 212, 1, 1),
    _Pmc1002Mesrline1RxPowerMeasIndex_Type()
)
pmc1002Mesrline1RxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1RxPowerMeasIndex.setStatus("current")


class _Pmc1002Mesrline1RxPowerMeasPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1RxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1RxPowerMeasPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1RxPowerMeasPortn_Object = MibTableColumn
pmc1002Mesrline1RxPowerMeasPortn = _Pmc1002Mesrline1RxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 212, 1, 2),
    _Pmc1002Mesrline1RxPowerMeasPortn_Type()
)
pmc1002Mesrline1RxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1RxPowerMeasPortn.setStatus("current")
_Pmc1002Mesrline1Aux1MeasTable_Object = MibTable
pmc1002Mesrline1Aux1MeasTable = _Pmc1002Mesrline1Aux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux1MeasTable.setStatus("deprecated")
_Pmc1002Mesrline1Aux1MeasEntry_Object = MibTableRow
pmc1002Mesrline1Aux1MeasEntry = _Pmc1002Mesrline1Aux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 213, 1)
)
pmc1002Mesrline1Aux1MeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1Aux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux1MeasEntry.setStatus("deprecated")


class _Pmc1002Mesrline1Aux1MeasIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1Aux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1Aux1MeasIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1Aux1MeasIndex_Object = MibTableColumn
pmc1002Mesrline1Aux1MeasIndex = _Pmc1002Mesrline1Aux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 213, 1, 1),
    _Pmc1002Mesrline1Aux1MeasIndex_Type()
)
pmc1002Mesrline1Aux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux1MeasIndex.setStatus("deprecated")


class _Pmc1002Mesrline1Aux1MeasPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1Aux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1Aux1MeasPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1Aux1MeasPortn_Object = MibTableColumn
pmc1002Mesrline1Aux1MeasPortn = _Pmc1002Mesrline1Aux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 213, 1, 2),
    _Pmc1002Mesrline1Aux1MeasPortn_Type()
)
pmc1002Mesrline1Aux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux1MeasPortn.setStatus("deprecated")
_Pmc1002Mesrline1Aux2MeasTable_Object = MibTable
pmc1002Mesrline1Aux2MeasTable = _Pmc1002Mesrline1Aux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux2MeasTable.setStatus("deprecated")
_Pmc1002Mesrline1Aux2MeasEntry_Object = MibTableRow
pmc1002Mesrline1Aux2MeasEntry = _Pmc1002Mesrline1Aux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 214, 1)
)
pmc1002Mesrline1Aux2MeasEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1Aux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux2MeasEntry.setStatus("deprecated")


class _Pmc1002Mesrline1Aux2MeasIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1Aux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1Aux2MeasIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1Aux2MeasIndex_Object = MibTableColumn
pmc1002Mesrline1Aux2MeasIndex = _Pmc1002Mesrline1Aux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 214, 1, 1),
    _Pmc1002Mesrline1Aux2MeasIndex_Type()
)
pmc1002Mesrline1Aux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux2MeasIndex.setStatus("deprecated")


class _Pmc1002Mesrline1Aux2MeasPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1Aux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1Aux2MeasPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1Aux2MeasPortn_Object = MibTableColumn
pmc1002Mesrline1Aux2MeasPortn = _Pmc1002Mesrline1Aux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 214, 1, 2),
    _Pmc1002Mesrline1Aux2MeasPortn_Type()
)
pmc1002Mesrline1Aux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1Aux2MeasPortn.setStatus("deprecated")
_Pmc1002Mesrline1AgingTable_Object = MibTable
pmc1002Mesrline1AgingTable = _Pmc1002Mesrline1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1AgingTable.setStatus("current")
_Pmc1002Mesrline1AgingEntry_Object = MibTableRow
pmc1002Mesrline1AgingEntry = _Pmc1002Mesrline1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 224, 1)
)
pmc1002Mesrline1AgingEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1AgingIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1AgingEntry.setStatus("current")


class _Pmc1002Mesrline1AgingIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1AgingIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1AgingIndex_Object = MibTableColumn
pmc1002Mesrline1AgingIndex = _Pmc1002Mesrline1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 224, 1, 1),
    _Pmc1002Mesrline1AgingIndex_Type()
)
pmc1002Mesrline1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1AgingIndex.setStatus("current")


class _Pmc1002Mesrline1AgingPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1AgingPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1AgingPortn_Object = MibTableColumn
pmc1002Mesrline1AgingPortn = _Pmc1002Mesrline1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 224, 1, 2),
    _Pmc1002Mesrline1AgingPortn_Type()
)
pmc1002Mesrline1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1AgingPortn.setStatus("current")
_Pmc1002Mesrline1LaserTemperatureTable_Object = MibTable
pmc1002Mesrline1LaserTemperatureTable = _Pmc1002Mesrline1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserTemperatureTable.setStatus("deprecated")
_Pmc1002Mesrline1LaserTemperatureEntry_Object = MibTableRow
pmc1002Mesrline1LaserTemperatureEntry = _Pmc1002Mesrline1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 225, 1)
)
pmc1002Mesrline1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserTemperatureEntry.setStatus("deprecated")


class _Pmc1002Mesrline1LaserTemperatureIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1LaserTemperatureIndex_Object = MibTableColumn
pmc1002Mesrline1LaserTemperatureIndex = _Pmc1002Mesrline1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 225, 1, 1),
    _Pmc1002Mesrline1LaserTemperatureIndex_Type()
)
pmc1002Mesrline1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserTemperatureIndex.setStatus("deprecated")


class _Pmc1002Mesrline1LaserTemperaturePortn_Type(Integer32):
    """Custom type pmc1002Mesrline1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1LaserTemperaturePortn_Object = MibTableColumn
pmc1002Mesrline1LaserTemperaturePortn = _Pmc1002Mesrline1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 225, 1, 2),
    _Pmc1002Mesrline1LaserTemperaturePortn_Type()
)
pmc1002Mesrline1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserTemperaturePortn.setStatus("deprecated")
_Pmc1002Mesrline1FreqDeviationTable_Object = MibTable
pmc1002Mesrline1FreqDeviationTable = _Pmc1002Mesrline1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1FreqDeviationTable.setStatus("current")
_Pmc1002Mesrline1FreqDeviationEntry_Object = MibTableRow
pmc1002Mesrline1FreqDeviationEntry = _Pmc1002Mesrline1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 226, 1)
)
pmc1002Mesrline1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1FreqDeviationEntry.setStatus("current")


class _Pmc1002Mesrline1FreqDeviationIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1FreqDeviationIndex_Object = MibTableColumn
pmc1002Mesrline1FreqDeviationIndex = _Pmc1002Mesrline1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 226, 1, 1),
    _Pmc1002Mesrline1FreqDeviationIndex_Type()
)
pmc1002Mesrline1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1FreqDeviationIndex.setStatus("current")


class _Pmc1002Mesrline1FreqDeviationPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1FreqDeviationPortn_Object = MibTableColumn
pmc1002Mesrline1FreqDeviationPortn = _Pmc1002Mesrline1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 226, 1, 2),
    _Pmc1002Mesrline1FreqDeviationPortn_Type()
)
pmc1002Mesrline1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1FreqDeviationPortn.setStatus("current")
_Pmc1002Mesrline1LaserWvlengthTable_Object = MibTable
pmc1002Mesrline1LaserWvlengthTable = _Pmc1002Mesrline1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserWvlengthTable.setStatus("current")
_Pmc1002Mesrline1LaserWvlengthEntry_Object = MibTableRow
pmc1002Mesrline1LaserWvlengthEntry = _Pmc1002Mesrline1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 227, 1)
)
pmc1002Mesrline1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002Mesrline1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserWvlengthEntry.setStatus("current")


class _Pmc1002Mesrline1LaserWvlengthIndex_Type(Integer32):
    """Custom type pmc1002Mesrline1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002Mesrline1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pmc1002Mesrline1LaserWvlengthIndex_Object = MibTableColumn
pmc1002Mesrline1LaserWvlengthIndex = _Pmc1002Mesrline1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 227, 1, 1),
    _Pmc1002Mesrline1LaserWvlengthIndex_Type()
)
pmc1002Mesrline1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserWvlengthIndex.setStatus("current")


class _Pmc1002Mesrline1LaserWvlengthPortn_Type(Integer32):
    """Custom type pmc1002Mesrline1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pmc1002Mesrline1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pmc1002Mesrline1LaserWvlengthPortn_Object = MibTableColumn
pmc1002Mesrline1LaserWvlengthPortn = _Pmc1002Mesrline1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 3, 3, 227, 1, 2),
    _Pmc1002Mesrline1LaserWvlengthPortn_Type()
)
pmc1002Mesrline1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002Mesrline1LaserWvlengthPortn.setStatus("current")
_Pmc1002counters_ObjectIdentity = ObjectIdentity
pmc1002counters = _Pmc1002counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4)
)
_Pmc1002CntOther_ObjectIdentity = ObjectIdentity
pmc1002CntOther = _Pmc1002CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 1)
)
_Pmc1002CntClient_ObjectIdentity = ObjectIdentity
pmc1002CntClient = _Pmc1002CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2)
)
_Pmc1002CntclientUpErrCntTable_Object = MibTable
pmc1002CntclientUpErrCntTable = _Pmc1002CntclientUpErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1002CntclientUpErrCntTable.setStatus("current")
_Pmc1002CntclientUpErrCntEntry_Object = MibTableRow
pmc1002CntclientUpErrCntEntry = _Pmc1002CntclientUpErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 32, 1)
)
pmc1002CntclientUpErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntclientUpErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntclientUpErrCntEntry.setStatus("current")


class _Pmc1002CntclientUpErrCntIndex_Type(Integer32):
    """Custom type pmc1002CntclientUpErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntclientUpErrCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntclientUpErrCntIndex_Object = MibTableColumn
pmc1002CntclientUpErrCntIndex = _Pmc1002CntclientUpErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 32, 1, 1),
    _Pmc1002CntclientUpErrCntIndex_Type()
)
pmc1002CntclientUpErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpErrCntIndex.setStatus("current")
_Pmc1002CntclientUpErrCntValuePortn_Type = Counter32
_Pmc1002CntclientUpErrCntValuePortn_Object = MibTableColumn
pmc1002CntclientUpErrCntValuePortn = _Pmc1002CntclientUpErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 32, 1, 2),
    _Pmc1002CntclientUpErrCntValuePortn_Type()
)
pmc1002CntclientUpErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpErrCntValuePortn.setStatus("current")
_Pmc1002CntclientUpErrCntErrorPortn_Type = EkiOnOff
_Pmc1002CntclientUpErrCntErrorPortn_Object = MibTableColumn
pmc1002CntclientUpErrCntErrorPortn = _Pmc1002CntclientUpErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 32, 1, 3),
    _Pmc1002CntclientUpErrCntErrorPortn_Type()
)
pmc1002CntclientUpErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpErrCntErrorPortn.setStatus("current")
_Pmc1002CntclientUpErrCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntclientUpErrCntOverloadPortn_Object = MibTableColumn
pmc1002CntclientUpErrCntOverloadPortn = _Pmc1002CntclientUpErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 32, 1, 4),
    _Pmc1002CntclientUpErrCntOverloadPortn_Type()
)
pmc1002CntclientUpErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpErrCntOverloadPortn.setStatus("current")
_Pmc1002CntclientUpTimCntTable_Object = MibTable
pmc1002CntclientUpTimCntTable = _Pmc1002CntclientUpTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pmc1002CntclientUpTimCntTable.setStatus("current")
_Pmc1002CntclientUpTimCntEntry_Object = MibTableRow
pmc1002CntclientUpTimCntEntry = _Pmc1002CntclientUpTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 40, 1)
)
pmc1002CntclientUpTimCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntclientUpTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntclientUpTimCntEntry.setStatus("current")


class _Pmc1002CntclientUpTimCntIndex_Type(Integer32):
    """Custom type pmc1002CntclientUpTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntclientUpTimCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntclientUpTimCntIndex_Object = MibTableColumn
pmc1002CntclientUpTimCntIndex = _Pmc1002CntclientUpTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 40, 1, 1),
    _Pmc1002CntclientUpTimCntIndex_Type()
)
pmc1002CntclientUpTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpTimCntIndex.setStatus("current")
_Pmc1002CntclientUpTimCntValuePortn_Type = Counter32
_Pmc1002CntclientUpTimCntValuePortn_Object = MibTableColumn
pmc1002CntclientUpTimCntValuePortn = _Pmc1002CntclientUpTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 40, 1, 2),
    _Pmc1002CntclientUpTimCntValuePortn_Type()
)
pmc1002CntclientUpTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpTimCntValuePortn.setStatus("current")
_Pmc1002CntclientUpTimCntErrorPortn_Type = EkiOnOff
_Pmc1002CntclientUpTimCntErrorPortn_Object = MibTableColumn
pmc1002CntclientUpTimCntErrorPortn = _Pmc1002CntclientUpTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 40, 1, 3),
    _Pmc1002CntclientUpTimCntErrorPortn_Type()
)
pmc1002CntclientUpTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpTimCntErrorPortn.setStatus("current")
_Pmc1002CntclientUpTimCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntclientUpTimCntOverloadPortn_Object = MibTableColumn
pmc1002CntclientUpTimCntOverloadPortn = _Pmc1002CntclientUpTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 40, 1, 4),
    _Pmc1002CntclientUpTimCntOverloadPortn_Type()
)
pmc1002CntclientUpTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientUpTimCntOverloadPortn.setStatus("current")
_Pmc1002CntclientDwErrCntTable_Object = MibTable
pmc1002CntclientDwErrCntTable = _Pmc1002CntclientDwErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pmc1002CntclientDwErrCntTable.setStatus("current")
_Pmc1002CntclientDwErrCntEntry_Object = MibTableRow
pmc1002CntclientDwErrCntEntry = _Pmc1002CntclientDwErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 64, 1)
)
pmc1002CntclientDwErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntclientDwErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntclientDwErrCntEntry.setStatus("current")


class _Pmc1002CntclientDwErrCntIndex_Type(Integer32):
    """Custom type pmc1002CntclientDwErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntclientDwErrCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntclientDwErrCntIndex_Object = MibTableColumn
pmc1002CntclientDwErrCntIndex = _Pmc1002CntclientDwErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 64, 1, 1),
    _Pmc1002CntclientDwErrCntIndex_Type()
)
pmc1002CntclientDwErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwErrCntIndex.setStatus("current")
_Pmc1002CntclientDwErrCntValuePortn_Type = Counter32
_Pmc1002CntclientDwErrCntValuePortn_Object = MibTableColumn
pmc1002CntclientDwErrCntValuePortn = _Pmc1002CntclientDwErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 64, 1, 2),
    _Pmc1002CntclientDwErrCntValuePortn_Type()
)
pmc1002CntclientDwErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwErrCntValuePortn.setStatus("current")
_Pmc1002CntclientDwErrCntErrorPortn_Type = EkiOnOff
_Pmc1002CntclientDwErrCntErrorPortn_Object = MibTableColumn
pmc1002CntclientDwErrCntErrorPortn = _Pmc1002CntclientDwErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 64, 1, 3),
    _Pmc1002CntclientDwErrCntErrorPortn_Type()
)
pmc1002CntclientDwErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwErrCntErrorPortn.setStatus("current")
_Pmc1002CntclientDwErrCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntclientDwErrCntOverloadPortn_Object = MibTableColumn
pmc1002CntclientDwErrCntOverloadPortn = _Pmc1002CntclientDwErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 64, 1, 4),
    _Pmc1002CntclientDwErrCntOverloadPortn_Type()
)
pmc1002CntclientDwErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwErrCntOverloadPortn.setStatus("current")
_Pmc1002CntclientDwTimCntTable_Object = MibTable
pmc1002CntclientDwTimCntTable = _Pmc1002CntclientDwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pmc1002CntclientDwTimCntTable.setStatus("current")
_Pmc1002CntclientDwTimCntEntry_Object = MibTableRow
pmc1002CntclientDwTimCntEntry = _Pmc1002CntclientDwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 72, 1)
)
pmc1002CntclientDwTimCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntclientDwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntclientDwTimCntEntry.setStatus("current")


class _Pmc1002CntclientDwTimCntIndex_Type(Integer32):
    """Custom type pmc1002CntclientDwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntclientDwTimCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntclientDwTimCntIndex_Object = MibTableColumn
pmc1002CntclientDwTimCntIndex = _Pmc1002CntclientDwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 72, 1, 1),
    _Pmc1002CntclientDwTimCntIndex_Type()
)
pmc1002CntclientDwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwTimCntIndex.setStatus("current")
_Pmc1002CntclientDwTimCntValuePortn_Type = Counter32
_Pmc1002CntclientDwTimCntValuePortn_Object = MibTableColumn
pmc1002CntclientDwTimCntValuePortn = _Pmc1002CntclientDwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 72, 1, 2),
    _Pmc1002CntclientDwTimCntValuePortn_Type()
)
pmc1002CntclientDwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwTimCntValuePortn.setStatus("current")
_Pmc1002CntclientDwTimCntErrorPortn_Type = EkiOnOff
_Pmc1002CntclientDwTimCntErrorPortn_Object = MibTableColumn
pmc1002CntclientDwTimCntErrorPortn = _Pmc1002CntclientDwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 72, 1, 3),
    _Pmc1002CntclientDwTimCntErrorPortn_Type()
)
pmc1002CntclientDwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwTimCntErrorPortn.setStatus("current")
_Pmc1002CntclientDwTimCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntclientDwTimCntOverloadPortn_Object = MibTableColumn
pmc1002CntclientDwTimCntOverloadPortn = _Pmc1002CntclientDwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 2, 72, 1, 4),
    _Pmc1002CntclientDwTimCntOverloadPortn_Type()
)
pmc1002CntclientDwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntclientDwTimCntOverloadPortn.setStatus("current")
_Pmc1002CntLine_ObjectIdentity = ObjectIdentity
pmc1002CntLine = _Pmc1002CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3)
)
_Pmc1002CntlineDfrmErrCntTable_Object = MibTable
pmc1002CntlineDfrmErrCntTable = _Pmc1002CntlineDfrmErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmErrCntTable.setStatus("current")
_Pmc1002CntlineDfrmErrCntEntry_Object = MibTableRow
pmc1002CntlineDfrmErrCntEntry = _Pmc1002CntlineDfrmErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 152, 1)
)
pmc1002CntlineDfrmErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntlineDfrmErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmErrCntEntry.setStatus("current")


class _Pmc1002CntlineDfrmErrCntIndex_Type(Integer32):
    """Custom type pmc1002CntlineDfrmErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntlineDfrmErrCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntlineDfrmErrCntIndex_Object = MibTableColumn
pmc1002CntlineDfrmErrCntIndex = _Pmc1002CntlineDfrmErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 152, 1, 1),
    _Pmc1002CntlineDfrmErrCntIndex_Type()
)
pmc1002CntlineDfrmErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmErrCntIndex.setStatus("current")
_Pmc1002CntlineDfrmErrCntValuePortn_Type = Counter32
_Pmc1002CntlineDfrmErrCntValuePortn_Object = MibTableColumn
pmc1002CntlineDfrmErrCntValuePortn = _Pmc1002CntlineDfrmErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 152, 1, 2),
    _Pmc1002CntlineDfrmErrCntValuePortn_Type()
)
pmc1002CntlineDfrmErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmErrCntValuePortn.setStatus("current")
_Pmc1002CntlineDfrmErrCntErrorPortn_Type = EkiOnOff
_Pmc1002CntlineDfrmErrCntErrorPortn_Object = MibTableColumn
pmc1002CntlineDfrmErrCntErrorPortn = _Pmc1002CntlineDfrmErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 152, 1, 3),
    _Pmc1002CntlineDfrmErrCntErrorPortn_Type()
)
pmc1002CntlineDfrmErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmErrCntErrorPortn.setStatus("current")
_Pmc1002CntlineDfrmErrCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntlineDfrmErrCntOverloadPortn_Object = MibTableColumn
pmc1002CntlineDfrmErrCntOverloadPortn = _Pmc1002CntlineDfrmErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 152, 1, 4),
    _Pmc1002CntlineDfrmErrCntOverloadPortn_Type()
)
pmc1002CntlineDfrmErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmErrCntOverloadPortn.setStatus("current")
_Pmc1002CntlineDfrmTimCntTable_Object = MibTable
pmc1002CntlineDfrmTimCntTable = _Pmc1002CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmTimCntTable.setStatus("current")
_Pmc1002CntlineDfrmTimCntEntry_Object = MibTableRow
pmc1002CntlineDfrmTimCntEntry = _Pmc1002CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 153, 1)
)
pmc1002CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmTimCntEntry.setStatus("current")


class _Pmc1002CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pmc1002CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntlineDfrmTimCntIndex_Object = MibTableColumn
pmc1002CntlineDfrmTimCntIndex = _Pmc1002CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 153, 1, 1),
    _Pmc1002CntlineDfrmTimCntIndex_Type()
)
pmc1002CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmTimCntIndex.setStatus("current")
_Pmc1002CntlineDfrmTimCntValuePortn_Type = Counter32
_Pmc1002CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pmc1002CntlineDfrmTimCntValuePortn = _Pmc1002CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 153, 1, 2),
    _Pmc1002CntlineDfrmTimCntValuePortn_Type()
)
pmc1002CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmTimCntValuePortn.setStatus("current")
_Pmc1002CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pmc1002CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pmc1002CntlineDfrmTimCntErrorPortn = _Pmc1002CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 153, 1, 3),
    _Pmc1002CntlineDfrmTimCntErrorPortn_Type()
)
pmc1002CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pmc1002CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pmc1002CntlineDfrmTimCntOverloadPortn = _Pmc1002CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 153, 1, 4),
    _Pmc1002CntlineDfrmTimCntOverloadPortn_Type()
)
pmc1002CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pmc1002CntlineDfrmPrimErrCntTable_Object = MibTable
pmc1002CntlineDfrmPrimErrCntTable = _Pmc1002CntlineDfrmPrimErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmPrimErrCntTable.setStatus("current")
_Pmc1002CntlineDfrmPrimErrCntEntry_Object = MibTableRow
pmc1002CntlineDfrmPrimErrCntEntry = _Pmc1002CntlineDfrmPrimErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 154, 1)
)
pmc1002CntlineDfrmPrimErrCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CntlineDfrmPrimErrCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmPrimErrCntEntry.setStatus("current")


class _Pmc1002CntlineDfrmPrimErrCntIndex_Type(Integer32):
    """Custom type pmc1002CntlineDfrmPrimErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CntlineDfrmPrimErrCntIndex_Type.__name__ = "Integer32"
_Pmc1002CntlineDfrmPrimErrCntIndex_Object = MibTableColumn
pmc1002CntlineDfrmPrimErrCntIndex = _Pmc1002CntlineDfrmPrimErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 154, 1, 1),
    _Pmc1002CntlineDfrmPrimErrCntIndex_Type()
)
pmc1002CntlineDfrmPrimErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmPrimErrCntIndex.setStatus("current")
_Pmc1002CntlineDfrmPrimErrCntValuePortn_Type = Counter32
_Pmc1002CntlineDfrmPrimErrCntValuePortn_Object = MibTableColumn
pmc1002CntlineDfrmPrimErrCntValuePortn = _Pmc1002CntlineDfrmPrimErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 154, 1, 2),
    _Pmc1002CntlineDfrmPrimErrCntValuePortn_Type()
)
pmc1002CntlineDfrmPrimErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmPrimErrCntValuePortn.setStatus("current")
_Pmc1002CntlineDfrmPrimErrCntErrorPortn_Type = EkiOnOff
_Pmc1002CntlineDfrmPrimErrCntErrorPortn_Object = MibTableColumn
pmc1002CntlineDfrmPrimErrCntErrorPortn = _Pmc1002CntlineDfrmPrimErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 154, 1, 3),
    _Pmc1002CntlineDfrmPrimErrCntErrorPortn_Type()
)
pmc1002CntlineDfrmPrimErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmPrimErrCntErrorPortn.setStatus("current")
_Pmc1002CntlineDfrmPrimErrCntOverloadPortn_Type = EkiOnOff
_Pmc1002CntlineDfrmPrimErrCntOverloadPortn_Object = MibTableColumn
pmc1002CntlineDfrmPrimErrCntOverloadPortn = _Pmc1002CntlineDfrmPrimErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 3, 154, 1, 4),
    _Pmc1002CntlineDfrmPrimErrCntOverloadPortn_Type()
)
pmc1002CntlineDfrmPrimErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CntlineDfrmPrimErrCntOverloadPortn.setStatus("current")
_Pmc1002CntCountersReset_Type = EkiOnOff
_Pmc1002CntCountersReset_Object = MibScalar
pmc1002CntCountersReset = _Pmc1002CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 259),
    _Pmc1002CntCountersReset_Type()
)
pmc1002CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CntCountersReset.setStatus("current")
_Pmc1002CntCountersStop_Type = EkiOnOff
_Pmc1002CntCountersStop_Object = MibScalar
pmc1002CntCountersStop = _Pmc1002CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 4, 260),
    _Pmc1002CntCountersStop_Type()
)
pmc1002CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CntCountersStop.setStatus("current")
_Pmc1002controlsWrite_ObjectIdentity = ObjectIdentity
pmc1002controlsWrite = _Pmc1002controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6)
)
_Pmc1002CtrlOther_ObjectIdentity = ObjectIdentity
pmc1002CtrlOther = _Pmc1002CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1)
)
_Pmc1002CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pmc1002CtrlconfMgnt1 = _Pmc1002CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 1)
)
_Pmc1002CtrlConf1Load1_Type = EkiOnOff
_Pmc1002CtrlConf1Load1_Object = MibScalar
pmc1002CtrlConf1Load1 = _Pmc1002CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 1, 1),
    _Pmc1002CtrlConf1Load1_Type()
)
pmc1002CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlConf1Load1.setStatus("current")
_Pmc1002CtrlConf2Load1_Type = EkiOnOff
_Pmc1002CtrlConf2Load1_Object = MibScalar
pmc1002CtrlConf2Load1 = _Pmc1002CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 1, 2),
    _Pmc1002CtrlConf2Load1_Type()
)
pmc1002CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlConf2Load1.setStatus("current")
_Pmc1002CtrlConf2Flash1_Type = EkiOnOff
_Pmc1002CtrlConf2Flash1_Object = MibScalar
pmc1002CtrlConf2Flash1 = _Pmc1002CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 1, 10),
    _Pmc1002CtrlConf2Flash1_Type()
)
pmc1002CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlConf2Flash1.setStatus("current")
_Pmc1002CtrlConf2Clear1_Type = EkiOnOff
_Pmc1002CtrlConf2Clear1_Object = MibScalar
pmc1002CtrlConf2Clear1 = _Pmc1002CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 1, 14),
    _Pmc1002CtrlConf2Clear1_Type()
)
pmc1002CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlConf2Clear1.setStatus("current")
_Pmc1002Ctrlsynth4_ObjectIdentity = ObjectIdentity
pmc1002Ctrlsynth4 = _Pmc1002Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 4)
)
_Pmc1002CtrlCorrelatOn_Type = EkiOnOff
_Pmc1002CtrlCorrelatOn_Object = MibScalar
pmc1002CtrlCorrelatOn = _Pmc1002CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 4, 1),
    _Pmc1002CtrlCorrelatOn_Type()
)
pmc1002CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlCorrelatOn.setStatus("current")
_Pmc1002CtrlCorrelatOff_Type = EkiOnOff
_Pmc1002CtrlCorrelatOff_Object = MibScalar
pmc1002CtrlCorrelatOff = _Pmc1002CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 4, 2),
    _Pmc1002CtrlCorrelatOff_Type()
)
pmc1002CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlCorrelatOff.setStatus("current")
_Pmc1002CtrlswMgnt_ObjectIdentity = ObjectIdentity
pmc1002CtrlswMgnt = _Pmc1002CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 5)
)
_Pmc1002CtrlColdReset_Type = EkiOnOff
_Pmc1002CtrlColdReset_Object = MibScalar
pmc1002CtrlColdReset = _Pmc1002CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 5, 2),
    _Pmc1002CtrlColdReset_Type()
)
pmc1002CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlColdReset.setStatus("current")
_Pmc1002CtrlWarmReset_Type = EkiOnOff
_Pmc1002CtrlWarmReset_Object = MibScalar
pmc1002CtrlWarmReset = _Pmc1002CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 5, 3),
    _Pmc1002CtrlWarmReset_Type()
)
pmc1002CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlWarmReset.setStatus("current")
_Pmc1002CtrlLoadSwBank1_Type = EkiOnOff
_Pmc1002CtrlLoadSwBank1_Object = MibScalar
pmc1002CtrlLoadSwBank1 = _Pmc1002CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 5, 5),
    _Pmc1002CtrlLoadSwBank1_Type()
)
pmc1002CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLoadSwBank1.setStatus("current")
_Pmc1002CtrlLoadSwBank2_Type = EkiOnOff
_Pmc1002CtrlLoadSwBank2_Object = MibScalar
pmc1002CtrlLoadSwBank2 = _Pmc1002CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 5, 6),
    _Pmc1002CtrlLoadSwBank2_Type()
)
pmc1002CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLoadSwBank2.setStatus("current")
_Pmc1002CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pmc1002CtrlgwMgnt = _Pmc1002CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 6)
)
_Pmc1002CtrlCurrentGwReset_Type = EkiOnOff
_Pmc1002CtrlCurrentGwReset_Object = MibScalar
pmc1002CtrlCurrentGwReset = _Pmc1002CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 6, 1),
    _Pmc1002CtrlCurrentGwReset_Type()
)
pmc1002CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlCurrentGwReset.setStatus("current")
_Pmc1002CtrlLoadGwBank1_Type = EkiOnOff
_Pmc1002CtrlLoadGwBank1_Object = MibScalar
pmc1002CtrlLoadGwBank1 = _Pmc1002CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 6, 5),
    _Pmc1002CtrlLoadGwBank1_Type()
)
pmc1002CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLoadGwBank1.setStatus("current")
_Pmc1002CtrlLoadGwBank2_Type = EkiOnOff
_Pmc1002CtrlLoadGwBank2_Object = MibScalar
pmc1002CtrlLoadGwBank2 = _Pmc1002CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 6, 6),
    _Pmc1002CtrlLoadGwBank2_Type()
)
pmc1002CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLoadGwBank2.setStatus("current")
_Pmc1002CtrlLoadGwBank3_Type = EkiOnOff
_Pmc1002CtrlLoadGwBank3_Object = MibScalar
pmc1002CtrlLoadGwBank3 = _Pmc1002CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 6, 7),
    _Pmc1002CtrlLoadGwBank3_Type()
)
pmc1002CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLoadGwBank3.setStatus("current")
_Pmc1002CtrlLoadGwBank4_Type = EkiOnOff
_Pmc1002CtrlLoadGwBank4_Object = MibScalar
pmc1002CtrlLoadGwBank4 = _Pmc1002CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 6, 8),
    _Pmc1002CtrlLoadGwBank4_Type()
)
pmc1002CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLoadGwBank4.setStatus("current")
_Pmc1002CtrlledTest_ObjectIdentity = ObjectIdentity
pmc1002CtrlledTest = _Pmc1002CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 192)
)
_Pmc1002CtrlGreenLed_Type = EkiOnOff
_Pmc1002CtrlGreenLed_Object = MibScalar
pmc1002CtrlGreenLed = _Pmc1002CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 192, 1),
    _Pmc1002CtrlGreenLed_Type()
)
pmc1002CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlGreenLed.setStatus("current")
_Pmc1002CtrlRedLed_Type = EkiOnOff
_Pmc1002CtrlRedLed_Object = MibScalar
pmc1002CtrlRedLed = _Pmc1002CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 192, 2),
    _Pmc1002CtrlRedLed_Type()
)
pmc1002CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlRedLed.setStatus("current")
_Pmc1002CtrlLedOff_Type = EkiOnOff
_Pmc1002CtrlLedOff_Object = MibScalar
pmc1002CtrlLedOff = _Pmc1002CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 192, 3),
    _Pmc1002CtrlLedOff_Type()
)
pmc1002CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlLedOff.setStatus("current")
_Pmc1002CtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pmc1002CtrlmoduleOosMode = _Pmc1002CtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 193)
)
_Pmc1002CtrlModuleOosMode_Type = EkiOnOff
_Pmc1002CtrlModuleOosMode_Object = MibScalar
pmc1002CtrlModuleOosMode = _Pmc1002CtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 193, 1),
    _Pmc1002CtrlModuleOosMode_Type()
)
pmc1002CtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlModuleOosMode.setStatus("current")
_Pmc1002CtrlmoduleDccMgnt_Type = Pmc1002DccMode
_Pmc1002CtrlmoduleDccMgnt_Object = MibScalar
pmc1002CtrlmoduleDccMgnt = _Pmc1002CtrlmoduleDccMgnt_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 196),
    _Pmc1002CtrlmoduleDccMgnt_Type()
)
pmc1002CtrlmoduleDccMgnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlmoduleDccMgnt.setStatus("current")
_Pmc1002CtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pmc1002CtrlmaintenanceMode = _Pmc1002CtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 197)
)
_Pmc1002CtrlMaintenanceMode_Type = EkiOnOff
_Pmc1002CtrlMaintenanceMode_Object = MibScalar
pmc1002CtrlMaintenanceMode = _Pmc1002CtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 1, 197, 1),
    _Pmc1002CtrlMaintenanceMode_Type()
)
pmc1002CtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlMaintenanceMode.setStatus("current")
_Pmc1002CtrlClient_ObjectIdentity = ObjectIdentity
pmc1002CtrlClient = _Pmc1002CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2)
)
_Pmc1002CtrlaccessLoopTable_Object = MibTable
pmc1002CtrlaccessLoopTable = _Pmc1002CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1002CtrlaccessLoopTable.setStatus("current")
_Pmc1002CtrlaccessLoopEntry_Object = MibTableRow
pmc1002CtrlaccessLoopEntry = _Pmc1002CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 16, 1)
)
pmc1002CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlaccessLoopEntry.setStatus("current")


class _Pmc1002CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pmc1002CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlaccessLoopIndex_Object = MibTableColumn
pmc1002CtrlaccessLoopIndex = _Pmc1002CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 16, 1, 1),
    _Pmc1002CtrlaccessLoopIndex_Type()
)
pmc1002CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlaccessLoopIndex.setStatus("current")
_Pmc1002CtrlaccessLoopPortn_Type = EkiState
_Pmc1002CtrlaccessLoopPortn_Object = MibTableColumn
pmc1002CtrlaccessLoopPortn = _Pmc1002CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 16, 1, 2),
    _Pmc1002CtrlaccessLoopPortn_Type()
)
pmc1002CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlaccessLoopPortn.setStatus("current")
_Pmc1002CtrlportOosModeTable_Object = MibTable
pmc1002CtrlportOosModeTable = _Pmc1002CtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pmc1002CtrlportOosModeTable.setStatus("current")
_Pmc1002CtrlportOosModeEntry_Object = MibTableRow
pmc1002CtrlportOosModeEntry = _Pmc1002CtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 18, 1)
)
pmc1002CtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlportOosModeEntry.setStatus("current")


class _Pmc1002CtrlportOosModeIndex_Type(Integer32):
    """Custom type pmc1002CtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlportOosModeIndex_Object = MibTableColumn
pmc1002CtrlportOosModeIndex = _Pmc1002CtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 18, 1, 1),
    _Pmc1002CtrlportOosModeIndex_Type()
)
pmc1002CtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlportOosModeIndex.setStatus("current")
_Pmc1002CtrlportOosModePortn_Type = EkiState
_Pmc1002CtrlportOosModePortn_Object = MibTableColumn
pmc1002CtrlportOosModePortn = _Pmc1002CtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 18, 1, 2),
    _Pmc1002CtrlportOosModePortn_Type()
)
pmc1002CtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlportOosModePortn.setStatus("current")
_Pmc1002CtrlsfpOffCtrlTable_Object = MibTable
pmc1002CtrlsfpOffCtrlTable = _Pmc1002CtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pmc1002CtrlsfpOffCtrlTable.setStatus("current")
_Pmc1002CtrlsfpOffCtrlEntry_Object = MibTableRow
pmc1002CtrlsfpOffCtrlEntry = _Pmc1002CtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 20, 1)
)
pmc1002CtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlsfpOffCtrlEntry.setStatus("current")


class _Pmc1002CtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pmc1002CtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlsfpOffCtrlIndex_Object = MibTableColumn
pmc1002CtrlsfpOffCtrlIndex = _Pmc1002CtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 20, 1, 1),
    _Pmc1002CtrlsfpOffCtrlIndex_Type()
)
pmc1002CtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlsfpOffCtrlIndex.setStatus("current")
_Pmc1002CtrlsfpOffCtrlPortn_Type = EkiState
_Pmc1002CtrlsfpOffCtrlPortn_Object = MibTableColumn
pmc1002CtrlsfpOffCtrlPortn = _Pmc1002CtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 20, 1, 2),
    _Pmc1002CtrlsfpOffCtrlPortn_Type()
)
pmc1002CtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlsfpOffCtrlPortn.setStatus("current")
_Pmc1002CtrlcsfUpInsTable_Object = MibTable
pmc1002CtrlcsfUpInsTable = _Pmc1002CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pmc1002CtrlcsfUpInsTable.setStatus("current")
_Pmc1002CtrlcsfUpInsEntry_Object = MibTableRow
pmc1002CtrlcsfUpInsEntry = _Pmc1002CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 21, 1)
)
pmc1002CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlcsfUpInsEntry.setStatus("current")


class _Pmc1002CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pmc1002CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlcsfUpInsIndex_Object = MibTableColumn
pmc1002CtrlcsfUpInsIndex = _Pmc1002CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 21, 1, 1),
    _Pmc1002CtrlcsfUpInsIndex_Type()
)
pmc1002CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlcsfUpInsIndex.setStatus("current")
_Pmc1002CtrlcsfUpInsPortn_Type = EkiState
_Pmc1002CtrlcsfUpInsPortn_Object = MibTableColumn
pmc1002CtrlcsfUpInsPortn = _Pmc1002CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 21, 1, 2),
    _Pmc1002CtrlcsfUpInsPortn_Type()
)
pmc1002CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlcsfUpInsPortn.setStatus("current")
_Pmc1002CtrlcaisDwInsTable_Object = MibTable
pmc1002CtrlcaisDwInsTable = _Pmc1002CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pmc1002CtrlcaisDwInsTable.setStatus("current")
_Pmc1002CtrlcaisDwInsEntry_Object = MibTableRow
pmc1002CtrlcaisDwInsEntry = _Pmc1002CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 22, 1)
)
pmc1002CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlcaisDwInsEntry.setStatus("current")


class _Pmc1002CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pmc1002CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlcaisDwInsIndex_Object = MibTableColumn
pmc1002CtrlcaisDwInsIndex = _Pmc1002CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 22, 1, 1),
    _Pmc1002CtrlcaisDwInsIndex_Type()
)
pmc1002CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlcaisDwInsIndex.setStatus("current")
_Pmc1002CtrlcaisDwInsPortn_Type = EkiState
_Pmc1002CtrlcaisDwInsPortn_Object = MibTableColumn
pmc1002CtrlcaisDwInsPortn = _Pmc1002CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 22, 1, 2),
    _Pmc1002CtrlcaisDwInsPortn_Type()
)
pmc1002CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlcaisDwInsPortn.setStatus("current")
_Pmc1002CtrlclientAccessTermLoopTable_Object = MibTable
pmc1002CtrlclientAccessTermLoopTable = _Pmc1002CtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pmc1002CtrlclientAccessTermLoopTable.setStatus("current")
_Pmc1002CtrlclientAccessTermLoopEntry_Object = MibTableRow
pmc1002CtrlclientAccessTermLoopEntry = _Pmc1002CtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 26, 1)
)
pmc1002CtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlclientAccessTermLoopEntry.setStatus("current")


class _Pmc1002CtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pmc1002CtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlclientAccessTermLoopIndex_Object = MibTableColumn
pmc1002CtrlclientAccessTermLoopIndex = _Pmc1002CtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 26, 1, 1),
    _Pmc1002CtrlclientAccessTermLoopIndex_Type()
)
pmc1002CtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlclientAccessTermLoopIndex.setStatus("current")
_Pmc1002CtrlclientAccessTermLoopPortn_Type = EkiState
_Pmc1002CtrlclientAccessTermLoopPortn_Object = MibTableColumn
pmc1002CtrlclientAccessTermLoopPortn = _Pmc1002CtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 26, 1, 2),
    _Pmc1002CtrlclientAccessTermLoopPortn_Type()
)
pmc1002CtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlclientAccessTermLoopPortn.setStatus("current")
_Pmc1002CtrlprotocolTable_Object = MibTable
pmc1002CtrlprotocolTable = _Pmc1002CtrlprotocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 52)
)
if mibBuilder.loadTexts:
    pmc1002CtrlprotocolTable.setStatus("current")
_Pmc1002CtrlprotocolEntry_Object = MibTableRow
pmc1002CtrlprotocolEntry = _Pmc1002CtrlprotocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 52, 1)
)
pmc1002CtrlprotocolEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlprotocolIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlprotocolEntry.setStatus("current")


class _Pmc1002CtrlprotocolIndex_Type(Integer32):
    """Custom type pmc1002CtrlprotocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlprotocolIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlprotocolIndex_Object = MibTableColumn
pmc1002CtrlprotocolIndex = _Pmc1002CtrlprotocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 52, 1, 1),
    _Pmc1002CtrlprotocolIndex_Type()
)
pmc1002CtrlprotocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlprotocolIndex.setStatus("current")
_Pmc1002CtrlprotocolPortn_Type = EkiProtocol
_Pmc1002CtrlprotocolPortn_Object = MibTableColumn
pmc1002CtrlprotocolPortn = _Pmc1002CtrlprotocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 52, 1, 2),
    _Pmc1002CtrlprotocolPortn_Type()
)
pmc1002CtrlprotocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlprotocolPortn.setStatus("current")
_Pmc1002CtrlclientResetAllCountTable_Object = MibTable
pmc1002CtrlclientResetAllCountTable = _Pmc1002CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 271)
)
if mibBuilder.loadTexts:
    pmc1002CtrlclientResetAllCountTable.setStatus("current")
_Pmc1002CtrlclientResetAllCountEntry_Object = MibTableRow
pmc1002CtrlclientResetAllCountEntry = _Pmc1002CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 271, 1)
)
pmc1002CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlclientResetAllCountEntry.setStatus("current")


class _Pmc1002CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pmc1002CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlclientResetAllCountIndex_Object = MibTableColumn
pmc1002CtrlclientResetAllCountIndex = _Pmc1002CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 271, 1, 1),
    _Pmc1002CtrlclientResetAllCountIndex_Type()
)
pmc1002CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlclientResetAllCountIndex.setStatus("current")
_Pmc1002CtrlclientResetAllCountsPortn_Type = EkiState
_Pmc1002CtrlclientResetAllCountsPortn_Object = MibTableColumn
pmc1002CtrlclientResetAllCountsPortn = _Pmc1002CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 2, 271, 1, 2),
    _Pmc1002CtrlclientResetAllCountsPortn_Type()
)
pmc1002CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlclientResetAllCountsPortn.setStatus("current")
_Pmc1002CtrlLine_ObjectIdentity = ObjectIdentity
pmc1002CtrlLine = _Pmc1002CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3)
)
_Pmc1002CtrlcommAccessLoopTable_Object = MibTable
pmc1002CtrlcommAccessLoopTable = _Pmc1002CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pmc1002CtrlcommAccessLoopTable.setStatus("deprecated")
_Pmc1002CtrlcommAccessLoopEntry_Object = MibTableRow
pmc1002CtrlcommAccessLoopEntry = _Pmc1002CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 64, 1)
)
pmc1002CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlcommAccessLoopEntry.setStatus("deprecated")


class _Pmc1002CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pmc1002CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlcommAccessLoopIndex_Object = MibTableColumn
pmc1002CtrlcommAccessLoopIndex = _Pmc1002CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 64, 1, 1),
    _Pmc1002CtrlcommAccessLoopIndex_Type()
)
pmc1002CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlcommAccessLoopIndex.setStatus("deprecated")
_Pmc1002CtrlcommAccessLoopPortn_Type = EkiState
_Pmc1002CtrlcommAccessLoopPortn_Object = MibTableColumn
pmc1002CtrlcommAccessLoopPortn = _Pmc1002CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 64, 1, 2),
    _Pmc1002CtrlcommAccessLoopPortn_Type()
)
pmc1002CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlcommAccessLoopPortn.setStatus("deprecated")
_Pmc1002CtrllineLoopTable_Object = MibTable
pmc1002CtrllineLoopTable = _Pmc1002CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopTable.setStatus("current")
_Pmc1002CtrllineLoopEntry_Object = MibTableRow
pmc1002CtrllineLoopEntry = _Pmc1002CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 66, 1)
)
pmc1002CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopEntry.setStatus("current")


class _Pmc1002CtrllineLoopIndex_Type(Integer32):
    """Custom type pmc1002CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllineLoopIndex_Object = MibTableColumn
pmc1002CtrllineLoopIndex = _Pmc1002CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 66, 1, 1),
    _Pmc1002CtrllineLoopIndex_Type()
)
pmc1002CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopIndex.setStatus("current")
_Pmc1002CtrllineLoopPortn_Type = EkiState
_Pmc1002CtrllineLoopPortn_Object = MibTableColumn
pmc1002CtrllineLoopPortn = _Pmc1002CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 66, 1, 2),
    _Pmc1002CtrllineLoopPortn_Type()
)
pmc1002CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopPortn.setStatus("current")
_Pmc1002CtrlmsAisTable_Object = MibTable
pmc1002CtrlmsAisTable = _Pmc1002CtrlmsAisTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 67)
)
if mibBuilder.loadTexts:
    pmc1002CtrlmsAisTable.setStatus("current")
_Pmc1002CtrlmsAisEntry_Object = MibTableRow
pmc1002CtrlmsAisEntry = _Pmc1002CtrlmsAisEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 67, 1)
)
pmc1002CtrlmsAisEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlmsAisIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlmsAisEntry.setStatus("current")


class _Pmc1002CtrlmsAisIndex_Type(Integer32):
    """Custom type pmc1002CtrlmsAisIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlmsAisIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlmsAisIndex_Object = MibTableColumn
pmc1002CtrlmsAisIndex = _Pmc1002CtrlmsAisIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 67, 1, 1),
    _Pmc1002CtrlmsAisIndex_Type()
)
pmc1002CtrlmsAisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlmsAisIndex.setStatus("current")
_Pmc1002CtrlmsAisPortn_Type = EkiState
_Pmc1002CtrlmsAisPortn_Object = MibTableColumn
pmc1002CtrlmsAisPortn = _Pmc1002CtrlmsAisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 67, 1, 2),
    _Pmc1002CtrlmsAisPortn_Type()
)
pmc1002CtrlmsAisPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlmsAisPortn.setStatus("current")
_Pmc1002CtrlfecDisableTable_Object = MibTable
pmc1002CtrlfecDisableTable = _Pmc1002CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pmc1002CtrlfecDisableTable.setStatus("current")
_Pmc1002CtrlfecDisableEntry_Object = MibTableRow
pmc1002CtrlfecDisableEntry = _Pmc1002CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 69, 1)
)
pmc1002CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlfecDisableEntry.setStatus("current")


class _Pmc1002CtrlfecDisableIndex_Type(Integer32):
    """Custom type pmc1002CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlfecDisableIndex_Object = MibTableColumn
pmc1002CtrlfecDisableIndex = _Pmc1002CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 69, 1, 1),
    _Pmc1002CtrlfecDisableIndex_Type()
)
pmc1002CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlfecDisableIndex.setStatus("current")
_Pmc1002CtrlfecDisablePortn_Type = EkiState
_Pmc1002CtrlfecDisablePortn_Object = MibTableColumn
pmc1002CtrlfecDisablePortn = _Pmc1002CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 69, 1, 2),
    _Pmc1002CtrlfecDisablePortn_Type()
)
pmc1002CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlfecDisablePortn.setStatus("current")
_Pmc1002CtrllineOosModeTable_Object = MibTable
pmc1002CtrllineOosModeTable = _Pmc1002CtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pmc1002CtrllineOosModeTable.setStatus("current")
_Pmc1002CtrllineOosModeEntry_Object = MibTableRow
pmc1002CtrllineOosModeEntry = _Pmc1002CtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 74, 1)
)
pmc1002CtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllineOosModeEntry.setStatus("current")


class _Pmc1002CtrllineOosModeIndex_Type(Integer32):
    """Custom type pmc1002CtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllineOosModeIndex_Object = MibTableColumn
pmc1002CtrllineOosModeIndex = _Pmc1002CtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 74, 1, 1),
    _Pmc1002CtrllineOosModeIndex_Type()
)
pmc1002CtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllineOosModeIndex.setStatus("current")
_Pmc1002CtrllineOosModePortn_Type = EkiState
_Pmc1002CtrllineOosModePortn_Object = MibTableColumn
pmc1002CtrllineOosModePortn = _Pmc1002CtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 74, 1, 2),
    _Pmc1002CtrllineOosModePortn_Type()
)
pmc1002CtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllineOosModePortn.setStatus("current")
_Pmc1002CtrlxfpOnoffTable_Object = MibTable
pmc1002CtrlxfpOnoffTable = _Pmc1002CtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pmc1002CtrlxfpOnoffTable.setStatus("current")
_Pmc1002CtrlxfpOnoffEntry_Object = MibTableRow
pmc1002CtrlxfpOnoffEntry = _Pmc1002CtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 208, 1)
)
pmc1002CtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlxfpOnoffEntry.setStatus("current")


class _Pmc1002CtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pmc1002CtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlxfpOnoffIndex_Object = MibTableColumn
pmc1002CtrlxfpOnoffIndex = _Pmc1002CtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 208, 1, 1),
    _Pmc1002CtrlxfpOnoffIndex_Type()
)
pmc1002CtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlxfpOnoffIndex.setStatus("current")
_Pmc1002CtrlxfpOnoffPortn_Type = EkiState
_Pmc1002CtrlxfpOnoffPortn_Object = MibTableColumn
pmc1002CtrlxfpOnoffPortn = _Pmc1002CtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 208, 1, 2),
    _Pmc1002CtrlxfpOnoffPortn_Type()
)
pmc1002CtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlxfpOnoffPortn.setStatus("current")
_Pmc1002CtrlxfpLineLoopTable_Object = MibTable
pmc1002CtrlxfpLineLoopTable = _Pmc1002CtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineLoopTable.setStatus("current")
_Pmc1002CtrlxfpLineLoopEntry_Object = MibTableRow
pmc1002CtrlxfpLineLoopEntry = _Pmc1002CtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 209, 1)
)
pmc1002CtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineLoopEntry.setStatus("current")


class _Pmc1002CtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pmc1002CtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlxfpLineLoopIndex_Object = MibTableColumn
pmc1002CtrlxfpLineLoopIndex = _Pmc1002CtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 209, 1, 1),
    _Pmc1002CtrlxfpLineLoopIndex_Type()
)
pmc1002CtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineLoopIndex.setStatus("current")
_Pmc1002CtrlxfpLineLoopPortn_Type = EkiState
_Pmc1002CtrlxfpLineLoopPortn_Object = MibTableColumn
pmc1002CtrlxfpLineLoopPortn = _Pmc1002CtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 209, 1, 2),
    _Pmc1002CtrlxfpLineLoopPortn_Type()
)
pmc1002CtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineLoopPortn.setStatus("current")
_Pmc1002CtrlxfpLineXfiLoopTable_Object = MibTable
pmc1002CtrlxfpLineXfiLoopTable = _Pmc1002CtrlxfpLineXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineXfiLoopTable.setStatus("current")
_Pmc1002CtrlxfpLineXfiLoopEntry_Object = MibTableRow
pmc1002CtrlxfpLineXfiLoopEntry = _Pmc1002CtrlxfpLineXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 210, 1)
)
pmc1002CtrlxfpLineXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlxfpLineXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineXfiLoopEntry.setStatus("current")


class _Pmc1002CtrlxfpLineXfiLoopIndex_Type(Integer32):
    """Custom type pmc1002CtrlxfpLineXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlxfpLineXfiLoopIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlxfpLineXfiLoopIndex_Object = MibTableColumn
pmc1002CtrlxfpLineXfiLoopIndex = _Pmc1002CtrlxfpLineXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 210, 1, 1),
    _Pmc1002CtrlxfpLineXfiLoopIndex_Type()
)
pmc1002CtrlxfpLineXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineXfiLoopIndex.setStatus("current")
_Pmc1002CtrlxfpLineXfiLoopPortn_Type = EkiState
_Pmc1002CtrlxfpLineXfiLoopPortn_Object = MibTableColumn
pmc1002CtrlxfpLineXfiLoopPortn = _Pmc1002CtrlxfpLineXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 210, 1, 2),
    _Pmc1002CtrlxfpLineXfiLoopPortn_Type()
)
pmc1002CtrlxfpLineXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlxfpLineXfiLoopPortn.setStatus("current")
_Pmc1002CtrllineTunableChannelTable_Object = MibTable
pmc1002CtrllineTunableChannelTable = _Pmc1002CtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pmc1002CtrllineTunableChannelTable.setStatus("current")
_Pmc1002CtrllineTunableChannelEntry_Object = MibTableRow
pmc1002CtrllineTunableChannelEntry = _Pmc1002CtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 212, 1)
)
pmc1002CtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllineTunableChannelEntry.setStatus("current")


class _Pmc1002CtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pmc1002CtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllineTunableChannelIndex_Object = MibTableColumn
pmc1002CtrllineTunableChannelIndex = _Pmc1002CtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 212, 1, 1),
    _Pmc1002CtrllineTunableChannelIndex_Type()
)
pmc1002CtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllineTunableChannelIndex.setStatus("current")
_Pmc1002CtrllineTunableChannelPortn_Type = Pmc1002OtxChannel
_Pmc1002CtrllineTunableChannelPortn_Object = MibTableColumn
pmc1002CtrllineTunableChannelPortn = _Pmc1002CtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 212, 1, 2),
    _Pmc1002CtrllineTunableChannelPortn_Type()
)
pmc1002CtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllineTunableChannelPortn.setStatus("current")
_Pmc1002CtrllinePhotodiodeModeTable_Object = MibTable
pmc1002CtrllinePhotodiodeModeTable = _Pmc1002CtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeModeTable.setStatus("current")
_Pmc1002CtrllinePhotodiodeModeEntry_Object = MibTableRow
pmc1002CtrllinePhotodiodeModeEntry = _Pmc1002CtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 213, 1)
)
pmc1002CtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeModeEntry.setStatus("current")


class _Pmc1002CtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pmc1002CtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllinePhotodiodeModeIndex_Object = MibTableColumn
pmc1002CtrllinePhotodiodeModeIndex = _Pmc1002CtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 213, 1, 1),
    _Pmc1002CtrllinePhotodiodeModeIndex_Type()
)
pmc1002CtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeModeIndex.setStatus("current")
_Pmc1002CtrllinePhotodiodeModePortn_Type = Pmc1002OtxMode
_Pmc1002CtrllinePhotodiodeModePortn_Object = MibTableColumn
pmc1002CtrllinePhotodiodeModePortn = _Pmc1002CtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 213, 1, 2),
    _Pmc1002CtrllinePhotodiodeModePortn_Type()
)
pmc1002CtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeModePortn.setStatus("current")
_Pmc1002CtrllinePhotodiodeValueTable_Object = MibTable
pmc1002CtrllinePhotodiodeValueTable = _Pmc1002CtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeValueTable.setStatus("current")
_Pmc1002CtrllinePhotodiodeValueEntry_Object = MibTableRow
pmc1002CtrllinePhotodiodeValueEntry = _Pmc1002CtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 214, 1)
)
pmc1002CtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeValueEntry.setStatus("current")


class _Pmc1002CtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pmc1002CtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllinePhotodiodeValueIndex_Object = MibTableColumn
pmc1002CtrllinePhotodiodeValueIndex = _Pmc1002CtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 214, 1, 1),
    _Pmc1002CtrllinePhotodiodeValueIndex_Type()
)
pmc1002CtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeValueIndex.setStatus("current")
_Pmc1002CtrllinePhotodiodeValuePortn_Type = Pmc1002AdjustValue
_Pmc1002CtrllinePhotodiodeValuePortn_Object = MibTableColumn
pmc1002CtrllinePhotodiodeValuePortn = _Pmc1002CtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 214, 1, 2),
    _Pmc1002CtrllinePhotodiodeValuePortn_Type()
)
pmc1002CtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllinePhotodiodeValuePortn.setStatus("current")
_Pmc1002CtrllinePowerLaserTable_Object = MibTable
pmc1002CtrllinePowerLaserTable = _Pmc1002CtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pmc1002CtrllinePowerLaserTable.setStatus("current")
_Pmc1002CtrllinePowerLaserEntry_Object = MibTableRow
pmc1002CtrllinePowerLaserEntry = _Pmc1002CtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 215, 1)
)
pmc1002CtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllinePowerLaserEntry.setStatus("current")


class _Pmc1002CtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pmc1002CtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllinePowerLaserIndex_Object = MibTableColumn
pmc1002CtrllinePowerLaserIndex = _Pmc1002CtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 215, 1, 1),
    _Pmc1002CtrllinePowerLaserIndex_Type()
)
pmc1002CtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllinePowerLaserIndex.setStatus("current")


class _Pmc1002CtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pmc1002CtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pmc1002CtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pmc1002CtrllinePowerLaserPortn_Object = MibTableColumn
pmc1002CtrllinePowerLaserPortn = _Pmc1002CtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 215, 1, 2),
    _Pmc1002CtrllinePowerLaserPortn_Type()
)
pmc1002CtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllinePowerLaserPortn.setStatus("current")
_Pmc1002CtrlotxVlhResetTable_Object = MibTable
pmc1002CtrlotxVlhResetTable = _Pmc1002CtrlotxVlhResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 216)
)
if mibBuilder.loadTexts:
    pmc1002CtrlotxVlhResetTable.setStatus("current")
_Pmc1002CtrlotxVlhResetEntry_Object = MibTableRow
pmc1002CtrlotxVlhResetEntry = _Pmc1002CtrlotxVlhResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 216, 1)
)
pmc1002CtrlotxVlhResetEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrlotxVlhResetIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrlotxVlhResetEntry.setStatus("current")


class _Pmc1002CtrlotxVlhResetIndex_Type(Integer32):
    """Custom type pmc1002CtrlotxVlhResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrlotxVlhResetIndex_Type.__name__ = "Integer32"
_Pmc1002CtrlotxVlhResetIndex_Object = MibTableColumn
pmc1002CtrlotxVlhResetIndex = _Pmc1002CtrlotxVlhResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 216, 1, 1),
    _Pmc1002CtrlotxVlhResetIndex_Type()
)
pmc1002CtrlotxVlhResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrlotxVlhResetIndex.setStatus("current")
_Pmc1002CtrlotxVlhResetPortn_Type = EkiState
_Pmc1002CtrlotxVlhResetPortn_Object = MibTableColumn
pmc1002CtrlotxVlhResetPortn = _Pmc1002CtrlotxVlhResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 216, 1, 2),
    _Pmc1002CtrlotxVlhResetPortn_Type()
)
pmc1002CtrlotxVlhResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrlotxVlhResetPortn.setStatus("current")
_Pmc1002CtrllineLoopTransceiverTable_Object = MibTable
pmc1002CtrllineLoopTransceiverTable = _Pmc1002CtrllineLoopTransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 218)
)
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopTransceiverTable.setStatus("current")
_Pmc1002CtrllineLoopTransceiverEntry_Object = MibTableRow
pmc1002CtrllineLoopTransceiverEntry = _Pmc1002CtrllineLoopTransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 218, 1)
)
pmc1002CtrllineLoopTransceiverEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllineLoopTransceiverIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopTransceiverEntry.setStatus("current")


class _Pmc1002CtrllineLoopTransceiverIndex_Type(Integer32):
    """Custom type pmc1002CtrllineLoopTransceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllineLoopTransceiverIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllineLoopTransceiverIndex_Object = MibTableColumn
pmc1002CtrllineLoopTransceiverIndex = _Pmc1002CtrllineLoopTransceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 218, 1, 1),
    _Pmc1002CtrllineLoopTransceiverIndex_Type()
)
pmc1002CtrllineLoopTransceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopTransceiverIndex.setStatus("current")
_Pmc1002CtrllineLoopTransceiverPortn_Type = EkiState
_Pmc1002CtrllineLoopTransceiverPortn_Object = MibTableColumn
pmc1002CtrllineLoopTransceiverPortn = _Pmc1002CtrllineLoopTransceiverPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 218, 1, 2),
    _Pmc1002CtrllineLoopTransceiverPortn_Type()
)
pmc1002CtrllineLoopTransceiverPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllineLoopTransceiverPortn.setStatus("current")
_Pmc1002CtrllineResetAllCountTable_Object = MibTable
pmc1002CtrllineResetAllCountTable = _Pmc1002CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 335)
)
if mibBuilder.loadTexts:
    pmc1002CtrllineResetAllCountTable.setStatus("current")
_Pmc1002CtrllineResetAllCountEntry_Object = MibTableRow
pmc1002CtrllineResetAllCountEntry = _Pmc1002CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 335, 1)
)
pmc1002CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CtrllineResetAllCountEntry.setStatus("current")


class _Pmc1002CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pmc1002CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pmc1002CtrllineResetAllCountIndex_Object = MibTableColumn
pmc1002CtrllineResetAllCountIndex = _Pmc1002CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 335, 1, 1),
    _Pmc1002CtrllineResetAllCountIndex_Type()
)
pmc1002CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CtrllineResetAllCountIndex.setStatus("current")
_Pmc1002CtrllineResetAllCountsPortn_Type = EkiState
_Pmc1002CtrllineResetAllCountsPortn_Object = MibTableColumn
pmc1002CtrllineResetAllCountsPortn = _Pmc1002CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 6, 3, 335, 1, 2),
    _Pmc1002CtrllineResetAllCountsPortn_Type()
)
pmc1002CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CtrllineResetAllCountsPortn.setStatus("current")
_Pmc1002ri_ObjectIdentity = ObjectIdentity
pmc1002ri = _Pmc1002ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7)
)
_Pmc1002riTable_ObjectIdentity = ObjectIdentity
pmc1002riTable = _Pmc1002riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1)
)
_Pmc1002RinvClientTable_Object = MibTable
pmc1002RinvClientTable = _Pmc1002RinvClientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pmc1002RinvClientTable.setStatus("current")
_Pmc1002RinvClientEntry_Object = MibTableRow
pmc1002RinvClientEntry = _Pmc1002RinvClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 1, 1)
)
pmc1002RinvClientEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002RinvClientIndex"),
)
if mibBuilder.loadTexts:
    pmc1002RinvClientEntry.setStatus("current")


class _Pmc1002RinvClientIndex_Type(Integer32):
    """Custom type pmc1002RinvClientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmc1002RinvClientIndex_Type.__name__ = "Integer32"
_Pmc1002RinvClientIndex_Object = MibTableColumn
pmc1002RinvClientIndex = _Pmc1002RinvClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 1, 1, 1),
    _Pmc1002RinvClientIndex_Type()
)
pmc1002RinvClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvClientIndex.setStatus("current")
_Pmc1002RinvClient_Type = DisplayString
_Pmc1002RinvClient_Object = MibTableColumn
pmc1002RinvClient = _Pmc1002RinvClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 1, 1, 2),
    _Pmc1002RinvClient_Type()
)
pmc1002RinvClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvClient.setStatus("current")
_Pmc1002RinvLineTable_Object = MibTable
pmc1002RinvLineTable = _Pmc1002RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pmc1002RinvLineTable.setStatus("current")
_Pmc1002RinvLineEntry_Object = MibTableRow
pmc1002RinvLineEntry = _Pmc1002RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 2, 1)
)
pmc1002RinvLineEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pmc1002RinvLineEntry.setStatus("current")


class _Pmc1002RinvLineIndex_Type(Integer32):
    """Custom type pmc1002RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pmc1002RinvLineIndex_Type.__name__ = "Integer32"
_Pmc1002RinvLineIndex_Object = MibTableColumn
pmc1002RinvLineIndex = _Pmc1002RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 2, 1, 1),
    _Pmc1002RinvLineIndex_Type()
)
pmc1002RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvLineIndex.setStatus("current")
_Pmc1002RinvxfpLine_Type = DisplayString
_Pmc1002RinvxfpLine_Object = MibTableColumn
pmc1002RinvxfpLine = _Pmc1002RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 1, 2, 1, 2),
    _Pmc1002RinvxfpLine_Type()
)
pmc1002RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvxfpLine.setStatus("current")
_Pmc1002RinvReloadInventory_Type = EkiOnOff
_Pmc1002RinvReloadInventory_Object = MibScalar
pmc1002RinvReloadInventory = _Pmc1002RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 2),
    _Pmc1002RinvReloadInventory_Type()
)
pmc1002RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002RinvReloadInventory.setStatus("current")
_Pmc1002RinvHwPlatform_Type = DisplayString
_Pmc1002RinvHwPlatform_Object = MibScalar
pmc1002RinvHwPlatform = _Pmc1002RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 3),
    _Pmc1002RinvHwPlatform_Type()
)
pmc1002RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvHwPlatform.setStatus("current")
_Pmc1002RinvModulePlatform_Type = DisplayString
_Pmc1002RinvModulePlatform_Object = MibScalar
pmc1002RinvModulePlatform = _Pmc1002RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 4),
    _Pmc1002RinvModulePlatform_Type()
)
pmc1002RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvModulePlatform.setStatus("current")
_Pmc1002RinvSwPlatform_Type = DisplayString
_Pmc1002RinvSwPlatform_Object = MibScalar
pmc1002RinvSwPlatform = _Pmc1002RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 5),
    _Pmc1002RinvSwPlatform_Type()
)
pmc1002RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvSwPlatform.setStatus("current")
_Pmc1002RinvGwPlatform_Type = DisplayString
_Pmc1002RinvGwPlatform_Object = MibScalar
pmc1002RinvGwPlatform = _Pmc1002RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 7, 6),
    _Pmc1002RinvGwPlatform_Type()
)
pmc1002RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002RinvGwPlatform.setStatus("current")
_Pmc1002download_ObjectIdentity = ObjectIdentity
pmc1002download = _Pmc1002download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8)
)
_Pmc1002DwlOther_ObjectIdentity = ObjectIdentity
pmc1002DwlOther = _Pmc1002DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1)
)
_Pmc1002DwlrestartProcess_ObjectIdentity = ObjectIdentity
pmc1002DwlrestartProcess = _Pmc1002DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 0)
)
_Pmc1002DwlWarmRestartProcessed_Type = EkiOnOff
_Pmc1002DwlWarmRestartProcessed_Object = MibScalar
pmc1002DwlWarmRestartProcessed = _Pmc1002DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 0, 1),
    _Pmc1002DwlWarmRestartProcessed_Type()
)
pmc1002DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlWarmRestartProcessed.setStatus("current")
_Pmc1002DwlColdRestartProcessed_Type = EkiOnOff
_Pmc1002DwlColdRestartProcessed_Object = MibScalar
pmc1002DwlColdRestartProcessed = _Pmc1002DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 0, 2),
    _Pmc1002DwlColdRestartProcessed_Type()
)
pmc1002DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlColdRestartProcessed.setStatus("current")
_Pmc1002DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pmc1002DwlswBanksUsed = _Pmc1002DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 1)
)
_Pmc1002DwlSwBank1Used_Type = EkiOnOff
_Pmc1002DwlSwBank1Used_Object = MibScalar
pmc1002DwlSwBank1Used = _Pmc1002DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 1, 1),
    _Pmc1002DwlSwBank1Used_Type()
)
pmc1002DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlSwBank1Used.setStatus("current")
_Pmc1002DwlSwBank2Used_Type = EkiOnOff
_Pmc1002DwlSwBank2Used_Object = MibScalar
pmc1002DwlSwBank2Used = _Pmc1002DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 1, 2),
    _Pmc1002DwlSwBank2Used_Type()
)
pmc1002DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlSwBank2Used.setStatus("current")
_Pmc1002DwlSwBank1Notempty_Type = EkiOnOff
_Pmc1002DwlSwBank1Notempty_Object = MibScalar
pmc1002DwlSwBank1Notempty = _Pmc1002DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 1, 5),
    _Pmc1002DwlSwBank1Notempty_Type()
)
pmc1002DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlSwBank1Notempty.setStatus("current")
_Pmc1002DwlSwBank2Notempty_Type = EkiOnOff
_Pmc1002DwlSwBank2Notempty_Object = MibScalar
pmc1002DwlSwBank2Notempty = _Pmc1002DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 1, 6),
    _Pmc1002DwlSwBank2Notempty_Type()
)
pmc1002DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlSwBank2Notempty.setStatus("current")
_Pmc1002DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pmc1002DwlgwBanksUsed = _Pmc1002DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2)
)
_Pmc1002DwlGwBank1Used_Type = EkiOnOff
_Pmc1002DwlGwBank1Used_Object = MibScalar
pmc1002DwlGwBank1Used = _Pmc1002DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 1),
    _Pmc1002DwlGwBank1Used_Type()
)
pmc1002DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank1Used.setStatus("current")
_Pmc1002DwlGwBank2Used_Type = EkiOnOff
_Pmc1002DwlGwBank2Used_Object = MibScalar
pmc1002DwlGwBank2Used = _Pmc1002DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 2),
    _Pmc1002DwlGwBank2Used_Type()
)
pmc1002DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank2Used.setStatus("deprecated")
_Pmc1002DwlGwBank3Used_Type = EkiOnOff
_Pmc1002DwlGwBank3Used_Object = MibScalar
pmc1002DwlGwBank3Used = _Pmc1002DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 3),
    _Pmc1002DwlGwBank3Used_Type()
)
pmc1002DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank3Used.setStatus("current")
_Pmc1002DwlGwBank4Used_Type = EkiOnOff
_Pmc1002DwlGwBank4Used_Object = MibScalar
pmc1002DwlGwBank4Used = _Pmc1002DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 4),
    _Pmc1002DwlGwBank4Used_Type()
)
pmc1002DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank4Used.setStatus("deprecated")
_Pmc1002DwlGwBank1Notempty_Type = EkiOnOff
_Pmc1002DwlGwBank1Notempty_Object = MibScalar
pmc1002DwlGwBank1Notempty = _Pmc1002DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 5),
    _Pmc1002DwlGwBank1Notempty_Type()
)
pmc1002DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank1Notempty.setStatus("current")
_Pmc1002DwlGwBank2Notempty_Type = EkiOnOff
_Pmc1002DwlGwBank2Notempty_Object = MibScalar
pmc1002DwlGwBank2Notempty = _Pmc1002DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 6),
    _Pmc1002DwlGwBank2Notempty_Type()
)
pmc1002DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank2Notempty.setStatus("deprecated")
_Pmc1002DwlGwBank3Notempty_Type = EkiOnOff
_Pmc1002DwlGwBank3Notempty_Object = MibScalar
pmc1002DwlGwBank3Notempty = _Pmc1002DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 7),
    _Pmc1002DwlGwBank3Notempty_Type()
)
pmc1002DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank3Notempty.setStatus("current")
_Pmc1002DwlGwBank4Notempty_Type = EkiOnOff
_Pmc1002DwlGwBank4Notempty_Object = MibScalar
pmc1002DwlGwBank4Notempty = _Pmc1002DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 1, 2, 8),
    _Pmc1002DwlGwBank4Notempty_Type()
)
pmc1002DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002DwlGwBank4Notempty.setStatus("deprecated")
_Pmc1002DwlClient_ObjectIdentity = ObjectIdentity
pmc1002DwlClient = _Pmc1002DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 2)
)
_Pmc1002DwlLine_ObjectIdentity = ObjectIdentity
pmc1002DwlLine = _Pmc1002DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 8, 3)
)
_Pmc1002Config_ObjectIdentity = ObjectIdentity
pmc1002Config = _Pmc1002Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10)
)
_Pmc1002CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pmc1002CfgAccessCAisCsf = _Pmc1002CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1)
)
_Pmc1002CfgClientcaiscsfTable_Object = MibTable
pmc1002CfgClientcaiscsfTable = _Pmc1002CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1)
)
if mibBuilder.loadTexts:
    pmc1002CfgClientcaiscsfTable.setStatus("current")
_Pmc1002CfgClientcaiscsfEntry_Object = MibTableRow
pmc1002CfgClientcaiscsfEntry = _Pmc1002CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1)
)
pmc1002CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgClientcaiscsfEntry.setStatus("current")


class _Pmc1002CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pmc1002CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pmc1002CfgClientcaiscsfIndex_Object = MibTableColumn
pmc1002CfgClientcaiscsfIndex = _Pmc1002CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 1),
    _Pmc1002CfgClientcaiscsfIndex_Type()
)
pmc1002CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgClientcaiscsfIndex.setStatus("current")


class _Pmc1002CfgCAisModePortn_Type(Unsigned32):
    """Custom type pmc1002CfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgCAisModePortn_Object = MibTableColumn
pmc1002CfgCAisModePortn = _Pmc1002CfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 3),
    _Pmc1002CfgCAisModePortn_Type()
)
pmc1002CfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgCAisModePortn.setStatus("current")


class _Pmc1002CfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pmc1002CfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgUpAccessioAlmPortn_Object = MibTableColumn
pmc1002CfgUpAccessioAlmPortn = _Pmc1002CfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 9),
    _Pmc1002CfgUpAccessioAlmPortn_Type()
)
pmc1002CfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgUpAccessioAlmPortn.setStatus("current")


class _Pmc1002CfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pmc1002CfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgUpMapperDeAlmPortn_Object = MibTableColumn
pmc1002CfgUpMapperDeAlmPortn = _Pmc1002CfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 10),
    _Pmc1002CfgUpMapperDeAlmPortn_Type()
)
pmc1002CfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgUpMapperDeAlmPortn.setStatus("current")


class _Pmc1002CfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pmc1002CfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgDownAccessioAlmPortn_Object = MibTableColumn
pmc1002CfgDownAccessioAlmPortn = _Pmc1002CfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 17),
    _Pmc1002CfgDownAccessioAlmPortn_Type()
)
pmc1002CfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgDownAccessioAlmPortn.setStatus("current")


class _Pmc1002CfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pmc1002CfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgDownMapperDeAlmPortn_Object = MibTableColumn
pmc1002CfgDownMapperDeAlmPortn = _Pmc1002CfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 18),
    _Pmc1002CfgDownMapperDeAlmPortn_Type()
)
pmc1002CfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgDownMapperDeAlmPortn.setStatus("current")


class _Pmc1002CfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pmc1002CfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgDownDfrmAlmPortn_Object = MibTableColumn
pmc1002CfgDownDfrmAlmPortn = _Pmc1002CfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 19),
    _Pmc1002CfgDownDfrmAlmPortn_Type()
)
pmc1002CfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgDownDfrmAlmPortn.setStatus("current")


class _Pmc1002CfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pmc1002CfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pmc1002CfgDownLineSyncAlarmsPortn = _Pmc1002CfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 1, 1, 1, 20),
    _Pmc1002CfgDownLineSyncAlarmsPortn_Type()
)
pmc1002CfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pmc1002CfgStartup_ObjectIdentity = ObjectIdentity
pmc1002CfgStartup = _Pmc1002CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2)
)
_Pmc1002CfgClientStartupTable_Object = MibTable
pmc1002CfgClientStartupTable = _Pmc1002CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 1)
)
if mibBuilder.loadTexts:
    pmc1002CfgClientStartupTable.setStatus("current")
_Pmc1002CfgClientStartupEntry_Object = MibTableRow
pmc1002CfgClientStartupEntry = _Pmc1002CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 1, 1)
)
pmc1002CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgClientStartupEntry.setStatus("current")


class _Pmc1002CfgClientStartupIndex_Type(Integer32):
    """Custom type pmc1002CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pmc1002CfgClientStartupIndex_Object = MibTableColumn
pmc1002CfgClientStartupIndex = _Pmc1002CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 1, 1, 1),
    _Pmc1002CfgClientStartupIndex_Type()
)
pmc1002CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgClientStartupIndex.setStatus("current")


class _Pmc1002CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pmc1002CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgSystConfPortPortn_Object = MibTableColumn
pmc1002CfgSystConfPortPortn = _Pmc1002CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 1, 1, 3),
    _Pmc1002CfgSystConfPortPortn_Type()
)
pmc1002CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgSystConfPortPortn.setStatus("current")


class _Pmc1002CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pmc1002CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgNetConfPortPortn_Object = MibTableColumn
pmc1002CfgNetConfPortPortn = _Pmc1002CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 1, 1, 4),
    _Pmc1002CfgNetConfPortPortn_Type()
)
pmc1002CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgNetConfPortPortn.setStatus("current")


class _Pmc1002CfgPortsOptionsPortn_Type(Unsigned32):
    """Custom type pmc1002CfgPortsOptionsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgPortsOptionsPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgPortsOptionsPortn_Object = MibTableColumn
pmc1002CfgPortsOptionsPortn = _Pmc1002CfgPortsOptionsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 1, 1, 6),
    _Pmc1002CfgPortsOptionsPortn_Type()
)
pmc1002CfgPortsOptionsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgPortsOptionsPortn.setStatus("current")
_Pmc1002tablelineStartup_ObjectIdentity = ObjectIdentity
pmc1002tablelineStartup = _Pmc1002tablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 2)
)


class _Pmc1002CfgsynthTransLine1_Type(Unsigned32):
    """Custom type pmc1002CfgsynthTransLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgsynthTransLine1_Type.__name__ = "Unsigned32"
_Pmc1002CfgsynthTransLine1_Object = MibScalar
pmc1002CfgsynthTransLine1 = _Pmc1002CfgsynthTransLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 2, 2),
    _Pmc1002CfgsynthTransLine1_Type()
)
pmc1002CfgsynthTransLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgsynthTransLine1.setStatus("current")


class _Pmc1002CfgnetConfMod_Type(Unsigned32):
    """Custom type pmc1002CfgnetConfMod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgnetConfMod_Type.__name__ = "Unsigned32"
_Pmc1002CfgnetConfMod_Object = MibScalar
pmc1002CfgnetConfMod = _Pmc1002CfgnetConfMod_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 2, 3),
    _Pmc1002CfgnetConfMod_Type()
)
pmc1002CfgnetConfMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgnetConfMod.setStatus("current")


class _Pmc1002CfglineOptions1_Type(Unsigned32):
    """Custom type pmc1002CfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfglineOptions1_Type.__name__ = "Unsigned32"
_Pmc1002CfglineOptions1_Object = MibScalar
pmc1002CfglineOptions1 = _Pmc1002CfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 2, 5),
    _Pmc1002CfglineOptions1_Type()
)
pmc1002CfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfglineOptions1.setStatus("current")


class _Pmc1002CfgsystTransLine2_Type(Unsigned32):
    """Custom type pmc1002CfgsystTransLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgsystTransLine2_Type.__name__ = "Unsigned32"
_Pmc1002CfgsystTransLine2_Object = MibScalar
pmc1002CfgsystTransLine2 = _Pmc1002CfgsystTransLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 2, 6),
    _Pmc1002CfgsystTransLine2_Type()
)
pmc1002CfgsystTransLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgsystTransLine2.setStatus("current")


class _Pmc1002CfglineSelection_Type(Unsigned32):
    """Custom type pmc1002CfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfglineSelection_Type.__name__ = "Unsigned32"
_Pmc1002CfglineSelection_Object = MibScalar
pmc1002CfglineSelection = _Pmc1002CfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 2, 7),
    _Pmc1002CfglineSelection_Type()
)
pmc1002CfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfglineSelection.setStatus("current")
_Pmc1002CfgXfpTable_Object = MibTable
pmc1002CfgXfpTable = _Pmc1002CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 3)
)
if mibBuilder.loadTexts:
    pmc1002CfgXfpTable.setStatus("current")
_Pmc1002CfgXfpEntry_Object = MibTableRow
pmc1002CfgXfpEntry = _Pmc1002CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 3, 1)
)
pmc1002CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgXfpEntry.setStatus("current")


class _Pmc1002CfgXfpIndex_Type(Integer32):
    """Custom type pmc1002CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgXfpIndex_Type.__name__ = "Integer32"
_Pmc1002CfgXfpIndex_Object = MibTableColumn
pmc1002CfgXfpIndex = _Pmc1002CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 3, 1, 1),
    _Pmc1002CfgXfpIndex_Type()
)
pmc1002CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgXfpIndex.setStatus("current")


class _Pmc1002CfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pmc1002CfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgSystConfXfpPortn_Object = MibTableColumn
pmc1002CfgSystConfXfpPortn = _Pmc1002CfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 3, 1, 3),
    _Pmc1002CfgSystConfXfpPortn_Type()
)
pmc1002CfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgSystConfXfpPortn.setStatus("current")


class _Pmc1002CfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pmc1002CfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgDataRateConfXfpPortn_Object = MibTableColumn
pmc1002CfgDataRateConfXfpPortn = _Pmc1002CfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 3, 1, 4),
    _Pmc1002CfgDataRateConfXfpPortn_Type()
)
pmc1002CfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgDataRateConfXfpPortn.setStatus("deprecated")
_Pmc1002CfgOtxtlhTable_Object = MibTable
pmc1002CfgOtxtlhTable = _Pmc1002CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4)
)
if mibBuilder.loadTexts:
    pmc1002CfgOtxtlhTable.setStatus("current")
_Pmc1002CfgOtxtlhEntry_Object = MibTableRow
pmc1002CfgOtxtlhEntry = _Pmc1002CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1)
)
pmc1002CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgOtxtlhEntry.setStatus("current")


class _Pmc1002CfgOtxtlhIndex_Type(Integer32):
    """Custom type pmc1002CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pmc1002CfgOtxtlhIndex_Object = MibTableColumn
pmc1002CfgOtxtlhIndex = _Pmc1002CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 1),
    _Pmc1002CfgOtxtlhIndex_Type()
)
pmc1002CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgOtxtlhIndex.setStatus("current")


class _Pmc1002CfgLineOtxMiscPortn_Type(Unsigned32):
    """Custom type pmc1002CfgLineOtxMiscPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLineOtxMiscPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLineOtxMiscPortn_Object = MibTableColumn
pmc1002CfgLineOtxMiscPortn = _Pmc1002CfgLineOtxMiscPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 3),
    _Pmc1002CfgLineOtxMiscPortn_Type()
)
pmc1002CfgLineOtxMiscPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLineOtxMiscPortn.setStatus("current")


class _Pmc1002CfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pmc1002CfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLineDitherRatePortn_Object = MibTableColumn
pmc1002CfgLineDitherRatePortn = _Pmc1002CfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 4),
    _Pmc1002CfgLineDitherRatePortn_Type()
)
pmc1002CfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLineDitherRatePortn.setStatus("current")


class _Pmc1002CfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pmc1002CfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLineDitherFhzPortn_Object = MibTableColumn
pmc1002CfgLineDitherFhzPortn = _Pmc1002CfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 5),
    _Pmc1002CfgLineDitherFhzPortn_Type()
)
pmc1002CfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLineDitherFhzPortn.setStatus("current")


class _Pmc1002CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pmc1002CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLinePwrLaserPortn_Object = MibTableColumn
pmc1002CfgLinePwrLaserPortn = _Pmc1002CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 6),
    _Pmc1002CfgLinePwrLaserPortn_Type()
)
pmc1002CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLinePwrLaserPortn.setStatus("current")


class _Pmc1002CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pmc1002CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLineFCurrentPortn_Object = MibTableColumn
pmc1002CfgLineFCurrentPortn = _Pmc1002CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 7),
    _Pmc1002CfgLineFCurrentPortn_Type()
)
pmc1002CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLineFCurrentPortn.setStatus("current")


class _Pmc1002CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pmc1002CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLineGridCurrentPortn_Object = MibTableColumn
pmc1002CfgLineGridCurrentPortn = _Pmc1002CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 8),
    _Pmc1002CfgLineGridCurrentPortn_Type()
)
pmc1002CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLineGridCurrentPortn.setStatus("current")


class _Pmc1002CfgFPortn_Type(Unsigned32):
    """Custom type pmc1002CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgFPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgFPortn_Object = MibTableColumn
pmc1002CfgFPortn = _Pmc1002CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 9),
    _Pmc1002CfgFPortn_Type()
)
pmc1002CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgFPortn.setStatus("current")


class _Pmc1002CfgReservedPortn_Type(Unsigned32):
    """Custom type pmc1002CfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgReservedPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgReservedPortn_Object = MibTableColumn
pmc1002CfgReservedPortn = _Pmc1002CfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 10),
    _Pmc1002CfgReservedPortn_Type()
)
pmc1002CfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgReservedPortn.setStatus("deprecated")


class _Pmc1002CfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pmc1002CfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLinePhotodiodeModePortn_Object = MibTableColumn
pmc1002CfgLinePhotodiodeModePortn = _Pmc1002CfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 11),
    _Pmc1002CfgLinePhotodiodeModePortn_Type()
)
pmc1002CfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLinePhotodiodeModePortn.setStatus("current")


class _Pmc1002CfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pmc1002CfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLinePhotodiodeValuePortn_Object = MibTableColumn
pmc1002CfgLinePhotodiodeValuePortn = _Pmc1002CfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 2, 4, 1, 12),
    _Pmc1002CfgLinePhotodiodeValuePortn_Type()
)
pmc1002CfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLinePhotodiodeValuePortn.setStatus("current")
_Pmc1002CfgLabels_ObjectIdentity = ObjectIdentity
pmc1002CfgLabels = _Pmc1002CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3)
)
_Pmc1002CfgLabelclientTable_Object = MibTable
pmc1002CfgLabelclientTable = _Pmc1002CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 1)
)
if mibBuilder.loadTexts:
    pmc1002CfgLabelclientTable.setStatus("current")
_Pmc1002CfgLabelclientEntry_Object = MibTableRow
pmc1002CfgLabelclientEntry = _Pmc1002CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 1, 1)
)
pmc1002CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgLabelclientEntry.setStatus("current")


class _Pmc1002CfgLabelclientIndex_Type(Integer32):
    """Custom type pmc1002CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pmc1002CfgLabelclientIndex_Object = MibTableColumn
pmc1002CfgLabelclientIndex = _Pmc1002CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 1, 1, 1),
    _Pmc1002CfgLabelclientIndex_Type()
)
pmc1002CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgLabelclientIndex.setStatus("current")


class _Pmc1002CfgLabelclientPortn_Type(DisplayString):
    """Custom type pmc1002CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmc1002CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pmc1002CfgLabelclientPortn_Object = MibTableColumn
pmc1002CfgLabelclientPortn = _Pmc1002CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 1, 1, 3),
    _Pmc1002CfgLabelclientPortn_Type()
)
pmc1002CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLabelclientPortn.setStatus("current")
_Pmc1002CfgLabellineTable_Object = MibTable
pmc1002CfgLabellineTable = _Pmc1002CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 2)
)
if mibBuilder.loadTexts:
    pmc1002CfgLabellineTable.setStatus("current")
_Pmc1002CfgLabellineEntry_Object = MibTableRow
pmc1002CfgLabellineEntry = _Pmc1002CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 2, 1)
)
pmc1002CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgLabellineEntry.setStatus("current")


class _Pmc1002CfgLabellineIndex_Type(Integer32):
    """Custom type pmc1002CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgLabellineIndex_Type.__name__ = "Integer32"
_Pmc1002CfgLabellineIndex_Object = MibTableColumn
pmc1002CfgLabellineIndex = _Pmc1002CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 2, 1, 1),
    _Pmc1002CfgLabellineIndex_Type()
)
pmc1002CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgLabellineIndex.setStatus("current")


class _Pmc1002CfgLabellinePortn_Type(DisplayString):
    """Custom type pmc1002CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pmc1002CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pmc1002CfgLabellinePortn_Object = MibTableColumn
pmc1002CfgLabellinePortn = _Pmc1002CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 3, 2, 1, 3),
    _Pmc1002CfgLabellinePortn_Type()
)
pmc1002CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgLabellinePortn.setStatus("current")
_Pmc1002CfgOther_ObjectIdentity = ObjectIdentity
pmc1002CfgOther = _Pmc1002CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 4)
)
_Pmc1002tablemoduleOther_ObjectIdentity = ObjectIdentity
pmc1002tablemoduleOther = _Pmc1002tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 4, 1)
)


class _Pmc1002Cfgmode_Type(Unsigned32):
    """Custom type pmc1002Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002Cfgmode_Type.__name__ = "Unsigned32"
_Pmc1002Cfgmode_Object = MibScalar
pmc1002Cfgmode = _Pmc1002Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 4, 1, 2),
    _Pmc1002Cfgmode_Type()
)
pmc1002Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Cfgmode.setStatus("current")
_Pmc1002CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pmc1002CfgStartuptablefive = _Pmc1002CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5)
)
_Pmc1002CfgOtxtlhcapabilitiesTable_Object = MibTable
pmc1002CfgOtxtlhcapabilitiesTable = _Pmc1002CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1)
)
if mibBuilder.loadTexts:
    pmc1002CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pmc1002CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pmc1002CfgOtxtlhcapabilitiesEntry = _Pmc1002CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1)
)
pmc1002CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pmc1002CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pmc1002CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pmc1002CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pmc1002CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pmc1002CfgOtxtlhcapabilitiesIndex = _Pmc1002CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1, 1),
    _Pmc1002CfgOtxtlhcapabilitiesIndex_Type()
)
pmc1002CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pmc1002CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pmc1002CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgComponentTypePortn_Object = MibTableColumn
pmc1002CfgComponentTypePortn = _Pmc1002CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1, 3),
    _Pmc1002CfgComponentTypePortn_Type()
)
pmc1002CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgComponentTypePortn.setStatus("current")


class _Pmc1002CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pmc1002CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgMiscellaneousPortn_Object = MibTableColumn
pmc1002CfgMiscellaneousPortn = _Pmc1002CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1, 4),
    _Pmc1002CfgMiscellaneousPortn_Type()
)
pmc1002CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgMiscellaneousPortn.setStatus("current")


class _Pmc1002CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pmc1002CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgFirstChannelPortn_Object = MibTableColumn
pmc1002CfgFirstChannelPortn = _Pmc1002CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1, 5),
    _Pmc1002CfgFirstChannelPortn_Type()
)
pmc1002CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgFirstChannelPortn.setStatus("current")


class _Pmc1002CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pmc1002CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgLastChannelPortn_Object = MibTableColumn
pmc1002CfgLastChannelPortn = _Pmc1002CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1, 6),
    _Pmc1002CfgLastChannelPortn_Type()
)
pmc1002CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgLastChannelPortn.setStatus("current")


class _Pmc1002CfgGridPortn_Type(Unsigned32):
    """Custom type pmc1002CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pmc1002CfgGridPortn_Type.__name__ = "Unsigned32"
_Pmc1002CfgGridPortn_Object = MibTableColumn
pmc1002CfgGridPortn = _Pmc1002CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 5, 1, 1, 7),
    _Pmc1002CfgGridPortn_Type()
)
pmc1002CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002CfgGridPortn.setStatus("current")
_Pmc1002CfgWriteConfiguration_Type = EkiOnOff
_Pmc1002CfgWriteConfiguration_Object = MibScalar
pmc1002CfgWriteConfiguration = _Pmc1002CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 10, 257),
    _Pmc1002CfgWriteConfiguration_Type()
)
pmc1002CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002CfgWriteConfiguration.setStatus("current")
_Pmc1002traps_ObjectIdentity = ObjectIdentity
pmc1002traps = _Pmc1002traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11)
)


class _Pmc1002trapBoardNumber_Type(Integer32):
    """Custom type pmc1002trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc1002trapBoardNumber_Type.__name__ = "Integer32"
_Pmc1002trapBoardNumber_Object = MibScalar
pmc1002trapBoardNumber = _Pmc1002trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 1),
    _Pmc1002trapBoardNumber_Type()
)
pmc1002trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002trapBoardNumber.setStatus("current")


class _Pmc1002trapClientNumber_Type(Integer32):
    """Custom type pmc1002trapClientNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc1002trapClientNumber_Type.__name__ = "Integer32"
_Pmc1002trapClientNumber_Object = MibScalar
pmc1002trapClientNumber = _Pmc1002trapClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 2),
    _Pmc1002trapClientNumber_Type()
)
pmc1002trapClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002trapClientNumber.setStatus("current")


class _Pmc1002trapLineNumber_Type(Integer32):
    """Custom type pmc1002trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pmc1002trapLineNumber_Type.__name__ = "Integer32"
_Pmc1002trapLineNumber_Object = MibScalar
pmc1002trapLineNumber = _Pmc1002trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 3),
    _Pmc1002trapLineNumber_Type()
)
pmc1002trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002trapLineNumber.setStatus("current")
_Pmc1002Monitoring_ObjectIdentity = ObjectIdentity
pmc1002Monitoring = _Pmc1002Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12)
)
_Pmc1002MonOther_ObjectIdentity = ObjectIdentity
pmc1002MonOther = _Pmc1002MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1)
)
_Pmc1002MonSync_ObjectIdentity = ObjectIdentity
pmc1002MonSync = _Pmc1002MonSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 1)
)
_Pmc1002PerfEnable_Type = EkiOnOff
_Pmc1002PerfEnable_Object = MibScalar
pmc1002PerfEnable = _Pmc1002PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 1, 257),
    _Pmc1002PerfEnable_Type()
)
pmc1002PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002PerfEnable.setStatus("current")
_Pmc1002Perf15minSync_Type = EkiOnOff
_Pmc1002Perf15minSync_Object = MibScalar
pmc1002Perf15minSync = _Pmc1002Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 1, 259),
    _Pmc1002Perf15minSync_Type()
)
pmc1002Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Perf15minSync.setStatus("current")
_Pmc1002Perf24hSync_Type = EkiOnOff
_Pmc1002Perf24hSync_Object = MibScalar
pmc1002Perf24hSync = _Pmc1002Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 1, 260),
    _Pmc1002Perf24hSync_Type()
)
pmc1002Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Perf24hSync.setStatus("current")
_Pmc1002MonTimeStamp_ObjectIdentity = ObjectIdentity
pmc1002MonTimeStamp = _Pmc1002MonTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2)
)
_Pmc1002Perf15MinShort_Type = EkiOnOff
_Pmc1002Perf15MinShort_Object = MibScalar
pmc1002Perf15MinShort = _Pmc1002Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2, 1),
    _Pmc1002Perf15MinShort_Type()
)
pmc1002Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Perf15MinShort.setStatus("current")
_Pmc1002Perf15MinLong_Type = EkiOnOff
_Pmc1002Perf15MinLong_Object = MibScalar
pmc1002Perf15MinLong = _Pmc1002Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2, 2),
    _Pmc1002Perf15MinLong_Type()
)
pmc1002Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Perf15MinLong.setStatus("current")
_Pmc1002Perf24HoursShort_Type = Counter32
_Pmc1002Perf24HoursShort_Object = MibScalar
pmc1002Perf24HoursShort = _Pmc1002Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2, 5),
    _Pmc1002Perf24HoursShort_Type()
)
pmc1002Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Perf24HoursShort.setStatus("current")
_Pmc1002Perf24HoursLong_Type = Counter32
_Pmc1002Perf24HoursLong_Object = MibScalar
pmc1002Perf24HoursLong = _Pmc1002Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2, 6),
    _Pmc1002Perf24HoursLong_Type()
)
pmc1002Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002Perf24HoursLong.setStatus("current")
_Pmc1002PerfCurrent15MinElapsedTime_Type = Counter32
_Pmc1002PerfCurrent15MinElapsedTime_Object = MibScalar
pmc1002PerfCurrent15MinElapsedTime = _Pmc1002PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2, 7),
    _Pmc1002PerfCurrent15MinElapsedTime_Type()
)
pmc1002PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002PerfCurrent15MinElapsedTime.setStatus("current")
_Pmc1002PerfCurrent24HoursElapsedTime_Type = Counter32
_Pmc1002PerfCurrent24HoursElapsedTime_Object = MibScalar
pmc1002PerfCurrent24HoursElapsedTime = _Pmc1002PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 1, 2, 8),
    _Pmc1002PerfCurrent24HoursElapsedTime_Type()
)
pmc1002PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002PerfCurrent24HoursElapsedTime.setStatus("current")
_Pmc1002MonClient_ObjectIdentity = ObjectIdentity
pmc1002MonClient = _Pmc1002MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2)
)
_Pmc1002PerfTelecomClientCurrent15StatTable_Object = MibTable
pmc1002PerfTelecomClientCurrent15StatTable = _Pmc1002PerfTelecomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatTable.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatEntry_Object = MibTableRow
pmc1002PerfTelecomClientCurrent15StatEntry = _Pmc1002PerfTelecomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1)
)
pmc1002PerfTelecomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatEntry.setStatus("current")


class _Pmc1002PerfTelecomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pmc1002PerfTelecomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomClientCurrent15StatIndex_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatIndex = _Pmc1002PerfTelecomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 1),
    _Pmc1002PerfTelecomClientCurrent15StatIndex_Type()
)
pmc1002PerfTelecomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatIndex.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent15StatInvCvPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatInvCvPortn = _Pmc1002PerfTelecomClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 2),
    _Pmc1002PerfTelecomClientCurrent15StatInvCvPortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatInvCvPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent15StatCvValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatCvValuePortn = _Pmc1002PerfTelecomClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 3),
    _Pmc1002PerfTelecomClientCurrent15StatCvValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatCvValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent15StatInvEsPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatInvEsPortn = _Pmc1002PerfTelecomClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 4),
    _Pmc1002PerfTelecomClientCurrent15StatInvEsPortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatInvEsPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent15StatEsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatEsValuePortn = _Pmc1002PerfTelecomClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 5),
    _Pmc1002PerfTelecomClientCurrent15StatEsValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatEsValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent15StatInvSesPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatInvSesPortn = _Pmc1002PerfTelecomClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 6),
    _Pmc1002PerfTelecomClientCurrent15StatInvSesPortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatInvSesPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent15StatSesValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatSesValuePortn = _Pmc1002PerfTelecomClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 7),
    _Pmc1002PerfTelecomClientCurrent15StatSesValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatSesValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatInvSefsPortn = _Pmc1002PerfTelecomClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 8),
    _Pmc1002PerfTelecomClientCurrent15StatInvSefsPortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatInvSefsPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatSefsValuePortn = _Pmc1002PerfTelecomClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 9),
    _Pmc1002PerfTelecomClientCurrent15StatSefsValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatSefsValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent15StatInvUasPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatInvUasPortn = _Pmc1002PerfTelecomClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 10),
    _Pmc1002PerfTelecomClientCurrent15StatInvUasPortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatInvUasPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent15StatUasValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent15StatUasValuePortn = _Pmc1002PerfTelecomClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 16, 1, 11),
    _Pmc1002PerfTelecomClientCurrent15StatUasValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent15StatUasValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryPort1Table_Object = MibTable
pmc1002PerfTelecomClientPast15StatHistoryPort1Table = _Pmc1002PerfTelecomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryPort1Table.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pmc1002PerfTelecomClientPast15StatHistoryPort1Entry = _Pmc1002PerfTelecomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1)
)
pmc1002PerfTelecomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pmc1002PerfTelecomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1002PerfTelecomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryPort1Index = _Pmc1002PerfTelecomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 1),
    _Pmc1002PerfTelecomClientPast15StatHistoryPort1Index_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryPort1Index.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1 = _Pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 2),
    _Pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1 = _Pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 3),
    _Pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1 = _Pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 4),
    _Pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1 = _Pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 5),
    _Pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1 = _Pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 6),
    _Pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistorySesValuePort1 = _Pmc1002PerfTelecomClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 7),
    _Pmc1002PerfTelecomClientPast15StatHistorySesValuePort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistorySesValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1 = _Pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 8),
    _Pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1 = _Pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 9),
    _Pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1 = _Pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 10),
    _Pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1 = _Pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 24, 1, 11),
    _Pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1_Type()
)
pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatTable_Object = MibTable
pmc1002PerfTelecomClientCurrent24StatTable = _Pmc1002PerfTelecomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatTable.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatEntry_Object = MibTableRow
pmc1002PerfTelecomClientCurrent24StatEntry = _Pmc1002PerfTelecomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1)
)
pmc1002PerfTelecomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatEntry.setStatus("current")


class _Pmc1002PerfTelecomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pmc1002PerfTelecomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomClientCurrent24StatIndex_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatIndex = _Pmc1002PerfTelecomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 1),
    _Pmc1002PerfTelecomClientCurrent24StatIndex_Type()
)
pmc1002PerfTelecomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatIndex.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent24StatInvCvPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatInvCvPortn = _Pmc1002PerfTelecomClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 2),
    _Pmc1002PerfTelecomClientCurrent24StatInvCvPortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatInvCvPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent24StatCvValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatCvValuePortn = _Pmc1002PerfTelecomClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 3),
    _Pmc1002PerfTelecomClientCurrent24StatCvValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatCvValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent24StatInvEsPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatInvEsPortn = _Pmc1002PerfTelecomClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 4),
    _Pmc1002PerfTelecomClientCurrent24StatInvEsPortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatInvEsPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent24StatEsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatEsValuePortn = _Pmc1002PerfTelecomClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 5),
    _Pmc1002PerfTelecomClientCurrent24StatEsValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatEsValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent24StatInvSesPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatInvSesPortn = _Pmc1002PerfTelecomClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 6),
    _Pmc1002PerfTelecomClientCurrent24StatInvSesPortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatInvSesPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent24StatSesValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatSesValuePortn = _Pmc1002PerfTelecomClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 7),
    _Pmc1002PerfTelecomClientCurrent24StatSesValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatSesValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatInvSefsPortn = _Pmc1002PerfTelecomClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 8),
    _Pmc1002PerfTelecomClientCurrent24StatInvSefsPortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatInvSefsPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatSefsValuePortn = _Pmc1002PerfTelecomClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 9),
    _Pmc1002PerfTelecomClientCurrent24StatSefsValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatSefsValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pmc1002PerfTelecomClientCurrent24StatInvUasPortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatInvUasPortn = _Pmc1002PerfTelecomClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 10),
    _Pmc1002PerfTelecomClientCurrent24StatInvUasPortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatInvUasPortn.setStatus("current")
_Pmc1002PerfTelecomClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomClientCurrent24StatUasValuePortn_Object = MibTableColumn
pmc1002PerfTelecomClientCurrent24StatUasValuePortn = _Pmc1002PerfTelecomClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 32, 1, 11),
    _Pmc1002PerfTelecomClientCurrent24StatUasValuePortn_Type()
)
pmc1002PerfTelecomClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientCurrent24StatUasValuePortn.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryPort1Table_Object = MibTable
pmc1002PerfTelecomClientPast24StatHistoryPort1Table = _Pmc1002PerfTelecomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryPort1Table.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pmc1002PerfTelecomClientPast24StatHistoryPort1Entry = _Pmc1002PerfTelecomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1)
)
pmc1002PerfTelecomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pmc1002PerfTelecomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1002PerfTelecomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryPort1Index = _Pmc1002PerfTelecomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 1),
    _Pmc1002PerfTelecomClientPast24StatHistoryPort1Index_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryPort1Index.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1 = _Pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 2),
    _Pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1 = _Pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 3),
    _Pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1 = _Pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 4),
    _Pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1 = _Pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 5),
    _Pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1 = _Pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 6),
    _Pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistorySesValuePort1 = _Pmc1002PerfTelecomClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 7),
    _Pmc1002PerfTelecomClientPast24StatHistorySesValuePort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistorySesValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1 = _Pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 8),
    _Pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1 = _Pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 9),
    _Pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1 = _Pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 10),
    _Pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1 = _Pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 40, 1, 11),
    _Pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1_Type()
)
pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pmc1002PerfDatacomClientCurrent15StatTable_Object = MibTable
pmc1002PerfDatacomClientCurrent15StatTable = _Pmc1002PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256)
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientCurrent15StatTable.setStatus("current")
_Pmc1002PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pmc1002PerfDatacomClientCurrent15StatEntry = _Pmc1002PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1)
)
pmc1002PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pmc1002PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pmc1002PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc1002PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pmc1002PerfDatacomClientCurrent15StatIndex = _Pmc1002PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 1),
    _Pmc1002PerfDatacomClientCurrent15StatIndex_Type()
)
pmc1002PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 2),
    _Pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInBytesCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatInBytesCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInBytesCountPortn = _Pmc1002perfdatacomclientCurrent15StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 3),
    _Pmc1002perfdatacomclientCurrent15StatInBytesCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInBytesCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 4),
    _Pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInCrcCountPortn = _Pmc1002perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 5),
    _Pmc1002perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 8),
    _Pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn = _Pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 9),
    _Pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 10),
    _Pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn = _Pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 11),
    _Pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 20),
    _Pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn = _Pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 21),
    _Pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 22),
    _Pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn = _Pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 23),
    _Pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 26),
    _Pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn = _Pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 27),
    _Pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 32),
    _Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn = _Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 33),
    _Pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 34),
    _Pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn = _Pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 35),
    _Pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 42),
    _Pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn = _Pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 43),
    _Pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn = _Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 44),
    _Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn = _Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 256, 1, 45),
    _Pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn.setStatus("current")
_Pmc1002PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pmc1002PerfDatacomClientPast15StatHistoryPort1Table = _Pmc1002PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264)
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pmc1002PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pmc1002PerfDatacomClientPast15StatHistoryPort1Entry = _Pmc1002PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1)
)
pmc1002PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pmc1002PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1002PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1002PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pmc1002PerfDatacomClientPast15StatHistoryPort1Index = _Pmc1002PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 1),
    _Pmc1002PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pmc1002PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInBytesCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatInBytesCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInBytesCountInvPort1 = _Pmc1002perfdatacomclientPast15StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 2),
    _Pmc1002perfdatacomclientPast15StatInBytesCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInBytesCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInBytesCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatInBytesCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInBytesCountPort1 = _Pmc1002perfdatacomclientPast15StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 3),
    _Pmc1002perfdatacomclientPast15StatInBytesCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInBytesCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInCrcCountInvPort1 = _Pmc1002perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 4),
    _Pmc1002perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInCrcCountPort1 = _Pmc1002perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 5),
    _Pmc1002perfdatacomclientPast15StatInCrcCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 8),
    _Pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInBroadcastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatInBroadcastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInBroadcastCountPort1 = _Pmc1002perfdatacomclientPast15StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 9),
    _Pmc1002perfdatacomclientPast15StatInBroadcastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInBroadcastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 10),
    _Pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInMulticastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatInMulticastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInMulticastCountPort1 = _Pmc1002perfdatacomclientPast15StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 11),
    _Pmc1002perfdatacomclientPast15StatInMulticastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInMulticastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 20),
    _Pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInUnicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatInUnicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInUnicastCountPort1 = _Pmc1002perfdatacomclientPast15StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 21),
    _Pmc1002perfdatacomclientPast15StatInUnicastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInUnicastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 22),
    _Pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatInNonunicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatInNonunicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatInNonunicastCountPort1 = _Pmc1002perfdatacomclientPast15StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 23),
    _Pmc1002perfdatacomclientPast15StatInNonunicastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatInNonunicastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1 = _Pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 26),
    _Pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutBytesCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatOutBytesCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutBytesCountPort1 = _Pmc1002perfdatacomclientPast15StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 27),
    _Pmc1002perfdatacomclientPast15StatOutBytesCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutBytesCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 32),
    _Pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1 = _Pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 33),
    _Pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 34),
    _Pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutMulticastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatOutMulticastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutMulticastCountPort1 = _Pmc1002perfdatacomclientPast15StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 35),
    _Pmc1002perfdatacomclientPast15StatOutMulticastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutMulticastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 42),
    _Pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutUnicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatOutUnicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutUnicastCountPort1 = _Pmc1002perfdatacomclientPast15StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 43),
    _Pmc1002perfdatacomclientPast15StatOutUnicastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutUnicastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1 = _Pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 44),
    _Pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1 = _Pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 264, 1, 45),
    _Pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1_Type()
)
pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1.setStatus("current")
_Pmc1002PerfDatacomClientCurrent24StatTable_Object = MibTable
pmc1002PerfDatacomClientCurrent24StatTable = _Pmc1002PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272)
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientCurrent24StatTable.setStatus("current")
_Pmc1002PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pmc1002PerfDatacomClientCurrent24StatEntry = _Pmc1002PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1)
)
pmc1002PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pmc1002PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pmc1002PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc1002PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pmc1002PerfDatacomClientCurrent24StatIndex = _Pmc1002PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 1),
    _Pmc1002PerfDatacomClientCurrent24StatIndex_Type()
)
pmc1002PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 2),
    _Pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInBytesCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatInBytesCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInBytesCountPortn = _Pmc1002perfdatacomclientCurrent24StatInBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 3),
    _Pmc1002perfdatacomclientCurrent24StatInBytesCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInBytesCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 4),
    _Pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInCrcCountPortn = _Pmc1002perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 5),
    _Pmc1002perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 8),
    _Pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn = _Pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 9),
    _Pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 10),
    _Pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn = _Pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 11),
    _Pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 20),
    _Pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn = _Pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 21),
    _Pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 22),
    _Pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn = _Pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 23),
    _Pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 26),
    _Pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn = _Pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 27),
    _Pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 32),
    _Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn = _Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 33),
    _Pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 34),
    _Pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn = _Pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 35),
    _Pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 42),
    _Pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn = _Pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 43),
    _Pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type = EkiOnOff
_Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn = _Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 44),
    _Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn.setStatus("current")
_Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Type = Counter64
_Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Object = MibTableColumn
pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn = _Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 272, 1, 45),
    _Pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn_Type()
)
pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn.setStatus("current")
_Pmc1002PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pmc1002PerfDatacomClientPast24StatHistoryPort1Table = _Pmc1002PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280)
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pmc1002PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pmc1002PerfDatacomClientPast24StatHistoryPort1Entry = _Pmc1002PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1)
)
pmc1002PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pmc1002PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1002PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1002PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pmc1002PerfDatacomClientPast24StatHistoryPort1Index = _Pmc1002PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 1),
    _Pmc1002PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pmc1002PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInBytesCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatInBytesCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInBytesCountInvPort1 = _Pmc1002perfdatacomclientPast24StatInBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 2),
    _Pmc1002perfdatacomclientPast24StatInBytesCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatInBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInBytesCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInBytesCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatInBytesCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInBytesCountPort1 = _Pmc1002perfdatacomclientPast24StatInBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 3),
    _Pmc1002perfdatacomclientPast24StatInBytesCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatInBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInBytesCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInCrcCountInvPort1 = _Pmc1002perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 4),
    _Pmc1002perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInCrcCountPort1 = _Pmc1002perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 5),
    _Pmc1002perfdatacomclientPast24StatInCrcCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 8),
    _Pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInBroadcastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatInBroadcastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInBroadcastCountPort1 = _Pmc1002perfdatacomclientPast24StatInBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 9),
    _Pmc1002perfdatacomclientPast24StatInBroadcastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatInBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInBroadcastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 10),
    _Pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInMulticastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatInMulticastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInMulticastCountPort1 = _Pmc1002perfdatacomclientPast24StatInMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 11),
    _Pmc1002perfdatacomclientPast24StatInMulticastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatInMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInMulticastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 20),
    _Pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInUnicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatInUnicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInUnicastCountPort1 = _Pmc1002perfdatacomclientPast24StatInUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 21),
    _Pmc1002perfdatacomclientPast24StatInUnicastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatInUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInUnicastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 22),
    _Pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatInNonunicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatInNonunicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatInNonunicastCountPort1 = _Pmc1002perfdatacomclientPast24StatInNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 23),
    _Pmc1002perfdatacomclientPast24StatInNonunicastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatInNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatInNonunicastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1 = _Pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 26),
    _Pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutBytesCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatOutBytesCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutBytesCountPort1 = _Pmc1002perfdatacomclientPast24StatOutBytesCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 27),
    _Pmc1002perfdatacomclientPast24StatOutBytesCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutBytesCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutBytesCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 32),
    _Pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1 = _Pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 33),
    _Pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 34),
    _Pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutMulticastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatOutMulticastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutMulticastCountPort1 = _Pmc1002perfdatacomclientPast24StatOutMulticastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 35),
    _Pmc1002perfdatacomclientPast24StatOutMulticastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutMulticastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutMulticastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 42),
    _Pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutUnicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatOutUnicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutUnicastCountPort1 = _Pmc1002perfdatacomclientPast24StatOutUnicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 43),
    _Pmc1002perfdatacomclientPast24StatOutUnicastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutUnicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutUnicastCountPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Type = EkiOnOff
_Pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1 = _Pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 44),
    _Pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1.setStatus("current")
_Pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1_Type = Counter64
_Pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1_Object = MibTableColumn
pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1 = _Pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 2, 280, 1, 45),
    _Pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1_Type()
)
pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1.setStatus("current")
_Pmc1002MonLine_ObjectIdentity = ObjectIdentity
pmc1002MonLine = _Pmc1002MonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3)
)
_Pmc1002PerfTelecomLineCurrent15StatTable_Object = MibTable
pmc1002PerfTelecomLineCurrent15StatTable = _Pmc1002PerfTelecomLineCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatTable.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatEntry_Object = MibTableRow
pmc1002PerfTelecomLineCurrent15StatEntry = _Pmc1002PerfTelecomLineCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1)
)
pmc1002PerfTelecomLineCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomLineCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatEntry.setStatus("current")


class _Pmc1002PerfTelecomLineCurrent15StatIndex_Type(Integer32):
    """Custom type pmc1002PerfTelecomLineCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomLineCurrent15StatIndex_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomLineCurrent15StatIndex_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatIndex = _Pmc1002PerfTelecomLineCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 1),
    _Pmc1002PerfTelecomLineCurrent15StatIndex_Type()
)
pmc1002PerfTelecomLineCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatIndex.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatInvCvPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent15StatInvCvPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatInvCvPortn = _Pmc1002PerfTelecomLineCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 2),
    _Pmc1002PerfTelecomLineCurrent15StatInvCvPortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatInvCvPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatCvValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent15StatCvValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatCvValuePortn = _Pmc1002PerfTelecomLineCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 3),
    _Pmc1002PerfTelecomLineCurrent15StatCvValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatCvValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatInvEsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent15StatInvEsPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatInvEsPortn = _Pmc1002PerfTelecomLineCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 4),
    _Pmc1002PerfTelecomLineCurrent15StatInvEsPortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatInvEsPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatEsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent15StatEsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatEsValuePortn = _Pmc1002PerfTelecomLineCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 5),
    _Pmc1002PerfTelecomLineCurrent15StatEsValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatEsValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatInvSesPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent15StatInvSesPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatInvSesPortn = _Pmc1002PerfTelecomLineCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 6),
    _Pmc1002PerfTelecomLineCurrent15StatInvSesPortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatInvSesPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatSesValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent15StatSesValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatSesValuePortn = _Pmc1002PerfTelecomLineCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 7),
    _Pmc1002PerfTelecomLineCurrent15StatSesValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatSesValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent15StatInvSefsPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatInvSefsPortn = _Pmc1002PerfTelecomLineCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 8),
    _Pmc1002PerfTelecomLineCurrent15StatInvSefsPortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatInvSefsPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatSefsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent15StatSefsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatSefsValuePortn = _Pmc1002PerfTelecomLineCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 9),
    _Pmc1002PerfTelecomLineCurrent15StatSefsValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatSefsValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatInvUasPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent15StatInvUasPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatInvUasPortn = _Pmc1002PerfTelecomLineCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 10),
    _Pmc1002PerfTelecomLineCurrent15StatInvUasPortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatInvUasPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent15StatUasValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent15StatUasValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent15StatUasValuePortn = _Pmc1002PerfTelecomLineCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 128, 1, 11),
    _Pmc1002PerfTelecomLineCurrent15StatUasValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent15StatUasValuePortn.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryPort1Table_Object = MibTable
pmc1002PerfTelecomLinePast15StatHistoryPort1Table = _Pmc1002PerfTelecomLinePast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryPort1Table.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryPort1Entry_Object = MibTableRow
pmc1002PerfTelecomLinePast15StatHistoryPort1Entry = _Pmc1002PerfTelecomLinePast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1)
)
pmc1002PerfTelecomLinePast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomLinePast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryPort1Entry.setStatus("current")


class _Pmc1002PerfTelecomLinePast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1002PerfTelecomLinePast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomLinePast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomLinePast15StatHistoryPort1Index_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryPort1Index = _Pmc1002PerfTelecomLinePast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 1),
    _Pmc1002PerfTelecomLinePast15StatHistoryPort1Index_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryPort1Index.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1 = _Pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 2),
    _Pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1 = _Pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 3),
    _Pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1 = _Pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 4),
    _Pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1 = _Pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 5),
    _Pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1 = _Pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 6),
    _Pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistorySesValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast15StatHistorySesValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistorySesValuePort1 = _Pmc1002PerfTelecomLinePast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 7),
    _Pmc1002PerfTelecomLinePast15StatHistorySesValuePort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistorySesValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1 = _Pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 8),
    _Pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1 = _Pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 9),
    _Pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1 = _Pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 10),
    _Pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1 = _Pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 129, 1, 11),
    _Pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1_Type()
)
pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatTable_Object = MibTable
pmc1002PerfTelecomLineCurrent24StatTable = _Pmc1002PerfTelecomLineCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatTable.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatEntry_Object = MibTableRow
pmc1002PerfTelecomLineCurrent24StatEntry = _Pmc1002PerfTelecomLineCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1)
)
pmc1002PerfTelecomLineCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomLineCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatEntry.setStatus("current")


class _Pmc1002PerfTelecomLineCurrent24StatIndex_Type(Integer32):
    """Custom type pmc1002PerfTelecomLineCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomLineCurrent24StatIndex_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomLineCurrent24StatIndex_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatIndex = _Pmc1002PerfTelecomLineCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 1),
    _Pmc1002PerfTelecomLineCurrent24StatIndex_Type()
)
pmc1002PerfTelecomLineCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatIndex.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatInvCvPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent24StatInvCvPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatInvCvPortn = _Pmc1002PerfTelecomLineCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 2),
    _Pmc1002PerfTelecomLineCurrent24StatInvCvPortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatInvCvPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatCvValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent24StatCvValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatCvValuePortn = _Pmc1002PerfTelecomLineCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 3),
    _Pmc1002PerfTelecomLineCurrent24StatCvValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatCvValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatInvEsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent24StatInvEsPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatInvEsPortn = _Pmc1002PerfTelecomLineCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 4),
    _Pmc1002PerfTelecomLineCurrent24StatInvEsPortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatInvEsPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatEsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent24StatEsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatEsValuePortn = _Pmc1002PerfTelecomLineCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 5),
    _Pmc1002PerfTelecomLineCurrent24StatEsValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatEsValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatInvSesPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent24StatInvSesPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatInvSesPortn = _Pmc1002PerfTelecomLineCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 6),
    _Pmc1002PerfTelecomLineCurrent24StatInvSesPortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatInvSesPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatSesValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent24StatSesValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatSesValuePortn = _Pmc1002PerfTelecomLineCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 7),
    _Pmc1002PerfTelecomLineCurrent24StatSesValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatSesValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent24StatInvSefsPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatInvSefsPortn = _Pmc1002PerfTelecomLineCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 8),
    _Pmc1002PerfTelecomLineCurrent24StatInvSefsPortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatInvSefsPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatSefsValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent24StatSefsValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatSefsValuePortn = _Pmc1002PerfTelecomLineCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 9),
    _Pmc1002PerfTelecomLineCurrent24StatSefsValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatSefsValuePortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatInvUasPortn_Type = EkiOnOff
_Pmc1002PerfTelecomLineCurrent24StatInvUasPortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatInvUasPortn = _Pmc1002PerfTelecomLineCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 10),
    _Pmc1002PerfTelecomLineCurrent24StatInvUasPortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatInvUasPortn.setStatus("current")
_Pmc1002PerfTelecomLineCurrent24StatUasValuePortn_Type = Unsigned32
_Pmc1002PerfTelecomLineCurrent24StatUasValuePortn_Object = MibTableColumn
pmc1002PerfTelecomLineCurrent24StatUasValuePortn = _Pmc1002PerfTelecomLineCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 130, 1, 11),
    _Pmc1002PerfTelecomLineCurrent24StatUasValuePortn_Type()
)
pmc1002PerfTelecomLineCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLineCurrent24StatUasValuePortn.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryPort1Table_Object = MibTable
pmc1002PerfTelecomLinePast24StatHistoryPort1Table = _Pmc1002PerfTelecomLinePast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131)
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryPort1Table.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryPort1Entry_Object = MibTableRow
pmc1002PerfTelecomLinePast24StatHistoryPort1Entry = _Pmc1002PerfTelecomLinePast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1)
)
pmc1002PerfTelecomLinePast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002PerfTelecomLinePast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryPort1Entry.setStatus("current")


class _Pmc1002PerfTelecomLinePast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pmc1002PerfTelecomLinePast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002PerfTelecomLinePast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pmc1002PerfTelecomLinePast24StatHistoryPort1Index_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryPort1Index = _Pmc1002PerfTelecomLinePast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 1),
    _Pmc1002PerfTelecomLinePast24StatHistoryPort1Index_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryPort1Index.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1 = _Pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 2),
    _Pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1 = _Pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 3),
    _Pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1 = _Pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 4),
    _Pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1 = _Pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 5),
    _Pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1 = _Pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 6),
    _Pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistorySesValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast24StatHistorySesValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistorySesValuePort1 = _Pmc1002PerfTelecomLinePast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 7),
    _Pmc1002PerfTelecomLinePast24StatHistorySesValuePort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistorySesValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1 = _Pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 8),
    _Pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1 = _Pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 9),
    _Pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1 = _Pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 10),
    _Pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1.setStatus("current")
_Pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1_Type = Unsigned32
_Pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1_Object = MibTableColumn
pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1 = _Pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 3, 131, 1, 11),
    _Pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1_Type()
)
pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1.setStatus("current")
_Pmc1002Rmon_ObjectIdentity = ObjectIdentity
pmc1002Rmon = _Pmc1002Rmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4)
)
_Pmc1002RmonClient_ObjectIdentity = ObjectIdentity
pmc1002RmonClient = _Pmc1002RmonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1)
)
_Pmc1002MonupRmonByteCntTable_Object = MibTable
pmc1002MonupRmonByteCntTable = _Pmc1002MonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 16)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonByteCntTable.setStatus("current")
_Pmc1002MonupRmonByteCntEntry_Object = MibTableRow
pmc1002MonupRmonByteCntEntry = _Pmc1002MonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 16, 1)
)
pmc1002MonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonByteCntEntry.setStatus("current")


class _Pmc1002MonupRmonByteCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonByteCntIndex_Object = MibTableColumn
pmc1002MonupRmonByteCntIndex = _Pmc1002MonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 16, 1, 1),
    _Pmc1002MonupRmonByteCntIndex_Type()
)
pmc1002MonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonByteCntIndex.setStatus("current")
_Pmc1002MonupRmonByteCntValuePortn_Type = Counter64
_Pmc1002MonupRmonByteCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonByteCntValuePortn = _Pmc1002MonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 16, 1, 2),
    _Pmc1002MonupRmonByteCntValuePortn_Type()
)
pmc1002MonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonByteCntValuePortn.setStatus("current")
_Pmc1002MonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonByteCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonByteCntErrorPortn = _Pmc1002MonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 16, 1, 3),
    _Pmc1002MonupRmonByteCntErrorPortn_Type()
)
pmc1002MonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonByteCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonByteCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonByteCntOverloadPortn = _Pmc1002MonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 16, 1, 4),
    _Pmc1002MonupRmonByteCntOverloadPortn_Type()
)
pmc1002MonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonByteCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonCrcErrorCntTable_Object = MibTable
pmc1002MonupRmonCrcErrorCntTable = _Pmc1002MonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 24)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonCrcErrorCntTable.setStatus("current")
_Pmc1002MonupRmonCrcErrorCntEntry_Object = MibTableRow
pmc1002MonupRmonCrcErrorCntEntry = _Pmc1002MonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 24, 1)
)
pmc1002MonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonCrcErrorCntEntry.setStatus("current")


class _Pmc1002MonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonCrcErrorCntIndex_Object = MibTableColumn
pmc1002MonupRmonCrcErrorCntIndex = _Pmc1002MonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 24, 1, 1),
    _Pmc1002MonupRmonCrcErrorCntIndex_Type()
)
pmc1002MonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonCrcErrorCntIndex.setStatus("current")
_Pmc1002MonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pmc1002MonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonCrcErrorCntValuePortn = _Pmc1002MonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 24, 1, 2),
    _Pmc1002MonupRmonCrcErrorCntValuePortn_Type()
)
pmc1002MonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pmc1002MonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonCrcErrorCntErrorPortn = _Pmc1002MonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 24, 1, 3),
    _Pmc1002MonupRmonCrcErrorCntErrorPortn_Type()
)
pmc1002MonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonCrcErrorCntOverloadPortn = _Pmc1002MonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 24, 1, 4),
    _Pmc1002MonupRmonCrcErrorCntOverloadPortn_Type()
)
pmc1002MonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonPacketsCntTable_Object = MibTable
pmc1002MonupRmonPacketsCntTable = _Pmc1002MonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 32)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonPacketsCntTable.setStatus("current")
_Pmc1002MonupRmonPacketsCntEntry_Object = MibTableRow
pmc1002MonupRmonPacketsCntEntry = _Pmc1002MonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 32, 1)
)
pmc1002MonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonPacketsCntEntry.setStatus("current")


class _Pmc1002MonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonPacketsCntIndex_Object = MibTableColumn
pmc1002MonupRmonPacketsCntIndex = _Pmc1002MonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 32, 1, 1),
    _Pmc1002MonupRmonPacketsCntIndex_Type()
)
pmc1002MonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPacketsCntIndex.setStatus("current")
_Pmc1002MonupRmonPacketsCntValuePortn_Type = Counter64
_Pmc1002MonupRmonPacketsCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonPacketsCntValuePortn = _Pmc1002MonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 32, 1, 2),
    _Pmc1002MonupRmonPacketsCntValuePortn_Type()
)
pmc1002MonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPacketsCntValuePortn.setStatus("current")
_Pmc1002MonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonPacketsCntErrorPortn = _Pmc1002MonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 32, 1, 3),
    _Pmc1002MonupRmonPacketsCntErrorPortn_Type()
)
pmc1002MonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPacketsCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonPacketsCntOverloadPortn = _Pmc1002MonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 32, 1, 4),
    _Pmc1002MonupRmonPacketsCntOverloadPortn_Type()
)
pmc1002MonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonBroadcastCntTable_Object = MibTable
pmc1002MonupRmonBroadcastCntTable = _Pmc1002MonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 40)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonBroadcastCntTable.setStatus("current")
_Pmc1002MonupRmonBroadcastCntEntry_Object = MibTableRow
pmc1002MonupRmonBroadcastCntEntry = _Pmc1002MonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 40, 1)
)
pmc1002MonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonBroadcastCntEntry.setStatus("current")


class _Pmc1002MonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonBroadcastCntIndex_Object = MibTableColumn
pmc1002MonupRmonBroadcastCntIndex = _Pmc1002MonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 40, 1, 1),
    _Pmc1002MonupRmonBroadcastCntIndex_Type()
)
pmc1002MonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBroadcastCntIndex.setStatus("current")
_Pmc1002MonupRmonBroadcastCntValuePortn_Type = Counter64
_Pmc1002MonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonBroadcastCntValuePortn = _Pmc1002MonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 40, 1, 2),
    _Pmc1002MonupRmonBroadcastCntValuePortn_Type()
)
pmc1002MonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBroadcastCntValuePortn.setStatus("current")
_Pmc1002MonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonBroadcastCntErrorPortn = _Pmc1002MonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 40, 1, 3),
    _Pmc1002MonupRmonBroadcastCntErrorPortn_Type()
)
pmc1002MonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonBroadcastCntOverloadPortn = _Pmc1002MonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 40, 1, 4),
    _Pmc1002MonupRmonBroadcastCntOverloadPortn_Type()
)
pmc1002MonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonMulticastCntTable_Object = MibTable
pmc1002MonupRmonMulticastCntTable = _Pmc1002MonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 48)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonMulticastCntTable.setStatus("current")
_Pmc1002MonupRmonMulticastCntEntry_Object = MibTableRow
pmc1002MonupRmonMulticastCntEntry = _Pmc1002MonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 48, 1)
)
pmc1002MonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonMulticastCntEntry.setStatus("current")


class _Pmc1002MonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonMulticastCntIndex_Object = MibTableColumn
pmc1002MonupRmonMulticastCntIndex = _Pmc1002MonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 48, 1, 1),
    _Pmc1002MonupRmonMulticastCntIndex_Type()
)
pmc1002MonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonMulticastCntIndex.setStatus("current")
_Pmc1002MonupRmonMulticastCntValuePortn_Type = Counter64
_Pmc1002MonupRmonMulticastCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonMulticastCntValuePortn = _Pmc1002MonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 48, 1, 2),
    _Pmc1002MonupRmonMulticastCntValuePortn_Type()
)
pmc1002MonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonMulticastCntValuePortn.setStatus("current")
_Pmc1002MonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonMulticastCntErrorPortn = _Pmc1002MonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 48, 1, 3),
    _Pmc1002MonupRmonMulticastCntErrorPortn_Type()
)
pmc1002MonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonMulticastCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonMulticastCntOverloadPortn = _Pmc1002MonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 48, 1, 4),
    _Pmc1002MonupRmonMulticastCntOverloadPortn_Type()
)
pmc1002MonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonTimerCntTable_Object = MibTable
pmc1002MonupRmonTimerCntTable = _Pmc1002MonupRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 56)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonTimerCntTable.setStatus("current")
_Pmc1002MonupRmonTimerCntEntry_Object = MibTableRow
pmc1002MonupRmonTimerCntEntry = _Pmc1002MonupRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 56, 1)
)
pmc1002MonupRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonTimerCntEntry.setStatus("current")


class _Pmc1002MonupRmonTimerCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonTimerCntIndex_Object = MibTableColumn
pmc1002MonupRmonTimerCntIndex = _Pmc1002MonupRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 56, 1, 1),
    _Pmc1002MonupRmonTimerCntIndex_Type()
)
pmc1002MonupRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonTimerCntIndex.setStatus("current")
_Pmc1002MonupRmonTimerCntValuePortn_Type = Counter64
_Pmc1002MonupRmonTimerCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonTimerCntValuePortn = _Pmc1002MonupRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 56, 1, 2),
    _Pmc1002MonupRmonTimerCntValuePortn_Type()
)
pmc1002MonupRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonTimerCntValuePortn.setStatus("current")
_Pmc1002MonupRmonTimerCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonTimerCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonTimerCntErrorPortn = _Pmc1002MonupRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 56, 1, 3),
    _Pmc1002MonupRmonTimerCntErrorPortn_Type()
)
pmc1002MonupRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonTimerCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonTimerCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonTimerCntOverloadPortn = _Pmc1002MonupRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 56, 1, 4),
    _Pmc1002MonupRmonTimerCntOverloadPortn_Type()
)
pmc1002MonupRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonTimerCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonPauseFrameCntTable_Object = MibTable
pmc1002MonupRmonPauseFrameCntTable = _Pmc1002MonupRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 64)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonPauseFrameCntTable.setStatus("current")
_Pmc1002MonupRmonPauseFrameCntEntry_Object = MibTableRow
pmc1002MonupRmonPauseFrameCntEntry = _Pmc1002MonupRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 64, 1)
)
pmc1002MonupRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonPauseFrameCntEntry.setStatus("current")


class _Pmc1002MonupRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonPauseFrameCntIndex_Object = MibTableColumn
pmc1002MonupRmonPauseFrameCntIndex = _Pmc1002MonupRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 64, 1, 1),
    _Pmc1002MonupRmonPauseFrameCntIndex_Type()
)
pmc1002MonupRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPauseFrameCntIndex.setStatus("current")
_Pmc1002MonupRmonPauseFrameCntValuePortn_Type = Counter64
_Pmc1002MonupRmonPauseFrameCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonPauseFrameCntValuePortn = _Pmc1002MonupRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 64, 1, 2),
    _Pmc1002MonupRmonPauseFrameCntValuePortn_Type()
)
pmc1002MonupRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPauseFrameCntValuePortn.setStatus("current")
_Pmc1002MonupRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonPauseFrameCntErrorPortn = _Pmc1002MonupRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 64, 1, 3),
    _Pmc1002MonupRmonPauseFrameCntErrorPortn_Type()
)
pmc1002MonupRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPauseFrameCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonPauseFrameCntOverloadPortn = _Pmc1002MonupRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 64, 1, 4),
    _Pmc1002MonupRmonPauseFrameCntOverloadPortn_Type()
)
pmc1002MonupRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonDropFrameCntTable_Object = MibTable
pmc1002MonupRmonDropFrameCntTable = _Pmc1002MonupRmonDropFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 72)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonDropFrameCntTable.setStatus("current")
_Pmc1002MonupRmonDropFrameCntEntry_Object = MibTableRow
pmc1002MonupRmonDropFrameCntEntry = _Pmc1002MonupRmonDropFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 72, 1)
)
pmc1002MonupRmonDropFrameCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonDropFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonDropFrameCntEntry.setStatus("current")


class _Pmc1002MonupRmonDropFrameCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonDropFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonDropFrameCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonDropFrameCntIndex_Object = MibTableColumn
pmc1002MonupRmonDropFrameCntIndex = _Pmc1002MonupRmonDropFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 72, 1, 1),
    _Pmc1002MonupRmonDropFrameCntIndex_Type()
)
pmc1002MonupRmonDropFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonDropFrameCntIndex.setStatus("current")
_Pmc1002MonupRmonDropFrameCntValuePortn_Type = Counter64
_Pmc1002MonupRmonDropFrameCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonDropFrameCntValuePortn = _Pmc1002MonupRmonDropFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 72, 1, 2),
    _Pmc1002MonupRmonDropFrameCntValuePortn_Type()
)
pmc1002MonupRmonDropFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonDropFrameCntValuePortn.setStatus("current")
_Pmc1002MonupRmonDropFrameCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonDropFrameCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonDropFrameCntErrorPortn = _Pmc1002MonupRmonDropFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 72, 1, 3),
    _Pmc1002MonupRmonDropFrameCntErrorPortn_Type()
)
pmc1002MonupRmonDropFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonDropFrameCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonDropFrameCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonDropFrameCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonDropFrameCntOverloadPortn = _Pmc1002MonupRmonDropFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 72, 1, 4),
    _Pmc1002MonupRmonDropFrameCntOverloadPortn_Type()
)
pmc1002MonupRmonDropFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonDropFrameCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonBitsCntTable_Object = MibTable
pmc1002MonupRmonBitsCntTable = _Pmc1002MonupRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 80)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonBitsCntTable.setStatus("current")
_Pmc1002MonupRmonBitsCntEntry_Object = MibTableRow
pmc1002MonupRmonBitsCntEntry = _Pmc1002MonupRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 80, 1)
)
pmc1002MonupRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonBitsCntEntry.setStatus("current")


class _Pmc1002MonupRmonBitsCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonBitsCntIndex_Object = MibTableColumn
pmc1002MonupRmonBitsCntIndex = _Pmc1002MonupRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 80, 1, 1),
    _Pmc1002MonupRmonBitsCntIndex_Type()
)
pmc1002MonupRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBitsCntIndex.setStatus("current")
_Pmc1002MonupRmonBitsCntValuePortn_Type = Counter64
_Pmc1002MonupRmonBitsCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonBitsCntValuePortn = _Pmc1002MonupRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 80, 1, 2),
    _Pmc1002MonupRmonBitsCntValuePortn_Type()
)
pmc1002MonupRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBitsCntValuePortn.setStatus("current")
_Pmc1002MonupRmonBitsCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonBitsCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonBitsCntErrorPortn = _Pmc1002MonupRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 80, 1, 3),
    _Pmc1002MonupRmonBitsCntErrorPortn_Type()
)
pmc1002MonupRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBitsCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonBitsCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonBitsCntOverloadPortn = _Pmc1002MonupRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 80, 1, 4),
    _Pmc1002MonupRmonBitsCntOverloadPortn_Type()
)
pmc1002MonupRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonBitsCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonUnicastCntTable_Object = MibTable
pmc1002MonupRmonUnicastCntTable = _Pmc1002MonupRmonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 88)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonUnicastCntTable.setStatus("current")
_Pmc1002MonupRmonUnicastCntEntry_Object = MibTableRow
pmc1002MonupRmonUnicastCntEntry = _Pmc1002MonupRmonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 88, 1)
)
pmc1002MonupRmonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonUnicastCntEntry.setStatus("current")


class _Pmc1002MonupRmonUnicastCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonUnicastCntIndex_Object = MibTableColumn
pmc1002MonupRmonUnicastCntIndex = _Pmc1002MonupRmonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 88, 1, 1),
    _Pmc1002MonupRmonUnicastCntIndex_Type()
)
pmc1002MonupRmonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonUnicastCntIndex.setStatus("current")
_Pmc1002MonupRmonUnicastCntValuePortn_Type = Counter64
_Pmc1002MonupRmonUnicastCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonUnicastCntValuePortn = _Pmc1002MonupRmonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 88, 1, 2),
    _Pmc1002MonupRmonUnicastCntValuePortn_Type()
)
pmc1002MonupRmonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonUnicastCntValuePortn.setStatus("current")
_Pmc1002MonupRmonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonUnicastCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonUnicastCntErrorPortn = _Pmc1002MonupRmonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 88, 1, 3),
    _Pmc1002MonupRmonUnicastCntErrorPortn_Type()
)
pmc1002MonupRmonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonUnicastCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonUnicastCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonUnicastCntOverloadPortn = _Pmc1002MonupRmonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 88, 1, 4),
    _Pmc1002MonupRmonUnicastCntOverloadPortn_Type()
)
pmc1002MonupRmonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonUnicastCntOverloadPortn.setStatus("current")
_Pmc1002MonupRmonNonUnicastCntTable_Object = MibTable
pmc1002MonupRmonNonUnicastCntTable = _Pmc1002MonupRmonNonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 96)
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonNonUnicastCntTable.setStatus("current")
_Pmc1002MonupRmonNonUnicastCntEntry_Object = MibTableRow
pmc1002MonupRmonNonUnicastCntEntry = _Pmc1002MonupRmonNonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 96, 1)
)
pmc1002MonupRmonNonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MonupRmonNonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MonupRmonNonUnicastCntEntry.setStatus("current")


class _Pmc1002MonupRmonNonUnicastCntIndex_Type(Integer32):
    """Custom type pmc1002MonupRmonNonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MonupRmonNonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MonupRmonNonUnicastCntIndex_Object = MibTableColumn
pmc1002MonupRmonNonUnicastCntIndex = _Pmc1002MonupRmonNonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 96, 1, 1),
    _Pmc1002MonupRmonNonUnicastCntIndex_Type()
)
pmc1002MonupRmonNonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonNonUnicastCntIndex.setStatus("current")
_Pmc1002MonupRmonNonUnicastCntValuePortn_Type = Counter64
_Pmc1002MonupRmonNonUnicastCntValuePortn_Object = MibTableColumn
pmc1002MonupRmonNonUnicastCntValuePortn = _Pmc1002MonupRmonNonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 96, 1, 2),
    _Pmc1002MonupRmonNonUnicastCntValuePortn_Type()
)
pmc1002MonupRmonNonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonNonUnicastCntValuePortn.setStatus("current")
_Pmc1002MonupRmonNonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc1002MonupRmonNonUnicastCntErrorPortn_Object = MibTableColumn
pmc1002MonupRmonNonUnicastCntErrorPortn = _Pmc1002MonupRmonNonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 96, 1, 3),
    _Pmc1002MonupRmonNonUnicastCntErrorPortn_Type()
)
pmc1002MonupRmonNonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonNonUnicastCntErrorPortn.setStatus("current")
_Pmc1002MonupRmonNonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MonupRmonNonUnicastCntOverloadPortn_Object = MibTableColumn
pmc1002MonupRmonNonUnicastCntOverloadPortn = _Pmc1002MonupRmonNonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 96, 1, 4),
    _Pmc1002MonupRmonNonUnicastCntOverloadPortn_Type()
)
pmc1002MonupRmonNonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MonupRmonNonUnicastCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonByteCntTable_Object = MibTable
pmc1002MondwRmonByteCntTable = _Pmc1002MondwRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 112)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonByteCntTable.setStatus("current")
_Pmc1002MondwRmonByteCntEntry_Object = MibTableRow
pmc1002MondwRmonByteCntEntry = _Pmc1002MondwRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 112, 1)
)
pmc1002MondwRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonByteCntEntry.setStatus("current")


class _Pmc1002MondwRmonByteCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonByteCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonByteCntIndex_Object = MibTableColumn
pmc1002MondwRmonByteCntIndex = _Pmc1002MondwRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 112, 1, 1),
    _Pmc1002MondwRmonByteCntIndex_Type()
)
pmc1002MondwRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonByteCntIndex.setStatus("current")
_Pmc1002MondwRmonByteCntValuePortn_Type = Counter64
_Pmc1002MondwRmonByteCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonByteCntValuePortn = _Pmc1002MondwRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 112, 1, 2),
    _Pmc1002MondwRmonByteCntValuePortn_Type()
)
pmc1002MondwRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonByteCntValuePortn.setStatus("current")
_Pmc1002MondwRmonByteCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonByteCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonByteCntErrorPortn = _Pmc1002MondwRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 112, 1, 3),
    _Pmc1002MondwRmonByteCntErrorPortn_Type()
)
pmc1002MondwRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonByteCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonByteCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonByteCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonByteCntOverloadPortn = _Pmc1002MondwRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 112, 1, 4),
    _Pmc1002MondwRmonByteCntOverloadPortn_Type()
)
pmc1002MondwRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonByteCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonCrcErrorCntTable_Object = MibTable
pmc1002MondwRmonCrcErrorCntTable = _Pmc1002MondwRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 120)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonCrcErrorCntTable.setStatus("current")
_Pmc1002MondwRmonCrcErrorCntEntry_Object = MibTableRow
pmc1002MondwRmonCrcErrorCntEntry = _Pmc1002MondwRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 120, 1)
)
pmc1002MondwRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonCrcErrorCntEntry.setStatus("current")


class _Pmc1002MondwRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonCrcErrorCntIndex_Object = MibTableColumn
pmc1002MondwRmonCrcErrorCntIndex = _Pmc1002MondwRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 120, 1, 1),
    _Pmc1002MondwRmonCrcErrorCntIndex_Type()
)
pmc1002MondwRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonCrcErrorCntIndex.setStatus("current")
_Pmc1002MondwRmonCrcErrorCntValuePortn_Type = Counter64
_Pmc1002MondwRmonCrcErrorCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonCrcErrorCntValuePortn = _Pmc1002MondwRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 120, 1, 2),
    _Pmc1002MondwRmonCrcErrorCntValuePortn_Type()
)
pmc1002MondwRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonCrcErrorCntValuePortn.setStatus("current")
_Pmc1002MondwRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonCrcErrorCntErrorPortn = _Pmc1002MondwRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 120, 1, 3),
    _Pmc1002MondwRmonCrcErrorCntErrorPortn_Type()
)
pmc1002MondwRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonCrcErrorCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonCrcErrorCntOverloadPortn = _Pmc1002MondwRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 120, 1, 4),
    _Pmc1002MondwRmonCrcErrorCntOverloadPortn_Type()
)
pmc1002MondwRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonPacketsCntTable_Object = MibTable
pmc1002MondwRmonPacketsCntTable = _Pmc1002MondwRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 128)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonPacketsCntTable.setStatus("current")
_Pmc1002MondwRmonPacketsCntEntry_Object = MibTableRow
pmc1002MondwRmonPacketsCntEntry = _Pmc1002MondwRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 128, 1)
)
pmc1002MondwRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonPacketsCntEntry.setStatus("current")


class _Pmc1002MondwRmonPacketsCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonPacketsCntIndex_Object = MibTableColumn
pmc1002MondwRmonPacketsCntIndex = _Pmc1002MondwRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 128, 1, 1),
    _Pmc1002MondwRmonPacketsCntIndex_Type()
)
pmc1002MondwRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPacketsCntIndex.setStatus("current")
_Pmc1002MondwRmonPacketsCntValuePortn_Type = Counter64
_Pmc1002MondwRmonPacketsCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonPacketsCntValuePortn = _Pmc1002MondwRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 128, 1, 2),
    _Pmc1002MondwRmonPacketsCntValuePortn_Type()
)
pmc1002MondwRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPacketsCntValuePortn.setStatus("current")
_Pmc1002MondwRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonPacketsCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonPacketsCntErrorPortn = _Pmc1002MondwRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 128, 1, 3),
    _Pmc1002MondwRmonPacketsCntErrorPortn_Type()
)
pmc1002MondwRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPacketsCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonPacketsCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonPacketsCntOverloadPortn = _Pmc1002MondwRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 128, 1, 4),
    _Pmc1002MondwRmonPacketsCntOverloadPortn_Type()
)
pmc1002MondwRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPacketsCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonBroadcastCntTable_Object = MibTable
pmc1002MondwRmonBroadcastCntTable = _Pmc1002MondwRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 136)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonBroadcastCntTable.setStatus("current")
_Pmc1002MondwRmonBroadcastCntEntry_Object = MibTableRow
pmc1002MondwRmonBroadcastCntEntry = _Pmc1002MondwRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 136, 1)
)
pmc1002MondwRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonBroadcastCntEntry.setStatus("current")


class _Pmc1002MondwRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonBroadcastCntIndex_Object = MibTableColumn
pmc1002MondwRmonBroadcastCntIndex = _Pmc1002MondwRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 136, 1, 1),
    _Pmc1002MondwRmonBroadcastCntIndex_Type()
)
pmc1002MondwRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBroadcastCntIndex.setStatus("current")
_Pmc1002MondwRmonBroadcastCntValuePortn_Type = Counter64
_Pmc1002MondwRmonBroadcastCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonBroadcastCntValuePortn = _Pmc1002MondwRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 136, 1, 2),
    _Pmc1002MondwRmonBroadcastCntValuePortn_Type()
)
pmc1002MondwRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBroadcastCntValuePortn.setStatus("current")
_Pmc1002MondwRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonBroadcastCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonBroadcastCntErrorPortn = _Pmc1002MondwRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 136, 1, 3),
    _Pmc1002MondwRmonBroadcastCntErrorPortn_Type()
)
pmc1002MondwRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBroadcastCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonBroadcastCntOverloadPortn = _Pmc1002MondwRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 136, 1, 4),
    _Pmc1002MondwRmonBroadcastCntOverloadPortn_Type()
)
pmc1002MondwRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBroadcastCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonMulticastCntTable_Object = MibTable
pmc1002MondwRmonMulticastCntTable = _Pmc1002MondwRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 144)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonMulticastCntTable.setStatus("current")
_Pmc1002MondwRmonMulticastCntEntry_Object = MibTableRow
pmc1002MondwRmonMulticastCntEntry = _Pmc1002MondwRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 144, 1)
)
pmc1002MondwRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonMulticastCntEntry.setStatus("current")


class _Pmc1002MondwRmonMulticastCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonMulticastCntIndex_Object = MibTableColumn
pmc1002MondwRmonMulticastCntIndex = _Pmc1002MondwRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 144, 1, 1),
    _Pmc1002MondwRmonMulticastCntIndex_Type()
)
pmc1002MondwRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonMulticastCntIndex.setStatus("current")
_Pmc1002MondwRmonMulticastCntValuePortn_Type = Counter64
_Pmc1002MondwRmonMulticastCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonMulticastCntValuePortn = _Pmc1002MondwRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 144, 1, 2),
    _Pmc1002MondwRmonMulticastCntValuePortn_Type()
)
pmc1002MondwRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonMulticastCntValuePortn.setStatus("current")
_Pmc1002MondwRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonMulticastCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonMulticastCntErrorPortn = _Pmc1002MondwRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 144, 1, 3),
    _Pmc1002MondwRmonMulticastCntErrorPortn_Type()
)
pmc1002MondwRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonMulticastCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonMulticastCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonMulticastCntOverloadPortn = _Pmc1002MondwRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 144, 1, 4),
    _Pmc1002MondwRmonMulticastCntOverloadPortn_Type()
)
pmc1002MondwRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonMulticastCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonPauseFrameCntTable_Object = MibTable
pmc1002MondwRmonPauseFrameCntTable = _Pmc1002MondwRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 152)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonPauseFrameCntTable.setStatus("current")
_Pmc1002MondwRmonPauseFrameCntEntry_Object = MibTableRow
pmc1002MondwRmonPauseFrameCntEntry = _Pmc1002MondwRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 152, 1)
)
pmc1002MondwRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonPauseFrameCntEntry.setStatus("current")


class _Pmc1002MondwRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonPauseFrameCntIndex_Object = MibTableColumn
pmc1002MondwRmonPauseFrameCntIndex = _Pmc1002MondwRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 152, 1, 1),
    _Pmc1002MondwRmonPauseFrameCntIndex_Type()
)
pmc1002MondwRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPauseFrameCntIndex.setStatus("current")
_Pmc1002MondwRmonPauseFrameCntValuePortn_Type = Counter64
_Pmc1002MondwRmonPauseFrameCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonPauseFrameCntValuePortn = _Pmc1002MondwRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 152, 1, 2),
    _Pmc1002MondwRmonPauseFrameCntValuePortn_Type()
)
pmc1002MondwRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPauseFrameCntValuePortn.setStatus("current")
_Pmc1002MondwRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonPauseFrameCntErrorPortn = _Pmc1002MondwRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 152, 1, 3),
    _Pmc1002MondwRmonPauseFrameCntErrorPortn_Type()
)
pmc1002MondwRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPauseFrameCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonPauseFrameCntOverloadPortn = _Pmc1002MondwRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 152, 1, 4),
    _Pmc1002MondwRmonPauseFrameCntOverloadPortn_Type()
)
pmc1002MondwRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonTimerCntTable_Object = MibTable
pmc1002MondwRmonTimerCntTable = _Pmc1002MondwRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 160)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonTimerCntTable.setStatus("current")
_Pmc1002MondwRmonTimerCntEntry_Object = MibTableRow
pmc1002MondwRmonTimerCntEntry = _Pmc1002MondwRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 160, 1)
)
pmc1002MondwRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonTimerCntEntry.setStatus("current")


class _Pmc1002MondwRmonTimerCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonTimerCntIndex_Object = MibTableColumn
pmc1002MondwRmonTimerCntIndex = _Pmc1002MondwRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 160, 1, 1),
    _Pmc1002MondwRmonTimerCntIndex_Type()
)
pmc1002MondwRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonTimerCntIndex.setStatus("current")
_Pmc1002MondwRmonTimerCntValuePortn_Type = Counter64
_Pmc1002MondwRmonTimerCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonTimerCntValuePortn = _Pmc1002MondwRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 160, 1, 2),
    _Pmc1002MondwRmonTimerCntValuePortn_Type()
)
pmc1002MondwRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonTimerCntValuePortn.setStatus("current")
_Pmc1002MondwRmonTimerCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonTimerCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonTimerCntErrorPortn = _Pmc1002MondwRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 160, 1, 3),
    _Pmc1002MondwRmonTimerCntErrorPortn_Type()
)
pmc1002MondwRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonTimerCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonTimerCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonTimerCntOverloadPortn = _Pmc1002MondwRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 160, 1, 4),
    _Pmc1002MondwRmonTimerCntOverloadPortn_Type()
)
pmc1002MondwRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonTimerCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonBitsCntTable_Object = MibTable
pmc1002MondwRmonBitsCntTable = _Pmc1002MondwRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 168)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonBitsCntTable.setStatus("current")
_Pmc1002MondwRmonBitsCntEntry_Object = MibTableRow
pmc1002MondwRmonBitsCntEntry = _Pmc1002MondwRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 168, 1)
)
pmc1002MondwRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonBitsCntEntry.setStatus("current")


class _Pmc1002MondwRmonBitsCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonBitsCntIndex_Object = MibTableColumn
pmc1002MondwRmonBitsCntIndex = _Pmc1002MondwRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 168, 1, 1),
    _Pmc1002MondwRmonBitsCntIndex_Type()
)
pmc1002MondwRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBitsCntIndex.setStatus("current")
_Pmc1002MondwRmonBitsCntValuePortn_Type = Counter64
_Pmc1002MondwRmonBitsCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonBitsCntValuePortn = _Pmc1002MondwRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 168, 1, 2),
    _Pmc1002MondwRmonBitsCntValuePortn_Type()
)
pmc1002MondwRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBitsCntValuePortn.setStatus("current")
_Pmc1002MondwRmonBitsCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonBitsCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonBitsCntErrorPortn = _Pmc1002MondwRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 168, 1, 3),
    _Pmc1002MondwRmonBitsCntErrorPortn_Type()
)
pmc1002MondwRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBitsCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonBitsCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonBitsCntOverloadPortn = _Pmc1002MondwRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 168, 1, 4),
    _Pmc1002MondwRmonBitsCntOverloadPortn_Type()
)
pmc1002MondwRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonBitsCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonUnicastCntTable_Object = MibTable
pmc1002MondwRmonUnicastCntTable = _Pmc1002MondwRmonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 176)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonUnicastCntTable.setStatus("current")
_Pmc1002MondwRmonUnicastCntEntry_Object = MibTableRow
pmc1002MondwRmonUnicastCntEntry = _Pmc1002MondwRmonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 176, 1)
)
pmc1002MondwRmonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonUnicastCntEntry.setStatus("current")


class _Pmc1002MondwRmonUnicastCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonUnicastCntIndex_Object = MibTableColumn
pmc1002MondwRmonUnicastCntIndex = _Pmc1002MondwRmonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 176, 1, 1),
    _Pmc1002MondwRmonUnicastCntIndex_Type()
)
pmc1002MondwRmonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonUnicastCntIndex.setStatus("current")
_Pmc1002MondwRmonUnicastCntValuePortn_Type = Counter64
_Pmc1002MondwRmonUnicastCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonUnicastCntValuePortn = _Pmc1002MondwRmonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 176, 1, 2),
    _Pmc1002MondwRmonUnicastCntValuePortn_Type()
)
pmc1002MondwRmonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonUnicastCntValuePortn.setStatus("current")
_Pmc1002MondwRmonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonUnicastCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonUnicastCntErrorPortn = _Pmc1002MondwRmonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 176, 1, 3),
    _Pmc1002MondwRmonUnicastCntErrorPortn_Type()
)
pmc1002MondwRmonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonUnicastCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonUnicastCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonUnicastCntOverloadPortn = _Pmc1002MondwRmonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 176, 1, 4),
    _Pmc1002MondwRmonUnicastCntOverloadPortn_Type()
)
pmc1002MondwRmonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonUnicastCntOverloadPortn.setStatus("current")
_Pmc1002MondwRmonNonUnicastCntTable_Object = MibTable
pmc1002MondwRmonNonUnicastCntTable = _Pmc1002MondwRmonNonUnicastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 184)
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonNonUnicastCntTable.setStatus("current")
_Pmc1002MondwRmonNonUnicastCntEntry_Object = MibTableRow
pmc1002MondwRmonNonUnicastCntEntry = _Pmc1002MondwRmonNonUnicastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 184, 1)
)
pmc1002MondwRmonNonUnicastCntEntry.setIndexNames(
    (0, "EKINOPS-PMC1002-MIB", "pmc1002MondwRmonNonUnicastCntIndex"),
)
if mibBuilder.loadTexts:
    pmc1002MondwRmonNonUnicastCntEntry.setStatus("current")


class _Pmc1002MondwRmonNonUnicastCntIndex_Type(Integer32):
    """Custom type pmc1002MondwRmonNonUnicastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pmc1002MondwRmonNonUnicastCntIndex_Type.__name__ = "Integer32"
_Pmc1002MondwRmonNonUnicastCntIndex_Object = MibTableColumn
pmc1002MondwRmonNonUnicastCntIndex = _Pmc1002MondwRmonNonUnicastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 184, 1, 1),
    _Pmc1002MondwRmonNonUnicastCntIndex_Type()
)
pmc1002MondwRmonNonUnicastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonNonUnicastCntIndex.setStatus("current")
_Pmc1002MondwRmonNonUnicastCntValuePortn_Type = Counter64
_Pmc1002MondwRmonNonUnicastCntValuePortn_Object = MibTableColumn
pmc1002MondwRmonNonUnicastCntValuePortn = _Pmc1002MondwRmonNonUnicastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 184, 1, 2),
    _Pmc1002MondwRmonNonUnicastCntValuePortn_Type()
)
pmc1002MondwRmonNonUnicastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonNonUnicastCntValuePortn.setStatus("current")
_Pmc1002MondwRmonNonUnicastCntErrorPortn_Type = EkiOnOff
_Pmc1002MondwRmonNonUnicastCntErrorPortn_Object = MibTableColumn
pmc1002MondwRmonNonUnicastCntErrorPortn = _Pmc1002MondwRmonNonUnicastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 184, 1, 3),
    _Pmc1002MondwRmonNonUnicastCntErrorPortn_Type()
)
pmc1002MondwRmonNonUnicastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonNonUnicastCntErrorPortn.setStatus("current")
_Pmc1002MondwRmonNonUnicastCntOverloadPortn_Type = EkiOnOff
_Pmc1002MondwRmonNonUnicastCntOverloadPortn_Object = MibTableColumn
pmc1002MondwRmonNonUnicastCntOverloadPortn = _Pmc1002MondwRmonNonUnicastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 1, 184, 1, 4),
    _Pmc1002MondwRmonNonUnicastCntOverloadPortn_Type()
)
pmc1002MondwRmonNonUnicastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmc1002MondwRmonNonUnicastCntOverloadPortn.setStatus("current")
_Pmc1002RmonLine_ObjectIdentity = ObjectIdentity
pmc1002RmonLine = _Pmc1002RmonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 2)
)
_Pmc1002RmonOther_ObjectIdentity = ObjectIdentity
pmc1002RmonOther = _Pmc1002RmonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 3)
)
_Pmc1002MonCountersReset_Type = EkiOnOff
_Pmc1002MonCountersReset_Object = MibScalar
pmc1002MonCountersReset = _Pmc1002MonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 3, 359),
    _Pmc1002MonCountersReset_Type()
)
pmc1002MonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002MonCountersReset.setStatus("current")
_Pmc1002MonCountersStop_Type = EkiOnOff
_Pmc1002MonCountersStop_Object = MibScalar
pmc1002MonCountersStop = _Pmc1002MonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 50, 12, 4, 3, 360),
    _Pmc1002MonCountersStop_Type()
)
pmc1002MonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmc1002MonCountersStop.setStatus("current")

# Managed Objects groups


# Notification objects

pmc1002LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 30)
)
pmc1002LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmLineDdmWarningPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapLineNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmc1002LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 31)
)
pmc1002LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmLineDdmWarningPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapLineNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmc1002LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 32)
)
pmc1002LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmLineDdmAlmPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapLineNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc1002LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 33)
)
pmc1002LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmLineDdmAlmPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapLineNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pmc1002LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 34)
)
pmc1002LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmLineFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002AlmLineHwFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapLineNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002LineTrapCritGoesOn.setStatus(
        "current"
    )

pmc1002LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 35)
)
pmc1002LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmLineFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002AlmLineHwFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapLineNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002LineTrapCritGoesOff.setStatus(
        "current"
    )

pmc1002ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 40)
)
pmc1002ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapClientNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pmc1002ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 41)
)
pmc1002ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmClientSfpDdmWarningPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapClientNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pmc1002ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 42)
)
pmc1002ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapClientNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc1002ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 43)
)
pmc1002ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmClientSfpDdmAlmPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapClientNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pmc1002ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 44)
)
pmc1002ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmClientFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002AlmClientHwFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapClientNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002ClientTrapCritGoesOn.setStatus(
        "current"
    )

pmc1002ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 45)
)
pmc1002ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmClientFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002AlmClientHwFailPortn"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapClientNumber"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002ClientTrapCritGoesOff.setStatus(
        "current"
    )

pmc1002PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 50)
)
pmc1002PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmDefFuseB"),
        ("EKINOPS-PMC1002-MIB", "pmc1002AlmDefFuseA"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pmc1002PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 50, 11, 51)
)
pmc1002PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-PMC1002-MIB", "pmc1002AlmDefFuseB"),
        ("EKINOPS-PMC1002-MIB", "pmc1002AlmDefFuseA"),
        ("EKINOPS-PMC1002-MIB", "pmc1002trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pmc1002PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-PMC1002-MIB",
    **{"Pmc1002OtxMode": Pmc1002OtxMode,
       "Pmc1002OtxGrid": Pmc1002OtxGrid,
       "Pmc1002AdjustValue": Pmc1002AdjustValue,
       "Pmc1002OtxChannel": Pmc1002OtxChannel,
       "Pmc1002DccMode": Pmc1002DccMode,
       "Pmc1002Mode": Pmc1002Mode,
       "modulepmc1002": modulepmc1002,
       "pmc1002alarms": pmc1002alarms,
       "pmc1002AlmOther": pmc1002AlmOther,
       "pmc1002AlmOtherNurg": pmc1002AlmOtherNurg,
       "pmc1002AlmsynthAlm2": pmc1002AlmsynthAlm2,
       "pmc1002AlmConfTableSave": pmc1002AlmConfTableSave,
       "pmc1002AlmInvUpload": pmc1002AlmInvUpload,
       "pmc1002AlmConfTableLoad": pmc1002AlmConfTableLoad,
       "pmc1002AlmCorrelatOff": pmc1002AlmCorrelatOff,
       "pmc1002AlmMaintenanceOn": pmc1002AlmMaintenanceOn,
       "pmc1002AlmOtherUrg": pmc1002AlmOtherUrg,
       "pmc1002AlmmodInitFailLevel2": pmc1002AlmmodInitFailLevel2,
       "pmc1002AlmLedFail": pmc1002AlmLedFail,
       "pmc1002AlmNextColdBootForced": pmc1002AlmNextColdBootForced,
       "pmc1002AlmBootUndone": pmc1002AlmBootUndone,
       "pmc1002AlmResetHwInitFail": pmc1002AlmResetHwInitFail,
       "pmc1002AlmSwInitFail": pmc1002AlmSwInitFail,
       "pmc1002AlmmodInitFailLevel3": pmc1002AlmmodInitFailLevel3,
       "pmc1002AlmGwIdentFail": pmc1002AlmGwIdentFail,
       "pmc1002AlmObmTypeReadFail": pmc1002AlmObmTypeReadFail,
       "pmc1002AlmInitModuleFail": pmc1002AlmInitModuleFail,
       "pmc1002AlmXfp1InitFail": pmc1002AlmXfp1InitFail,
       "pmc1002AlmXfp2InitFail": pmc1002AlmXfp2InitFail,
       "pmc1002AlmLine1InitFail": pmc1002AlmLine1InitFail,
       "pmc1002AlmClient1InitFail": pmc1002AlmClient1InitFail,
       "pmc1002AlmOtherCrit": pmc1002AlmOtherCrit,
       "pmc1002AlmsynthAlm0": pmc1002AlmsynthAlm0,
       "pmc1002AlmModGlobFail": pmc1002AlmModGlobFail,
       "pmc1002AlmDefFuseA": pmc1002AlmDefFuseA,
       "pmc1002AlmDefFuseB": pmc1002AlmDefFuseB,
       "pmc1002AlmClient": pmc1002AlmClient,
       "pmc1002AlmClientNurg": pmc1002AlmClientNurg,
       "pmc1002AlmclientXfpWarningsTable": pmc1002AlmclientXfpWarningsTable,
       "pmc1002AlmclientXfpWarningsEntry": pmc1002AlmclientXfpWarningsEntry,
       "pmc1002AlmclientXfpWarningsIndex": pmc1002AlmclientXfpWarningsIndex,
       "pmc1002AlmClientTxPowerLowWarningPortn": pmc1002AlmClientTxPowerLowWarningPortn,
       "pmc1002AlmClientTxPowerHighWarningPortn": pmc1002AlmClientTxPowerHighWarningPortn,
       "pmc1002AlmClientTxBiasLowWarningPortn": pmc1002AlmClientTxBiasLowWarningPortn,
       "pmc1002AlmClientTxBiasHighWarningPortn": pmc1002AlmClientTxBiasHighWarningPortn,
       "pmc1002AlmClientTempLowWarningPortn": pmc1002AlmClientTempLowWarningPortn,
       "pmc1002AlmClientTempHighWarningPortn": pmc1002AlmClientTempHighWarningPortn,
       "pmc1002AlmClientRxPowerLowWarningPortn": pmc1002AlmClientRxPowerLowWarningPortn,
       "pmc1002AlmClientRxPowerHighWarningPortn": pmc1002AlmClientRxPowerHighWarningPortn,
       "pmc1002AlmClientUrg": pmc1002AlmClientUrg,
       "pmc1002AlmclientXfpAlarm1Table": pmc1002AlmclientXfpAlarm1Table,
       "pmc1002AlmclientXfpAlarm1Entry": pmc1002AlmclientXfpAlarm1Entry,
       "pmc1002AlmclientXfpAlarm1Index": pmc1002AlmclientXfpAlarm1Index,
       "pmc1002AlmClientTxPowerLowAlarmPortn": pmc1002AlmClientTxPowerLowAlarmPortn,
       "pmc1002AlmClientTxPowerHighAlarmPortn": pmc1002AlmClientTxPowerHighAlarmPortn,
       "pmc1002AlmClientTxBiasLowAlarmPortn": pmc1002AlmClientTxBiasLowAlarmPortn,
       "pmc1002AlmClientTxBiasHighAlarmPortn": pmc1002AlmClientTxBiasHighAlarmPortn,
       "pmc1002AlmClientTempLowAlarmPortn": pmc1002AlmClientTempLowAlarmPortn,
       "pmc1002AlmClientTempHighAlarmPortn": pmc1002AlmClientTempHighAlarmPortn,
       "pmc1002AlmClientRxPowerLowAlarmPortn": pmc1002AlmClientRxPowerLowAlarmPortn,
       "pmc1002AlmClientRxPowerHighAlarmPortn": pmc1002AlmClientRxPowerHighAlarmPortn,
       "pmc1002AlmclientXfpSupplyAlarmTable": pmc1002AlmclientXfpSupplyAlarmTable,
       "pmc1002AlmclientXfpSupplyAlarmEntry": pmc1002AlmclientXfpSupplyAlarmEntry,
       "pmc1002AlmclientXfpSupplyAlarmIndex": pmc1002AlmclientXfpSupplyAlarmIndex,
       "pmc1002AlmClientVee5LowAlarmPortn": pmc1002AlmClientVee5LowAlarmPortn,
       "pmc1002AlmClientVee5HighAlarmPortn": pmc1002AlmClientVee5HighAlarmPortn,
       "pmc1002AlmClientVcc2LowAlarmPortn": pmc1002AlmClientVcc2LowAlarmPortn,
       "pmc1002AlmClientVcc2HighAlarmPortn": pmc1002AlmClientVcc2HighAlarmPortn,
       "pmc1002AlmClientVcc3LowAlarmPortn": pmc1002AlmClientVcc3LowAlarmPortn,
       "pmc1002AlmClientVcc3HighAlarmPortn": pmc1002AlmClientVcc3HighAlarmPortn,
       "pmc1002AlmClientVcc5LowAlarmPortn": pmc1002AlmClientVcc5LowAlarmPortn,
       "pmc1002AlmClientVcc5HighAlarmPortn": pmc1002AlmClientVcc5HighAlarmPortn,
       "pmc1002AlmClientVee5LowWarningPortn": pmc1002AlmClientVee5LowWarningPortn,
       "pmc1002AlmClientVee5HighWarningPortn": pmc1002AlmClientVee5HighWarningPortn,
       "pmc1002AlmClientVcc2LowWarningPortn": pmc1002AlmClientVcc2LowWarningPortn,
       "pmc1002AlmClientVcc2HighWarningPortn": pmc1002AlmClientVcc2HighWarningPortn,
       "pmc1002AlmClientVcc3LowWarningPortn": pmc1002AlmClientVcc3LowWarningPortn,
       "pmc1002AlmClientVcc3HighWarningPortn": pmc1002AlmClientVcc3HighWarningPortn,
       "pmc1002AlmClientVcc5LowWarningPortn": pmc1002AlmClientVcc5LowWarningPortn,
       "pmc1002AlmClientVcc5HighWarningPortn": pmc1002AlmClientVcc5HighWarningPortn,
       "pmc1002AlmClientCrit": pmc1002AlmClientCrit,
       "pmc1002AlmsynthAlmPortTable": pmc1002AlmsynthAlmPortTable,
       "pmc1002AlmsynthAlmPortEntry": pmc1002AlmsynthAlmPortEntry,
       "pmc1002AlmsynthAlmPortIndex": pmc1002AlmsynthAlmPortIndex,
       "pmc1002AlmClientSfpAbsentPortn": pmc1002AlmClientSfpAbsentPortn,
       "pmc1002AlmClientDdmAbsentPortn": pmc1002AlmClientDdmAbsentPortn,
       "pmc1002AlmClientHwFailPortn": pmc1002AlmClientHwFailPortn,
       "pmc1002AlmClientDwLsdPortn": pmc1002AlmClientDwLsdPortn,
       "pmc1002AlmClientLocalOosPortn": pmc1002AlmClientLocalOosPortn,
       "pmc1002AlmClientDwCaisPortn": pmc1002AlmClientDwCaisPortn,
       "pmc1002AlmClientSfpDdmWarningPortn": pmc1002AlmClientSfpDdmWarningPortn,
       "pmc1002AlmClientSfpDdmAlmPortn": pmc1002AlmClientSfpDdmAlmPortn,
       "pmc1002AlmClientFailPortn": pmc1002AlmClientFailPortn,
       "pmc1002AlmClientUpCsfPortn": pmc1002AlmClientUpCsfPortn,
       "pmc1002AlmclientAccessioAlmTable": pmc1002AlmclientAccessioAlmTable,
       "pmc1002AlmclientAccessioAlmEntry": pmc1002AlmclientAccessioAlmEntry,
       "pmc1002AlmclientAccessioAlmIndex": pmc1002AlmclientAccessioAlmIndex,
       "pmc1002AlmClientDwLasFailPortn": pmc1002AlmClientDwLasFailPortn,
       "pmc1002AlmClientUpLosPortn": pmc1002AlmClientUpLosPortn,
       "pmc1002AlmclientXfpAlarm2Table": pmc1002AlmclientXfpAlarm2Table,
       "pmc1002AlmclientXfpAlarm2Entry": pmc1002AlmclientXfpAlarm2Entry,
       "pmc1002AlmclientXfpAlarm2Index": pmc1002AlmclientXfpAlarm2Index,
       "pmc1002AlmClientModNrPortn": pmc1002AlmClientModNrPortn,
       "pmc1002AlmClientRxCdrNotLockedPortn": pmc1002AlmClientRxCdrNotLockedPortn,
       "pmc1002AlmClientRxNrPortn": pmc1002AlmClientRxNrPortn,
       "pmc1002AlmClientTxCdrNotLockedPortn": pmc1002AlmClientTxCdrNotLockedPortn,
       "pmc1002AlmClientTxFaultPortn": pmc1002AlmClientTxFaultPortn,
       "pmc1002AlmClientTxNrPortn": pmc1002AlmClientTxNrPortn,
       "pmc1002AlmClientWavelengthUnlockedPortn": pmc1002AlmClientWavelengthUnlockedPortn,
       "pmc1002AlmClientTecFaultPortn": pmc1002AlmClientTecFaultPortn,
       "pmc1002AlmClientApdSupplyFaultPortn": pmc1002AlmClientApdSupplyFaultPortn,
       "pmc1002AlmclientMapperDeAlmTable": pmc1002AlmclientMapperDeAlmTable,
       "pmc1002AlmclientMapperDeAlmEntry": pmc1002AlmclientMapperDeAlmEntry,
       "pmc1002AlmclientMapperDeAlmIndex": pmc1002AlmclientMapperDeAlmIndex,
       "pmc1002AlmClientUpAccOosPortn": pmc1002AlmClientUpAccOosPortn,
       "pmc1002AlmClientUpBufferOvlPortn": pmc1002AlmClientUpBufferOvlPortn,
       "pmc1002AlmClientDwCsfDetPortn": pmc1002AlmClientDwCsfDetPortn,
       "pmc1002AlmClientDwBufferOvlPortn": pmc1002AlmClientDwBufferOvlPortn,
       "pmc1002AlmLine": pmc1002AlmLine,
       "pmc1002AlmLineNurg": pmc1002AlmLineNurg,
       "pmc1002AlmlineXfp1WarningsTable": pmc1002AlmlineXfp1WarningsTable,
       "pmc1002AlmlineXfp1WarningsEntry": pmc1002AlmlineXfp1WarningsEntry,
       "pmc1002AlmlineXfp1WarningsIndex": pmc1002AlmlineXfp1WarningsIndex,
       "pmc1002AlmLineTxPowerLowWarningPortn": pmc1002AlmLineTxPowerLowWarningPortn,
       "pmc1002AlmLineTxPowerHighWarningPortn": pmc1002AlmLineTxPowerHighWarningPortn,
       "pmc1002AlmLineTxBiasLowWarningPortn": pmc1002AlmLineTxBiasLowWarningPortn,
       "pmc1002AlmLineTxBiasHighWarningPortn": pmc1002AlmLineTxBiasHighWarningPortn,
       "pmc1002AlmLineTempLowWarningPortn": pmc1002AlmLineTempLowWarningPortn,
       "pmc1002AlmLineTempHighWarningPortn": pmc1002AlmLineTempHighWarningPortn,
       "pmc1002AlmLineRxPowerLowWarningPortn": pmc1002AlmLineRxPowerLowWarningPortn,
       "pmc1002AlmLineRxPowerHighWarningPortn": pmc1002AlmLineRxPowerHighWarningPortn,
       "pmc1002AlmlineOtx1TlhWarningsTable": pmc1002AlmlineOtx1TlhWarningsTable,
       "pmc1002AlmlineOtx1TlhWarningsEntry": pmc1002AlmlineOtx1TlhWarningsEntry,
       "pmc1002AlmlineOtx1TlhWarningsIndex": pmc1002AlmlineOtx1TlhWarningsIndex,
       "pmc1002AlmLineModulatorAgingHighWarningPortn": pmc1002AlmLineModulatorAgingHighWarningPortn,
       "pmc1002AlmLineAgingHighWarningPortn": pmc1002AlmLineAgingHighWarningPortn,
       "pmc1002AlmLineFreqDevHighWarningPortn": pmc1002AlmLineFreqDevHighWarningPortn,
       "pmc1002AlmLineLaserTempHighWarningPortn": pmc1002AlmLineLaserTempHighWarningPortn,
       "pmc1002AlmLineUrg": pmc1002AlmLineUrg,
       "pmc1002AlmdfrmBerTable": pmc1002AlmdfrmBerTable,
       "pmc1002AlmdfrmBerEntry": pmc1002AlmdfrmBerEntry,
       "pmc1002AlmdfrmBerIndex": pmc1002AlmdfrmBerIndex,
       "pmc1002AlmLineSignalDegradePortn": pmc1002AlmLineSignalDegradePortn,
       "pmc1002AlmLineSignalFailPortn": pmc1002AlmLineSignalFailPortn,
       "pmc1002AlmLineDegradePortn": pmc1002AlmLineDegradePortn,
       "pmc1002AlmlineXfp1AlarmTable": pmc1002AlmlineXfp1AlarmTable,
       "pmc1002AlmlineXfp1AlarmEntry": pmc1002AlmlineXfp1AlarmEntry,
       "pmc1002AlmlineXfp1AlarmIndex": pmc1002AlmlineXfp1AlarmIndex,
       "pmc1002AlmLineTxPowerLowAlarmPortn": pmc1002AlmLineTxPowerLowAlarmPortn,
       "pmc1002AlmLineTxPowerHighAlarmPortn": pmc1002AlmLineTxPowerHighAlarmPortn,
       "pmc1002AlmLineTxBiasLowAlarmPortn": pmc1002AlmLineTxBiasLowAlarmPortn,
       "pmc1002AlmLineTxBiasHighAlarmPortn": pmc1002AlmLineTxBiasHighAlarmPortn,
       "pmc1002AlmLineTempLowAlarmPortn": pmc1002AlmLineTempLowAlarmPortn,
       "pmc1002AlmLineTempHighAlarmPortn": pmc1002AlmLineTempHighAlarmPortn,
       "pmc1002AlmLineRxPowerLowAlarmPortn": pmc1002AlmLineRxPowerLowAlarmPortn,
       "pmc1002AlmLineRxPowerHighAlarmPortn": pmc1002AlmLineRxPowerHighAlarmPortn,
       "pmc1002AlmlineXfp1SupplyAlarmTable": pmc1002AlmlineXfp1SupplyAlarmTable,
       "pmc1002AlmlineXfp1SupplyAlarmEntry": pmc1002AlmlineXfp1SupplyAlarmEntry,
       "pmc1002AlmlineXfp1SupplyAlarmIndex": pmc1002AlmlineXfp1SupplyAlarmIndex,
       "pmc1002AlmLineVee5LowAlarmPortn": pmc1002AlmLineVee5LowAlarmPortn,
       "pmc1002AlmLineVee5HighAlarmPortn": pmc1002AlmLineVee5HighAlarmPortn,
       "pmc1002AlmLineVcc2LowAlarmPortn": pmc1002AlmLineVcc2LowAlarmPortn,
       "pmc1002AlmLineVcc2HighAlarmPortn": pmc1002AlmLineVcc2HighAlarmPortn,
       "pmc1002AlmLineVcc3LowAlarmPortn": pmc1002AlmLineVcc3LowAlarmPortn,
       "pmc1002AlmLineVcc3HighAlarmPortn": pmc1002AlmLineVcc3HighAlarmPortn,
       "pmc1002AlmLineVcc5LowAlarmPortn": pmc1002AlmLineVcc5LowAlarmPortn,
       "pmc1002AlmLineVcc5HighAlarmPortn": pmc1002AlmLineVcc5HighAlarmPortn,
       "pmc1002AlmLineVee5LowLineWarningPortn": pmc1002AlmLineVee5LowLineWarningPortn,
       "pmc1002AlmLineVee5HighWarningPortn": pmc1002AlmLineVee5HighWarningPortn,
       "pmc1002AlmLineVcc2LowWarningPortn": pmc1002AlmLineVcc2LowWarningPortn,
       "pmc1002AlmLineVcc2HighWarningPortn": pmc1002AlmLineVcc2HighWarningPortn,
       "pmc1002AlmLineVcc3LowWarningPortn": pmc1002AlmLineVcc3LowWarningPortn,
       "pmc1002AlmLineVcc3HighWarningPortn": pmc1002AlmLineVcc3HighWarningPortn,
       "pmc1002AlmLineVcc5LowWarningPortn": pmc1002AlmLineVcc5LowWarningPortn,
       "pmc1002AlmLineVcc5HighWarningPortn": pmc1002AlmLineVcc5HighWarningPortn,
       "pmc1002AlmlineOtx1TlhAlarmsTable": pmc1002AlmlineOtx1TlhAlarmsTable,
       "pmc1002AlmlineOtx1TlhAlarmsEntry": pmc1002AlmlineOtx1TlhAlarmsEntry,
       "pmc1002AlmlineOtx1TlhAlarmsIndex": pmc1002AlmlineOtx1TlhAlarmsIndex,
       "pmc1002AlmLineModulatorAgingHighAlaPortn": pmc1002AlmLineModulatorAgingHighAlaPortn,
       "pmc1002AlmLineAgingHighAlaPortn": pmc1002AlmLineAgingHighAlaPortn,
       "pmc1002AlmLineCdrNotReadyPortn": pmc1002AlmLineCdrNotReadyPortn,
       "pmc1002AlmLineFreqDevHighAlaPortn": pmc1002AlmLineFreqDevHighAlaPortn,
       "pmc1002AlmLineLaserTempHighAlaPortn": pmc1002AlmLineLaserTempHighAlaPortn,
       "pmc1002AlmLineCrit": pmc1002AlmLineCrit,
       "pmc1002AlmsynthAlmLineTable": pmc1002AlmsynthAlmLineTable,
       "pmc1002AlmsynthAlmLineEntry": pmc1002AlmsynthAlmLineEntry,
       "pmc1002AlmsynthAlmLineIndex": pmc1002AlmsynthAlmLineIndex,
       "pmc1002AlmLineXfpAbsentPortn": pmc1002AlmLineXfpAbsentPortn,
       "pmc1002AlmLineXfpInitNotComplPortn": pmc1002AlmLineXfpInitNotComplPortn,
       "pmc1002AlmLineHwFailPortn": pmc1002AlmLineHwFailPortn,
       "pmc1002AlmLineXfpTxOffPortn": pmc1002AlmLineXfpTxOffPortn,
       "pmc1002AlmLineLocalOosPortn": pmc1002AlmLineLocalOosPortn,
       "pmc1002AlmLineUpRdiInsPortn": pmc1002AlmLineUpRdiInsPortn,
       "pmc1002AlmLineDdmWarningPortn": pmc1002AlmLineDdmWarningPortn,
       "pmc1002AlmLineDdmAlmPortn": pmc1002AlmLineDdmAlmPortn,
       "pmc1002AlmLineFailPortn": pmc1002AlmLineFailPortn,
       "pmc1002AlmLineActivePortn": pmc1002AlmLineActivePortn,
       "pmc1002AlmdfrmAlmTable": pmc1002AlmdfrmAlmTable,
       "pmc1002AlmdfrmAlmEntry": pmc1002AlmdfrmAlmEntry,
       "pmc1002AlmdfrmAlmIndex": pmc1002AlmdfrmAlmIndex,
       "pmc1002AlmLineDwAisDetPortn": pmc1002AlmLineDwAisDetPortn,
       "pmc1002AlmLineDwRdiDetPortn": pmc1002AlmLineDwRdiDetPortn,
       "pmc1002AlmLineDwOofPortn": pmc1002AlmLineDwOofPortn,
       "pmc1002AlmLineDwLofPortn": pmc1002AlmLineDwLofPortn,
       "pmc1002AlmLineFecFailPortn": pmc1002AlmLineFecFailPortn,
       "pmc1002AlmlineSyncAlarmsTable": pmc1002AlmlineSyncAlarmsTable,
       "pmc1002AlmlineSyncAlarmsEntry": pmc1002AlmlineSyncAlarmsEntry,
       "pmc1002AlmlineSyncAlarmsIndex": pmc1002AlmlineSyncAlarmsIndex,
       "pmc1002AlmLineDwLockerrPortn": pmc1002AlmLineDwLockerrPortn,
       "pmc1002AlmLineUpLockerrPortn": pmc1002AlmLineUpLockerrPortn,
       "pmc1002AlmLineDwLosPortn": pmc1002AlmLineDwLosPortn,
       "pmc1002AlmlineXfp1AlarmsTable": pmc1002AlmlineXfp1AlarmsTable,
       "pmc1002AlmlineXfp1AlarmsEntry": pmc1002AlmlineXfp1AlarmsEntry,
       "pmc1002AlmlineXfp1AlarmsIndex": pmc1002AlmlineXfp1AlarmsIndex,
       "pmc1002AlmLineModNrPortn": pmc1002AlmLineModNrPortn,
       "pmc1002AlmLineRxCdrNotLockedPortn": pmc1002AlmLineRxCdrNotLockedPortn,
       "pmc1002AlmLineRxNrPortn": pmc1002AlmLineRxNrPortn,
       "pmc1002AlmLineTxCdrNotLockedPortn": pmc1002AlmLineTxCdrNotLockedPortn,
       "pmc1002AlmLineTxFaultPortn": pmc1002AlmLineTxFaultPortn,
       "pmc1002AlmLineTxNrPortn": pmc1002AlmLineTxNrPortn,
       "pmc1002AlmLineChannelNotAcquiredPortn": pmc1002AlmLineChannelNotAcquiredPortn,
       "pmc1002AlmLineWavelengthUnlockedPortn": pmc1002AlmLineWavelengthUnlockedPortn,
       "pmc1002AlmLineTecFaultPortn": pmc1002AlmLineTecFaultPortn,
       "pmc1002AlmLineApdSupplyFaultPortn": pmc1002AlmLineApdSupplyFaultPortn,
       "pmc1002measures": pmc1002measures,
       "pmc1002MesrOther": pmc1002MesrOther,
       "pmc1002Mesrsynth0": pmc1002Mesrsynth0,
       "pmc1002Mesrsynth1": pmc1002Mesrsynth1,
       "pmc1002MesrClient": pmc1002MesrClient,
       "pmc1002MesrclientModTempMeasTable": pmc1002MesrclientModTempMeasTable,
       "pmc1002MesrclientModTempMeasEntry": pmc1002MesrclientModTempMeasEntry,
       "pmc1002MesrclientModTempMeasIndex": pmc1002MesrclientModTempMeasIndex,
       "pmc1002MesrclientModTempMeasPortn": pmc1002MesrclientModTempMeasPortn,
       "pmc1002MesrclientBiasCurrentMeasTable": pmc1002MesrclientBiasCurrentMeasTable,
       "pmc1002MesrclientBiasCurrentMeasEntry": pmc1002MesrclientBiasCurrentMeasEntry,
       "pmc1002MesrclientBiasCurrentMeasIndex": pmc1002MesrclientBiasCurrentMeasIndex,
       "pmc1002MesrclientBiasCurrentMeasPortn": pmc1002MesrclientBiasCurrentMeasPortn,
       "pmc1002MesrclientTxPowerMeasTable": pmc1002MesrclientTxPowerMeasTable,
       "pmc1002MesrclientTxPowerMeasEntry": pmc1002MesrclientTxPowerMeasEntry,
       "pmc1002MesrclientTxPowerMeasIndex": pmc1002MesrclientTxPowerMeasIndex,
       "pmc1002MesrclientTxPowerMeasPortn": pmc1002MesrclientTxPowerMeasPortn,
       "pmc1002MesrclientRxPowerMeasTable": pmc1002MesrclientRxPowerMeasTable,
       "pmc1002MesrclientRxPowerMeasEntry": pmc1002MesrclientRxPowerMeasEntry,
       "pmc1002MesrclientRxPowerMeasIndex": pmc1002MesrclientRxPowerMeasIndex,
       "pmc1002MesrclientRxPowerMeasPortn": pmc1002MesrclientRxPowerMeasPortn,
       "pmc1002MesrLine": pmc1002MesrLine,
       "pmc1002Mesrline1ModTempMeasTable": pmc1002Mesrline1ModTempMeasTable,
       "pmc1002Mesrline1ModTempMeasEntry": pmc1002Mesrline1ModTempMeasEntry,
       "pmc1002Mesrline1ModTempMeasIndex": pmc1002Mesrline1ModTempMeasIndex,
       "pmc1002Mesrline1ModTempMeasPortn": pmc1002Mesrline1ModTempMeasPortn,
       "pmc1002Mesrline1ReservedTable": pmc1002Mesrline1ReservedTable,
       "pmc1002Mesrline1ReservedEntry": pmc1002Mesrline1ReservedEntry,
       "pmc1002Mesrline1ReservedIndex": pmc1002Mesrline1ReservedIndex,
       "pmc1002Mesrline1ReservedPortn": pmc1002Mesrline1ReservedPortn,
       "pmc1002Mesrline1BiasCurrentMeasTable": pmc1002Mesrline1BiasCurrentMeasTable,
       "pmc1002Mesrline1BiasCurrentMeasEntry": pmc1002Mesrline1BiasCurrentMeasEntry,
       "pmc1002Mesrline1BiasCurrentMeasIndex": pmc1002Mesrline1BiasCurrentMeasIndex,
       "pmc1002Mesrline1BiasCurrentMeasPortn": pmc1002Mesrline1BiasCurrentMeasPortn,
       "pmc1002Mesrline1TxPowerMeasTable": pmc1002Mesrline1TxPowerMeasTable,
       "pmc1002Mesrline1TxPowerMeasEntry": pmc1002Mesrline1TxPowerMeasEntry,
       "pmc1002Mesrline1TxPowerMeasIndex": pmc1002Mesrline1TxPowerMeasIndex,
       "pmc1002Mesrline1TxPowerMeasPortn": pmc1002Mesrline1TxPowerMeasPortn,
       "pmc1002Mesrline1RxPowerMeasTable": pmc1002Mesrline1RxPowerMeasTable,
       "pmc1002Mesrline1RxPowerMeasEntry": pmc1002Mesrline1RxPowerMeasEntry,
       "pmc1002Mesrline1RxPowerMeasIndex": pmc1002Mesrline1RxPowerMeasIndex,
       "pmc1002Mesrline1RxPowerMeasPortn": pmc1002Mesrline1RxPowerMeasPortn,
       "pmc1002Mesrline1Aux1MeasTable": pmc1002Mesrline1Aux1MeasTable,
       "pmc1002Mesrline1Aux1MeasEntry": pmc1002Mesrline1Aux1MeasEntry,
       "pmc1002Mesrline1Aux1MeasIndex": pmc1002Mesrline1Aux1MeasIndex,
       "pmc1002Mesrline1Aux1MeasPortn": pmc1002Mesrline1Aux1MeasPortn,
       "pmc1002Mesrline1Aux2MeasTable": pmc1002Mesrline1Aux2MeasTable,
       "pmc1002Mesrline1Aux2MeasEntry": pmc1002Mesrline1Aux2MeasEntry,
       "pmc1002Mesrline1Aux2MeasIndex": pmc1002Mesrline1Aux2MeasIndex,
       "pmc1002Mesrline1Aux2MeasPortn": pmc1002Mesrline1Aux2MeasPortn,
       "pmc1002Mesrline1AgingTable": pmc1002Mesrline1AgingTable,
       "pmc1002Mesrline1AgingEntry": pmc1002Mesrline1AgingEntry,
       "pmc1002Mesrline1AgingIndex": pmc1002Mesrline1AgingIndex,
       "pmc1002Mesrline1AgingPortn": pmc1002Mesrline1AgingPortn,
       "pmc1002Mesrline1LaserTemperatureTable": pmc1002Mesrline1LaserTemperatureTable,
       "pmc1002Mesrline1LaserTemperatureEntry": pmc1002Mesrline1LaserTemperatureEntry,
       "pmc1002Mesrline1LaserTemperatureIndex": pmc1002Mesrline1LaserTemperatureIndex,
       "pmc1002Mesrline1LaserTemperaturePortn": pmc1002Mesrline1LaserTemperaturePortn,
       "pmc1002Mesrline1FreqDeviationTable": pmc1002Mesrline1FreqDeviationTable,
       "pmc1002Mesrline1FreqDeviationEntry": pmc1002Mesrline1FreqDeviationEntry,
       "pmc1002Mesrline1FreqDeviationIndex": pmc1002Mesrline1FreqDeviationIndex,
       "pmc1002Mesrline1FreqDeviationPortn": pmc1002Mesrline1FreqDeviationPortn,
       "pmc1002Mesrline1LaserWvlengthTable": pmc1002Mesrline1LaserWvlengthTable,
       "pmc1002Mesrline1LaserWvlengthEntry": pmc1002Mesrline1LaserWvlengthEntry,
       "pmc1002Mesrline1LaserWvlengthIndex": pmc1002Mesrline1LaserWvlengthIndex,
       "pmc1002Mesrline1LaserWvlengthPortn": pmc1002Mesrline1LaserWvlengthPortn,
       "pmc1002counters": pmc1002counters,
       "pmc1002CntOther": pmc1002CntOther,
       "pmc1002CntClient": pmc1002CntClient,
       "pmc1002CntclientUpErrCntTable": pmc1002CntclientUpErrCntTable,
       "pmc1002CntclientUpErrCntEntry": pmc1002CntclientUpErrCntEntry,
       "pmc1002CntclientUpErrCntIndex": pmc1002CntclientUpErrCntIndex,
       "pmc1002CntclientUpErrCntValuePortn": pmc1002CntclientUpErrCntValuePortn,
       "pmc1002CntclientUpErrCntErrorPortn": pmc1002CntclientUpErrCntErrorPortn,
       "pmc1002CntclientUpErrCntOverloadPortn": pmc1002CntclientUpErrCntOverloadPortn,
       "pmc1002CntclientUpTimCntTable": pmc1002CntclientUpTimCntTable,
       "pmc1002CntclientUpTimCntEntry": pmc1002CntclientUpTimCntEntry,
       "pmc1002CntclientUpTimCntIndex": pmc1002CntclientUpTimCntIndex,
       "pmc1002CntclientUpTimCntValuePortn": pmc1002CntclientUpTimCntValuePortn,
       "pmc1002CntclientUpTimCntErrorPortn": pmc1002CntclientUpTimCntErrorPortn,
       "pmc1002CntclientUpTimCntOverloadPortn": pmc1002CntclientUpTimCntOverloadPortn,
       "pmc1002CntclientDwErrCntTable": pmc1002CntclientDwErrCntTable,
       "pmc1002CntclientDwErrCntEntry": pmc1002CntclientDwErrCntEntry,
       "pmc1002CntclientDwErrCntIndex": pmc1002CntclientDwErrCntIndex,
       "pmc1002CntclientDwErrCntValuePortn": pmc1002CntclientDwErrCntValuePortn,
       "pmc1002CntclientDwErrCntErrorPortn": pmc1002CntclientDwErrCntErrorPortn,
       "pmc1002CntclientDwErrCntOverloadPortn": pmc1002CntclientDwErrCntOverloadPortn,
       "pmc1002CntclientDwTimCntTable": pmc1002CntclientDwTimCntTable,
       "pmc1002CntclientDwTimCntEntry": pmc1002CntclientDwTimCntEntry,
       "pmc1002CntclientDwTimCntIndex": pmc1002CntclientDwTimCntIndex,
       "pmc1002CntclientDwTimCntValuePortn": pmc1002CntclientDwTimCntValuePortn,
       "pmc1002CntclientDwTimCntErrorPortn": pmc1002CntclientDwTimCntErrorPortn,
       "pmc1002CntclientDwTimCntOverloadPortn": pmc1002CntclientDwTimCntOverloadPortn,
       "pmc1002CntLine": pmc1002CntLine,
       "pmc1002CntlineDfrmErrCntTable": pmc1002CntlineDfrmErrCntTable,
       "pmc1002CntlineDfrmErrCntEntry": pmc1002CntlineDfrmErrCntEntry,
       "pmc1002CntlineDfrmErrCntIndex": pmc1002CntlineDfrmErrCntIndex,
       "pmc1002CntlineDfrmErrCntValuePortn": pmc1002CntlineDfrmErrCntValuePortn,
       "pmc1002CntlineDfrmErrCntErrorPortn": pmc1002CntlineDfrmErrCntErrorPortn,
       "pmc1002CntlineDfrmErrCntOverloadPortn": pmc1002CntlineDfrmErrCntOverloadPortn,
       "pmc1002CntlineDfrmTimCntTable": pmc1002CntlineDfrmTimCntTable,
       "pmc1002CntlineDfrmTimCntEntry": pmc1002CntlineDfrmTimCntEntry,
       "pmc1002CntlineDfrmTimCntIndex": pmc1002CntlineDfrmTimCntIndex,
       "pmc1002CntlineDfrmTimCntValuePortn": pmc1002CntlineDfrmTimCntValuePortn,
       "pmc1002CntlineDfrmTimCntErrorPortn": pmc1002CntlineDfrmTimCntErrorPortn,
       "pmc1002CntlineDfrmTimCntOverloadPortn": pmc1002CntlineDfrmTimCntOverloadPortn,
       "pmc1002CntlineDfrmPrimErrCntTable": pmc1002CntlineDfrmPrimErrCntTable,
       "pmc1002CntlineDfrmPrimErrCntEntry": pmc1002CntlineDfrmPrimErrCntEntry,
       "pmc1002CntlineDfrmPrimErrCntIndex": pmc1002CntlineDfrmPrimErrCntIndex,
       "pmc1002CntlineDfrmPrimErrCntValuePortn": pmc1002CntlineDfrmPrimErrCntValuePortn,
       "pmc1002CntlineDfrmPrimErrCntErrorPortn": pmc1002CntlineDfrmPrimErrCntErrorPortn,
       "pmc1002CntlineDfrmPrimErrCntOverloadPortn": pmc1002CntlineDfrmPrimErrCntOverloadPortn,
       "pmc1002CntCountersReset": pmc1002CntCountersReset,
       "pmc1002CntCountersStop": pmc1002CntCountersStop,
       "pmc1002controlsWrite": pmc1002controlsWrite,
       "pmc1002CtrlOther": pmc1002CtrlOther,
       "pmc1002CtrlconfMgnt1": pmc1002CtrlconfMgnt1,
       "pmc1002CtrlConf1Load1": pmc1002CtrlConf1Load1,
       "pmc1002CtrlConf2Load1": pmc1002CtrlConf2Load1,
       "pmc1002CtrlConf2Flash1": pmc1002CtrlConf2Flash1,
       "pmc1002CtrlConf2Clear1": pmc1002CtrlConf2Clear1,
       "pmc1002Ctrlsynth4": pmc1002Ctrlsynth4,
       "pmc1002CtrlCorrelatOn": pmc1002CtrlCorrelatOn,
       "pmc1002CtrlCorrelatOff": pmc1002CtrlCorrelatOff,
       "pmc1002CtrlswMgnt": pmc1002CtrlswMgnt,
       "pmc1002CtrlColdReset": pmc1002CtrlColdReset,
       "pmc1002CtrlWarmReset": pmc1002CtrlWarmReset,
       "pmc1002CtrlLoadSwBank1": pmc1002CtrlLoadSwBank1,
       "pmc1002CtrlLoadSwBank2": pmc1002CtrlLoadSwBank2,
       "pmc1002CtrlgwMgnt": pmc1002CtrlgwMgnt,
       "pmc1002CtrlCurrentGwReset": pmc1002CtrlCurrentGwReset,
       "pmc1002CtrlLoadGwBank1": pmc1002CtrlLoadGwBank1,
       "pmc1002CtrlLoadGwBank2": pmc1002CtrlLoadGwBank2,
       "pmc1002CtrlLoadGwBank3": pmc1002CtrlLoadGwBank3,
       "pmc1002CtrlLoadGwBank4": pmc1002CtrlLoadGwBank4,
       "pmc1002CtrlledTest": pmc1002CtrlledTest,
       "pmc1002CtrlGreenLed": pmc1002CtrlGreenLed,
       "pmc1002CtrlRedLed": pmc1002CtrlRedLed,
       "pmc1002CtrlLedOff": pmc1002CtrlLedOff,
       "pmc1002CtrlmoduleOosMode": pmc1002CtrlmoduleOosMode,
       "pmc1002CtrlModuleOosMode": pmc1002CtrlModuleOosMode,
       "pmc1002CtrlmoduleDccMgnt": pmc1002CtrlmoduleDccMgnt,
       "pmc1002CtrlmaintenanceMode": pmc1002CtrlmaintenanceMode,
       "pmc1002CtrlMaintenanceMode": pmc1002CtrlMaintenanceMode,
       "pmc1002CtrlClient": pmc1002CtrlClient,
       "pmc1002CtrlaccessLoopTable": pmc1002CtrlaccessLoopTable,
       "pmc1002CtrlaccessLoopEntry": pmc1002CtrlaccessLoopEntry,
       "pmc1002CtrlaccessLoopIndex": pmc1002CtrlaccessLoopIndex,
       "pmc1002CtrlaccessLoopPortn": pmc1002CtrlaccessLoopPortn,
       "pmc1002CtrlportOosModeTable": pmc1002CtrlportOosModeTable,
       "pmc1002CtrlportOosModeEntry": pmc1002CtrlportOosModeEntry,
       "pmc1002CtrlportOosModeIndex": pmc1002CtrlportOosModeIndex,
       "pmc1002CtrlportOosModePortn": pmc1002CtrlportOosModePortn,
       "pmc1002CtrlsfpOffCtrlTable": pmc1002CtrlsfpOffCtrlTable,
       "pmc1002CtrlsfpOffCtrlEntry": pmc1002CtrlsfpOffCtrlEntry,
       "pmc1002CtrlsfpOffCtrlIndex": pmc1002CtrlsfpOffCtrlIndex,
       "pmc1002CtrlsfpOffCtrlPortn": pmc1002CtrlsfpOffCtrlPortn,
       "pmc1002CtrlcsfUpInsTable": pmc1002CtrlcsfUpInsTable,
       "pmc1002CtrlcsfUpInsEntry": pmc1002CtrlcsfUpInsEntry,
       "pmc1002CtrlcsfUpInsIndex": pmc1002CtrlcsfUpInsIndex,
       "pmc1002CtrlcsfUpInsPortn": pmc1002CtrlcsfUpInsPortn,
       "pmc1002CtrlcaisDwInsTable": pmc1002CtrlcaisDwInsTable,
       "pmc1002CtrlcaisDwInsEntry": pmc1002CtrlcaisDwInsEntry,
       "pmc1002CtrlcaisDwInsIndex": pmc1002CtrlcaisDwInsIndex,
       "pmc1002CtrlcaisDwInsPortn": pmc1002CtrlcaisDwInsPortn,
       "pmc1002CtrlclientAccessTermLoopTable": pmc1002CtrlclientAccessTermLoopTable,
       "pmc1002CtrlclientAccessTermLoopEntry": pmc1002CtrlclientAccessTermLoopEntry,
       "pmc1002CtrlclientAccessTermLoopIndex": pmc1002CtrlclientAccessTermLoopIndex,
       "pmc1002CtrlclientAccessTermLoopPortn": pmc1002CtrlclientAccessTermLoopPortn,
       "pmc1002CtrlprotocolTable": pmc1002CtrlprotocolTable,
       "pmc1002CtrlprotocolEntry": pmc1002CtrlprotocolEntry,
       "pmc1002CtrlprotocolIndex": pmc1002CtrlprotocolIndex,
       "pmc1002CtrlprotocolPortn": pmc1002CtrlprotocolPortn,
       "pmc1002CtrlclientResetAllCountTable": pmc1002CtrlclientResetAllCountTable,
       "pmc1002CtrlclientResetAllCountEntry": pmc1002CtrlclientResetAllCountEntry,
       "pmc1002CtrlclientResetAllCountIndex": pmc1002CtrlclientResetAllCountIndex,
       "pmc1002CtrlclientResetAllCountsPortn": pmc1002CtrlclientResetAllCountsPortn,
       "pmc1002CtrlLine": pmc1002CtrlLine,
       "pmc1002CtrlcommAccessLoopTable": pmc1002CtrlcommAccessLoopTable,
       "pmc1002CtrlcommAccessLoopEntry": pmc1002CtrlcommAccessLoopEntry,
       "pmc1002CtrlcommAccessLoopIndex": pmc1002CtrlcommAccessLoopIndex,
       "pmc1002CtrlcommAccessLoopPortn": pmc1002CtrlcommAccessLoopPortn,
       "pmc1002CtrllineLoopTable": pmc1002CtrllineLoopTable,
       "pmc1002CtrllineLoopEntry": pmc1002CtrllineLoopEntry,
       "pmc1002CtrllineLoopIndex": pmc1002CtrllineLoopIndex,
       "pmc1002CtrllineLoopPortn": pmc1002CtrllineLoopPortn,
       "pmc1002CtrlmsAisTable": pmc1002CtrlmsAisTable,
       "pmc1002CtrlmsAisEntry": pmc1002CtrlmsAisEntry,
       "pmc1002CtrlmsAisIndex": pmc1002CtrlmsAisIndex,
       "pmc1002CtrlmsAisPortn": pmc1002CtrlmsAisPortn,
       "pmc1002CtrlfecDisableTable": pmc1002CtrlfecDisableTable,
       "pmc1002CtrlfecDisableEntry": pmc1002CtrlfecDisableEntry,
       "pmc1002CtrlfecDisableIndex": pmc1002CtrlfecDisableIndex,
       "pmc1002CtrlfecDisablePortn": pmc1002CtrlfecDisablePortn,
       "pmc1002CtrllineOosModeTable": pmc1002CtrllineOosModeTable,
       "pmc1002CtrllineOosModeEntry": pmc1002CtrllineOosModeEntry,
       "pmc1002CtrllineOosModeIndex": pmc1002CtrllineOosModeIndex,
       "pmc1002CtrllineOosModePortn": pmc1002CtrllineOosModePortn,
       "pmc1002CtrlxfpOnoffTable": pmc1002CtrlxfpOnoffTable,
       "pmc1002CtrlxfpOnoffEntry": pmc1002CtrlxfpOnoffEntry,
       "pmc1002CtrlxfpOnoffIndex": pmc1002CtrlxfpOnoffIndex,
       "pmc1002CtrlxfpOnoffPortn": pmc1002CtrlxfpOnoffPortn,
       "pmc1002CtrlxfpLineLoopTable": pmc1002CtrlxfpLineLoopTable,
       "pmc1002CtrlxfpLineLoopEntry": pmc1002CtrlxfpLineLoopEntry,
       "pmc1002CtrlxfpLineLoopIndex": pmc1002CtrlxfpLineLoopIndex,
       "pmc1002CtrlxfpLineLoopPortn": pmc1002CtrlxfpLineLoopPortn,
       "pmc1002CtrlxfpLineXfiLoopTable": pmc1002CtrlxfpLineXfiLoopTable,
       "pmc1002CtrlxfpLineXfiLoopEntry": pmc1002CtrlxfpLineXfiLoopEntry,
       "pmc1002CtrlxfpLineXfiLoopIndex": pmc1002CtrlxfpLineXfiLoopIndex,
       "pmc1002CtrlxfpLineXfiLoopPortn": pmc1002CtrlxfpLineXfiLoopPortn,
       "pmc1002CtrllineTunableChannelTable": pmc1002CtrllineTunableChannelTable,
       "pmc1002CtrllineTunableChannelEntry": pmc1002CtrllineTunableChannelEntry,
       "pmc1002CtrllineTunableChannelIndex": pmc1002CtrllineTunableChannelIndex,
       "pmc1002CtrllineTunableChannelPortn": pmc1002CtrllineTunableChannelPortn,
       "pmc1002CtrllinePhotodiodeModeTable": pmc1002CtrllinePhotodiodeModeTable,
       "pmc1002CtrllinePhotodiodeModeEntry": pmc1002CtrllinePhotodiodeModeEntry,
       "pmc1002CtrllinePhotodiodeModeIndex": pmc1002CtrllinePhotodiodeModeIndex,
       "pmc1002CtrllinePhotodiodeModePortn": pmc1002CtrllinePhotodiodeModePortn,
       "pmc1002CtrllinePhotodiodeValueTable": pmc1002CtrllinePhotodiodeValueTable,
       "pmc1002CtrllinePhotodiodeValueEntry": pmc1002CtrllinePhotodiodeValueEntry,
       "pmc1002CtrllinePhotodiodeValueIndex": pmc1002CtrllinePhotodiodeValueIndex,
       "pmc1002CtrllinePhotodiodeValuePortn": pmc1002CtrllinePhotodiodeValuePortn,
       "pmc1002CtrllinePowerLaserTable": pmc1002CtrllinePowerLaserTable,
       "pmc1002CtrllinePowerLaserEntry": pmc1002CtrllinePowerLaserEntry,
       "pmc1002CtrllinePowerLaserIndex": pmc1002CtrllinePowerLaserIndex,
       "pmc1002CtrllinePowerLaserPortn": pmc1002CtrllinePowerLaserPortn,
       "pmc1002CtrlotxVlhResetTable": pmc1002CtrlotxVlhResetTable,
       "pmc1002CtrlotxVlhResetEntry": pmc1002CtrlotxVlhResetEntry,
       "pmc1002CtrlotxVlhResetIndex": pmc1002CtrlotxVlhResetIndex,
       "pmc1002CtrlotxVlhResetPortn": pmc1002CtrlotxVlhResetPortn,
       "pmc1002CtrllineLoopTransceiverTable": pmc1002CtrllineLoopTransceiverTable,
       "pmc1002CtrllineLoopTransceiverEntry": pmc1002CtrllineLoopTransceiverEntry,
       "pmc1002CtrllineLoopTransceiverIndex": pmc1002CtrllineLoopTransceiverIndex,
       "pmc1002CtrllineLoopTransceiverPortn": pmc1002CtrllineLoopTransceiverPortn,
       "pmc1002CtrllineResetAllCountTable": pmc1002CtrllineResetAllCountTable,
       "pmc1002CtrllineResetAllCountEntry": pmc1002CtrllineResetAllCountEntry,
       "pmc1002CtrllineResetAllCountIndex": pmc1002CtrllineResetAllCountIndex,
       "pmc1002CtrllineResetAllCountsPortn": pmc1002CtrllineResetAllCountsPortn,
       "pmc1002ri": pmc1002ri,
       "pmc1002riTable": pmc1002riTable,
       "pmc1002RinvClientTable": pmc1002RinvClientTable,
       "pmc1002RinvClientEntry": pmc1002RinvClientEntry,
       "pmc1002RinvClientIndex": pmc1002RinvClientIndex,
       "pmc1002RinvClient": pmc1002RinvClient,
       "pmc1002RinvLineTable": pmc1002RinvLineTable,
       "pmc1002RinvLineEntry": pmc1002RinvLineEntry,
       "pmc1002RinvLineIndex": pmc1002RinvLineIndex,
       "pmc1002RinvxfpLine": pmc1002RinvxfpLine,
       "pmc1002RinvReloadInventory": pmc1002RinvReloadInventory,
       "pmc1002RinvHwPlatform": pmc1002RinvHwPlatform,
       "pmc1002RinvModulePlatform": pmc1002RinvModulePlatform,
       "pmc1002RinvSwPlatform": pmc1002RinvSwPlatform,
       "pmc1002RinvGwPlatform": pmc1002RinvGwPlatform,
       "pmc1002download": pmc1002download,
       "pmc1002DwlOther": pmc1002DwlOther,
       "pmc1002DwlrestartProcess": pmc1002DwlrestartProcess,
       "pmc1002DwlWarmRestartProcessed": pmc1002DwlWarmRestartProcessed,
       "pmc1002DwlColdRestartProcessed": pmc1002DwlColdRestartProcessed,
       "pmc1002DwlswBanksUsed": pmc1002DwlswBanksUsed,
       "pmc1002DwlSwBank1Used": pmc1002DwlSwBank1Used,
       "pmc1002DwlSwBank2Used": pmc1002DwlSwBank2Used,
       "pmc1002DwlSwBank1Notempty": pmc1002DwlSwBank1Notempty,
       "pmc1002DwlSwBank2Notempty": pmc1002DwlSwBank2Notempty,
       "pmc1002DwlgwBanksUsed": pmc1002DwlgwBanksUsed,
       "pmc1002DwlGwBank1Used": pmc1002DwlGwBank1Used,
       "pmc1002DwlGwBank2Used": pmc1002DwlGwBank2Used,
       "pmc1002DwlGwBank3Used": pmc1002DwlGwBank3Used,
       "pmc1002DwlGwBank4Used": pmc1002DwlGwBank4Used,
       "pmc1002DwlGwBank1Notempty": pmc1002DwlGwBank1Notempty,
       "pmc1002DwlGwBank2Notempty": pmc1002DwlGwBank2Notempty,
       "pmc1002DwlGwBank3Notempty": pmc1002DwlGwBank3Notempty,
       "pmc1002DwlGwBank4Notempty": pmc1002DwlGwBank4Notempty,
       "pmc1002DwlClient": pmc1002DwlClient,
       "pmc1002DwlLine": pmc1002DwlLine,
       "pmc1002Config": pmc1002Config,
       "pmc1002CfgAccessCAisCsf": pmc1002CfgAccessCAisCsf,
       "pmc1002CfgClientcaiscsfTable": pmc1002CfgClientcaiscsfTable,
       "pmc1002CfgClientcaiscsfEntry": pmc1002CfgClientcaiscsfEntry,
       "pmc1002CfgClientcaiscsfIndex": pmc1002CfgClientcaiscsfIndex,
       "pmc1002CfgCAisModePortn": pmc1002CfgCAisModePortn,
       "pmc1002CfgUpAccessioAlmPortn": pmc1002CfgUpAccessioAlmPortn,
       "pmc1002CfgUpMapperDeAlmPortn": pmc1002CfgUpMapperDeAlmPortn,
       "pmc1002CfgDownAccessioAlmPortn": pmc1002CfgDownAccessioAlmPortn,
       "pmc1002CfgDownMapperDeAlmPortn": pmc1002CfgDownMapperDeAlmPortn,
       "pmc1002CfgDownDfrmAlmPortn": pmc1002CfgDownDfrmAlmPortn,
       "pmc1002CfgDownLineSyncAlarmsPortn": pmc1002CfgDownLineSyncAlarmsPortn,
       "pmc1002CfgStartup": pmc1002CfgStartup,
       "pmc1002CfgClientStartupTable": pmc1002CfgClientStartupTable,
       "pmc1002CfgClientStartupEntry": pmc1002CfgClientStartupEntry,
       "pmc1002CfgClientStartupIndex": pmc1002CfgClientStartupIndex,
       "pmc1002CfgSystConfPortPortn": pmc1002CfgSystConfPortPortn,
       "pmc1002CfgNetConfPortPortn": pmc1002CfgNetConfPortPortn,
       "pmc1002CfgPortsOptionsPortn": pmc1002CfgPortsOptionsPortn,
       "pmc1002tablelineStartup": pmc1002tablelineStartup,
       "pmc1002CfgsynthTransLine1": pmc1002CfgsynthTransLine1,
       "pmc1002CfgnetConfMod": pmc1002CfgnetConfMod,
       "pmc1002CfglineOptions1": pmc1002CfglineOptions1,
       "pmc1002CfgsystTransLine2": pmc1002CfgsystTransLine2,
       "pmc1002CfglineSelection": pmc1002CfglineSelection,
       "pmc1002CfgXfpTable": pmc1002CfgXfpTable,
       "pmc1002CfgXfpEntry": pmc1002CfgXfpEntry,
       "pmc1002CfgXfpIndex": pmc1002CfgXfpIndex,
       "pmc1002CfgSystConfXfpPortn": pmc1002CfgSystConfXfpPortn,
       "pmc1002CfgDataRateConfXfpPortn": pmc1002CfgDataRateConfXfpPortn,
       "pmc1002CfgOtxtlhTable": pmc1002CfgOtxtlhTable,
       "pmc1002CfgOtxtlhEntry": pmc1002CfgOtxtlhEntry,
       "pmc1002CfgOtxtlhIndex": pmc1002CfgOtxtlhIndex,
       "pmc1002CfgLineOtxMiscPortn": pmc1002CfgLineOtxMiscPortn,
       "pmc1002CfgLineDitherRatePortn": pmc1002CfgLineDitherRatePortn,
       "pmc1002CfgLineDitherFhzPortn": pmc1002CfgLineDitherFhzPortn,
       "pmc1002CfgLinePwrLaserPortn": pmc1002CfgLinePwrLaserPortn,
       "pmc1002CfgLineFCurrentPortn": pmc1002CfgLineFCurrentPortn,
       "pmc1002CfgLineGridCurrentPortn": pmc1002CfgLineGridCurrentPortn,
       "pmc1002CfgFPortn": pmc1002CfgFPortn,
       "pmc1002CfgReservedPortn": pmc1002CfgReservedPortn,
       "pmc1002CfgLinePhotodiodeModePortn": pmc1002CfgLinePhotodiodeModePortn,
       "pmc1002CfgLinePhotodiodeValuePortn": pmc1002CfgLinePhotodiodeValuePortn,
       "pmc1002CfgLabels": pmc1002CfgLabels,
       "pmc1002CfgLabelclientTable": pmc1002CfgLabelclientTable,
       "pmc1002CfgLabelclientEntry": pmc1002CfgLabelclientEntry,
       "pmc1002CfgLabelclientIndex": pmc1002CfgLabelclientIndex,
       "pmc1002CfgLabelclientPortn": pmc1002CfgLabelclientPortn,
       "pmc1002CfgLabellineTable": pmc1002CfgLabellineTable,
       "pmc1002CfgLabellineEntry": pmc1002CfgLabellineEntry,
       "pmc1002CfgLabellineIndex": pmc1002CfgLabellineIndex,
       "pmc1002CfgLabellinePortn": pmc1002CfgLabellinePortn,
       "pmc1002CfgOther": pmc1002CfgOther,
       "pmc1002tablemoduleOther": pmc1002tablemoduleOther,
       "pmc1002Cfgmode": pmc1002Cfgmode,
       "pmc1002CfgStartuptablefive": pmc1002CfgStartuptablefive,
       "pmc1002CfgOtxtlhcapabilitiesTable": pmc1002CfgOtxtlhcapabilitiesTable,
       "pmc1002CfgOtxtlhcapabilitiesEntry": pmc1002CfgOtxtlhcapabilitiesEntry,
       "pmc1002CfgOtxtlhcapabilitiesIndex": pmc1002CfgOtxtlhcapabilitiesIndex,
       "pmc1002CfgComponentTypePortn": pmc1002CfgComponentTypePortn,
       "pmc1002CfgMiscellaneousPortn": pmc1002CfgMiscellaneousPortn,
       "pmc1002CfgFirstChannelPortn": pmc1002CfgFirstChannelPortn,
       "pmc1002CfgLastChannelPortn": pmc1002CfgLastChannelPortn,
       "pmc1002CfgGridPortn": pmc1002CfgGridPortn,
       "pmc1002CfgWriteConfiguration": pmc1002CfgWriteConfiguration,
       "pmc1002traps": pmc1002traps,
       "pmc1002trapBoardNumber": pmc1002trapBoardNumber,
       "pmc1002trapClientNumber": pmc1002trapClientNumber,
       "pmc1002trapLineNumber": pmc1002trapLineNumber,
       "pmc1002LineTrapNotUrgentGoesOn": pmc1002LineTrapNotUrgentGoesOn,
       "pmc1002LineTrapNotUrgentGoesOff": pmc1002LineTrapNotUrgentGoesOff,
       "pmc1002LineTrapUrgentGoesOn": pmc1002LineTrapUrgentGoesOn,
       "pmc1002LineTrapUrgentGoesOff": pmc1002LineTrapUrgentGoesOff,
       "pmc1002LineTrapCritGoesOn": pmc1002LineTrapCritGoesOn,
       "pmc1002LineTrapCritGoesOff": pmc1002LineTrapCritGoesOff,
       "pmc1002ClientTrapNotUrgentGoesOn": pmc1002ClientTrapNotUrgentGoesOn,
       "pmc1002ClientTrapNotUrgentGoesOff": pmc1002ClientTrapNotUrgentGoesOff,
       "pmc1002ClientTrapUrgentGoesOn": pmc1002ClientTrapUrgentGoesOn,
       "pmc1002ClientTrapUrgentGoesOff": pmc1002ClientTrapUrgentGoesOff,
       "pmc1002ClientTrapCritGoesOn": pmc1002ClientTrapCritGoesOn,
       "pmc1002ClientTrapCritGoesOff": pmc1002ClientTrapCritGoesOff,
       "pmc1002PowerTrapUrgentGoesOn": pmc1002PowerTrapUrgentGoesOn,
       "pmc1002PowerTrapUrgentGoesOff": pmc1002PowerTrapUrgentGoesOff,
       "pmc1002Monitoring": pmc1002Monitoring,
       "pmc1002MonOther": pmc1002MonOther,
       "pmc1002MonSync": pmc1002MonSync,
       "pmc1002PerfEnable": pmc1002PerfEnable,
       "pmc1002Perf15minSync": pmc1002Perf15minSync,
       "pmc1002Perf24hSync": pmc1002Perf24hSync,
       "pmc1002MonTimeStamp": pmc1002MonTimeStamp,
       "pmc1002Perf15MinShort": pmc1002Perf15MinShort,
       "pmc1002Perf15MinLong": pmc1002Perf15MinLong,
       "pmc1002Perf24HoursShort": pmc1002Perf24HoursShort,
       "pmc1002Perf24HoursLong": pmc1002Perf24HoursLong,
       "pmc1002PerfCurrent15MinElapsedTime": pmc1002PerfCurrent15MinElapsedTime,
       "pmc1002PerfCurrent24HoursElapsedTime": pmc1002PerfCurrent24HoursElapsedTime,
       "pmc1002MonClient": pmc1002MonClient,
       "pmc1002PerfTelecomClientCurrent15StatTable": pmc1002PerfTelecomClientCurrent15StatTable,
       "pmc1002PerfTelecomClientCurrent15StatEntry": pmc1002PerfTelecomClientCurrent15StatEntry,
       "pmc1002PerfTelecomClientCurrent15StatIndex": pmc1002PerfTelecomClientCurrent15StatIndex,
       "pmc1002PerfTelecomClientCurrent15StatInvCvPortn": pmc1002PerfTelecomClientCurrent15StatInvCvPortn,
       "pmc1002PerfTelecomClientCurrent15StatCvValuePortn": pmc1002PerfTelecomClientCurrent15StatCvValuePortn,
       "pmc1002PerfTelecomClientCurrent15StatInvEsPortn": pmc1002PerfTelecomClientCurrent15StatInvEsPortn,
       "pmc1002PerfTelecomClientCurrent15StatEsValuePortn": pmc1002PerfTelecomClientCurrent15StatEsValuePortn,
       "pmc1002PerfTelecomClientCurrent15StatInvSesPortn": pmc1002PerfTelecomClientCurrent15StatInvSesPortn,
       "pmc1002PerfTelecomClientCurrent15StatSesValuePortn": pmc1002PerfTelecomClientCurrent15StatSesValuePortn,
       "pmc1002PerfTelecomClientCurrent15StatInvSefsPortn": pmc1002PerfTelecomClientCurrent15StatInvSefsPortn,
       "pmc1002PerfTelecomClientCurrent15StatSefsValuePortn": pmc1002PerfTelecomClientCurrent15StatSefsValuePortn,
       "pmc1002PerfTelecomClientCurrent15StatInvUasPortn": pmc1002PerfTelecomClientCurrent15StatInvUasPortn,
       "pmc1002PerfTelecomClientCurrent15StatUasValuePortn": pmc1002PerfTelecomClientCurrent15StatUasValuePortn,
       "pmc1002PerfTelecomClientPast15StatHistoryPort1Table": pmc1002PerfTelecomClientPast15StatHistoryPort1Table,
       "pmc1002PerfTelecomClientPast15StatHistoryPort1Entry": pmc1002PerfTelecomClientPast15StatHistoryPort1Entry,
       "pmc1002PerfTelecomClientPast15StatHistoryPort1Index": pmc1002PerfTelecomClientPast15StatHistoryPort1Index,
       "pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1": pmc1002PerfTelecomClientPast15StatHistoryInvCvPort1,
       "pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1": pmc1002PerfTelecomClientPast15StatHistoryCvValuePort1,
       "pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1": pmc1002PerfTelecomClientPast15StatHistoryInvEsPort1,
       "pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1": pmc1002PerfTelecomClientPast15StatHistoryEsValuePort1,
       "pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1": pmc1002PerfTelecomClientPast15StatHistoryInvSesPort1,
       "pmc1002PerfTelecomClientPast15StatHistorySesValuePort1": pmc1002PerfTelecomClientPast15StatHistorySesValuePort1,
       "pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1": pmc1002PerfTelecomClientPast15StatHistoryInvSefsPort1,
       "pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1": pmc1002PerfTelecomClientPast15StatHistorySefsValuePort1,
       "pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1": pmc1002PerfTelecomClientPast15StatHistoryInvUasPort1,
       "pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1": pmc1002PerfTelecomClientPast15StatHistoryUasValuePort1,
       "pmc1002PerfTelecomClientCurrent24StatTable": pmc1002PerfTelecomClientCurrent24StatTable,
       "pmc1002PerfTelecomClientCurrent24StatEntry": pmc1002PerfTelecomClientCurrent24StatEntry,
       "pmc1002PerfTelecomClientCurrent24StatIndex": pmc1002PerfTelecomClientCurrent24StatIndex,
       "pmc1002PerfTelecomClientCurrent24StatInvCvPortn": pmc1002PerfTelecomClientCurrent24StatInvCvPortn,
       "pmc1002PerfTelecomClientCurrent24StatCvValuePortn": pmc1002PerfTelecomClientCurrent24StatCvValuePortn,
       "pmc1002PerfTelecomClientCurrent24StatInvEsPortn": pmc1002PerfTelecomClientCurrent24StatInvEsPortn,
       "pmc1002PerfTelecomClientCurrent24StatEsValuePortn": pmc1002PerfTelecomClientCurrent24StatEsValuePortn,
       "pmc1002PerfTelecomClientCurrent24StatInvSesPortn": pmc1002PerfTelecomClientCurrent24StatInvSesPortn,
       "pmc1002PerfTelecomClientCurrent24StatSesValuePortn": pmc1002PerfTelecomClientCurrent24StatSesValuePortn,
       "pmc1002PerfTelecomClientCurrent24StatInvSefsPortn": pmc1002PerfTelecomClientCurrent24StatInvSefsPortn,
       "pmc1002PerfTelecomClientCurrent24StatSefsValuePortn": pmc1002PerfTelecomClientCurrent24StatSefsValuePortn,
       "pmc1002PerfTelecomClientCurrent24StatInvUasPortn": pmc1002PerfTelecomClientCurrent24StatInvUasPortn,
       "pmc1002PerfTelecomClientCurrent24StatUasValuePortn": pmc1002PerfTelecomClientCurrent24StatUasValuePortn,
       "pmc1002PerfTelecomClientPast24StatHistoryPort1Table": pmc1002PerfTelecomClientPast24StatHistoryPort1Table,
       "pmc1002PerfTelecomClientPast24StatHistoryPort1Entry": pmc1002PerfTelecomClientPast24StatHistoryPort1Entry,
       "pmc1002PerfTelecomClientPast24StatHistoryPort1Index": pmc1002PerfTelecomClientPast24StatHistoryPort1Index,
       "pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1": pmc1002PerfTelecomClientPast24StatHistoryInvCvPort1,
       "pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1": pmc1002PerfTelecomClientPast24StatHistoryCvValuePort1,
       "pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1": pmc1002PerfTelecomClientPast24StatHistoryInvEsPort1,
       "pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1": pmc1002PerfTelecomClientPast24StatHistoryEsValuePort1,
       "pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1": pmc1002PerfTelecomClientPast24StatHistoryInvSesPort1,
       "pmc1002PerfTelecomClientPast24StatHistorySesValuePort1": pmc1002PerfTelecomClientPast24StatHistorySesValuePort1,
       "pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1": pmc1002PerfTelecomClientPast24StatHistoryInvSefsPort1,
       "pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1": pmc1002PerfTelecomClientPast24StatHistorySefsValuePort1,
       "pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1": pmc1002PerfTelecomClientPast24StatHistoryInvUasPort1,
       "pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1": pmc1002PerfTelecomClientPast24StatHistoryUasValuePort1,
       "pmc1002PerfDatacomClientCurrent15StatTable": pmc1002PerfDatacomClientCurrent15StatTable,
       "pmc1002PerfDatacomClientCurrent15StatEntry": pmc1002PerfDatacomClientCurrent15StatEntry,
       "pmc1002PerfDatacomClientCurrent15StatIndex": pmc1002PerfDatacomClientCurrent15StatIndex,
       "pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn": pmc1002perfdatacomclientCurrent15StatInBytesCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatInBytesCountPortn": pmc1002perfdatacomclientCurrent15StatInBytesCountPortn,
       "pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn": pmc1002perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatInCrcCountPortn": pmc1002perfdatacomclientCurrent15StatInCrcCountPortn,
       "pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn": pmc1002perfdatacomclientCurrent15StatInBroadcastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn": pmc1002perfdatacomclientCurrent15StatInBroadcastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn": pmc1002perfdatacomclientCurrent15StatInMulticastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn": pmc1002perfdatacomclientCurrent15StatInMulticastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn": pmc1002perfdatacomclientCurrent15StatInUnicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn": pmc1002perfdatacomclientCurrent15StatInUnicastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn": pmc1002perfdatacomclientCurrent15StatInNonunicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn": pmc1002perfdatacomclientCurrent15StatInNonunicastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn": pmc1002perfdatacomclientCurrent15StatOutBytesCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn": pmc1002perfdatacomclientCurrent15StatOutBytesCountPortn,
       "pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn": pmc1002perfdatacomclientCurrent15StatOutBroadcastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn": pmc1002perfdatacomclientCurrent15StatOutBroadcastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn": pmc1002perfdatacomclientCurrent15StatOutMulticastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn": pmc1002perfdatacomclientCurrent15StatOutMulticastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn": pmc1002perfdatacomclientCurrent15StatOutUnicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn": pmc1002perfdatacomclientCurrent15StatOutUnicastCountPortn,
       "pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn": pmc1002perfdatacomclientCurrent15StatOutNonunicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn": pmc1002perfdatacomclientCurrent15StatOutNonunicastCountPortn,
       "pmc1002PerfDatacomClientPast15StatHistoryPort1Table": pmc1002PerfDatacomClientPast15StatHistoryPort1Table,
       "pmc1002PerfDatacomClientPast15StatHistoryPort1Entry": pmc1002PerfDatacomClientPast15StatHistoryPort1Entry,
       "pmc1002PerfDatacomClientPast15StatHistoryPort1Index": pmc1002PerfDatacomClientPast15StatHistoryPort1Index,
       "pmc1002perfdatacomclientPast15StatInBytesCountInvPort1": pmc1002perfdatacomclientPast15StatInBytesCountInvPort1,
       "pmc1002perfdatacomclientPast15StatInBytesCountPort1": pmc1002perfdatacomclientPast15StatInBytesCountPort1,
       "pmc1002perfdatacomclientPast15StatInCrcCountInvPort1": pmc1002perfdatacomclientPast15StatInCrcCountInvPort1,
       "pmc1002perfdatacomclientPast15StatInCrcCountPort1": pmc1002perfdatacomclientPast15StatInCrcCountPort1,
       "pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1": pmc1002perfdatacomclientPast15StatInBroadcastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatInBroadcastCountPort1": pmc1002perfdatacomclientPast15StatInBroadcastCountPort1,
       "pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1": pmc1002perfdatacomclientPast15StatInMulticastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatInMulticastCountPort1": pmc1002perfdatacomclientPast15StatInMulticastCountPort1,
       "pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1": pmc1002perfdatacomclientPast15StatInUnicastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatInUnicastCountPort1": pmc1002perfdatacomclientPast15StatInUnicastCountPort1,
       "pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1": pmc1002perfdatacomclientPast15StatInNonunicastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatInNonunicastCountPort1": pmc1002perfdatacomclientPast15StatInNonunicastCountPort1,
       "pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1": pmc1002perfdatacomclientPast15StatOutBytesCountInvPort1,
       "pmc1002perfdatacomclientPast15StatOutBytesCountPort1": pmc1002perfdatacomclientPast15StatOutBytesCountPort1,
       "pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1": pmc1002perfdatacomclientPast15StatOutBroadcastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1": pmc1002perfdatacomclientPast15StatOutBroadcastCountPort1,
       "pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1": pmc1002perfdatacomclientPast15StatOutMulticastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatOutMulticastCountPort1": pmc1002perfdatacomclientPast15StatOutMulticastCountPort1,
       "pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1": pmc1002perfdatacomclientPast15StatOutUnicastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatOutUnicastCountPort1": pmc1002perfdatacomclientPast15StatOutUnicastCountPort1,
       "pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1": pmc1002perfdatacomclientPast15StatOutNonunicastCountInvPort1,
       "pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1": pmc1002perfdatacomclientPast15StatOutNonunicastCountPort1,
       "pmc1002PerfDatacomClientCurrent24StatTable": pmc1002PerfDatacomClientCurrent24StatTable,
       "pmc1002PerfDatacomClientCurrent24StatEntry": pmc1002PerfDatacomClientCurrent24StatEntry,
       "pmc1002PerfDatacomClientCurrent24StatIndex": pmc1002PerfDatacomClientCurrent24StatIndex,
       "pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn": pmc1002perfdatacomclientCurrent24StatInBytesCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatInBytesCountPortn": pmc1002perfdatacomclientCurrent24StatInBytesCountPortn,
       "pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn": pmc1002perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatInCrcCountPortn": pmc1002perfdatacomclientCurrent24StatInCrcCountPortn,
       "pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn": pmc1002perfdatacomclientCurrent24StatInBroadcastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn": pmc1002perfdatacomclientCurrent24StatInBroadcastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn": pmc1002perfdatacomclientCurrent24StatInMulticastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn": pmc1002perfdatacomclientCurrent24StatInMulticastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn": pmc1002perfdatacomclientCurrent24StatInUnicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn": pmc1002perfdatacomclientCurrent24StatInUnicastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn": pmc1002perfdatacomclientCurrent24StatInNonunicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn": pmc1002perfdatacomclientCurrent24StatInNonunicastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn": pmc1002perfdatacomclientCurrent24StatOutBytesCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn": pmc1002perfdatacomclientCurrent24StatOutBytesCountPortn,
       "pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn": pmc1002perfdatacomclientCurrent24StatOutBroadcastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn": pmc1002perfdatacomclientCurrent24StatOutBroadcastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn": pmc1002perfdatacomclientCurrent24StatOutMulticastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn": pmc1002perfdatacomclientCurrent24StatOutMulticastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn": pmc1002perfdatacomclientCurrent24StatOutUnicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn": pmc1002perfdatacomclientCurrent24StatOutUnicastCountPortn,
       "pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn": pmc1002perfdatacomclientCurrent24StatOutNonunicastCountInvPortn,
       "pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn": pmc1002perfdatacomclientCurrent24StatOutNonunicastCountPortn,
       "pmc1002PerfDatacomClientPast24StatHistoryPort1Table": pmc1002PerfDatacomClientPast24StatHistoryPort1Table,
       "pmc1002PerfDatacomClientPast24StatHistoryPort1Entry": pmc1002PerfDatacomClientPast24StatHistoryPort1Entry,
       "pmc1002PerfDatacomClientPast24StatHistoryPort1Index": pmc1002PerfDatacomClientPast24StatHistoryPort1Index,
       "pmc1002perfdatacomclientPast24StatInBytesCountInvPort1": pmc1002perfdatacomclientPast24StatInBytesCountInvPort1,
       "pmc1002perfdatacomclientPast24StatInBytesCountPort1": pmc1002perfdatacomclientPast24StatInBytesCountPort1,
       "pmc1002perfdatacomclientPast24StatInCrcCountInvPort1": pmc1002perfdatacomclientPast24StatInCrcCountInvPort1,
       "pmc1002perfdatacomclientPast24StatInCrcCountPort1": pmc1002perfdatacomclientPast24StatInCrcCountPort1,
       "pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1": pmc1002perfdatacomclientPast24StatInBroadcastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatInBroadcastCountPort1": pmc1002perfdatacomclientPast24StatInBroadcastCountPort1,
       "pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1": pmc1002perfdatacomclientPast24StatInMulticastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatInMulticastCountPort1": pmc1002perfdatacomclientPast24StatInMulticastCountPort1,
       "pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1": pmc1002perfdatacomclientPast24StatInUnicastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatInUnicastCountPort1": pmc1002perfdatacomclientPast24StatInUnicastCountPort1,
       "pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1": pmc1002perfdatacomclientPast24StatInNonunicastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatInNonunicastCountPort1": pmc1002perfdatacomclientPast24StatInNonunicastCountPort1,
       "pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1": pmc1002perfdatacomclientPast24StatOutBytesCountInvPort1,
       "pmc1002perfdatacomclientPast24StatOutBytesCountPort1": pmc1002perfdatacomclientPast24StatOutBytesCountPort1,
       "pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1": pmc1002perfdatacomclientPast24StatOutBroadcastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1": pmc1002perfdatacomclientPast24StatOutBroadcastCountPort1,
       "pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1": pmc1002perfdatacomclientPast24StatOutMulticastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatOutMulticastCountPort1": pmc1002perfdatacomclientPast24StatOutMulticastCountPort1,
       "pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1": pmc1002perfdatacomclientPast24StatOutUnicastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatOutUnicastCountPort1": pmc1002perfdatacomclientPast24StatOutUnicastCountPort1,
       "pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1": pmc1002perfdatacomclientPast24StatOutNonunicastCountInvPort1,
       "pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1": pmc1002perfdatacomclientPast24StatOutNonunicastCountPort1,
       "pmc1002MonLine": pmc1002MonLine,
       "pmc1002PerfTelecomLineCurrent15StatTable": pmc1002PerfTelecomLineCurrent15StatTable,
       "pmc1002PerfTelecomLineCurrent15StatEntry": pmc1002PerfTelecomLineCurrent15StatEntry,
       "pmc1002PerfTelecomLineCurrent15StatIndex": pmc1002PerfTelecomLineCurrent15StatIndex,
       "pmc1002PerfTelecomLineCurrent15StatInvCvPortn": pmc1002PerfTelecomLineCurrent15StatInvCvPortn,
       "pmc1002PerfTelecomLineCurrent15StatCvValuePortn": pmc1002PerfTelecomLineCurrent15StatCvValuePortn,
       "pmc1002PerfTelecomLineCurrent15StatInvEsPortn": pmc1002PerfTelecomLineCurrent15StatInvEsPortn,
       "pmc1002PerfTelecomLineCurrent15StatEsValuePortn": pmc1002PerfTelecomLineCurrent15StatEsValuePortn,
       "pmc1002PerfTelecomLineCurrent15StatInvSesPortn": pmc1002PerfTelecomLineCurrent15StatInvSesPortn,
       "pmc1002PerfTelecomLineCurrent15StatSesValuePortn": pmc1002PerfTelecomLineCurrent15StatSesValuePortn,
       "pmc1002PerfTelecomLineCurrent15StatInvSefsPortn": pmc1002PerfTelecomLineCurrent15StatInvSefsPortn,
       "pmc1002PerfTelecomLineCurrent15StatSefsValuePortn": pmc1002PerfTelecomLineCurrent15StatSefsValuePortn,
       "pmc1002PerfTelecomLineCurrent15StatInvUasPortn": pmc1002PerfTelecomLineCurrent15StatInvUasPortn,
       "pmc1002PerfTelecomLineCurrent15StatUasValuePortn": pmc1002PerfTelecomLineCurrent15StatUasValuePortn,
       "pmc1002PerfTelecomLinePast15StatHistoryPort1Table": pmc1002PerfTelecomLinePast15StatHistoryPort1Table,
       "pmc1002PerfTelecomLinePast15StatHistoryPort1Entry": pmc1002PerfTelecomLinePast15StatHistoryPort1Entry,
       "pmc1002PerfTelecomLinePast15StatHistoryPort1Index": pmc1002PerfTelecomLinePast15StatHistoryPort1Index,
       "pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1": pmc1002PerfTelecomLinePast15StatHistoryInvCvPort1,
       "pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1": pmc1002PerfTelecomLinePast15StatHistoryCvValuePort1,
       "pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1": pmc1002PerfTelecomLinePast15StatHistoryInvEsPort1,
       "pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1": pmc1002PerfTelecomLinePast15StatHistoryEsValuePort1,
       "pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1": pmc1002PerfTelecomLinePast15StatHistoryInvSesPort1,
       "pmc1002PerfTelecomLinePast15StatHistorySesValuePort1": pmc1002PerfTelecomLinePast15StatHistorySesValuePort1,
       "pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1": pmc1002PerfTelecomLinePast15StatHistoryInvSefsPort1,
       "pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1": pmc1002PerfTelecomLinePast15StatHistorySefsValuePort1,
       "pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1": pmc1002PerfTelecomLinePast15StatHistoryInvUasPort1,
       "pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1": pmc1002PerfTelecomLinePast15StatHistoryUasValuePort1,
       "pmc1002PerfTelecomLineCurrent24StatTable": pmc1002PerfTelecomLineCurrent24StatTable,
       "pmc1002PerfTelecomLineCurrent24StatEntry": pmc1002PerfTelecomLineCurrent24StatEntry,
       "pmc1002PerfTelecomLineCurrent24StatIndex": pmc1002PerfTelecomLineCurrent24StatIndex,
       "pmc1002PerfTelecomLineCurrent24StatInvCvPortn": pmc1002PerfTelecomLineCurrent24StatInvCvPortn,
       "pmc1002PerfTelecomLineCurrent24StatCvValuePortn": pmc1002PerfTelecomLineCurrent24StatCvValuePortn,
       "pmc1002PerfTelecomLineCurrent24StatInvEsPortn": pmc1002PerfTelecomLineCurrent24StatInvEsPortn,
       "pmc1002PerfTelecomLineCurrent24StatEsValuePortn": pmc1002PerfTelecomLineCurrent24StatEsValuePortn,
       "pmc1002PerfTelecomLineCurrent24StatInvSesPortn": pmc1002PerfTelecomLineCurrent24StatInvSesPortn,
       "pmc1002PerfTelecomLineCurrent24StatSesValuePortn": pmc1002PerfTelecomLineCurrent24StatSesValuePortn,
       "pmc1002PerfTelecomLineCurrent24StatInvSefsPortn": pmc1002PerfTelecomLineCurrent24StatInvSefsPortn,
       "pmc1002PerfTelecomLineCurrent24StatSefsValuePortn": pmc1002PerfTelecomLineCurrent24StatSefsValuePortn,
       "pmc1002PerfTelecomLineCurrent24StatInvUasPortn": pmc1002PerfTelecomLineCurrent24StatInvUasPortn,
       "pmc1002PerfTelecomLineCurrent24StatUasValuePortn": pmc1002PerfTelecomLineCurrent24StatUasValuePortn,
       "pmc1002PerfTelecomLinePast24StatHistoryPort1Table": pmc1002PerfTelecomLinePast24StatHistoryPort1Table,
       "pmc1002PerfTelecomLinePast24StatHistoryPort1Entry": pmc1002PerfTelecomLinePast24StatHistoryPort1Entry,
       "pmc1002PerfTelecomLinePast24StatHistoryPort1Index": pmc1002PerfTelecomLinePast24StatHistoryPort1Index,
       "pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1": pmc1002PerfTelecomLinePast24StatHistoryInvCvPort1,
       "pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1": pmc1002PerfTelecomLinePast24StatHistoryCvValuePort1,
       "pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1": pmc1002PerfTelecomLinePast24StatHistoryInvEsPort1,
       "pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1": pmc1002PerfTelecomLinePast24StatHistoryEsValuePort1,
       "pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1": pmc1002PerfTelecomLinePast24StatHistoryInvSesPort1,
       "pmc1002PerfTelecomLinePast24StatHistorySesValuePort1": pmc1002PerfTelecomLinePast24StatHistorySesValuePort1,
       "pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1": pmc1002PerfTelecomLinePast24StatHistoryInvSefsPort1,
       "pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1": pmc1002PerfTelecomLinePast24StatHistorySefsValuePort1,
       "pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1": pmc1002PerfTelecomLinePast24StatHistoryInvUasPort1,
       "pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1": pmc1002PerfTelecomLinePast24StatHistoryUasValuePort1,
       "pmc1002Rmon": pmc1002Rmon,
       "pmc1002RmonClient": pmc1002RmonClient,
       "pmc1002MonupRmonByteCntTable": pmc1002MonupRmonByteCntTable,
       "pmc1002MonupRmonByteCntEntry": pmc1002MonupRmonByteCntEntry,
       "pmc1002MonupRmonByteCntIndex": pmc1002MonupRmonByteCntIndex,
       "pmc1002MonupRmonByteCntValuePortn": pmc1002MonupRmonByteCntValuePortn,
       "pmc1002MonupRmonByteCntErrorPortn": pmc1002MonupRmonByteCntErrorPortn,
       "pmc1002MonupRmonByteCntOverloadPortn": pmc1002MonupRmonByteCntOverloadPortn,
       "pmc1002MonupRmonCrcErrorCntTable": pmc1002MonupRmonCrcErrorCntTable,
       "pmc1002MonupRmonCrcErrorCntEntry": pmc1002MonupRmonCrcErrorCntEntry,
       "pmc1002MonupRmonCrcErrorCntIndex": pmc1002MonupRmonCrcErrorCntIndex,
       "pmc1002MonupRmonCrcErrorCntValuePortn": pmc1002MonupRmonCrcErrorCntValuePortn,
       "pmc1002MonupRmonCrcErrorCntErrorPortn": pmc1002MonupRmonCrcErrorCntErrorPortn,
       "pmc1002MonupRmonCrcErrorCntOverloadPortn": pmc1002MonupRmonCrcErrorCntOverloadPortn,
       "pmc1002MonupRmonPacketsCntTable": pmc1002MonupRmonPacketsCntTable,
       "pmc1002MonupRmonPacketsCntEntry": pmc1002MonupRmonPacketsCntEntry,
       "pmc1002MonupRmonPacketsCntIndex": pmc1002MonupRmonPacketsCntIndex,
       "pmc1002MonupRmonPacketsCntValuePortn": pmc1002MonupRmonPacketsCntValuePortn,
       "pmc1002MonupRmonPacketsCntErrorPortn": pmc1002MonupRmonPacketsCntErrorPortn,
       "pmc1002MonupRmonPacketsCntOverloadPortn": pmc1002MonupRmonPacketsCntOverloadPortn,
       "pmc1002MonupRmonBroadcastCntTable": pmc1002MonupRmonBroadcastCntTable,
       "pmc1002MonupRmonBroadcastCntEntry": pmc1002MonupRmonBroadcastCntEntry,
       "pmc1002MonupRmonBroadcastCntIndex": pmc1002MonupRmonBroadcastCntIndex,
       "pmc1002MonupRmonBroadcastCntValuePortn": pmc1002MonupRmonBroadcastCntValuePortn,
       "pmc1002MonupRmonBroadcastCntErrorPortn": pmc1002MonupRmonBroadcastCntErrorPortn,
       "pmc1002MonupRmonBroadcastCntOverloadPortn": pmc1002MonupRmonBroadcastCntOverloadPortn,
       "pmc1002MonupRmonMulticastCntTable": pmc1002MonupRmonMulticastCntTable,
       "pmc1002MonupRmonMulticastCntEntry": pmc1002MonupRmonMulticastCntEntry,
       "pmc1002MonupRmonMulticastCntIndex": pmc1002MonupRmonMulticastCntIndex,
       "pmc1002MonupRmonMulticastCntValuePortn": pmc1002MonupRmonMulticastCntValuePortn,
       "pmc1002MonupRmonMulticastCntErrorPortn": pmc1002MonupRmonMulticastCntErrorPortn,
       "pmc1002MonupRmonMulticastCntOverloadPortn": pmc1002MonupRmonMulticastCntOverloadPortn,
       "pmc1002MonupRmonTimerCntTable": pmc1002MonupRmonTimerCntTable,
       "pmc1002MonupRmonTimerCntEntry": pmc1002MonupRmonTimerCntEntry,
       "pmc1002MonupRmonTimerCntIndex": pmc1002MonupRmonTimerCntIndex,
       "pmc1002MonupRmonTimerCntValuePortn": pmc1002MonupRmonTimerCntValuePortn,
       "pmc1002MonupRmonTimerCntErrorPortn": pmc1002MonupRmonTimerCntErrorPortn,
       "pmc1002MonupRmonTimerCntOverloadPortn": pmc1002MonupRmonTimerCntOverloadPortn,
       "pmc1002MonupRmonPauseFrameCntTable": pmc1002MonupRmonPauseFrameCntTable,
       "pmc1002MonupRmonPauseFrameCntEntry": pmc1002MonupRmonPauseFrameCntEntry,
       "pmc1002MonupRmonPauseFrameCntIndex": pmc1002MonupRmonPauseFrameCntIndex,
       "pmc1002MonupRmonPauseFrameCntValuePortn": pmc1002MonupRmonPauseFrameCntValuePortn,
       "pmc1002MonupRmonPauseFrameCntErrorPortn": pmc1002MonupRmonPauseFrameCntErrorPortn,
       "pmc1002MonupRmonPauseFrameCntOverloadPortn": pmc1002MonupRmonPauseFrameCntOverloadPortn,
       "pmc1002MonupRmonDropFrameCntTable": pmc1002MonupRmonDropFrameCntTable,
       "pmc1002MonupRmonDropFrameCntEntry": pmc1002MonupRmonDropFrameCntEntry,
       "pmc1002MonupRmonDropFrameCntIndex": pmc1002MonupRmonDropFrameCntIndex,
       "pmc1002MonupRmonDropFrameCntValuePortn": pmc1002MonupRmonDropFrameCntValuePortn,
       "pmc1002MonupRmonDropFrameCntErrorPortn": pmc1002MonupRmonDropFrameCntErrorPortn,
       "pmc1002MonupRmonDropFrameCntOverloadPortn": pmc1002MonupRmonDropFrameCntOverloadPortn,
       "pmc1002MonupRmonBitsCntTable": pmc1002MonupRmonBitsCntTable,
       "pmc1002MonupRmonBitsCntEntry": pmc1002MonupRmonBitsCntEntry,
       "pmc1002MonupRmonBitsCntIndex": pmc1002MonupRmonBitsCntIndex,
       "pmc1002MonupRmonBitsCntValuePortn": pmc1002MonupRmonBitsCntValuePortn,
       "pmc1002MonupRmonBitsCntErrorPortn": pmc1002MonupRmonBitsCntErrorPortn,
       "pmc1002MonupRmonBitsCntOverloadPortn": pmc1002MonupRmonBitsCntOverloadPortn,
       "pmc1002MonupRmonUnicastCntTable": pmc1002MonupRmonUnicastCntTable,
       "pmc1002MonupRmonUnicastCntEntry": pmc1002MonupRmonUnicastCntEntry,
       "pmc1002MonupRmonUnicastCntIndex": pmc1002MonupRmonUnicastCntIndex,
       "pmc1002MonupRmonUnicastCntValuePortn": pmc1002MonupRmonUnicastCntValuePortn,
       "pmc1002MonupRmonUnicastCntErrorPortn": pmc1002MonupRmonUnicastCntErrorPortn,
       "pmc1002MonupRmonUnicastCntOverloadPortn": pmc1002MonupRmonUnicastCntOverloadPortn,
       "pmc1002MonupRmonNonUnicastCntTable": pmc1002MonupRmonNonUnicastCntTable,
       "pmc1002MonupRmonNonUnicastCntEntry": pmc1002MonupRmonNonUnicastCntEntry,
       "pmc1002MonupRmonNonUnicastCntIndex": pmc1002MonupRmonNonUnicastCntIndex,
       "pmc1002MonupRmonNonUnicastCntValuePortn": pmc1002MonupRmonNonUnicastCntValuePortn,
       "pmc1002MonupRmonNonUnicastCntErrorPortn": pmc1002MonupRmonNonUnicastCntErrorPortn,
       "pmc1002MonupRmonNonUnicastCntOverloadPortn": pmc1002MonupRmonNonUnicastCntOverloadPortn,
       "pmc1002MondwRmonByteCntTable": pmc1002MondwRmonByteCntTable,
       "pmc1002MondwRmonByteCntEntry": pmc1002MondwRmonByteCntEntry,
       "pmc1002MondwRmonByteCntIndex": pmc1002MondwRmonByteCntIndex,
       "pmc1002MondwRmonByteCntValuePortn": pmc1002MondwRmonByteCntValuePortn,
       "pmc1002MondwRmonByteCntErrorPortn": pmc1002MondwRmonByteCntErrorPortn,
       "pmc1002MondwRmonByteCntOverloadPortn": pmc1002MondwRmonByteCntOverloadPortn,
       "pmc1002MondwRmonCrcErrorCntTable": pmc1002MondwRmonCrcErrorCntTable,
       "pmc1002MondwRmonCrcErrorCntEntry": pmc1002MondwRmonCrcErrorCntEntry,
       "pmc1002MondwRmonCrcErrorCntIndex": pmc1002MondwRmonCrcErrorCntIndex,
       "pmc1002MondwRmonCrcErrorCntValuePortn": pmc1002MondwRmonCrcErrorCntValuePortn,
       "pmc1002MondwRmonCrcErrorCntErrorPortn": pmc1002MondwRmonCrcErrorCntErrorPortn,
       "pmc1002MondwRmonCrcErrorCntOverloadPortn": pmc1002MondwRmonCrcErrorCntOverloadPortn,
       "pmc1002MondwRmonPacketsCntTable": pmc1002MondwRmonPacketsCntTable,
       "pmc1002MondwRmonPacketsCntEntry": pmc1002MondwRmonPacketsCntEntry,
       "pmc1002MondwRmonPacketsCntIndex": pmc1002MondwRmonPacketsCntIndex,
       "pmc1002MondwRmonPacketsCntValuePortn": pmc1002MondwRmonPacketsCntValuePortn,
       "pmc1002MondwRmonPacketsCntErrorPortn": pmc1002MondwRmonPacketsCntErrorPortn,
       "pmc1002MondwRmonPacketsCntOverloadPortn": pmc1002MondwRmonPacketsCntOverloadPortn,
       "pmc1002MondwRmonBroadcastCntTable": pmc1002MondwRmonBroadcastCntTable,
       "pmc1002MondwRmonBroadcastCntEntry": pmc1002MondwRmonBroadcastCntEntry,
       "pmc1002MondwRmonBroadcastCntIndex": pmc1002MondwRmonBroadcastCntIndex,
       "pmc1002MondwRmonBroadcastCntValuePortn": pmc1002MondwRmonBroadcastCntValuePortn,
       "pmc1002MondwRmonBroadcastCntErrorPortn": pmc1002MondwRmonBroadcastCntErrorPortn,
       "pmc1002MondwRmonBroadcastCntOverloadPortn": pmc1002MondwRmonBroadcastCntOverloadPortn,
       "pmc1002MondwRmonMulticastCntTable": pmc1002MondwRmonMulticastCntTable,
       "pmc1002MondwRmonMulticastCntEntry": pmc1002MondwRmonMulticastCntEntry,
       "pmc1002MondwRmonMulticastCntIndex": pmc1002MondwRmonMulticastCntIndex,
       "pmc1002MondwRmonMulticastCntValuePortn": pmc1002MondwRmonMulticastCntValuePortn,
       "pmc1002MondwRmonMulticastCntErrorPortn": pmc1002MondwRmonMulticastCntErrorPortn,
       "pmc1002MondwRmonMulticastCntOverloadPortn": pmc1002MondwRmonMulticastCntOverloadPortn,
       "pmc1002MondwRmonPauseFrameCntTable": pmc1002MondwRmonPauseFrameCntTable,
       "pmc1002MondwRmonPauseFrameCntEntry": pmc1002MondwRmonPauseFrameCntEntry,
       "pmc1002MondwRmonPauseFrameCntIndex": pmc1002MondwRmonPauseFrameCntIndex,
       "pmc1002MondwRmonPauseFrameCntValuePortn": pmc1002MondwRmonPauseFrameCntValuePortn,
       "pmc1002MondwRmonPauseFrameCntErrorPortn": pmc1002MondwRmonPauseFrameCntErrorPortn,
       "pmc1002MondwRmonPauseFrameCntOverloadPortn": pmc1002MondwRmonPauseFrameCntOverloadPortn,
       "pmc1002MondwRmonTimerCntTable": pmc1002MondwRmonTimerCntTable,
       "pmc1002MondwRmonTimerCntEntry": pmc1002MondwRmonTimerCntEntry,
       "pmc1002MondwRmonTimerCntIndex": pmc1002MondwRmonTimerCntIndex,
       "pmc1002MondwRmonTimerCntValuePortn": pmc1002MondwRmonTimerCntValuePortn,
       "pmc1002MondwRmonTimerCntErrorPortn": pmc1002MondwRmonTimerCntErrorPortn,
       "pmc1002MondwRmonTimerCntOverloadPortn": pmc1002MondwRmonTimerCntOverloadPortn,
       "pmc1002MondwRmonBitsCntTable": pmc1002MondwRmonBitsCntTable,
       "pmc1002MondwRmonBitsCntEntry": pmc1002MondwRmonBitsCntEntry,
       "pmc1002MondwRmonBitsCntIndex": pmc1002MondwRmonBitsCntIndex,
       "pmc1002MondwRmonBitsCntValuePortn": pmc1002MondwRmonBitsCntValuePortn,
       "pmc1002MondwRmonBitsCntErrorPortn": pmc1002MondwRmonBitsCntErrorPortn,
       "pmc1002MondwRmonBitsCntOverloadPortn": pmc1002MondwRmonBitsCntOverloadPortn,
       "pmc1002MondwRmonUnicastCntTable": pmc1002MondwRmonUnicastCntTable,
       "pmc1002MondwRmonUnicastCntEntry": pmc1002MondwRmonUnicastCntEntry,
       "pmc1002MondwRmonUnicastCntIndex": pmc1002MondwRmonUnicastCntIndex,
       "pmc1002MondwRmonUnicastCntValuePortn": pmc1002MondwRmonUnicastCntValuePortn,
       "pmc1002MondwRmonUnicastCntErrorPortn": pmc1002MondwRmonUnicastCntErrorPortn,
       "pmc1002MondwRmonUnicastCntOverloadPortn": pmc1002MondwRmonUnicastCntOverloadPortn,
       "pmc1002MondwRmonNonUnicastCntTable": pmc1002MondwRmonNonUnicastCntTable,
       "pmc1002MondwRmonNonUnicastCntEntry": pmc1002MondwRmonNonUnicastCntEntry,
       "pmc1002MondwRmonNonUnicastCntIndex": pmc1002MondwRmonNonUnicastCntIndex,
       "pmc1002MondwRmonNonUnicastCntValuePortn": pmc1002MondwRmonNonUnicastCntValuePortn,
       "pmc1002MondwRmonNonUnicastCntErrorPortn": pmc1002MondwRmonNonUnicastCntErrorPortn,
       "pmc1002MondwRmonNonUnicastCntOverloadPortn": pmc1002MondwRmonNonUnicastCntOverloadPortn,
       "pmc1002RmonLine": pmc1002RmonLine,
       "pmc1002RmonOther": pmc1002RmonOther,
       "pmc1002MonCountersReset": pmc1002MonCountersReset,
       "pmc1002MonCountersStop": pmc1002MonCountersStop}
)
