# SNMP MIB module (EKINOPS-Pm1001IM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1001IM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:47 2025
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

modulePm1001im = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15)
)
if mibBuilder.loadTexts:
    modulePm1001im.setRevisions(
        ("2007-06-05 00:00",
         "2007-07-09 00:00",
         "2007-12-07 00:00",
         "2008-11-27 00:00",
         "2008-12-04 00:00",
         "2009-04-09 00:00",
         "2009-10-06 00:00",
         "2010-02-04 00:00",
         "2010-02-04 00:00",
         "2010-03-03 00:00",
         "2011-02-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1001imBandwidthMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oneline", 0),
          ("twolines", 1),
          ("threelines", 2),
          ("fourlines", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Pm1001imalarms_ObjectIdentity = ObjectIdentity
pm1001imalarms = _Pm1001imalarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2)
)
_Pm1001imAlmOther_ObjectIdentity = ObjectIdentity
pm1001imAlmOther = _Pm1001imAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1)
)
_Pm1001imAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1001imAlmOtherNurg = _Pm1001imAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1)
)
_Pm1001imAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1001imAlmsynthAlm2 = _Pm1001imAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1, 2)
)
_Pm1001imAlmConfTableSave_Type = EkiOnOff
_Pm1001imAlmConfTableSave_Object = MibScalar
pm1001imAlmConfTableSave = _Pm1001imAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1, 2, 1),
    _Pm1001imAlmConfTableSave_Type()
)
pm1001imAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmConfTableSave.setStatus("current")
_Pm1001imAlmInvUpload_Type = EkiOnOff
_Pm1001imAlmInvUpload_Object = MibScalar
pm1001imAlmInvUpload = _Pm1001imAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1, 2, 2),
    _Pm1001imAlmInvUpload_Type()
)
pm1001imAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmInvUpload.setStatus("current")
_Pm1001imAlmConfTableLoad_Type = EkiOnOff
_Pm1001imAlmConfTableLoad_Object = MibScalar
pm1001imAlmConfTableLoad = _Pm1001imAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1, 2, 3),
    _Pm1001imAlmConfTableLoad_Type()
)
pm1001imAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmConfTableLoad.setStatus("current")
_Pm1001imAlmCorrelatOff_Type = EkiOnOff
_Pm1001imAlmCorrelatOff_Object = MibScalar
pm1001imAlmCorrelatOff = _Pm1001imAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1, 2, 4),
    _Pm1001imAlmCorrelatOff_Type()
)
pm1001imAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmCorrelatOff.setStatus("current")
_Pm1001imAlmMaintenanceOn_Type = EkiOnOff
_Pm1001imAlmMaintenanceOn_Object = MibScalar
pm1001imAlmMaintenanceOn = _Pm1001imAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 1, 2, 5),
    _Pm1001imAlmMaintenanceOn_Type()
)
pm1001imAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmMaintenanceOn.setStatus("current")
_Pm1001imAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1001imAlmOtherUrg = _Pm1001imAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2)
)
_Pm1001imAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1001imAlmmodInitFailLevel2 = _Pm1001imAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 194)
)
_Pm1001imAlmLedFail_Type = EkiOnOff
_Pm1001imAlmLedFail_Object = MibScalar
pm1001imAlmLedFail = _Pm1001imAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 194, 1),
    _Pm1001imAlmLedFail_Type()
)
pm1001imAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLedFail.setStatus("current")
_Pm1001imAlmNextColdBootForced_Type = EkiOnOff
_Pm1001imAlmNextColdBootForced_Object = MibScalar
pm1001imAlmNextColdBootForced = _Pm1001imAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 194, 2),
    _Pm1001imAlmNextColdBootForced_Type()
)
pm1001imAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmNextColdBootForced.setStatus("current")
_Pm1001imAlmBootUndone_Type = EkiOnOff
_Pm1001imAlmBootUndone_Object = MibScalar
pm1001imAlmBootUndone = _Pm1001imAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 194, 3),
    _Pm1001imAlmBootUndone_Type()
)
pm1001imAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmBootUndone.setStatus("current")
_Pm1001imAlmResetHwInitFail_Type = EkiOnOff
_Pm1001imAlmResetHwInitFail_Object = MibScalar
pm1001imAlmResetHwInitFail = _Pm1001imAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 194, 4),
    _Pm1001imAlmResetHwInitFail_Type()
)
pm1001imAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmResetHwInitFail.setStatus("current")
_Pm1001imAlmSwInitFail_Type = EkiOnOff
_Pm1001imAlmSwInitFail_Object = MibScalar
pm1001imAlmSwInitFail = _Pm1001imAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 194, 5),
    _Pm1001imAlmSwInitFail_Type()
)
pm1001imAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmSwInitFail.setStatus("current")
_Pm1001imAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1001imAlmmodInitFailLevel3 = _Pm1001imAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195)
)
_Pm1001imAlmGwIdentFail_Type = EkiOnOff
_Pm1001imAlmGwIdentFail_Object = MibScalar
pm1001imAlmGwIdentFail = _Pm1001imAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 1),
    _Pm1001imAlmGwIdentFail_Type()
)
pm1001imAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmGwIdentFail.setStatus("current")
_Pm1001imAlmObmTypeReadFail_Type = EkiOnOff
_Pm1001imAlmObmTypeReadFail_Object = MibScalar
pm1001imAlmObmTypeReadFail = _Pm1001imAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 2),
    _Pm1001imAlmObmTypeReadFail_Type()
)
pm1001imAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmObmTypeReadFail.setStatus("current")
_Pm1001imAlmInitModuleFail_Type = EkiOnOff
_Pm1001imAlmInitModuleFail_Object = MibScalar
pm1001imAlmInitModuleFail = _Pm1001imAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 3),
    _Pm1001imAlmInitModuleFail_Type()
)
pm1001imAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmInitModuleFail.setStatus("current")
_Pm1001imAlmClientXfpInitFail_Type = EkiOnOff
_Pm1001imAlmClientXfpInitFail_Object = MibScalar
pm1001imAlmClientXfpInitFail = _Pm1001imAlmClientXfpInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 5),
    _Pm1001imAlmClientXfpInitFail_Type()
)
pm1001imAlmClientXfpInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientXfpInitFail.setStatus("current")
_Pm1001imAlmLineInitFail_Type = EkiOnOff
_Pm1001imAlmLineInitFail_Object = MibScalar
pm1001imAlmLineInitFail = _Pm1001imAlmLineInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 7),
    _Pm1001imAlmLineInitFail_Type()
)
pm1001imAlmLineInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineInitFail.setStatus("current")
_Pm1001imAlmLine1InitFail_Type = EkiOnOff
_Pm1001imAlmLine1InitFail_Object = MibScalar
pm1001imAlmLine1InitFail = _Pm1001imAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 9),
    _Pm1001imAlmLine1InitFail_Type()
)
pm1001imAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLine1InitFail.setStatus("current")
_Pm1001imAlmLine2InitFail_Type = EkiOnOff
_Pm1001imAlmLine2InitFail_Object = MibScalar
pm1001imAlmLine2InitFail = _Pm1001imAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 10),
    _Pm1001imAlmLine2InitFail_Type()
)
pm1001imAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLine2InitFail.setStatus("current")
_Pm1001imAlmLine3InitFail_Type = EkiOnOff
_Pm1001imAlmLine3InitFail_Object = MibScalar
pm1001imAlmLine3InitFail = _Pm1001imAlmLine3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 11),
    _Pm1001imAlmLine3InitFail_Type()
)
pm1001imAlmLine3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLine3InitFail.setStatus("current")
_Pm1001imAlmLine4InitFail_Type = EkiOnOff
_Pm1001imAlmLine4InitFail_Object = MibScalar
pm1001imAlmLine4InitFail = _Pm1001imAlmLine4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 2, 195, 12),
    _Pm1001imAlmLine4InitFail_Type()
)
pm1001imAlmLine4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLine4InitFail.setStatus("current")
_Pm1001imAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1001imAlmOtherCrit = _Pm1001imAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 3)
)
_Pm1001imAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1001imAlmsynthAlm0 = _Pm1001imAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 3, 0)
)
_Pm1001imAlmModGlobFail_Type = EkiOnOff
_Pm1001imAlmModGlobFail_Object = MibScalar
pm1001imAlmModGlobFail = _Pm1001imAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 3, 0, 9),
    _Pm1001imAlmModGlobFail_Type()
)
pm1001imAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmModGlobFail.setStatus("current")
_Pm1001imAlmDefFuseA_Type = EkiOnOff
_Pm1001imAlmDefFuseA_Object = MibScalar
pm1001imAlmDefFuseA = _Pm1001imAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 3, 0, 15),
    _Pm1001imAlmDefFuseA_Type()
)
pm1001imAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDefFuseA.setStatus("current")
_Pm1001imAlmDefFuseB_Type = EkiOnOff
_Pm1001imAlmDefFuseB_Object = MibScalar
pm1001imAlmDefFuseB = _Pm1001imAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 1, 3, 0, 16),
    _Pm1001imAlmDefFuseB_Type()
)
pm1001imAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDefFuseB.setStatus("current")
_Pm1001imAlmClient_ObjectIdentity = ObjectIdentity
pm1001imAlmClient = _Pm1001imAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2)
)
_Pm1001imAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1001imAlmClientNurg = _Pm1001imAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1)
)
_Pm1001imAlmclientXfpWarnings_ObjectIdentity = ObjectIdentity
pm1001imAlmclientXfpWarnings = _Pm1001imAlmclientXfpWarnings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209)
)
_Pm1001imAlmClientTxPowerLowWarning_Type = EkiOnOff
_Pm1001imAlmClientTxPowerLowWarning_Object = MibScalar
pm1001imAlmClientTxPowerLowWarning = _Pm1001imAlmClientTxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 1),
    _Pm1001imAlmClientTxPowerLowWarning_Type()
)
pm1001imAlmClientTxPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxPowerLowWarning.setStatus("current")
_Pm1001imAlmClientTxPowerHighWarning_Type = EkiOnOff
_Pm1001imAlmClientTxPowerHighWarning_Object = MibScalar
pm1001imAlmClientTxPowerHighWarning = _Pm1001imAlmClientTxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 2),
    _Pm1001imAlmClientTxPowerHighWarning_Type()
)
pm1001imAlmClientTxPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxPowerHighWarning.setStatus("current")
_Pm1001imAlmClientTxBiasLowWarning_Type = EkiOnOff
_Pm1001imAlmClientTxBiasLowWarning_Object = MibScalar
pm1001imAlmClientTxBiasLowWarning = _Pm1001imAlmClientTxBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 3),
    _Pm1001imAlmClientTxBiasLowWarning_Type()
)
pm1001imAlmClientTxBiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxBiasLowWarning.setStatus("current")
_Pm1001imAlmClientTxBiasHighWarning_Type = EkiOnOff
_Pm1001imAlmClientTxBiasHighWarning_Object = MibScalar
pm1001imAlmClientTxBiasHighWarning = _Pm1001imAlmClientTxBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 4),
    _Pm1001imAlmClientTxBiasHighWarning_Type()
)
pm1001imAlmClientTxBiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxBiasHighWarning.setStatus("current")
_Pm1001imAlmClientTempLowWarning_Type = EkiOnOff
_Pm1001imAlmClientTempLowWarning_Object = MibScalar
pm1001imAlmClientTempLowWarning = _Pm1001imAlmClientTempLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 7),
    _Pm1001imAlmClientTempLowWarning_Type()
)
pm1001imAlmClientTempLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTempLowWarning.setStatus("current")
_Pm1001imAlmClientTempHighWarning_Type = EkiOnOff
_Pm1001imAlmClientTempHighWarning_Object = MibScalar
pm1001imAlmClientTempHighWarning = _Pm1001imAlmClientTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 8),
    _Pm1001imAlmClientTempHighWarning_Type()
)
pm1001imAlmClientTempHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTempHighWarning.setStatus("current")
_Pm1001imAlmClientRxPowerLowWarning_Type = EkiOnOff
_Pm1001imAlmClientRxPowerLowWarning_Object = MibScalar
pm1001imAlmClientRxPowerLowWarning = _Pm1001imAlmClientRxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 15),
    _Pm1001imAlmClientRxPowerLowWarning_Type()
)
pm1001imAlmClientRxPowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRxPowerLowWarning.setStatus("current")
_Pm1001imAlmClientRxPowerHighWarning_Type = EkiOnOff
_Pm1001imAlmClientRxPowerHighWarning_Object = MibScalar
pm1001imAlmClientRxPowerHighWarning = _Pm1001imAlmClientRxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 1, 209, 16),
    _Pm1001imAlmClientRxPowerHighWarning_Type()
)
pm1001imAlmClientRxPowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRxPowerHighWarning.setStatus("current")
_Pm1001imAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1001imAlmClientUrg = _Pm1001imAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2)
)
_Pm1001imAlmclientXfpAlarm1_ObjectIdentity = ObjectIdentity
pm1001imAlmclientXfpAlarm1 = _Pm1001imAlmclientXfpAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208)
)
_Pm1001imAlmClientTxPowerLowAlarm_Type = EkiOnOff
_Pm1001imAlmClientTxPowerLowAlarm_Object = MibScalar
pm1001imAlmClientTxPowerLowAlarm = _Pm1001imAlmClientTxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 1),
    _Pm1001imAlmClientTxPowerLowAlarm_Type()
)
pm1001imAlmClientTxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxPowerLowAlarm.setStatus("current")
_Pm1001imAlmClientTxPowerHighAlarm_Type = EkiOnOff
_Pm1001imAlmClientTxPowerHighAlarm_Object = MibScalar
pm1001imAlmClientTxPowerHighAlarm = _Pm1001imAlmClientTxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 2),
    _Pm1001imAlmClientTxPowerHighAlarm_Type()
)
pm1001imAlmClientTxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxPowerHighAlarm.setStatus("current")
_Pm1001imAlmClientTxBiasLowAlarm_Type = EkiOnOff
_Pm1001imAlmClientTxBiasLowAlarm_Object = MibScalar
pm1001imAlmClientTxBiasLowAlarm = _Pm1001imAlmClientTxBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 3),
    _Pm1001imAlmClientTxBiasLowAlarm_Type()
)
pm1001imAlmClientTxBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxBiasLowAlarm.setStatus("current")
_Pm1001imAlmClientTxBiasHighAlarm_Type = EkiOnOff
_Pm1001imAlmClientTxBiasHighAlarm_Object = MibScalar
pm1001imAlmClientTxBiasHighAlarm = _Pm1001imAlmClientTxBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 4),
    _Pm1001imAlmClientTxBiasHighAlarm_Type()
)
pm1001imAlmClientTxBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxBiasHighAlarm.setStatus("current")
_Pm1001imAlmClientTempLowAlarm_Type = EkiOnOff
_Pm1001imAlmClientTempLowAlarm_Object = MibScalar
pm1001imAlmClientTempLowAlarm = _Pm1001imAlmClientTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 7),
    _Pm1001imAlmClientTempLowAlarm_Type()
)
pm1001imAlmClientTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTempLowAlarm.setStatus("current")
_Pm1001imAlmClientTempHighAlarm_Type = EkiOnOff
_Pm1001imAlmClientTempHighAlarm_Object = MibScalar
pm1001imAlmClientTempHighAlarm = _Pm1001imAlmClientTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 8),
    _Pm1001imAlmClientTempHighAlarm_Type()
)
pm1001imAlmClientTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTempHighAlarm.setStatus("current")
_Pm1001imAlmClientRxPowerLowAlarm_Type = EkiOnOff
_Pm1001imAlmClientRxPowerLowAlarm_Object = MibScalar
pm1001imAlmClientRxPowerLowAlarm = _Pm1001imAlmClientRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 15),
    _Pm1001imAlmClientRxPowerLowAlarm_Type()
)
pm1001imAlmClientRxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRxPowerLowAlarm.setStatus("current")
_Pm1001imAlmClientRxPowerHighAlarm_Type = EkiOnOff
_Pm1001imAlmClientRxPowerHighAlarm_Object = MibScalar
pm1001imAlmClientRxPowerHighAlarm = _Pm1001imAlmClientRxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 208, 16),
    _Pm1001imAlmClientRxPowerHighAlarm_Type()
)
pm1001imAlmClientRxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRxPowerHighAlarm.setStatus("current")
_Pm1001imAlmclientXfpSupplyAlarm_ObjectIdentity = ObjectIdentity
pm1001imAlmclientXfpSupplyAlarm = _Pm1001imAlmclientXfpSupplyAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212)
)
_Pm1001imAlmClientVee5LowAlarm_Type = EkiOnOff
_Pm1001imAlmClientVee5LowAlarm_Object = MibScalar
pm1001imAlmClientVee5LowAlarm = _Pm1001imAlmClientVee5LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 1),
    _Pm1001imAlmClientVee5LowAlarm_Type()
)
pm1001imAlmClientVee5LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVee5LowAlarm.setStatus("current")
_Pm1001imAlmClientVee5HighAlarm_Type = EkiOnOff
_Pm1001imAlmClientVee5HighAlarm_Object = MibScalar
pm1001imAlmClientVee5HighAlarm = _Pm1001imAlmClientVee5HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 2),
    _Pm1001imAlmClientVee5HighAlarm_Type()
)
pm1001imAlmClientVee5HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVee5HighAlarm.setStatus("current")
_Pm1001imAlmClientVcc2LowAlarm_Type = EkiOnOff
_Pm1001imAlmClientVcc2LowAlarm_Object = MibScalar
pm1001imAlmClientVcc2LowAlarm = _Pm1001imAlmClientVcc2LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 3),
    _Pm1001imAlmClientVcc2LowAlarm_Type()
)
pm1001imAlmClientVcc2LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc2LowAlarm.setStatus("current")
_Pm1001imAlmClientVcc2HighAlarm_Type = EkiOnOff
_Pm1001imAlmClientVcc2HighAlarm_Object = MibScalar
pm1001imAlmClientVcc2HighAlarm = _Pm1001imAlmClientVcc2HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 4),
    _Pm1001imAlmClientVcc2HighAlarm_Type()
)
pm1001imAlmClientVcc2HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc2HighAlarm.setStatus("current")
_Pm1001imAlmClientVcc3LowAlarm_Type = EkiOnOff
_Pm1001imAlmClientVcc3LowAlarm_Object = MibScalar
pm1001imAlmClientVcc3LowAlarm = _Pm1001imAlmClientVcc3LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 5),
    _Pm1001imAlmClientVcc3LowAlarm_Type()
)
pm1001imAlmClientVcc3LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc3LowAlarm.setStatus("current")
_Pm1001imAlmClientVcc3HighAlarm_Type = EkiOnOff
_Pm1001imAlmClientVcc3HighAlarm_Object = MibScalar
pm1001imAlmClientVcc3HighAlarm = _Pm1001imAlmClientVcc3HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 6),
    _Pm1001imAlmClientVcc3HighAlarm_Type()
)
pm1001imAlmClientVcc3HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc3HighAlarm.setStatus("current")
_Pm1001imAlmClientVcc5LowAlarm_Type = EkiOnOff
_Pm1001imAlmClientVcc5LowAlarm_Object = MibScalar
pm1001imAlmClientVcc5LowAlarm = _Pm1001imAlmClientVcc5LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 7),
    _Pm1001imAlmClientVcc5LowAlarm_Type()
)
pm1001imAlmClientVcc5LowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc5LowAlarm.setStatus("current")
_Pm1001imAlmClientVcc5HighAlarm_Type = EkiOnOff
_Pm1001imAlmClientVcc5HighAlarm_Object = MibScalar
pm1001imAlmClientVcc5HighAlarm = _Pm1001imAlmClientVcc5HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 8),
    _Pm1001imAlmClientVcc5HighAlarm_Type()
)
pm1001imAlmClientVcc5HighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc5HighAlarm.setStatus("current")
_Pm1001imAlmClientVee5LowWarning_Type = EkiOnOff
_Pm1001imAlmClientVee5LowWarning_Object = MibScalar
pm1001imAlmClientVee5LowWarning = _Pm1001imAlmClientVee5LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 9),
    _Pm1001imAlmClientVee5LowWarning_Type()
)
pm1001imAlmClientVee5LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVee5LowWarning.setStatus("current")
_Pm1001imAlmClientVee5HighWarning_Type = EkiOnOff
_Pm1001imAlmClientVee5HighWarning_Object = MibScalar
pm1001imAlmClientVee5HighWarning = _Pm1001imAlmClientVee5HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 10),
    _Pm1001imAlmClientVee5HighWarning_Type()
)
pm1001imAlmClientVee5HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVee5HighWarning.setStatus("current")
_Pm1001imAlmClientVcc2LowWarning_Type = EkiOnOff
_Pm1001imAlmClientVcc2LowWarning_Object = MibScalar
pm1001imAlmClientVcc2LowWarning = _Pm1001imAlmClientVcc2LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 11),
    _Pm1001imAlmClientVcc2LowWarning_Type()
)
pm1001imAlmClientVcc2LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc2LowWarning.setStatus("current")
_Pm1001imAlmClientVcc2HighWarning_Type = EkiOnOff
_Pm1001imAlmClientVcc2HighWarning_Object = MibScalar
pm1001imAlmClientVcc2HighWarning = _Pm1001imAlmClientVcc2HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 12),
    _Pm1001imAlmClientVcc2HighWarning_Type()
)
pm1001imAlmClientVcc2HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc2HighWarning.setStatus("current")
_Pm1001imAlmClientVcc3LowWarning_Type = EkiOnOff
_Pm1001imAlmClientVcc3LowWarning_Object = MibScalar
pm1001imAlmClientVcc3LowWarning = _Pm1001imAlmClientVcc3LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 13),
    _Pm1001imAlmClientVcc3LowWarning_Type()
)
pm1001imAlmClientVcc3LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc3LowWarning.setStatus("current")
_Pm1001imAlmClientVcc3HighWarning_Type = EkiOnOff
_Pm1001imAlmClientVcc3HighWarning_Object = MibScalar
pm1001imAlmClientVcc3HighWarning = _Pm1001imAlmClientVcc3HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 14),
    _Pm1001imAlmClientVcc3HighWarning_Type()
)
pm1001imAlmClientVcc3HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc3HighWarning.setStatus("current")
_Pm1001imAlmClientVcc5LowWarning_Type = EkiOnOff
_Pm1001imAlmClientVcc5LowWarning_Object = MibScalar
pm1001imAlmClientVcc5LowWarning = _Pm1001imAlmClientVcc5LowWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 15),
    _Pm1001imAlmClientVcc5LowWarning_Type()
)
pm1001imAlmClientVcc5LowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc5LowWarning.setStatus("current")
_Pm1001imAlmClientVcc5HighWarning_Type = EkiOnOff
_Pm1001imAlmClientVcc5HighWarning_Object = MibScalar
pm1001imAlmClientVcc5HighWarning = _Pm1001imAlmClientVcc5HighWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 2, 212, 16),
    _Pm1001imAlmClientVcc5HighWarning_Type()
)
pm1001imAlmClientVcc5HighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientVcc5HighWarning.setStatus("current")
_Pm1001imAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1001imAlmClientCrit = _Pm1001imAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3)
)
_Pm1001imAlmsynthAlmClient_ObjectIdentity = ObjectIdentity
pm1001imAlmsynthAlmClient = _Pm1001imAlmsynthAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7)
)
_Pm1001imAlmClientXfpAbsent_Type = EkiOnOff
_Pm1001imAlmClientXfpAbsent_Object = MibScalar
pm1001imAlmClientXfpAbsent = _Pm1001imAlmClientXfpAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 1),
    _Pm1001imAlmClientXfpAbsent_Type()
)
pm1001imAlmClientXfpAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientXfpAbsent.setStatus("current")
_Pm1001imAlmClientDdmAbsent_Type = EkiOnOff
_Pm1001imAlmClientDdmAbsent_Object = MibScalar
pm1001imAlmClientDdmAbsent = _Pm1001imAlmClientDdmAbsent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 2),
    _Pm1001imAlmClientDdmAbsent_Type()
)
pm1001imAlmClientDdmAbsent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientDdmAbsent.setStatus("current")
_Pm1001imAlmClientHwFail_Type = EkiOnOff
_Pm1001imAlmClientHwFail_Object = MibScalar
pm1001imAlmClientHwFail = _Pm1001imAlmClientHwFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 4),
    _Pm1001imAlmClientHwFail_Type()
)
pm1001imAlmClientHwFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientHwFail.setStatus("current")
_Pm1001imAlmClientDwLsd_Type = EkiOnOff
_Pm1001imAlmClientDwLsd_Object = MibScalar
pm1001imAlmClientDwLsd = _Pm1001imAlmClientDwLsd_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 5),
    _Pm1001imAlmClientDwLsd_Type()
)
pm1001imAlmClientDwLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientDwLsd.setStatus("current")
_Pm1001imAlmClientLocalOos0_Type = EkiOnOff
_Pm1001imAlmClientLocalOos0_Object = MibScalar
pm1001imAlmClientLocalOos0 = _Pm1001imAlmClientLocalOos0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 6),
    _Pm1001imAlmClientLocalOos0_Type()
)
pm1001imAlmClientLocalOos0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientLocalOos0.setStatus("current")
_Pm1001imAlmClientRemoteOos0_Type = EkiOnOff
_Pm1001imAlmClientRemoteOos0_Object = MibScalar
pm1001imAlmClientRemoteOos0 = _Pm1001imAlmClientRemoteOos0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 7),
    _Pm1001imAlmClientRemoteOos0_Type()
)
pm1001imAlmClientRemoteOos0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRemoteOos0.setStatus("current")
_Pm1001imAlmClientDwCais_Type = EkiOnOff
_Pm1001imAlmClientDwCais_Object = MibScalar
pm1001imAlmClientDwCais = _Pm1001imAlmClientDwCais_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 8),
    _Pm1001imAlmClientDwCais_Type()
)
pm1001imAlmClientDwCais.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientDwCais.setStatus("current")
_Pm1001imAlmClientSfpDdmWarning_Type = EkiOnOff
_Pm1001imAlmClientSfpDdmWarning_Object = MibScalar
pm1001imAlmClientSfpDdmWarning = _Pm1001imAlmClientSfpDdmWarning_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 9),
    _Pm1001imAlmClientSfpDdmWarning_Type()
)
pm1001imAlmClientSfpDdmWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientSfpDdmWarning.setStatus("current")
_Pm1001imAlmClientSfpDdmAlm_Type = EkiOnOff
_Pm1001imAlmClientSfpDdmAlm_Object = MibScalar
pm1001imAlmClientSfpDdmAlm = _Pm1001imAlmClientSfpDdmAlm_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 10),
    _Pm1001imAlmClientSfpDdmAlm_Type()
)
pm1001imAlmClientSfpDdmAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientSfpDdmAlm.setStatus("current")
_Pm1001imAlmClientFail_Type = EkiOnOff
_Pm1001imAlmClientFail_Object = MibScalar
pm1001imAlmClientFail = _Pm1001imAlmClientFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 12),
    _Pm1001imAlmClientFail_Type()
)
pm1001imAlmClientFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientFail.setStatus("current")
_Pm1001imAlmClientUpCsf_Type = EkiOnOff
_Pm1001imAlmClientUpCsf_Object = MibScalar
pm1001imAlmClientUpCsf = _Pm1001imAlmClientUpCsf_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 7, 16),
    _Pm1001imAlmClientUpCsf_Type()
)
pm1001imAlmClientUpCsf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientUpCsf.setStatus("current")
_Pm1001imAlmclientAccessioAlm_ObjectIdentity = ObjectIdentity
pm1001imAlmclientAccessioAlm = _Pm1001imAlmclientAccessioAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 168)
)
_Pm1001imAlmClientDwLasFail_Type = EkiOnOff
_Pm1001imAlmClientDwLasFail_Object = MibScalar
pm1001imAlmClientDwLasFail = _Pm1001imAlmClientDwLasFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 168, 1),
    _Pm1001imAlmClientDwLasFail_Type()
)
pm1001imAlmClientDwLasFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientDwLasFail.setStatus("current")
_Pm1001imAlmClientUpLos_Type = EkiOnOff
_Pm1001imAlmClientUpLos_Object = MibScalar
pm1001imAlmClientUpLos = _Pm1001imAlmClientUpLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 168, 4),
    _Pm1001imAlmClientUpLos_Type()
)
pm1001imAlmClientUpLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientUpLos.setStatus("current")
_Pm1001imAlmclientMapperDeAlm_ObjectIdentity = ObjectIdentity
pm1001imAlmclientMapperDeAlm = _Pm1001imAlmclientMapperDeAlm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 169)
)
_Pm1001imAlmClientUpAccOos_Type = EkiOnOff
_Pm1001imAlmClientUpAccOos_Object = MibScalar
pm1001imAlmClientUpAccOos = _Pm1001imAlmClientUpAccOos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 169, 1),
    _Pm1001imAlmClientUpAccOos_Type()
)
pm1001imAlmClientUpAccOos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientUpAccOos.setStatus("current")
_Pm1001imAlmClientUpBufferOvl_Type = EkiOnOff
_Pm1001imAlmClientUpBufferOvl_Object = MibScalar
pm1001imAlmClientUpBufferOvl = _Pm1001imAlmClientUpBufferOvl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 169, 10),
    _Pm1001imAlmClientUpBufferOvl_Type()
)
pm1001imAlmClientUpBufferOvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientUpBufferOvl.setStatus("current")
_Pm1001imAlmClientDwCsfDet_Type = EkiOnOff
_Pm1001imAlmClientDwCsfDet_Object = MibScalar
pm1001imAlmClientDwCsfDet = _Pm1001imAlmClientDwCsfDet_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 169, 11),
    _Pm1001imAlmClientDwCsfDet_Type()
)
pm1001imAlmClientDwCsfDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientDwCsfDet.setStatus("current")
_Pm1001imAlmClientDwBufferOvl_Type = EkiOnOff
_Pm1001imAlmClientDwBufferOvl_Object = MibScalar
pm1001imAlmClientDwBufferOvl = _Pm1001imAlmClientDwBufferOvl_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 169, 14),
    _Pm1001imAlmClientDwBufferOvl_Type()
)
pm1001imAlmClientDwBufferOvl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientDwBufferOvl.setStatus("current")
_Pm1001imAlmclientXfpAlarms2_ObjectIdentity = ObjectIdentity
pm1001imAlmclientXfpAlarms2 = _Pm1001imAlmclientXfpAlarms2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211)
)
_Pm1001imAlmClientModNr_Type = EkiOnOff
_Pm1001imAlmClientModNr_Object = MibScalar
pm1001imAlmClientModNr = _Pm1001imAlmClientModNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 2),
    _Pm1001imAlmClientModNr_Type()
)
pm1001imAlmClientModNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientModNr.setStatus("current")
_Pm1001imAlmClientRxCdrNotLocked1_Type = EkiOnOff
_Pm1001imAlmClientRxCdrNotLocked1_Object = MibScalar
pm1001imAlmClientRxCdrNotLocked1 = _Pm1001imAlmClientRxCdrNotLocked1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 3),
    _Pm1001imAlmClientRxCdrNotLocked1_Type()
)
pm1001imAlmClientRxCdrNotLocked1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRxCdrNotLocked1.setStatus("current")
_Pm1001imAlmClientRxNr_Type = EkiOnOff
_Pm1001imAlmClientRxNr_Object = MibScalar
pm1001imAlmClientRxNr = _Pm1001imAlmClientRxNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 5),
    _Pm1001imAlmClientRxNr_Type()
)
pm1001imAlmClientRxNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientRxNr.setStatus("current")
_Pm1001imAlmClientTxCdrNotLocked1_Type = EkiOnOff
_Pm1001imAlmClientTxCdrNotLocked1_Object = MibScalar
pm1001imAlmClientTxCdrNotLocked1 = _Pm1001imAlmClientTxCdrNotLocked1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 6),
    _Pm1001imAlmClientTxCdrNotLocked1_Type()
)
pm1001imAlmClientTxCdrNotLocked1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxCdrNotLocked1.setStatus("current")
_Pm1001imAlmClientTxFault_Type = EkiOnOff
_Pm1001imAlmClientTxFault_Object = MibScalar
pm1001imAlmClientTxFault = _Pm1001imAlmClientTxFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 7),
    _Pm1001imAlmClientTxFault_Type()
)
pm1001imAlmClientTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxFault.setStatus("current")
_Pm1001imAlmClientTxNr_Type = EkiOnOff
_Pm1001imAlmClientTxNr_Object = MibScalar
pm1001imAlmClientTxNr = _Pm1001imAlmClientTxNr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 8),
    _Pm1001imAlmClientTxNr_Type()
)
pm1001imAlmClientTxNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTxNr.setStatus("current")
_Pm1001imAlmClientWavelengthUnlocked_Type = EkiOnOff
_Pm1001imAlmClientWavelengthUnlocked_Object = MibScalar
pm1001imAlmClientWavelengthUnlocked = _Pm1001imAlmClientWavelengthUnlocked_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 14),
    _Pm1001imAlmClientWavelengthUnlocked_Type()
)
pm1001imAlmClientWavelengthUnlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientWavelengthUnlocked.setStatus("current")
_Pm1001imAlmClientTecFault_Type = EkiOnOff
_Pm1001imAlmClientTecFault_Object = MibScalar
pm1001imAlmClientTecFault = _Pm1001imAlmClientTecFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 15),
    _Pm1001imAlmClientTecFault_Type()
)
pm1001imAlmClientTecFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientTecFault.setStatus("current")
_Pm1001imAlmClientApdSupplyFault_Type = EkiOnOff
_Pm1001imAlmClientApdSupplyFault_Object = MibScalar
pm1001imAlmClientApdSupplyFault = _Pm1001imAlmClientApdSupplyFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 2, 3, 211, 16),
    _Pm1001imAlmClientApdSupplyFault_Type()
)
pm1001imAlmClientApdSupplyFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmClientApdSupplyFault.setStatus("current")
_Pm1001imAlmLine_ObjectIdentity = ObjectIdentity
pm1001imAlmLine = _Pm1001imAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3)
)
_Pm1001imAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1001imAlmLineNurg = _Pm1001imAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1)
)
_Pm1001imAlmlineSfpWarnDdmTable_Object = MibTable
pm1001imAlmlineSfpWarnDdmTable = _Pm1001imAlmlineSfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48)
)
if mibBuilder.loadTexts:
    pm1001imAlmlineSfpWarnDdmTable.setStatus("current")
