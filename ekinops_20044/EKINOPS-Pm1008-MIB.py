# SNMP MIB module (EKINOPS-Pm1008-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1008-MIB.mib
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

modulePm1008 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3)
)
if mibBuilder.loadTexts:
    modulePm1008.setRevisions(
        ("2004-12-20 00:00",
         "2005-06-03 00:00",
         "2005-09-09 00:00",
         "2005-10-21 00:00",
         "2005-11-04 00:00",
         "2006-01-31 00:00",
         "2007-02-21 00:00",
         "2007-09-17 00:00",
         "2007-11-09 00:00",
         "2008-05-28 00:00",
         "2008-12-09 00:00",
         "2009-04-09 00:00",
         "2009-05-07 00:00",
         "2010-02-15 00:00",
         "2010-10-27 00:00",
         "2010-10-27 00:00",
         "2012-07-02 00:00",
         "2013-04-02 00:00",
         "2014-03-25 00:00",
         "2014-12-18 00:00",
         "2016-05-19 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1008MultiRate(TextualConvention, Integer32):
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
        *(("rate100Mhz", 0),
          ("rate250Mhz", 1),
          ("rate500Mhz", 2),
          ("rate1Ghz", 3))
    )



class Pm1008OtxMode(TextualConvention, Integer32):
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



class Pm1008OtxGrid(TextualConvention, Integer32):
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



class Pm1008AdjustValue(TextualConvention, Integer32):
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



class Pm1008OtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1008alarms_ObjectIdentity = ObjectIdentity
pm1008alarms = _Pm1008alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2)
)
_Pm1008AlmOther_ObjectIdentity = ObjectIdentity
pm1008AlmOther = _Pm1008AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1)
)
_Pm1008AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1008AlmOtherNurg = _Pm1008AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1)
)
_Pm1008AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1008AlmsynthAlm2 = _Pm1008AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1, 2)
)
_Pm1008AlmConfTableSave_Type = EkiOnOff
_Pm1008AlmConfTableSave_Object = MibScalar
pm1008AlmConfTableSave = _Pm1008AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1, 2, 1),
    _Pm1008AlmConfTableSave_Type()
)
pm1008AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmConfTableSave.setStatus("current")
_Pm1008AlmInvUpload_Type = EkiOnOff
_Pm1008AlmInvUpload_Object = MibScalar
pm1008AlmInvUpload = _Pm1008AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1, 2, 2),
    _Pm1008AlmInvUpload_Type()
)
pm1008AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmInvUpload.setStatus("current")
_Pm1008AlmConfTableLoad_Type = EkiOnOff
_Pm1008AlmConfTableLoad_Object = MibScalar
pm1008AlmConfTableLoad = _Pm1008AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1, 2, 3),
    _Pm1008AlmConfTableLoad_Type()
)
pm1008AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmConfTableLoad.setStatus("current")
_Pm1008AlmCorrelatOff_Type = EkiOnOff
_Pm1008AlmCorrelatOff_Object = MibScalar
pm1008AlmCorrelatOff = _Pm1008AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1, 2, 4),
    _Pm1008AlmCorrelatOff_Type()
)
pm1008AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmCorrelatOff.setStatus("current")
_Pm1008AlmMaintenanceOn_Type = EkiOnOff
_Pm1008AlmMaintenanceOn_Object = MibScalar
pm1008AlmMaintenanceOn = _Pm1008AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 1, 2, 5),
    _Pm1008AlmMaintenanceOn_Type()
)
pm1008AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmMaintenanceOn.setStatus("current")
_Pm1008AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1008AlmOtherUrg = _Pm1008AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2)
)
_Pm1008AlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1008AlmmodInitFailLevel2 = _Pm1008AlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 194)
)
_Pm1008AlmLedFail_Type = EkiOnOff
_Pm1008AlmLedFail_Object = MibScalar
pm1008AlmLedFail = _Pm1008AlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 194, 1),
    _Pm1008AlmLedFail_Type()
)
pm1008AlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLedFail.setStatus("current")
_Pm1008AlmNextColdBootForced_Type = EkiOnOff
_Pm1008AlmNextColdBootForced_Object = MibScalar
pm1008AlmNextColdBootForced = _Pm1008AlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 194, 2),
    _Pm1008AlmNextColdBootForced_Type()
)
pm1008AlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmNextColdBootForced.setStatus("current")
_Pm1008AlmBootUndone_Type = EkiOnOff
_Pm1008AlmBootUndone_Object = MibScalar
pm1008AlmBootUndone = _Pm1008AlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 194, 3),
    _Pm1008AlmBootUndone_Type()
)
pm1008AlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmBootUndone.setStatus("current")
_Pm1008AlmResetHwInitFail_Type = EkiOnOff
_Pm1008AlmResetHwInitFail_Object = MibScalar
pm1008AlmResetHwInitFail = _Pm1008AlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 194, 4),
    _Pm1008AlmResetHwInitFail_Type()
)
pm1008AlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmResetHwInitFail.setStatus("current")
_Pm1008AlmSwInitFail_Type = EkiOnOff
_Pm1008AlmSwInitFail_Object = MibScalar
pm1008AlmSwInitFail = _Pm1008AlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 194, 5),
    _Pm1008AlmSwInitFail_Type()
)
pm1008AlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmSwInitFail.setStatus("current")
_Pm1008AlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1008AlmmodInitFailLevel3 = _Pm1008AlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195)
)
_Pm1008AlmGwIdentFail_Type = EkiOnOff
_Pm1008AlmGwIdentFail_Object = MibScalar
pm1008AlmGwIdentFail = _Pm1008AlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 1),
    _Pm1008AlmGwIdentFail_Type()
)
pm1008AlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmGwIdentFail.setStatus("current")
_Pm1008AlmObmTypeReadFail_Type = EkiOnOff
_Pm1008AlmObmTypeReadFail_Object = MibScalar
pm1008AlmObmTypeReadFail = _Pm1008AlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 2),
    _Pm1008AlmObmTypeReadFail_Type()
)
pm1008AlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmObmTypeReadFail.setStatus("current")
_Pm1008AlmInitModuleFail_Type = EkiOnOff
_Pm1008AlmInitModuleFail_Object = MibScalar
pm1008AlmInitModuleFail = _Pm1008AlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 3),
    _Pm1008AlmInitModuleFail_Type()
)
pm1008AlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmInitModuleFail.setStatus("current")
_Pm1008AlmXfp1InitFail_Type = EkiOnOff
_Pm1008AlmXfp1InitFail_Object = MibScalar
pm1008AlmXfp1InitFail = _Pm1008AlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 5),
    _Pm1008AlmXfp1InitFail_Type()
)
pm1008AlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmXfp1InitFail.setStatus("current")
_Pm1008AlmXfp2InitFail_Type = EkiOnOff
_Pm1008AlmXfp2InitFail_Object = MibScalar
pm1008AlmXfp2InitFail = _Pm1008AlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 6),
    _Pm1008AlmXfp2InitFail_Type()
)
pm1008AlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmXfp2InitFail.setStatus("current")
_Pm1008AlmLine1InitFail_Type = EkiOnOff
_Pm1008AlmLine1InitFail_Object = MibScalar
pm1008AlmLine1InitFail = _Pm1008AlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 7),
    _Pm1008AlmLine1InitFail_Type()
)
pm1008AlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLine1InitFail.setStatus("current")
_Pm1008AlmLine2InitFail_Type = EkiOnOff
_Pm1008AlmLine2InitFail_Object = MibScalar
pm1008AlmLine2InitFail = _Pm1008AlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 8),
    _Pm1008AlmLine2InitFail_Type()
)
pm1008AlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLine2InitFail.setStatus("current")
_Pm1008AlmClient1InitFail_Type = EkiOnOff
_Pm1008AlmClient1InitFail_Object = MibScalar
pm1008AlmClient1InitFail = _Pm1008AlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 9),
    _Pm1008AlmClient1InitFail_Type()
)
pm1008AlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient1InitFail.setStatus("current")
_Pm1008AlmClient2InitFail_Type = EkiOnOff
_Pm1008AlmClient2InitFail_Object = MibScalar
pm1008AlmClient2InitFail = _Pm1008AlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 10),
    _Pm1008AlmClient2InitFail_Type()
)
pm1008AlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient2InitFail.setStatus("current")
_Pm1008AlmClient3InitFail_Type = EkiOnOff
_Pm1008AlmClient3InitFail_Object = MibScalar
pm1008AlmClient3InitFail = _Pm1008AlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 11),
    _Pm1008AlmClient3InitFail_Type()
)
pm1008AlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient3InitFail.setStatus("current")
_Pm1008AlmClient4InitFail_Type = EkiOnOff
_Pm1008AlmClient4InitFail_Object = MibScalar
pm1008AlmClient4InitFail = _Pm1008AlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 12),
    _Pm1008AlmClient4InitFail_Type()
)
pm1008AlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient4InitFail.setStatus("current")
_Pm1008AlmClient5InitFail_Type = EkiOnOff
_Pm1008AlmClient5InitFail_Object = MibScalar
pm1008AlmClient5InitFail = _Pm1008AlmClient5InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 13),
    _Pm1008AlmClient5InitFail_Type()
)
pm1008AlmClient5InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient5InitFail.setStatus("current")
_Pm1008AlmClient6InitFail_Type = EkiOnOff
_Pm1008AlmClient6InitFail_Object = MibScalar
pm1008AlmClient6InitFail = _Pm1008AlmClient6InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 14),
    _Pm1008AlmClient6InitFail_Type()
)
pm1008AlmClient6InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient6InitFail.setStatus("current")
_Pm1008AlmClient7InitFail_Type = EkiOnOff
_Pm1008AlmClient7InitFail_Object = MibScalar
pm1008AlmClient7InitFail = _Pm1008AlmClient7InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 15),
    _Pm1008AlmClient7InitFail_Type()
)
pm1008AlmClient7InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient7InitFail.setStatus("current")
_Pm1008AlmClient8InitFail_Type = EkiOnOff
_Pm1008AlmClient8InitFail_Object = MibScalar
pm1008AlmClient8InitFail = _Pm1008AlmClient8InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 2, 195, 16),
    _Pm1008AlmClient8InitFail_Type()
)
pm1008AlmClient8InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClient8InitFail.setStatus("current")
_Pm1008AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1008AlmOtherCrit = _Pm1008AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 3)
)
_Pm1008AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1008AlmsynthAlm0 = _Pm1008AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 3, 0)
)
_Pm1008AlmModGlobFail_Type = EkiOnOff
_Pm1008AlmModGlobFail_Object = MibScalar
pm1008AlmModGlobFail = _Pm1008AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 3, 0, 9),
    _Pm1008AlmModGlobFail_Type()
)
pm1008AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmModGlobFail.setStatus("current")
_Pm1008AlmDefFuseA_Type = EkiOnOff
_Pm1008AlmDefFuseA_Object = MibScalar
pm1008AlmDefFuseA = _Pm1008AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 3, 0, 15),
    _Pm1008AlmDefFuseA_Type()
)
pm1008AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDefFuseA.setStatus("current")
_Pm1008AlmDefFuseB_Type = EkiOnOff
_Pm1008AlmDefFuseB_Object = MibScalar
pm1008AlmDefFuseB = _Pm1008AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 1, 3, 0, 16),
    _Pm1008AlmDefFuseB_Type()
)
pm1008AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDefFuseB.setStatus("current")
_Pm1008AlmClient_ObjectIdentity = ObjectIdentity
pm1008AlmClient = _Pm1008AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2)
)
_Pm1008AlmClientNurg_ObjectIdentity = ObjectIdentity
pm1008AlmClientNurg = _Pm1008AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1)
)
_Pm1008AlmsfpWarnDdmTable_Object = MibTable
pm1008AlmsfpWarnDdmTable = _Pm1008AlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm1008AlmsfpWarnDdmTable.setStatus("current")
_Pm1008AlmsfpWarnDdmEntry_Object = MibTableRow
pm1008AlmsfpWarnDdmEntry = _Pm1008AlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1)
)
pm1008AlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmsfpWarnDdmEntry.setStatus("current")


class _Pm1008AlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1008AlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1008AlmsfpWarnDdmIndex_Object = MibTableColumn
pm1008AlmsfpWarnDdmIndex = _Pm1008AlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 1),
    _Pm1008AlmsfpWarnDdmIndex_Type()
)
pm1008AlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmsfpWarnDdmIndex.setStatus("current")
_Pm1008AlmTxPwLowWngPortn_Type = EkiOnOff
_Pm1008AlmTxPwLowWngPortn_Object = MibTableColumn
pm1008AlmTxPwLowWngPortn = _Pm1008AlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 2),
    _Pm1008AlmTxPwLowWngPortn_Type()
)
pm1008AlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPwLowWngPortn.setStatus("current")
_Pm1008AlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm1008AlmTxPwrHighWngPortn_Object = MibTableColumn
pm1008AlmTxPwrHighWngPortn = _Pm1008AlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 3),
    _Pm1008AlmTxPwrHighWngPortn_Type()
)
pm1008AlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPwrHighWngPortn.setStatus("current")
_Pm1008AlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm1008AlmTxBiasLowWngPortn_Object = MibTableColumn
pm1008AlmTxBiasLowWngPortn = _Pm1008AlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 4),
    _Pm1008AlmTxBiasLowWngPortn_Type()
)
pm1008AlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasLowWngPortn.setStatus("current")
_Pm1008AlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm1008AlmTxBiasHighWngPortn_Object = MibTableColumn
pm1008AlmTxBiasHighWngPortn = _Pm1008AlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 5),
    _Pm1008AlmTxBiasHighWngPortn_Type()
)
pm1008AlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasHighWngPortn.setStatus("current")
_Pm1008AlmVccLowWngPortn_Type = EkiOnOff
_Pm1008AlmVccLowWngPortn_Object = MibTableColumn
pm1008AlmVccLowWngPortn = _Pm1008AlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 6),
    _Pm1008AlmVccLowWngPortn_Type()
)
pm1008AlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVccLowWngPortn.setStatus("current")
_Pm1008AlmVccHighWngPortn_Type = EkiOnOff
_Pm1008AlmVccHighWngPortn_Object = MibTableColumn
pm1008AlmVccHighWngPortn = _Pm1008AlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 7),
    _Pm1008AlmVccHighWngPortn_Type()
)
pm1008AlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVccHighWngPortn.setStatus("current")
_Pm1008AlmTempLowWngPortn_Type = EkiOnOff
_Pm1008AlmTempLowWngPortn_Object = MibTableColumn
pm1008AlmTempLowWngPortn = _Pm1008AlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 8),
    _Pm1008AlmTempLowWngPortn_Type()
)
pm1008AlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempLowWngPortn.setStatus("current")
_Pm1008AlmTempHighWngPortn_Type = EkiOnOff
_Pm1008AlmTempHighWngPortn_Object = MibTableColumn
pm1008AlmTempHighWngPortn = _Pm1008AlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 9),
    _Pm1008AlmTempHighWngPortn_Type()
)
pm1008AlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempHighWngPortn.setStatus("current")
_Pm1008AlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm1008AlmRxPwrLowWngPortn_Object = MibTableColumn
pm1008AlmRxPwrLowWngPortn = _Pm1008AlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 16),
    _Pm1008AlmRxPwrLowWngPortn_Type()
)
pm1008AlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPwrLowWngPortn.setStatus("current")
_Pm1008AlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm1008AlmRxPwrHighWngPortn_Object = MibTableColumn
pm1008AlmRxPwrHighWngPortn = _Pm1008AlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 1, 48, 1, 17),
    _Pm1008AlmRxPwrHighWngPortn_Type()
)
pm1008AlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPwrHighWngPortn.setStatus("current")
_Pm1008AlmClientUrg_ObjectIdentity = ObjectIdentity
pm1008AlmClientUrg = _Pm1008AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2)
)
_Pm1008AlmsfpAlmDdmTable_Object = MibTable
pm1008AlmsfpAlmDdmTable = _Pm1008AlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm1008AlmsfpAlmDdmTable.setStatus("current")
_Pm1008AlmsfpAlmDdmEntry_Object = MibTableRow
pm1008AlmsfpAlmDdmEntry = _Pm1008AlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1)
)
pm1008AlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmsfpAlmDdmEntry.setStatus("current")


class _Pm1008AlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1008AlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1008AlmsfpAlmDdmIndex_Object = MibTableColumn
pm1008AlmsfpAlmDdmIndex = _Pm1008AlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 1),
    _Pm1008AlmsfpAlmDdmIndex_Type()
)
pm1008AlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmsfpAlmDdmIndex.setStatus("current")
_Pm1008AlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1008AlmTxPwrLowAlaPortn_Object = MibTableColumn
pm1008AlmTxPwrLowAlaPortn = _Pm1008AlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 2),
    _Pm1008AlmTxPwrLowAlaPortn_Type()
)
pm1008AlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPwrLowAlaPortn.setStatus("current")
_Pm1008AlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1008AlmTxPwrHighAlaPortn_Object = MibTableColumn
pm1008AlmTxPwrHighAlaPortn = _Pm1008AlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 3),
    _Pm1008AlmTxPwrHighAlaPortn_Type()
)
pm1008AlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPwrHighAlaPortn.setStatus("current")
_Pm1008AlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1008AlmTxBiasLowAlaPortn_Object = MibTableColumn
pm1008AlmTxBiasLowAlaPortn = _Pm1008AlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 4),
    _Pm1008AlmTxBiasLowAlaPortn_Type()
)
pm1008AlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasLowAlaPortn.setStatus("current")
_Pm1008AlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1008AlmTxBiasHighAlaPortn_Object = MibTableColumn
pm1008AlmTxBiasHighAlaPortn = _Pm1008AlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 5),
    _Pm1008AlmTxBiasHighAlaPortn_Type()
)
pm1008AlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasHighAlaPortn.setStatus("current")
_Pm1008AlmVccLowAlaPortn_Type = EkiOnOff
_Pm1008AlmVccLowAlaPortn_Object = MibTableColumn
pm1008AlmVccLowAlaPortn = _Pm1008AlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 6),
    _Pm1008AlmVccLowAlaPortn_Type()
)
pm1008AlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVccLowAlaPortn.setStatus("current")
_Pm1008AlmVccHighAlaPortn_Type = EkiOnOff
_Pm1008AlmVccHighAlaPortn_Object = MibTableColumn
pm1008AlmVccHighAlaPortn = _Pm1008AlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 7),
    _Pm1008AlmVccHighAlaPortn_Type()
)
pm1008AlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVccHighAlaPortn.setStatus("current")
_Pm1008AlmTempLowAlaPortn_Type = EkiOnOff
_Pm1008AlmTempLowAlaPortn_Object = MibTableColumn
pm1008AlmTempLowAlaPortn = _Pm1008AlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 8),
    _Pm1008AlmTempLowAlaPortn_Type()
)
pm1008AlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempLowAlaPortn.setStatus("current")
_Pm1008AlmTempHighAlaPortn_Type = EkiOnOff
_Pm1008AlmTempHighAlaPortn_Object = MibTableColumn
pm1008AlmTempHighAlaPortn = _Pm1008AlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 9),
    _Pm1008AlmTempHighAlaPortn_Type()
)
pm1008AlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempHighAlaPortn.setStatus("current")
_Pm1008AlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1008AlmRxPwrLowAlaPortn_Object = MibTableColumn
pm1008AlmRxPwrLowAlaPortn = _Pm1008AlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 16),
    _Pm1008AlmRxPwrLowAlaPortn_Type()
)
pm1008AlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPwrLowAlaPortn.setStatus("current")
_Pm1008AlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1008AlmRxPwrHighAlaPortn_Object = MibTableColumn
pm1008AlmRxPwrHighAlaPortn = _Pm1008AlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 2, 32, 1, 17),
    _Pm1008AlmRxPwrHighAlaPortn_Type()
)
pm1008AlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPwrHighAlaPortn.setStatus("current")
_Pm1008AlmClientCrit_ObjectIdentity = ObjectIdentity
pm1008AlmClientCrit = _Pm1008AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3)
)
_Pm1008AlmsynthAlmPortTable_Object = MibTable
pm1008AlmsynthAlmPortTable = _Pm1008AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1008AlmsynthAlmPortTable.setStatus("current")
_Pm1008AlmsynthAlmPortEntry_Object = MibTableRow
pm1008AlmsynthAlmPortEntry = _Pm1008AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1)
)
pm1008AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmsynthAlmPortEntry.setStatus("current")


class _Pm1008AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1008AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1008AlmsynthAlmPortIndex_Object = MibTableColumn
pm1008AlmsynthAlmPortIndex = _Pm1008AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 1),
    _Pm1008AlmsynthAlmPortIndex_Type()
)
pm1008AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmsynthAlmPortIndex.setStatus("current")
_Pm1008AlmSfpAbsentPortn_Type = EkiOnOff
_Pm1008AlmSfpAbsentPortn_Object = MibTableColumn
pm1008AlmSfpAbsentPortn = _Pm1008AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 2),
    _Pm1008AlmSfpAbsentPortn_Type()
)
pm1008AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmSfpAbsentPortn.setStatus("current")
_Pm1008AlmDdmAbsentPortn_Type = EkiOnOff
_Pm1008AlmDdmAbsentPortn_Object = MibTableColumn
pm1008AlmDdmAbsentPortn = _Pm1008AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 3),
    _Pm1008AlmDdmAbsentPortn_Type()
)
pm1008AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDdmAbsentPortn.setStatus("current")
_Pm1008AlmHwFailAccPortn_Type = EkiOnOff
_Pm1008AlmHwFailAccPortn_Object = MibTableColumn
pm1008AlmHwFailAccPortn = _Pm1008AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 5),
    _Pm1008AlmHwFailAccPortn_Type()
)
pm1008AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmHwFailAccPortn.setStatus("current")
_Pm1008AlmDwLsdPortn_Type = EkiOnOff
_Pm1008AlmDwLsdPortn_Object = MibTableColumn
pm1008AlmDwLsdPortn = _Pm1008AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 6),
    _Pm1008AlmDwLsdPortn_Type()
)
pm1008AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwLsdPortn.setStatus("current")
_Pm1008AlmClientLocalOosPortn_Type = EkiOnOff
_Pm1008AlmClientLocalOosPortn_Object = MibTableColumn
pm1008AlmClientLocalOosPortn = _Pm1008AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 7),
    _Pm1008AlmClientLocalOosPortn_Type()
)
pm1008AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClientLocalOosPortn.setStatus("current")
_Pm1008AlmClientRemoteOosPortn_Type = EkiOnOff
_Pm1008AlmClientRemoteOosPortn_Object = MibTableColumn
pm1008AlmClientRemoteOosPortn = _Pm1008AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 8),
    _Pm1008AlmClientRemoteOosPortn_Type()
)
pm1008AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmClientRemoteOosPortn.setStatus("current")
_Pm1008AlmDwCaisPortn_Type = EkiOnOff
_Pm1008AlmDwCaisPortn_Object = MibTableColumn
pm1008AlmDwCaisPortn = _Pm1008AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 9),
    _Pm1008AlmDwCaisPortn_Type()
)
pm1008AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwCaisPortn.setStatus("current")
_Pm1008AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm1008AlmSfpDdmWarningPortn_Object = MibTableColumn
pm1008AlmSfpDdmWarningPortn = _Pm1008AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 10),
    _Pm1008AlmSfpDdmWarningPortn_Type()
)
pm1008AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmSfpDdmWarningPortn.setStatus("current")
_Pm1008AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm1008AlmSfpDdmAlmPortn_Object = MibTableColumn
pm1008AlmSfpDdmAlmPortn = _Pm1008AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 11),
    _Pm1008AlmSfpDdmAlmPortn_Type()
)
pm1008AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmSfpDdmAlmPortn.setStatus("current")
_Pm1008AlmFailAccPortn_Type = EkiOnOff
_Pm1008AlmFailAccPortn_Object = MibTableColumn
pm1008AlmFailAccPortn = _Pm1008AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 13),
    _Pm1008AlmFailAccPortn_Type()
)
pm1008AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmFailAccPortn.setStatus("current")
_Pm1008AlmUpCsfPortn_Type = EkiOnOff
_Pm1008AlmUpCsfPortn_Object = MibTableColumn
pm1008AlmUpCsfPortn = _Pm1008AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 8, 1, 17),
    _Pm1008AlmUpCsfPortn_Type()
)
pm1008AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmUpCsfPortn.setStatus("current")
_Pm1008AlmaccessioAlmTable_Object = MibTable
pm1008AlmaccessioAlmTable = _Pm1008AlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1008AlmaccessioAlmTable.setStatus("current")
_Pm1008AlmaccessioAlmEntry_Object = MibTableRow
pm1008AlmaccessioAlmEntry = _Pm1008AlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 16, 1)
)
pm1008AlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmaccessioAlmEntry.setStatus("current")


class _Pm1008AlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1008AlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1008AlmaccessioAlmIndex_Object = MibTableColumn
pm1008AlmaccessioAlmIndex = _Pm1008AlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 16, 1, 1),
    _Pm1008AlmaccessioAlmIndex_Type()
)
pm1008AlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmaccessioAlmIndex.setStatus("current")
_Pm1008AlmDwLasFailPortn_Type = EkiOnOff
_Pm1008AlmDwLasFailPortn_Object = MibTableColumn
pm1008AlmDwLasFailPortn = _Pm1008AlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 16, 1, 2),
    _Pm1008AlmDwLasFailPortn_Type()
)
pm1008AlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwLasFailPortn.setStatus("current")
_Pm1008AlmUpLosPortn_Type = EkiOnOff
_Pm1008AlmUpLosPortn_Object = MibTableColumn
pm1008AlmUpLosPortn = _Pm1008AlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 16, 1, 5),
    _Pm1008AlmUpLosPortn_Type()
)
pm1008AlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmUpLosPortn.setStatus("current")
_Pm1008AlmmapperDeAlmTable_Object = MibTable
pm1008AlmmapperDeAlmTable = _Pm1008AlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1008AlmmapperDeAlmTable.setStatus("current")
_Pm1008AlmmapperDeAlmEntry_Object = MibTableRow
pm1008AlmmapperDeAlmEntry = _Pm1008AlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72, 1)
)
pm1008AlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmmapperDeAlmEntry.setStatus("current")