_Pm1001imAlmlineSfpWarnDdmEntry_Object = MibTableRow
pm1001imAlmlineSfpWarnDdmEntry = _Pm1001imAlmlineSfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1)
)
pm1001imAlmlineSfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imAlmlineSfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1001imAlmlineSfpWarnDdmEntry.setStatus("current")


class _Pm1001imAlmlineSfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1001imAlmlineSfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imAlmlineSfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1001imAlmlineSfpWarnDdmIndex_Object = MibTableColumn
pm1001imAlmlineSfpWarnDdmIndex = _Pm1001imAlmlineSfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 1),
    _Pm1001imAlmlineSfpWarnDdmIndex_Type()
)
pm1001imAlmlineSfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineSfpWarnDdmIndex.setStatus("current")
_Pm1001imAlmLineTxPwrLowWngPortn_Type = EkiOnOff
_Pm1001imAlmLineTxPwrLowWngPortn_Object = MibTableColumn
pm1001imAlmLineTxPwrLowWngPortn = _Pm1001imAlmLineTxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 2),
    _Pm1001imAlmLineTxPwrLowWngPortn_Type()
)
pm1001imAlmLineTxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxPwrLowWngPortn.setStatus("current")
_Pm1001imAlmLineTxPwrHighWngPortn_Type = EkiOnOff
_Pm1001imAlmLineTxPwrHighWngPortn_Object = MibTableColumn
pm1001imAlmLineTxPwrHighWngPortn = _Pm1001imAlmLineTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 3),
    _Pm1001imAlmLineTxPwrHighWngPortn_Type()
)
pm1001imAlmLineTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxPwrHighWngPortn.setStatus("current")
_Pm1001imAlmLineTxBiasLowWngPortn_Type = EkiOnOff
_Pm1001imAlmLineTxBiasLowWngPortn_Object = MibTableColumn
pm1001imAlmLineTxBiasLowWngPortn = _Pm1001imAlmLineTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 4),
    _Pm1001imAlmLineTxBiasLowWngPortn_Type()
)
pm1001imAlmLineTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxBiasLowWngPortn.setStatus("current")
_Pm1001imAlmLineTxBiasHighWngPortn_Type = EkiOnOff
_Pm1001imAlmLineTxBiasHighWngPortn_Object = MibTableColumn
pm1001imAlmLineTxBiasHighWngPortn = _Pm1001imAlmLineTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 5),
    _Pm1001imAlmLineTxBiasHighWngPortn_Type()
)
pm1001imAlmLineTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxBiasHighWngPortn.setStatus("current")
_Pm1001imAlmLineVccLowWngPortn_Type = EkiOnOff
_Pm1001imAlmLineVccLowWngPortn_Object = MibTableColumn
pm1001imAlmLineVccLowWngPortn = _Pm1001imAlmLineVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 6),
    _Pm1001imAlmLineVccLowWngPortn_Type()
)
pm1001imAlmLineVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineVccLowWngPortn.setStatus("current")
_Pm1001imAlmLineVccHighWngPortn_Type = EkiOnOff
_Pm1001imAlmLineVccHighWngPortn_Object = MibTableColumn
pm1001imAlmLineVccHighWngPortn = _Pm1001imAlmLineVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 7),
    _Pm1001imAlmLineVccHighWngPortn_Type()
)
pm1001imAlmLineVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineVccHighWngPortn.setStatus("current")
_Pm1001imAlmLineTempLowWngPortn_Type = EkiOnOff
_Pm1001imAlmLineTempLowWngPortn_Object = MibTableColumn
pm1001imAlmLineTempLowWngPortn = _Pm1001imAlmLineTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 8),
    _Pm1001imAlmLineTempLowWngPortn_Type()
)
pm1001imAlmLineTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTempLowWngPortn.setStatus("current")
_Pm1001imAlmLineTempHighWngPortn_Type = EkiOnOff
_Pm1001imAlmLineTempHighWngPortn_Object = MibTableColumn
pm1001imAlmLineTempHighWngPortn = _Pm1001imAlmLineTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 9),
    _Pm1001imAlmLineTempHighWngPortn_Type()
)
pm1001imAlmLineTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTempHighWngPortn.setStatus("current")
_Pm1001imAlmLineRxPwrLowWngPortn_Type = EkiOnOff
_Pm1001imAlmLineRxPwrLowWngPortn_Object = MibTableColumn
pm1001imAlmLineRxPwrLowWngPortn = _Pm1001imAlmLineRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 16),
    _Pm1001imAlmLineRxPwrLowWngPortn_Type()
)
pm1001imAlmLineRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineRxPwrLowWngPortn.setStatus("current")
_Pm1001imAlmLineRxPwrHighWngPortn_Type = EkiOnOff
_Pm1001imAlmLineRxPwrHighWngPortn_Object = MibTableColumn
pm1001imAlmLineRxPwrHighWngPortn = _Pm1001imAlmLineRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 48, 1, 17),
    _Pm1001imAlmLineRxPwrHighWngPortn_Type()
)
pm1001imAlmLineRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineRxPwrHighWngPortn.setStatus("current")


class _Pm1001imAlmlineDownS1Line1_Type(Unsigned32):
    """Custom type pm1001imAlmlineDownS1Line1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001imAlmlineDownS1Line1_Type.__name__ = "Unsigned32"
_Pm1001imAlmlineDownS1Line1_Object = MibScalar
pm1001imAlmlineDownS1Line1 = _Pm1001imAlmlineDownS1Line1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 130),
    _Pm1001imAlmlineDownS1Line1_Type()
)
pm1001imAlmlineDownS1Line1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineDownS1Line1.setStatus("current")


class _Pm1001imAlmlineDownK1Line1_Type(Unsigned32):
    """Custom type pm1001imAlmlineDownK1Line1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001imAlmlineDownK1Line1_Type.__name__ = "Unsigned32"
_Pm1001imAlmlineDownK1Line1_Object = MibScalar
pm1001imAlmlineDownK1Line1 = _Pm1001imAlmlineDownK1Line1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 131),
    _Pm1001imAlmlineDownK1Line1_Type()
)
pm1001imAlmlineDownK1Line1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineDownK1Line1.setStatus("current")


class _Pm1001imAlmlineDownK2Line1_Type(Unsigned32):
    """Custom type pm1001imAlmlineDownK2Line1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001imAlmlineDownK2Line1_Type.__name__ = "Unsigned32"
_Pm1001imAlmlineDownK2Line1_Object = MibScalar
pm1001imAlmlineDownK2Line1 = _Pm1001imAlmlineDownK2Line1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 1, 132),
    _Pm1001imAlmlineDownK2Line1_Type()
)
pm1001imAlmlineDownK2Line1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineDownK2Line1.setStatus("current")
_Pm1001imAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1001imAlmLineUrg = _Pm1001imAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2)
)
_Pm1001imAlmlineSfpAlmDdmTable_Object = MibTable
pm1001imAlmlineSfpAlmDdmTable = _Pm1001imAlmlineSfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1001imAlmlineSfpAlmDdmTable.setStatus("current")
_Pm1001imAlmlineSfpAlmDdmEntry_Object = MibTableRow
pm1001imAlmlineSfpAlmDdmEntry = _Pm1001imAlmlineSfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1)
)
pm1001imAlmlineSfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imAlmlineSfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1001imAlmlineSfpAlmDdmEntry.setStatus("current")


class _Pm1001imAlmlineSfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1001imAlmlineSfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imAlmlineSfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1001imAlmlineSfpAlmDdmIndex_Object = MibTableColumn
pm1001imAlmlineSfpAlmDdmIndex = _Pm1001imAlmlineSfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 1),
    _Pm1001imAlmlineSfpAlmDdmIndex_Type()
)
pm1001imAlmlineSfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineSfpAlmDdmIndex.setStatus("current")
_Pm1001imAlmLineTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineTxPwrLowAlaPortn_Object = MibTableColumn
pm1001imAlmLineTxPwrLowAlaPortn = _Pm1001imAlmLineTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 2),
    _Pm1001imAlmLineTxPwrLowAlaPortn_Type()
)
pm1001imAlmLineTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxPwrLowAlaPortn.setStatus("current")
_Pm1001imAlmLineTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineTxPwrHighAlaPortn_Object = MibTableColumn
pm1001imAlmLineTxPwrHighAlaPortn = _Pm1001imAlmLineTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 3),
    _Pm1001imAlmLineTxPwrHighAlaPortn_Type()
)
pm1001imAlmLineTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxPwrHighAlaPortn.setStatus("current")
_Pm1001imAlmLineTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineTxBiasLowAlaPortn_Object = MibTableColumn
pm1001imAlmLineTxBiasLowAlaPortn = _Pm1001imAlmLineTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 4),
    _Pm1001imAlmLineTxBiasLowAlaPortn_Type()
)
pm1001imAlmLineTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxBiasLowAlaPortn.setStatus("current")
_Pm1001imAlmLineTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineTxBiasHighAlaPortn_Object = MibTableColumn
pm1001imAlmLineTxBiasHighAlaPortn = _Pm1001imAlmLineTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 5),
    _Pm1001imAlmLineTxBiasHighAlaPortn_Type()
)
pm1001imAlmLineTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTxBiasHighAlaPortn.setStatus("current")
_Pm1001imAlmLineVccLowAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineVccLowAlaPortn_Object = MibTableColumn
pm1001imAlmLineVccLowAlaPortn = _Pm1001imAlmLineVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 6),
    _Pm1001imAlmLineVccLowAlaPortn_Type()
)
pm1001imAlmLineVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineVccLowAlaPortn.setStatus("current")
_Pm1001imAlmLineVccHighAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineVccHighAlaPortn_Object = MibTableColumn
pm1001imAlmLineVccHighAlaPortn = _Pm1001imAlmLineVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 7),
    _Pm1001imAlmLineVccHighAlaPortn_Type()
)
pm1001imAlmLineVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineVccHighAlaPortn.setStatus("current")
_Pm1001imAlmLineTempLowAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineTempLowAlaPortn_Object = MibTableColumn
pm1001imAlmLineTempLowAlaPortn = _Pm1001imAlmLineTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 8),
    _Pm1001imAlmLineTempLowAlaPortn_Type()
)
pm1001imAlmLineTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTempLowAlaPortn.setStatus("current")
_Pm1001imAlmLineTempHighAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineTempHighAlaPortn_Object = MibTableColumn
pm1001imAlmLineTempHighAlaPortn = _Pm1001imAlmLineTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 9),
    _Pm1001imAlmLineTempHighAlaPortn_Type()
)
pm1001imAlmLineTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineTempHighAlaPortn.setStatus("current")
_Pm1001imAlmLineRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineRxPwrLowAlaPortn_Object = MibTableColumn
pm1001imAlmLineRxPwrLowAlaPortn = _Pm1001imAlmLineRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 16),
    _Pm1001imAlmLineRxPwrLowAlaPortn_Type()
)
pm1001imAlmLineRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineRxPwrLowAlaPortn.setStatus("current")
_Pm1001imAlmLineRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1001imAlmLineRxPwrHighAlaPortn_Object = MibTableColumn
pm1001imAlmLineRxPwrHighAlaPortn = _Pm1001imAlmLineRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 32, 1, 17),
    _Pm1001imAlmLineRxPwrHighAlaPortn_Type()
)
pm1001imAlmLineRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineRxPwrHighAlaPortn.setStatus("current")
_Pm1001imAlmlineDfrmBer1_ObjectIdentity = ObjectIdentity
pm1001imAlmlineDfrmBer1 = _Pm1001imAlmlineDfrmBer1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 129)
)
_Pm1001imAlmLineSignalDegrade1_Type = EkiOnOff
_Pm1001imAlmLineSignalDegrade1_Object = MibScalar
pm1001imAlmLineSignalDegrade1 = _Pm1001imAlmLineSignalDegrade1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 129, 1),
    _Pm1001imAlmLineSignalDegrade1_Type()
)
pm1001imAlmLineSignalDegrade1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineSignalDegrade1.setStatus("current")
_Pm1001imAlmLineSignalFail1_Type = EkiOnOff
_Pm1001imAlmLineSignalFail1_Object = MibScalar
pm1001imAlmLineSignalFail1 = _Pm1001imAlmLineSignalFail1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 129, 2),
    _Pm1001imAlmLineSignalFail1_Type()
)
pm1001imAlmLineSignalFail1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineSignalFail1.setStatus("current")
_Pm1001imAlmLineDegrade1_Type = EkiOnOff
_Pm1001imAlmLineDegrade1_Object = MibScalar
pm1001imAlmLineDegrade1 = _Pm1001imAlmLineDegrade1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 2, 129, 5),
    _Pm1001imAlmLineDegrade1_Type()
)
pm1001imAlmLineDegrade1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineDegrade1.setStatus("current")
_Pm1001imAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1001imAlmLineCrit = _Pm1001imAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3)
)
_Pm1001imAlmsynthAlmLineTable_Object = MibTable
pm1001imAlmsynthAlmLineTable = _Pm1001imAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8)
)
if mibBuilder.loadTexts:
    pm1001imAlmsynthAlmLineTable.setStatus("current")
_Pm1001imAlmsynthAlmLineEntry_Object = MibTableRow
pm1001imAlmsynthAlmLineEntry = _Pm1001imAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1)
)
pm1001imAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1001imAlmsynthAlmLineEntry.setStatus("current")


class _Pm1001imAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1001imAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1001imAlmsynthAlmLineIndex_Object = MibTableColumn
pm1001imAlmsynthAlmLineIndex = _Pm1001imAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 1),
    _Pm1001imAlmsynthAlmLineIndex_Type()
)
pm1001imAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmsynthAlmLineIndex.setStatus("current")
_Pm1001imAlmLineSfpAbsentPortn_Type = EkiOnOff
_Pm1001imAlmLineSfpAbsentPortn_Object = MibTableColumn
pm1001imAlmLineSfpAbsentPortn = _Pm1001imAlmLineSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 2),
    _Pm1001imAlmLineSfpAbsentPortn_Type()
)
pm1001imAlmLineSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineSfpAbsentPortn.setStatus("current")
_Pm1001imAlmLineDdmAbsentPortn_Type = EkiOnOff
_Pm1001imAlmLineDdmAbsentPortn_Object = MibTableColumn
pm1001imAlmLineDdmAbsentPortn = _Pm1001imAlmLineDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 3),
    _Pm1001imAlmLineDdmAbsentPortn_Type()
)
pm1001imAlmLineDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineDdmAbsentPortn.setStatus("current")
_Pm1001imAlmLineHwFailPortn_Type = EkiOnOff
_Pm1001imAlmLineHwFailPortn_Object = MibTableColumn
pm1001imAlmLineHwFailPortn = _Pm1001imAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 5),
    _Pm1001imAlmLineHwFailPortn_Type()
)
pm1001imAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineHwFailPortn.setStatus("current")
_Pm1001imAlmLineUpLsdPortn_Type = EkiOnOff
_Pm1001imAlmLineUpLsdPortn_Object = MibTableColumn
pm1001imAlmLineUpLsdPortn = _Pm1001imAlmLineUpLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 6),
    _Pm1001imAlmLineUpLsdPortn_Type()
)
pm1001imAlmLineUpLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineUpLsdPortn.setStatus("current")
_Pm1001imAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1001imAlmLineLocalOosPortn_Object = MibTableColumn
pm1001imAlmLineLocalOosPortn = _Pm1001imAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 7),
    _Pm1001imAlmLineLocalOosPortn_Type()
)
pm1001imAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineLocalOosPortn.setStatus("current")
_Pm1001imAlmLineUpRdiInsPortn_Type = EkiOnOff
_Pm1001imAlmLineUpRdiInsPortn_Object = MibTableColumn
pm1001imAlmLineUpRdiInsPortn = _Pm1001imAlmLineUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 9),
    _Pm1001imAlmLineUpRdiInsPortn_Type()
)
pm1001imAlmLineUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineUpRdiInsPortn.setStatus("current")
_Pm1001imAlmLineSfpDdmWarningPortn_Type = EkiOnOff
_Pm1001imAlmLineSfpDdmWarningPortn_Object = MibTableColumn
pm1001imAlmLineSfpDdmWarningPortn = _Pm1001imAlmLineSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 10),
    _Pm1001imAlmLineSfpDdmWarningPortn_Type()
)
pm1001imAlmLineSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineSfpDdmWarningPortn.setStatus("current")
_Pm1001imAlmLineSfpDdmAlmPortn_Type = EkiOnOff
_Pm1001imAlmLineSfpDdmAlmPortn_Object = MibTableColumn
pm1001imAlmLineSfpDdmAlmPortn = _Pm1001imAlmLineSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 11),
    _Pm1001imAlmLineSfpDdmAlmPortn_Type()
)
pm1001imAlmLineSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineSfpDdmAlmPortn.setStatus("current")
_Pm1001imAlmLineFailPortn_Type = EkiOnOff
_Pm1001imAlmLineFailPortn_Object = MibTableColumn
pm1001imAlmLineFailPortn = _Pm1001imAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 8, 1, 13),
    _Pm1001imAlmLineFailPortn_Type()
)
pm1001imAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineFailPortn.setStatus("current")
_Pm1001imAlmlineAlmTable_Object = MibTable
pm1001imAlmlineAlmTable = _Pm1001imAlmlineAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 16)
)
if mibBuilder.loadTexts:
    pm1001imAlmlineAlmTable.setStatus("current")
_Pm1001imAlmlineAlmEntry_Object = MibTableRow
pm1001imAlmlineAlmEntry = _Pm1001imAlmlineAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 16, 1)
)
pm1001imAlmlineAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imAlmlineAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1001imAlmlineAlmEntry.setStatus("current")


class _Pm1001imAlmlineAlmIndex_Type(Integer32):
    """Custom type pm1001imAlmlineAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imAlmlineAlmIndex_Type.__name__ = "Integer32"
_Pm1001imAlmlineAlmIndex_Object = MibTableColumn
pm1001imAlmlineAlmIndex = _Pm1001imAlmlineAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 16, 1, 1),
    _Pm1001imAlmlineAlmIndex_Type()
)
pm1001imAlmlineAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineAlmIndex.setStatus("current")
_Pm1001imAlmLineDwLasFailPortn_Type = EkiOnOff
_Pm1001imAlmLineDwLasFailPortn_Object = MibTableColumn
pm1001imAlmLineDwLasFailPortn = _Pm1001imAlmLineDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 16, 1, 2),
    _Pm1001imAlmLineDwLasFailPortn_Type()
)
pm1001imAlmLineDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineDwLasFailPortn.setStatus("current")
_Pm1001imAlmLineUpLosPortn_Type = EkiOnOff
_Pm1001imAlmLineUpLosPortn_Object = MibTableColumn
pm1001imAlmLineUpLosPortn = _Pm1001imAlmLineUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 16, 1, 5),
    _Pm1001imAlmLineUpLosPortn_Type()
)
pm1001imAlmLineUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineUpLosPortn.setStatus("current")
_Pm1001imAlmlineMapperDeAlmTable_Object = MibTable
pm1001imAlmlineMapperDeAlmTable = _Pm1001imAlmlineMapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 72)
)
if mibBuilder.loadTexts:
    pm1001imAlmlineMapperDeAlmTable.setStatus("current")
_Pm1001imAlmlineMapperDeAlmEntry_Object = MibTableRow
pm1001imAlmlineMapperDeAlmEntry = _Pm1001imAlmlineMapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 72, 1)
)
pm1001imAlmlineMapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imAlmlineMapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1001imAlmlineMapperDeAlmEntry.setStatus("current")


class _Pm1001imAlmlineMapperDeAlmIndex_Type(Integer32):
    """Custom type pm1001imAlmlineMapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imAlmlineMapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1001imAlmlineMapperDeAlmIndex_Object = MibTableColumn
pm1001imAlmlineMapperDeAlmIndex = _Pm1001imAlmlineMapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 72, 1, 1),
    _Pm1001imAlmlineMapperDeAlmIndex_Type()
)
pm1001imAlmlineMapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmlineMapperDeAlmIndex.setStatus("current")
_Pm1001imAlmLineDwLofPortn_Type = EkiOnOff
_Pm1001imAlmLineDwLofPortn_Object = MibTableColumn
pm1001imAlmLineDwLofPortn = _Pm1001imAlmLineDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 72, 1, 2),
    _Pm1001imAlmLineDwLofPortn_Type()
)
pm1001imAlmLineDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineDwLofPortn.setStatus("current")
_Pm1001imAlmLineB1IndicPortn_Type = EkiOnOff
_Pm1001imAlmLineB1IndicPortn_Object = MibTableColumn
pm1001imAlmLineB1IndicPortn = _Pm1001imAlmLineB1IndicPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 72, 1, 7),
    _Pm1001imAlmLineB1IndicPortn_Type()
)
pm1001imAlmLineB1IndicPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineB1IndicPortn.setStatus("current")
_Pm1001imAlmLineLoopFifoFailPortn_Type = EkiOnOff
_Pm1001imAlmLineLoopFifoFailPortn_Object = MibTableColumn
pm1001imAlmLineLoopFifoFailPortn = _Pm1001imAlmLineLoopFifoFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 72, 1, 16),
    _Pm1001imAlmLineLoopFifoFailPortn_Type()
)
pm1001imAlmLineLoopFifoFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmLineLoopFifoFailPortn.setStatus("current")
_Pm1001imAlmlineDfrmAlm1_ObjectIdentity = ObjectIdentity
pm1001imAlmlineDfrmAlm1 = _Pm1001imAlmlineDfrmAlm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 128)
)
_Pm1001imAlmDwAisDet1_Type = EkiOnOff
_Pm1001imAlmDwAisDet1_Object = MibScalar
pm1001imAlmDwAisDet1 = _Pm1001imAlmDwAisDet1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 128, 1),
    _Pm1001imAlmDwAisDet1_Type()
)
pm1001imAlmDwAisDet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDwAisDet1.setStatus("current")
_Pm1001imAlmDwRdiDet1_Type = EkiOnOff
_Pm1001imAlmDwRdiDet1_Object = MibScalar
pm1001imAlmDwRdiDet1 = _Pm1001imAlmDwRdiDet1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 128, 2),
    _Pm1001imAlmDwRdiDet1_Type()
)
pm1001imAlmDwRdiDet1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDwRdiDet1.setStatus("current")
_Pm1001imAlmDwOof1_Type = EkiOnOff
_Pm1001imAlmDwOof1_Object = MibScalar
pm1001imAlmDwOof1 = _Pm1001imAlmDwOof1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 128, 3),
    _Pm1001imAlmDwOof1_Type()
)
pm1001imAlmDwOof1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDwOof1.setStatus("current")
_Pm1001imAlmDwLof1_Type = EkiOnOff
_Pm1001imAlmDwLof1_Object = MibScalar
pm1001imAlmDwLof1 = _Pm1001imAlmDwLof1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 128, 4),
    _Pm1001imAlmDwLof1_Type()
)
pm1001imAlmDwLof1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDwLof1.setStatus("current")
_Pm1001imAlmlineSyncAlarms1_ObjectIdentity = ObjectIdentity
pm1001imAlmlineSyncAlarms1 = _Pm1001imAlmlineSyncAlarms1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 133)
)
_Pm1001imAlmDwLockerr_Type = EkiOnOff
_Pm1001imAlmDwLockerr_Object = MibScalar
pm1001imAlmDwLockerr = _Pm1001imAlmDwLockerr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 133, 12),
    _Pm1001imAlmDwLockerr_Type()
)
pm1001imAlmDwLockerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDwLockerr.setStatus("current")
_Pm1001imAlmUpLockerr_Type = EkiOnOff
_Pm1001imAlmUpLockerr_Object = MibScalar
pm1001imAlmUpLockerr = _Pm1001imAlmUpLockerr_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 133, 13),
    _Pm1001imAlmUpLockerr_Type()
)
pm1001imAlmUpLockerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmUpLockerr.setStatus("current")
_Pm1001imAlmDwLos_Type = EkiOnOff
_Pm1001imAlmDwLos_Object = MibScalar
pm1001imAlmDwLos = _Pm1001imAlmDwLos_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 2, 3, 3, 133, 16),
    _Pm1001imAlmDwLos_Type()
)
pm1001imAlmDwLos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imAlmDwLos.setStatus("current")
_Pm1001immeasures_ObjectIdentity = ObjectIdentity
pm1001immeasures = _Pm1001immeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3)
)
_Pm1001imMesrOther_ObjectIdentity = ObjectIdentity
pm1001imMesrOther = _Pm1001imMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 1)
)
_Pm1001imMesrsynth0_Type = EkiMeasureType
_Pm1001imMesrsynth0_Object = MibScalar
pm1001imMesrsynth0 = _Pm1001imMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 1, 0),
    _Pm1001imMesrsynth0_Type()
)
pm1001imMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrsynth0.setStatus("deprecated")
_Pm1001imMesrsynth1_Type = EkiMeasureType
_Pm1001imMesrsynth1_Object = MibScalar
pm1001imMesrsynth1 = _Pm1001imMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 1, 1),
    _Pm1001imMesrsynth1_Type()
)
pm1001imMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrsynth1.setStatus("deprecated")
_Pm1001imMesrClient_ObjectIdentity = ObjectIdentity
pm1001imMesrClient = _Pm1001imMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2)
)


class _Pm1001imMesrclientModTempMeas_Type(Unsigned32):
    """Custom type pm1001imMesrclientModTempMeas based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientModTempMeas_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientModTempMeas_Object = MibScalar
pm1001imMesrclientModTempMeas = _Pm1001imMesrclientModTempMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 208),
    _Pm1001imMesrclientModTempMeas_Type()
)
pm1001imMesrclientModTempMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientModTempMeas.setStatus("current")


class _Pm1001imMesrclientReserved_Type(Unsigned32):
    """Custom type pm1001imMesrclientReserved based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientReserved_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientReserved_Object = MibScalar
pm1001imMesrclientReserved = _Pm1001imMesrclientReserved_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 209),
    _Pm1001imMesrclientReserved_Type()
)
pm1001imMesrclientReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientReserved.setStatus("deprecated")


class _Pm1001imMesrclientBiasCurrentMeas_Type(Unsigned32):
    """Custom type pm1001imMesrclientBiasCurrentMeas based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientBiasCurrentMeas_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientBiasCurrentMeas_Object = MibScalar
pm1001imMesrclientBiasCurrentMeas = _Pm1001imMesrclientBiasCurrentMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 210),
    _Pm1001imMesrclientBiasCurrentMeas_Type()
)
pm1001imMesrclientBiasCurrentMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientBiasCurrentMeas.setStatus("current")


class _Pm1001imMesrclientTxPowerMeas_Type(Unsigned32):
    """Custom type pm1001imMesrclientTxPowerMeas based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientTxPowerMeas_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientTxPowerMeas_Object = MibScalar
pm1001imMesrclientTxPowerMeas = _Pm1001imMesrclientTxPowerMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 211),
    _Pm1001imMesrclientTxPowerMeas_Type()
)
pm1001imMesrclientTxPowerMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientTxPowerMeas.setStatus("current")


class _Pm1001imMesrclientRxPowerMeas_Type(Unsigned32):
    """Custom type pm1001imMesrclientRxPowerMeas based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientRxPowerMeas_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientRxPowerMeas_Object = MibScalar
pm1001imMesrclientRxPowerMeas = _Pm1001imMesrclientRxPowerMeas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 212),
    _Pm1001imMesrclientRxPowerMeas_Type()
)
pm1001imMesrclientRxPowerMeas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientRxPowerMeas.setStatus("current")


class _Pm1001imMesrclientAux1Meas_Type(Unsigned32):
    """Custom type pm1001imMesrclientAux1Meas based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientAux1Meas_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientAux1Meas_Object = MibScalar
pm1001imMesrclientAux1Meas = _Pm1001imMesrclientAux1Meas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 213),
    _Pm1001imMesrclientAux1Meas_Type()
)
pm1001imMesrclientAux1Meas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientAux1Meas.setStatus("deprecated")


class _Pm1001imMesrclientAux2Meas_Type(Unsigned32):
    """Custom type pm1001imMesrclientAux2Meas based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrclientAux2Meas_Type.__name__ = "Unsigned32"
_Pm1001imMesrclientAux2Meas_Object = MibScalar
pm1001imMesrclientAux2Meas = _Pm1001imMesrclientAux2Meas_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 2, 214),
    _Pm1001imMesrclientAux2Meas_Type()
)
pm1001imMesrclientAux2Meas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrclientAux2Meas.setStatus("deprecated")
_Pm1001imMesrLine_ObjectIdentity = ObjectIdentity
pm1001imMesrLine = _Pm1001imMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3)
)
_Pm1001imMesrlineTempMeasTable_Object = MibTable
pm1001imMesrlineTempMeasTable = _Pm1001imMesrlineTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 16)
)
if mibBuilder.loadTexts:
    pm1001imMesrlineTempMeasTable.setStatus("current")
_Pm1001imMesrlineTempMeasEntry_Object = MibTableRow
pm1001imMesrlineTempMeasEntry = _Pm1001imMesrlineTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 16, 1)
)
pm1001imMesrlineTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMesrlineTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMesrlineTempMeasEntry.setStatus("current")


class _Pm1001imMesrlineTempMeasIndex_Type(Integer32):
    """Custom type pm1001imMesrlineTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMesrlineTempMeasIndex_Type.__name__ = "Integer32"
_Pm1001imMesrlineTempMeasIndex_Object = MibTableColumn
pm1001imMesrlineTempMeasIndex = _Pm1001imMesrlineTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 16, 1, 1),
    _Pm1001imMesrlineTempMeasIndex_Type()
)
pm1001imMesrlineTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineTempMeasIndex.setStatus("current")


class _Pm1001imMesrlineTempMeasPortn_Type(Integer32):
    """Custom type pm1001imMesrlineTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrlineTempMeasPortn_Type.__name__ = "Integer32"
_Pm1001imMesrlineTempMeasPortn_Object = MibTableColumn
pm1001imMesrlineTempMeasPortn = _Pm1001imMesrlineTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 16, 1, 2),
    _Pm1001imMesrlineTempMeasPortn_Type()
)
pm1001imMesrlineTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineTempMeasPortn.setStatus("current")
_Pm1001imMesrlineVoltMeasTable_Object = MibTable
pm1001imMesrlineVoltMeasTable = _Pm1001imMesrlineVoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 24)
)
if mibBuilder.loadTexts:
    pm1001imMesrlineVoltMeasTable.setStatus("current")
_Pm1001imMesrlineVoltMeasEntry_Object = MibTableRow
pm1001imMesrlineVoltMeasEntry = _Pm1001imMesrlineVoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 24, 1)
)
pm1001imMesrlineVoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMesrlineVoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMesrlineVoltMeasEntry.setStatus("current")


class _Pm1001imMesrlineVoltMeasIndex_Type(Integer32):
    """Custom type pm1001imMesrlineVoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMesrlineVoltMeasIndex_Type.__name__ = "Integer32"
_Pm1001imMesrlineVoltMeasIndex_Object = MibTableColumn
pm1001imMesrlineVoltMeasIndex = _Pm1001imMesrlineVoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 24, 1, 1),
    _Pm1001imMesrlineVoltMeasIndex_Type()
)
pm1001imMesrlineVoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineVoltMeasIndex.setStatus("current")


class _Pm1001imMesrlineVoltMeasPortn_Type(Integer32):
    """Custom type pm1001imMesrlineVoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrlineVoltMeasPortn_Type.__name__ = "Integer32"
_Pm1001imMesrlineVoltMeasPortn_Object = MibTableColumn
pm1001imMesrlineVoltMeasPortn = _Pm1001imMesrlineVoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 24, 1, 2),
    _Pm1001imMesrlineVoltMeasPortn_Type()
)
pm1001imMesrlineVoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineVoltMeasPortn.setStatus("current")
_Pm1001imMesrlineBiasMeasTable_Object = MibTable
pm1001imMesrlineBiasMeasTable = _Pm1001imMesrlineBiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 32)
)
if mibBuilder.loadTexts:
    pm1001imMesrlineBiasMeasTable.setStatus("current")
_Pm1001imMesrlineBiasMeasEntry_Object = MibTableRow
pm1001imMesrlineBiasMeasEntry = _Pm1001imMesrlineBiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 32, 1)
)
pm1001imMesrlineBiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMesrlineBiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMesrlineBiasMeasEntry.setStatus("current")


class _Pm1001imMesrlineBiasMeasIndex_Type(Integer32):
    """Custom type pm1001imMesrlineBiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMesrlineBiasMeasIndex_Type.__name__ = "Integer32"
_Pm1001imMesrlineBiasMeasIndex_Object = MibTableColumn
pm1001imMesrlineBiasMeasIndex = _Pm1001imMesrlineBiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 32, 1, 1),
    _Pm1001imMesrlineBiasMeasIndex_Type()
)
pm1001imMesrlineBiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineBiasMeasIndex.setStatus("current")


class _Pm1001imMesrlineBiasMeasPortn_Type(Integer32):
    """Custom type pm1001imMesrlineBiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrlineBiasMeasPortn_Type.__name__ = "Integer32"
_Pm1001imMesrlineBiasMeasPortn_Object = MibTableColumn
pm1001imMesrlineBiasMeasPortn = _Pm1001imMesrlineBiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 32, 1, 2),
    _Pm1001imMesrlineBiasMeasPortn_Type()
)
pm1001imMesrlineBiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineBiasMeasPortn.setStatus("current")
_Pm1001imMesrlineTxpwrMeasTable_Object = MibTable
pm1001imMesrlineTxpwrMeasTable = _Pm1001imMesrlineTxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pm1001imMesrlineTxpwrMeasTable.setStatus("current")
_Pm1001imMesrlineTxpwrMeasEntry_Object = MibTableRow
pm1001imMesrlineTxpwrMeasEntry = _Pm1001imMesrlineTxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 40, 1)
)
pm1001imMesrlineTxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMesrlineTxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMesrlineTxpwrMeasEntry.setStatus("current")


class _Pm1001imMesrlineTxpwrMeasIndex_Type(Integer32):
    """Custom type pm1001imMesrlineTxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMesrlineTxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1001imMesrlineTxpwrMeasIndex_Object = MibTableColumn
pm1001imMesrlineTxpwrMeasIndex = _Pm1001imMesrlineTxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 40, 1, 1),
    _Pm1001imMesrlineTxpwrMeasIndex_Type()
)
pm1001imMesrlineTxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineTxpwrMeasIndex.setStatus("current")


class _Pm1001imMesrlineTxpwrMeasPortn_Type(Integer32):
    """Custom type pm1001imMesrlineTxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrlineTxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1001imMesrlineTxpwrMeasPortn_Object = MibTableColumn
pm1001imMesrlineTxpwrMeasPortn = _Pm1001imMesrlineTxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 40, 1, 2),
    _Pm1001imMesrlineTxpwrMeasPortn_Type()
)
pm1001imMesrlineTxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineTxpwrMeasPortn.setStatus("current")
_Pm1001imMesrlineRxpwrMeasTable_Object = MibTable
pm1001imMesrlineRxpwrMeasTable = _Pm1001imMesrlineRxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 48)
)
if mibBuilder.loadTexts:
    pm1001imMesrlineRxpwrMeasTable.setStatus("current")
_Pm1001imMesrlineRxpwrMeasEntry_Object = MibTableRow
pm1001imMesrlineRxpwrMeasEntry = _Pm1001imMesrlineRxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 48, 1)
)
pm1001imMesrlineRxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMesrlineRxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMesrlineRxpwrMeasEntry.setStatus("current")


class _Pm1001imMesrlineRxpwrMeasIndex_Type(Integer32):
    """Custom type pm1001imMesrlineRxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMesrlineRxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1001imMesrlineRxpwrMeasIndex_Object = MibTableColumn
pm1001imMesrlineRxpwrMeasIndex = _Pm1001imMesrlineRxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 48, 1, 1),
    _Pm1001imMesrlineRxpwrMeasIndex_Type()
)
pm1001imMesrlineRxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineRxpwrMeasIndex.setStatus("current")


class _Pm1001imMesrlineRxpwrMeasPortn_Type(Integer32):
    """Custom type pm1001imMesrlineRxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1001imMesrlineRxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1001imMesrlineRxpwrMeasPortn_Object = MibTableColumn
pm1001imMesrlineRxpwrMeasPortn = _Pm1001imMesrlineRxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 3, 3, 48, 1, 2),
    _Pm1001imMesrlineRxpwrMeasPortn_Type()
)
pm1001imMesrlineRxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMesrlineRxpwrMeasPortn.setStatus("current")
_Pm1001imcounters_ObjectIdentity = ObjectIdentity
pm1001imcounters = _Pm1001imcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4)
)
_Pm1001imCntOther_ObjectIdentity = ObjectIdentity
pm1001imCntOther = _Pm1001imCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 1)
)
_Pm1001imCntClient_ObjectIdentity = ObjectIdentity
pm1001imCntClient = _Pm1001imCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2)
)
_Pm1001imCntclientUpErrCntTable_Object = MibTable
pm1001imCntclientUpErrCntTable = _Pm1001imCntclientUpErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 210)
)
if mibBuilder.loadTexts:
    pm1001imCntclientUpErrCntTable.setStatus("current")
_Pm1001imCntclientUpErrCntEntry_Object = MibTableRow
pm1001imCntclientUpErrCntEntry = _Pm1001imCntclientUpErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 210, 1)
)
pm1001imCntclientUpErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCntclientUpErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCntclientUpErrCntEntry.setStatus("current")


class _Pm1001imCntclientUpErrCntIndex_Type(Integer32):
    """Custom type pm1001imCntclientUpErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCntclientUpErrCntIndex_Type.__name__ = "Integer32"
_Pm1001imCntclientUpErrCntIndex_Object = MibTableColumn
pm1001imCntclientUpErrCntIndex = _Pm1001imCntclientUpErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 210, 1, 1),
    _Pm1001imCntclientUpErrCntIndex_Type()
)
pm1001imCntclientUpErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpErrCntIndex.setStatus("current")
_Pm1001imCntclientUpErrCntValuePortn_Type = Counter32
_Pm1001imCntclientUpErrCntValuePortn_Object = MibTableColumn
pm1001imCntclientUpErrCntValuePortn = _Pm1001imCntclientUpErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 210, 1, 2),
    _Pm1001imCntclientUpErrCntValuePortn_Type()
)
pm1001imCntclientUpErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpErrCntValuePortn.setStatus("current")
_Pm1001imCntclientUpErrCntErrorPortn_Type = EkiOnOff
_Pm1001imCntclientUpErrCntErrorPortn_Object = MibTableColumn
pm1001imCntclientUpErrCntErrorPortn = _Pm1001imCntclientUpErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 210, 1, 3),
    _Pm1001imCntclientUpErrCntErrorPortn_Type()
)
pm1001imCntclientUpErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpErrCntErrorPortn.setStatus("current")
_Pm1001imCntclientUpErrCntOverloadPortn_Type = EkiOnOff
_Pm1001imCntclientUpErrCntOverloadPortn_Object = MibTableColumn
pm1001imCntclientUpErrCntOverloadPortn = _Pm1001imCntclientUpErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 210, 1, 4),
    _Pm1001imCntclientUpErrCntOverloadPortn_Type()
)
pm1001imCntclientUpErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpErrCntOverloadPortn.setStatus("current")
_Pm1001imCntclientUpTimCntTable_Object = MibTable
pm1001imCntclientUpTimCntTable = _Pm1001imCntclientUpTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 211)
)
if mibBuilder.loadTexts:
    pm1001imCntclientUpTimCntTable.setStatus("current")
_Pm1001imCntclientUpTimCntEntry_Object = MibTableRow
pm1001imCntclientUpTimCntEntry = _Pm1001imCntclientUpTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 211, 1)
)
pm1001imCntclientUpTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCntclientUpTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCntclientUpTimCntEntry.setStatus("current")


class _Pm1001imCntclientUpTimCntIndex_Type(Integer32):
    """Custom type pm1001imCntclientUpTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCntclientUpTimCntIndex_Type.__name__ = "Integer32"
_Pm1001imCntclientUpTimCntIndex_Object = MibTableColumn
pm1001imCntclientUpTimCntIndex = _Pm1001imCntclientUpTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 211, 1, 1),
    _Pm1001imCntclientUpTimCntIndex_Type()
)
pm1001imCntclientUpTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpTimCntIndex.setStatus("current")
_Pm1001imCntclientUpTimCntValuePortn_Type = Counter32
_Pm1001imCntclientUpTimCntValuePortn_Object = MibTableColumn
pm1001imCntclientUpTimCntValuePortn = _Pm1001imCntclientUpTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 211, 1, 2),
    _Pm1001imCntclientUpTimCntValuePortn_Type()
)
pm1001imCntclientUpTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpTimCntValuePortn.setStatus("current")
_Pm1001imCntclientUpTimCntErrorPortn_Type = EkiOnOff
_Pm1001imCntclientUpTimCntErrorPortn_Object = MibTableColumn
pm1001imCntclientUpTimCntErrorPortn = _Pm1001imCntclientUpTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 211, 1, 3),
    _Pm1001imCntclientUpTimCntErrorPortn_Type()
)
pm1001imCntclientUpTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpTimCntErrorPortn.setStatus("current")
_Pm1001imCntclientUpTimCntOverloadPortn_Type = EkiOnOff
_Pm1001imCntclientUpTimCntOverloadPortn_Object = MibTableColumn
pm1001imCntclientUpTimCntOverloadPortn = _Pm1001imCntclientUpTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 211, 1, 4),
    _Pm1001imCntclientUpTimCntOverloadPortn_Type()
)
pm1001imCntclientUpTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientUpTimCntOverloadPortn.setStatus("current")
_Pm1001imCntclientDwErrCntTable_Object = MibTable
pm1001imCntclientDwErrCntTable = _Pm1001imCntclientDwErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 213)
)
if mibBuilder.loadTexts:
    pm1001imCntclientDwErrCntTable.setStatus("current")
_Pm1001imCntclientDwErrCntEntry_Object = MibTableRow
pm1001imCntclientDwErrCntEntry = _Pm1001imCntclientDwErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 213, 1)
)
pm1001imCntclientDwErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCntclientDwErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCntclientDwErrCntEntry.setStatus("current")


class _Pm1001imCntclientDwErrCntIndex_Type(Integer32):
    """Custom type pm1001imCntclientDwErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCntclientDwErrCntIndex_Type.__name__ = "Integer32"
_Pm1001imCntclientDwErrCntIndex_Object = MibTableColumn
pm1001imCntclientDwErrCntIndex = _Pm1001imCntclientDwErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 213, 1, 1),
    _Pm1001imCntclientDwErrCntIndex_Type()
)
pm1001imCntclientDwErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwErrCntIndex.setStatus("current")
_Pm1001imCntclientDwErrCntValuePortn_Type = Counter32
_Pm1001imCntclientDwErrCntValuePortn_Object = MibTableColumn
pm1001imCntclientDwErrCntValuePortn = _Pm1001imCntclientDwErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 213, 1, 2),
    _Pm1001imCntclientDwErrCntValuePortn_Type()
)
pm1001imCntclientDwErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwErrCntValuePortn.setStatus("current")
_Pm1001imCntclientDwErrCntErrorPortn_Type = EkiOnOff
_Pm1001imCntclientDwErrCntErrorPortn_Object = MibTableColumn
pm1001imCntclientDwErrCntErrorPortn = _Pm1001imCntclientDwErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 213, 1, 3),
    _Pm1001imCntclientDwErrCntErrorPortn_Type()
)
pm1001imCntclientDwErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwErrCntErrorPortn.setStatus("current")
_Pm1001imCntclientDwErrCntOverloadPortn_Type = EkiOnOff
_Pm1001imCntclientDwErrCntOverloadPortn_Object = MibTableColumn
pm1001imCntclientDwErrCntOverloadPortn = _Pm1001imCntclientDwErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 213, 1, 4),
    _Pm1001imCntclientDwErrCntOverloadPortn_Type()
)
pm1001imCntclientDwErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwErrCntOverloadPortn.setStatus("current")
_Pm1001imCntclientDwTimCntTable_Object = MibTable
pm1001imCntclientDwTimCntTable = _Pm1001imCntclientDwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 214)
)
if mibBuilder.loadTexts:
    pm1001imCntclientDwTimCntTable.setStatus("current")
_Pm1001imCntclientDwTimCntEntry_Object = MibTableRow
pm1001imCntclientDwTimCntEntry = _Pm1001imCntclientDwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 214, 1)
)
pm1001imCntclientDwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCntclientDwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCntclientDwTimCntEntry.setStatus("current")


class _Pm1001imCntclientDwTimCntIndex_Type(Integer32):
    """Custom type pm1001imCntclientDwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCntclientDwTimCntIndex_Type.__name__ = "Integer32"
_Pm1001imCntclientDwTimCntIndex_Object = MibTableColumn
pm1001imCntclientDwTimCntIndex = _Pm1001imCntclientDwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 214, 1, 1),
    _Pm1001imCntclientDwTimCntIndex_Type()
)
pm1001imCntclientDwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwTimCntIndex.setStatus("current")
_Pm1001imCntclientDwTimCntValuePortn_Type = Counter32
_Pm1001imCntclientDwTimCntValuePortn_Object = MibTableColumn
pm1001imCntclientDwTimCntValuePortn = _Pm1001imCntclientDwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 214, 1, 2),
    _Pm1001imCntclientDwTimCntValuePortn_Type()
)
pm1001imCntclientDwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwTimCntValuePortn.setStatus("current")
_Pm1001imCntclientDwTimCntErrorPortn_Type = EkiOnOff
_Pm1001imCntclientDwTimCntErrorPortn_Object = MibTableColumn
pm1001imCntclientDwTimCntErrorPortn = _Pm1001imCntclientDwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 214, 1, 3),
    _Pm1001imCntclientDwTimCntErrorPortn_Type()
)
pm1001imCntclientDwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwTimCntErrorPortn.setStatus("current")
_Pm1001imCntclientDwTimCntOverloadPortn_Type = EkiOnOff
_Pm1001imCntclientDwTimCntOverloadPortn_Object = MibTableColumn
pm1001imCntclientDwTimCntOverloadPortn = _Pm1001imCntclientDwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 2, 214, 1, 4),
    _Pm1001imCntclientDwTimCntOverloadPortn_Type()
)
pm1001imCntclientDwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntclientDwTimCntOverloadPortn.setStatus("current")
_Pm1001imCntLine_ObjectIdentity = ObjectIdentity
pm1001imCntLine = _Pm1001imCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3)
)
_Pm1001imCntdfrmB1ErrCntTable_Object = MibTable
pm1001imCntdfrmB1ErrCntTable = _Pm1001imCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1001imCntdfrmB1ErrCntTable.setStatus("current")
_Pm1001imCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1001imCntdfrmB1ErrCntEntry = _Pm1001imCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 152, 1)
)
pm1001imCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1001imCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1001imCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1001imCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1001imCntdfrmB1ErrCntIndex = _Pm1001imCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 152, 1, 1),
    _Pm1001imCntdfrmB1ErrCntIndex_Type()
)
pm1001imCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1001imCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1001imCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1001imCntdfrmB1ErrCntValuePortn = _Pm1001imCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 152, 1, 2),
    _Pm1001imCntdfrmB1ErrCntValuePortn_Type()
)
pm1001imCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1001imCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1001imCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1001imCntdfrmB1ErrCntErrorPortn = _Pm1001imCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 152, 1, 3),
    _Pm1001imCntdfrmB1ErrCntErrorPortn_Type()
)
pm1001imCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1001imCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1001imCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1001imCntdfrmB1ErrCntOverloadPortn = _Pm1001imCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 152, 1, 4),
    _Pm1001imCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1001imCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1001imCntdfrmTimCntTable_Object = MibTable
pm1001imCntdfrmTimCntTable = _Pm1001imCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1001imCntdfrmTimCntTable.setStatus("current")
_Pm1001imCntdfrmTimCntEntry_Object = MibTableRow
pm1001imCntdfrmTimCntEntry = _Pm1001imCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 153, 1)
)
pm1001imCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCntdfrmTimCntEntry.setStatus("current")