class _Pm1008AlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1008AlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1008AlmmapperDeAlmIndex_Object = MibTableColumn
pm1008AlmmapperDeAlmIndex = _Pm1008AlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72, 1, 1),
    _Pm1008AlmmapperDeAlmIndex_Type()
)
pm1008AlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmmapperDeAlmIndex.setStatus("current")
_Pm1008AlmUpAccOosPortn_Type = EkiOnOff
_Pm1008AlmUpAccOosPortn_Object = MibTableColumn
pm1008AlmUpAccOosPortn = _Pm1008AlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72, 1, 2),
    _Pm1008AlmUpAccOosPortn_Type()
)
pm1008AlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmUpAccOosPortn.setStatus("current")
_Pm1008AlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1008AlmUpBufferOvlPortn_Object = MibTableColumn
pm1008AlmUpBufferOvlPortn = _Pm1008AlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72, 1, 11),
    _Pm1008AlmUpBufferOvlPortn_Type()
)
pm1008AlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmUpBufferOvlPortn.setStatus("current")
_Pm1008AlmDwCsfDetPortn_Type = EkiOnOff
_Pm1008AlmDwCsfDetPortn_Object = MibTableColumn
pm1008AlmDwCsfDetPortn = _Pm1008AlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72, 1, 12),
    _Pm1008AlmDwCsfDetPortn_Type()
)
pm1008AlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwCsfDetPortn.setStatus("current")
_Pm1008AlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1008AlmDwBufferOvlPortn_Object = MibTableColumn
pm1008AlmDwBufferOvlPortn = _Pm1008AlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 2, 3, 72, 1, 15),
    _Pm1008AlmDwBufferOvlPortn_Type()
)
pm1008AlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwBufferOvlPortn.setStatus("current")
_Pm1008AlmLine_ObjectIdentity = ObjectIdentity
pm1008AlmLine = _Pm1008AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3)
)
_Pm1008AlmLineNurg_ObjectIdentity = ObjectIdentity
pm1008AlmLineNurg = _Pm1008AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1)
)
_Pm1008AlmlineXfp1WarningsTable_Object = MibTable
pm1008AlmlineXfp1WarningsTable = _Pm1008AlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1WarningsTable.setStatus("current")
_Pm1008AlmlineXfp1WarningsEntry_Object = MibTableRow
pm1008AlmlineXfp1WarningsEntry = _Pm1008AlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1)
)
pm1008AlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1008AlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1008AlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1008AlmlineXfp1WarningsIndex = _Pm1008AlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 1),
    _Pm1008AlmlineXfp1WarningsIndex_Type()
)
pm1008AlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1WarningsIndex.setStatus("current")
_Pm1008AlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1008AlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1008AlmTxPowerLowWarningPortn = _Pm1008AlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 2),
    _Pm1008AlmTxPowerLowWarningPortn_Type()
)
pm1008AlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPowerLowWarningPortn.setStatus("current")
_Pm1008AlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1008AlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1008AlmTxPowerHighWarningPortn = _Pm1008AlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 3),
    _Pm1008AlmTxPowerHighWarningPortn_Type()
)
pm1008AlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPowerHighWarningPortn.setStatus("current")
_Pm1008AlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1008AlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1008AlmTxBiasLowWarningPortn = _Pm1008AlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 4),
    _Pm1008AlmTxBiasLowWarningPortn_Type()
)
pm1008AlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasLowWarningPortn.setStatus("current")
_Pm1008AlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1008AlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1008AlmTxBiasHighWarningPortn = _Pm1008AlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 5),
    _Pm1008AlmTxBiasHighWarningPortn_Type()
)
pm1008AlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasHighWarningPortn.setStatus("current")
_Pm1008AlmTempLowWarningPortn_Type = EkiOnOff
_Pm1008AlmTempLowWarningPortn_Object = MibTableColumn
pm1008AlmTempLowWarningPortn = _Pm1008AlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 8),
    _Pm1008AlmTempLowWarningPortn_Type()
)
pm1008AlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempLowWarningPortn.setStatus("current")
_Pm1008AlmTempHighWarningPortn_Type = EkiOnOff
_Pm1008AlmTempHighWarningPortn_Object = MibTableColumn
pm1008AlmTempHighWarningPortn = _Pm1008AlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 9),
    _Pm1008AlmTempHighWarningPortn_Type()
)
pm1008AlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempHighWarningPortn.setStatus("current")
_Pm1008AlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1008AlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1008AlmRxPowerLowWarningPortn = _Pm1008AlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 16),
    _Pm1008AlmRxPowerLowWarningPortn_Type()
)
pm1008AlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPowerLowWarningPortn.setStatus("current")
_Pm1008AlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1008AlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1008AlmRxPowerHighWarningPortn = _Pm1008AlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 209, 1, 17),
    _Pm1008AlmRxPowerHighWarningPortn_Type()
)
pm1008AlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPowerHighWarningPortn.setStatus("current")
_Pm1008AlmlineOtx1TlhWarningsTable_Object = MibTable
pm1008AlmlineOtx1TlhWarningsTable = _Pm1008AlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1008AlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1008AlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1008AlmlineOtx1TlhWarningsEntry = _Pm1008AlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225, 1)
)
pm1008AlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1008AlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1008AlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1008AlmlineOtx1TlhWarningsIndex = _Pm1008AlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225, 1, 1),
    _Pm1008AlmlineOtx1TlhWarningsIndex_Type()
)
pm1008AlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1008AlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1008AlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1008AlmLineModulatorAgingHighWarningPortn = _Pm1008AlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225, 1, 6),
    _Pm1008AlmLineModulatorAgingHighWarningPortn_Type()
)
pm1008AlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1008AlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1008AlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1008AlmLineAgingHighWarningPortn = _Pm1008AlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225, 1, 7),
    _Pm1008AlmLineAgingHighWarningPortn_Type()
)
pm1008AlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineAgingHighWarningPortn.setStatus("current")
_Pm1008AlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1008AlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1008AlmLineFreqDevHighWarningPortn = _Pm1008AlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225, 1, 13),
    _Pm1008AlmLineFreqDevHighWarningPortn_Type()
)
pm1008AlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1008AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1008AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1008AlmLineLaserTempHighWarningPortn = _Pm1008AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 1, 225, 1, 15),
    _Pm1008AlmLineLaserTempHighWarningPortn_Type()
)
pm1008AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1008AlmLineUrg_ObjectIdentity = ObjectIdentity
pm1008AlmLineUrg = _Pm1008AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2)
)
_Pm1008AlmdfrmBerTable_Object = MibTable
pm1008AlmdfrmBerTable = _Pm1008AlmdfrmBerTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 129)
)
if mibBuilder.loadTexts:
    pm1008AlmdfrmBerTable.setStatus("current")
_Pm1008AlmdfrmBerEntry_Object = MibTableRow
pm1008AlmdfrmBerEntry = _Pm1008AlmdfrmBerEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 129, 1)
)
pm1008AlmdfrmBerEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmdfrmBerIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmdfrmBerEntry.setStatus("current")


class _Pm1008AlmdfrmBerIndex_Type(Integer32):
    """Custom type pm1008AlmdfrmBerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmdfrmBerIndex_Type.__name__ = "Integer32"
_Pm1008AlmdfrmBerIndex_Object = MibTableColumn
pm1008AlmdfrmBerIndex = _Pm1008AlmdfrmBerIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 129, 1, 1),
    _Pm1008AlmdfrmBerIndex_Type()
)
pm1008AlmdfrmBerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmdfrmBerIndex.setStatus("current")
_Pm1008AlmLineSignalDegradePortn_Type = EkiOnOff
_Pm1008AlmLineSignalDegradePortn_Object = MibTableColumn
pm1008AlmLineSignalDegradePortn = _Pm1008AlmLineSignalDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 129, 1, 2),
    _Pm1008AlmLineSignalDegradePortn_Type()
)
pm1008AlmLineSignalDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineSignalDegradePortn.setStatus("current")
_Pm1008AlmLineSignalFailPortn_Type = EkiOnOff
_Pm1008AlmLineSignalFailPortn_Object = MibTableColumn
pm1008AlmLineSignalFailPortn = _Pm1008AlmLineSignalFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 129, 1, 3),
    _Pm1008AlmLineSignalFailPortn_Type()
)
pm1008AlmLineSignalFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineSignalFailPortn.setStatus("current")
_Pm1008AlmLineDegradePortn_Type = EkiOnOff
_Pm1008AlmLineDegradePortn_Object = MibTableColumn
pm1008AlmLineDegradePortn = _Pm1008AlmLineDegradePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 129, 1, 6),
    _Pm1008AlmLineDegradePortn_Type()
)
pm1008AlmLineDegradePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineDegradePortn.setStatus("current")
_Pm1008AlmlineXfp1AlarmTable_Object = MibTable
pm1008AlmlineXfp1AlarmTable = _Pm1008AlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1AlarmTable.setStatus("current")
_Pm1008AlmlineXfp1AlarmEntry_Object = MibTableRow
pm1008AlmlineXfp1AlarmEntry = _Pm1008AlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1)
)
pm1008AlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1008AlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1008AlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1008AlmlineXfp1AlarmIndex = _Pm1008AlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 1),
    _Pm1008AlmlineXfp1AlarmIndex_Type()
)
pm1008AlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1AlarmIndex.setStatus("current")
_Pm1008AlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1008AlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1008AlmTxPowerLowAlarmPortn = _Pm1008AlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 2),
    _Pm1008AlmTxPowerLowAlarmPortn_Type()
)
pm1008AlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1008AlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1008AlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1008AlmTxPowerHighAlarmPortn = _Pm1008AlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 3),
    _Pm1008AlmTxPowerHighAlarmPortn_Type()
)
pm1008AlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1008AlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1008AlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1008AlmTxBiasLowAlarmPortn = _Pm1008AlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 4),
    _Pm1008AlmTxBiasLowAlarmPortn_Type()
)
pm1008AlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1008AlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1008AlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1008AlmTxBiasHighAlarmPortn = _Pm1008AlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 5),
    _Pm1008AlmTxBiasHighAlarmPortn_Type()
)
pm1008AlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1008AlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1008AlmTempLowAlarmPortn_Object = MibTableColumn
pm1008AlmTempLowAlarmPortn = _Pm1008AlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 8),
    _Pm1008AlmTempLowAlarmPortn_Type()
)
pm1008AlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempLowAlarmPortn.setStatus("current")
_Pm1008AlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1008AlmTempHighAlarmPortn_Object = MibTableColumn
pm1008AlmTempHighAlarmPortn = _Pm1008AlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 9),
    _Pm1008AlmTempHighAlarmPortn_Type()
)
pm1008AlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTempHighAlarmPortn.setStatus("current")
_Pm1008AlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1008AlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1008AlmRxPowerLowAlarmPortn = _Pm1008AlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 16),
    _Pm1008AlmRxPowerLowAlarmPortn_Type()
)
pm1008AlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1008AlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1008AlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1008AlmRxPowerHighAlarmPortn = _Pm1008AlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 208, 1, 17),
    _Pm1008AlmRxPowerHighAlarmPortn_Type()
)
pm1008AlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1008AlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1008AlmlineXfp1SupplyAlarmTable = _Pm1008AlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1008AlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1008AlmlineXfp1SupplyAlarmEntry = _Pm1008AlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1)
)
pm1008AlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1008AlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1008AlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1008AlmlineXfp1SupplyAlarmIndex = _Pm1008AlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 1),
    _Pm1008AlmlineXfp1SupplyAlarmIndex_Type()
)
pm1008AlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1008AlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1008AlmVee5LowAlarmPortn_Object = MibTableColumn
pm1008AlmVee5LowAlarmPortn = _Pm1008AlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 2),
    _Pm1008AlmVee5LowAlarmPortn_Type()
)
pm1008AlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVee5LowAlarmPortn.setStatus("current")
_Pm1008AlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1008AlmVee5HighAlarmPortn_Object = MibTableColumn
pm1008AlmVee5HighAlarmPortn = _Pm1008AlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 3),
    _Pm1008AlmVee5HighAlarmPortn_Type()
)
pm1008AlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVee5HighAlarmPortn.setStatus("current")
_Pm1008AlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1008AlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1008AlmVcc2LowAlarmPortn = _Pm1008AlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 4),
    _Pm1008AlmVcc2LowAlarmPortn_Type()
)
pm1008AlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc2LowAlarmPortn.setStatus("current")
_Pm1008AlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1008AlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1008AlmVcc2HighAlarmPortn = _Pm1008AlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 5),
    _Pm1008AlmVcc2HighAlarmPortn_Type()
)
pm1008AlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc2HighAlarmPortn.setStatus("current")
_Pm1008AlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1008AlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1008AlmVcc3LowAlarmPortn = _Pm1008AlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 6),
    _Pm1008AlmVcc3LowAlarmPortn_Type()
)
pm1008AlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc3LowAlarmPortn.setStatus("current")
_Pm1008AlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1008AlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1008AlmVcc3HighAlarmPortn = _Pm1008AlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 7),
    _Pm1008AlmVcc3HighAlarmPortn_Type()
)
pm1008AlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc3HighAlarmPortn.setStatus("current")
_Pm1008AlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1008AlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1008AlmVcc5LowAlarmPortn = _Pm1008AlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 8),
    _Pm1008AlmVcc5LowAlarmPortn_Type()
)
pm1008AlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc5LowAlarmPortn.setStatus("current")
_Pm1008AlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1008AlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1008AlmVcc5HighAlarmPortn = _Pm1008AlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 9),
    _Pm1008AlmVcc5HighAlarmPortn_Type()
)
pm1008AlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc5HighAlarmPortn.setStatus("current")
_Pm1008AlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1008AlmVee5LowWarningPortn_Object = MibTableColumn
pm1008AlmVee5LowWarningPortn = _Pm1008AlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 10),
    _Pm1008AlmVee5LowWarningPortn_Type()
)
pm1008AlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVee5LowWarningPortn.setStatus("current")
_Pm1008AlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1008AlmVee5HighWarningPortn_Object = MibTableColumn
pm1008AlmVee5HighWarningPortn = _Pm1008AlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 11),
    _Pm1008AlmVee5HighWarningPortn_Type()
)
pm1008AlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVee5HighWarningPortn.setStatus("current")
_Pm1008AlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1008AlmVcc2LowWarningPortn_Object = MibTableColumn
pm1008AlmVcc2LowWarningPortn = _Pm1008AlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 12),
    _Pm1008AlmVcc2LowWarningPortn_Type()
)
pm1008AlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc2LowWarningPortn.setStatus("current")
_Pm1008AlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1008AlmVcc2HighWarningPortn_Object = MibTableColumn
pm1008AlmVcc2HighWarningPortn = _Pm1008AlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 13),
    _Pm1008AlmVcc2HighWarningPortn_Type()
)
pm1008AlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc2HighWarningPortn.setStatus("current")
_Pm1008AlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1008AlmVcc3LowWarningPortn_Object = MibTableColumn
pm1008AlmVcc3LowWarningPortn = _Pm1008AlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 14),
    _Pm1008AlmVcc3LowWarningPortn_Type()
)
pm1008AlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc3LowWarningPortn.setStatus("current")
_Pm1008AlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1008AlmVcc3HighWarningPortn_Object = MibTableColumn
pm1008AlmVcc3HighWarningPortn = _Pm1008AlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 15),
    _Pm1008AlmVcc3HighWarningPortn_Type()
)
pm1008AlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc3HighWarningPortn.setStatus("current")
_Pm1008AlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1008AlmVcc5LowWarningPortn_Object = MibTableColumn
pm1008AlmVcc5LowWarningPortn = _Pm1008AlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 16),
    _Pm1008AlmVcc5LowWarningPortn_Type()
)
pm1008AlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc5LowWarningPortn.setStatus("current")
_Pm1008AlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1008AlmVcc5HighWarningPortn_Object = MibTableColumn
pm1008AlmVcc5HighWarningPortn = _Pm1008AlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 212, 1, 17),
    _Pm1008AlmVcc5HighWarningPortn_Type()
)
pm1008AlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmVcc5HighWarningPortn.setStatus("current")
_Pm1008AlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1008AlmlineOtx1TlhAlarmsTable = _Pm1008AlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1008AlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1008AlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1008AlmlineOtx1TlhAlarmsEntry = _Pm1008AlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224, 1)
)
pm1008AlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1008AlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1008AlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1008AlmlineOtx1TlhAlarmsIndex = _Pm1008AlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224, 1, 1),
    _Pm1008AlmlineOtx1TlhAlarmsIndex_Type()
)
pm1008AlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1008AlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1008AlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1008AlmLineModulatorAgingHighAlaPortn = _Pm1008AlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224, 1, 6),
    _Pm1008AlmLineModulatorAgingHighAlaPortn_Type()
)
pm1008AlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1008AlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1008AlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1008AlmLineAgingHighAlaPortn = _Pm1008AlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224, 1, 7),
    _Pm1008AlmLineAgingHighAlaPortn_Type()
)
pm1008AlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineAgingHighAlaPortn.setStatus("current")
_Pm1008AlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1008AlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1008AlmLineFreqDevHighAlaPortn = _Pm1008AlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224, 1, 13),
    _Pm1008AlmLineFreqDevHighAlaPortn_Type()
)
pm1008AlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1008AlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1008AlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1008AlmLineLaserTempHighAlaPortn = _Pm1008AlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 2, 224, 1, 15),
    _Pm1008AlmLineLaserTempHighAlaPortn_Type()
)
pm1008AlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1008AlmLineCrit_ObjectIdentity = ObjectIdentity
pm1008AlmLineCrit = _Pm1008AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3)
)
_Pm1008AlmsynthAlmLineTable_Object = MibTable
pm1008AlmsynthAlmLineTable = _Pm1008AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1008AlmsynthAlmLineTable.setStatus("current")
_Pm1008AlmsynthAlmLineEntry_Object = MibTableRow
pm1008AlmsynthAlmLineEntry = _Pm1008AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1)
)
pm1008AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmsynthAlmLineEntry.setStatus("current")


class _Pm1008AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1008AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1008AlmsynthAlmLineIndex_Object = MibTableColumn
pm1008AlmsynthAlmLineIndex = _Pm1008AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 1),
    _Pm1008AlmsynthAlmLineIndex_Type()
)
pm1008AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmsynthAlmLineIndex.setStatus("current")
_Pm1008AlmXfpAbsentPortn_Type = EkiOnOff
_Pm1008AlmXfpAbsentPortn_Object = MibTableColumn
pm1008AlmXfpAbsentPortn = _Pm1008AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 2),
    _Pm1008AlmXfpAbsentPortn_Type()
)
pm1008AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmXfpAbsentPortn.setStatus("current")
_Pm1008AlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1008AlmXfpInitNotComplPortn_Object = MibTableColumn
pm1008AlmXfpInitNotComplPortn = _Pm1008AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 3),
    _Pm1008AlmXfpInitNotComplPortn_Type()
)
pm1008AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmXfpInitNotComplPortn.setStatus("current")
_Pm1008AlmLineHwFailPortn_Type = EkiOnOff
_Pm1008AlmLineHwFailPortn_Object = MibTableColumn
pm1008AlmLineHwFailPortn = _Pm1008AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 5),
    _Pm1008AlmLineHwFailPortn_Type()
)
pm1008AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineHwFailPortn.setStatus("current")
_Pm1008AlmXfpTxOffPortn_Type = EkiOnOff
_Pm1008AlmXfpTxOffPortn_Object = MibTableColumn
pm1008AlmXfpTxOffPortn = _Pm1008AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 6),
    _Pm1008AlmXfpTxOffPortn_Type()
)
pm1008AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmXfpTxOffPortn.setStatus("current")
_Pm1008AlmLineLocalOosPortn_Type = EkiOnOff
_Pm1008AlmLineLocalOosPortn_Object = MibTableColumn
pm1008AlmLineLocalOosPortn = _Pm1008AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 7),
    _Pm1008AlmLineLocalOosPortn_Type()
)
pm1008AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineLocalOosPortn.setStatus("current")
_Pm1008AlmUpRdiInsPortn_Type = EkiOnOff
_Pm1008AlmUpRdiInsPortn_Object = MibTableColumn
pm1008AlmUpRdiInsPortn = _Pm1008AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 9),
    _Pm1008AlmUpRdiInsPortn_Type()
)
pm1008AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmUpRdiInsPortn.setStatus("current")
_Pm1008AlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1008AlmLineDdmWarningPortn_Object = MibTableColumn
pm1008AlmLineDdmWarningPortn = _Pm1008AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 10),
    _Pm1008AlmLineDdmWarningPortn_Type()
)
pm1008AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineDdmWarningPortn.setStatus("current")
_Pm1008AlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1008AlmLineDdmAlmPortn_Object = MibTableColumn
pm1008AlmLineDdmAlmPortn = _Pm1008AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 11),
    _Pm1008AlmLineDdmAlmPortn_Type()
)
pm1008AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineDdmAlmPortn.setStatus("current")
_Pm1008AlmLineFailPortn_Type = EkiOnOff
_Pm1008AlmLineFailPortn_Object = MibTableColumn
pm1008AlmLineFailPortn = _Pm1008AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 13),
    _Pm1008AlmLineFailPortn_Type()
)
pm1008AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineFailPortn.setStatus("current")
_Pm1008AlmLineActivePortn_Type = EkiOnOff
_Pm1008AlmLineActivePortn_Object = MibTableColumn
pm1008AlmLineActivePortn = _Pm1008AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 7, 1, 17),
    _Pm1008AlmLineActivePortn_Type()
)
pm1008AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmLineActivePortn.setStatus("current")
_Pm1008AlmdfrmAlmTable_Object = MibTable
pm1008AlmdfrmAlmTable = _Pm1008AlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1008AlmdfrmAlmTable.setStatus("current")
_Pm1008AlmdfrmAlmEntry_Object = MibTableRow
pm1008AlmdfrmAlmEntry = _Pm1008AlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1)
)
pm1008AlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmdfrmAlmEntry.setStatus("current")


class _Pm1008AlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1008AlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1008AlmdfrmAlmIndex_Object = MibTableColumn
pm1008AlmdfrmAlmIndex = _Pm1008AlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 1),
    _Pm1008AlmdfrmAlmIndex_Type()
)
pm1008AlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmdfrmAlmIndex.setStatus("current")
_Pm1008AlmDwAisDetPortn_Type = EkiOnOff
_Pm1008AlmDwAisDetPortn_Object = MibTableColumn
pm1008AlmDwAisDetPortn = _Pm1008AlmDwAisDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 2),
    _Pm1008AlmDwAisDetPortn_Type()
)
pm1008AlmDwAisDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwAisDetPortn.setStatus("current")
_Pm1008AlmDwRdiDetPortn_Type = EkiOnOff
_Pm1008AlmDwRdiDetPortn_Object = MibTableColumn
pm1008AlmDwRdiDetPortn = _Pm1008AlmDwRdiDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 3),
    _Pm1008AlmDwRdiDetPortn_Type()
)
pm1008AlmDwRdiDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwRdiDetPortn.setStatus("current")
_Pm1008AlmDwOofPortn_Type = EkiOnOff
_Pm1008AlmDwOofPortn_Object = MibTableColumn
pm1008AlmDwOofPortn = _Pm1008AlmDwOofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 4),
    _Pm1008AlmDwOofPortn_Type()
)
pm1008AlmDwOofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwOofPortn.setStatus("current")
_Pm1008AlmDwLofPortn_Type = EkiOnOff
_Pm1008AlmDwLofPortn_Object = MibTableColumn
pm1008AlmDwLofPortn = _Pm1008AlmDwLofPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 5),
    _Pm1008AlmDwLofPortn_Type()
)
pm1008AlmDwLofPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwLofPortn.setStatus("current")
_Pm1008AlmDccLoopbackPortn_Type = EkiOnOff
_Pm1008AlmDccLoopbackPortn_Object = MibTableColumn
pm1008AlmDccLoopbackPortn = _Pm1008AlmDccLoopbackPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 15),
    _Pm1008AlmDccLoopbackPortn_Type()
)
pm1008AlmDccLoopbackPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDccLoopbackPortn.setStatus("current")
_Pm1008AlmRxDccBroadStormPortn_Type = EkiOnOff
_Pm1008AlmRxDccBroadStormPortn_Object = MibTableColumn
pm1008AlmRxDccBroadStormPortn = _Pm1008AlmRxDccBroadStormPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 16),
    _Pm1008AlmRxDccBroadStormPortn_Type()
)
pm1008AlmRxDccBroadStormPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxDccBroadStormPortn.setStatus("current")
_Pm1008AlmTxDccBroadStormPortn_Type = EkiOnOff
_Pm1008AlmTxDccBroadStormPortn_Object = MibTableColumn
pm1008AlmTxDccBroadStormPortn = _Pm1008AlmTxDccBroadStormPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 128, 1, 17),
    _Pm1008AlmTxDccBroadStormPortn_Type()
)
pm1008AlmTxDccBroadStormPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxDccBroadStormPortn.setStatus("current")
_Pm1008AlmlineSyncAlarmsTable_Object = MibTable
pm1008AlmlineSyncAlarmsTable = _Pm1008AlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1008AlmlineSyncAlarmsTable.setStatus("current")
_Pm1008AlmlineSyncAlarmsEntry_Object = MibTableRow
pm1008AlmlineSyncAlarmsEntry = _Pm1008AlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 133, 1)
)
pm1008AlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1008AlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1008AlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1008AlmlineSyncAlarmsIndex = _Pm1008AlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 133, 1, 1),
    _Pm1008AlmlineSyncAlarmsIndex_Type()
)
pm1008AlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineSyncAlarmsIndex.setStatus("current")
_Pm1008AlmDwLockerrPortn_Type = EkiOnOff
_Pm1008AlmDwLockerrPortn_Object = MibTableColumn
pm1008AlmDwLockerrPortn = _Pm1008AlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 133, 1, 13),
    _Pm1008AlmDwLockerrPortn_Type()
)
pm1008AlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwLockerrPortn.setStatus("current")
_Pm1008AlmUpLockerrPortn_Type = EkiOnOff
_Pm1008AlmUpLockerrPortn_Object = MibTableColumn
pm1008AlmUpLockerrPortn = _Pm1008AlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 133, 1, 14),
    _Pm1008AlmUpLockerrPortn_Type()
)
pm1008AlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmUpLockerrPortn.setStatus("current")
_Pm1008AlmDwLosPortn_Type = EkiOnOff
_Pm1008AlmDwLosPortn_Object = MibTableColumn
pm1008AlmDwLosPortn = _Pm1008AlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 133, 1, 17),
    _Pm1008AlmDwLosPortn_Type()
)
pm1008AlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmDwLosPortn.setStatus("current")
_Pm1008AlmlineXfp1AlarmsTable_Object = MibTable
pm1008AlmlineXfp1AlarmsTable = _Pm1008AlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1AlarmsTable.setStatus("current")
_Pm1008AlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1008AlmlineXfp1AlarmsEntry = _Pm1008AlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1)
)
pm1008AlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008AlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1008AlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1008AlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008AlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1008AlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1008AlmlineXfp1AlarmsIndex = _Pm1008AlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 1),
    _Pm1008AlmlineXfp1AlarmsIndex_Type()
)
pm1008AlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1008AlmModNrPortn_Type = EkiOnOff
_Pm1008AlmModNrPortn_Object = MibTableColumn
pm1008AlmModNrPortn = _Pm1008AlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 3),
    _Pm1008AlmModNrPortn_Type()
)
pm1008AlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmModNrPortn.setStatus("current")
_Pm1008AlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1008AlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1008AlmRxCdrNotLockedPortn = _Pm1008AlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 4),
    _Pm1008AlmRxCdrNotLockedPortn_Type()
)
pm1008AlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxCdrNotLockedPortn.setStatus("current")
_Pm1008AlmRxNrPortn_Type = EkiOnOff
_Pm1008AlmRxNrPortn_Object = MibTableColumn
pm1008AlmRxNrPortn = _Pm1008AlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 6),
    _Pm1008AlmRxNrPortn_Type()
)
pm1008AlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmRxNrPortn.setStatus("current")
_Pm1008AlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1008AlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1008AlmTxCdrNotLockedPortn = _Pm1008AlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 7),
    _Pm1008AlmTxCdrNotLockedPortn_Type()
)
pm1008AlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxCdrNotLockedPortn.setStatus("current")
_Pm1008AlmTxFaultPortn_Type = EkiOnOff
_Pm1008AlmTxFaultPortn_Object = MibTableColumn
pm1008AlmTxFaultPortn = _Pm1008AlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 8),
    _Pm1008AlmTxFaultPortn_Type()
)
pm1008AlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxFaultPortn.setStatus("current")
_Pm1008AlmTxNrPortn_Type = EkiOnOff
_Pm1008AlmTxNrPortn_Object = MibTableColumn
pm1008AlmTxNrPortn = _Pm1008AlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 9),
    _Pm1008AlmTxNrPortn_Type()
)
pm1008AlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTxNrPortn.setStatus("current")
_Pm1008AlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1008AlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1008AlmWavelengthUnlockedPortn = _Pm1008AlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 15),
    _Pm1008AlmWavelengthUnlockedPortn_Type()
)
pm1008AlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmWavelengthUnlockedPortn.setStatus("current")
_Pm1008AlmTecFaultPortn_Type = EkiOnOff
_Pm1008AlmTecFaultPortn_Object = MibTableColumn
pm1008AlmTecFaultPortn = _Pm1008AlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 16),
    _Pm1008AlmTecFaultPortn_Type()
)
pm1008AlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmTecFaultPortn.setStatus("current")
_Pm1008AlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1008AlmApdSupplyFaultPortn_Object = MibTableColumn
pm1008AlmApdSupplyFaultPortn = _Pm1008AlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 2, 3, 3, 211, 1, 17),
    _Pm1008AlmApdSupplyFaultPortn_Type()
)
pm1008AlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008AlmApdSupplyFaultPortn.setStatus("current")
_Pm1008measures_ObjectIdentity = ObjectIdentity
pm1008measures = _Pm1008measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3)
)
_Pm1008MesrOther_ObjectIdentity = ObjectIdentity
pm1008MesrOther = _Pm1008MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 1)
)
_Pm1008Mesrsynth0_Type = EkiMeasureType
_Pm1008Mesrsynth0_Object = MibScalar
pm1008Mesrsynth0 = _Pm1008Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 1, 0),
    _Pm1008Mesrsynth0_Type()
)
pm1008Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrsynth0.setStatus("deprecated")
_Pm1008Mesrsynth1_Type = EkiMeasureType
_Pm1008Mesrsynth1_Object = MibScalar
pm1008Mesrsynth1 = _Pm1008Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 1, 1),
    _Pm1008Mesrsynth1_Type()
)
pm1008Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrsynth1.setStatus("deprecated")
_Pm1008MesrClient_ObjectIdentity = ObjectIdentity
pm1008MesrClient = _Pm1008MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2)
)
_Pm1008MesrtempMeasTable_Object = MibTable
pm1008MesrtempMeasTable = _Pm1008MesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm1008MesrtempMeasTable.setStatus("current")
_Pm1008MesrtempMeasEntry_Object = MibTableRow
pm1008MesrtempMeasEntry = _Pm1008MesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 16, 1)
)
pm1008MesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008MesrtempMeasEntry.setStatus("current")


class _Pm1008MesrtempMeasIndex_Type(Integer32):
    """Custom type pm1008MesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MesrtempMeasIndex_Type.__name__ = "Integer32"
_Pm1008MesrtempMeasIndex_Object = MibTableColumn
pm1008MesrtempMeasIndex = _Pm1008MesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 16, 1, 1),
    _Pm1008MesrtempMeasIndex_Type()
)
pm1008MesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrtempMeasIndex.setStatus("current")


class _Pm1008MesrtempMeasPortn_Type(Integer32):
    """Custom type pm1008MesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008MesrtempMeasPortn_Type.__name__ = "Integer32"
_Pm1008MesrtempMeasPortn_Object = MibTableColumn
pm1008MesrtempMeasPortn = _Pm1008MesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 16, 1, 2),
    _Pm1008MesrtempMeasPortn_Type()
)
pm1008MesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrtempMeasPortn.setStatus("current")
_Pm1008MesrvoltMeasTable_Object = MibTable
pm1008MesrvoltMeasTable = _Pm1008MesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm1008MesrvoltMeasTable.setStatus("current")
_Pm1008MesrvoltMeasEntry_Object = MibTableRow
pm1008MesrvoltMeasEntry = _Pm1008MesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 24, 1)
)
pm1008MesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008MesrvoltMeasEntry.setStatus("current")


class _Pm1008MesrvoltMeasIndex_Type(Integer32):
    """Custom type pm1008MesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pm1008MesrvoltMeasIndex_Object = MibTableColumn
pm1008MesrvoltMeasIndex = _Pm1008MesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 24, 1, 1),
    _Pm1008MesrvoltMeasIndex_Type()
)
pm1008MesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrvoltMeasIndex.setStatus("current")


class _Pm1008MesrvoltMeasPortn_Type(Integer32):
    """Custom type pm1008MesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008MesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pm1008MesrvoltMeasPortn_Object = MibTableColumn
pm1008MesrvoltMeasPortn = _Pm1008MesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 24, 1, 2),
    _Pm1008MesrvoltMeasPortn_Type()
)
pm1008MesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrvoltMeasPortn.setStatus("current")
_Pm1008MesrbiasMeasTable_Object = MibTable
pm1008MesrbiasMeasTable = _Pm1008MesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1008MesrbiasMeasTable.setStatus("current")
_Pm1008MesrbiasMeasEntry_Object = MibTableRow
pm1008MesrbiasMeasEntry = _Pm1008MesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 32, 1)
)
pm1008MesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008MesrbiasMeasEntry.setStatus("current")


class _Pm1008MesrbiasMeasIndex_Type(Integer32):
    """Custom type pm1008MesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pm1008MesrbiasMeasIndex_Object = MibTableColumn
pm1008MesrbiasMeasIndex = _Pm1008MesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 32, 1, 1),
    _Pm1008MesrbiasMeasIndex_Type()
)
pm1008MesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrbiasMeasIndex.setStatus("current")


class _Pm1008MesrbiasMeasPortn_Type(Integer32):
    """Custom type pm1008MesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008MesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pm1008MesrbiasMeasPortn_Object = MibTableColumn
pm1008MesrbiasMeasPortn = _Pm1008MesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 32, 1, 2),
    _Pm1008MesrbiasMeasPortn_Type()
)
pm1008MesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrbiasMeasPortn.setStatus("current")
_Pm1008MesrtxpwrMeasTable_Object = MibTable
pm1008MesrtxpwrMeasTable = _Pm1008MesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm1008MesrtxpwrMeasTable.setStatus("current")
_Pm1008MesrtxpwrMeasEntry_Object = MibTableRow
pm1008MesrtxpwrMeasEntry = _Pm1008MesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 40, 1)
)
pm1008MesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008MesrtxpwrMeasEntry.setStatus("current")


class _Pm1008MesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pm1008MesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1008MesrtxpwrMeasIndex_Object = MibTableColumn
pm1008MesrtxpwrMeasIndex = _Pm1008MesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 40, 1, 1),
    _Pm1008MesrtxpwrMeasIndex_Type()
)
pm1008MesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrtxpwrMeasIndex.setStatus("current")


class _Pm1008MesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pm1008MesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008MesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1008MesrtxpwrMeasPortn_Object = MibTableColumn
pm1008MesrtxpwrMeasPortn = _Pm1008MesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 40, 1, 2),
    _Pm1008MesrtxpwrMeasPortn_Type()
)
pm1008MesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrtxpwrMeasPortn.setStatus("current")
_Pm1008MesrrxpwrMeasTable_Object = MibTable
pm1008MesrrxpwrMeasTable = _Pm1008MesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm1008MesrrxpwrMeasTable.setStatus("current")
_Pm1008MesrrxpwrMeasEntry_Object = MibTableRow
pm1008MesrrxpwrMeasEntry = _Pm1008MesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 48, 1)
)
pm1008MesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008MesrrxpwrMeasEntry.setStatus("current")


class _Pm1008MesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pm1008MesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1008MesrrxpwrMeasIndex_Object = MibTableColumn
pm1008MesrrxpwrMeasIndex = _Pm1008MesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 48, 1, 1),
    _Pm1008MesrrxpwrMeasIndex_Type()
)
pm1008MesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrrxpwrMeasIndex.setStatus("current")


class _Pm1008MesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pm1008MesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008MesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1008MesrrxpwrMeasPortn_Object = MibTableColumn
pm1008MesrrxpwrMeasPortn = _Pm1008MesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 2, 48, 1, 2),
    _Pm1008MesrrxpwrMeasPortn_Type()
)
pm1008MesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MesrrxpwrMeasPortn.setStatus("current")
_Pm1008MesrLine_ObjectIdentity = ObjectIdentity
pm1008MesrLine = _Pm1008MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3)
)
_Pm1008Mesrxfp1LxModTempMeasTable_Object = MibTable
pm1008Mesrxfp1LxModTempMeasTable = _Pm1008Mesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1008Mesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1008Mesrxfp1LxModTempMeasEntry = _Pm1008Mesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 208, 1)
)
pm1008Mesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1008Mesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1008Mesrxfp1LxModTempMeasIndex = _Pm1008Mesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 208, 1, 1),
    _Pm1008Mesrxfp1LxModTempMeasIndex_Type()
)
pm1008Mesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1008Mesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1008Mesrxfp1LxModTempMeasPortn = _Pm1008Mesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 208, 1, 2),
    _Pm1008Mesrxfp1LxModTempMeasPortn_Type()
)
pm1008Mesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1008Mesrxfp1ReservedTable_Object = MibTable
pm1008Mesrxfp1ReservedTable = _Pm1008Mesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1ReservedTable.setStatus("deprecated")
_Pm1008Mesrxfp1ReservedEntry_Object = MibTableRow
pm1008Mesrxfp1ReservedEntry = _Pm1008Mesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 209, 1)
)
pm1008Mesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1008Mesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1ReservedIndex_Object = MibTableColumn
pm1008Mesrxfp1ReservedIndex = _Pm1008Mesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 209, 1, 1),
    _Pm1008Mesrxfp1ReservedIndex_Type()
)
pm1008Mesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1008Mesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1ReservedPortn_Object = MibTableColumn
pm1008Mesrxfp1ReservedPortn = _Pm1008Mesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 209, 1, 2),
    _Pm1008Mesrxfp1ReservedPortn_Type()
)
pm1008Mesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1008Mesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1008Mesrxfp1LoBiasCurrentMeasTable = _Pm1008Mesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1008Mesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1008Mesrxfp1LoBiasCurrentMeasEntry = _Pm1008Mesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 210, 1)
)
pm1008Mesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1008Mesrxfp1LoBiasCurrentMeasIndex = _Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 210, 1, 1),
    _Pm1008Mesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1008Mesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1008Mesrxfp1LoBiasCurrentMeasPortn = _Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 210, 1, 2),
    _Pm1008Mesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1008Mesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1008Mesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1008Mesrxfp1LoTxPowerMeasTable = _Pm1008Mesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1008Mesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1008Mesrxfp1LoTxPowerMeasEntry = _Pm1008Mesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 211, 1)
)
pm1008Mesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1008Mesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1008Mesrxfp1LoTxPowerMeasIndex = _Pm1008Mesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 211, 1, 1),
    _Pm1008Mesrxfp1LoTxPowerMeasIndex_Type()
)
pm1008Mesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1008Mesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1008Mesrxfp1LoTxPowerMeasPortn = _Pm1008Mesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 211, 1, 2),
    _Pm1008Mesrxfp1LoTxPowerMeasPortn_Type()
)
pm1008Mesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1008Mesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1008Mesrxfp1LiRxPowerMeasTable = _Pm1008Mesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1008Mesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1008Mesrxfp1LiRxPowerMeasEntry = _Pm1008Mesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 212, 1)
)
pm1008Mesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1008Mesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1008Mesrxfp1LiRxPowerMeasIndex = _Pm1008Mesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 212, 1, 1),
    _Pm1008Mesrxfp1LiRxPowerMeasIndex_Type()
)
pm1008Mesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1008Mesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1008Mesrxfp1LiRxPowerMeasPortn = _Pm1008Mesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 212, 1, 2),
    _Pm1008Mesrxfp1LiRxPowerMeasPortn_Type()
)
pm1008Mesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1008Mesrxfp1LxAux1MeasTable_Object = MibTable
pm1008Mesrxfp1LxAux1MeasTable = _Pm1008Mesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1008Mesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1008Mesrxfp1LxAux1MeasEntry = _Pm1008Mesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 213, 1)
)
pm1008Mesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1008Mesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1008Mesrxfp1LxAux1MeasIndex = _Pm1008Mesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 213, 1, 1),
    _Pm1008Mesrxfp1LxAux1MeasIndex_Type()
)
pm1008Mesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1008Mesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1008Mesrxfp1LxAux1MeasPortn = _Pm1008Mesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 213, 1, 2),
    _Pm1008Mesrxfp1LxAux1MeasPortn_Type()
)
pm1008Mesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1008Mesrxfp1LxAux2MeasTable_Object = MibTable
pm1008Mesrxfp1LxAux2MeasTable = _Pm1008Mesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1008Mesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1008Mesrxfp1LxAux2MeasEntry = _Pm1008Mesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 214, 1)
)
pm1008Mesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1008Mesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1008Mesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1008Mesrxfp1LxAux2MeasIndex = _Pm1008Mesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 214, 1, 1),
    _Pm1008Mesrxfp1LxAux2MeasIndex_Type()
)
pm1008Mesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1008Mesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1008Mesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1008Mesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1008Mesrxfp1LxAux2MeasPortn = _Pm1008Mesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 214, 1, 2),
    _Pm1008Mesrxfp1LxAux2MeasPortn_Type()
)
pm1008Mesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1008Mesrotx1AgingTable_Object = MibTable
pm1008Mesrotx1AgingTable = _Pm1008Mesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1AgingTable.setStatus("current")
_Pm1008Mesrotx1AgingEntry_Object = MibTableRow
pm1008Mesrotx1AgingEntry = _Pm1008Mesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 224, 1)
)
pm1008Mesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1AgingEntry.setStatus("current")


class _Pm1008Mesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1008Mesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1008Mesrotx1AgingIndex_Object = MibTableColumn
pm1008Mesrotx1AgingIndex = _Pm1008Mesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 224, 1, 1),
    _Pm1008Mesrotx1AgingIndex_Type()
)
pm1008Mesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1AgingIndex.setStatus("current")


class _Pm1008Mesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1008Mesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1008Mesrotx1AgingPortn_Object = MibTableColumn
pm1008Mesrotx1AgingPortn = _Pm1008Mesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 224, 1, 2),
    _Pm1008Mesrotx1AgingPortn_Type()
)
pm1008Mesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1AgingPortn.setStatus("current")
_Pm1008Mesrotx1LaserTemperatureTable_Object = MibTable
pm1008Mesrotx1LaserTemperatureTable = _Pm1008Mesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1008Mesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1008Mesrotx1LaserTemperatureEntry = _Pm1008Mesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 225, 1)
)
pm1008Mesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1008Mesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1008Mesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1008Mesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1008Mesrotx1LaserTemperatureIndex = _Pm1008Mesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 225, 1, 1),
    _Pm1008Mesrotx1LaserTemperatureIndex_Type()
)
pm1008Mesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1008Mesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1008Mesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1008Mesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1008Mesrotx1LaserTemperaturePortn = _Pm1008Mesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 225, 1, 2),
    _Pm1008Mesrotx1LaserTemperaturePortn_Type()
)
pm1008Mesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1008Mesrotx1FreqDeviationTable_Object = MibTable
pm1008Mesrotx1FreqDeviationTable = _Pm1008Mesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1FreqDeviationTable.setStatus("current")
_Pm1008Mesrotx1FreqDeviationEntry_Object = MibTableRow
pm1008Mesrotx1FreqDeviationEntry = _Pm1008Mesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 226, 1)
)
pm1008Mesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1008Mesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1008Mesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1008Mesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1008Mesrotx1FreqDeviationIndex = _Pm1008Mesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 226, 1, 1),
    _Pm1008Mesrotx1FreqDeviationIndex_Type()
)
pm1008Mesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1008Mesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1008Mesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1008Mesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1008Mesrotx1FreqDeviationPortn = _Pm1008Mesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 226, 1, 2),
    _Pm1008Mesrotx1FreqDeviationPortn_Type()
)
pm1008Mesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1FreqDeviationPortn.setStatus("current")
_Pm1008Mesrotx1LaserWvlengthTable_Object = MibTable
pm1008Mesrotx1LaserWvlengthTable = _Pm1008Mesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserWvlengthTable.setStatus("current")
_Pm1008Mesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1008Mesrotx1LaserWvlengthEntry = _Pm1008Mesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 227, 1)
)
pm1008Mesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008Mesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1008Mesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1008Mesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008Mesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1008Mesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1008Mesrotx1LaserWvlengthIndex = _Pm1008Mesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 227, 1, 1),
    _Pm1008Mesrotx1LaserWvlengthIndex_Type()
)
pm1008Mesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1008Mesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1008Mesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1008Mesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1008Mesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1008Mesrotx1LaserWvlengthPortn = _Pm1008Mesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 3, 3, 227, 1, 2),
    _Pm1008Mesrotx1LaserWvlengthPortn_Type()
)
pm1008Mesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Mesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1008counters_ObjectIdentity = ObjectIdentity
pm1008counters = _Pm1008counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4)
)
_Pm1008CntOther_ObjectIdentity = ObjectIdentity
pm1008CntOther = _Pm1008CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 1)
)
_Pm1008CntClient_ObjectIdentity = ObjectIdentity
pm1008CntClient = _Pm1008CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2)
)
_Pm1008CntupRaRemCntTable_Object = MibTable
pm1008CntupRaRemCntTable = _Pm1008CntupRaRemCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 16)
)
if mibBuilder.loadTexts:
    pm1008CntupRaRemCntTable.setStatus("current")
_Pm1008CntupRaRemCntEntry_Object = MibTableRow
pm1008CntupRaRemCntEntry = _Pm1008CntupRaRemCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 16, 1)
)
pm1008CntupRaRemCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntupRaRemCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntupRaRemCntEntry.setStatus("current")


class _Pm1008CntupRaRemCntIndex_Type(Integer32):
    """Custom type pm1008CntupRaRemCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntupRaRemCntIndex_Type.__name__ = "Integer32"
_Pm1008CntupRaRemCntIndex_Object = MibTableColumn
pm1008CntupRaRemCntIndex = _Pm1008CntupRaRemCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 16, 1, 1),
    _Pm1008CntupRaRemCntIndex_Type()
)
pm1008CntupRaRemCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaRemCntIndex.setStatus("current")
_Pm1008CntupRaRemCntValuePortn_Type = Counter32
_Pm1008CntupRaRemCntValuePortn_Object = MibTableColumn
pm1008CntupRaRemCntValuePortn = _Pm1008CntupRaRemCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 16, 1, 2),
    _Pm1008CntupRaRemCntValuePortn_Type()
)
pm1008CntupRaRemCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaRemCntValuePortn.setStatus("current")
_Pm1008CntupRaRemCntErrorPortn_Type = EkiOnOff
_Pm1008CntupRaRemCntErrorPortn_Object = MibTableColumn
pm1008CntupRaRemCntErrorPortn = _Pm1008CntupRaRemCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 16, 1, 3),
    _Pm1008CntupRaRemCntErrorPortn_Type()
)
pm1008CntupRaRemCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaRemCntErrorPortn.setStatus("current")
_Pm1008CntupRaRemCntOverloadPortn_Type = EkiOnOff
_Pm1008CntupRaRemCntOverloadPortn_Object = MibTableColumn
pm1008CntupRaRemCntOverloadPortn = _Pm1008CntupRaRemCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 16, 1, 4),
    _Pm1008CntupRaRemCntOverloadPortn_Type()
)
pm1008CntupRaRemCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaRemCntOverloadPortn.setStatus("current")
_Pm1008CntupRaInsCntTable_Object = MibTable
pm1008CntupRaInsCntTable = _Pm1008CntupRaInsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 24)
)
if mibBuilder.loadTexts:
    pm1008CntupRaInsCntTable.setStatus("current")
_Pm1008CntupRaInsCntEntry_Object = MibTableRow
pm1008CntupRaInsCntEntry = _Pm1008CntupRaInsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 24, 1)
)
pm1008CntupRaInsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntupRaInsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntupRaInsCntEntry.setStatus("current")


class _Pm1008CntupRaInsCntIndex_Type(Integer32):
    """Custom type pm1008CntupRaInsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntupRaInsCntIndex_Type.__name__ = "Integer32"
_Pm1008CntupRaInsCntIndex_Object = MibTableColumn
pm1008CntupRaInsCntIndex = _Pm1008CntupRaInsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 24, 1, 1),
    _Pm1008CntupRaInsCntIndex_Type()
)
pm1008CntupRaInsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaInsCntIndex.setStatus("current")
_Pm1008CntupRaInsCntValuePortn_Type = Counter32
_Pm1008CntupRaInsCntValuePortn_Object = MibTableColumn
pm1008CntupRaInsCntValuePortn = _Pm1008CntupRaInsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 24, 1, 2),
    _Pm1008CntupRaInsCntValuePortn_Type()
)
pm1008CntupRaInsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaInsCntValuePortn.setStatus("current")
_Pm1008CntupRaInsCntErrorPortn_Type = EkiOnOff
_Pm1008CntupRaInsCntErrorPortn_Object = MibTableColumn
pm1008CntupRaInsCntErrorPortn = _Pm1008CntupRaInsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 24, 1, 3),
    _Pm1008CntupRaInsCntErrorPortn_Type()
)
pm1008CntupRaInsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaInsCntErrorPortn.setStatus("current")
_Pm1008CntupRaInsCntOverloadPortn_Type = EkiOnOff
_Pm1008CntupRaInsCntOverloadPortn_Object = MibTableColumn
pm1008CntupRaInsCntOverloadPortn = _Pm1008CntupRaInsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 24, 1, 4),
    _Pm1008CntupRaInsCntOverloadPortn_Type()
)
pm1008CntupRaInsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRaInsCntOverloadPortn.setStatus("current")
_Pm1008CntupRdErrCntTable_Object = MibTable
pm1008CntupRdErrCntTable = _Pm1008CntupRdErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 32)
)
if mibBuilder.loadTexts:
    pm1008CntupRdErrCntTable.setStatus("current")
_Pm1008CntupRdErrCntEntry_Object = MibTableRow
pm1008CntupRdErrCntEntry = _Pm1008CntupRdErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 32, 1)
)
pm1008CntupRdErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntupRdErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntupRdErrCntEntry.setStatus("current")


class _Pm1008CntupRdErrCntIndex_Type(Integer32):
    """Custom type pm1008CntupRdErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntupRdErrCntIndex_Type.__name__ = "Integer32"
_Pm1008CntupRdErrCntIndex_Object = MibTableColumn
pm1008CntupRdErrCntIndex = _Pm1008CntupRdErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 32, 1, 1),
    _Pm1008CntupRdErrCntIndex_Type()
)
pm1008CntupRdErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRdErrCntIndex.setStatus("current")
_Pm1008CntupRdErrCntValuePortn_Type = Counter32
_Pm1008CntupRdErrCntValuePortn_Object = MibTableColumn
pm1008CntupRdErrCntValuePortn = _Pm1008CntupRdErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 32, 1, 2),
    _Pm1008CntupRdErrCntValuePortn_Type()
)
pm1008CntupRdErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRdErrCntValuePortn.setStatus("current")
_Pm1008CntupRdErrCntErrorPortn_Type = EkiOnOff
_Pm1008CntupRdErrCntErrorPortn_Object = MibTableColumn
pm1008CntupRdErrCntErrorPortn = _Pm1008CntupRdErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 32, 1, 3),
    _Pm1008CntupRdErrCntErrorPortn_Type()
)
pm1008CntupRdErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRdErrCntErrorPortn.setStatus("current")
_Pm1008CntupRdErrCntOverloadPortn_Type = EkiOnOff
_Pm1008CntupRdErrCntOverloadPortn_Object = MibTableColumn
pm1008CntupRdErrCntOverloadPortn = _Pm1008CntupRdErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 32, 1, 4),
    _Pm1008CntupRdErrCntOverloadPortn_Type()
)
pm1008CntupRdErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupRdErrCntOverloadPortn.setStatus("current")
_Pm1008CntupTimCntTable_Object = MibTable
pm1008CntupTimCntTable = _Pm1008CntupTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 40)
)
if mibBuilder.loadTexts:
    pm1008CntupTimCntTable.setStatus("current")
_Pm1008CntupTimCntEntry_Object = MibTableRow
pm1008CntupTimCntEntry = _Pm1008CntupTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 40, 1)
)
pm1008CntupTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntupTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntupTimCntEntry.setStatus("current")


class _Pm1008CntupTimCntIndex_Type(Integer32):
    """Custom type pm1008CntupTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntupTimCntIndex_Type.__name__ = "Integer32"
_Pm1008CntupTimCntIndex_Object = MibTableColumn
pm1008CntupTimCntIndex = _Pm1008CntupTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 40, 1, 1),
    _Pm1008CntupTimCntIndex_Type()
)
pm1008CntupTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupTimCntIndex.setStatus("current")
_Pm1008CntupTimCntValuePortn_Type = Counter32
_Pm1008CntupTimCntValuePortn_Object = MibTableColumn
pm1008CntupTimCntValuePortn = _Pm1008CntupTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 40, 1, 2),
    _Pm1008CntupTimCntValuePortn_Type()
)
pm1008CntupTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupTimCntValuePortn.setStatus("current")
_Pm1008CntupTimCntErrorPortn_Type = EkiOnOff
_Pm1008CntupTimCntErrorPortn_Object = MibTableColumn
pm1008CntupTimCntErrorPortn = _Pm1008CntupTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 40, 1, 3),
    _Pm1008CntupTimCntErrorPortn_Type()
)
pm1008CntupTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupTimCntErrorPortn.setStatus("current")
_Pm1008CntupTimCntOverloadPortn_Type = EkiOnOff
_Pm1008CntupTimCntOverloadPortn_Object = MibTableColumn
pm1008CntupTimCntOverloadPortn = _Pm1008CntupTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 40, 1, 4),
    _Pm1008CntupTimCntOverloadPortn_Type()
)
pm1008CntupTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupTimCntOverloadPortn.setStatus("current")
_Pm1008CntupCvErrCntTable_Object = MibTable
pm1008CntupCvErrCntTable = _Pm1008CntupCvErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 48)
)
if mibBuilder.loadTexts:
    pm1008CntupCvErrCntTable.setStatus("current")
_Pm1008CntupCvErrCntEntry_Object = MibTableRow
pm1008CntupCvErrCntEntry = _Pm1008CntupCvErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 48, 1)
)
pm1008CntupCvErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntupCvErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntupCvErrCntEntry.setStatus("current")


class _Pm1008CntupCvErrCntIndex_Type(Integer32):
    """Custom type pm1008CntupCvErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntupCvErrCntIndex_Type.__name__ = "Integer32"
_Pm1008CntupCvErrCntIndex_Object = MibTableColumn
pm1008CntupCvErrCntIndex = _Pm1008CntupCvErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 48, 1, 1),
    _Pm1008CntupCvErrCntIndex_Type()
)
pm1008CntupCvErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupCvErrCntIndex.setStatus("current")
_Pm1008CntupCvErrCntValuePortn_Type = Counter32
_Pm1008CntupCvErrCntValuePortn_Object = MibTableColumn
pm1008CntupCvErrCntValuePortn = _Pm1008CntupCvErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 48, 1, 2),
    _Pm1008CntupCvErrCntValuePortn_Type()
)
pm1008CntupCvErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupCvErrCntValuePortn.setStatus("current")
_Pm1008CntupCvErrCntErrorPortn_Type = EkiOnOff
_Pm1008CntupCvErrCntErrorPortn_Object = MibTableColumn
pm1008CntupCvErrCntErrorPortn = _Pm1008CntupCvErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 48, 1, 3),
    _Pm1008CntupCvErrCntErrorPortn_Type()
)
pm1008CntupCvErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupCvErrCntErrorPortn.setStatus("current")
_Pm1008CntupCvErrCntOverloadPortn_Type = EkiOnOff
_Pm1008CntupCvErrCntOverloadPortn_Object = MibTableColumn
pm1008CntupCvErrCntOverloadPortn = _Pm1008CntupCvErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 48, 1, 4),
    _Pm1008CntupCvErrCntOverloadPortn_Type()
)
pm1008CntupCvErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntupCvErrCntOverloadPortn.setStatus("current")
_Pm1008CntdwCbipCntTable_Object = MibTable
pm1008CntdwCbipCntTable = _Pm1008CntdwCbipCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 64)
)
if mibBuilder.loadTexts:
    pm1008CntdwCbipCntTable.setStatus("current")
_Pm1008CntdwCbipCntEntry_Object = MibTableRow
pm1008CntdwCbipCntEntry = _Pm1008CntdwCbipCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 64, 1)
)
pm1008CntdwCbipCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntdwCbipCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntdwCbipCntEntry.setStatus("current")