class _Pm1001imCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1001imCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1001imCntdfrmTimCntIndex_Object = MibTableColumn
pm1001imCntdfrmTimCntIndex = _Pm1001imCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 153, 1, 1),
    _Pm1001imCntdfrmTimCntIndex_Type()
)
pm1001imCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmTimCntIndex.setStatus("current")
_Pm1001imCntdfrmTimCntValuePortn_Type = Counter32
_Pm1001imCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1001imCntdfrmTimCntValuePortn = _Pm1001imCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 153, 1, 2),
    _Pm1001imCntdfrmTimCntValuePortn_Type()
)
pm1001imCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmTimCntValuePortn.setStatus("current")
_Pm1001imCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1001imCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1001imCntdfrmTimCntErrorPortn = _Pm1001imCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 153, 1, 3),
    _Pm1001imCntdfrmTimCntErrorPortn_Type()
)
pm1001imCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1001imCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1001imCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1001imCntdfrmTimCntOverloadPortn = _Pm1001imCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 3, 153, 1, 4),
    _Pm1001imCntdfrmTimCntOverloadPortn_Type()
)
pm1001imCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1001imCntCountersReset_Type = EkiOnOff
_Pm1001imCntCountersReset_Object = MibScalar
pm1001imCntCountersReset = _Pm1001imCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 259),
    _Pm1001imCntCountersReset_Type()
)
pm1001imCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCntCountersReset.setStatus("current")
_Pm1001imCntCountersStop_Type = EkiOnOff
_Pm1001imCntCountersStop_Object = MibScalar
pm1001imCntCountersStop = _Pm1001imCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 4, 260),
    _Pm1001imCntCountersStop_Type()
)
pm1001imCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCntCountersStop.setStatus("current")
_Pm1001imcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1001imcontrolsWrite = _Pm1001imcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6)
)
_Pm1001imCtrlOther_ObjectIdentity = ObjectIdentity
pm1001imCtrlOther = _Pm1001imCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1)
)
_Pm1001imCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1001imCtrlconfMgnt1 = _Pm1001imCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 1)
)
_Pm1001imCtrlConf1Load1_Type = EkiOnOff
_Pm1001imCtrlConf1Load1_Object = MibScalar
pm1001imCtrlConf1Load1 = _Pm1001imCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 1, 1),
    _Pm1001imCtrlConf1Load1_Type()
)
pm1001imCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlConf1Load1.setStatus("current")
_Pm1001imCtrlConf2Load1_Type = EkiOnOff
_Pm1001imCtrlConf2Load1_Object = MibScalar
pm1001imCtrlConf2Load1 = _Pm1001imCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 1, 2),
    _Pm1001imCtrlConf2Load1_Type()
)
pm1001imCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlConf2Load1.setStatus("current")
_Pm1001imCtrlConf2Flash1_Type = EkiOnOff
_Pm1001imCtrlConf2Flash1_Object = MibScalar
pm1001imCtrlConf2Flash1 = _Pm1001imCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 1, 10),
    _Pm1001imCtrlConf2Flash1_Type()
)
pm1001imCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlConf2Flash1.setStatus("current")
_Pm1001imCtrlConf2Clear1_Type = EkiOnOff
_Pm1001imCtrlConf2Clear1_Object = MibScalar
pm1001imCtrlConf2Clear1 = _Pm1001imCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 1, 14),
    _Pm1001imCtrlConf2Clear1_Type()
)
pm1001imCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlConf2Clear1.setStatus("current")
_Pm1001imCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1001imCtrlsynth4 = _Pm1001imCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 4)
)
_Pm1001imCtrlCorrelatOn_Type = EkiOnOff
_Pm1001imCtrlCorrelatOn_Object = MibScalar
pm1001imCtrlCorrelatOn = _Pm1001imCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 4, 1),
    _Pm1001imCtrlCorrelatOn_Type()
)
pm1001imCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlCorrelatOn.setStatus("current")
_Pm1001imCtrlCorrelatOff_Type = EkiOnOff
_Pm1001imCtrlCorrelatOff_Object = MibScalar
pm1001imCtrlCorrelatOff = _Pm1001imCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 4, 2),
    _Pm1001imCtrlCorrelatOff_Type()
)
pm1001imCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlCorrelatOff.setStatus("current")
_Pm1001imCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1001imCtrlswMgnt = _Pm1001imCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 5)
)
_Pm1001imCtrlColdReset_Type = EkiOnOff
_Pm1001imCtrlColdReset_Object = MibScalar
pm1001imCtrlColdReset = _Pm1001imCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 5, 2),
    _Pm1001imCtrlColdReset_Type()
)
pm1001imCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlColdReset.setStatus("current")
_Pm1001imCtrlWarmReset_Type = EkiOnOff
_Pm1001imCtrlWarmReset_Object = MibScalar
pm1001imCtrlWarmReset = _Pm1001imCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 5, 3),
    _Pm1001imCtrlWarmReset_Type()
)
pm1001imCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlWarmReset.setStatus("current")
_Pm1001imCtrlLoadSwBank1_Type = EkiOnOff
_Pm1001imCtrlLoadSwBank1_Object = MibScalar
pm1001imCtrlLoadSwBank1 = _Pm1001imCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 5, 5),
    _Pm1001imCtrlLoadSwBank1_Type()
)
pm1001imCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLoadSwBank1.setStatus("current")
_Pm1001imCtrlLoadSwBank2_Type = EkiOnOff
_Pm1001imCtrlLoadSwBank2_Object = MibScalar
pm1001imCtrlLoadSwBank2 = _Pm1001imCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 5, 6),
    _Pm1001imCtrlLoadSwBank2_Type()
)
pm1001imCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLoadSwBank2.setStatus("current")
_Pm1001imCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1001imCtrlgwMgnt = _Pm1001imCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 6)
)
_Pm1001imCtrlCurrentGwReset_Type = EkiOnOff
_Pm1001imCtrlCurrentGwReset_Object = MibScalar
pm1001imCtrlCurrentGwReset = _Pm1001imCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 6, 1),
    _Pm1001imCtrlCurrentGwReset_Type()
)
pm1001imCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlCurrentGwReset.setStatus("current")
_Pm1001imCtrlLoadGwBank1_Type = EkiOnOff
_Pm1001imCtrlLoadGwBank1_Object = MibScalar
pm1001imCtrlLoadGwBank1 = _Pm1001imCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 6, 5),
    _Pm1001imCtrlLoadGwBank1_Type()
)
pm1001imCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLoadGwBank1.setStatus("current")
_Pm1001imCtrlLoadGwBank2_Type = EkiOnOff
_Pm1001imCtrlLoadGwBank2_Object = MibScalar
pm1001imCtrlLoadGwBank2 = _Pm1001imCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 6, 6),
    _Pm1001imCtrlLoadGwBank2_Type()
)
pm1001imCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLoadGwBank2.setStatus("current")
_Pm1001imCtrlLoadGwBank3_Type = EkiOnOff
_Pm1001imCtrlLoadGwBank3_Object = MibScalar
pm1001imCtrlLoadGwBank3 = _Pm1001imCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 6, 7),
    _Pm1001imCtrlLoadGwBank3_Type()
)
pm1001imCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLoadGwBank3.setStatus("current")
_Pm1001imCtrlLoadGwBank4_Type = EkiOnOff
_Pm1001imCtrlLoadGwBank4_Object = MibScalar
pm1001imCtrlLoadGwBank4 = _Pm1001imCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 6, 8),
    _Pm1001imCtrlLoadGwBank4_Type()
)
pm1001imCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLoadGwBank4.setStatus("current")
_Pm1001imCtrlledTest_ObjectIdentity = ObjectIdentity
pm1001imCtrlledTest = _Pm1001imCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 192)
)
_Pm1001imCtrlGreenLed_Type = EkiOnOff
_Pm1001imCtrlGreenLed_Object = MibScalar
pm1001imCtrlGreenLed = _Pm1001imCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 192, 1),
    _Pm1001imCtrlGreenLed_Type()
)
pm1001imCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlGreenLed.setStatus("current")
_Pm1001imCtrlRedLed_Type = EkiOnOff
_Pm1001imCtrlRedLed_Object = MibScalar
pm1001imCtrlRedLed = _Pm1001imCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 192, 2),
    _Pm1001imCtrlRedLed_Type()
)
pm1001imCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlRedLed.setStatus("current")
_Pm1001imCtrlLedOff_Type = EkiOnOff
_Pm1001imCtrlLedOff_Object = MibScalar
pm1001imCtrlLedOff = _Pm1001imCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 192, 3),
    _Pm1001imCtrlLedOff_Type()
)
pm1001imCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLedOff.setStatus("current")
_Pm1001imCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1001imCtrlmoduleOosMode = _Pm1001imCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 193)
)
_Pm1001imCtrlModuleOosMode_Type = EkiOnOff
_Pm1001imCtrlModuleOosMode_Object = MibScalar
pm1001imCtrlModuleOosMode = _Pm1001imCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 193, 1),
    _Pm1001imCtrlModuleOosMode_Type()
)
pm1001imCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlModuleOosMode.setStatus("current")
_Pm1001imCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1001imCtrlmaintenanceMode = _Pm1001imCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 197)
)
_Pm1001imCtrlMaintenanceMode_Type = EkiOnOff
_Pm1001imCtrlMaintenanceMode_Object = MibScalar
pm1001imCtrlMaintenanceMode = _Pm1001imCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 197, 1),
    _Pm1001imCtrlMaintenanceMode_Type()
)
pm1001imCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlMaintenanceMode.setStatus("current")
_Pm1001imCtrldccEnable_ObjectIdentity = ObjectIdentity
pm1001imCtrldccEnable = _Pm1001imCtrldccEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 198)
)
_Pm1001imCtrlDccEnable_Type = EkiOnOff
_Pm1001imCtrlDccEnable_Object = MibScalar
pm1001imCtrlDccEnable = _Pm1001imCtrlDccEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 1, 198, 1),
    _Pm1001imCtrlDccEnable_Type()
)
pm1001imCtrlDccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlDccEnable.setStatus("current")
_Pm1001imCtrlClient_ObjectIdentity = ObjectIdentity
pm1001imCtrlClient = _Pm1001imCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2)
)
_Pm1001imCtrlaccessLoop_ObjectIdentity = ObjectIdentity
pm1001imCtrlaccessLoop = _Pm1001imCtrlaccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 16)
)
_Pm1001imCtrlaccessLoopClient_Type = EkiOnOff
_Pm1001imCtrlaccessLoopClient_Object = MibScalar
pm1001imCtrlaccessLoopClient = _Pm1001imCtrlaccessLoopClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 16, 1),
    _Pm1001imCtrlaccessLoopClient_Type()
)
pm1001imCtrlaccessLoopClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlaccessLoopClient.setStatus("current")
_Pm1001imCtrlportOosMode_ObjectIdentity = ObjectIdentity
pm1001imCtrlportOosMode = _Pm1001imCtrlportOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 18)
)
_Pm1001imCtrlportOosModeClient_Type = EkiOnOff
_Pm1001imCtrlportOosModeClient_Object = MibScalar
pm1001imCtrlportOosModeClient = _Pm1001imCtrlportOosModeClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 18, 1),
    _Pm1001imCtrlportOosModeClient_Type()
)
pm1001imCtrlportOosModeClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlportOosModeClient.setStatus("current")
_Pm1001imCtrlclientXfpOff_ObjectIdentity = ObjectIdentity
pm1001imCtrlclientXfpOff = _Pm1001imCtrlclientXfpOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 20)
)
_Pm1001imCtrlclientXfpOffClient_Type = EkiOnOff
_Pm1001imCtrlclientXfpOffClient_Object = MibScalar
pm1001imCtrlclientXfpOffClient = _Pm1001imCtrlclientXfpOffClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 20, 1),
    _Pm1001imCtrlclientXfpOffClient_Type()
)
pm1001imCtrlclientXfpOffClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlclientXfpOffClient.setStatus("current")
_Pm1001imCtrlcsfUpIns_ObjectIdentity = ObjectIdentity
pm1001imCtrlcsfUpIns = _Pm1001imCtrlcsfUpIns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 21)
)
_Pm1001imCtrlcsfUpInsClient_Type = EkiOnOff
_Pm1001imCtrlcsfUpInsClient_Object = MibScalar
pm1001imCtrlcsfUpInsClient = _Pm1001imCtrlcsfUpInsClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 21, 1),
    _Pm1001imCtrlcsfUpInsClient_Type()
)
pm1001imCtrlcsfUpInsClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlcsfUpInsClient.setStatus("current")
_Pm1001imCtrlcaisDwIns_ObjectIdentity = ObjectIdentity
pm1001imCtrlcaisDwIns = _Pm1001imCtrlcaisDwIns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 22)
)
_Pm1001imCtrlcaisDwInsClient_Type = EkiOnOff
_Pm1001imCtrlcaisDwInsClient_Object = MibScalar
pm1001imCtrlcaisDwInsClient = _Pm1001imCtrlcaisDwInsClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 2, 22, 1),
    _Pm1001imCtrlcaisDwInsClient_Type()
)
pm1001imCtrlcaisDwInsClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlcaisDwInsClient.setStatus("current")
_Pm1001imCtrlLine_ObjectIdentity = ObjectIdentity
pm1001imCtrlLine = _Pm1001imCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3)
)
_Pm1001imCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1001imCtrllineLoop = _Pm1001imCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 66)
)
_Pm1001imCtrlLineLoop_Type = EkiOnOff
_Pm1001imCtrlLineLoop_Object = MibScalar
pm1001imCtrlLineLoop = _Pm1001imCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 66, 1),
    _Pm1001imCtrlLineLoop_Type()
)
pm1001imCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlLineLoop.setStatus("deprecated")
_Pm1001imCtrllineMsAis_ObjectIdentity = ObjectIdentity
pm1001imCtrllineMsAis = _Pm1001imCtrllineMsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 67)
)
_Pm1001imCtrlMsAis_Type = EkiOnOff
_Pm1001imCtrlMsAis_Object = MibScalar
pm1001imCtrlMsAis = _Pm1001imCtrlMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 67, 1),
    _Pm1001imCtrlMsAis_Type()
)
pm1001imCtrlMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrlMsAis.setStatus("current")


class _Pm1001imCtrllineUpS1_Type(Unsigned32):
    """Custom type pm1001imCtrllineUpS1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001imCtrllineUpS1_Type.__name__ = "Unsigned32"
_Pm1001imCtrllineUpS1_Object = MibScalar
pm1001imCtrllineUpS1 = _Pm1001imCtrllineUpS1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 70),
    _Pm1001imCtrllineUpS1_Type()
)
pm1001imCtrllineUpS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrllineUpS1.setStatus("current")


class _Pm1001imCtrllineUpK1_Type(Unsigned32):
    """Custom type pm1001imCtrllineUpK1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001imCtrllineUpK1_Type.__name__ = "Unsigned32"
_Pm1001imCtrllineUpK1_Object = MibScalar
pm1001imCtrllineUpK1 = _Pm1001imCtrllineUpK1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 71),
    _Pm1001imCtrllineUpK1_Type()
)
pm1001imCtrllineUpK1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrllineUpK1.setStatus("current")


class _Pm1001imCtrllineUpK2_Type(Unsigned32):
    """Custom type pm1001imCtrllineUpK2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1001imCtrllineUpK2_Type.__name__ = "Unsigned32"
_Pm1001imCtrllineUpK2_Object = MibScalar
pm1001imCtrllineUpK2 = _Pm1001imCtrllineUpK2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 72),
    _Pm1001imCtrllineUpK2_Type()
)
pm1001imCtrllineUpK2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrllineUpK2.setStatus("current")
_Pm1001imCtrllineOosMode_ObjectIdentity = ObjectIdentity
pm1001imCtrllineOosMode = _Pm1001imCtrllineOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 74)
)
_Pm1001imCtrllineOosModeAllLines_Type = EkiOnOff
_Pm1001imCtrllineOosModeAllLines_Object = MibScalar
pm1001imCtrllineOosModeAllLines = _Pm1001imCtrllineOosModeAllLines_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 74, 1),
    _Pm1001imCtrllineOosModeAllLines_Type()
)
pm1001imCtrllineOosModeAllLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrllineOosModeAllLines.setStatus("current")
_Pm1001imCtrllineBandwidth_Type = Pm1001imBandwidthMode
_Pm1001imCtrllineBandwidth_Object = MibScalar
pm1001imCtrllineBandwidth = _Pm1001imCtrllineBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 100),
    _Pm1001imCtrllineBandwidth_Type()
)
pm1001imCtrllineBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrllineBandwidth.setStatus("current")
_Pm1001imCtrllineOnoff_ObjectIdentity = ObjectIdentity
pm1001imCtrllineOnoff = _Pm1001imCtrllineOnoff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 208)
)
_Pm1001imCtrllineOnoffAllLines_Type = EkiOnOff
_Pm1001imCtrllineOnoffAllLines_Object = MibScalar
pm1001imCtrllineOnoffAllLines = _Pm1001imCtrllineOnoffAllLines_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 6, 3, 208, 1),
    _Pm1001imCtrllineOnoffAllLines_Type()
)
pm1001imCtrllineOnoffAllLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCtrllineOnoffAllLines.setStatus("current")
_Pm1001imri_ObjectIdentity = ObjectIdentity
pm1001imri = _Pm1001imri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7)
)
_Pm1001imriTable_ObjectIdentity = ObjectIdentity
pm1001imriTable = _Pm1001imriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 1)
)
_Pm1001imRinvLineTable_Object = MibTable
pm1001imRinvLineTable = _Pm1001imRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1001imRinvLineTable.setStatus("current")
_Pm1001imRinvLineEntry_Object = MibTableRow
pm1001imRinvLineEntry = _Pm1001imRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 1, 2, 1)
)
pm1001imRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1001imRinvLineEntry.setStatus("current")


class _Pm1001imRinvLineIndex_Type(Integer32):
    """Custom type pm1001imRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1001imRinvLineIndex_Type.__name__ = "Integer32"
_Pm1001imRinvLineIndex_Object = MibTableColumn
pm1001imRinvLineIndex = _Pm1001imRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 1, 2, 1, 1),
    _Pm1001imRinvLineIndex_Type()
)
pm1001imRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvLineIndex.setStatus("current")
_Pm1001imRinvSfpLine_Type = DisplayString
_Pm1001imRinvSfpLine_Object = MibTableColumn
pm1001imRinvSfpLine = _Pm1001imRinvSfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 1, 2, 1, 2),
    _Pm1001imRinvSfpLine_Type()
)
pm1001imRinvSfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvSfpLine.setStatus("current")
_Pm1001imRinvReloadInventory_Type = EkiOnOff
_Pm1001imRinvReloadInventory_Object = MibScalar
pm1001imRinvReloadInventory = _Pm1001imRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 2),
    _Pm1001imRinvReloadInventory_Type()
)
pm1001imRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imRinvReloadInventory.setStatus("current")
_Pm1001imRinvHwPlatform_Type = DisplayString
_Pm1001imRinvHwPlatform_Object = MibScalar
pm1001imRinvHwPlatform = _Pm1001imRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 3),
    _Pm1001imRinvHwPlatform_Type()
)
pm1001imRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvHwPlatform.setStatus("current")
_Pm1001imRinvModulePlatform_Type = DisplayString
_Pm1001imRinvModulePlatform_Object = MibScalar
pm1001imRinvModulePlatform = _Pm1001imRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 4),
    _Pm1001imRinvModulePlatform_Type()
)
pm1001imRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvModulePlatform.setStatus("current")
_Pm1001imRinvSwPlatform_Type = DisplayString
_Pm1001imRinvSwPlatform_Object = MibScalar
pm1001imRinvSwPlatform = _Pm1001imRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 5),
    _Pm1001imRinvSwPlatform_Type()
)
pm1001imRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvSwPlatform.setStatus("current")
_Pm1001imRinvGwPlatform_Type = DisplayString
_Pm1001imRinvGwPlatform_Object = MibScalar
pm1001imRinvGwPlatform = _Pm1001imRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 6),
    _Pm1001imRinvGwPlatform_Type()
)
pm1001imRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvGwPlatform.setStatus("current")
_Pm1001imRinvXfpClient_Type = DisplayString
_Pm1001imRinvXfpClient_Object = MibScalar
pm1001imRinvXfpClient = _Pm1001imRinvXfpClient_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 7, 7),
    _Pm1001imRinvXfpClient_Type()
)
pm1001imRinvXfpClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imRinvXfpClient.setStatus("current")
_Pm1001imdownload_ObjectIdentity = ObjectIdentity
pm1001imdownload = _Pm1001imdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8)
)
_Pm1001imDwlOther_ObjectIdentity = ObjectIdentity
pm1001imDwlOther = _Pm1001imDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1)
)
_Pm1001imDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1001imDwlrestartProcess = _Pm1001imDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 0)
)
_Pm1001imDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1001imDwlWarmRestartProcessed_Object = MibScalar
pm1001imDwlWarmRestartProcessed = _Pm1001imDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 0, 1),
    _Pm1001imDwlWarmRestartProcessed_Type()
)
pm1001imDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlWarmRestartProcessed.setStatus("current")
_Pm1001imDwlColdRestartProcessed_Type = EkiOnOff
_Pm1001imDwlColdRestartProcessed_Object = MibScalar
pm1001imDwlColdRestartProcessed = _Pm1001imDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 0, 2),
    _Pm1001imDwlColdRestartProcessed_Type()
)
pm1001imDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlColdRestartProcessed.setStatus("current")
_Pm1001imDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1001imDwlswBanksUsed = _Pm1001imDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 1)
)
_Pm1001imDwlSwBank1Used_Type = EkiOnOff
_Pm1001imDwlSwBank1Used_Object = MibScalar
pm1001imDwlSwBank1Used = _Pm1001imDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 1, 1),
    _Pm1001imDwlSwBank1Used_Type()
)
pm1001imDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlSwBank1Used.setStatus("current")
_Pm1001imDwlSwBank2Used_Type = EkiOnOff
_Pm1001imDwlSwBank2Used_Object = MibScalar
pm1001imDwlSwBank2Used = _Pm1001imDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 1, 2),
    _Pm1001imDwlSwBank2Used_Type()
)
pm1001imDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlSwBank2Used.setStatus("current")
_Pm1001imDwlSwBank1Notempty_Type = EkiOnOff
_Pm1001imDwlSwBank1Notempty_Object = MibScalar
pm1001imDwlSwBank1Notempty = _Pm1001imDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 1, 5),
    _Pm1001imDwlSwBank1Notempty_Type()
)
pm1001imDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlSwBank1Notempty.setStatus("current")
_Pm1001imDwlSwBank2Notempty_Type = EkiOnOff
_Pm1001imDwlSwBank2Notempty_Object = MibScalar
pm1001imDwlSwBank2Notempty = _Pm1001imDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 1, 6),
    _Pm1001imDwlSwBank2Notempty_Type()
)
pm1001imDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlSwBank2Notempty.setStatus("current")
_Pm1001imDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1001imDwlgwBanksUsed = _Pm1001imDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2)
)
_Pm1001imDwlGwBank1Used_Type = EkiOnOff
_Pm1001imDwlGwBank1Used_Object = MibScalar
pm1001imDwlGwBank1Used = _Pm1001imDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 1),
    _Pm1001imDwlGwBank1Used_Type()
)
pm1001imDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank1Used.setStatus("current")
_Pm1001imDwlGwBank2Used_Type = EkiOnOff
_Pm1001imDwlGwBank2Used_Object = MibScalar
pm1001imDwlGwBank2Used = _Pm1001imDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 2),
    _Pm1001imDwlGwBank2Used_Type()
)
pm1001imDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank2Used.setStatus("current")
_Pm1001imDwlGwBank3Used_Type = EkiOnOff
_Pm1001imDwlGwBank3Used_Object = MibScalar
pm1001imDwlGwBank3Used = _Pm1001imDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 3),
    _Pm1001imDwlGwBank3Used_Type()
)
pm1001imDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank3Used.setStatus("current")
_Pm1001imDwlGwBank4Used_Type = EkiOnOff
_Pm1001imDwlGwBank4Used_Object = MibScalar
pm1001imDwlGwBank4Used = _Pm1001imDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 4),
    _Pm1001imDwlGwBank4Used_Type()
)
pm1001imDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank4Used.setStatus("current")
_Pm1001imDwlGwBank1Notempty_Type = EkiOnOff
_Pm1001imDwlGwBank1Notempty_Object = MibScalar
pm1001imDwlGwBank1Notempty = _Pm1001imDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 5),
    _Pm1001imDwlGwBank1Notempty_Type()
)
pm1001imDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank1Notempty.setStatus("current")
_Pm1001imDwlGwBank2Notempty_Type = EkiOnOff
_Pm1001imDwlGwBank2Notempty_Object = MibScalar
pm1001imDwlGwBank2Notempty = _Pm1001imDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 6),
    _Pm1001imDwlGwBank2Notempty_Type()
)
pm1001imDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank2Notempty.setStatus("current")
_Pm1001imDwlGwBank3Notempty_Type = EkiOnOff
_Pm1001imDwlGwBank3Notempty_Object = MibScalar
pm1001imDwlGwBank3Notempty = _Pm1001imDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 7),
    _Pm1001imDwlGwBank3Notempty_Type()
)
pm1001imDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank3Notempty.setStatus("current")
_Pm1001imDwlGwBank4Notempty_Type = EkiOnOff
_Pm1001imDwlGwBank4Notempty_Object = MibScalar
pm1001imDwlGwBank4Notempty = _Pm1001imDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 1, 2, 8),
    _Pm1001imDwlGwBank4Notempty_Type()
)
pm1001imDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imDwlGwBank4Notempty.setStatus("current")
_Pm1001imDwlClient_ObjectIdentity = ObjectIdentity
pm1001imDwlClient = _Pm1001imDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 2)
)
_Pm1001imDwlLine_ObjectIdentity = ObjectIdentity
pm1001imDwlLine = _Pm1001imDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 8, 3)
)
_Pm1001imrmon_ObjectIdentity = ObjectIdentity
pm1001imrmon = _Pm1001imrmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9)
)
_Pm1001imRmonOther_ObjectIdentity = ObjectIdentity
pm1001imRmonOther = _Pm1001imRmonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 1)
)
_Pm1001imMonCountersReset_Type = EkiOnOff
_Pm1001imMonCountersReset_Object = MibScalar
pm1001imMonCountersReset = _Pm1001imMonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 1, 359),
    _Pm1001imMonCountersReset_Type()
)
pm1001imMonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imMonCountersReset.setStatus("current")
_Pm1001imMonCountersStop_Type = EkiOnOff
_Pm1001imMonCountersStop_Object = MibScalar
pm1001imMonCountersStop = _Pm1001imMonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 1, 360),
    _Pm1001imMonCountersStop_Type()
)
pm1001imMonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imMonCountersStop.setStatus("current")
_Pm1001imRmonClient_ObjectIdentity = ObjectIdentity
pm1001imRmonClient = _Pm1001imRmonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2)
)
_Pm1001imMonupRmonByteCntTable_Object = MibTable
pm1001imMonupRmonByteCntTable = _Pm1001imMonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 16)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntTable.setStatus("current")
_Pm1001imMonupRmonByteCntEntry_Object = MibTableRow
pm1001imMonupRmonByteCntEntry = _Pm1001imMonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 16, 1)
)
pm1001imMonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntEntry.setStatus("current")


class _Pm1001imMonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonByteCntIndex_Object = MibTableColumn
pm1001imMonupRmonByteCntIndex = _Pm1001imMonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 16, 1, 1),
    _Pm1001imMonupRmonByteCntIndex_Type()
)
pm1001imMonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntIndex.setStatus("current")
_Pm1001imMonupRmonByteCntValuePortn_Type = Counter64
_Pm1001imMonupRmonByteCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonByteCntValuePortn = _Pm1001imMonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 16, 1, 2),
    _Pm1001imMonupRmonByteCntValuePortn_Type()
)
pm1001imMonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntValuePortn.setStatus("current")
_Pm1001imMonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonByteCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonByteCntErrorPortn = _Pm1001imMonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 16, 1, 3),
    _Pm1001imMonupRmonByteCntErrorPortn_Type()
)
pm1001imMonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonByteCntOverloadPortn = _Pm1001imMonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 16, 1, 4),
    _Pm1001imMonupRmonByteCntOverloadPortn_Type()
)
pm1001imMonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntTable_Object = MibTable
pm1001imMonupRmonCrcErrorCntTable = _Pm1001imMonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 24)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntTable.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntEntry_Object = MibTableRow
pm1001imMonupRmonCrcErrorCntEntry = _Pm1001imMonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 24, 1)
)
pm1001imMonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm1001imMonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntIndex = _Pm1001imMonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 24, 1, 1),
    _Pm1001imMonupRmonCrcErrorCntIndex_Type()
)
pm1001imMonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntIndex.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1001imMonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntValuePortn = _Pm1001imMonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 24, 1, 2),
    _Pm1001imMonupRmonCrcErrorCntValuePortn_Type()
)
pm1001imMonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntErrorPortn = _Pm1001imMonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 24, 1, 3),
    _Pm1001imMonupRmonCrcErrorCntErrorPortn_Type()
)
pm1001imMonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntOverloadPortn = _Pm1001imMonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 24, 1, 4),
    _Pm1001imMonupRmonCrcErrorCntOverloadPortn_Type()
)
pm1001imMonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonPacketsCntTable_Object = MibTable
pm1001imMonupRmonPacketsCntTable = _Pm1001imMonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 32)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntTable.setStatus("current")
_Pm1001imMonupRmonPacketsCntEntry_Object = MibTableRow
pm1001imMonupRmonPacketsCntEntry = _Pm1001imMonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 32, 1)
)
pm1001imMonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntEntry.setStatus("current")


class _Pm1001imMonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonPacketsCntIndex_Object = MibTableColumn
pm1001imMonupRmonPacketsCntIndex = _Pm1001imMonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 32, 1, 1),
    _Pm1001imMonupRmonPacketsCntIndex_Type()
)
pm1001imMonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntIndex.setStatus("current")
_Pm1001imMonupRmonPacketsCntValuePortn_Type = Counter64
_Pm1001imMonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonPacketsCntValuePortn = _Pm1001imMonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 32, 1, 2),
    _Pm1001imMonupRmonPacketsCntValuePortn_Type()
)
pm1001imMonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntValuePortn.setStatus("current")
_Pm1001imMonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonPacketsCntErrorPortn = _Pm1001imMonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 32, 1, 3),
    _Pm1001imMonupRmonPacketsCntErrorPortn_Type()
)
pm1001imMonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonPacketsCntOverloadPortn = _Pm1001imMonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 32, 1, 4),
    _Pm1001imMonupRmonPacketsCntOverloadPortn_Type()
)
pm1001imMonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonBroadcastCntTable_Object = MibTable
pm1001imMonupRmonBroadcastCntTable = _Pm1001imMonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 40)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntTable.setStatus("current")
_Pm1001imMonupRmonBroadcastCntEntry_Object = MibTableRow
pm1001imMonupRmonBroadcastCntEntry = _Pm1001imMonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 40, 1)
)
pm1001imMonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntEntry.setStatus("current")


class _Pm1001imMonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonBroadcastCntIndex_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntIndex = _Pm1001imMonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 40, 1, 1),
    _Pm1001imMonupRmonBroadcastCntIndex_Type()
)
pm1001imMonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntIndex.setStatus("current")
_Pm1001imMonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm1001imMonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntValuePortn = _Pm1001imMonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 40, 1, 2),
    _Pm1001imMonupRmonBroadcastCntValuePortn_Type()
)
pm1001imMonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm1001imMonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntErrorPortn = _Pm1001imMonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 40, 1, 3),
    _Pm1001imMonupRmonBroadcastCntErrorPortn_Type()
)
pm1001imMonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntOverloadPortn = _Pm1001imMonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 40, 1, 4),
    _Pm1001imMonupRmonBroadcastCntOverloadPortn_Type()
)
pm1001imMonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonMulticastCntTable_Object = MibTable
pm1001imMonupRmonMulticastCntTable = _Pm1001imMonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 48)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntTable.setStatus("current")
_Pm1001imMonupRmonMulticastCntEntry_Object = MibTableRow
pm1001imMonupRmonMulticastCntEntry = _Pm1001imMonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 48, 1)
)
pm1001imMonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntEntry.setStatus("current")


class _Pm1001imMonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonMulticastCntIndex_Object = MibTableColumn
pm1001imMonupRmonMulticastCntIndex = _Pm1001imMonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 48, 1, 1),
    _Pm1001imMonupRmonMulticastCntIndex_Type()
)
pm1001imMonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntIndex.setStatus("current")
_Pm1001imMonupRmonMulticastCntValuePortn_Type = Counter64
_Pm1001imMonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonMulticastCntValuePortn = _Pm1001imMonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 48, 1, 2),
    _Pm1001imMonupRmonMulticastCntValuePortn_Type()
)
pm1001imMonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntValuePortn.setStatus("current")
_Pm1001imMonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonMulticastCntErrorPortn = _Pm1001imMonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 48, 1, 3),
    _Pm1001imMonupRmonMulticastCntErrorPortn_Type()
)
pm1001imMonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonMulticastCntOverloadPortn = _Pm1001imMonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 48, 1, 4),
    _Pm1001imMonupRmonMulticastCntOverloadPortn_Type()
)
pm1001imMonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonTimerCntTable_Object = MibTable
pm1001imMonupRmonTimerCntTable = _Pm1001imMonupRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 56)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonTimerCntTable.setStatus("current")
_Pm1001imMonupRmonTimerCntEntry_Object = MibTableRow
pm1001imMonupRmonTimerCntEntry = _Pm1001imMonupRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 56, 1)
)
pm1001imMonupRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonTimerCntEntry.setStatus("current")