class _Pm1008CntdwCbipCntIndex_Type(Integer32):
    """Custom type pm1008CntdwCbipCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntdwCbipCntIndex_Type.__name__ = "Integer32"
_Pm1008CntdwCbipCntIndex_Object = MibTableColumn
pm1008CntdwCbipCntIndex = _Pm1008CntdwCbipCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 64, 1, 1),
    _Pm1008CntdwCbipCntIndex_Type()
)
pm1008CntdwCbipCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwCbipCntIndex.setStatus("current")
_Pm1008CntdwCbipCntValuePortn_Type = Counter32
_Pm1008CntdwCbipCntValuePortn_Object = MibTableColumn
pm1008CntdwCbipCntValuePortn = _Pm1008CntdwCbipCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 64, 1, 2),
    _Pm1008CntdwCbipCntValuePortn_Type()
)
pm1008CntdwCbipCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwCbipCntValuePortn.setStatus("current")
_Pm1008CntdwCbipCntErrorPortn_Type = EkiOnOff
_Pm1008CntdwCbipCntErrorPortn_Object = MibTableColumn
pm1008CntdwCbipCntErrorPortn = _Pm1008CntdwCbipCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 64, 1, 3),
    _Pm1008CntdwCbipCntErrorPortn_Type()
)
pm1008CntdwCbipCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwCbipCntErrorPortn.setStatus("current")
_Pm1008CntdwCbipCntOverloadPortn_Type = EkiOnOff
_Pm1008CntdwCbipCntOverloadPortn_Object = MibTableColumn
pm1008CntdwCbipCntOverloadPortn = _Pm1008CntdwCbipCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 64, 1, 4),
    _Pm1008CntdwCbipCntOverloadPortn_Type()
)
pm1008CntdwCbipCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwCbipCntOverloadPortn.setStatus("current")
_Pm1008CntdwTimCntTable_Object = MibTable
pm1008CntdwTimCntTable = _Pm1008CntdwTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 72)
)
if mibBuilder.loadTexts:
    pm1008CntdwTimCntTable.setStatus("current")
_Pm1008CntdwTimCntEntry_Object = MibTableRow
pm1008CntdwTimCntEntry = _Pm1008CntdwTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 72, 1)
)
pm1008CntdwTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntdwTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntdwTimCntEntry.setStatus("current")


class _Pm1008CntdwTimCntIndex_Type(Integer32):
    """Custom type pm1008CntdwTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntdwTimCntIndex_Type.__name__ = "Integer32"
_Pm1008CntdwTimCntIndex_Object = MibTableColumn
pm1008CntdwTimCntIndex = _Pm1008CntdwTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 72, 1, 1),
    _Pm1008CntdwTimCntIndex_Type()
)
pm1008CntdwTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwTimCntIndex.setStatus("current")
_Pm1008CntdwTimCntValuePortn_Type = Counter32
_Pm1008CntdwTimCntValuePortn_Object = MibTableColumn
pm1008CntdwTimCntValuePortn = _Pm1008CntdwTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 72, 1, 2),
    _Pm1008CntdwTimCntValuePortn_Type()
)
pm1008CntdwTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwTimCntValuePortn.setStatus("current")
_Pm1008CntdwTimCntErrorPortn_Type = EkiOnOff
_Pm1008CntdwTimCntErrorPortn_Object = MibTableColumn
pm1008CntdwTimCntErrorPortn = _Pm1008CntdwTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 72, 1, 3),
    _Pm1008CntdwTimCntErrorPortn_Type()
)
pm1008CntdwTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwTimCntErrorPortn.setStatus("current")
_Pm1008CntdwTimCntOverloadPortn_Type = EkiOnOff
_Pm1008CntdwTimCntOverloadPortn_Object = MibTableColumn
pm1008CntdwTimCntOverloadPortn = _Pm1008CntdwTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 2, 72, 1, 4),
    _Pm1008CntdwTimCntOverloadPortn_Type()
)
pm1008CntdwTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdwTimCntOverloadPortn.setStatus("current")
_Pm1008CntLine_ObjectIdentity = ObjectIdentity
pm1008CntLine = _Pm1008CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3)
)
_Pm1008CntdfrmB1ErrCntTable_Object = MibTable
pm1008CntdfrmB1ErrCntTable = _Pm1008CntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1008CntdfrmB1ErrCntTable.setStatus("current")
_Pm1008CntdfrmB1ErrCntEntry_Object = MibTableRow
pm1008CntdfrmB1ErrCntEntry = _Pm1008CntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 152, 1)
)
pm1008CntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1008CntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1008CntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1008CntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1008CntdfrmB1ErrCntIndex = _Pm1008CntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 152, 1, 1),
    _Pm1008CntdfrmB1ErrCntIndex_Type()
)
pm1008CntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmB1ErrCntIndex.setStatus("current")
_Pm1008CntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1008CntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1008CntdfrmB1ErrCntValuePortn = _Pm1008CntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 152, 1, 2),
    _Pm1008CntdfrmB1ErrCntValuePortn_Type()
)
pm1008CntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1008CntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1008CntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1008CntdfrmB1ErrCntErrorPortn = _Pm1008CntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 152, 1, 3),
    _Pm1008CntdfrmB1ErrCntErrorPortn_Type()
)
pm1008CntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1008CntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1008CntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1008CntdfrmB1ErrCntOverloadPortn = _Pm1008CntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 152, 1, 4),
    _Pm1008CntdfrmB1ErrCntOverloadPortn_Type()
)
pm1008CntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1008CntdfrmTimCntTable_Object = MibTable
pm1008CntdfrmTimCntTable = _Pm1008CntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1008CntdfrmTimCntTable.setStatus("current")
_Pm1008CntdfrmTimCntEntry_Object = MibTableRow
pm1008CntdfrmTimCntEntry = _Pm1008CntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 153, 1)
)
pm1008CntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntdfrmTimCntEntry.setStatus("current")


class _Pm1008CntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1008CntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1008CntdfrmTimCntIndex_Object = MibTableColumn
pm1008CntdfrmTimCntIndex = _Pm1008CntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 153, 1, 1),
    _Pm1008CntdfrmTimCntIndex_Type()
)
pm1008CntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmTimCntIndex.setStatus("current")
_Pm1008CntdfrmTimCntValuePortn_Type = Counter32
_Pm1008CntdfrmTimCntValuePortn_Object = MibTableColumn
pm1008CntdfrmTimCntValuePortn = _Pm1008CntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 153, 1, 2),
    _Pm1008CntdfrmTimCntValuePortn_Type()
)
pm1008CntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmTimCntValuePortn.setStatus("current")
_Pm1008CntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1008CntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1008CntdfrmTimCntErrorPortn = _Pm1008CntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 153, 1, 3),
    _Pm1008CntdfrmTimCntErrorPortn_Type()
)
pm1008CntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmTimCntErrorPortn.setStatus("current")
_Pm1008CntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1008CntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1008CntdfrmTimCntOverloadPortn = _Pm1008CntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 153, 1, 4),
    _Pm1008CntdfrmTimCntOverloadPortn_Type()
)
pm1008CntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1008CntdfrmPrimLineErrCntTable_Object = MibTable
pm1008CntdfrmPrimLineErrCntTable = _Pm1008CntdfrmPrimLineErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 154)
)
if mibBuilder.loadTexts:
    pm1008CntdfrmPrimLineErrCntTable.setStatus("current")
_Pm1008CntdfrmPrimLineErrCntEntry_Object = MibTableRow
pm1008CntdfrmPrimLineErrCntEntry = _Pm1008CntdfrmPrimLineErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 154, 1)
)
pm1008CntdfrmPrimLineErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CntdfrmPrimLineErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008CntdfrmPrimLineErrCntEntry.setStatus("current")


class _Pm1008CntdfrmPrimLineErrCntIndex_Type(Integer32):
    """Custom type pm1008CntdfrmPrimLineErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CntdfrmPrimLineErrCntIndex_Type.__name__ = "Integer32"
_Pm1008CntdfrmPrimLineErrCntIndex_Object = MibTableColumn
pm1008CntdfrmPrimLineErrCntIndex = _Pm1008CntdfrmPrimLineErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 154, 1, 1),
    _Pm1008CntdfrmPrimLineErrCntIndex_Type()
)
pm1008CntdfrmPrimLineErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmPrimLineErrCntIndex.setStatus("current")
_Pm1008CntdfrmPrimLineErrCntValuePortn_Type = Counter32
_Pm1008CntdfrmPrimLineErrCntValuePortn_Object = MibTableColumn
pm1008CntdfrmPrimLineErrCntValuePortn = _Pm1008CntdfrmPrimLineErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 154, 1, 2),
    _Pm1008CntdfrmPrimLineErrCntValuePortn_Type()
)
pm1008CntdfrmPrimLineErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmPrimLineErrCntValuePortn.setStatus("current")
_Pm1008CntdfrmPrimLineErrCntErrorPortn_Type = EkiOnOff
_Pm1008CntdfrmPrimLineErrCntErrorPortn_Object = MibTableColumn
pm1008CntdfrmPrimLineErrCntErrorPortn = _Pm1008CntdfrmPrimLineErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 154, 1, 3),
    _Pm1008CntdfrmPrimLineErrCntErrorPortn_Type()
)
pm1008CntdfrmPrimLineErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmPrimLineErrCntErrorPortn.setStatus("current")
_Pm1008CntdfrmPrimLineErrCntOverloadPortn_Type = EkiOnOff
_Pm1008CntdfrmPrimLineErrCntOverloadPortn_Object = MibTableColumn
pm1008CntdfrmPrimLineErrCntOverloadPortn = _Pm1008CntdfrmPrimLineErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 3, 154, 1, 4),
    _Pm1008CntdfrmPrimLineErrCntOverloadPortn_Type()
)
pm1008CntdfrmPrimLineErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CntdfrmPrimLineErrCntOverloadPortn.setStatus("current")
_Pm1008CntCountersReset_Type = EkiOnOff
_Pm1008CntCountersReset_Object = MibScalar
pm1008CntCountersReset = _Pm1008CntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 259),
    _Pm1008CntCountersReset_Type()
)
pm1008CntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CntCountersReset.setStatus("current")
_Pm1008CntCountersStop_Type = EkiOnOff
_Pm1008CntCountersStop_Object = MibScalar
pm1008CntCountersStop = _Pm1008CntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 4, 260),
    _Pm1008CntCountersStop_Type()
)
pm1008CntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CntCountersStop.setStatus("current")
_Pm1008controlsWrite_ObjectIdentity = ObjectIdentity
pm1008controlsWrite = _Pm1008controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6)
)
_Pm1008CtrlOther_ObjectIdentity = ObjectIdentity
pm1008CtrlOther = _Pm1008CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1)
)
_Pm1008CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1008CtrlconfMgnt1 = _Pm1008CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 1)
)
_Pm1008CtrlConf1Load1_Type = EkiOnOff
_Pm1008CtrlConf1Load1_Object = MibScalar
pm1008CtrlConf1Load1 = _Pm1008CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 1, 1),
    _Pm1008CtrlConf1Load1_Type()
)
pm1008CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlConf1Load1.setStatus("current")
_Pm1008CtrlConf2Load1_Type = EkiOnOff
_Pm1008CtrlConf2Load1_Object = MibScalar
pm1008CtrlConf2Load1 = _Pm1008CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 1, 2),
    _Pm1008CtrlConf2Load1_Type()
)
pm1008CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlConf2Load1.setStatus("current")
_Pm1008CtrlConf2Flash1_Type = EkiOnOff
_Pm1008CtrlConf2Flash1_Object = MibScalar
pm1008CtrlConf2Flash1 = _Pm1008CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 1, 10),
    _Pm1008CtrlConf2Flash1_Type()
)
pm1008CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlConf2Flash1.setStatus("current")
_Pm1008CtrlConf2Clear1_Type = EkiOnOff
_Pm1008CtrlConf2Clear1_Object = MibScalar
pm1008CtrlConf2Clear1 = _Pm1008CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 1, 14),
    _Pm1008CtrlConf2Clear1_Type()
)
pm1008CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlConf2Clear1.setStatus("current")
_Pm1008Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm1008Ctrlsynth4 = _Pm1008Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 4)
)
_Pm1008CtrlCorrelatOn_Type = EkiOnOff
_Pm1008CtrlCorrelatOn_Object = MibScalar
pm1008CtrlCorrelatOn = _Pm1008CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 4, 1),
    _Pm1008CtrlCorrelatOn_Type()
)
pm1008CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlCorrelatOn.setStatus("current")
_Pm1008CtrlCorrelatOff_Type = EkiOnOff
_Pm1008CtrlCorrelatOff_Object = MibScalar
pm1008CtrlCorrelatOff = _Pm1008CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 4, 2),
    _Pm1008CtrlCorrelatOff_Type()
)
pm1008CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlCorrelatOff.setStatus("current")
_Pm1008CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1008CtrlswMgnt = _Pm1008CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 5)
)
_Pm1008CtrlColdReset_Type = EkiOnOff
_Pm1008CtrlColdReset_Object = MibScalar
pm1008CtrlColdReset = _Pm1008CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 5, 2),
    _Pm1008CtrlColdReset_Type()
)
pm1008CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlColdReset.setStatus("current")
_Pm1008CtrlWarmReset_Type = EkiOnOff
_Pm1008CtrlWarmReset_Object = MibScalar
pm1008CtrlWarmReset = _Pm1008CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 5, 3),
    _Pm1008CtrlWarmReset_Type()
)
pm1008CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlWarmReset.setStatus("current")
_Pm1008CtrlLoadSwBank1_Type = EkiOnOff
_Pm1008CtrlLoadSwBank1_Object = MibScalar
pm1008CtrlLoadSwBank1 = _Pm1008CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 5, 5),
    _Pm1008CtrlLoadSwBank1_Type()
)
pm1008CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLoadSwBank1.setStatus("current")
_Pm1008CtrlLoadSwBank2_Type = EkiOnOff
_Pm1008CtrlLoadSwBank2_Object = MibScalar
pm1008CtrlLoadSwBank2 = _Pm1008CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 5, 6),
    _Pm1008CtrlLoadSwBank2_Type()
)
pm1008CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLoadSwBank2.setStatus("current")
_Pm1008CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1008CtrlgwMgnt = _Pm1008CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 6)
)
_Pm1008CtrlCurrentGwReset_Type = EkiOnOff
_Pm1008CtrlCurrentGwReset_Object = MibScalar
pm1008CtrlCurrentGwReset = _Pm1008CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 6, 1),
    _Pm1008CtrlCurrentGwReset_Type()
)
pm1008CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlCurrentGwReset.setStatus("current")
_Pm1008CtrlLoadGwBank1_Type = EkiOnOff
_Pm1008CtrlLoadGwBank1_Object = MibScalar
pm1008CtrlLoadGwBank1 = _Pm1008CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 6, 5),
    _Pm1008CtrlLoadGwBank1_Type()
)
pm1008CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLoadGwBank1.setStatus("current")
_Pm1008CtrlLoadGwBank2_Type = EkiOnOff
_Pm1008CtrlLoadGwBank2_Object = MibScalar
pm1008CtrlLoadGwBank2 = _Pm1008CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 6, 6),
    _Pm1008CtrlLoadGwBank2_Type()
)
pm1008CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLoadGwBank2.setStatus("current")
_Pm1008CtrlLoadGwBank3_Type = EkiOnOff
_Pm1008CtrlLoadGwBank3_Object = MibScalar
pm1008CtrlLoadGwBank3 = _Pm1008CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 6, 7),
    _Pm1008CtrlLoadGwBank3_Type()
)
pm1008CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLoadGwBank3.setStatus("current")
_Pm1008CtrlLoadGwBank4_Type = EkiOnOff
_Pm1008CtrlLoadGwBank4_Object = MibScalar
pm1008CtrlLoadGwBank4 = _Pm1008CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 6, 8),
    _Pm1008CtrlLoadGwBank4_Type()
)
pm1008CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLoadGwBank4.setStatus("current")
_Pm1008CtrlledTest_ObjectIdentity = ObjectIdentity
pm1008CtrlledTest = _Pm1008CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 192)
)
_Pm1008CtrlGreenLed_Type = EkiOnOff
_Pm1008CtrlGreenLed_Object = MibScalar
pm1008CtrlGreenLed = _Pm1008CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 192, 1),
    _Pm1008CtrlGreenLed_Type()
)
pm1008CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlGreenLed.setStatus("current")
_Pm1008CtrlRedLed_Type = EkiOnOff
_Pm1008CtrlRedLed_Object = MibScalar
pm1008CtrlRedLed = _Pm1008CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 192, 2),
    _Pm1008CtrlRedLed_Type()
)
pm1008CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlRedLed.setStatus("current")
_Pm1008CtrlLedOff_Type = EkiOnOff
_Pm1008CtrlLedOff_Object = MibScalar
pm1008CtrlLedOff = _Pm1008CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 192, 3),
    _Pm1008CtrlLedOff_Type()
)
pm1008CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLedOff.setStatus("current")
_Pm1008CtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1008CtrlmoduleOosMode = _Pm1008CtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 193)
)
_Pm1008CtrlModuleOosMode_Type = EkiOnOff
_Pm1008CtrlModuleOosMode_Object = MibScalar
pm1008CtrlModuleOosMode = _Pm1008CtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 193, 1),
    _Pm1008CtrlModuleOosMode_Type()
)
pm1008CtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlModuleOosMode.setStatus("current")
_Pm1008CtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1008CtrlmaintenanceMode = _Pm1008CtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 197)
)
_Pm1008CtrlMaintenanceMode_Type = EkiOnOff
_Pm1008CtrlMaintenanceMode_Object = MibScalar
pm1008CtrlMaintenanceMode = _Pm1008CtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 197, 1),
    _Pm1008CtrlMaintenanceMode_Type()
)
pm1008CtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlMaintenanceMode.setStatus("current")
_Pm1008CtrldccEnable_ObjectIdentity = ObjectIdentity
pm1008CtrldccEnable = _Pm1008CtrldccEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 198)
)
_Pm1008CtrlDccEnable_Type = EkiOnOff
_Pm1008CtrlDccEnable_Object = MibScalar
pm1008CtrlDccEnable = _Pm1008CtrlDccEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 1, 198, 1),
    _Pm1008CtrlDccEnable_Type()
)
pm1008CtrlDccEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlDccEnable.setStatus("current")
_Pm1008CtrlClient_ObjectIdentity = ObjectIdentity
pm1008CtrlClient = _Pm1008CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2)
)
_Pm1008CtrlaccessLoopTable_Object = MibTable
pm1008CtrlaccessLoopTable = _Pm1008CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1008CtrlaccessLoopTable.setStatus("current")
_Pm1008CtrlaccessLoopEntry_Object = MibTableRow
pm1008CtrlaccessLoopEntry = _Pm1008CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 16, 1)
)
pm1008CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlaccessLoopEntry.setStatus("current")


class _Pm1008CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1008CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1008CtrlaccessLoopIndex_Object = MibTableColumn
pm1008CtrlaccessLoopIndex = _Pm1008CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 16, 1, 1),
    _Pm1008CtrlaccessLoopIndex_Type()
)
pm1008CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlaccessLoopIndex.setStatus("current")
_Pm1008CtrlaccessLoopPortn_Type = EkiState
_Pm1008CtrlaccessLoopPortn_Object = MibTableColumn
pm1008CtrlaccessLoopPortn = _Pm1008CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 16, 1, 2),
    _Pm1008CtrlaccessLoopPortn_Type()
)
pm1008CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlaccessLoopPortn.setStatus("current")
_Pm1008CtrlportOosModeTable_Object = MibTable
pm1008CtrlportOosModeTable = _Pm1008CtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1008CtrlportOosModeTable.setStatus("current")
_Pm1008CtrlportOosModeEntry_Object = MibTableRow
pm1008CtrlportOosModeEntry = _Pm1008CtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 18, 1)
)
pm1008CtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlportOosModeEntry.setStatus("current")


class _Pm1008CtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1008CtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1008CtrlportOosModeIndex_Object = MibTableColumn
pm1008CtrlportOosModeIndex = _Pm1008CtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 18, 1, 1),
    _Pm1008CtrlportOosModeIndex_Type()
)
pm1008CtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlportOosModeIndex.setStatus("current")
_Pm1008CtrlportOosModePortn_Type = EkiState
_Pm1008CtrlportOosModePortn_Object = MibTableColumn
pm1008CtrlportOosModePortn = _Pm1008CtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 18, 1, 2),
    _Pm1008CtrlportOosModePortn_Type()
)
pm1008CtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlportOosModePortn.setStatus("current")
_Pm1008CtrlsfpOnCtrlTable_Object = MibTable
pm1008CtrlsfpOnCtrlTable = _Pm1008CtrlsfpOnCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 19)
)
if mibBuilder.loadTexts:
    pm1008CtrlsfpOnCtrlTable.setStatus("current")
_Pm1008CtrlsfpOnCtrlEntry_Object = MibTableRow
pm1008CtrlsfpOnCtrlEntry = _Pm1008CtrlsfpOnCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 19, 1)
)
pm1008CtrlsfpOnCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlsfpOnCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlsfpOnCtrlEntry.setStatus("current")


class _Pm1008CtrlsfpOnCtrlIndex_Type(Integer32):
    """Custom type pm1008CtrlsfpOnCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlsfpOnCtrlIndex_Type.__name__ = "Integer32"
_Pm1008CtrlsfpOnCtrlIndex_Object = MibTableColumn
pm1008CtrlsfpOnCtrlIndex = _Pm1008CtrlsfpOnCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 19, 1, 1),
    _Pm1008CtrlsfpOnCtrlIndex_Type()
)
pm1008CtrlsfpOnCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlsfpOnCtrlIndex.setStatus("current")
_Pm1008CtrlsfpOnCtrlPortn_Type = EkiState
_Pm1008CtrlsfpOnCtrlPortn_Object = MibTableColumn
pm1008CtrlsfpOnCtrlPortn = _Pm1008CtrlsfpOnCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 19, 1, 2),
    _Pm1008CtrlsfpOnCtrlPortn_Type()
)
pm1008CtrlsfpOnCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlsfpOnCtrlPortn.setStatus("current")
_Pm1008CtrlsfpOffCtrlTable_Object = MibTable
pm1008CtrlsfpOffCtrlTable = _Pm1008CtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1008CtrlsfpOffCtrlTable.setStatus("current")
_Pm1008CtrlsfpOffCtrlEntry_Object = MibTableRow
pm1008CtrlsfpOffCtrlEntry = _Pm1008CtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 20, 1)
)
pm1008CtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1008CtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1008CtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1008CtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1008CtrlsfpOffCtrlIndex = _Pm1008CtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 20, 1, 1),
    _Pm1008CtrlsfpOffCtrlIndex_Type()
)
pm1008CtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlsfpOffCtrlIndex.setStatus("current")
_Pm1008CtrlsfpOffCtrlPortn_Type = EkiState
_Pm1008CtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1008CtrlsfpOffCtrlPortn = _Pm1008CtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 20, 1, 2),
    _Pm1008CtrlsfpOffCtrlPortn_Type()
)
pm1008CtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlsfpOffCtrlPortn.setStatus("current")
_Pm1008CtrlcsfUpInsTable_Object = MibTable
pm1008CtrlcsfUpInsTable = _Pm1008CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1008CtrlcsfUpInsTable.setStatus("current")
_Pm1008CtrlcsfUpInsEntry_Object = MibTableRow
pm1008CtrlcsfUpInsEntry = _Pm1008CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 21, 1)
)
pm1008CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlcsfUpInsEntry.setStatus("current")


class _Pm1008CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1008CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1008CtrlcsfUpInsIndex_Object = MibTableColumn
pm1008CtrlcsfUpInsIndex = _Pm1008CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 21, 1, 1),
    _Pm1008CtrlcsfUpInsIndex_Type()
)
pm1008CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlcsfUpInsIndex.setStatus("current")
_Pm1008CtrlcsfUpInsPortn_Type = EkiState
_Pm1008CtrlcsfUpInsPortn_Object = MibTableColumn
pm1008CtrlcsfUpInsPortn = _Pm1008CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 21, 1, 2),
    _Pm1008CtrlcsfUpInsPortn_Type()
)
pm1008CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlcsfUpInsPortn.setStatus("current")
_Pm1008CtrlcaisDwInsTable_Object = MibTable
pm1008CtrlcaisDwInsTable = _Pm1008CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1008CtrlcaisDwInsTable.setStatus("current")
_Pm1008CtrlcaisDwInsEntry_Object = MibTableRow
pm1008CtrlcaisDwInsEntry = _Pm1008CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 22, 1)
)
pm1008CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlcaisDwInsEntry.setStatus("current")


class _Pm1008CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1008CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1008CtrlcaisDwInsIndex_Object = MibTableColumn
pm1008CtrlcaisDwInsIndex = _Pm1008CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 22, 1, 1),
    _Pm1008CtrlcaisDwInsIndex_Type()
)
pm1008CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlcaisDwInsIndex.setStatus("current")
_Pm1008CtrlcaisDwInsPortn_Type = EkiState
_Pm1008CtrlcaisDwInsPortn_Object = MibTableColumn
pm1008CtrlcaisDwInsPortn = _Pm1008CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 22, 1, 2),
    _Pm1008CtrlcaisDwInsPortn_Type()
)
pm1008CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlcaisDwInsPortn.setStatus("current")
_Pm1008CtrlflowControlTable_Object = MibTable
pm1008CtrlflowControlTable = _Pm1008CtrlflowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 23)
)
if mibBuilder.loadTexts:
    pm1008CtrlflowControlTable.setStatus("current")
_Pm1008CtrlflowControlEntry_Object = MibTableRow
pm1008CtrlflowControlEntry = _Pm1008CtrlflowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 23, 1)
)
pm1008CtrlflowControlEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlflowControlIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlflowControlEntry.setStatus("current")


class _Pm1008CtrlflowControlIndex_Type(Integer32):
    """Custom type pm1008CtrlflowControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlflowControlIndex_Type.__name__ = "Integer32"
_Pm1008CtrlflowControlIndex_Object = MibTableColumn
pm1008CtrlflowControlIndex = _Pm1008CtrlflowControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 23, 1, 1),
    _Pm1008CtrlflowControlIndex_Type()
)
pm1008CtrlflowControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlflowControlIndex.setStatus("current")
_Pm1008CtrlflowControlPortn_Type = EkiState
_Pm1008CtrlflowControlPortn_Object = MibTableColumn
pm1008CtrlflowControlPortn = _Pm1008CtrlflowControlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 23, 1, 2),
    _Pm1008CtrlflowControlPortn_Type()
)
pm1008CtrlflowControlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlflowControlPortn.setStatus("current")
_Pm1008CtrlclientAccessTermLoopTable_Object = MibTable
pm1008CtrlclientAccessTermLoopTable = _Pm1008CtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1008CtrlclientAccessTermLoopTable.setStatus("current")
_Pm1008CtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1008CtrlclientAccessTermLoopEntry = _Pm1008CtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 26, 1)
)
pm1008CtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1008CtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1008CtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1008CtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1008CtrlclientAccessTermLoopIndex = _Pm1008CtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 26, 1, 1),
    _Pm1008CtrlclientAccessTermLoopIndex_Type()
)
pm1008CtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1008CtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1008CtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1008CtrlclientAccessTermLoopPortn = _Pm1008CtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 26, 1, 2),
    _Pm1008CtrlclientAccessTermLoopPortn_Type()
)
pm1008CtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1008CtrlselectMultirateTable_Object = MibTable
pm1008CtrlselectMultirateTable = _Pm1008CtrlselectMultirateTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 42)
)
if mibBuilder.loadTexts:
    pm1008CtrlselectMultirateTable.setStatus("current")
_Pm1008CtrlselectMultirateEntry_Object = MibTableRow
pm1008CtrlselectMultirateEntry = _Pm1008CtrlselectMultirateEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 42, 1)
)
pm1008CtrlselectMultirateEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlselectMultirateIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlselectMultirateEntry.setStatus("current")


class _Pm1008CtrlselectMultirateIndex_Type(Integer32):
    """Custom type pm1008CtrlselectMultirateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlselectMultirateIndex_Type.__name__ = "Integer32"
_Pm1008CtrlselectMultirateIndex_Object = MibTableColumn
pm1008CtrlselectMultirateIndex = _Pm1008CtrlselectMultirateIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 42, 1, 1),
    _Pm1008CtrlselectMultirateIndex_Type()
)
pm1008CtrlselectMultirateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlselectMultirateIndex.setStatus("current")
_Pm1008CtrlselectMultiratePortn_Type = Pm1008MultiRate
_Pm1008CtrlselectMultiratePortn_Object = MibTableColumn
pm1008CtrlselectMultiratePortn = _Pm1008CtrlselectMultiratePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 42, 1, 2),
    _Pm1008CtrlselectMultiratePortn_Type()
)
pm1008CtrlselectMultiratePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlselectMultiratePortn.setStatus("current")
_Pm1008CtrlprotocolTable_Object = MibTable
pm1008CtrlprotocolTable = _Pm1008CtrlprotocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 48)
)
if mibBuilder.loadTexts:
    pm1008CtrlprotocolTable.setStatus("current")
_Pm1008CtrlprotocolEntry_Object = MibTableRow
pm1008CtrlprotocolEntry = _Pm1008CtrlprotocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 48, 1)
)
pm1008CtrlprotocolEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlprotocolIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlprotocolEntry.setStatus("current")


class _Pm1008CtrlprotocolIndex_Type(Integer32):
    """Custom type pm1008CtrlprotocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlprotocolIndex_Type.__name__ = "Integer32"
_Pm1008CtrlprotocolIndex_Object = MibTableColumn
pm1008CtrlprotocolIndex = _Pm1008CtrlprotocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 48, 1, 1),
    _Pm1008CtrlprotocolIndex_Type()
)
pm1008CtrlprotocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlprotocolIndex.setStatus("current")
_Pm1008CtrlprotocolPortn_Type = EkiProtocol
_Pm1008CtrlprotocolPortn_Object = MibTableColumn
pm1008CtrlprotocolPortn = _Pm1008CtrlprotocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 2, 48, 1, 2),
    _Pm1008CtrlprotocolPortn_Type()
)
pm1008CtrlprotocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlprotocolPortn.setStatus("current")
_Pm1008CtrlLine_ObjectIdentity = ObjectIdentity
pm1008CtrlLine = _Pm1008CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3)
)
_Pm1008CtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1008CtrlcommAccessLoop = _Pm1008CtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 64)
)
_Pm1008CtrlCommAccessloop_Type = EkiOnOff
_Pm1008CtrlCommAccessloop_Object = MibScalar
pm1008CtrlCommAccessloop = _Pm1008CtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 64, 1),
    _Pm1008CtrlCommAccessloop_Type()
)
pm1008CtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlCommAccessloop.setStatus("deprecated")
_Pm1008CtrllineLoop_ObjectIdentity = ObjectIdentity
pm1008CtrllineLoop = _Pm1008CtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 66)
)
_Pm1008CtrlLineLoop_Type = EkiOnOff
_Pm1008CtrlLineLoop_Object = MibScalar
pm1008CtrlLineLoop = _Pm1008CtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 66, 1),
    _Pm1008CtrlLineLoop_Type()
)
pm1008CtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLineLoop.setStatus("deprecated")
_Pm1008CtrlmsAis_ObjectIdentity = ObjectIdentity
pm1008CtrlmsAis = _Pm1008CtrlmsAis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 67)
)
_Pm1008CtrlMsAis_Type = EkiOnOff
_Pm1008CtrlMsAis_Object = MibScalar
pm1008CtrlMsAis = _Pm1008CtrlMsAis_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 67, 1),
    _Pm1008CtrlMsAis_Type()
)
pm1008CtrlMsAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlMsAis.setStatus("current")
_Pm1008CtrlfecDisableTable_Object = MibTable
pm1008CtrlfecDisableTable = _Pm1008CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm1008CtrlfecDisableTable.setStatus("current")
_Pm1008CtrlfecDisableEntry_Object = MibTableRow
pm1008CtrlfecDisableEntry = _Pm1008CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 69, 1)
)
pm1008CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlfecDisableEntry.setStatus("current")


class _Pm1008CtrlfecDisableIndex_Type(Integer32):
    """Custom type pm1008CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm1008CtrlfecDisableIndex_Object = MibTableColumn
pm1008CtrlfecDisableIndex = _Pm1008CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 69, 1, 1),
    _Pm1008CtrlfecDisableIndex_Type()
)
pm1008CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlfecDisableIndex.setStatus("current")
_Pm1008CtrlfecDisablePortn_Type = EkiState
_Pm1008CtrlfecDisablePortn_Object = MibTableColumn
pm1008CtrlfecDisablePortn = _Pm1008CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 69, 1, 2),
    _Pm1008CtrlfecDisablePortn_Type()
)
pm1008CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlfecDisablePortn.setStatus("current")
_Pm1008CtrlProtMgnt_ObjectIdentity = ObjectIdentity
pm1008CtrlProtMgnt = _Pm1008CtrlProtMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 73)
)


class _Pm1008CtrlLineNumber_Type(Unsigned32):
    """Custom type pm1008CtrlLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pm1008CtrlLineNumber_Type.__name__ = "Unsigned32"
_Pm1008CtrlLineNumber_Object = MibScalar
pm1008CtrlLineNumber = _Pm1008CtrlLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 73, 1),
    _Pm1008CtrlLineNumber_Type()
)
pm1008CtrlLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlLineNumber.setStatus("current")
_Pm1008CtrlProtMode_Type = EkiMode
_Pm1008CtrlProtMode_Object = MibScalar
pm1008CtrlProtMode = _Pm1008CtrlProtMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 73, 2),
    _Pm1008CtrlProtMode_Type()
)
pm1008CtrlProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlProtMode.setStatus("current")
_Pm1008CtrllineOosModeTable_Object = MibTable
pm1008CtrllineOosModeTable = _Pm1008CtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1008CtrllineOosModeTable.setStatus("current")
_Pm1008CtrllineOosModeEntry_Object = MibTableRow
pm1008CtrllineOosModeEntry = _Pm1008CtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 74, 1)
)
pm1008CtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrllineOosModeEntry.setStatus("current")


class _Pm1008CtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1008CtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1008CtrllineOosModeIndex_Object = MibTableColumn
pm1008CtrllineOosModeIndex = _Pm1008CtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 74, 1, 1),
    _Pm1008CtrllineOosModeIndex_Type()
)
pm1008CtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrllineOosModeIndex.setStatus("current")
_Pm1008CtrllineOosModePortn_Type = EkiState
_Pm1008CtrllineOosModePortn_Object = MibTableColumn
pm1008CtrllineOosModePortn = _Pm1008CtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 74, 1, 2),
    _Pm1008CtrllineOosModePortn_Type()
)
pm1008CtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrllineOosModePortn.setStatus("current")
_Pm1008CtrlxfpOnoffTable_Object = MibTable
pm1008CtrlxfpOnoffTable = _Pm1008CtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1008CtrlxfpOnoffTable.setStatus("current")
_Pm1008CtrlxfpOnoffEntry_Object = MibTableRow
pm1008CtrlxfpOnoffEntry = _Pm1008CtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 208, 1)
)
pm1008CtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlxfpOnoffEntry.setStatus("current")


class _Pm1008CtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1008CtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1008CtrlxfpOnoffIndex_Object = MibTableColumn
pm1008CtrlxfpOnoffIndex = _Pm1008CtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 208, 1, 1),
    _Pm1008CtrlxfpOnoffIndex_Type()
)
pm1008CtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlxfpOnoffIndex.setStatus("current")
_Pm1008CtrlxfpOnoffPortn_Type = EkiState
_Pm1008CtrlxfpOnoffPortn_Object = MibTableColumn
pm1008CtrlxfpOnoffPortn = _Pm1008CtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 208, 1, 2),
    _Pm1008CtrlxfpOnoffPortn_Type()
)
pm1008CtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlxfpOnoffPortn.setStatus("current")
_Pm1008CtrlxfpLineLoopTable_Object = MibTable
pm1008CtrlxfpLineLoopTable = _Pm1008CtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1008CtrlxfpLineLoopTable.setStatus("current")
_Pm1008CtrlxfpLineLoopEntry_Object = MibTableRow
pm1008CtrlxfpLineLoopEntry = _Pm1008CtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 209, 1)
)
pm1008CtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlxfpLineLoopEntry.setStatus("current")


class _Pm1008CtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1008CtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1008CtrlxfpLineLoopIndex_Object = MibTableColumn
pm1008CtrlxfpLineLoopIndex = _Pm1008CtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 209, 1, 1),
    _Pm1008CtrlxfpLineLoopIndex_Type()
)
pm1008CtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlxfpLineLoopIndex.setStatus("current")
_Pm1008CtrlxfpLineLoopPortn_Type = EkiState
_Pm1008CtrlxfpLineLoopPortn_Object = MibTableColumn
pm1008CtrlxfpLineLoopPortn = _Pm1008CtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 209, 1, 2),
    _Pm1008CtrlxfpLineLoopPortn_Type()
)
pm1008CtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlxfpLineLoopPortn.setStatus("current")
_Pm1008CtrlxfpXfiLoopTable_Object = MibTable
pm1008CtrlxfpXfiLoopTable = _Pm1008CtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1008CtrlxfpXfiLoopTable.setStatus("current")
_Pm1008CtrlxfpXfiLoopEntry_Object = MibTableRow
pm1008CtrlxfpXfiLoopEntry = _Pm1008CtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 210, 1)
)
pm1008CtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1008CtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1008CtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1008CtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1008CtrlxfpXfiLoopIndex = _Pm1008CtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 210, 1, 1),
    _Pm1008CtrlxfpXfiLoopIndex_Type()
)
pm1008CtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrlxfpXfiLoopIndex.setStatus("current")
_Pm1008CtrlxfpXfiLoopPortn_Type = EkiState
_Pm1008CtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1008CtrlxfpXfiLoopPortn = _Pm1008CtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 210, 1, 2),
    _Pm1008CtrlxfpXfiLoopPortn_Type()
)
pm1008CtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrlxfpXfiLoopPortn.setStatus("current")
_Pm1008CtrllineTunableChannelTable_Object = MibTable
pm1008CtrllineTunableChannelTable = _Pm1008CtrllineTunableChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm1008CtrllineTunableChannelTable.setStatus("current")
_Pm1008CtrllineTunableChannelEntry_Object = MibTableRow
pm1008CtrllineTunableChannelEntry = _Pm1008CtrllineTunableChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 212, 1)
)
pm1008CtrllineTunableChannelEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrllineTunableChannelIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrllineTunableChannelEntry.setStatus("current")


class _Pm1008CtrllineTunableChannelIndex_Type(Integer32):
    """Custom type pm1008CtrllineTunableChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrllineTunableChannelIndex_Type.__name__ = "Integer32"
_Pm1008CtrllineTunableChannelIndex_Object = MibTableColumn
pm1008CtrllineTunableChannelIndex = _Pm1008CtrllineTunableChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 212, 1, 1),
    _Pm1008CtrllineTunableChannelIndex_Type()
)
pm1008CtrllineTunableChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrllineTunableChannelIndex.setStatus("current")
_Pm1008CtrllineTunableChannelPortn_Type = Pm1008OtxChannel
_Pm1008CtrllineTunableChannelPortn_Object = MibTableColumn
pm1008CtrllineTunableChannelPortn = _Pm1008CtrllineTunableChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 212, 1, 2),
    _Pm1008CtrllineTunableChannelPortn_Type()
)
pm1008CtrllineTunableChannelPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrllineTunableChannelPortn.setStatus("current")
_Pm1008CtrllinePhotodiodeModeTable_Object = MibTable
pm1008CtrllinePhotodiodeModeTable = _Pm1008CtrllinePhotodiodeModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 213)
)
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeModeTable.setStatus("current")
_Pm1008CtrllinePhotodiodeModeEntry_Object = MibTableRow
pm1008CtrllinePhotodiodeModeEntry = _Pm1008CtrllinePhotodiodeModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 213, 1)
)
pm1008CtrllinePhotodiodeModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrllinePhotodiodeModeIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeModeEntry.setStatus("current")


class _Pm1008CtrllinePhotodiodeModeIndex_Type(Integer32):
    """Custom type pm1008CtrllinePhotodiodeModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrllinePhotodiodeModeIndex_Type.__name__ = "Integer32"
_Pm1008CtrllinePhotodiodeModeIndex_Object = MibTableColumn
pm1008CtrllinePhotodiodeModeIndex = _Pm1008CtrllinePhotodiodeModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 213, 1, 1),
    _Pm1008CtrllinePhotodiodeModeIndex_Type()
)
pm1008CtrllinePhotodiodeModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeModeIndex.setStatus("current")
_Pm1008CtrllinePhotodiodeModePortn_Type = Pm1008OtxMode
_Pm1008CtrllinePhotodiodeModePortn_Object = MibTableColumn
pm1008CtrllinePhotodiodeModePortn = _Pm1008CtrllinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 213, 1, 2),
    _Pm1008CtrllinePhotodiodeModePortn_Type()
)
pm1008CtrllinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeModePortn.setStatus("current")
_Pm1008CtrllinePhotodiodeValueTable_Object = MibTable
pm1008CtrllinePhotodiodeValueTable = _Pm1008CtrllinePhotodiodeValueTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 214)
)
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeValueTable.setStatus("current")
_Pm1008CtrllinePhotodiodeValueEntry_Object = MibTableRow
pm1008CtrllinePhotodiodeValueEntry = _Pm1008CtrllinePhotodiodeValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 214, 1)
)
pm1008CtrllinePhotodiodeValueEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrllinePhotodiodeValueIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeValueEntry.setStatus("current")


class _Pm1008CtrllinePhotodiodeValueIndex_Type(Integer32):
    """Custom type pm1008CtrllinePhotodiodeValueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrllinePhotodiodeValueIndex_Type.__name__ = "Integer32"
_Pm1008CtrllinePhotodiodeValueIndex_Object = MibTableColumn
pm1008CtrllinePhotodiodeValueIndex = _Pm1008CtrllinePhotodiodeValueIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 214, 1, 1),
    _Pm1008CtrllinePhotodiodeValueIndex_Type()
)
pm1008CtrllinePhotodiodeValueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeValueIndex.setStatus("current")
_Pm1008CtrllinePhotodiodeValuePortn_Type = Pm1008AdjustValue
_Pm1008CtrllinePhotodiodeValuePortn_Object = MibTableColumn
pm1008CtrllinePhotodiodeValuePortn = _Pm1008CtrllinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 214, 1, 2),
    _Pm1008CtrllinePhotodiodeValuePortn_Type()
)
pm1008CtrllinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrllinePhotodiodeValuePortn.setStatus("current")
_Pm1008CtrllinePowerLaserTable_Object = MibTable
pm1008CtrllinePowerLaserTable = _Pm1008CtrllinePowerLaserTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 215)
)
if mibBuilder.loadTexts:
    pm1008CtrllinePowerLaserTable.setStatus("current")
_Pm1008CtrllinePowerLaserEntry_Object = MibTableRow
pm1008CtrllinePowerLaserEntry = _Pm1008CtrllinePowerLaserEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 215, 1)
)
pm1008CtrllinePowerLaserEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CtrllinePowerLaserIndex"),
)
if mibBuilder.loadTexts:
    pm1008CtrllinePowerLaserEntry.setStatus("current")


class _Pm1008CtrllinePowerLaserIndex_Type(Integer32):
    """Custom type pm1008CtrllinePowerLaserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CtrllinePowerLaserIndex_Type.__name__ = "Integer32"
_Pm1008CtrllinePowerLaserIndex_Object = MibTableColumn
pm1008CtrllinePowerLaserIndex = _Pm1008CtrllinePowerLaserIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 215, 1, 1),
    _Pm1008CtrllinePowerLaserIndex_Type()
)
pm1008CtrllinePowerLaserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CtrllinePowerLaserIndex.setStatus("current")


class _Pm1008CtrllinePowerLaserPortn_Type(Integer32):
    """Custom type pm1008CtrllinePowerLaserPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Pm1008CtrllinePowerLaserPortn_Type.__name__ = "Integer32"
_Pm1008CtrllinePowerLaserPortn_Object = MibTableColumn
pm1008CtrllinePowerLaserPortn = _Pm1008CtrllinePowerLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 6, 3, 215, 1, 2),
    _Pm1008CtrllinePowerLaserPortn_Type()
)
pm1008CtrllinePowerLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CtrllinePowerLaserPortn.setStatus("current")
_Pm1008ri_ObjectIdentity = ObjectIdentity
pm1008ri = _Pm1008ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7)
)
_Pm1008riTable_ObjectIdentity = ObjectIdentity
pm1008riTable = _Pm1008riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1)
)
_Pm1008RinvSfpTable_Object = MibTable
pm1008RinvSfpTable = _Pm1008RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1008RinvSfpTable.setStatus("current")
_Pm1008RinvSfpEntry_Object = MibTableRow
pm1008RinvSfpEntry = _Pm1008RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 1, 1)
)
pm1008RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm1008RinvSfpEntry.setStatus("current")


class _Pm1008RinvSfpIndex_Type(Integer32):
    """Custom type pm1008RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1008RinvSfpIndex_Type.__name__ = "Integer32"
_Pm1008RinvSfpIndex_Object = MibTableColumn
pm1008RinvSfpIndex = _Pm1008RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 1, 1, 1),
    _Pm1008RinvSfpIndex_Type()
)
pm1008RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvSfpIndex.setStatus("current")
_Pm1008Rinvsfp_Type = DisplayString
_Pm1008Rinvsfp_Object = MibTableColumn
pm1008Rinvsfp = _Pm1008Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 1, 1, 2),
    _Pm1008Rinvsfp_Type()
)
pm1008Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008Rinvsfp.setStatus("current")
_Pm1008RinvLineTable_Object = MibTable
pm1008RinvLineTable = _Pm1008RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1008RinvLineTable.setStatus("current")
_Pm1008RinvLineEntry_Object = MibTableRow
pm1008RinvLineEntry = _Pm1008RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 2, 1)
)
pm1008RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1008RinvLineEntry.setStatus("current")


class _Pm1008RinvLineIndex_Type(Integer32):
    """Custom type pm1008RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1008RinvLineIndex_Type.__name__ = "Integer32"
_Pm1008RinvLineIndex_Object = MibTableColumn
pm1008RinvLineIndex = _Pm1008RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 2, 1, 1),
    _Pm1008RinvLineIndex_Type()
)
pm1008RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvLineIndex.setStatus("current")
_Pm1008RinvxfpLine_Type = DisplayString
_Pm1008RinvxfpLine_Object = MibTableColumn
pm1008RinvxfpLine = _Pm1008RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 1, 2, 1, 2),
    _Pm1008RinvxfpLine_Type()
)
pm1008RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvxfpLine.setStatus("current")
_Pm1008RinvReloadInventory_Type = EkiOnOff
_Pm1008RinvReloadInventory_Object = MibScalar
pm1008RinvReloadInventory = _Pm1008RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 2),
    _Pm1008RinvReloadInventory_Type()
)
pm1008RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008RinvReloadInventory.setStatus("current")
_Pm1008RinvHwPlatform_Type = DisplayString
_Pm1008RinvHwPlatform_Object = MibScalar
pm1008RinvHwPlatform = _Pm1008RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 3),
    _Pm1008RinvHwPlatform_Type()
)
pm1008RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvHwPlatform.setStatus("current")
_Pm1008RinvModulePlatform_Type = DisplayString
_Pm1008RinvModulePlatform_Object = MibScalar
pm1008RinvModulePlatform = _Pm1008RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 4),
    _Pm1008RinvModulePlatform_Type()
)
pm1008RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvModulePlatform.setStatus("current")
_Pm1008RinvSwPlatform_Type = DisplayString
_Pm1008RinvSwPlatform_Object = MibScalar
pm1008RinvSwPlatform = _Pm1008RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 5),
    _Pm1008RinvSwPlatform_Type()
)
pm1008RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvSwPlatform.setStatus("current")
_Pm1008RinvGwPlatform_Type = DisplayString
_Pm1008RinvGwPlatform_Object = MibScalar
pm1008RinvGwPlatform = _Pm1008RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 7, 6),
    _Pm1008RinvGwPlatform_Type()
)
pm1008RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008RinvGwPlatform.setStatus("current")
_Pm1008download_ObjectIdentity = ObjectIdentity
pm1008download = _Pm1008download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8)
)
_Pm1008DwlOther_ObjectIdentity = ObjectIdentity
pm1008DwlOther = _Pm1008DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1)
)
_Pm1008DwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1008DwlrestartProcess = _Pm1008DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 0)
)
_Pm1008DwlWarmRestartProcessed_Type = EkiOnOff
_Pm1008DwlWarmRestartProcessed_Object = MibScalar
pm1008DwlWarmRestartProcessed = _Pm1008DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 0, 1),
    _Pm1008DwlWarmRestartProcessed_Type()
)
pm1008DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlWarmRestartProcessed.setStatus("current")
_Pm1008DwlColdRestartProcessed_Type = EkiOnOff
_Pm1008DwlColdRestartProcessed_Object = MibScalar
pm1008DwlColdRestartProcessed = _Pm1008DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 0, 2),
    _Pm1008DwlColdRestartProcessed_Type()
)
pm1008DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlColdRestartProcessed.setStatus("current")
_Pm1008DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1008DwlswBanksUsed = _Pm1008DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 1)
)
_Pm1008DwlSwBank1Used_Type = EkiOnOff
_Pm1008DwlSwBank1Used_Object = MibScalar
pm1008DwlSwBank1Used = _Pm1008DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 1, 1),
    _Pm1008DwlSwBank1Used_Type()
)
pm1008DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlSwBank1Used.setStatus("current")
_Pm1008DwlSwBank2Used_Type = EkiOnOff
_Pm1008DwlSwBank2Used_Object = MibScalar
pm1008DwlSwBank2Used = _Pm1008DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 1, 2),
    _Pm1008DwlSwBank2Used_Type()
)
pm1008DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlSwBank2Used.setStatus("current")
_Pm1008DwlSwBank1Notempty_Type = EkiOnOff
_Pm1008DwlSwBank1Notempty_Object = MibScalar
pm1008DwlSwBank1Notempty = _Pm1008DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 1, 5),
    _Pm1008DwlSwBank1Notempty_Type()
)
pm1008DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlSwBank1Notempty.setStatus("current")
_Pm1008DwlSwBank2Notempty_Type = EkiOnOff
_Pm1008DwlSwBank2Notempty_Object = MibScalar
pm1008DwlSwBank2Notempty = _Pm1008DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 1, 6),
    _Pm1008DwlSwBank2Notempty_Type()
)
pm1008DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlSwBank2Notempty.setStatus("current")
_Pm1008DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1008DwlgwBanksUsed = _Pm1008DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2)
)
_Pm1008DwlGwBank1Used_Type = EkiOnOff
_Pm1008DwlGwBank1Used_Object = MibScalar
pm1008DwlGwBank1Used = _Pm1008DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 1),
    _Pm1008DwlGwBank1Used_Type()
)
pm1008DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank1Used.setStatus("current")
_Pm1008DwlGwBank2Used_Type = EkiOnOff
_Pm1008DwlGwBank2Used_Object = MibScalar
pm1008DwlGwBank2Used = _Pm1008DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 2),
    _Pm1008DwlGwBank2Used_Type()
)
pm1008DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank2Used.setStatus("current")
_Pm1008DwlGwBank3Used_Type = EkiOnOff
_Pm1008DwlGwBank3Used_Object = MibScalar
pm1008DwlGwBank3Used = _Pm1008DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 3),
    _Pm1008DwlGwBank3Used_Type()
)
pm1008DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank3Used.setStatus("current")
_Pm1008DwlGwBank4Used_Type = EkiOnOff
_Pm1008DwlGwBank4Used_Object = MibScalar
pm1008DwlGwBank4Used = _Pm1008DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 4),
    _Pm1008DwlGwBank4Used_Type()
)
pm1008DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank4Used.setStatus("current")
_Pm1008DwlGwBank1Notempty_Type = EkiOnOff
_Pm1008DwlGwBank1Notempty_Object = MibScalar
pm1008DwlGwBank1Notempty = _Pm1008DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 5),
    _Pm1008DwlGwBank1Notempty_Type()
)
pm1008DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank1Notempty.setStatus("current")
_Pm1008DwlGwBank2Notempty_Type = EkiOnOff
_Pm1008DwlGwBank2Notempty_Object = MibScalar
pm1008DwlGwBank2Notempty = _Pm1008DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 6),
    _Pm1008DwlGwBank2Notempty_Type()
)
pm1008DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank2Notempty.setStatus("current")
_Pm1008DwlGwBank3Notempty_Type = EkiOnOff
_Pm1008DwlGwBank3Notempty_Object = MibScalar
pm1008DwlGwBank3Notempty = _Pm1008DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 7),
    _Pm1008DwlGwBank3Notempty_Type()
)
pm1008DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank3Notempty.setStatus("current")
_Pm1008DwlGwBank4Notempty_Type = EkiOnOff
_Pm1008DwlGwBank4Notempty_Object = MibScalar
pm1008DwlGwBank4Notempty = _Pm1008DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 1, 2, 8),
    _Pm1008DwlGwBank4Notempty_Type()
)
pm1008DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008DwlGwBank4Notempty.setStatus("current")
_Pm1008DwlClient_ObjectIdentity = ObjectIdentity
pm1008DwlClient = _Pm1008DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 2)
)
_Pm1008DwlLine_ObjectIdentity = ObjectIdentity
pm1008DwlLine = _Pm1008DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 8, 3)
)
_Pm1008Config_ObjectIdentity = ObjectIdentity
pm1008Config = _Pm1008Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9)
)
_Pm1008CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1008CfgAccessCAisCsf = _Pm1008CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1)
)
_Pm1008CfgClientcaiscsfTable_Object = MibTable
pm1008CfgClientcaiscsfTable = _Pm1008CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1008CfgClientcaiscsfTable.setStatus("current")
_Pm1008CfgClientcaiscsfEntry_Object = MibTableRow
pm1008CfgClientcaiscsfEntry = _Pm1008CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1)
)
pm1008CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgClientcaiscsfEntry.setStatus("current")


class _Pm1008CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1008CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1008CfgClientcaiscsfIndex_Object = MibTableColumn
pm1008CfgClientcaiscsfIndex = _Pm1008CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 1),
    _Pm1008CfgClientcaiscsfIndex_Type()
)
pm1008CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgClientcaiscsfIndex.setStatus("current")


class _Pm1008CfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1008CfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1008CfgCAisModePortn_Object = MibTableColumn
pm1008CfgCAisModePortn = _Pm1008CfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 3),
    _Pm1008CfgCAisModePortn_Type()
)
pm1008CfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgCAisModePortn.setStatus("current")


class _Pm1008CfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1008CfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgUpAccessioAlmPortn_Object = MibTableColumn
pm1008CfgUpAccessioAlmPortn = _Pm1008CfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 9),
    _Pm1008CfgUpAccessioAlmPortn_Type()
)
pm1008CfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgUpAccessioAlmPortn.setStatus("current")