class _Pm1001imMonupRmonTimerCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonTimerCntIndex_Object = MibTableColumn
pm1001imMonupRmonTimerCntIndex = _Pm1001imMonupRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 56, 1, 1),
    _Pm1001imMonupRmonTimerCntIndex_Type()
)
pm1001imMonupRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonTimerCntIndex.setStatus("current")
_Pm1001imMonupRmonTimerCntValuePortn_Type = Counter64
_Pm1001imMonupRmonTimerCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonTimerCntValuePortn = _Pm1001imMonupRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 56, 1, 2),
    _Pm1001imMonupRmonTimerCntValuePortn_Type()
)
pm1001imMonupRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonTimerCntValuePortn.setStatus("current")
_Pm1001imMonupRmonTimerCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonTimerCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonTimerCntErrorPortn = _Pm1001imMonupRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 56, 1, 3),
    _Pm1001imMonupRmonTimerCntErrorPortn_Type()
)
pm1001imMonupRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonTimerCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonTimerCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonTimerCntOverloadPortn = _Pm1001imMonupRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 56, 1, 4),
    _Pm1001imMonupRmonTimerCntOverloadPortn_Type()
)
pm1001imMonupRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonTimerCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntTable_Object = MibTable
pm1001imMonupRmonPauseFrameCntTable = _Pm1001imMonupRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 64)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntTable.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntEntry_Object = MibTableRow
pm1001imMonupRmonPauseFrameCntEntry = _Pm1001imMonupRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 64, 1)
)
pm1001imMonupRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntEntry.setStatus("current")


class _Pm1001imMonupRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonPauseFrameCntIndex_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntIndex = _Pm1001imMonupRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 64, 1, 1),
    _Pm1001imMonupRmonPauseFrameCntIndex_Type()
)
pm1001imMonupRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntIndex.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntValuePortn_Type = Counter64
_Pm1001imMonupRmonPauseFrameCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntValuePortn = _Pm1001imMonupRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 64, 1, 2),
    _Pm1001imMonupRmonPauseFrameCntValuePortn_Type()
)
pm1001imMonupRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntValuePortn.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntErrorPortn = _Pm1001imMonupRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 64, 1, 3),
    _Pm1001imMonupRmonPauseFrameCntErrorPortn_Type()
)
pm1001imMonupRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntOverloadPortn = _Pm1001imMonupRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 64, 1, 4),
    _Pm1001imMonupRmonPauseFrameCntOverloadPortn_Type()
)
pm1001imMonupRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonDropFrameCntTable_Object = MibTable
pm1001imMonupRmonDropFrameCntTable = _Pm1001imMonupRmonDropFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 72)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntTable.setStatus("current")
_Pm1001imMonupRmonDropFrameCntEntry_Object = MibTableRow
pm1001imMonupRmonDropFrameCntEntry = _Pm1001imMonupRmonDropFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 72, 1)
)
pm1001imMonupRmonDropFrameCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonDropFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntEntry.setStatus("current")


class _Pm1001imMonupRmonDropFrameCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonDropFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonDropFrameCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonDropFrameCntIndex_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntIndex = _Pm1001imMonupRmonDropFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 72, 1, 1),
    _Pm1001imMonupRmonDropFrameCntIndex_Type()
)
pm1001imMonupRmonDropFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntIndex.setStatus("current")
_Pm1001imMonupRmonDropFrameCntValuePortn_Type = Counter64
_Pm1001imMonupRmonDropFrameCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntValuePortn = _Pm1001imMonupRmonDropFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 72, 1, 2),
    _Pm1001imMonupRmonDropFrameCntValuePortn_Type()
)
pm1001imMonupRmonDropFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntValuePortn.setStatus("current")
_Pm1001imMonupRmonDropFrameCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonDropFrameCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntErrorPortn = _Pm1001imMonupRmonDropFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 72, 1, 3),
    _Pm1001imMonupRmonDropFrameCntErrorPortn_Type()
)
pm1001imMonupRmonDropFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonDropFrameCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonDropFrameCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntOverloadPortn = _Pm1001imMonupRmonDropFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 72, 1, 4),
    _Pm1001imMonupRmonDropFrameCntOverloadPortn_Type()
)
pm1001imMonupRmonDropFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonBitsCntTable_Object = MibTable
pm1001imMonupRmonBitsCntTable = _Pm1001imMonupRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 80)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntTable.setStatus("current")
_Pm1001imMonupRmonBitsCntEntry_Object = MibTableRow
pm1001imMonupRmonBitsCntEntry = _Pm1001imMonupRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 80, 1)
)
pm1001imMonupRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntEntry.setStatus("current")


class _Pm1001imMonupRmonBitsCntIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonBitsCntIndex_Object = MibTableColumn
pm1001imMonupRmonBitsCntIndex = _Pm1001imMonupRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 80, 1, 1),
    _Pm1001imMonupRmonBitsCntIndex_Type()
)
pm1001imMonupRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntIndex.setStatus("current")
_Pm1001imMonupRmonBitsCntValuePortn_Type = Counter64
_Pm1001imMonupRmonBitsCntValuePortn_Object = MibTableColumn
pm1001imMonupRmonBitsCntValuePortn = _Pm1001imMonupRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 80, 1, 2),
    _Pm1001imMonupRmonBitsCntValuePortn_Type()
)
pm1001imMonupRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntValuePortn.setStatus("current")
_Pm1001imMonupRmonBitsCntErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonBitsCntErrorPortn_Object = MibTableColumn
pm1001imMonupRmonBitsCntErrorPortn = _Pm1001imMonupRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 80, 1, 3),
    _Pm1001imMonupRmonBitsCntErrorPortn_Type()
)
pm1001imMonupRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntErrorPortn.setStatus("current")
_Pm1001imMonupRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonBitsCntOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonBitsCntOverloadPortn = _Pm1001imMonupRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 80, 1, 4),
    _Pm1001imMonupRmonBitsCntOverloadPortn_Type()
)
pm1001imMonupRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonByteCntTable_Object = MibTable
pm1001imMondwRmonByteCntTable = _Pm1001imMondwRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 112)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntTable.setStatus("current")
_Pm1001imMondwRmonByteCntEntry_Object = MibTableRow
pm1001imMondwRmonByteCntEntry = _Pm1001imMondwRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 112, 1)
)
pm1001imMondwRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntEntry.setStatus("current")


class _Pm1001imMondwRmonByteCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonByteCntIndex_Object = MibTableColumn
pm1001imMondwRmonByteCntIndex = _Pm1001imMondwRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 112, 1, 1),
    _Pm1001imMondwRmonByteCntIndex_Type()
)
pm1001imMondwRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntIndex.setStatus("current")
_Pm1001imMondwRmonByteCntValuePortn_Type = Counter64
_Pm1001imMondwRmonByteCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonByteCntValuePortn = _Pm1001imMondwRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 112, 1, 2),
    _Pm1001imMondwRmonByteCntValuePortn_Type()
)
pm1001imMondwRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntValuePortn.setStatus("current")
_Pm1001imMondwRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonByteCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonByteCntErrorPortn = _Pm1001imMondwRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 112, 1, 3),
    _Pm1001imMondwRmonByteCntErrorPortn_Type()
)
pm1001imMondwRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonByteCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonByteCntOverloadPortn = _Pm1001imMondwRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 112, 1, 4),
    _Pm1001imMondwRmonByteCntOverloadPortn_Type()
)
pm1001imMondwRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntTable_Object = MibTable
pm1001imMondwRmonCrcErrorCntTable = _Pm1001imMondwRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 120)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntTable.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntEntry_Object = MibTableRow
pm1001imMondwRmonCrcErrorCntEntry = _Pm1001imMondwRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 120, 1)
)
pm1001imMondwRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntEntry.setStatus("current")


class _Pm1001imMondwRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonCrcErrorCntIndex_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntIndex = _Pm1001imMondwRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 120, 1, 1),
    _Pm1001imMondwRmonCrcErrorCntIndex_Type()
)
pm1001imMondwRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntIndex.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1001imMondwRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntValuePortn = _Pm1001imMondwRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 120, 1, 2),
    _Pm1001imMondwRmonCrcErrorCntValuePortn_Type()
)
pm1001imMondwRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntErrorPortn = _Pm1001imMondwRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 120, 1, 3),
    _Pm1001imMondwRmonCrcErrorCntErrorPortn_Type()
)
pm1001imMondwRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntOverloadPortn = _Pm1001imMondwRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 120, 1, 4),
    _Pm1001imMondwRmonCrcErrorCntOverloadPortn_Type()
)
pm1001imMondwRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonPacketsCntTable_Object = MibTable
pm1001imMondwRmonPacketsCntTable = _Pm1001imMondwRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 128)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntTable.setStatus("current")
_Pm1001imMondwRmonPacketsCntEntry_Object = MibTableRow
pm1001imMondwRmonPacketsCntEntry = _Pm1001imMondwRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 128, 1)
)
pm1001imMondwRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntEntry.setStatus("current")


class _Pm1001imMondwRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonPacketsCntIndex_Object = MibTableColumn
pm1001imMondwRmonPacketsCntIndex = _Pm1001imMondwRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 128, 1, 1),
    _Pm1001imMondwRmonPacketsCntIndex_Type()
)
pm1001imMondwRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntIndex.setStatus("current")
_Pm1001imMondwRmonPacketsCntValuePortn_Type = Counter64
_Pm1001imMondwRmonPacketsCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonPacketsCntValuePortn = _Pm1001imMondwRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 128, 1, 2),
    _Pm1001imMondwRmonPacketsCntValuePortn_Type()
)
pm1001imMondwRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntValuePortn.setStatus("current")
_Pm1001imMondwRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonPacketsCntErrorPortn = _Pm1001imMondwRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 128, 1, 3),
    _Pm1001imMondwRmonPacketsCntErrorPortn_Type()
)
pm1001imMondwRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonPacketsCntOverloadPortn = _Pm1001imMondwRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 128, 1, 4),
    _Pm1001imMondwRmonPacketsCntOverloadPortn_Type()
)
pm1001imMondwRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonBroadcastCntTable_Object = MibTable
pm1001imMondwRmonBroadcastCntTable = _Pm1001imMondwRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 136)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntTable.setStatus("current")
_Pm1001imMondwRmonBroadcastCntEntry_Object = MibTableRow
pm1001imMondwRmonBroadcastCntEntry = _Pm1001imMondwRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 136, 1)
)
pm1001imMondwRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntEntry.setStatus("current")


class _Pm1001imMondwRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonBroadcastCntIndex_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntIndex = _Pm1001imMondwRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 136, 1, 1),
    _Pm1001imMondwRmonBroadcastCntIndex_Type()
)
pm1001imMondwRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntIndex.setStatus("current")
_Pm1001imMondwRmonBroadcastCntValuePortn_Type = Counter64
_Pm1001imMondwRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntValuePortn = _Pm1001imMondwRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 136, 1, 2),
    _Pm1001imMondwRmonBroadcastCntValuePortn_Type()
)
pm1001imMondwRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntValuePortn.setStatus("current")
_Pm1001imMondwRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntErrorPortn = _Pm1001imMondwRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 136, 1, 3),
    _Pm1001imMondwRmonBroadcastCntErrorPortn_Type()
)
pm1001imMondwRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntOverloadPortn = _Pm1001imMondwRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 136, 1, 4),
    _Pm1001imMondwRmonBroadcastCntOverloadPortn_Type()
)
pm1001imMondwRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonMulticastCntTable_Object = MibTable
pm1001imMondwRmonMulticastCntTable = _Pm1001imMondwRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 144)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntTable.setStatus("current")
_Pm1001imMondwRmonMulticastCntEntry_Object = MibTableRow
pm1001imMondwRmonMulticastCntEntry = _Pm1001imMondwRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 144, 1)
)
pm1001imMondwRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntEntry.setStatus("current")


class _Pm1001imMondwRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonMulticastCntIndex_Object = MibTableColumn
pm1001imMondwRmonMulticastCntIndex = _Pm1001imMondwRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 144, 1, 1),
    _Pm1001imMondwRmonMulticastCntIndex_Type()
)
pm1001imMondwRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntIndex.setStatus("current")
_Pm1001imMondwRmonMulticastCntValuePortn_Type = Counter64
_Pm1001imMondwRmonMulticastCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonMulticastCntValuePortn = _Pm1001imMondwRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 144, 1, 2),
    _Pm1001imMondwRmonMulticastCntValuePortn_Type()
)
pm1001imMondwRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntValuePortn.setStatus("current")
_Pm1001imMondwRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonMulticastCntErrorPortn = _Pm1001imMondwRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 144, 1, 3),
    _Pm1001imMondwRmonMulticastCntErrorPortn_Type()
)
pm1001imMondwRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonMulticastCntOverloadPortn = _Pm1001imMondwRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 144, 1, 4),
    _Pm1001imMondwRmonMulticastCntOverloadPortn_Type()
)
pm1001imMondwRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntTable_Object = MibTable
pm1001imMondwRmonPauseFrameCntTable = _Pm1001imMondwRmonPauseFrameCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 152)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntTable.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntEntry_Object = MibTableRow
pm1001imMondwRmonPauseFrameCntEntry = _Pm1001imMondwRmonPauseFrameCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 152, 1)
)
pm1001imMondwRmonPauseFrameCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonPauseFrameCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntEntry.setStatus("current")


class _Pm1001imMondwRmonPauseFrameCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonPauseFrameCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonPauseFrameCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonPauseFrameCntIndex_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntIndex = _Pm1001imMondwRmonPauseFrameCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 152, 1, 1),
    _Pm1001imMondwRmonPauseFrameCntIndex_Type()
)
pm1001imMondwRmonPauseFrameCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntIndex.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntValuePortn_Type = Counter64
_Pm1001imMondwRmonPauseFrameCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntValuePortn = _Pm1001imMondwRmonPauseFrameCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 152, 1, 2),
    _Pm1001imMondwRmonPauseFrameCntValuePortn_Type()
)
pm1001imMondwRmonPauseFrameCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntValuePortn.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonPauseFrameCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntErrorPortn = _Pm1001imMondwRmonPauseFrameCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 152, 1, 3),
    _Pm1001imMondwRmonPauseFrameCntErrorPortn_Type()
)
pm1001imMondwRmonPauseFrameCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonPauseFrameCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntOverloadPortn = _Pm1001imMondwRmonPauseFrameCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 152, 1, 4),
    _Pm1001imMondwRmonPauseFrameCntOverloadPortn_Type()
)
pm1001imMondwRmonPauseFrameCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonTimerCntTable_Object = MibTable
pm1001imMondwRmonTimerCntTable = _Pm1001imMondwRmonTimerCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 160)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonTimerCntTable.setStatus("current")
_Pm1001imMondwRmonTimerCntEntry_Object = MibTableRow
pm1001imMondwRmonTimerCntEntry = _Pm1001imMondwRmonTimerCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 160, 1)
)
pm1001imMondwRmonTimerCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonTimerCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonTimerCntEntry.setStatus("current")


class _Pm1001imMondwRmonTimerCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonTimerCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonTimerCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonTimerCntIndex_Object = MibTableColumn
pm1001imMondwRmonTimerCntIndex = _Pm1001imMondwRmonTimerCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 160, 1, 1),
    _Pm1001imMondwRmonTimerCntIndex_Type()
)
pm1001imMondwRmonTimerCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonTimerCntIndex.setStatus("current")
_Pm1001imMondwRmonTimerCntValuePortn_Type = Counter64
_Pm1001imMondwRmonTimerCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonTimerCntValuePortn = _Pm1001imMondwRmonTimerCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 160, 1, 2),
    _Pm1001imMondwRmonTimerCntValuePortn_Type()
)
pm1001imMondwRmonTimerCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonTimerCntValuePortn.setStatus("current")
_Pm1001imMondwRmonTimerCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonTimerCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonTimerCntErrorPortn = _Pm1001imMondwRmonTimerCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 160, 1, 3),
    _Pm1001imMondwRmonTimerCntErrorPortn_Type()
)
pm1001imMondwRmonTimerCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonTimerCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonTimerCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonTimerCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonTimerCntOverloadPortn = _Pm1001imMondwRmonTimerCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 160, 1, 4),
    _Pm1001imMondwRmonTimerCntOverloadPortn_Type()
)
pm1001imMondwRmonTimerCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonTimerCntOverloadPortn.setStatus("current")
_Pm1001imMondwRmonBitsCntTable_Object = MibTable
pm1001imMondwRmonBitsCntTable = _Pm1001imMondwRmonBitsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 168)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntTable.setStatus("current")
_Pm1001imMondwRmonBitsCntEntry_Object = MibTableRow
pm1001imMondwRmonBitsCntEntry = _Pm1001imMondwRmonBitsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 168, 1)
)
pm1001imMondwRmonBitsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonBitsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntEntry.setStatus("current")


class _Pm1001imMondwRmonBitsCntIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonBitsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonBitsCntIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonBitsCntIndex_Object = MibTableColumn
pm1001imMondwRmonBitsCntIndex = _Pm1001imMondwRmonBitsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 168, 1, 1),
    _Pm1001imMondwRmonBitsCntIndex_Type()
)
pm1001imMondwRmonBitsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntIndex.setStatus("current")
_Pm1001imMondwRmonBitsCntValuePortn_Type = Counter64
_Pm1001imMondwRmonBitsCntValuePortn_Object = MibTableColumn
pm1001imMondwRmonBitsCntValuePortn = _Pm1001imMondwRmonBitsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 168, 1, 2),
    _Pm1001imMondwRmonBitsCntValuePortn_Type()
)
pm1001imMondwRmonBitsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntValuePortn.setStatus("current")
_Pm1001imMondwRmonBitsCntErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonBitsCntErrorPortn_Object = MibTableColumn
pm1001imMondwRmonBitsCntErrorPortn = _Pm1001imMondwRmonBitsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 168, 1, 3),
    _Pm1001imMondwRmonBitsCntErrorPortn_Type()
)
pm1001imMondwRmonBitsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntErrorPortn.setStatus("current")
_Pm1001imMondwRmonBitsCntOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonBitsCntOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonBitsCntOverloadPortn = _Pm1001imMondwRmonBitsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 168, 1, 4),
    _Pm1001imMondwRmonBitsCntOverloadPortn_Type()
)
pm1001imMondwRmonBitsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntOverloadPortn.setStatus("current")
_Pm1001imMonupRmonByteCntSTable_Object = MibTable
pm1001imMonupRmonByteCntSTable = _Pm1001imMonupRmonByteCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1024)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntSTable.setStatus("current")
_Pm1001imMonupRmonByteCntSEntry_Object = MibTableRow
pm1001imMonupRmonByteCntSEntry = _Pm1001imMonupRmonByteCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1024, 1)
)
pm1001imMonupRmonByteCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonByteCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntSEntry.setStatus("current")


class _Pm1001imMonupRmonByteCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonByteCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonByteCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonByteCntSIndex_Object = MibTableColumn
pm1001imMonupRmonByteCntSIndex = _Pm1001imMonupRmonByteCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1024, 1, 1),
    _Pm1001imMonupRmonByteCntSIndex_Type()
)
pm1001imMonupRmonByteCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntSIndex.setStatus("current")
_Pm1001imMonupRmonByteCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonByteCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonByteCntSValuePortn = _Pm1001imMonupRmonByteCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1024, 1, 2),
    _Pm1001imMonupRmonByteCntSValuePortn_Type()
)
pm1001imMonupRmonByteCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonByteCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonByteCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonByteCntSErrorPortn = _Pm1001imMonupRmonByteCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1024, 1, 3),
    _Pm1001imMonupRmonByteCntSErrorPortn_Type()
)
pm1001imMonupRmonByteCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonByteCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonByteCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonByteCntSOverloadPortn = _Pm1001imMonupRmonByteCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1024, 1, 4),
    _Pm1001imMonupRmonByteCntSOverloadPortn_Type()
)
pm1001imMonupRmonByteCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonByteCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntSTable_Object = MibTable
pm1001imMonupRmonCrcErrorCntSTable = _Pm1001imMonupRmonCrcErrorCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1032)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntSTable.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntSEntry_Object = MibTableRow
pm1001imMonupRmonCrcErrorCntSEntry = _Pm1001imMonupRmonCrcErrorCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1032, 1)
)
pm1001imMonupRmonCrcErrorCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonCrcErrorCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntSEntry.setStatus("current")


class _Pm1001imMonupRmonCrcErrorCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonCrcErrorCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonCrcErrorCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonCrcErrorCntSIndex_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntSIndex = _Pm1001imMonupRmonCrcErrorCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1032, 1, 1),
    _Pm1001imMonupRmonCrcErrorCntSIndex_Type()
)
pm1001imMonupRmonCrcErrorCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntSIndex.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonCrcErrorCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntSValuePortn = _Pm1001imMonupRmonCrcErrorCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1032, 1, 2),
    _Pm1001imMonupRmonCrcErrorCntSValuePortn_Type()
)
pm1001imMonupRmonCrcErrorCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonCrcErrorCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntSErrorPortn = _Pm1001imMonupRmonCrcErrorCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1032, 1, 3),
    _Pm1001imMonupRmonCrcErrorCntSErrorPortn_Type()
)
pm1001imMonupRmonCrcErrorCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonCrcErrorCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonCrcErrorCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonCrcErrorCntSOverloadPortn = _Pm1001imMonupRmonCrcErrorCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1032, 1, 4),
    _Pm1001imMonupRmonCrcErrorCntSOverloadPortn_Type()
)
pm1001imMonupRmonCrcErrorCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonCrcErrorCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonPacketsCntSTable_Object = MibTable
pm1001imMonupRmonPacketsCntSTable = _Pm1001imMonupRmonPacketsCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1040)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntSTable.setStatus("current")
_Pm1001imMonupRmonPacketsCntSEntry_Object = MibTableRow
pm1001imMonupRmonPacketsCntSEntry = _Pm1001imMonupRmonPacketsCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1040, 1)
)
pm1001imMonupRmonPacketsCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonPacketsCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntSEntry.setStatus("current")


class _Pm1001imMonupRmonPacketsCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonPacketsCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonPacketsCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonPacketsCntSIndex_Object = MibTableColumn
pm1001imMonupRmonPacketsCntSIndex = _Pm1001imMonupRmonPacketsCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1040, 1, 1),
    _Pm1001imMonupRmonPacketsCntSIndex_Type()
)
pm1001imMonupRmonPacketsCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntSIndex.setStatus("current")
_Pm1001imMonupRmonPacketsCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonPacketsCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonPacketsCntSValuePortn = _Pm1001imMonupRmonPacketsCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1040, 1, 2),
    _Pm1001imMonupRmonPacketsCntSValuePortn_Type()
)
pm1001imMonupRmonPacketsCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonPacketsCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonPacketsCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonPacketsCntSErrorPortn = _Pm1001imMonupRmonPacketsCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1040, 1, 3),
    _Pm1001imMonupRmonPacketsCntSErrorPortn_Type()
)
pm1001imMonupRmonPacketsCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonPacketsCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonPacketsCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonPacketsCntSOverloadPortn = _Pm1001imMonupRmonPacketsCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1040, 1, 4),
    _Pm1001imMonupRmonPacketsCntSOverloadPortn_Type()
)
pm1001imMonupRmonPacketsCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPacketsCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonBroadcastCntSTable_Object = MibTable
pm1001imMonupRmonBroadcastCntSTable = _Pm1001imMonupRmonBroadcastCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1048)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntSTable.setStatus("current")
_Pm1001imMonupRmonBroadcastCntSEntry_Object = MibTableRow
pm1001imMonupRmonBroadcastCntSEntry = _Pm1001imMonupRmonBroadcastCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1048, 1)
)
pm1001imMonupRmonBroadcastCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonBroadcastCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntSEntry.setStatus("current")


class _Pm1001imMonupRmonBroadcastCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonBroadcastCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonBroadcastCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonBroadcastCntSIndex_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntSIndex = _Pm1001imMonupRmonBroadcastCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1048, 1, 1),
    _Pm1001imMonupRmonBroadcastCntSIndex_Type()
)
pm1001imMonupRmonBroadcastCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntSIndex.setStatus("current")
_Pm1001imMonupRmonBroadcastCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonBroadcastCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntSValuePortn = _Pm1001imMonupRmonBroadcastCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1048, 1, 2),
    _Pm1001imMonupRmonBroadcastCntSValuePortn_Type()
)
pm1001imMonupRmonBroadcastCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonBroadcastCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonBroadcastCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntSErrorPortn = _Pm1001imMonupRmonBroadcastCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1048, 1, 3),
    _Pm1001imMonupRmonBroadcastCntSErrorPortn_Type()
)
pm1001imMonupRmonBroadcastCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonBroadcastCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonBroadcastCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonBroadcastCntSOverloadPortn = _Pm1001imMonupRmonBroadcastCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1048, 1, 4),
    _Pm1001imMonupRmonBroadcastCntSOverloadPortn_Type()
)
pm1001imMonupRmonBroadcastCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBroadcastCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonMulticastCntSTable_Object = MibTable
pm1001imMonupRmonMulticastCntSTable = _Pm1001imMonupRmonMulticastCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1056)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntSTable.setStatus("current")
_Pm1001imMonupRmonMulticastCntSEntry_Object = MibTableRow
pm1001imMonupRmonMulticastCntSEntry = _Pm1001imMonupRmonMulticastCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1056, 1)
)
pm1001imMonupRmonMulticastCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonMulticastCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntSEntry.setStatus("current")


class _Pm1001imMonupRmonMulticastCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonMulticastCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonMulticastCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonMulticastCntSIndex_Object = MibTableColumn
pm1001imMonupRmonMulticastCntSIndex = _Pm1001imMonupRmonMulticastCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1056, 1, 1),
    _Pm1001imMonupRmonMulticastCntSIndex_Type()
)
pm1001imMonupRmonMulticastCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntSIndex.setStatus("current")
_Pm1001imMonupRmonMulticastCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonMulticastCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonMulticastCntSValuePortn = _Pm1001imMonupRmonMulticastCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1056, 1, 2),
    _Pm1001imMonupRmonMulticastCntSValuePortn_Type()
)
pm1001imMonupRmonMulticastCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonMulticastCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonMulticastCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonMulticastCntSErrorPortn = _Pm1001imMonupRmonMulticastCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1056, 1, 3),
    _Pm1001imMonupRmonMulticastCntSErrorPortn_Type()
)
pm1001imMonupRmonMulticastCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonMulticastCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonMulticastCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonMulticastCntSOverloadPortn = _Pm1001imMonupRmonMulticastCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1056, 1, 4),
    _Pm1001imMonupRmonMulticastCntSOverloadPortn_Type()
)
pm1001imMonupRmonMulticastCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonMulticastCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntSTable_Object = MibTable
pm1001imMonupRmonPauseFrameCntSTable = _Pm1001imMonupRmonPauseFrameCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1072)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntSTable.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntSEntry_Object = MibTableRow
pm1001imMonupRmonPauseFrameCntSEntry = _Pm1001imMonupRmonPauseFrameCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1072, 1)
)
pm1001imMonupRmonPauseFrameCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonPauseFrameCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntSEntry.setStatus("current")


class _Pm1001imMonupRmonPauseFrameCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonPauseFrameCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonPauseFrameCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonPauseFrameCntSIndex_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntSIndex = _Pm1001imMonupRmonPauseFrameCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1072, 1, 1),
    _Pm1001imMonupRmonPauseFrameCntSIndex_Type()
)
pm1001imMonupRmonPauseFrameCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntSIndex.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonPauseFrameCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntSValuePortn = _Pm1001imMonupRmonPauseFrameCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1072, 1, 2),
    _Pm1001imMonupRmonPauseFrameCntSValuePortn_Type()
)
pm1001imMonupRmonPauseFrameCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonPauseFrameCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntSErrorPortn = _Pm1001imMonupRmonPauseFrameCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1072, 1, 3),
    _Pm1001imMonupRmonPauseFrameCntSErrorPortn_Type()
)
pm1001imMonupRmonPauseFrameCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonPauseFrameCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonPauseFrameCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonPauseFrameCntSOverloadPortn = _Pm1001imMonupRmonPauseFrameCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1072, 1, 4),
    _Pm1001imMonupRmonPauseFrameCntSOverloadPortn_Type()
)
pm1001imMonupRmonPauseFrameCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonPauseFrameCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonDropFrameCntSTable_Object = MibTable
pm1001imMonupRmonDropFrameCntSTable = _Pm1001imMonupRmonDropFrameCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1080)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntSTable.setStatus("current")
_Pm1001imMonupRmonDropFrameCntSEntry_Object = MibTableRow
pm1001imMonupRmonDropFrameCntSEntry = _Pm1001imMonupRmonDropFrameCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1080, 1)
)
pm1001imMonupRmonDropFrameCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonDropFrameCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntSEntry.setStatus("current")


class _Pm1001imMonupRmonDropFrameCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonDropFrameCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonDropFrameCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonDropFrameCntSIndex_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntSIndex = _Pm1001imMonupRmonDropFrameCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1080, 1, 1),
    _Pm1001imMonupRmonDropFrameCntSIndex_Type()
)
pm1001imMonupRmonDropFrameCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntSIndex.setStatus("current")
_Pm1001imMonupRmonDropFrameCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonDropFrameCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntSValuePortn = _Pm1001imMonupRmonDropFrameCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1080, 1, 2),
    _Pm1001imMonupRmonDropFrameCntSValuePortn_Type()
)
pm1001imMonupRmonDropFrameCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonDropFrameCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonDropFrameCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntSErrorPortn = _Pm1001imMonupRmonDropFrameCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1080, 1, 3),
    _Pm1001imMonupRmonDropFrameCntSErrorPortn_Type()
)
pm1001imMonupRmonDropFrameCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonDropFrameCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonDropFrameCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonDropFrameCntSOverloadPortn = _Pm1001imMonupRmonDropFrameCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1080, 1, 4),
    _Pm1001imMonupRmonDropFrameCntSOverloadPortn_Type()
)
pm1001imMonupRmonDropFrameCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonDropFrameCntSOverloadPortn.setStatus("current")
_Pm1001imMonupRmonBitsCntSTable_Object = MibTable
pm1001imMonupRmonBitsCntSTable = _Pm1001imMonupRmonBitsCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1088)
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntSTable.setStatus("current")
_Pm1001imMonupRmonBitsCntSEntry_Object = MibTableRow
pm1001imMonupRmonBitsCntSEntry = _Pm1001imMonupRmonBitsCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1088, 1)
)
pm1001imMonupRmonBitsCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMonupRmonBitsCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntSEntry.setStatus("current")


class _Pm1001imMonupRmonBitsCntSIndex_Type(Integer32):
    """Custom type pm1001imMonupRmonBitsCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMonupRmonBitsCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMonupRmonBitsCntSIndex_Object = MibTableColumn
pm1001imMonupRmonBitsCntSIndex = _Pm1001imMonupRmonBitsCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1088, 1, 1),
    _Pm1001imMonupRmonBitsCntSIndex_Type()
)
pm1001imMonupRmonBitsCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntSIndex.setStatus("current")
_Pm1001imMonupRmonBitsCntSValuePortn_Type = Counter64
_Pm1001imMonupRmonBitsCntSValuePortn_Object = MibTableColumn
pm1001imMonupRmonBitsCntSValuePortn = _Pm1001imMonupRmonBitsCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1088, 1, 2),
    _Pm1001imMonupRmonBitsCntSValuePortn_Type()
)
pm1001imMonupRmonBitsCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntSValuePortn.setStatus("current")
_Pm1001imMonupRmonBitsCntSErrorPortn_Type = EkiOnOff
_Pm1001imMonupRmonBitsCntSErrorPortn_Object = MibTableColumn
pm1001imMonupRmonBitsCntSErrorPortn = _Pm1001imMonupRmonBitsCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1088, 1, 3),
    _Pm1001imMonupRmonBitsCntSErrorPortn_Type()
)
pm1001imMonupRmonBitsCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntSErrorPortn.setStatus("current")
_Pm1001imMonupRmonBitsCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMonupRmonBitsCntSOverloadPortn_Object = MibTableColumn
pm1001imMonupRmonBitsCntSOverloadPortn = _Pm1001imMonupRmonBitsCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1088, 1, 4),
    _Pm1001imMonupRmonBitsCntSOverloadPortn_Type()
)
pm1001imMonupRmonBitsCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMonupRmonBitsCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonByteCntSTable_Object = MibTable
pm1001imMondwRmonByteCntSTable = _Pm1001imMondwRmonByteCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1120)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntSTable.setStatus("current")
_Pm1001imMondwRmonByteCntSEntry_Object = MibTableRow
pm1001imMondwRmonByteCntSEntry = _Pm1001imMondwRmonByteCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1120, 1)
)
pm1001imMondwRmonByteCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonByteCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntSEntry.setStatus("current")


class _Pm1001imMondwRmonByteCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonByteCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonByteCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonByteCntSIndex_Object = MibTableColumn
pm1001imMondwRmonByteCntSIndex = _Pm1001imMondwRmonByteCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1120, 1, 1),
    _Pm1001imMondwRmonByteCntSIndex_Type()
)
pm1001imMondwRmonByteCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntSIndex.setStatus("current")
_Pm1001imMondwRmonByteCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonByteCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonByteCntSValuePortn = _Pm1001imMondwRmonByteCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1120, 1, 2),
    _Pm1001imMondwRmonByteCntSValuePortn_Type()
)
pm1001imMondwRmonByteCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonByteCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonByteCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonByteCntSErrorPortn = _Pm1001imMondwRmonByteCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1120, 1, 3),
    _Pm1001imMondwRmonByteCntSErrorPortn_Type()
)
pm1001imMondwRmonByteCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonByteCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonByteCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonByteCntSOverloadPortn = _Pm1001imMondwRmonByteCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1120, 1, 4),
    _Pm1001imMondwRmonByteCntSOverloadPortn_Type()
)
pm1001imMondwRmonByteCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonByteCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntSTable_Object = MibTable
pm1001imMondwRmonCrcErrorCntSTable = _Pm1001imMondwRmonCrcErrorCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1128)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntSTable.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntSEntry_Object = MibTableRow
pm1001imMondwRmonCrcErrorCntSEntry = _Pm1001imMondwRmonCrcErrorCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1128, 1)
)
pm1001imMondwRmonCrcErrorCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonCrcErrorCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntSEntry.setStatus("current")


class _Pm1001imMondwRmonCrcErrorCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonCrcErrorCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonCrcErrorCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonCrcErrorCntSIndex_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntSIndex = _Pm1001imMondwRmonCrcErrorCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1128, 1, 1),
    _Pm1001imMondwRmonCrcErrorCntSIndex_Type()
)
pm1001imMondwRmonCrcErrorCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntSIndex.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonCrcErrorCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntSValuePortn = _Pm1001imMondwRmonCrcErrorCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1128, 1, 2),
    _Pm1001imMondwRmonCrcErrorCntSValuePortn_Type()
)
pm1001imMondwRmonCrcErrorCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonCrcErrorCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntSErrorPortn = _Pm1001imMondwRmonCrcErrorCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1128, 1, 3),
    _Pm1001imMondwRmonCrcErrorCntSErrorPortn_Type()
)
pm1001imMondwRmonCrcErrorCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonCrcErrorCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonCrcErrorCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonCrcErrorCntSOverloadPortn = _Pm1001imMondwRmonCrcErrorCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1128, 1, 4),
    _Pm1001imMondwRmonCrcErrorCntSOverloadPortn_Type()
)
pm1001imMondwRmonCrcErrorCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonCrcErrorCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonPacketsCntSTable_Object = MibTable
pm1001imMondwRmonPacketsCntSTable = _Pm1001imMondwRmonPacketsCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1136)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntSTable.setStatus("current")
_Pm1001imMondwRmonPacketsCntSEntry_Object = MibTableRow
pm1001imMondwRmonPacketsCntSEntry = _Pm1001imMondwRmonPacketsCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1136, 1)
)
pm1001imMondwRmonPacketsCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonPacketsCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntSEntry.setStatus("current")


class _Pm1001imMondwRmonPacketsCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonPacketsCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonPacketsCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonPacketsCntSIndex_Object = MibTableColumn
pm1001imMondwRmonPacketsCntSIndex = _Pm1001imMondwRmonPacketsCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1136, 1, 1),
    _Pm1001imMondwRmonPacketsCntSIndex_Type()
)
pm1001imMondwRmonPacketsCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntSIndex.setStatus("current")
_Pm1001imMondwRmonPacketsCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonPacketsCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonPacketsCntSValuePortn = _Pm1001imMondwRmonPacketsCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1136, 1, 2),
    _Pm1001imMondwRmonPacketsCntSValuePortn_Type()
)
pm1001imMondwRmonPacketsCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonPacketsCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonPacketsCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonPacketsCntSErrorPortn = _Pm1001imMondwRmonPacketsCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1136, 1, 3),
    _Pm1001imMondwRmonPacketsCntSErrorPortn_Type()
)
pm1001imMondwRmonPacketsCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonPacketsCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonPacketsCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonPacketsCntSOverloadPortn = _Pm1001imMondwRmonPacketsCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1136, 1, 4),
    _Pm1001imMondwRmonPacketsCntSOverloadPortn_Type()
)
pm1001imMondwRmonPacketsCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPacketsCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonBroadcastCntSTable_Object = MibTable
pm1001imMondwRmonBroadcastCntSTable = _Pm1001imMondwRmonBroadcastCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1144)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntSTable.setStatus("current")
_Pm1001imMondwRmonBroadcastCntSEntry_Object = MibTableRow
pm1001imMondwRmonBroadcastCntSEntry = _Pm1001imMondwRmonBroadcastCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1144, 1)
)
pm1001imMondwRmonBroadcastCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonBroadcastCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntSEntry.setStatus("current")


class _Pm1001imMondwRmonBroadcastCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonBroadcastCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonBroadcastCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonBroadcastCntSIndex_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntSIndex = _Pm1001imMondwRmonBroadcastCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1144, 1, 1),
    _Pm1001imMondwRmonBroadcastCntSIndex_Type()
)
pm1001imMondwRmonBroadcastCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntSIndex.setStatus("current")
_Pm1001imMondwRmonBroadcastCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonBroadcastCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntSValuePortn = _Pm1001imMondwRmonBroadcastCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1144, 1, 2),
    _Pm1001imMondwRmonBroadcastCntSValuePortn_Type()
)
pm1001imMondwRmonBroadcastCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonBroadcastCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonBroadcastCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntSErrorPortn = _Pm1001imMondwRmonBroadcastCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1144, 1, 3),
    _Pm1001imMondwRmonBroadcastCntSErrorPortn_Type()
)
pm1001imMondwRmonBroadcastCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonBroadcastCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonBroadcastCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonBroadcastCntSOverloadPortn = _Pm1001imMondwRmonBroadcastCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1144, 1, 4),
    _Pm1001imMondwRmonBroadcastCntSOverloadPortn_Type()
)
pm1001imMondwRmonBroadcastCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBroadcastCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonMulticastCntSTable_Object = MibTable
pm1001imMondwRmonMulticastCntSTable = _Pm1001imMondwRmonMulticastCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1152)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntSTable.setStatus("current")
_Pm1001imMondwRmonMulticastCntSEntry_Object = MibTableRow
pm1001imMondwRmonMulticastCntSEntry = _Pm1001imMondwRmonMulticastCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1152, 1)
)
pm1001imMondwRmonMulticastCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonMulticastCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntSEntry.setStatus("current")


class _Pm1001imMondwRmonMulticastCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonMulticastCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonMulticastCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonMulticastCntSIndex_Object = MibTableColumn
pm1001imMondwRmonMulticastCntSIndex = _Pm1001imMondwRmonMulticastCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1152, 1, 1),
    _Pm1001imMondwRmonMulticastCntSIndex_Type()
)
pm1001imMondwRmonMulticastCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntSIndex.setStatus("current")
_Pm1001imMondwRmonMulticastCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonMulticastCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonMulticastCntSValuePortn = _Pm1001imMondwRmonMulticastCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1152, 1, 2),
    _Pm1001imMondwRmonMulticastCntSValuePortn_Type()
)
pm1001imMondwRmonMulticastCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonMulticastCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonMulticastCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonMulticastCntSErrorPortn = _Pm1001imMondwRmonMulticastCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1152, 1, 3),
    _Pm1001imMondwRmonMulticastCntSErrorPortn_Type()
)
pm1001imMondwRmonMulticastCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonMulticastCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonMulticastCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonMulticastCntSOverloadPortn = _Pm1001imMondwRmonMulticastCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1152, 1, 4),
    _Pm1001imMondwRmonMulticastCntSOverloadPortn_Type()
)
pm1001imMondwRmonMulticastCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonMulticastCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntSTable_Object = MibTable
pm1001imMondwRmonPauseFrameCntSTable = _Pm1001imMondwRmonPauseFrameCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1160)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntSTable.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntSEntry_Object = MibTableRow
pm1001imMondwRmonPauseFrameCntSEntry = _Pm1001imMondwRmonPauseFrameCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1160, 1)
)
pm1001imMondwRmonPauseFrameCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonPauseFrameCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntSEntry.setStatus("current")


class _Pm1001imMondwRmonPauseFrameCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonPauseFrameCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonPauseFrameCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonPauseFrameCntSIndex_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntSIndex = _Pm1001imMondwRmonPauseFrameCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1160, 1, 1),
    _Pm1001imMondwRmonPauseFrameCntSIndex_Type()
)
pm1001imMondwRmonPauseFrameCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntSIndex.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonPauseFrameCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntSValuePortn = _Pm1001imMondwRmonPauseFrameCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1160, 1, 2),
    _Pm1001imMondwRmonPauseFrameCntSValuePortn_Type()
)
pm1001imMondwRmonPauseFrameCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonPauseFrameCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntSErrorPortn = _Pm1001imMondwRmonPauseFrameCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1160, 1, 3),
    _Pm1001imMondwRmonPauseFrameCntSErrorPortn_Type()
)
pm1001imMondwRmonPauseFrameCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonPauseFrameCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonPauseFrameCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonPauseFrameCntSOverloadPortn = _Pm1001imMondwRmonPauseFrameCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1160, 1, 4),
    _Pm1001imMondwRmonPauseFrameCntSOverloadPortn_Type()
)
pm1001imMondwRmonPauseFrameCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonPauseFrameCntSOverloadPortn.setStatus("current")
_Pm1001imMondwRmonBitsCntSTable_Object = MibTable
pm1001imMondwRmonBitsCntSTable = _Pm1001imMondwRmonBitsCntSTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1176)
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntSTable.setStatus("current")
_Pm1001imMondwRmonBitsCntSEntry_Object = MibTableRow
pm1001imMondwRmonBitsCntSEntry = _Pm1001imMondwRmonBitsCntSEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1176, 1)
)
pm1001imMondwRmonBitsCntSEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imMondwRmonBitsCntSIndex"),
)
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntSEntry.setStatus("current")


class _Pm1001imMondwRmonBitsCntSIndex_Type(Integer32):
    """Custom type pm1001imMondwRmonBitsCntSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imMondwRmonBitsCntSIndex_Type.__name__ = "Integer32"
_Pm1001imMondwRmonBitsCntSIndex_Object = MibTableColumn
pm1001imMondwRmonBitsCntSIndex = _Pm1001imMondwRmonBitsCntSIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1176, 1, 1),
    _Pm1001imMondwRmonBitsCntSIndex_Type()
)
pm1001imMondwRmonBitsCntSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntSIndex.setStatus("current")
_Pm1001imMondwRmonBitsCntSValuePortn_Type = Counter64
_Pm1001imMondwRmonBitsCntSValuePortn_Object = MibTableColumn
pm1001imMondwRmonBitsCntSValuePortn = _Pm1001imMondwRmonBitsCntSValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1176, 1, 2),
    _Pm1001imMondwRmonBitsCntSValuePortn_Type()
)
pm1001imMondwRmonBitsCntSValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntSValuePortn.setStatus("current")
_Pm1001imMondwRmonBitsCntSErrorPortn_Type = EkiOnOff
_Pm1001imMondwRmonBitsCntSErrorPortn_Object = MibTableColumn
pm1001imMondwRmonBitsCntSErrorPortn = _Pm1001imMondwRmonBitsCntSErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1176, 1, 3),
    _Pm1001imMondwRmonBitsCntSErrorPortn_Type()
)
pm1001imMondwRmonBitsCntSErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntSErrorPortn.setStatus("current")
_Pm1001imMondwRmonBitsCntSOverloadPortn_Type = EkiOnOff
_Pm1001imMondwRmonBitsCntSOverloadPortn_Object = MibTableColumn
pm1001imMondwRmonBitsCntSOverloadPortn = _Pm1001imMondwRmonBitsCntSOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 2, 1176, 1, 4),
    _Pm1001imMondwRmonBitsCntSOverloadPortn_Type()
)
pm1001imMondwRmonBitsCntSOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imMondwRmonBitsCntSOverloadPortn.setStatus("current")
_Pm1001imRmonLine_ObjectIdentity = ObjectIdentity
pm1001imRmonLine = _Pm1001imRmonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 9, 3)
)
_Pm1001imConfig_ObjectIdentity = ObjectIdentity
pm1001imConfig = _Pm1001imConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10)
)
_Pm1001imCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1001imCfgAccessCAisCsf = _Pm1001imCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1)
)
_Pm1001imCfgClientcaiscsfTable_Object = MibTable
pm1001imCfgClientcaiscsfTable = _Pm1001imCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1)
)
if mibBuilder.loadTexts:
    pm1001imCfgClientcaiscsfTable.setStatus("current")
_Pm1001imCfgClientcaiscsfEntry_Object = MibTableRow
pm1001imCfgClientcaiscsfEntry = _Pm1001imCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1)
)
pm1001imCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCfgClientcaiscsfEntry.setStatus("current")


class _Pm1001imCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1001imCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1001imCfgClientcaiscsfIndex_Object = MibTableColumn
pm1001imCfgClientcaiscsfIndex = _Pm1001imCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 1),
    _Pm1001imCfgClientcaiscsfIndex_Type()
)
pm1001imCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCfgClientcaiscsfIndex.setStatus("current")


class _Pm1001imCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1001imCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgCAisModePortn_Object = MibTableColumn
pm1001imCfgCAisModePortn = _Pm1001imCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 3),
    _Pm1001imCfgCAisModePortn_Type()
)
pm1001imCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgCAisModePortn.setStatus("current")


class _Pm1001imCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1001imCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1001imCfgUpAccessioAlmPortn = _Pm1001imCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 9),
    _Pm1001imCfgUpAccessioAlmPortn_Type()
)
pm1001imCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1001imCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1001imCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1001imCfgUpMapperDeAlmPortn = _Pm1001imCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 10),
    _Pm1001imCfgUpMapperDeAlmPortn_Type()
)
pm1001imCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1001imCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1001imCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1001imCfgDownAccessioAlmPortn = _Pm1001imCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 17),
    _Pm1001imCfgDownAccessioAlmPortn_Type()
)
pm1001imCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1001imCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1001imCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1001imCfgDownMapperDeAlmPortn = _Pm1001imCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 18),
    _Pm1001imCfgDownMapperDeAlmPortn_Type()
)
pm1001imCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1001imCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1001imCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1001imCfgDownDfrmAlmPortn = _Pm1001imCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 19),
    _Pm1001imCfgDownDfrmAlmPortn_Type()
)
pm1001imCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1001imCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1001imCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1001imCfgDownLineSyncAlarmsPortn = _Pm1001imCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 1, 1, 1, 20),
    _Pm1001imCfgDownLineSyncAlarmsPortn_Type()
)
pm1001imCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pm1001imCfgStartup_ObjectIdentity = ObjectIdentity
pm1001imCfgStartup = _Pm1001imCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2)
)
_Pm1001imCfgClientStartupTable_Object = MibTable
pm1001imCfgClientStartupTable = _Pm1001imCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 1)
)
if mibBuilder.loadTexts:
    pm1001imCfgClientStartupTable.setStatus("current")
_Pm1001imCfgClientStartupEntry_Object = MibTableRow
pm1001imCfgClientStartupEntry = _Pm1001imCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 1, 1)
)
pm1001imCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCfgClientStartupEntry.setStatus("current")


class _Pm1001imCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1001imCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1001imCfgClientStartupIndex_Object = MibTableColumn
pm1001imCfgClientStartupIndex = _Pm1001imCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 1, 1, 1),
    _Pm1001imCfgClientStartupIndex_Type()
)
pm1001imCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCfgClientStartupIndex.setStatus("current")


class _Pm1001imCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1001imCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgSystConfPortPortn_Object = MibTableColumn
pm1001imCfgSystConfPortPortn = _Pm1001imCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 1, 1, 3),
    _Pm1001imCfgSystConfPortPortn_Type()
)
pm1001imCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgSystConfPortPortn.setStatus("current")


class _Pm1001imCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1001imCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgNetConfPortPortn_Object = MibTableColumn
pm1001imCfgNetConfPortPortn = _Pm1001imCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 1, 1, 4),
    _Pm1001imCfgNetConfPortPortn_Type()
)
pm1001imCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgNetConfPortPortn.setStatus("current")
_Pm1001imtablelineStartup_ObjectIdentity = ObjectIdentity
pm1001imtablelineStartup = _Pm1001imtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 2)
)


class _Pm1001imCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1001imCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1001imCfgsystConfLine1_Object = MibScalar
pm1001imCfgsystConfLine1 = _Pm1001imCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 2, 2),
    _Pm1001imCfgsystConfLine1_Type()
)
pm1001imCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgsystConfLine1.setStatus("current")


class _Pm1001imCfglineBandwidth1_Type(Unsigned32):
    """Custom type pm1001imCfglineBandwidth1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfglineBandwidth1_Type.__name__ = "Unsigned32"
_Pm1001imCfglineBandwidth1_Object = MibScalar
pm1001imCfglineBandwidth1 = _Pm1001imCfglineBandwidth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 2, 4),
    _Pm1001imCfglineBandwidth1_Type()
)
pm1001imCfglineBandwidth1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfglineBandwidth1.setStatus("current")


class _Pm1001imCfglineOptions1_Type(Unsigned32):
    """Custom type pm1001imCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1001imCfglineOptions1_Object = MibScalar
pm1001imCfglineOptions1 = _Pm1001imCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 2, 5),
    _Pm1001imCfglineOptions1_Type()
)
pm1001imCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfglineOptions1.setStatus("current")
_Pm1001imCfgXfpTable_Object = MibTable
pm1001imCfgXfpTable = _Pm1001imCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 3)
)
if mibBuilder.loadTexts:
    pm1001imCfgXfpTable.setStatus("current")
_Pm1001imCfgXfpEntry_Object = MibTableRow
pm1001imCfgXfpEntry = _Pm1001imCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 3, 1)
)
pm1001imCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCfgXfpEntry.setStatus("current")


class _Pm1001imCfgXfpIndex_Type(Integer32):
    """Custom type pm1001imCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1001imCfgXfpIndex_Object = MibTableColumn
pm1001imCfgXfpIndex = _Pm1001imCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 3, 1, 1),
    _Pm1001imCfgXfpIndex_Type()
)
pm1001imCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCfgXfpIndex.setStatus("current")


class _Pm1001imCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1001imCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgSystConfXfpPortn_Object = MibTableColumn
pm1001imCfgSystConfXfpPortn = _Pm1001imCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 3, 1, 3),
    _Pm1001imCfgSystConfXfpPortn_Type()
)
pm1001imCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgSystConfXfpPortn.setStatus("current")


class _Pm1001imCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1001imCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1001imCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1001imCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1001imCfgDataRateConfXfpPortn = _Pm1001imCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 2, 3, 1, 4),
    _Pm1001imCfgDataRateConfXfpPortn_Type()
)
pm1001imCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1001imCfgLabels_ObjectIdentity = ObjectIdentity
pm1001imCfgLabels = _Pm1001imCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3)
)
_Pm1001imCfgLabelclientTable_Object = MibTable
pm1001imCfgLabelclientTable = _Pm1001imCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 1)
)
if mibBuilder.loadTexts:
    pm1001imCfgLabelclientTable.setStatus("current")
_Pm1001imCfgLabelclientEntry_Object = MibTableRow
pm1001imCfgLabelclientEntry = _Pm1001imCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 1, 1)
)
pm1001imCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCfgLabelclientEntry.setStatus("current")


class _Pm1001imCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1001imCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1001imCfgLabelclientIndex_Object = MibTableColumn
pm1001imCfgLabelclientIndex = _Pm1001imCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 1, 1, 1),
    _Pm1001imCfgLabelclientIndex_Type()
)
pm1001imCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCfgLabelclientIndex.setStatus("current")


class _Pm1001imCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1001imCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1001imCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1001imCfgLabelclientPortn_Object = MibTableColumn
pm1001imCfgLabelclientPortn = _Pm1001imCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 1, 1, 3),
    _Pm1001imCfgLabelclientPortn_Type()
)
pm1001imCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgLabelclientPortn.setStatus("current")
_Pm1001imCfgLabellineTable_Object = MibTable
pm1001imCfgLabellineTable = _Pm1001imCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 2)
)
if mibBuilder.loadTexts:
    pm1001imCfgLabellineTable.setStatus("current")
_Pm1001imCfgLabellineEntry_Object = MibTableRow
pm1001imCfgLabellineEntry = _Pm1001imCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 2, 1)
)
pm1001imCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1001IM-MIB", "pm1001imCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1001imCfgLabellineEntry.setStatus("current")


class _Pm1001imCfgLabellineIndex_Type(Integer32):
    """Custom type pm1001imCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1001imCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1001imCfgLabellineIndex_Object = MibTableColumn
pm1001imCfgLabellineIndex = _Pm1001imCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 2, 1, 1),
    _Pm1001imCfgLabellineIndex_Type()
)
pm1001imCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imCfgLabellineIndex.setStatus("current")


class _Pm1001imCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1001imCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1001imCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1001imCfgLabellinePortn_Object = MibTableColumn
pm1001imCfgLabellinePortn = _Pm1001imCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 3, 2, 1, 3),
    _Pm1001imCfgLabellinePortn_Type()
)
pm1001imCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgLabellinePortn.setStatus("current")
_Pm1001imCfgWriteConfiguration_Type = EkiOnOff
_Pm1001imCfgWriteConfiguration_Object = MibScalar
pm1001imCfgWriteConfiguration = _Pm1001imCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 10, 257),
    _Pm1001imCfgWriteConfiguration_Type()
)
pm1001imCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1001imCfgWriteConfiguration.setStatus("current")
_Pm1001imtraps_ObjectIdentity = ObjectIdentity
pm1001imtraps = _Pm1001imtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11)
)


class _Pm1001imtrapLineNumber_Type(Integer32):
    """Custom type pm1001imtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1001imtrapLineNumber_Type.__name__ = "Integer32"
_Pm1001imtrapLineNumber_Object = MibScalar
pm1001imtrapLineNumber = _Pm1001imtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 3),
    _Pm1001imtrapLineNumber_Type()
)
pm1001imtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imtrapLineNumber.setStatus("current")


class _Pm1001imtrapBoardNumber_Type(Integer32):
    """Custom type pm1001imtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1001imtrapBoardNumber_Type.__name__ = "Integer32"
_Pm1001imtrapBoardNumber_Object = MibScalar
pm1001imtrapBoardNumber = _Pm1001imtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 4),
    _Pm1001imtrapBoardNumber_Type()
)
pm1001imtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1001imtrapBoardNumber.setStatus("current")

# Managed Objects groups


# Notification objects