class _Pm1008CfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1008CfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1008CfgUpMapperDeAlmPortn = _Pm1008CfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 10),
    _Pm1008CfgUpMapperDeAlmPortn_Type()
)
pm1008CfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1008CfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1008CfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgDownAccessioAlmPortn_Object = MibTableColumn
pm1008CfgDownAccessioAlmPortn = _Pm1008CfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 17),
    _Pm1008CfgDownAccessioAlmPortn_Type()
)
pm1008CfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgDownAccessioAlmPortn.setStatus("current")


class _Pm1008CfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1008CfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1008CfgDownMapperDeAlmPortn = _Pm1008CfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 18),
    _Pm1008CfgDownMapperDeAlmPortn_Type()
)
pm1008CfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1008CfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1008CfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgDownDfrmAlmPortn_Object = MibTableColumn
pm1008CfgDownDfrmAlmPortn = _Pm1008CfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 19),
    _Pm1008CfgDownDfrmAlmPortn_Type()
)
pm1008CfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgDownDfrmAlmPortn.setStatus("current")


class _Pm1008CfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1008CfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1008CfgDownLineSyncAlarmsPortn = _Pm1008CfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 1, 1, 1, 20),
    _Pm1008CfgDownLineSyncAlarmsPortn_Type()
)
pm1008CfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pm1008CfgStartup_ObjectIdentity = ObjectIdentity
pm1008CfgStartup = _Pm1008CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2)
)
_Pm1008CfgClientStartupTable_Object = MibTable
pm1008CfgClientStartupTable = _Pm1008CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1008CfgClientStartupTable.setStatus("current")
_Pm1008CfgClientStartupEntry_Object = MibTableRow
pm1008CfgClientStartupEntry = _Pm1008CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 1, 1)
)
pm1008CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgClientStartupEntry.setStatus("current")


class _Pm1008CfgClientStartupIndex_Type(Integer32):
    """Custom type pm1008CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1008CfgClientStartupIndex_Object = MibTableColumn
pm1008CfgClientStartupIndex = _Pm1008CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 1, 1, 1),
    _Pm1008CfgClientStartupIndex_Type()
)
pm1008CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgClientStartupIndex.setStatus("current")


class _Pm1008CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1008CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgSystConfPortPortn_Object = MibTableColumn
pm1008CfgSystConfPortPortn = _Pm1008CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 1, 1, 3),
    _Pm1008CfgSystConfPortPortn_Type()
)
pm1008CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgSystConfPortPortn.setStatus("current")


class _Pm1008CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1008CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgNetConfPortPortn_Object = MibTableColumn
pm1008CfgNetConfPortPortn = _Pm1008CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 1, 1, 4),
    _Pm1008CfgNetConfPortPortn_Type()
)
pm1008CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgNetConfPortPortn.setStatus("current")


class _Pm1008CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm1008CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgOptionsPortPortn_Object = MibTableColumn
pm1008CfgOptionsPortPortn = _Pm1008CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 1, 1, 6),
    _Pm1008CfgOptionsPortPortn_Type()
)
pm1008CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgOptionsPortPortn.setStatus("current")
_Pm1008tablelineStartup_ObjectIdentity = ObjectIdentity
pm1008tablelineStartup = _Pm1008tablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 2)
)


class _Pm1008CfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1008CfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1008CfgsystConfLine1_Object = MibScalar
pm1008CfgsystConfLine1 = _Pm1008CfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 2, 2),
    _Pm1008CfgsystConfLine1_Type()
)
pm1008CfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgsystConfLine1.setStatus("current")


class _Pm1008CfglineOptions1_Type(Unsigned32):
    """Custom type pm1008CfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1008CfglineOptions1_Object = MibScalar
pm1008CfglineOptions1 = _Pm1008CfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 2, 5),
    _Pm1008CfglineOptions1_Type()
)
pm1008CfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfglineOptions1.setStatus("current")


class _Pm1008CfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1008CfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1008CfgsystConfLine2_Object = MibScalar
pm1008CfgsystConfLine2 = _Pm1008CfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 2, 6),
    _Pm1008CfgsystConfLine2_Type()
)
pm1008CfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgsystConfLine2.setStatus("current")


class _Pm1008CfglineSelection_Type(Unsigned32):
    """Custom type pm1008CfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfglineSelection_Type.__name__ = "Unsigned32"
_Pm1008CfglineSelection_Object = MibScalar
pm1008CfglineSelection = _Pm1008CfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 2, 7),
    _Pm1008CfglineSelection_Type()
)
pm1008CfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfglineSelection.setStatus("current")
_Pm1008CfgXfpTable_Object = MibTable
pm1008CfgXfpTable = _Pm1008CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1008CfgXfpTable.setStatus("current")
_Pm1008CfgXfpEntry_Object = MibTableRow
pm1008CfgXfpEntry = _Pm1008CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 3, 1)
)
pm1008CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgXfpEntry.setStatus("current")


class _Pm1008CfgXfpIndex_Type(Integer32):
    """Custom type pm1008CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgXfpIndex_Type.__name__ = "Integer32"
_Pm1008CfgXfpIndex_Object = MibTableColumn
pm1008CfgXfpIndex = _Pm1008CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 3, 1, 1),
    _Pm1008CfgXfpIndex_Type()
)
pm1008CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgXfpIndex.setStatus("current")


class _Pm1008CfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1008CfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgSystConfXfpPortn_Object = MibTableColumn
pm1008CfgSystConfXfpPortn = _Pm1008CfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 3, 1, 3),
    _Pm1008CfgSystConfXfpPortn_Type()
)
pm1008CfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgSystConfXfpPortn.setStatus("current")


class _Pm1008CfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1008CfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgDataRateConfXfpPortn_Object = MibTableColumn
pm1008CfgDataRateConfXfpPortn = _Pm1008CfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 2, 3, 1, 4),
    _Pm1008CfgDataRateConfXfpPortn_Type()
)
pm1008CfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1008CfgLabels_ObjectIdentity = ObjectIdentity
pm1008CfgLabels = _Pm1008CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3)
)
_Pm1008CfgLabelclientTable_Object = MibTable
pm1008CfgLabelclientTable = _Pm1008CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1008CfgLabelclientTable.setStatus("current")
_Pm1008CfgLabelclientEntry_Object = MibTableRow
pm1008CfgLabelclientEntry = _Pm1008CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 1, 1)
)
pm1008CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgLabelclientEntry.setStatus("current")


class _Pm1008CfgLabelclientIndex_Type(Integer32):
    """Custom type pm1008CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1008CfgLabelclientIndex_Object = MibTableColumn
pm1008CfgLabelclientIndex = _Pm1008CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 1, 1, 1),
    _Pm1008CfgLabelclientIndex_Type()
)
pm1008CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgLabelclientIndex.setStatus("current")


class _Pm1008CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1008CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1008CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1008CfgLabelclientPortn_Object = MibTableColumn
pm1008CfgLabelclientPortn = _Pm1008CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 1, 1, 3),
    _Pm1008CfgLabelclientPortn_Type()
)
pm1008CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLabelclientPortn.setStatus("current")
_Pm1008CfgLabellineTable_Object = MibTable
pm1008CfgLabellineTable = _Pm1008CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1008CfgLabellineTable.setStatus("current")
_Pm1008CfgLabellineEntry_Object = MibTableRow
pm1008CfgLabellineEntry = _Pm1008CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 2, 1)
)
pm1008CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgLabellineEntry.setStatus("current")


class _Pm1008CfgLabellineIndex_Type(Integer32):
    """Custom type pm1008CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1008CfgLabellineIndex_Object = MibTableColumn
pm1008CfgLabellineIndex = _Pm1008CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 2, 1, 1),
    _Pm1008CfgLabellineIndex_Type()
)
pm1008CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgLabellineIndex.setStatus("current")


class _Pm1008CfgLabellinePortn_Type(DisplayString):
    """Custom type pm1008CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1008CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1008CfgLabellinePortn_Object = MibTableColumn
pm1008CfgLabellinePortn = _Pm1008CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 3, 2, 1, 3),
    _Pm1008CfgLabellinePortn_Type()
)
pm1008CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLabellinePortn.setStatus("current")
_Pm1008CfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1008CfgStartuptlh = _Pm1008CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4)
)
_Pm1008CfgOtxtlhTable_Object = MibTable
pm1008CfgOtxtlhTable = _Pm1008CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1008CfgOtxtlhTable.setStatus("current")
_Pm1008CfgOtxtlhEntry_Object = MibTableRow
pm1008CfgOtxtlhEntry = _Pm1008CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1)
)
pm1008CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgOtxtlhEntry.setStatus("current")


class _Pm1008CfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1008CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1008CfgOtxtlhIndex_Object = MibTableColumn
pm1008CfgOtxtlhIndex = _Pm1008CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 1),
    _Pm1008CfgOtxtlhIndex_Type()
)
pm1008CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgOtxtlhIndex.setStatus("current")


class _Pm1008CfgNuPortn_Type(Unsigned32):
    """Custom type pm1008CfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgNuPortn_Object = MibTableColumn
pm1008CfgNuPortn = _Pm1008CfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 3),
    _Pm1008CfgNuPortn_Type()
)
pm1008CfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgNuPortn.setStatus("deprecated")


class _Pm1008CfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1008CfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLineDitherRatePortn_Object = MibTableColumn
pm1008CfgLineDitherRatePortn = _Pm1008CfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 4),
    _Pm1008CfgLineDitherRatePortn_Type()
)
pm1008CfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLineDitherRatePortn.setStatus("current")


class _Pm1008CfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1008CfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLineDitherFhzPortn_Object = MibTableColumn
pm1008CfgLineDitherFhzPortn = _Pm1008CfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 5),
    _Pm1008CfgLineDitherFhzPortn_Type()
)
pm1008CfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLineDitherFhzPortn.setStatus("current")


class _Pm1008CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1008CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLinePwrLaserPortn_Object = MibTableColumn
pm1008CfgLinePwrLaserPortn = _Pm1008CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 6),
    _Pm1008CfgLinePwrLaserPortn_Type()
)
pm1008CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLinePwrLaserPortn.setStatus("current")


class _Pm1008CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1008CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLineFCurrentPortn_Object = MibTableColumn
pm1008CfgLineFCurrentPortn = _Pm1008CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 7),
    _Pm1008CfgLineFCurrentPortn_Type()
)
pm1008CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLineFCurrentPortn.setStatus("current")


class _Pm1008CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1008CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLineGridCurrentPortn_Object = MibTableColumn
pm1008CfgLineGridCurrentPortn = _Pm1008CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 8),
    _Pm1008CfgLineGridCurrentPortn_Type()
)
pm1008CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLineGridCurrentPortn.setStatus("current")


class _Pm1008CfgFPortn_Type(Unsigned32):
    """Custom type pm1008CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgFPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgFPortn_Object = MibTableColumn
pm1008CfgFPortn = _Pm1008CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 9),
    _Pm1008CfgFPortn_Type()
)
pm1008CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgFPortn.setStatus("current")


class _Pm1008CfgReservedPortn_Type(Unsigned32):
    """Custom type pm1008CfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgReservedPortn_Object = MibTableColumn
pm1008CfgReservedPortn = _Pm1008CfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 10),
    _Pm1008CfgReservedPortn_Type()
)
pm1008CfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgReservedPortn.setStatus("deprecated")


class _Pm1008CfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1008CfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1008CfgLinePhotodiodeModePortn = _Pm1008CfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 11),
    _Pm1008CfgLinePhotodiodeModePortn_Type()
)
pm1008CfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1008CfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1008CfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1008CfgLinePhotodiodeValuePortn = _Pm1008CfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 4, 1, 1, 12),
    _Pm1008CfgLinePhotodiodeValuePortn_Type()
)
pm1008CfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1008CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1008CfgStartuptablefive = _Pm1008CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5)
)
_Pm1008CfgOtxtlhcapabilitiesTable_Object = MibTable
pm1008CfgOtxtlhcapabilitiesTable = _Pm1008CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1008CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1008CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1008CfgOtxtlhcapabilitiesEntry = _Pm1008CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1)
)
pm1008CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1008CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1008CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1008CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1008CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1008CfgOtxtlhcapabilitiesIndex = _Pm1008CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1, 1),
    _Pm1008CfgOtxtlhcapabilitiesIndex_Type()
)
pm1008CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1008CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1008CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1008CfgComponentTypePortn_Object = MibTableColumn
pm1008CfgComponentTypePortn = _Pm1008CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1, 3),
    _Pm1008CfgComponentTypePortn_Type()
)
pm1008CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgComponentTypePortn.setStatus("current")


class _Pm1008CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1008CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgMiscellaneousPortn_Object = MibTableColumn
pm1008CfgMiscellaneousPortn = _Pm1008CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1, 4),
    _Pm1008CfgMiscellaneousPortn_Type()
)
pm1008CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgMiscellaneousPortn.setStatus("current")


class _Pm1008CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1008CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgFirstChannelPortn_Object = MibTableColumn
pm1008CfgFirstChannelPortn = _Pm1008CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1, 5),
    _Pm1008CfgFirstChannelPortn_Type()
)
pm1008CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgFirstChannelPortn.setStatus("current")


class _Pm1008CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1008CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgLastChannelPortn_Object = MibTableColumn
pm1008CfgLastChannelPortn = _Pm1008CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1, 6),
    _Pm1008CfgLastChannelPortn_Type()
)
pm1008CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgLastChannelPortn.setStatus("current")


class _Pm1008CfgGridPortn_Type(Unsigned32):
    """Custom type pm1008CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1008CfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1008CfgGridPortn_Object = MibTableColumn
pm1008CfgGridPortn = _Pm1008CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 5, 1, 1, 7),
    _Pm1008CfgGridPortn_Type()
)
pm1008CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008CfgGridPortn.setStatus("current")
_Pm1008CfgWriteConfiguration_Type = EkiOnOff
_Pm1008CfgWriteConfiguration_Object = MibScalar
pm1008CfgWriteConfiguration = _Pm1008CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 9, 257),
    _Pm1008CfgWriteConfiguration_Type()
)
pm1008CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008CfgWriteConfiguration.setStatus("current")
_Pm1008traps_ObjectIdentity = ObjectIdentity
pm1008traps = _Pm1008traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10)
)


class _Pm1008trapPortNumber_Type(Integer32):
    """Custom type pm1008trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1008trapPortNumber_Type.__name__ = "Integer32"
_Pm1008trapPortNumber_Object = MibScalar
pm1008trapPortNumber = _Pm1008trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 2),
    _Pm1008trapPortNumber_Type()
)
pm1008trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008trapPortNumber.setStatus("current")


class _Pm1008trapLineNumber_Type(Integer32):
    """Custom type pm1008trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1008trapLineNumber_Type.__name__ = "Integer32"
_Pm1008trapLineNumber_Object = MibScalar
pm1008trapLineNumber = _Pm1008trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 3),
    _Pm1008trapLineNumber_Type()
)
pm1008trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008trapLineNumber.setStatus("current")


class _Pm1008trapBoardNumber_Type(Integer32):
    """Custom type pm1008trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1008trapBoardNumber_Type.__name__ = "Integer32"
_Pm1008trapBoardNumber_Object = MibScalar
pm1008trapBoardNumber = _Pm1008trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 4),
    _Pm1008trapBoardNumber_Type()
)
pm1008trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008trapBoardNumber.setStatus("current")
_Pm1008Monitoring_ObjectIdentity = ObjectIdentity
pm1008Monitoring = _Pm1008Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11)
)
_Pm1008MonOther_ObjectIdentity = ObjectIdentity
pm1008MonOther = _Pm1008MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 1)
)
_Pm1008MonRmon_ObjectIdentity = ObjectIdentity
pm1008MonRmon = _Pm1008MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 1, 3)
)
_Pm1008MonCountersReset_Type = EkiOnOff
_Pm1008MonCountersReset_Object = MibScalar
pm1008MonCountersReset = _Pm1008MonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 1, 3, 359),
    _Pm1008MonCountersReset_Type()
)
pm1008MonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008MonCountersReset.setStatus("current")
_Pm1008MonCountersStop_Type = EkiOnOff
_Pm1008MonCountersStop_Object = MibScalar
pm1008MonCountersStop = _Pm1008MonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 1, 3, 360),
    _Pm1008MonCountersStop_Type()
)
pm1008MonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1008MonCountersStop.setStatus("current")
_Pm1008MonClient_ObjectIdentity = ObjectIdentity
pm1008MonClient = _Pm1008MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2)
)
_Pm1008MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm1008MonClientRmonCounter = _Pm1008MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4)
)
_Pm1008MonupRmonByteCntTable_Object = MibTable
pm1008MonupRmonByteCntTable = _Pm1008MonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm1008MonupRmonByteCntTable.setStatus("current")
_Pm1008MonupRmonByteCntEntry_Object = MibTableRow
pm1008MonupRmonByteCntEntry = _Pm1008MonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 16, 1)
)
pm1008MonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008MonupRmonByteCntEntry.setStatus("current")


class _Pm1008MonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm1008MonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1008MonupRmonByteCntIndex_Object = MibTableColumn
pm1008MonupRmonByteCntIndex = _Pm1008MonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 16, 1, 1),
    _Pm1008MonupRmonByteCntIndex_Type()
)
pm1008MonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonByteCntIndex.setStatus("current")
_Pm1008MonupRmonByteCntValuePortn_Type = Counter64
_Pm1008MonupRmonByteCntValuePortn_Object = MibTableColumn
pm1008MonupRmonByteCntValuePortn = _Pm1008MonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 16, 1, 2),
    _Pm1008MonupRmonByteCntValuePortn_Type()
)
pm1008MonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonByteCntValuePortn.setStatus("current")
_Pm1008MonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1008MonupRmonByteCntErrorPortn_Object = MibTableColumn
pm1008MonupRmonByteCntErrorPortn = _Pm1008MonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 16, 1, 3),
    _Pm1008MonupRmonByteCntErrorPortn_Type()
)
pm1008MonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonByteCntErrorPortn.setStatus("current")
_Pm1008MonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1008MonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm1008MonupRmonByteCntOverloadPortn = _Pm1008MonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 16, 1, 4),
    _Pm1008MonupRmonByteCntOverloadPortn_Type()
)
pm1008MonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonByteCntOverloadPortn.setStatus("current")
_Pm1008MonupRmonCrcErrorCntTable_Object = MibTable
pm1008MonupRmonCrcErrorCntTable = _Pm1008MonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pm1008MonupRmonCrcErrorCntTable.setStatus("current")
_Pm1008MonupRmonCrcErrorCntEntry_Object = MibTableRow
pm1008MonupRmonCrcErrorCntEntry = _Pm1008MonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 24, 1)
)
pm1008MonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008MonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm1008MonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1008MonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1008MonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm1008MonupRmonCrcErrorCntIndex = _Pm1008MonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 24, 1, 1),
    _Pm1008MonupRmonCrcErrorCntIndex_Type()
)
pm1008MonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonCrcErrorCntIndex.setStatus("current")
_Pm1008MonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1008MonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1008MonupRmonCrcErrorCntValuePortn = _Pm1008MonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 24, 1, 2),
    _Pm1008MonupRmonCrcErrorCntValuePortn_Type()
)
pm1008MonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1008MonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1008MonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1008MonupRmonCrcErrorCntErrorPortn = _Pm1008MonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 24, 1, 3),
    _Pm1008MonupRmonCrcErrorCntErrorPortn_Type()
)
pm1008MonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1008MonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1008MonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1008MonupRmonCrcErrorCntOverloadPortn = _Pm1008MonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 24, 1, 4),
    _Pm1008MonupRmonCrcErrorCntOverloadPortn_Type()
)
pm1008MonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1008MonupRmonPacketsCntTable_Object = MibTable
pm1008MonupRmonPacketsCntTable = _Pm1008MonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm1008MonupRmonPacketsCntTable.setStatus("current")
_Pm1008MonupRmonPacketsCntEntry_Object = MibTableRow
pm1008MonupRmonPacketsCntEntry = _Pm1008MonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 32, 1)
)
pm1008MonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008MonupRmonPacketsCntEntry.setStatus("current")


class _Pm1008MonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1008MonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1008MonupRmonPacketsCntIndex_Object = MibTableColumn
pm1008MonupRmonPacketsCntIndex = _Pm1008MonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 32, 1, 1),
    _Pm1008MonupRmonPacketsCntIndex_Type()
)
pm1008MonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonPacketsCntIndex.setStatus("current")
_Pm1008MonupRmonPacketsCntValuePortn_Type = Counter64
_Pm1008MonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm1008MonupRmonPacketsCntValuePortn = _Pm1008MonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 32, 1, 2),
    _Pm1008MonupRmonPacketsCntValuePortn_Type()
)
pm1008MonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonPacketsCntValuePortn.setStatus("current")
_Pm1008MonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1008MonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1008MonupRmonPacketsCntErrorPortn = _Pm1008MonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 32, 1, 3),
    _Pm1008MonupRmonPacketsCntErrorPortn_Type()
)
pm1008MonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm1008MonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1008MonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1008MonupRmonPacketsCntOverloadPortn = _Pm1008MonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 32, 1, 4),
    _Pm1008MonupRmonPacketsCntOverloadPortn_Type()
)
pm1008MonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1008MonupRmonBroadcastCntTable_Object = MibTable
pm1008MonupRmonBroadcastCntTable = _Pm1008MonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pm1008MonupRmonBroadcastCntTable.setStatus("current")
_Pm1008MonupRmonBroadcastCntEntry_Object = MibTableRow
pm1008MonupRmonBroadcastCntEntry = _Pm1008MonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 40, 1)
)
pm1008MonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008MonupRmonBroadcastCntEntry.setStatus("current")


class _Pm1008MonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1008MonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1008MonupRmonBroadcastCntIndex_Object = MibTableColumn
pm1008MonupRmonBroadcastCntIndex = _Pm1008MonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 40, 1, 1),
    _Pm1008MonupRmonBroadcastCntIndex_Type()
)
pm1008MonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonBroadcastCntIndex.setStatus("current")
_Pm1008MonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm1008MonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1008MonupRmonBroadcastCntValuePortn = _Pm1008MonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 40, 1, 2),
    _Pm1008MonupRmonBroadcastCntValuePortn_Type()
)
pm1008MonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm1008MonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1008MonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1008MonupRmonBroadcastCntErrorPortn = _Pm1008MonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 40, 1, 3),
    _Pm1008MonupRmonBroadcastCntErrorPortn_Type()
)
pm1008MonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1008MonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1008MonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1008MonupRmonBroadcastCntOverloadPortn = _Pm1008MonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 40, 1, 4),
    _Pm1008MonupRmonBroadcastCntOverloadPortn_Type()
)
pm1008MonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1008MonupRmonMulticastCntTable_Object = MibTable
pm1008MonupRmonMulticastCntTable = _Pm1008MonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm1008MonupRmonMulticastCntTable.setStatus("current")
_Pm1008MonupRmonMulticastCntEntry_Object = MibTableRow
pm1008MonupRmonMulticastCntEntry = _Pm1008MonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 48, 1)
)
pm1008MonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1008-MIB", "pm1008MonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1008MonupRmonMulticastCntEntry.setStatus("current")


class _Pm1008MonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1008MonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1008MonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1008MonupRmonMulticastCntIndex_Object = MibTableColumn
pm1008MonupRmonMulticastCntIndex = _Pm1008MonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 48, 1, 1),
    _Pm1008MonupRmonMulticastCntIndex_Type()
)
pm1008MonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonMulticastCntIndex.setStatus("current")
_Pm1008MonupRmonMulticastCntValuePortn_Type = Counter64
_Pm1008MonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm1008MonupRmonMulticastCntValuePortn = _Pm1008MonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 48, 1, 2),
    _Pm1008MonupRmonMulticastCntValuePortn_Type()
)
pm1008MonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonMulticastCntValuePortn.setStatus("current")
_Pm1008MonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1008MonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1008MonupRmonMulticastCntErrorPortn = _Pm1008MonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 48, 1, 3),
    _Pm1008MonupRmonMulticastCntErrorPortn_Type()
)
pm1008MonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm1008MonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1008MonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1008MonupRmonMulticastCntOverloadPortn = _Pm1008MonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 3, 11, 2, 4, 48, 1, 4),
    _Pm1008MonupRmonMulticastCntOverloadPortn_Type()
)
pm1008MonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1008MonupRmonMulticastCntOverloadPortn.setStatus("current")

# Managed Objects groups


# Notification objects

pm1008LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 30)
)
pm1008LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapLineNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1008LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 31)
)
pm1008LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapLineNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1008LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 32)
)
pm1008LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapLineNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1008LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 33)
)
pm1008LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapLineNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1008LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 34)
)
pm1008LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmLineFailPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008AlmLineHwFailPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapLineNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008LineTrapCritGoesOn.setStatus(
        "current"
    )

pm1008LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 35)
)
pm1008LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmLineFailPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008AlmLineHwFailPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapLineNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008LineTrapCritGoesOff.setStatus(
        "current"
    )