pm1001imLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 30)
)
pm1001imLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineSfpDdmWarningPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapLineNumber"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1001imLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 31)
)
pm1001imLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineSfpDdmWarningPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapLineNumber"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1001imLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 32)
)
pm1001imLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineSfpDdmAlmPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapLineNumber"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001imLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 33)
)
pm1001imLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineSfpDdmAlmPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapLineNumber"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1001imLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 34)
)
pm1001imLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineFailPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineHwFailPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapLineNumber"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1001imLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 35)
)
pm1001imLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineFailPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imAlmLineHwFailPortn"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapLineNumber"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1001imClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 40)
)
pm1001imClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientSfpDdmWarning"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1001imClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 41)
)
pm1001imClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientSfpDdmWarning"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1001imClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 42)
)
pm1001imClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientSfpDdmAlm"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001imClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 43)
)
pm1001imClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientSfpDdmAlm"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1001imClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 44)
)
pm1001imClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientFail"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientHwFail"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1001imClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 45)
)
pm1001imClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientFail"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imAlmClientHwFail"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1001imPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 50)
)
pm1001imPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmDefFuseB"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imAlmDefFuseA"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1001imPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 15, 11, 51)
)
pm1001imPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1001IM-MIB", "pm1001imAlmDefFuseB"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imAlmDefFuseA"),
        ("EKINOPS-Pm1001IM-MIB", "pm1001imtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1001imPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1001IM-MIB",
    **{"Pm1001imBandwidthMode": Pm1001imBandwidthMode,
       "modulePm1001im": modulePm1001im,
       "pm1001imalarms": pm1001imalarms,
       "pm1001imAlmOther": pm1001imAlmOther,
       "pm1001imAlmOtherNurg": pm1001imAlmOtherNurg,
       "pm1001imAlmsynthAlm2": pm1001imAlmsynthAlm2,
       "pm1001imAlmConfTableSave": pm1001imAlmConfTableSave,
       "pm1001imAlmInvUpload": pm1001imAlmInvUpload,
       "pm1001imAlmConfTableLoad": pm1001imAlmConfTableLoad,
       "pm1001imAlmCorrelatOff": pm1001imAlmCorrelatOff,
       "pm1001imAlmMaintenanceOn": pm1001imAlmMaintenanceOn,
       "pm1001imAlmOtherUrg": pm1001imAlmOtherUrg,
       "pm1001imAlmmodInitFailLevel2": pm1001imAlmmodInitFailLevel2,
       "pm1001imAlmLedFail": pm1001imAlmLedFail,
       "pm1001imAlmNextColdBootForced": pm1001imAlmNextColdBootForced,
       "pm1001imAlmBootUndone": pm1001imAlmBootUndone,
       "pm1001imAlmResetHwInitFail": pm1001imAlmResetHwInitFail,
       "pm1001imAlmSwInitFail": pm1001imAlmSwInitFail,
       "pm1001imAlmmodInitFailLevel3": pm1001imAlmmodInitFailLevel3,
       "pm1001imAlmGwIdentFail": pm1001imAlmGwIdentFail,
       "pm1001imAlmObmTypeReadFail": pm1001imAlmObmTypeReadFail,
       "pm1001imAlmInitModuleFail": pm1001imAlmInitModuleFail,
       "pm1001imAlmClientXfpInitFail": pm1001imAlmClientXfpInitFail,
       "pm1001imAlmLineInitFail": pm1001imAlmLineInitFail,
       "pm1001imAlmLine1InitFail": pm1001imAlmLine1InitFail,
       "pm1001imAlmLine2InitFail": pm1001imAlmLine2InitFail,
       "pm1001imAlmLine3InitFail": pm1001imAlmLine3InitFail,
       "pm1001imAlmLine4InitFail": pm1001imAlmLine4InitFail,
       "pm1001imAlmOtherCrit": pm1001imAlmOtherCrit,
       "pm1001imAlmsynthAlm0": pm1001imAlmsynthAlm0,
       "pm1001imAlmModGlobFail": pm1001imAlmModGlobFail,
       "pm1001imAlmDefFuseA": pm1001imAlmDefFuseA,
       "pm1001imAlmDefFuseB": pm1001imAlmDefFuseB,
       "pm1001imAlmClient": pm1001imAlmClient,
       "pm1001imAlmClientNurg": pm1001imAlmClientNurg,
       "pm1001imAlmclientXfpWarnings": pm1001imAlmclientXfpWarnings,
       "pm1001imAlmClientTxPowerLowWarning": pm1001imAlmClientTxPowerLowWarning,
       "pm1001imAlmClientTxPowerHighWarning": pm1001imAlmClientTxPowerHighWarning,
       "pm1001imAlmClientTxBiasLowWarning": pm1001imAlmClientTxBiasLowWarning,
       "pm1001imAlmClientTxBiasHighWarning": pm1001imAlmClientTxBiasHighWarning,
       "pm1001imAlmClientTempLowWarning": pm1001imAlmClientTempLowWarning,
       "pm1001imAlmClientTempHighWarning": pm1001imAlmClientTempHighWarning,
       "pm1001imAlmClientRxPowerLowWarning": pm1001imAlmClientRxPowerLowWarning,
       "pm1001imAlmClientRxPowerHighWarning": pm1001imAlmClientRxPowerHighWarning,
       "pm1001imAlmClientUrg": pm1001imAlmClientUrg,
       "pm1001imAlmclientXfpAlarm1": pm1001imAlmclientXfpAlarm1,
       "pm1001imAlmClientTxPowerLowAlarm": pm1001imAlmClientTxPowerLowAlarm,
       "pm1001imAlmClientTxPowerHighAlarm": pm1001imAlmClientTxPowerHighAlarm,
       "pm1001imAlmClientTxBiasLowAlarm": pm1001imAlmClientTxBiasLowAlarm,
       "pm1001imAlmClientTxBiasHighAlarm": pm1001imAlmClientTxBiasHighAlarm,
       "pm1001imAlmClientTempLowAlarm": pm1001imAlmClientTempLowAlarm,
       "pm1001imAlmClientTempHighAlarm": pm1001imAlmClientTempHighAlarm,
       "pm1001imAlmClientRxPowerLowAlarm": pm1001imAlmClientRxPowerLowAlarm,
       "pm1001imAlmClientRxPowerHighAlarm": pm1001imAlmClientRxPowerHighAlarm,
       "pm1001imAlmclientXfpSupplyAlarm": pm1001imAlmclientXfpSupplyAlarm,
       "pm1001imAlmClientVee5LowAlarm": pm1001imAlmClientVee5LowAlarm,
       "pm1001imAlmClientVee5HighAlarm": pm1001imAlmClientVee5HighAlarm,
       "pm1001imAlmClientVcc2LowAlarm": pm1001imAlmClientVcc2LowAlarm,
       "pm1001imAlmClientVcc2HighAlarm": pm1001imAlmClientVcc2HighAlarm,
       "pm1001imAlmClientVcc3LowAlarm": pm1001imAlmClientVcc3LowAlarm,
       "pm1001imAlmClientVcc3HighAlarm": pm1001imAlmClientVcc3HighAlarm,
       "pm1001imAlmClientVcc5LowAlarm": pm1001imAlmClientVcc5LowAlarm,
       "pm1001imAlmClientVcc5HighAlarm": pm1001imAlmClientVcc5HighAlarm,
       "pm1001imAlmClientVee5LowWarning": pm1001imAlmClientVee5LowWarning,
       "pm1001imAlmClientVee5HighWarning": pm1001imAlmClientVee5HighWarning,
       "pm1001imAlmClientVcc2LowWarning": pm1001imAlmClientVcc2LowWarning,
       "pm1001imAlmClientVcc2HighWarning": pm1001imAlmClientVcc2HighWarning,
       "pm1001imAlmClientVcc3LowWarning": pm1001imAlmClientVcc3LowWarning,
       "pm1001imAlmClientVcc3HighWarning": pm1001imAlmClientVcc3HighWarning,
       "pm1001imAlmClientVcc5LowWarning": pm1001imAlmClientVcc5LowWarning,
       "pm1001imAlmClientVcc5HighWarning": pm1001imAlmClientVcc5HighWarning,
       "pm1001imAlmClientCrit": pm1001imAlmClientCrit,
       "pm1001imAlmsynthAlmClient": pm1001imAlmsynthAlmClient,
       "pm1001imAlmClientXfpAbsent": pm1001imAlmClientXfpAbsent,
       "pm1001imAlmClientDdmAbsent": pm1001imAlmClientDdmAbsent,
       "pm1001imAlmClientHwFail": pm1001imAlmClientHwFail,
       "pm1001imAlmClientDwLsd": pm1001imAlmClientDwLsd,
       "pm1001imAlmClientLocalOos0": pm1001imAlmClientLocalOos0,
       "pm1001imAlmClientRemoteOos0": pm1001imAlmClientRemoteOos0,
       "pm1001imAlmClientDwCais": pm1001imAlmClientDwCais,
       "pm1001imAlmClientSfpDdmWarning": pm1001imAlmClientSfpDdmWarning,
       "pm1001imAlmClientSfpDdmAlm": pm1001imAlmClientSfpDdmAlm,
       "pm1001imAlmClientFail": pm1001imAlmClientFail,
       "pm1001imAlmClientUpCsf": pm1001imAlmClientUpCsf,
       "pm1001imAlmclientAccessioAlm": pm1001imAlmclientAccessioAlm,
       "pm1001imAlmClientDwLasFail": pm1001imAlmClientDwLasFail,
       "pm1001imAlmClientUpLos": pm1001imAlmClientUpLos,
       "pm1001imAlmclientMapperDeAlm": pm1001imAlmclientMapperDeAlm,
       "pm1001imAlmClientUpAccOos": pm1001imAlmClientUpAccOos,
       "pm1001imAlmClientUpBufferOvl": pm1001imAlmClientUpBufferOvl,
       "pm1001imAlmClientDwCsfDet": pm1001imAlmClientDwCsfDet,
       "pm1001imAlmClientDwBufferOvl": pm1001imAlmClientDwBufferOvl,
       "pm1001imAlmclientXfpAlarms2": pm1001imAlmclientXfpAlarms2,
       "pm1001imAlmClientModNr": pm1001imAlmClientModNr,
       "pm1001imAlmClientRxCdrNotLocked1": pm1001imAlmClientRxCdrNotLocked1,
       "pm1001imAlmClientRxNr": pm1001imAlmClientRxNr,
       "pm1001imAlmClientTxCdrNotLocked1": pm1001imAlmClientTxCdrNotLocked1,
       "pm1001imAlmClientTxFault": pm1001imAlmClientTxFault,
       "pm1001imAlmClientTxNr": pm1001imAlmClientTxNr,
       "pm1001imAlmClientWavelengthUnlocked": pm1001imAlmClientWavelengthUnlocked,
       "pm1001imAlmClientTecFault": pm1001imAlmClientTecFault,
       "pm1001imAlmClientApdSupplyFault": pm1001imAlmClientApdSupplyFault,
       "pm1001imAlmLine": pm1001imAlmLine,
       "pm1001imAlmLineNurg": pm1001imAlmLineNurg,
       "pm1001imAlmlineSfpWarnDdmTable": pm1001imAlmlineSfpWarnDdmTable,
       "pm1001imAlmlineSfpWarnDdmEntry": pm1001imAlmlineSfpWarnDdmEntry,
       "pm1001imAlmlineSfpWarnDdmIndex": pm1001imAlmlineSfpWarnDdmIndex,
       "pm1001imAlmLineTxPwrLowWngPortn": pm1001imAlmLineTxPwrLowWngPortn,
       "pm1001imAlmLineTxPwrHighWngPortn": pm1001imAlmLineTxPwrHighWngPortn,
       "pm1001imAlmLineTxBiasLowWngPortn": pm1001imAlmLineTxBiasLowWngPortn,
       "pm1001imAlmLineTxBiasHighWngPortn": pm1001imAlmLineTxBiasHighWngPortn,
       "pm1001imAlmLineVccLowWngPortn": pm1001imAlmLineVccLowWngPortn,
       "pm1001imAlmLineVccHighWngPortn": pm1001imAlmLineVccHighWngPortn,
       "pm1001imAlmLineTempLowWngPortn": pm1001imAlmLineTempLowWngPortn,
       "pm1001imAlmLineTempHighWngPortn": pm1001imAlmLineTempHighWngPortn,
       "pm1001imAlmLineRxPwrLowWngPortn": pm1001imAlmLineRxPwrLowWngPortn,
       "pm1001imAlmLineRxPwrHighWngPortn": pm1001imAlmLineRxPwrHighWngPortn,
       "pm1001imAlmlineDownS1Line1": pm1001imAlmlineDownS1Line1,
       "pm1001imAlmlineDownK1Line1": pm1001imAlmlineDownK1Line1,
       "pm1001imAlmlineDownK2Line1": pm1001imAlmlineDownK2Line1,
       "pm1001imAlmLineUrg": pm1001imAlmLineUrg,
       "pm1001imAlmlineSfpAlmDdmTable": pm1001imAlmlineSfpAlmDdmTable,
       "pm1001imAlmlineSfpAlmDdmEntry": pm1001imAlmlineSfpAlmDdmEntry,
       "pm1001imAlmlineSfpAlmDdmIndex": pm1001imAlmlineSfpAlmDdmIndex,
       "pm1001imAlmLineTxPwrLowAlaPortn": pm1001imAlmLineTxPwrLowAlaPortn,
       "pm1001imAlmLineTxPwrHighAlaPortn": pm1001imAlmLineTxPwrHighAlaPortn,
       "pm1001imAlmLineTxBiasLowAlaPortn": pm1001imAlmLineTxBiasLowAlaPortn,
       "pm1001imAlmLineTxBiasHighAlaPortn": pm1001imAlmLineTxBiasHighAlaPortn,
       "pm1001imAlmLineVccLowAlaPortn": pm1001imAlmLineVccLowAlaPortn,
       "pm1001imAlmLineVccHighAlaPortn": pm1001imAlmLineVccHighAlaPortn,
       "pm1001imAlmLineTempLowAlaPortn": pm1001imAlmLineTempLowAlaPortn,
       "pm1001imAlmLineTempHighAlaPortn": pm1001imAlmLineTempHighAlaPortn,
       "pm1001imAlmLineRxPwrLowAlaPortn": pm1001imAlmLineRxPwrLowAlaPortn,
       "pm1001imAlmLineRxPwrHighAlaPortn": pm1001imAlmLineRxPwrHighAlaPortn,
       "pm1001imAlmlineDfrmBer1": pm1001imAlmlineDfrmBer1,
       "pm1001imAlmLineSignalDegrade1": pm1001imAlmLineSignalDegrade1,
       "pm1001imAlmLineSignalFail1": pm1001imAlmLineSignalFail1,
       "pm1001imAlmLineDegrade1": pm1001imAlmLineDegrade1,
       "pm1001imAlmLineCrit": pm1001imAlmLineCrit,
       "pm1001imAlmsynthAlmLineTable": pm1001imAlmsynthAlmLineTable,
       "pm1001imAlmsynthAlmLineEntry": pm1001imAlmsynthAlmLineEntry,
       "pm1001imAlmsynthAlmLineIndex": pm1001imAlmsynthAlmLineIndex,
       "pm1001imAlmLineSfpAbsentPortn": pm1001imAlmLineSfpAbsentPortn,
       "pm1001imAlmLineDdmAbsentPortn": pm1001imAlmLineDdmAbsentPortn,
       "pm1001imAlmLineHwFailPortn": pm1001imAlmLineHwFailPortn,
       "pm1001imAlmLineUpLsdPortn": pm1001imAlmLineUpLsdPortn,
       "pm1001imAlmLineLocalOosPortn": pm1001imAlmLineLocalOosPortn,
       "pm1001imAlmLineUpRdiInsPortn": pm1001imAlmLineUpRdiInsPortn,
       "pm1001imAlmLineSfpDdmWarningPortn": pm1001imAlmLineSfpDdmWarningPortn,
       "pm1001imAlmLineSfpDdmAlmPortn": pm1001imAlmLineSfpDdmAlmPortn,
       "pm1001imAlmLineFailPortn": pm1001imAlmLineFailPortn,
       "pm1001imAlmlineAlmTable": pm1001imAlmlineAlmTable,
       "pm1001imAlmlineAlmEntry": pm1001imAlmlineAlmEntry,
       "pm1001imAlmlineAlmIndex": pm1001imAlmlineAlmIndex,
       "pm1001imAlmLineDwLasFailPortn": pm1001imAlmLineDwLasFailPortn,
       "pm1001imAlmLineUpLosPortn": pm1001imAlmLineUpLosPortn,
       "pm1001imAlmlineMapperDeAlmTable": pm1001imAlmlineMapperDeAlmTable,
       "pm1001imAlmlineMapperDeAlmEntry": pm1001imAlmlineMapperDeAlmEntry,
       "pm1001imAlmlineMapperDeAlmIndex": pm1001imAlmlineMapperDeAlmIndex,
       "pm1001imAlmLineDwLofPortn": pm1001imAlmLineDwLofPortn,
       "pm1001imAlmLineB1IndicPortn": pm1001imAlmLineB1IndicPortn,
       "pm1001imAlmLineLoopFifoFailPortn": pm1001imAlmLineLoopFifoFailPortn,
       "pm1001imAlmlineDfrmAlm1": pm1001imAlmlineDfrmAlm1,
       "pm1001imAlmDwAisDet1": pm1001imAlmDwAisDet1,
       "pm1001imAlmDwRdiDet1": pm1001imAlmDwRdiDet1,
       "pm1001imAlmDwOof1": pm1001imAlmDwOof1,
       "pm1001imAlmDwLof1": pm1001imAlmDwLof1,
       "pm1001imAlmlineSyncAlarms1": pm1001imAlmlineSyncAlarms1,
       "pm1001imAlmDwLockerr": pm1001imAlmDwLockerr,
       "pm1001imAlmUpLockerr": pm1001imAlmUpLockerr,
       "pm1001imAlmDwLos": pm1001imAlmDwLos,
       "pm1001immeasures": pm1001immeasures,
       "pm1001imMesrOther": pm1001imMesrOther,
       "pm1001imMesrsynth0": pm1001imMesrsynth0,
       "pm1001imMesrsynth1": pm1001imMesrsynth1,
       "pm1001imMesrClient": pm1001imMesrClient,
       "pm1001imMesrclientModTempMeas": pm1001imMesrclientModTempMeas,
       "pm1001imMesrclientReserved": pm1001imMesrclientReserved,
       "pm1001imMesrclientBiasCurrentMeas": pm1001imMesrclientBiasCurrentMeas,
       "pm1001imMesrclientTxPowerMeas": pm1001imMesrclientTxPowerMeas,
       "pm1001imMesrclientRxPowerMeas": pm1001imMesrclientRxPowerMeas,
       "pm1001imMesrclientAux1Meas": pm1001imMesrclientAux1Meas,
       "pm1001imMesrclientAux2Meas": pm1001imMesrclientAux2Meas,
       "pm1001imMesrLine": pm1001imMesrLine,
       "pm1001imMesrlineTempMeasTable": pm1001imMesrlineTempMeasTable,
       "pm1001imMesrlineTempMeasEntry": pm1001imMesrlineTempMeasEntry,
       "pm1001imMesrlineTempMeasIndex": pm1001imMesrlineTempMeasIndex,
       "pm1001imMesrlineTempMeasPortn": pm1001imMesrlineTempMeasPortn,
       "pm1001imMesrlineVoltMeasTable": pm1001imMesrlineVoltMeasTable,
       "pm1001imMesrlineVoltMeasEntry": pm1001imMesrlineVoltMeasEntry,
       "pm1001imMesrlineVoltMeasIndex": pm1001imMesrlineVoltMeasIndex,
       "pm1001imMesrlineVoltMeasPortn": pm1001imMesrlineVoltMeasPortn,
       "pm1001imMesrlineBiasMeasTable": pm1001imMesrlineBiasMeasTable,
       "pm1001imMesrlineBiasMeasEntry": pm1001imMesrlineBiasMeasEntry,
       "pm1001imMesrlineBiasMeasIndex": pm1001imMesrlineBiasMeasIndex,
       "pm1001imMesrlineBiasMeasPortn": pm1001imMesrlineBiasMeasPortn,
       "pm1001imMesrlineTxpwrMeasTable": pm1001imMesrlineTxpwrMeasTable,
       "pm1001imMesrlineTxpwrMeasEntry": pm1001imMesrlineTxpwrMeasEntry,
       "pm1001imMesrlineTxpwrMeasIndex": pm1001imMesrlineTxpwrMeasIndex,
       "pm1001imMesrlineTxpwrMeasPortn": pm1001imMesrlineTxpwrMeasPortn,
       "pm1001imMesrlineRxpwrMeasTable": pm1001imMesrlineRxpwrMeasTable,
       "pm1001imMesrlineRxpwrMeasEntry": pm1001imMesrlineRxpwrMeasEntry,
       "pm1001imMesrlineRxpwrMeasIndex": pm1001imMesrlineRxpwrMeasIndex,
       "pm1001imMesrlineRxpwrMeasPortn": pm1001imMesrlineRxpwrMeasPortn,
       "pm1001imcounters": pm1001imcounters,
       "pm1001imCntOther": pm1001imCntOther,
       "pm1001imCntClient": pm1001imCntClient,
       "pm1001imCntclientUpErrCntTable": pm1001imCntclientUpErrCntTable,
       "pm1001imCntclientUpErrCntEntry": pm1001imCntclientUpErrCntEntry,
       "pm1001imCntclientUpErrCntIndex": pm1001imCntclientUpErrCntIndex,
       "pm1001imCntclientUpErrCntValuePortn": pm1001imCntclientUpErrCntValuePortn,
       "pm1001imCntclientUpErrCntErrorPortn": pm1001imCntclientUpErrCntErrorPortn,
       "pm1001imCntclientUpErrCntOverloadPortn": pm1001imCntclientUpErrCntOverloadPortn,
       "pm1001imCntclientUpTimCntTable": pm1001imCntclientUpTimCntTable,
       "pm1001imCntclientUpTimCntEntry": pm1001imCntclientUpTimCntEntry,
       "pm1001imCntclientUpTimCntIndex": pm1001imCntclientUpTimCntIndex,
       "pm1001imCntclientUpTimCntValuePortn": pm1001imCntclientUpTimCntValuePortn,
       "pm1001imCntclientUpTimCntErrorPortn": pm1001imCntclientUpTimCntErrorPortn,
       "pm1001imCntclientUpTimCntOverloadPortn": pm1001imCntclientUpTimCntOverloadPortn,
       "pm1001imCntclientDwErrCntTable": pm1001imCntclientDwErrCntTable,
       "pm1001imCntclientDwErrCntEntry": pm1001imCntclientDwErrCntEntry,
       "pm1001imCntclientDwErrCntIndex": pm1001imCntclientDwErrCntIndex,
       "pm1001imCntclientDwErrCntValuePortn": pm1001imCntclientDwErrCntValuePortn,
       "pm1001imCntclientDwErrCntErrorPortn": pm1001imCntclientDwErrCntErrorPortn,
       "pm1001imCntclientDwErrCntOverloadPortn": pm1001imCntclientDwErrCntOverloadPortn,
       "pm1001imCntclientDwTimCntTable": pm1001imCntclientDwTimCntTable,
       "pm1001imCntclientDwTimCntEntry": pm1001imCntclientDwTimCntEntry,
       "pm1001imCntclientDwTimCntIndex": pm1001imCntclientDwTimCntIndex,
       "pm1001imCntclientDwTimCntValuePortn": pm1001imCntclientDwTimCntValuePortn,
       "pm1001imCntclientDwTimCntErrorPortn": pm1001imCntclientDwTimCntErrorPortn,
       "pm1001imCntclientDwTimCntOverloadPortn": pm1001imCntclientDwTimCntOverloadPortn,
       "pm1001imCntLine": pm1001imCntLine,
       "pm1001imCntdfrmB1ErrCntTable": pm1001imCntdfrmB1ErrCntTable,
       "pm1001imCntdfrmB1ErrCntEntry": pm1001imCntdfrmB1ErrCntEntry,
       "pm1001imCntdfrmB1ErrCntIndex": pm1001imCntdfrmB1ErrCntIndex,
       "pm1001imCntdfrmB1ErrCntValuePortn": pm1001imCntdfrmB1ErrCntValuePortn,
       "pm1001imCntdfrmB1ErrCntErrorPortn": pm1001imCntdfrmB1ErrCntErrorPortn,
       "pm1001imCntdfrmB1ErrCntOverloadPortn": pm1001imCntdfrmB1ErrCntOverloadPortn,
       "pm1001imCntdfrmTimCntTable": pm1001imCntdfrmTimCntTable,
       "pm1001imCntdfrmTimCntEntry": pm1001imCntdfrmTimCntEntry,
       "pm1001imCntdfrmTimCntIndex": pm1001imCntdfrmTimCntIndex,
       "pm1001imCntdfrmTimCntValuePortn": pm1001imCntdfrmTimCntValuePortn,
       "pm1001imCntdfrmTimCntErrorPortn": pm1001imCntdfrmTimCntErrorPortn,
       "pm1001imCntdfrmTimCntOverloadPortn": pm1001imCntdfrmTimCntOverloadPortn,
       "pm1001imCntCountersReset": pm1001imCntCountersReset,
       "pm1001imCntCountersStop": pm1001imCntCountersStop,
       "pm1001imcontrolsWrite": pm1001imcontrolsWrite,
       "pm1001imCtrlOther": pm1001imCtrlOther,
       "pm1001imCtrlconfMgnt1": pm1001imCtrlconfMgnt1,
       "pm1001imCtrlConf1Load1": pm1001imCtrlConf1Load1,
       "pm1001imCtrlConf2Load1": pm1001imCtrlConf2Load1,
       "pm1001imCtrlConf2Flash1": pm1001imCtrlConf2Flash1,
       "pm1001imCtrlConf2Clear1": pm1001imCtrlConf2Clear1,
       "pm1001imCtrlsynth4": pm1001imCtrlsynth4,
       "pm1001imCtrlCorrelatOn": pm1001imCtrlCorrelatOn,
       "pm1001imCtrlCorrelatOff": pm1001imCtrlCorrelatOff,
       "pm1001imCtrlswMgnt": pm1001imCtrlswMgnt,
       "pm1001imCtrlColdReset": pm1001imCtrlColdReset,
       "pm1001imCtrlWarmReset": pm1001imCtrlWarmReset,
       "pm1001imCtrlLoadSwBank1": pm1001imCtrlLoadSwBank1,
       "pm1001imCtrlLoadSwBank2": pm1001imCtrlLoadSwBank2,
       "pm1001imCtrlgwMgnt": pm1001imCtrlgwMgnt,
       "pm1001imCtrlCurrentGwReset": pm1001imCtrlCurrentGwReset,
       "pm1001imCtrlLoadGwBank1": pm1001imCtrlLoadGwBank1,
       "pm1001imCtrlLoadGwBank2": pm1001imCtrlLoadGwBank2,
       "pm1001imCtrlLoadGwBank3": pm1001imCtrlLoadGwBank3,
       "pm1001imCtrlLoadGwBank4": pm1001imCtrlLoadGwBank4,
       "pm1001imCtrlledTest": pm1001imCtrlledTest,
       "pm1001imCtrlGreenLed": pm1001imCtrlGreenLed,
       "pm1001imCtrlRedLed": pm1001imCtrlRedLed,
       "pm1001imCtrlLedOff": pm1001imCtrlLedOff,
       "pm1001imCtrlmoduleOosMode": pm1001imCtrlmoduleOosMode,
       "pm1001imCtrlModuleOosMode": pm1001imCtrlModuleOosMode,
       "pm1001imCtrlmaintenanceMode": pm1001imCtrlmaintenanceMode,
       "pm1001imCtrlMaintenanceMode": pm1001imCtrlMaintenanceMode,
       "pm1001imCtrldccEnable": pm1001imCtrldccEnable,
       "pm1001imCtrlDccEnable": pm1001imCtrlDccEnable,
       "pm1001imCtrlClient": pm1001imCtrlClient,
       "pm1001imCtrlaccessLoop": pm1001imCtrlaccessLoop,
       "pm1001imCtrlaccessLoopClient": pm1001imCtrlaccessLoopClient,
       "pm1001imCtrlportOosMode": pm1001imCtrlportOosMode,
       "pm1001imCtrlportOosModeClient": pm1001imCtrlportOosModeClient,
       "pm1001imCtrlclientXfpOff": pm1001imCtrlclientXfpOff,
       "pm1001imCtrlclientXfpOffClient": pm1001imCtrlclientXfpOffClient,
       "pm1001imCtrlcsfUpIns": pm1001imCtrlcsfUpIns,
       "pm1001imCtrlcsfUpInsClient": pm1001imCtrlcsfUpInsClient,
       "pm1001imCtrlcaisDwIns": pm1001imCtrlcaisDwIns,
       "pm1001imCtrlcaisDwInsClient": pm1001imCtrlcaisDwInsClient,
       "pm1001imCtrlLine": pm1001imCtrlLine,
       "pm1001imCtrllineLoop": pm1001imCtrllineLoop,
       "pm1001imCtrlLineLoop": pm1001imCtrlLineLoop,
       "pm1001imCtrllineMsAis": pm1001imCtrllineMsAis,
       "pm1001imCtrlMsAis": pm1001imCtrlMsAis,
       "pm1001imCtrllineUpS1": pm1001imCtrllineUpS1,
       "pm1001imCtrllineUpK1": pm1001imCtrllineUpK1,
       "pm1001imCtrllineUpK2": pm1001imCtrllineUpK2,
       "pm1001imCtrllineOosMode": pm1001imCtrllineOosMode,
       "pm1001imCtrllineOosModeAllLines": pm1001imCtrllineOosModeAllLines,
       "pm1001imCtrllineBandwidth": pm1001imCtrllineBandwidth,
       "pm1001imCtrllineOnoff": pm1001imCtrllineOnoff,
       "pm1001imCtrllineOnoffAllLines": pm1001imCtrllineOnoffAllLines,
       "pm1001imri": pm1001imri,
       "pm1001imriTable": pm1001imriTable,
       "pm1001imRinvLineTable": pm1001imRinvLineTable,
       "pm1001imRinvLineEntry": pm1001imRinvLineEntry,
       "pm1001imRinvLineIndex": pm1001imRinvLineIndex,
       "pm1001imRinvSfpLine": pm1001imRinvSfpLine,
       "pm1001imRinvReloadInventory": pm1001imRinvReloadInventory,
       "pm1001imRinvHwPlatform": pm1001imRinvHwPlatform,
       "pm1001imRinvModulePlatform": pm1001imRinvModulePlatform,
       "pm1001imRinvSwPlatform": pm1001imRinvSwPlatform,
       "pm1001imRinvGwPlatform": pm1001imRinvGwPlatform,
       "pm1001imRinvXfpClient": pm1001imRinvXfpClient,
       "pm1001imdownload": pm1001imdownload,
       "pm1001imDwlOther": pm1001imDwlOther,
       "pm1001imDwlrestartProcess": pm1001imDwlrestartProcess,
       "pm1001imDwlWarmRestartProcessed": pm1001imDwlWarmRestartProcessed,
       "pm1001imDwlColdRestartProcessed": pm1001imDwlColdRestartProcessed,
       "pm1001imDwlswBanksUsed": pm1001imDwlswBanksUsed,
       "pm1001imDwlSwBank1Used": pm1001imDwlSwBank1Used,
       "pm1001imDwlSwBank2Used": pm1001imDwlSwBank2Used,
       "pm1001imDwlSwBank1Notempty": pm1001imDwlSwBank1Notempty,
       "pm1001imDwlSwBank2Notempty": pm1001imDwlSwBank2Notempty,
       "pm1001imDwlgwBanksUsed": pm1001imDwlgwBanksUsed,
       "pm1001imDwlGwBank1Used": pm1001imDwlGwBank1Used,
       "pm1001imDwlGwBank2Used": pm1001imDwlGwBank2Used,
       "pm1001imDwlGwBank3Used": pm1001imDwlGwBank3Used,
       "pm1001imDwlGwBank4Used": pm1001imDwlGwBank4Used,
       "pm1001imDwlGwBank1Notempty": pm1001imDwlGwBank1Notempty,
       "pm1001imDwlGwBank2Notempty": pm1001imDwlGwBank2Notempty,
       "pm1001imDwlGwBank3Notempty": pm1001imDwlGwBank3Notempty,
       "pm1001imDwlGwBank4Notempty": pm1001imDwlGwBank4Notempty,
       "pm1001imDwlClient": pm1001imDwlClient,
       "pm1001imDwlLine": pm1001imDwlLine,
       "pm1001imrmon": pm1001imrmon,
       "pm1001imRmonOther": pm1001imRmonOther,
       "pm1001imMonCountersReset": pm1001imMonCountersReset,
       "pm1001imMonCountersStop": pm1001imMonCountersStop,
       "pm1001imRmonClient": pm1001imRmonClient,
       "pm1001imMonupRmonByteCntTable": pm1001imMonupRmonByteCntTable,
       "pm1001imMonupRmonByteCntEntry": pm1001imMonupRmonByteCntEntry,
       "pm1001imMonupRmonByteCntIndex": pm1001imMonupRmonByteCntIndex,
       "pm1001imMonupRmonByteCntValuePortn": pm1001imMonupRmonByteCntValuePortn,
       "pm1001imMonupRmonByteCntErrorPortn": pm1001imMonupRmonByteCntErrorPortn,
       "pm1001imMonupRmonByteCntOverloadPortn": pm1001imMonupRmonByteCntOverloadPortn,
       "pm1001imMonupRmonCrcErrorCntTable": pm1001imMonupRmonCrcErrorCntTable,
       "pm1001imMonupRmonCrcErrorCntEntry": pm1001imMonupRmonCrcErrorCntEntry,
       "pm1001imMonupRmonCrcErrorCntIndex": pm1001imMonupRmonCrcErrorCntIndex,
       "pm1001imMonupRmonCrcErrorCntValuePortn": pm1001imMonupRmonCrcErrorCntValuePortn,
       "pm1001imMonupRmonCrcErrorCntErrorPortn": pm1001imMonupRmonCrcErrorCntErrorPortn,
       "pm1001imMonupRmonCrcErrorCntOverloadPortn": pm1001imMonupRmonCrcErrorCntOverloadPortn,
       "pm1001imMonupRmonPacketsCntTable": pm1001imMonupRmonPacketsCntTable,
       "pm1001imMonupRmonPacketsCntEntry": pm1001imMonupRmonPacketsCntEntry,
       "pm1001imMonupRmonPacketsCntIndex": pm1001imMonupRmonPacketsCntIndex,
       "pm1001imMonupRmonPacketsCntValuePortn": pm1001imMonupRmonPacketsCntValuePortn,
       "pm1001imMonupRmonPacketsCntErrorPortn": pm1001imMonupRmonPacketsCntErrorPortn,
       "pm1001imMonupRmonPacketsCntOverloadPortn": pm1001imMonupRmonPacketsCntOverloadPortn,
       "pm1001imMonupRmonBroadcastCntTable": pm1001imMonupRmonBroadcastCntTable,
       "pm1001imMonupRmonBroadcastCntEntry": pm1001imMonupRmonBroadcastCntEntry,
       "pm1001imMonupRmonBroadcastCntIndex": pm1001imMonupRmonBroadcastCntIndex,
       "pm1001imMonupRmonBroadcastCntValuePortn": pm1001imMonupRmonBroadcastCntValuePortn,
       "pm1001imMonupRmonBroadcastCntErrorPortn": pm1001imMonupRmonBroadcastCntErrorPortn,
       "pm1001imMonupRmonBroadcastCntOverloadPortn": pm1001imMonupRmonBroadcastCntOverloadPortn,
       "pm1001imMonupRmonMulticastCntTable": pm1001imMonupRmonMulticastCntTable,
       "pm1001imMonupRmonMulticastCntEntry": pm1001imMonupRmonMulticastCntEntry,
       "pm1001imMonupRmonMulticastCntIndex": pm1001imMonupRmonMulticastCntIndex,
       "pm1001imMonupRmonMulticastCntValuePortn": pm1001imMonupRmonMulticastCntValuePortn,
       "pm1001imMonupRmonMulticastCntErrorPortn": pm1001imMonupRmonMulticastCntErrorPortn,
       "pm1001imMonupRmonMulticastCntOverloadPortn": pm1001imMonupRmonMulticastCntOverloadPortn,
       "pm1001imMonupRmonTimerCntTable": pm1001imMonupRmonTimerCntTable,
       "pm1001imMonupRmonTimerCntEntry": pm1001imMonupRmonTimerCntEntry,
       "pm1001imMonupRmonTimerCntIndex": pm1001imMonupRmonTimerCntIndex,
       "pm1001imMonupRmonTimerCntValuePortn": pm1001imMonupRmonTimerCntValuePortn,
       "pm1001imMonupRmonTimerCntErrorPortn": pm1001imMonupRmonTimerCntErrorPortn,
       "pm1001imMonupRmonTimerCntOverloadPortn": pm1001imMonupRmonTimerCntOverloadPortn,
       "pm1001imMonupRmonPauseFrameCntTable": pm1001imMonupRmonPauseFrameCntTable,
       "pm1001imMonupRmonPauseFrameCntEntry": pm1001imMonupRmonPauseFrameCntEntry,
       "pm1001imMonupRmonPauseFrameCntIndex": pm1001imMonupRmonPauseFrameCntIndex,
       "pm1001imMonupRmonPauseFrameCntValuePortn": pm1001imMonupRmonPauseFrameCntValuePortn,
       "pm1001imMonupRmonPauseFrameCntErrorPortn": pm1001imMonupRmonPauseFrameCntErrorPortn,
       "pm1001imMonupRmonPauseFrameCntOverloadPortn": pm1001imMonupRmonPauseFrameCntOverloadPortn,
       "pm1001imMonupRmonDropFrameCntTable": pm1001imMonupRmonDropFrameCntTable,
       "pm1001imMonupRmonDropFrameCntEntry": pm1001imMonupRmonDropFrameCntEntry,
       "pm1001imMonupRmonDropFrameCntIndex": pm1001imMonupRmonDropFrameCntIndex,
       "pm1001imMonupRmonDropFrameCntValuePortn": pm1001imMonupRmonDropFrameCntValuePortn,
       "pm1001imMonupRmonDropFrameCntErrorPortn": pm1001imMonupRmonDropFrameCntErrorPortn,
       "pm1001imMonupRmonDropFrameCntOverloadPortn": pm1001imMonupRmonDropFrameCntOverloadPortn,
       "pm1001imMonupRmonBitsCntTable": pm1001imMonupRmonBitsCntTable,
       "pm1001imMonupRmonBitsCntEntry": pm1001imMonupRmonBitsCntEntry,
       "pm1001imMonupRmonBitsCntIndex": pm1001imMonupRmonBitsCntIndex,
       "pm1001imMonupRmonBitsCntValuePortn": pm1001imMonupRmonBitsCntValuePortn,
       "pm1001imMonupRmonBitsCntErrorPortn": pm1001imMonupRmonBitsCntErrorPortn,
       "pm1001imMonupRmonBitsCntOverloadPortn": pm1001imMonupRmonBitsCntOverloadPortn,
       "pm1001imMondwRmonByteCntTable": pm1001imMondwRmonByteCntTable,
       "pm1001imMondwRmonByteCntEntry": pm1001imMondwRmonByteCntEntry,
       "pm1001imMondwRmonByteCntIndex": pm1001imMondwRmonByteCntIndex,
       "pm1001imMondwRmonByteCntValuePortn": pm1001imMondwRmonByteCntValuePortn,
       "pm1001imMondwRmonByteCntErrorPortn": pm1001imMondwRmonByteCntErrorPortn,
       "pm1001imMondwRmonByteCntOverloadPortn": pm1001imMondwRmonByteCntOverloadPortn,
       "pm1001imMondwRmonCrcErrorCntTable": pm1001imMondwRmonCrcErrorCntTable,
       "pm1001imMondwRmonCrcErrorCntEntry": pm1001imMondwRmonCrcErrorCntEntry,
       "pm1001imMondwRmonCrcErrorCntIndex": pm1001imMondwRmonCrcErrorCntIndex,
       "pm1001imMondwRmonCrcErrorCntValuePortn": pm1001imMondwRmonCrcErrorCntValuePortn,
       "pm1001imMondwRmonCrcErrorCntErrorPortn": pm1001imMondwRmonCrcErrorCntErrorPortn,
       "pm1001imMondwRmonCrcErrorCntOverloadPortn": pm1001imMondwRmonCrcErrorCntOverloadPortn,
       "pm1001imMondwRmonPacketsCntTable": pm1001imMondwRmonPacketsCntTable,
       "pm1001imMondwRmonPacketsCntEntry": pm1001imMondwRmonPacketsCntEntry,
       "pm1001imMondwRmonPacketsCntIndex": pm1001imMondwRmonPacketsCntIndex,
       "pm1001imMondwRmonPacketsCntValuePortn": pm1001imMondwRmonPacketsCntValuePortn,
       "pm1001imMondwRmonPacketsCntErrorPortn": pm1001imMondwRmonPacketsCntErrorPortn,
       "pm1001imMondwRmonPacketsCntOverloadPortn": pm1001imMondwRmonPacketsCntOverloadPortn,
       "pm1001imMondwRmonBroadcastCntTable": pm1001imMondwRmonBroadcastCntTable,
       "pm1001imMondwRmonBroadcastCntEntry": pm1001imMondwRmonBroadcastCntEntry,
       "pm1001imMondwRmonBroadcastCntIndex": pm1001imMondwRmonBroadcastCntIndex,
       "pm1001imMondwRmonBroadcastCntValuePortn": pm1001imMondwRmonBroadcastCntValuePortn,
       "pm1001imMondwRmonBroadcastCntErrorPortn": pm1001imMondwRmonBroadcastCntErrorPortn,
       "pm1001imMondwRmonBroadcastCntOverloadPortn": pm1001imMondwRmonBroadcastCntOverloadPortn,
       "pm1001imMondwRmonMulticastCntTable": pm1001imMondwRmonMulticastCntTable,
       "pm1001imMondwRmonMulticastCntEntry": pm1001imMondwRmonMulticastCntEntry,
       "pm1001imMondwRmonMulticastCntIndex": pm1001imMondwRmonMulticastCntIndex,
       "pm1001imMondwRmonMulticastCntValuePortn": pm1001imMondwRmonMulticastCntValuePortn,
       "pm1001imMondwRmonMulticastCntErrorPortn": pm1001imMondwRmonMulticastCntErrorPortn,
       "pm1001imMondwRmonMulticastCntOverloadPortn": pm1001imMondwRmonMulticastCntOverloadPortn,
       "pm1001imMondwRmonPauseFrameCntTable": pm1001imMondwRmonPauseFrameCntTable,
       "pm1001imMondwRmonPauseFrameCntEntry": pm1001imMondwRmonPauseFrameCntEntry,
       "pm1001imMondwRmonPauseFrameCntIndex": pm1001imMondwRmonPauseFrameCntIndex,
       "pm1001imMondwRmonPauseFrameCntValuePortn": pm1001imMondwRmonPauseFrameCntValuePortn,
       "pm1001imMondwRmonPauseFrameCntErrorPortn": pm1001imMondwRmonPauseFrameCntErrorPortn,
       "pm1001imMondwRmonPauseFrameCntOverloadPortn": pm1001imMondwRmonPauseFrameCntOverloadPortn,
       "pm1001imMondwRmonTimerCntTable": pm1001imMondwRmonTimerCntTable,
       "pm1001imMondwRmonTimerCntEntry": pm1001imMondwRmonTimerCntEntry,
       "pm1001imMondwRmonTimerCntIndex": pm1001imMondwRmonTimerCntIndex,
       "pm1001imMondwRmonTimerCntValuePortn": pm1001imMondwRmonTimerCntValuePortn,
       "pm1001imMondwRmonTimerCntErrorPortn": pm1001imMondwRmonTimerCntErrorPortn,
       "pm1001imMondwRmonTimerCntOverloadPortn": pm1001imMondwRmonTimerCntOverloadPortn,
       "pm1001imMondwRmonBitsCntTable": pm1001imMondwRmonBitsCntTable,
       "pm1001imMondwRmonBitsCntEntry": pm1001imMondwRmonBitsCntEntry,
       "pm1001imMondwRmonBitsCntIndex": pm1001imMondwRmonBitsCntIndex,
       "pm1001imMondwRmonBitsCntValuePortn": pm1001imMondwRmonBitsCntValuePortn,
       "pm1001imMondwRmonBitsCntErrorPortn": pm1001imMondwRmonBitsCntErrorPortn,
       "pm1001imMondwRmonBitsCntOverloadPortn": pm1001imMondwRmonBitsCntOverloadPortn,
       "pm1001imMonupRmonByteCntSTable": pm1001imMonupRmonByteCntSTable,
       "pm1001imMonupRmonByteCntSEntry": pm1001imMonupRmonByteCntSEntry,
       "pm1001imMonupRmonByteCntSIndex": pm1001imMonupRmonByteCntSIndex,
       "pm1001imMonupRmonByteCntSValuePortn": pm1001imMonupRmonByteCntSValuePortn,
       "pm1001imMonupRmonByteCntSErrorPortn": pm1001imMonupRmonByteCntSErrorPortn,
       "pm1001imMonupRmonByteCntSOverloadPortn": pm1001imMonupRmonByteCntSOverloadPortn,
       "pm1001imMonupRmonCrcErrorCntSTable": pm1001imMonupRmonCrcErrorCntSTable,
       "pm1001imMonupRmonCrcErrorCntSEntry": pm1001imMonupRmonCrcErrorCntSEntry,
       "pm1001imMonupRmonCrcErrorCntSIndex": pm1001imMonupRmonCrcErrorCntSIndex,
       "pm1001imMonupRmonCrcErrorCntSValuePortn": pm1001imMonupRmonCrcErrorCntSValuePortn,
       "pm1001imMonupRmonCrcErrorCntSErrorPortn": pm1001imMonupRmonCrcErrorCntSErrorPortn,
       "pm1001imMonupRmonCrcErrorCntSOverloadPortn": pm1001imMonupRmonCrcErrorCntSOverloadPortn,
       "pm1001imMonupRmonPacketsCntSTable": pm1001imMonupRmonPacketsCntSTable,
       "pm1001imMonupRmonPacketsCntSEntry": pm1001imMonupRmonPacketsCntSEntry,
       "pm1001imMonupRmonPacketsCntSIndex": pm1001imMonupRmonPacketsCntSIndex,
       "pm1001imMonupRmonPacketsCntSValuePortn": pm1001imMonupRmonPacketsCntSValuePortn,
       "pm1001imMonupRmonPacketsCntSErrorPortn": pm1001imMonupRmonPacketsCntSErrorPortn,
       "pm1001imMonupRmonPacketsCntSOverloadPortn": pm1001imMonupRmonPacketsCntSOverloadPortn,
       "pm1001imMonupRmonBroadcastCntSTable": pm1001imMonupRmonBroadcastCntSTable,
       "pm1001imMonupRmonBroadcastCntSEntry": pm1001imMonupRmonBroadcastCntSEntry,
       "pm1001imMonupRmonBroadcastCntSIndex": pm1001imMonupRmonBroadcastCntSIndex,
       "pm1001imMonupRmonBroadcastCntSValuePortn": pm1001imMonupRmonBroadcastCntSValuePortn,
       "pm1001imMonupRmonBroadcastCntSErrorPortn": pm1001imMonupRmonBroadcastCntSErrorPortn,
       "pm1001imMonupRmonBroadcastCntSOverloadPortn": pm1001imMonupRmonBroadcastCntSOverloadPortn,
       "pm1001imMonupRmonMulticastCntSTable": pm1001imMonupRmonMulticastCntSTable,
       "pm1001imMonupRmonMulticastCntSEntry": pm1001imMonupRmonMulticastCntSEntry,
       "pm1001imMonupRmonMulticastCntSIndex": pm1001imMonupRmonMulticastCntSIndex,
       "pm1001imMonupRmonMulticastCntSValuePortn": pm1001imMonupRmonMulticastCntSValuePortn,
       "pm1001imMonupRmonMulticastCntSErrorPortn": pm1001imMonupRmonMulticastCntSErrorPortn,
       "pm1001imMonupRmonMulticastCntSOverloadPortn": pm1001imMonupRmonMulticastCntSOverloadPortn,
       "pm1001imMonupRmonPauseFrameCntSTable": pm1001imMonupRmonPauseFrameCntSTable,
       "pm1001imMonupRmonPauseFrameCntSEntry": pm1001imMonupRmonPauseFrameCntSEntry,
       "pm1001imMonupRmonPauseFrameCntSIndex": pm1001imMonupRmonPauseFrameCntSIndex,
       "pm1001imMonupRmonPauseFrameCntSValuePortn": pm1001imMonupRmonPauseFrameCntSValuePortn,
       "pm1001imMonupRmonPauseFrameCntSErrorPortn": pm1001imMonupRmonPauseFrameCntSErrorPortn,
       "pm1001imMonupRmonPauseFrameCntSOverloadPortn": pm1001imMonupRmonPauseFrameCntSOverloadPortn,
       "pm1001imMonupRmonDropFrameCntSTable": pm1001imMonupRmonDropFrameCntSTable,
       "pm1001imMonupRmonDropFrameCntSEntry": pm1001imMonupRmonDropFrameCntSEntry,
       "pm1001imMonupRmonDropFrameCntSIndex": pm1001imMonupRmonDropFrameCntSIndex,
       "pm1001imMonupRmonDropFrameCntSValuePortn": pm1001imMonupRmonDropFrameCntSValuePortn,
       "pm1001imMonupRmonDropFrameCntSErrorPortn": pm1001imMonupRmonDropFrameCntSErrorPortn,
       "pm1001imMonupRmonDropFrameCntSOverloadPortn": pm1001imMonupRmonDropFrameCntSOverloadPortn,
       "pm1001imMonupRmonBitsCntSTable": pm1001imMonupRmonBitsCntSTable,
       "pm1001imMonupRmonBitsCntSEntry": pm1001imMonupRmonBitsCntSEntry,
       "pm1001imMonupRmonBitsCntSIndex": pm1001imMonupRmonBitsCntSIndex,
       "pm1001imMonupRmonBitsCntSValuePortn": pm1001imMonupRmonBitsCntSValuePortn,
       "pm1001imMonupRmonBitsCntSErrorPortn": pm1001imMonupRmonBitsCntSErrorPortn,
       "pm1001imMonupRmonBitsCntSOverloadPortn": pm1001imMonupRmonBitsCntSOverloadPortn,
       "pm1001imMondwRmonByteCntSTable": pm1001imMondwRmonByteCntSTable,
       "pm1001imMondwRmonByteCntSEntry": pm1001imMondwRmonByteCntSEntry,
       "pm1001imMondwRmonByteCntSIndex": pm1001imMondwRmonByteCntSIndex,
       "pm1001imMondwRmonByteCntSValuePortn": pm1001imMondwRmonByteCntSValuePortn,
       "pm1001imMondwRmonByteCntSErrorPortn": pm1001imMondwRmonByteCntSErrorPortn,
       "pm1001imMondwRmonByteCntSOverloadPortn": pm1001imMondwRmonByteCntSOverloadPortn,
       "pm1001imMondwRmonCrcErrorCntSTable": pm1001imMondwRmonCrcErrorCntSTable,
       "pm1001imMondwRmonCrcErrorCntSEntry": pm1001imMondwRmonCrcErrorCntSEntry,
       "pm1001imMondwRmonCrcErrorCntSIndex": pm1001imMondwRmonCrcErrorCntSIndex,
       "pm1001imMondwRmonCrcErrorCntSValuePortn": pm1001imMondwRmonCrcErrorCntSValuePortn,
       "pm1001imMondwRmonCrcErrorCntSErrorPortn": pm1001imMondwRmonCrcErrorCntSErrorPortn,
       "pm1001imMondwRmonCrcErrorCntSOverloadPortn": pm1001imMondwRmonCrcErrorCntSOverloadPortn,
       "pm1001imMondwRmonPacketsCntSTable": pm1001imMondwRmonPacketsCntSTable,
       "pm1001imMondwRmonPacketsCntSEntry": pm1001imMondwRmonPacketsCntSEntry,
       "pm1001imMondwRmonPacketsCntSIndex": pm1001imMondwRmonPacketsCntSIndex,
       "pm1001imMondwRmonPacketsCntSValuePortn": pm1001imMondwRmonPacketsCntSValuePortn,
       "pm1001imMondwRmonPacketsCntSErrorPortn": pm1001imMondwRmonPacketsCntSErrorPortn,
       "pm1001imMondwRmonPacketsCntSOverloadPortn": pm1001imMondwRmonPacketsCntSOverloadPortn,
       "pm1001imMondwRmonBroadcastCntSTable": pm1001imMondwRmonBroadcastCntSTable,
       "pm1001imMondwRmonBroadcastCntSEntry": pm1001imMondwRmonBroadcastCntSEntry,
       "pm1001imMondwRmonBroadcastCntSIndex": pm1001imMondwRmonBroadcastCntSIndex,
       "pm1001imMondwRmonBroadcastCntSValuePortn": pm1001imMondwRmonBroadcastCntSValuePortn,
       "pm1001imMondwRmonBroadcastCntSErrorPortn": pm1001imMondwRmonBroadcastCntSErrorPortn,
       "pm1001imMondwRmonBroadcastCntSOverloadPortn": pm1001imMondwRmonBroadcastCntSOverloadPortn,
       "pm1001imMondwRmonMulticastCntSTable": pm1001imMondwRmonMulticastCntSTable,
       "pm1001imMondwRmonMulticastCntSEntry": pm1001imMondwRmonMulticastCntSEntry,
       "pm1001imMondwRmonMulticastCntSIndex": pm1001imMondwRmonMulticastCntSIndex,
       "pm1001imMondwRmonMulticastCntSValuePortn": pm1001imMondwRmonMulticastCntSValuePortn,
       "pm1001imMondwRmonMulticastCntSErrorPortn": pm1001imMondwRmonMulticastCntSErrorPortn,
       "pm1001imMondwRmonMulticastCntSOverloadPortn": pm1001imMondwRmonMulticastCntSOverloadPortn,
       "pm1001imMondwRmonPauseFrameCntSTable": pm1001imMondwRmonPauseFrameCntSTable,
       "pm1001imMondwRmonPauseFrameCntSEntry": pm1001imMondwRmonPauseFrameCntSEntry,
       "pm1001imMondwRmonPauseFrameCntSIndex": pm1001imMondwRmonPauseFrameCntSIndex,
       "pm1001imMondwRmonPauseFrameCntSValuePortn": pm1001imMondwRmonPauseFrameCntSValuePortn,
       "pm1001imMondwRmonPauseFrameCntSErrorPortn": pm1001imMondwRmonPauseFrameCntSErrorPortn,
       "pm1001imMondwRmonPauseFrameCntSOverloadPortn": pm1001imMondwRmonPauseFrameCntSOverloadPortn,
       "pm1001imMondwRmonBitsCntSTable": pm1001imMondwRmonBitsCntSTable,
       "pm1001imMondwRmonBitsCntSEntry": pm1001imMondwRmonBitsCntSEntry,
       "pm1001imMondwRmonBitsCntSIndex": pm1001imMondwRmonBitsCntSIndex,
       "pm1001imMondwRmonBitsCntSValuePortn": pm1001imMondwRmonBitsCntSValuePortn,
       "pm1001imMondwRmonBitsCntSErrorPortn": pm1001imMondwRmonBitsCntSErrorPortn,
       "pm1001imMondwRmonBitsCntSOverloadPortn": pm1001imMondwRmonBitsCntSOverloadPortn,
       "pm1001imRmonLine": pm1001imRmonLine,
       "pm1001imConfig": pm1001imConfig,
       "pm1001imCfgAccessCAisCsf": pm1001imCfgAccessCAisCsf,
       "pm1001imCfgClientcaiscsfTable": pm1001imCfgClientcaiscsfTable,
       "pm1001imCfgClientcaiscsfEntry": pm1001imCfgClientcaiscsfEntry,
       "pm1001imCfgClientcaiscsfIndex": pm1001imCfgClientcaiscsfIndex,
       "pm1001imCfgCAisModePortn": pm1001imCfgCAisModePortn,
       "pm1001imCfgUpAccessioAlmPortn": pm1001imCfgUpAccessioAlmPortn,
       "pm1001imCfgUpMapperDeAlmPortn": pm1001imCfgUpMapperDeAlmPortn,
       "pm1001imCfgDownAccessioAlmPortn": pm1001imCfgDownAccessioAlmPortn,
       "pm1001imCfgDownMapperDeAlmPortn": pm1001imCfgDownMapperDeAlmPortn,
       "pm1001imCfgDownDfrmAlmPortn": pm1001imCfgDownDfrmAlmPortn,
       "pm1001imCfgDownLineSyncAlarmsPortn": pm1001imCfgDownLineSyncAlarmsPortn,
       "pm1001imCfgStartup": pm1001imCfgStartup,
       "pm1001imCfgClientStartupTable": pm1001imCfgClientStartupTable,
       "pm1001imCfgClientStartupEntry": pm1001imCfgClientStartupEntry,
       "pm1001imCfgClientStartupIndex": pm1001imCfgClientStartupIndex,
       "pm1001imCfgSystConfPortPortn": pm1001imCfgSystConfPortPortn,
       "pm1001imCfgNetConfPortPortn": pm1001imCfgNetConfPortPortn,
       "pm1001imtablelineStartup": pm1001imtablelineStartup,
       "pm1001imCfgsystConfLine1": pm1001imCfgsystConfLine1,
       "pm1001imCfglineBandwidth1": pm1001imCfglineBandwidth1,
       "pm1001imCfglineOptions1": pm1001imCfglineOptions1,
       "pm1001imCfgXfpTable": pm1001imCfgXfpTable,
       "pm1001imCfgXfpEntry": pm1001imCfgXfpEntry,
       "pm1001imCfgXfpIndex": pm1001imCfgXfpIndex,
       "pm1001imCfgSystConfXfpPortn": pm1001imCfgSystConfXfpPortn,
       "pm1001imCfgDataRateConfXfpPortn": pm1001imCfgDataRateConfXfpPortn,
       "pm1001imCfgLabels": pm1001imCfgLabels,
       "pm1001imCfgLabelclientTable": pm1001imCfgLabelclientTable,
       "pm1001imCfgLabelclientEntry": pm1001imCfgLabelclientEntry,
       "pm1001imCfgLabelclientIndex": pm1001imCfgLabelclientIndex,
       "pm1001imCfgLabelclientPortn": pm1001imCfgLabelclientPortn,
       "pm1001imCfgLabellineTable": pm1001imCfgLabellineTable,
       "pm1001imCfgLabellineEntry": pm1001imCfgLabellineEntry,
       "pm1001imCfgLabellineIndex": pm1001imCfgLabellineIndex,
       "pm1001imCfgLabellinePortn": pm1001imCfgLabellinePortn,
       "pm1001imCfgWriteConfiguration": pm1001imCfgWriteConfiguration,
       "pm1001imtraps": pm1001imtraps,
       "pm1001imtrapLineNumber": pm1001imtrapLineNumber,
       "pm1001imtrapBoardNumber": pm1001imtrapBoardNumber,
       "pm1001imLineTrapNotUrgentGoesOn": pm1001imLineTrapNotUrgentGoesOn,
       "pm1001imLineTrapNotUrgentGoesOff": pm1001imLineTrapNotUrgentGoesOff,
       "pm1001imLineTrapUrgentGoesOn": pm1001imLineTrapUrgentGoesOn,
       "pm1001imLineTrapUrgentGoesOff": pm1001imLineTrapUrgentGoesOff,
       "pm1001imLineTrapCritGoesOn": pm1001imLineTrapCritGoesOn,
       "pm1001imLineTrapCritGoesOff": pm1001imLineTrapCritGoesOff,
       "pm1001imClientTrapNotUrgentGoesOn": pm1001imClientTrapNotUrgentGoesOn,
       "pm1001imClientTrapNotUrgentGoesOff": pm1001imClientTrapNotUrgentGoesOff,
       "pm1001imClientTrapUrgentGoesOn": pm1001imClientTrapUrgentGoesOn,
       "pm1001imClientTrapUrgentGoesOff": pm1001imClientTrapUrgentGoesOff,
       "pm1001imClientTrapCritGoesOn": pm1001imClientTrapCritGoesOn,
       "pm1001imClientTrapCritGoesOff": pm1001imClientTrapCritGoesOff,
       "pm1001imPowerTrapUrgentGoesOn": pm1001imPowerTrapUrgentGoesOn,
       "pm1001imPowerTrapUrgentGoesOff": pm1001imPowerTrapUrgentGoesOff}
)