pm1008ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 40)
)
pm1008ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapPortNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1008ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 41)
)
pm1008ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapPortNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1008ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 42)
)
pm1008ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapPortNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1008ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 43)
)
pm1008ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapPortNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1008ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 44)
)
pm1008ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmFailAccPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008AlmHwFailAccPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapPortNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008ClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1008ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 45)
)
pm1008ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmFailAccPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008AlmHwFailAccPortn"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapPortNumber"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008ClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1008PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 50)
)
pm1008PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmDefFuseB"),
        ("EKINOPS-Pm1008-MIB", "pm1008AlmDefFuseA"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1008PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 3, 10, 51)
)
pm1008PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1008-MIB", "pm1008AlmDefFuseB"),
        ("EKINOPS-Pm1008-MIB", "pm1008AlmDefFuseA"),
        ("EKINOPS-Pm1008-MIB", "pm1008trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1008PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1008-MIB",
    **{"Pm1008MultiRate": Pm1008MultiRate,
       "Pm1008OtxMode": Pm1008OtxMode,
       "Pm1008OtxGrid": Pm1008OtxGrid,
       "Pm1008AdjustValue": Pm1008AdjustValue,
       "Pm1008OtxChannel": Pm1008OtxChannel,
       "modulePm1008": modulePm1008,
       "pm1008alarms": pm1008alarms,
       "pm1008AlmOther": pm1008AlmOther,
       "pm1008AlmOtherNurg": pm1008AlmOtherNurg,
       "pm1008AlmsynthAlm2": pm1008AlmsynthAlm2,
       "pm1008AlmConfTableSave": pm1008AlmConfTableSave,
       "pm1008AlmInvUpload": pm1008AlmInvUpload,
       "pm1008AlmConfTableLoad": pm1008AlmConfTableLoad,
       "pm1008AlmCorrelatOff": pm1008AlmCorrelatOff,
       "pm1008AlmMaintenanceOn": pm1008AlmMaintenanceOn,
       "pm1008AlmOtherUrg": pm1008AlmOtherUrg,
       "pm1008AlmmodInitFailLevel2": pm1008AlmmodInitFailLevel2,
       "pm1008AlmLedFail": pm1008AlmLedFail,
       "pm1008AlmNextColdBootForced": pm1008AlmNextColdBootForced,
       "pm1008AlmBootUndone": pm1008AlmBootUndone,
       "pm1008AlmResetHwInitFail": pm1008AlmResetHwInitFail,
       "pm1008AlmSwInitFail": pm1008AlmSwInitFail,
       "pm1008AlmmodInitFailLevel3": pm1008AlmmodInitFailLevel3,
       "pm1008AlmGwIdentFail": pm1008AlmGwIdentFail,
       "pm1008AlmObmTypeReadFail": pm1008AlmObmTypeReadFail,
       "pm1008AlmInitModuleFail": pm1008AlmInitModuleFail,
       "pm1008AlmXfp1InitFail": pm1008AlmXfp1InitFail,
       "pm1008AlmXfp2InitFail": pm1008AlmXfp2InitFail,
       "pm1008AlmLine1InitFail": pm1008AlmLine1InitFail,
       "pm1008AlmLine2InitFail": pm1008AlmLine2InitFail,
       "pm1008AlmClient1InitFail": pm1008AlmClient1InitFail,
       "pm1008AlmClient2InitFail": pm1008AlmClient2InitFail,
       "pm1008AlmClient3InitFail": pm1008AlmClient3InitFail,
       "pm1008AlmClient4InitFail": pm1008AlmClient4InitFail,
       "pm1008AlmClient5InitFail": pm1008AlmClient5InitFail,
       "pm1008AlmClient6InitFail": pm1008AlmClient6InitFail,
       "pm1008AlmClient7InitFail": pm1008AlmClient7InitFail,
       "pm1008AlmClient8InitFail": pm1008AlmClient8InitFail,
       "pm1008AlmOtherCrit": pm1008AlmOtherCrit,
       "pm1008AlmsynthAlm0": pm1008AlmsynthAlm0,
       "pm1008AlmModGlobFail": pm1008AlmModGlobFail,
       "pm1008AlmDefFuseA": pm1008AlmDefFuseA,
       "pm1008AlmDefFuseB": pm1008AlmDefFuseB,
       "pm1008AlmClient": pm1008AlmClient,
       "pm1008AlmClientNurg": pm1008AlmClientNurg,
       "pm1008AlmsfpWarnDdmTable": pm1008AlmsfpWarnDdmTable,
       "pm1008AlmsfpWarnDdmEntry": pm1008AlmsfpWarnDdmEntry,
       "pm1008AlmsfpWarnDdmIndex": pm1008AlmsfpWarnDdmIndex,
       "pm1008AlmTxPwLowWngPortn": pm1008AlmTxPwLowWngPortn,
       "pm1008AlmTxPwrHighWngPortn": pm1008AlmTxPwrHighWngPortn,
       "pm1008AlmTxBiasLowWngPortn": pm1008AlmTxBiasLowWngPortn,
       "pm1008AlmTxBiasHighWngPortn": pm1008AlmTxBiasHighWngPortn,
       "pm1008AlmVccLowWngPortn": pm1008AlmVccLowWngPortn,
       "pm1008AlmVccHighWngPortn": pm1008AlmVccHighWngPortn,
       "pm1008AlmTempLowWngPortn": pm1008AlmTempLowWngPortn,
       "pm1008AlmTempHighWngPortn": pm1008AlmTempHighWngPortn,
       "pm1008AlmRxPwrLowWngPortn": pm1008AlmRxPwrLowWngPortn,
       "pm1008AlmRxPwrHighWngPortn": pm1008AlmRxPwrHighWngPortn,
       "pm1008AlmClientUrg": pm1008AlmClientUrg,
       "pm1008AlmsfpAlmDdmTable": pm1008AlmsfpAlmDdmTable,
       "pm1008AlmsfpAlmDdmEntry": pm1008AlmsfpAlmDdmEntry,
       "pm1008AlmsfpAlmDdmIndex": pm1008AlmsfpAlmDdmIndex,
       "pm1008AlmTxPwrLowAlaPortn": pm1008AlmTxPwrLowAlaPortn,
       "pm1008AlmTxPwrHighAlaPortn": pm1008AlmTxPwrHighAlaPortn,
       "pm1008AlmTxBiasLowAlaPortn": pm1008AlmTxBiasLowAlaPortn,
       "pm1008AlmTxBiasHighAlaPortn": pm1008AlmTxBiasHighAlaPortn,
       "pm1008AlmVccLowAlaPortn": pm1008AlmVccLowAlaPortn,
       "pm1008AlmVccHighAlaPortn": pm1008AlmVccHighAlaPortn,
       "pm1008AlmTempLowAlaPortn": pm1008AlmTempLowAlaPortn,
       "pm1008AlmTempHighAlaPortn": pm1008AlmTempHighAlaPortn,
       "pm1008AlmRxPwrLowAlaPortn": pm1008AlmRxPwrLowAlaPortn,
       "pm1008AlmRxPwrHighAlaPortn": pm1008AlmRxPwrHighAlaPortn,
       "pm1008AlmClientCrit": pm1008AlmClientCrit,
       "pm1008AlmsynthAlmPortTable": pm1008AlmsynthAlmPortTable,
       "pm1008AlmsynthAlmPortEntry": pm1008AlmsynthAlmPortEntry,
       "pm1008AlmsynthAlmPortIndex": pm1008AlmsynthAlmPortIndex,
       "pm1008AlmSfpAbsentPortn": pm1008AlmSfpAbsentPortn,
       "pm1008AlmDdmAbsentPortn": pm1008AlmDdmAbsentPortn,
       "pm1008AlmHwFailAccPortn": pm1008AlmHwFailAccPortn,
       "pm1008AlmDwLsdPortn": pm1008AlmDwLsdPortn,
       "pm1008AlmClientLocalOosPortn": pm1008AlmClientLocalOosPortn,
       "pm1008AlmClientRemoteOosPortn": pm1008AlmClientRemoteOosPortn,
       "pm1008AlmDwCaisPortn": pm1008AlmDwCaisPortn,
       "pm1008AlmSfpDdmWarningPortn": pm1008AlmSfpDdmWarningPortn,
       "pm1008AlmSfpDdmAlmPortn": pm1008AlmSfpDdmAlmPortn,
       "pm1008AlmFailAccPortn": pm1008AlmFailAccPortn,
       "pm1008AlmUpCsfPortn": pm1008AlmUpCsfPortn,
       "pm1008AlmaccessioAlmTable": pm1008AlmaccessioAlmTable,
       "pm1008AlmaccessioAlmEntry": pm1008AlmaccessioAlmEntry,
       "pm1008AlmaccessioAlmIndex": pm1008AlmaccessioAlmIndex,
       "pm1008AlmDwLasFailPortn": pm1008AlmDwLasFailPortn,
       "pm1008AlmUpLosPortn": pm1008AlmUpLosPortn,
       "pm1008AlmmapperDeAlmTable": pm1008AlmmapperDeAlmTable,
       "pm1008AlmmapperDeAlmEntry": pm1008AlmmapperDeAlmEntry,
       "pm1008AlmmapperDeAlmIndex": pm1008AlmmapperDeAlmIndex,
       "pm1008AlmUpAccOosPortn": pm1008AlmUpAccOosPortn,
       "pm1008AlmUpBufferOvlPortn": pm1008AlmUpBufferOvlPortn,
       "pm1008AlmDwCsfDetPortn": pm1008AlmDwCsfDetPortn,
       "pm1008AlmDwBufferOvlPortn": pm1008AlmDwBufferOvlPortn,
       "pm1008AlmLine": pm1008AlmLine,
       "pm1008AlmLineNurg": pm1008AlmLineNurg,
       "pm1008AlmlineXfp1WarningsTable": pm1008AlmlineXfp1WarningsTable,
       "pm1008AlmlineXfp1WarningsEntry": pm1008AlmlineXfp1WarningsEntry,
       "pm1008AlmlineXfp1WarningsIndex": pm1008AlmlineXfp1WarningsIndex,
       "pm1008AlmTxPowerLowWarningPortn": pm1008AlmTxPowerLowWarningPortn,
       "pm1008AlmTxPowerHighWarningPortn": pm1008AlmTxPowerHighWarningPortn,
       "pm1008AlmTxBiasLowWarningPortn": pm1008AlmTxBiasLowWarningPortn,
       "pm1008AlmTxBiasHighWarningPortn": pm1008AlmTxBiasHighWarningPortn,
       "pm1008AlmTempLowWarningPortn": pm1008AlmTempLowWarningPortn,
       "pm1008AlmTempHighWarningPortn": pm1008AlmTempHighWarningPortn,
       "pm1008AlmRxPowerLowWarningPortn": pm1008AlmRxPowerLowWarningPortn,
       "pm1008AlmRxPowerHighWarningPortn": pm1008AlmRxPowerHighWarningPortn,
       "pm1008AlmlineOtx1TlhWarningsTable": pm1008AlmlineOtx1TlhWarningsTable,
       "pm1008AlmlineOtx1TlhWarningsEntry": pm1008AlmlineOtx1TlhWarningsEntry,
       "pm1008AlmlineOtx1TlhWarningsIndex": pm1008AlmlineOtx1TlhWarningsIndex,
       "pm1008AlmLineModulatorAgingHighWarningPortn": pm1008AlmLineModulatorAgingHighWarningPortn,
       "pm1008AlmLineAgingHighWarningPortn": pm1008AlmLineAgingHighWarningPortn,
       "pm1008AlmLineFreqDevHighWarningPortn": pm1008AlmLineFreqDevHighWarningPortn,
       "pm1008AlmLineLaserTempHighWarningPortn": pm1008AlmLineLaserTempHighWarningPortn,
       "pm1008AlmLineUrg": pm1008AlmLineUrg,
       "pm1008AlmdfrmBerTable": pm1008AlmdfrmBerTable,
       "pm1008AlmdfrmBerEntry": pm1008AlmdfrmBerEntry,
       "pm1008AlmdfrmBerIndex": pm1008AlmdfrmBerIndex,
       "pm1008AlmLineSignalDegradePortn": pm1008AlmLineSignalDegradePortn,
       "pm1008AlmLineSignalFailPortn": pm1008AlmLineSignalFailPortn,
       "pm1008AlmLineDegradePortn": pm1008AlmLineDegradePortn,
       "pm1008AlmlineXfp1AlarmTable": pm1008AlmlineXfp1AlarmTable,
       "pm1008AlmlineXfp1AlarmEntry": pm1008AlmlineXfp1AlarmEntry,
       "pm1008AlmlineXfp1AlarmIndex": pm1008AlmlineXfp1AlarmIndex,
       "pm1008AlmTxPowerLowAlarmPortn": pm1008AlmTxPowerLowAlarmPortn,
       "pm1008AlmTxPowerHighAlarmPortn": pm1008AlmTxPowerHighAlarmPortn,
       "pm1008AlmTxBiasLowAlarmPortn": pm1008AlmTxBiasLowAlarmPortn,
       "pm1008AlmTxBiasHighAlarmPortn": pm1008AlmTxBiasHighAlarmPortn,
       "pm1008AlmTempLowAlarmPortn": pm1008AlmTempLowAlarmPortn,
       "pm1008AlmTempHighAlarmPortn": pm1008AlmTempHighAlarmPortn,
       "pm1008AlmRxPowerLowAlarmPortn": pm1008AlmRxPowerLowAlarmPortn,
       "pm1008AlmRxPowerHighAlarmPortn": pm1008AlmRxPowerHighAlarmPortn,
       "pm1008AlmlineXfp1SupplyAlarmTable": pm1008AlmlineXfp1SupplyAlarmTable,
       "pm1008AlmlineXfp1SupplyAlarmEntry": pm1008AlmlineXfp1SupplyAlarmEntry,
       "pm1008AlmlineXfp1SupplyAlarmIndex": pm1008AlmlineXfp1SupplyAlarmIndex,
       "pm1008AlmVee5LowAlarmPortn": pm1008AlmVee5LowAlarmPortn,
       "pm1008AlmVee5HighAlarmPortn": pm1008AlmVee5HighAlarmPortn,
       "pm1008AlmVcc2LowAlarmPortn": pm1008AlmVcc2LowAlarmPortn,
       "pm1008AlmVcc2HighAlarmPortn": pm1008AlmVcc2HighAlarmPortn,
       "pm1008AlmVcc3LowAlarmPortn": pm1008AlmVcc3LowAlarmPortn,
       "pm1008AlmVcc3HighAlarmPortn": pm1008AlmVcc3HighAlarmPortn,
       "pm1008AlmVcc5LowAlarmPortn": pm1008AlmVcc5LowAlarmPortn,
       "pm1008AlmVcc5HighAlarmPortn": pm1008AlmVcc5HighAlarmPortn,
       "pm1008AlmVee5LowWarningPortn": pm1008AlmVee5LowWarningPortn,
       "pm1008AlmVee5HighWarningPortn": pm1008AlmVee5HighWarningPortn,
       "pm1008AlmVcc2LowWarningPortn": pm1008AlmVcc2LowWarningPortn,
       "pm1008AlmVcc2HighWarningPortn": pm1008AlmVcc2HighWarningPortn,
       "pm1008AlmVcc3LowWarningPortn": pm1008AlmVcc3LowWarningPortn,
       "pm1008AlmVcc3HighWarningPortn": pm1008AlmVcc3HighWarningPortn,
       "pm1008AlmVcc5LowWarningPortn": pm1008AlmVcc5LowWarningPortn,
       "pm1008AlmVcc5HighWarningPortn": pm1008AlmVcc5HighWarningPortn,
       "pm1008AlmlineOtx1TlhAlarmsTable": pm1008AlmlineOtx1TlhAlarmsTable,
       "pm1008AlmlineOtx1TlhAlarmsEntry": pm1008AlmlineOtx1TlhAlarmsEntry,
       "pm1008AlmlineOtx1TlhAlarmsIndex": pm1008AlmlineOtx1TlhAlarmsIndex,
       "pm1008AlmLineModulatorAgingHighAlaPortn": pm1008AlmLineModulatorAgingHighAlaPortn,
       "pm1008AlmLineAgingHighAlaPortn": pm1008AlmLineAgingHighAlaPortn,
       "pm1008AlmLineFreqDevHighAlaPortn": pm1008AlmLineFreqDevHighAlaPortn,
       "pm1008AlmLineLaserTempHighAlaPortn": pm1008AlmLineLaserTempHighAlaPortn,
       "pm1008AlmLineCrit": pm1008AlmLineCrit,
       "pm1008AlmsynthAlmLineTable": pm1008AlmsynthAlmLineTable,
       "pm1008AlmsynthAlmLineEntry": pm1008AlmsynthAlmLineEntry,
       "pm1008AlmsynthAlmLineIndex": pm1008AlmsynthAlmLineIndex,
       "pm1008AlmXfpAbsentPortn": pm1008AlmXfpAbsentPortn,
       "pm1008AlmXfpInitNotComplPortn": pm1008AlmXfpInitNotComplPortn,
       "pm1008AlmLineHwFailPortn": pm1008AlmLineHwFailPortn,
       "pm1008AlmXfpTxOffPortn": pm1008AlmXfpTxOffPortn,
       "pm1008AlmLineLocalOosPortn": pm1008AlmLineLocalOosPortn,
       "pm1008AlmUpRdiInsPortn": pm1008AlmUpRdiInsPortn,
       "pm1008AlmLineDdmWarningPortn": pm1008AlmLineDdmWarningPortn,
       "pm1008AlmLineDdmAlmPortn": pm1008AlmLineDdmAlmPortn,
       "pm1008AlmLineFailPortn": pm1008AlmLineFailPortn,
       "pm1008AlmLineActivePortn": pm1008AlmLineActivePortn,
       "pm1008AlmdfrmAlmTable": pm1008AlmdfrmAlmTable,
       "pm1008AlmdfrmAlmEntry": pm1008AlmdfrmAlmEntry,
       "pm1008AlmdfrmAlmIndex": pm1008AlmdfrmAlmIndex,
       "pm1008AlmDwAisDetPortn": pm1008AlmDwAisDetPortn,
       "pm1008AlmDwRdiDetPortn": pm1008AlmDwRdiDetPortn,
       "pm1008AlmDwOofPortn": pm1008AlmDwOofPortn,
       "pm1008AlmDwLofPortn": pm1008AlmDwLofPortn,
       "pm1008AlmDccLoopbackPortn": pm1008AlmDccLoopbackPortn,
       "pm1008AlmRxDccBroadStormPortn": pm1008AlmRxDccBroadStormPortn,
       "pm1008AlmTxDccBroadStormPortn": pm1008AlmTxDccBroadStormPortn,
       "pm1008AlmlineSyncAlarmsTable": pm1008AlmlineSyncAlarmsTable,
       "pm1008AlmlineSyncAlarmsEntry": pm1008AlmlineSyncAlarmsEntry,
       "pm1008AlmlineSyncAlarmsIndex": pm1008AlmlineSyncAlarmsIndex,
       "pm1008AlmDwLockerrPortn": pm1008AlmDwLockerrPortn,
       "pm1008AlmUpLockerrPortn": pm1008AlmUpLockerrPortn,
       "pm1008AlmDwLosPortn": pm1008AlmDwLosPortn,
       "pm1008AlmlineXfp1AlarmsTable": pm1008AlmlineXfp1AlarmsTable,
       "pm1008AlmlineXfp1AlarmsEntry": pm1008AlmlineXfp1AlarmsEntry,
       "pm1008AlmlineXfp1AlarmsIndex": pm1008AlmlineXfp1AlarmsIndex,
       "pm1008AlmModNrPortn": pm1008AlmModNrPortn,
       "pm1008AlmRxCdrNotLockedPortn": pm1008AlmRxCdrNotLockedPortn,
       "pm1008AlmRxNrPortn": pm1008AlmRxNrPortn,
       "pm1008AlmTxCdrNotLockedPortn": pm1008AlmTxCdrNotLockedPortn,
       "pm1008AlmTxFaultPortn": pm1008AlmTxFaultPortn,
       "pm1008AlmTxNrPortn": pm1008AlmTxNrPortn,
       "pm1008AlmWavelengthUnlockedPortn": pm1008AlmWavelengthUnlockedPortn,
       "pm1008AlmTecFaultPortn": pm1008AlmTecFaultPortn,
       "pm1008AlmApdSupplyFaultPortn": pm1008AlmApdSupplyFaultPortn,
       "pm1008measures": pm1008measures,
       "pm1008MesrOther": pm1008MesrOther,
       "pm1008Mesrsynth0": pm1008Mesrsynth0,
       "pm1008Mesrsynth1": pm1008Mesrsynth1,
       "pm1008MesrClient": pm1008MesrClient,
       "pm1008MesrtempMeasTable": pm1008MesrtempMeasTable,
       "pm1008MesrtempMeasEntry": pm1008MesrtempMeasEntry,
       "pm1008MesrtempMeasIndex": pm1008MesrtempMeasIndex,
       "pm1008MesrtempMeasPortn": pm1008MesrtempMeasPortn,
       "pm1008MesrvoltMeasTable": pm1008MesrvoltMeasTable,
       "pm1008MesrvoltMeasEntry": pm1008MesrvoltMeasEntry,
       "pm1008MesrvoltMeasIndex": pm1008MesrvoltMeasIndex,
       "pm1008MesrvoltMeasPortn": pm1008MesrvoltMeasPortn,
       "pm1008MesrbiasMeasTable": pm1008MesrbiasMeasTable,
       "pm1008MesrbiasMeasEntry": pm1008MesrbiasMeasEntry,
       "pm1008MesrbiasMeasIndex": pm1008MesrbiasMeasIndex,
       "pm1008MesrbiasMeasPortn": pm1008MesrbiasMeasPortn,
       "pm1008MesrtxpwrMeasTable": pm1008MesrtxpwrMeasTable,
       "pm1008MesrtxpwrMeasEntry": pm1008MesrtxpwrMeasEntry,
       "pm1008MesrtxpwrMeasIndex": pm1008MesrtxpwrMeasIndex,
       "pm1008MesrtxpwrMeasPortn": pm1008MesrtxpwrMeasPortn,
       "pm1008MesrrxpwrMeasTable": pm1008MesrrxpwrMeasTable,
       "pm1008MesrrxpwrMeasEntry": pm1008MesrrxpwrMeasEntry,
       "pm1008MesrrxpwrMeasIndex": pm1008MesrrxpwrMeasIndex,
       "pm1008MesrrxpwrMeasPortn": pm1008MesrrxpwrMeasPortn,
       "pm1008MesrLine": pm1008MesrLine,
       "pm1008Mesrxfp1LxModTempMeasTable": pm1008Mesrxfp1LxModTempMeasTable,
       "pm1008Mesrxfp1LxModTempMeasEntry": pm1008Mesrxfp1LxModTempMeasEntry,
       "pm1008Mesrxfp1LxModTempMeasIndex": pm1008Mesrxfp1LxModTempMeasIndex,
       "pm1008Mesrxfp1LxModTempMeasPortn": pm1008Mesrxfp1LxModTempMeasPortn,
       "pm1008Mesrxfp1ReservedTable": pm1008Mesrxfp1ReservedTable,
       "pm1008Mesrxfp1ReservedEntry": pm1008Mesrxfp1ReservedEntry,
       "pm1008Mesrxfp1ReservedIndex": pm1008Mesrxfp1ReservedIndex,
       "pm1008Mesrxfp1ReservedPortn": pm1008Mesrxfp1ReservedPortn,
       "pm1008Mesrxfp1LoBiasCurrentMeasTable": pm1008Mesrxfp1LoBiasCurrentMeasTable,
       "pm1008Mesrxfp1LoBiasCurrentMeasEntry": pm1008Mesrxfp1LoBiasCurrentMeasEntry,
       "pm1008Mesrxfp1LoBiasCurrentMeasIndex": pm1008Mesrxfp1LoBiasCurrentMeasIndex,
       "pm1008Mesrxfp1LoBiasCurrentMeasPortn": pm1008Mesrxfp1LoBiasCurrentMeasPortn,
       "pm1008Mesrxfp1LoTxPowerMeasTable": pm1008Mesrxfp1LoTxPowerMeasTable,
       "pm1008Mesrxfp1LoTxPowerMeasEntry": pm1008Mesrxfp1LoTxPowerMeasEntry,
       "pm1008Mesrxfp1LoTxPowerMeasIndex": pm1008Mesrxfp1LoTxPowerMeasIndex,
       "pm1008Mesrxfp1LoTxPowerMeasPortn": pm1008Mesrxfp1LoTxPowerMeasPortn,
       "pm1008Mesrxfp1LiRxPowerMeasTable": pm1008Mesrxfp1LiRxPowerMeasTable,
       "pm1008Mesrxfp1LiRxPowerMeasEntry": pm1008Mesrxfp1LiRxPowerMeasEntry,
       "pm1008Mesrxfp1LiRxPowerMeasIndex": pm1008Mesrxfp1LiRxPowerMeasIndex,
       "pm1008Mesrxfp1LiRxPowerMeasPortn": pm1008Mesrxfp1LiRxPowerMeasPortn,
       "pm1008Mesrxfp1LxAux1MeasTable": pm1008Mesrxfp1LxAux1MeasTable,
       "pm1008Mesrxfp1LxAux1MeasEntry": pm1008Mesrxfp1LxAux1MeasEntry,
       "pm1008Mesrxfp1LxAux1MeasIndex": pm1008Mesrxfp1LxAux1MeasIndex,
       "pm1008Mesrxfp1LxAux1MeasPortn": pm1008Mesrxfp1LxAux1MeasPortn,
       "pm1008Mesrxfp1LxAux2MeasTable": pm1008Mesrxfp1LxAux2MeasTable,
       "pm1008Mesrxfp1LxAux2MeasEntry": pm1008Mesrxfp1LxAux2MeasEntry,
       "pm1008Mesrxfp1LxAux2MeasIndex": pm1008Mesrxfp1LxAux2MeasIndex,
       "pm1008Mesrxfp1LxAux2MeasPortn": pm1008Mesrxfp1LxAux2MeasPortn,
       "pm1008Mesrotx1AgingTable": pm1008Mesrotx1AgingTable,
       "pm1008Mesrotx1AgingEntry": pm1008Mesrotx1AgingEntry,
       "pm1008Mesrotx1AgingIndex": pm1008Mesrotx1AgingIndex,
       "pm1008Mesrotx1AgingPortn": pm1008Mesrotx1AgingPortn,
       "pm1008Mesrotx1LaserTemperatureTable": pm1008Mesrotx1LaserTemperatureTable,
       "pm1008Mesrotx1LaserTemperatureEntry": pm1008Mesrotx1LaserTemperatureEntry,
       "pm1008Mesrotx1LaserTemperatureIndex": pm1008Mesrotx1LaserTemperatureIndex,
       "pm1008Mesrotx1LaserTemperaturePortn": pm1008Mesrotx1LaserTemperaturePortn,
       "pm1008Mesrotx1FreqDeviationTable": pm1008Mesrotx1FreqDeviationTable,
       "pm1008Mesrotx1FreqDeviationEntry": pm1008Mesrotx1FreqDeviationEntry,
       "pm1008Mesrotx1FreqDeviationIndex": pm1008Mesrotx1FreqDeviationIndex,
       "pm1008Mesrotx1FreqDeviationPortn": pm1008Mesrotx1FreqDeviationPortn,
       "pm1008Mesrotx1LaserWvlengthTable": pm1008Mesrotx1LaserWvlengthTable,
       "pm1008Mesrotx1LaserWvlengthEntry": pm1008Mesrotx1LaserWvlengthEntry,
       "pm1008Mesrotx1LaserWvlengthIndex": pm1008Mesrotx1LaserWvlengthIndex,
       "pm1008Mesrotx1LaserWvlengthPortn": pm1008Mesrotx1LaserWvlengthPortn,
       "pm1008counters": pm1008counters,
       "pm1008CntOther": pm1008CntOther,
       "pm1008CntClient": pm1008CntClient,
       "pm1008CntupRaRemCntTable": pm1008CntupRaRemCntTable,
       "pm1008CntupRaRemCntEntry": pm1008CntupRaRemCntEntry,
       "pm1008CntupRaRemCntIndex": pm1008CntupRaRemCntIndex,
       "pm1008CntupRaRemCntValuePortn": pm1008CntupRaRemCntValuePortn,
       "pm1008CntupRaRemCntErrorPortn": pm1008CntupRaRemCntErrorPortn,
       "pm1008CntupRaRemCntOverloadPortn": pm1008CntupRaRemCntOverloadPortn,
       "pm1008CntupRaInsCntTable": pm1008CntupRaInsCntTable,
       "pm1008CntupRaInsCntEntry": pm1008CntupRaInsCntEntry,
       "pm1008CntupRaInsCntIndex": pm1008CntupRaInsCntIndex,
       "pm1008CntupRaInsCntValuePortn": pm1008CntupRaInsCntValuePortn,
       "pm1008CntupRaInsCntErrorPortn": pm1008CntupRaInsCntErrorPortn,
       "pm1008CntupRaInsCntOverloadPortn": pm1008CntupRaInsCntOverloadPortn,
       "pm1008CntupRdErrCntTable": pm1008CntupRdErrCntTable,
       "pm1008CntupRdErrCntEntry": pm1008CntupRdErrCntEntry,
       "pm1008CntupRdErrCntIndex": pm1008CntupRdErrCntIndex,
       "pm1008CntupRdErrCntValuePortn": pm1008CntupRdErrCntValuePortn,
       "pm1008CntupRdErrCntErrorPortn": pm1008CntupRdErrCntErrorPortn,
       "pm1008CntupRdErrCntOverloadPortn": pm1008CntupRdErrCntOverloadPortn,
       "pm1008CntupTimCntTable": pm1008CntupTimCntTable,
       "pm1008CntupTimCntEntry": pm1008CntupTimCntEntry,
       "pm1008CntupTimCntIndex": pm1008CntupTimCntIndex,
       "pm1008CntupTimCntValuePortn": pm1008CntupTimCntValuePortn,
       "pm1008CntupTimCntErrorPortn": pm1008CntupTimCntErrorPortn,
       "pm1008CntupTimCntOverloadPortn": pm1008CntupTimCntOverloadPortn,
       "pm1008CntupCvErrCntTable": pm1008CntupCvErrCntTable,
       "pm1008CntupCvErrCntEntry": pm1008CntupCvErrCntEntry,
       "pm1008CntupCvErrCntIndex": pm1008CntupCvErrCntIndex,
       "pm1008CntupCvErrCntValuePortn": pm1008CntupCvErrCntValuePortn,
       "pm1008CntupCvErrCntErrorPortn": pm1008CntupCvErrCntErrorPortn,
       "pm1008CntupCvErrCntOverloadPortn": pm1008CntupCvErrCntOverloadPortn,
       "pm1008CntdwCbipCntTable": pm1008CntdwCbipCntTable,
       "pm1008CntdwCbipCntEntry": pm1008CntdwCbipCntEntry,
       "pm1008CntdwCbipCntIndex": pm1008CntdwCbipCntIndex,
       "pm1008CntdwCbipCntValuePortn": pm1008CntdwCbipCntValuePortn,
       "pm1008CntdwCbipCntErrorPortn": pm1008CntdwCbipCntErrorPortn,
       "pm1008CntdwCbipCntOverloadPortn": pm1008CntdwCbipCntOverloadPortn,
       "pm1008CntdwTimCntTable": pm1008CntdwTimCntTable,
       "pm1008CntdwTimCntEntry": pm1008CntdwTimCntEntry,
       "pm1008CntdwTimCntIndex": pm1008CntdwTimCntIndex,
       "pm1008CntdwTimCntValuePortn": pm1008CntdwTimCntValuePortn,
       "pm1008CntdwTimCntErrorPortn": pm1008CntdwTimCntErrorPortn,
       "pm1008CntdwTimCntOverloadPortn": pm1008CntdwTimCntOverloadPortn,
       "pm1008CntLine": pm1008CntLine,
       "pm1008CntdfrmB1ErrCntTable": pm1008CntdfrmB1ErrCntTable,
       "pm1008CntdfrmB1ErrCntEntry": pm1008CntdfrmB1ErrCntEntry,
       "pm1008CntdfrmB1ErrCntIndex": pm1008CntdfrmB1ErrCntIndex,
       "pm1008CntdfrmB1ErrCntValuePortn": pm1008CntdfrmB1ErrCntValuePortn,
       "pm1008CntdfrmB1ErrCntErrorPortn": pm1008CntdfrmB1ErrCntErrorPortn,
       "pm1008CntdfrmB1ErrCntOverloadPortn": pm1008CntdfrmB1ErrCntOverloadPortn,
       "pm1008CntdfrmTimCntTable": pm1008CntdfrmTimCntTable,
       "pm1008CntdfrmTimCntEntry": pm1008CntdfrmTimCntEntry,
       "pm1008CntdfrmTimCntIndex": pm1008CntdfrmTimCntIndex,
       "pm1008CntdfrmTimCntValuePortn": pm1008CntdfrmTimCntValuePortn,
       "pm1008CntdfrmTimCntErrorPortn": pm1008CntdfrmTimCntErrorPortn,
       "pm1008CntdfrmTimCntOverloadPortn": pm1008CntdfrmTimCntOverloadPortn,
       "pm1008CntdfrmPrimLineErrCntTable": pm1008CntdfrmPrimLineErrCntTable,
       "pm1008CntdfrmPrimLineErrCntEntry": pm1008CntdfrmPrimLineErrCntEntry,
       "pm1008CntdfrmPrimLineErrCntIndex": pm1008CntdfrmPrimLineErrCntIndex,
       "pm1008CntdfrmPrimLineErrCntValuePortn": pm1008CntdfrmPrimLineErrCntValuePortn,
       "pm1008CntdfrmPrimLineErrCntErrorPortn": pm1008CntdfrmPrimLineErrCntErrorPortn,
       "pm1008CntdfrmPrimLineErrCntOverloadPortn": pm1008CntdfrmPrimLineErrCntOverloadPortn,
       "pm1008CntCountersReset": pm1008CntCountersReset,
       "pm1008CntCountersStop": pm1008CntCountersStop,
       "pm1008controlsWrite": pm1008controlsWrite,
       "pm1008CtrlOther": pm1008CtrlOther,
       "pm1008CtrlconfMgnt1": pm1008CtrlconfMgnt1,
       "pm1008CtrlConf1Load1": pm1008CtrlConf1Load1,
       "pm1008CtrlConf2Load1": pm1008CtrlConf2Load1,
       "pm1008CtrlConf2Flash1": pm1008CtrlConf2Flash1,
       "pm1008CtrlConf2Clear1": pm1008CtrlConf2Clear1,
       "pm1008Ctrlsynth4": pm1008Ctrlsynth4,
       "pm1008CtrlCorrelatOn": pm1008CtrlCorrelatOn,
       "pm1008CtrlCorrelatOff": pm1008CtrlCorrelatOff,
       "pm1008CtrlswMgnt": pm1008CtrlswMgnt,
       "pm1008CtrlColdReset": pm1008CtrlColdReset,
       "pm1008CtrlWarmReset": pm1008CtrlWarmReset,
       "pm1008CtrlLoadSwBank1": pm1008CtrlLoadSwBank1,
       "pm1008CtrlLoadSwBank2": pm1008CtrlLoadSwBank2,
       "pm1008CtrlgwMgnt": pm1008CtrlgwMgnt,
       "pm1008CtrlCurrentGwReset": pm1008CtrlCurrentGwReset,
       "pm1008CtrlLoadGwBank1": pm1008CtrlLoadGwBank1,
       "pm1008CtrlLoadGwBank2": pm1008CtrlLoadGwBank2,
       "pm1008CtrlLoadGwBank3": pm1008CtrlLoadGwBank3,
       "pm1008CtrlLoadGwBank4": pm1008CtrlLoadGwBank4,
       "pm1008CtrlledTest": pm1008CtrlledTest,
       "pm1008CtrlGreenLed": pm1008CtrlGreenLed,
       "pm1008CtrlRedLed": pm1008CtrlRedLed,
       "pm1008CtrlLedOff": pm1008CtrlLedOff,
       "pm1008CtrlmoduleOosMode": pm1008CtrlmoduleOosMode,
       "pm1008CtrlModuleOosMode": pm1008CtrlModuleOosMode,
       "pm1008CtrlmaintenanceMode": pm1008CtrlmaintenanceMode,
       "pm1008CtrlMaintenanceMode": pm1008CtrlMaintenanceMode,
       "pm1008CtrldccEnable": pm1008CtrldccEnable,
       "pm1008CtrlDccEnable": pm1008CtrlDccEnable,
       "pm1008CtrlClient": pm1008CtrlClient,
       "pm1008CtrlaccessLoopTable": pm1008CtrlaccessLoopTable,
       "pm1008CtrlaccessLoopEntry": pm1008CtrlaccessLoopEntry,
       "pm1008CtrlaccessLoopIndex": pm1008CtrlaccessLoopIndex,
       "pm1008CtrlaccessLoopPortn": pm1008CtrlaccessLoopPortn,
       "pm1008CtrlportOosModeTable": pm1008CtrlportOosModeTable,
       "pm1008CtrlportOosModeEntry": pm1008CtrlportOosModeEntry,
       "pm1008CtrlportOosModeIndex": pm1008CtrlportOosModeIndex,
       "pm1008CtrlportOosModePortn": pm1008CtrlportOosModePortn,
       "pm1008CtrlsfpOnCtrlTable": pm1008CtrlsfpOnCtrlTable,
       "pm1008CtrlsfpOnCtrlEntry": pm1008CtrlsfpOnCtrlEntry,
       "pm1008CtrlsfpOnCtrlIndex": pm1008CtrlsfpOnCtrlIndex,
       "pm1008CtrlsfpOnCtrlPortn": pm1008CtrlsfpOnCtrlPortn,
       "pm1008CtrlsfpOffCtrlTable": pm1008CtrlsfpOffCtrlTable,
       "pm1008CtrlsfpOffCtrlEntry": pm1008CtrlsfpOffCtrlEntry,
       "pm1008CtrlsfpOffCtrlIndex": pm1008CtrlsfpOffCtrlIndex,
       "pm1008CtrlsfpOffCtrlPortn": pm1008CtrlsfpOffCtrlPortn,
       "pm1008CtrlcsfUpInsTable": pm1008CtrlcsfUpInsTable,
       "pm1008CtrlcsfUpInsEntry": pm1008CtrlcsfUpInsEntry,
       "pm1008CtrlcsfUpInsIndex": pm1008CtrlcsfUpInsIndex,
       "pm1008CtrlcsfUpInsPortn": pm1008CtrlcsfUpInsPortn,
       "pm1008CtrlcaisDwInsTable": pm1008CtrlcaisDwInsTable,
       "pm1008CtrlcaisDwInsEntry": pm1008CtrlcaisDwInsEntry,
       "pm1008CtrlcaisDwInsIndex": pm1008CtrlcaisDwInsIndex,
       "pm1008CtrlcaisDwInsPortn": pm1008CtrlcaisDwInsPortn,
       "pm1008CtrlflowControlTable": pm1008CtrlflowControlTable,
       "pm1008CtrlflowControlEntry": pm1008CtrlflowControlEntry,
       "pm1008CtrlflowControlIndex": pm1008CtrlflowControlIndex,
       "pm1008CtrlflowControlPortn": pm1008CtrlflowControlPortn,
       "pm1008CtrlclientAccessTermLoopTable": pm1008CtrlclientAccessTermLoopTable,
       "pm1008CtrlclientAccessTermLoopEntry": pm1008CtrlclientAccessTermLoopEntry,
       "pm1008CtrlclientAccessTermLoopIndex": pm1008CtrlclientAccessTermLoopIndex,
       "pm1008CtrlclientAccessTermLoopPortn": pm1008CtrlclientAccessTermLoopPortn,
       "pm1008CtrlselectMultirateTable": pm1008CtrlselectMultirateTable,
       "pm1008CtrlselectMultirateEntry": pm1008CtrlselectMultirateEntry,
       "pm1008CtrlselectMultirateIndex": pm1008CtrlselectMultirateIndex,
       "pm1008CtrlselectMultiratePortn": pm1008CtrlselectMultiratePortn,
       "pm1008CtrlprotocolTable": pm1008CtrlprotocolTable,
       "pm1008CtrlprotocolEntry": pm1008CtrlprotocolEntry,
       "pm1008CtrlprotocolIndex": pm1008CtrlprotocolIndex,
       "pm1008CtrlprotocolPortn": pm1008CtrlprotocolPortn,
       "pm1008CtrlLine": pm1008CtrlLine,
       "pm1008CtrlcommAccessLoop": pm1008CtrlcommAccessLoop,
       "pm1008CtrlCommAccessloop": pm1008CtrlCommAccessloop,
       "pm1008CtrllineLoop": pm1008CtrllineLoop,
       "pm1008CtrlLineLoop": pm1008CtrlLineLoop,
       "pm1008CtrlmsAis": pm1008CtrlmsAis,
       "pm1008CtrlMsAis": pm1008CtrlMsAis,
       "pm1008CtrlfecDisableTable": pm1008CtrlfecDisableTable,
       "pm1008CtrlfecDisableEntry": pm1008CtrlfecDisableEntry,
       "pm1008CtrlfecDisableIndex": pm1008CtrlfecDisableIndex,
       "pm1008CtrlfecDisablePortn": pm1008CtrlfecDisablePortn,
       "pm1008CtrlProtMgnt": pm1008CtrlProtMgnt,
       "pm1008CtrlLineNumber": pm1008CtrlLineNumber,
       "pm1008CtrlProtMode": pm1008CtrlProtMode,
       "pm1008CtrllineOosModeTable": pm1008CtrllineOosModeTable,
       "pm1008CtrllineOosModeEntry": pm1008CtrllineOosModeEntry,
       "pm1008CtrllineOosModeIndex": pm1008CtrllineOosModeIndex,
       "pm1008CtrllineOosModePortn": pm1008CtrllineOosModePortn,
       "pm1008CtrlxfpOnoffTable": pm1008CtrlxfpOnoffTable,
       "pm1008CtrlxfpOnoffEntry": pm1008CtrlxfpOnoffEntry,
       "pm1008CtrlxfpOnoffIndex": pm1008CtrlxfpOnoffIndex,
       "pm1008CtrlxfpOnoffPortn": pm1008CtrlxfpOnoffPortn,
       "pm1008CtrlxfpLineLoopTable": pm1008CtrlxfpLineLoopTable,
       "pm1008CtrlxfpLineLoopEntry": pm1008CtrlxfpLineLoopEntry,
       "pm1008CtrlxfpLineLoopIndex": pm1008CtrlxfpLineLoopIndex,
       "pm1008CtrlxfpLineLoopPortn": pm1008CtrlxfpLineLoopPortn,
       "pm1008CtrlxfpXfiLoopTable": pm1008CtrlxfpXfiLoopTable,
       "pm1008CtrlxfpXfiLoopEntry": pm1008CtrlxfpXfiLoopEntry,
       "pm1008CtrlxfpXfiLoopIndex": pm1008CtrlxfpXfiLoopIndex,
       "pm1008CtrlxfpXfiLoopPortn": pm1008CtrlxfpXfiLoopPortn,
       "pm1008CtrllineTunableChannelTable": pm1008CtrllineTunableChannelTable,
       "pm1008CtrllineTunableChannelEntry": pm1008CtrllineTunableChannelEntry,
       "pm1008CtrllineTunableChannelIndex": pm1008CtrllineTunableChannelIndex,
       "pm1008CtrllineTunableChannelPortn": pm1008CtrllineTunableChannelPortn,
       "pm1008CtrllinePhotodiodeModeTable": pm1008CtrllinePhotodiodeModeTable,
       "pm1008CtrllinePhotodiodeModeEntry": pm1008CtrllinePhotodiodeModeEntry,
       "pm1008CtrllinePhotodiodeModeIndex": pm1008CtrllinePhotodiodeModeIndex,
       "pm1008CtrllinePhotodiodeModePortn": pm1008CtrllinePhotodiodeModePortn,
       "pm1008CtrllinePhotodiodeValueTable": pm1008CtrllinePhotodiodeValueTable,
       "pm1008CtrllinePhotodiodeValueEntry": pm1008CtrllinePhotodiodeValueEntry,
       "pm1008CtrllinePhotodiodeValueIndex": pm1008CtrllinePhotodiodeValueIndex,
       "pm1008CtrllinePhotodiodeValuePortn": pm1008CtrllinePhotodiodeValuePortn,
       "pm1008CtrllinePowerLaserTable": pm1008CtrllinePowerLaserTable,
       "pm1008CtrllinePowerLaserEntry": pm1008CtrllinePowerLaserEntry,
       "pm1008CtrllinePowerLaserIndex": pm1008CtrllinePowerLaserIndex,
       "pm1008CtrllinePowerLaserPortn": pm1008CtrllinePowerLaserPortn,
       "pm1008ri": pm1008ri,
       "pm1008riTable": pm1008riTable,
       "pm1008RinvSfpTable": pm1008RinvSfpTable,
       "pm1008RinvSfpEntry": pm1008RinvSfpEntry,
       "pm1008RinvSfpIndex": pm1008RinvSfpIndex,
       "pm1008Rinvsfp": pm1008Rinvsfp,
       "pm1008RinvLineTable": pm1008RinvLineTable,
       "pm1008RinvLineEntry": pm1008RinvLineEntry,
       "pm1008RinvLineIndex": pm1008RinvLineIndex,
       "pm1008RinvxfpLine": pm1008RinvxfpLine,
       "pm1008RinvReloadInventory": pm1008RinvReloadInventory,
       "pm1008RinvHwPlatform": pm1008RinvHwPlatform,
       "pm1008RinvModulePlatform": pm1008RinvModulePlatform,
       "pm1008RinvSwPlatform": pm1008RinvSwPlatform,
       "pm1008RinvGwPlatform": pm1008RinvGwPlatform,
       "pm1008download": pm1008download,
       "pm1008DwlOther": pm1008DwlOther,
       "pm1008DwlrestartProcess": pm1008DwlrestartProcess,
       "pm1008DwlWarmRestartProcessed": pm1008DwlWarmRestartProcessed,
       "pm1008DwlColdRestartProcessed": pm1008DwlColdRestartProcessed,
       "pm1008DwlswBanksUsed": pm1008DwlswBanksUsed,
       "pm1008DwlSwBank1Used": pm1008DwlSwBank1Used,
       "pm1008DwlSwBank2Used": pm1008DwlSwBank2Used,
       "pm1008DwlSwBank1Notempty": pm1008DwlSwBank1Notempty,
       "pm1008DwlSwBank2Notempty": pm1008DwlSwBank2Notempty,
       "pm1008DwlgwBanksUsed": pm1008DwlgwBanksUsed,
       "pm1008DwlGwBank1Used": pm1008DwlGwBank1Used,
       "pm1008DwlGwBank2Used": pm1008DwlGwBank2Used,
       "pm1008DwlGwBank3Used": pm1008DwlGwBank3Used,
       "pm1008DwlGwBank4Used": pm1008DwlGwBank4Used,
       "pm1008DwlGwBank1Notempty": pm1008DwlGwBank1Notempty,
       "pm1008DwlGwBank2Notempty": pm1008DwlGwBank2Notempty,
       "pm1008DwlGwBank3Notempty": pm1008DwlGwBank3Notempty,
       "pm1008DwlGwBank4Notempty": pm1008DwlGwBank4Notempty,
       "pm1008DwlClient": pm1008DwlClient,
       "pm1008DwlLine": pm1008DwlLine,
       "pm1008Config": pm1008Config,
       "pm1008CfgAccessCAisCsf": pm1008CfgAccessCAisCsf,
       "pm1008CfgClientcaiscsfTable": pm1008CfgClientcaiscsfTable,
       "pm1008CfgClientcaiscsfEntry": pm1008CfgClientcaiscsfEntry,
       "pm1008CfgClientcaiscsfIndex": pm1008CfgClientcaiscsfIndex,
       "pm1008CfgCAisModePortn": pm1008CfgCAisModePortn,
       "pm1008CfgUpAccessioAlmPortn": pm1008CfgUpAccessioAlmPortn,
       "pm1008CfgUpMapperDeAlmPortn": pm1008CfgUpMapperDeAlmPortn,
       "pm1008CfgDownAccessioAlmPortn": pm1008CfgDownAccessioAlmPortn,
       "pm1008CfgDownMapperDeAlmPortn": pm1008CfgDownMapperDeAlmPortn,
       "pm1008CfgDownDfrmAlmPortn": pm1008CfgDownDfrmAlmPortn,
       "pm1008CfgDownLineSyncAlarmsPortn": pm1008CfgDownLineSyncAlarmsPortn,
       "pm1008CfgStartup": pm1008CfgStartup,
       "pm1008CfgClientStartupTable": pm1008CfgClientStartupTable,
       "pm1008CfgClientStartupEntry": pm1008CfgClientStartupEntry,
       "pm1008CfgClientStartupIndex": pm1008CfgClientStartupIndex,
       "pm1008CfgSystConfPortPortn": pm1008CfgSystConfPortPortn,
       "pm1008CfgNetConfPortPortn": pm1008CfgNetConfPortPortn,
       "pm1008CfgOptionsPortPortn": pm1008CfgOptionsPortPortn,
       "pm1008tablelineStartup": pm1008tablelineStartup,
       "pm1008CfgsystConfLine1": pm1008CfgsystConfLine1,
       "pm1008CfglineOptions1": pm1008CfglineOptions1,
       "pm1008CfgsystConfLine2": pm1008CfgsystConfLine2,
       "pm1008CfglineSelection": pm1008CfglineSelection,
       "pm1008CfgXfpTable": pm1008CfgXfpTable,
       "pm1008CfgXfpEntry": pm1008CfgXfpEntry,
       "pm1008CfgXfpIndex": pm1008CfgXfpIndex,
       "pm1008CfgSystConfXfpPortn": pm1008CfgSystConfXfpPortn,
       "pm1008CfgDataRateConfXfpPortn": pm1008CfgDataRateConfXfpPortn,
       "pm1008CfgLabels": pm1008CfgLabels,
       "pm1008CfgLabelclientTable": pm1008CfgLabelclientTable,
       "pm1008CfgLabelclientEntry": pm1008CfgLabelclientEntry,
       "pm1008CfgLabelclientIndex": pm1008CfgLabelclientIndex,
       "pm1008CfgLabelclientPortn": pm1008CfgLabelclientPortn,
       "pm1008CfgLabellineTable": pm1008CfgLabellineTable,
       "pm1008CfgLabellineEntry": pm1008CfgLabellineEntry,
       "pm1008CfgLabellineIndex": pm1008CfgLabellineIndex,
       "pm1008CfgLabellinePortn": pm1008CfgLabellinePortn,
       "pm1008CfgStartuptlh": pm1008CfgStartuptlh,
       "pm1008CfgOtxtlhTable": pm1008CfgOtxtlhTable,
       "pm1008CfgOtxtlhEntry": pm1008CfgOtxtlhEntry,
       "pm1008CfgOtxtlhIndex": pm1008CfgOtxtlhIndex,
       "pm1008CfgNuPortn": pm1008CfgNuPortn,
       "pm1008CfgLineDitherRatePortn": pm1008CfgLineDitherRatePortn,
       "pm1008CfgLineDitherFhzPortn": pm1008CfgLineDitherFhzPortn,
       "pm1008CfgLinePwrLaserPortn": pm1008CfgLinePwrLaserPortn,
       "pm1008CfgLineFCurrentPortn": pm1008CfgLineFCurrentPortn,
       "pm1008CfgLineGridCurrentPortn": pm1008CfgLineGridCurrentPortn,
       "pm1008CfgFPortn": pm1008CfgFPortn,
       "pm1008CfgReservedPortn": pm1008CfgReservedPortn,
       "pm1008CfgLinePhotodiodeModePortn": pm1008CfgLinePhotodiodeModePortn,
       "pm1008CfgLinePhotodiodeValuePortn": pm1008CfgLinePhotodiodeValuePortn,
       "pm1008CfgStartuptablefive": pm1008CfgStartuptablefive,
       "pm1008CfgOtxtlhcapabilitiesTable": pm1008CfgOtxtlhcapabilitiesTable,
       "pm1008CfgOtxtlhcapabilitiesEntry": pm1008CfgOtxtlhcapabilitiesEntry,
       "pm1008CfgOtxtlhcapabilitiesIndex": pm1008CfgOtxtlhcapabilitiesIndex,
       "pm1008CfgComponentTypePortn": pm1008CfgComponentTypePortn,
       "pm1008CfgMiscellaneousPortn": pm1008CfgMiscellaneousPortn,
       "pm1008CfgFirstChannelPortn": pm1008CfgFirstChannelPortn,
       "pm1008CfgLastChannelPortn": pm1008CfgLastChannelPortn,
       "pm1008CfgGridPortn": pm1008CfgGridPortn,
       "pm1008CfgWriteConfiguration": pm1008CfgWriteConfiguration,
       "pm1008traps": pm1008traps,
       "pm1008trapPortNumber": pm1008trapPortNumber,
       "pm1008trapLineNumber": pm1008trapLineNumber,
       "pm1008trapBoardNumber": pm1008trapBoardNumber,
       "pm1008LineTrapNotUrgentGoesOn": pm1008LineTrapNotUrgentGoesOn,
       "pm1008LineTrapNotUrgentGoesOff": pm1008LineTrapNotUrgentGoesOff,
       "pm1008LineTrapUrgentGoesOn": pm1008LineTrapUrgentGoesOn,
       "pm1008LineTrapUrgentGoesOff": pm1008LineTrapUrgentGoesOff,
       "pm1008LineTrapCritGoesOn": pm1008LineTrapCritGoesOn,
       "pm1008LineTrapCritGoesOff": pm1008LineTrapCritGoesOff,
       "pm1008ClientTrapNotUrgentGoesOn": pm1008ClientTrapNotUrgentGoesOn,
       "pm1008ClientTrapNotUrgentGoesOff": pm1008ClientTrapNotUrgentGoesOff,
       "pm1008ClientTrapUrgentGoesOn": pm1008ClientTrapUrgentGoesOn,
       "pm1008ClientTrapUrgentGoesOff": pm1008ClientTrapUrgentGoesOff,
       "pm1008ClientTrapCritGoesOn": pm1008ClientTrapCritGoesOn,
       "pm1008ClientTrapCritGoesOff": pm1008ClientTrapCritGoesOff,
       "pm1008PowerTrapUrgentGoesOn": pm1008PowerTrapUrgentGoesOn,
       "pm1008PowerTrapUrgentGoesOff": pm1008PowerTrapUrgentGoesOff,
       "pm1008Monitoring": pm1008Monitoring,
       "pm1008MonOther": pm1008MonOther,
       "pm1008MonRmon": pm1008MonRmon,
       "pm1008MonCountersReset": pm1008MonCountersReset,
       "pm1008MonCountersStop": pm1008MonCountersStop,
       "pm1008MonClient": pm1008MonClient,
       "pm1008MonClientRmonCounter": pm1008MonClientRmonCounter,
       "pm1008MonupRmonByteCntTable": pm1008MonupRmonByteCntTable,
       "pm1008MonupRmonByteCntEntry": pm1008MonupRmonByteCntEntry,
       "pm1008MonupRmonByteCntIndex": pm1008MonupRmonByteCntIndex,
       "pm1008MonupRmonByteCntValuePortn": pm1008MonupRmonByteCntValuePortn,
       "pm1008MonupRmonByteCntErrorPortn": pm1008MonupRmonByteCntErrorPortn,
       "pm1008MonupRmonByteCntOverloadPortn": pm1008MonupRmonByteCntOverloadPortn,
       "pm1008MonupRmonCrcErrorCntTable": pm1008MonupRmonCrcErrorCntTable,
       "pm1008MonupRmonCrcErrorCntEntry": pm1008MonupRmonCrcErrorCntEntry,
       "pm1008MonupRmonCrcErrorCntIndex": pm1008MonupRmonCrcErrorCntIndex,
       "pm1008MonupRmonCrcErrorCntValuePortn": pm1008MonupRmonCrcErrorCntValuePortn,
       "pm1008MonupRmonCrcErrorCntErrorPortn": pm1008MonupRmonCrcErrorCntErrorPortn,
       "pm1008MonupRmonCrcErrorCntOverloadPortn": pm1008MonupRmonCrcErrorCntOverloadPortn,
       "pm1008MonupRmonPacketsCntTable": pm1008MonupRmonPacketsCntTable,
       "pm1008MonupRmonPacketsCntEntry": pm1008MonupRmonPacketsCntEntry,
       "pm1008MonupRmonPacketsCntIndex": pm1008MonupRmonPacketsCntIndex,
       "pm1008MonupRmonPacketsCntValuePortn": pm1008MonupRmonPacketsCntValuePortn,
       "pm1008MonupRmonPacketsCntErrorPortn": pm1008MonupRmonPacketsCntErrorPortn,
       "pm1008MonupRmonPacketsCntOverloadPortn": pm1008MonupRmonPacketsCntOverloadPortn,
       "pm1008MonupRmonBroadcastCntTable": pm1008MonupRmonBroadcastCntTable,
       "pm1008MonupRmonBroadcastCntEntry": pm1008MonupRmonBroadcastCntEntry,
       "pm1008MonupRmonBroadcastCntIndex": pm1008MonupRmonBroadcastCntIndex,
       "pm1008MonupRmonBroadcastCntValuePortn": pm1008MonupRmonBroadcastCntValuePortn,
       "pm1008MonupRmonBroadcastCntErrorPortn": pm1008MonupRmonBroadcastCntErrorPortn,
       "pm1008MonupRmonBroadcastCntOverloadPortn": pm1008MonupRmonBroadcastCntOverloadPortn,
       "pm1008MonupRmonMulticastCntTable": pm1008MonupRmonMulticastCntTable,
       "pm1008MonupRmonMulticastCntEntry": pm1008MonupRmonMulticastCntEntry,
       "pm1008MonupRmonMulticastCntIndex": pm1008MonupRmonMulticastCntIndex,
       "pm1008MonupRmonMulticastCntValuePortn": pm1008MonupRmonMulticastCntValuePortn,
       "pm1008MonupRmonMulticastCntErrorPortn": pm1008MonupRmonMulticastCntErrorPortn,
       "pm1008MonupRmonMulticastCntOverloadPortn": pm1008MonupRmonMulticastCntOverloadPortn}
)
