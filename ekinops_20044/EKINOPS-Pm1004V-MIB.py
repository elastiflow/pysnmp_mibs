# SNMP MIB module (EKINOPS-Pm1004V-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm1004V-MIB.mib
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

modulePm1004v = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32)
)
if mibBuilder.loadTexts:
    modulePm1004v.setRevisions(
        ("2008-03-11 00:00",
         "2008-08-18 00:00",
         "2008-12-02 00:00",
         "2008-12-08 00:00",
         "2009-05-26 00:00",
         "2009-07-22 00:00",
         "2009-09-02 00:00",
         "2009-10-27 00:00",
         "2010-03-03 00:00",
         "2011-02-04 00:00",
         "2011-04-29 00:00",
         "2012-07-03 00:00",
         "2014-03-28 00:00",
         "2014-12-23 00:00",
         "2016-05-20 00:00",
         "2016-06-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm1004vModeTimeSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            256
        )
    )
    namedValues = NamedValues(
        ("singleSplitSelect", 256)
    )



class Pm1004vModeAddDrop(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            256
        )
    )
    namedValues = NamedValues(
        ("singleSplitSelect", 256)
    )



class Pm1004vProtectionTimeSlot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              257,
              513)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("manualX2Line2", 257),
          ("manualX1Line1", 513))
    )



class Pm1004vProtectionStartUp(TextualConvention, Integer32):
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
        *(("manualX2Line2", 0),
          ("manualX1Line1", 1),
          ("auto", 2))
    )



class Pm1004vDccMode(TextualConvention, Integer32):
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



class Pm1004vClientOosMode(TextualConvention, Integer32):
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
        *(("clientportis", 0),
          ("clienttxoos", 1),
          ("clientrxoos", 2),
          ("clientportoos", 3))
    )



class Pm1004vOtxMode(TextualConvention, Integer32):
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



class Pm1004vOtxGrid(TextualConvention, Integer32):
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



class Pm1004vAdjustValue(TextualConvention, Integer32):
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



class Pm1004vOtxChannel(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Pm1004valarms_ObjectIdentity = ObjectIdentity
pm1004valarms = _Pm1004valarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2)
)
_Pm1004vAlmOther_ObjectIdentity = ObjectIdentity
pm1004vAlmOther = _Pm1004vAlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1)
)
_Pm1004vAlmOtherNurg_ObjectIdentity = ObjectIdentity
pm1004vAlmOtherNurg = _Pm1004vAlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1)
)
_Pm1004vAlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm1004vAlmsynthAlm2 = _Pm1004vAlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1, 2)
)
_Pm1004vAlmConfTableSave_Type = EkiOnOff
_Pm1004vAlmConfTableSave_Object = MibScalar
pm1004vAlmConfTableSave = _Pm1004vAlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1, 2, 1),
    _Pm1004vAlmConfTableSave_Type()
)
pm1004vAlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmConfTableSave.setStatus("current")
_Pm1004vAlmInvUpload_Type = EkiOnOff
_Pm1004vAlmInvUpload_Object = MibScalar
pm1004vAlmInvUpload = _Pm1004vAlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1, 2, 2),
    _Pm1004vAlmInvUpload_Type()
)
pm1004vAlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmInvUpload.setStatus("current")
_Pm1004vAlmConfTableLoad_Type = EkiOnOff
_Pm1004vAlmConfTableLoad_Object = MibScalar
pm1004vAlmConfTableLoad = _Pm1004vAlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1, 2, 3),
    _Pm1004vAlmConfTableLoad_Type()
)
pm1004vAlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmConfTableLoad.setStatus("current")
_Pm1004vAlmCorrelatOff_Type = EkiOnOff
_Pm1004vAlmCorrelatOff_Object = MibScalar
pm1004vAlmCorrelatOff = _Pm1004vAlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1, 2, 4),
    _Pm1004vAlmCorrelatOff_Type()
)
pm1004vAlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmCorrelatOff.setStatus("current")
_Pm1004vAlmMaintenanceOn_Type = EkiOnOff
_Pm1004vAlmMaintenanceOn_Object = MibScalar
pm1004vAlmMaintenanceOn = _Pm1004vAlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 1, 2, 5),
    _Pm1004vAlmMaintenanceOn_Type()
)
pm1004vAlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmMaintenanceOn.setStatus("current")
_Pm1004vAlmOtherUrg_ObjectIdentity = ObjectIdentity
pm1004vAlmOtherUrg = _Pm1004vAlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2)
)
_Pm1004vAlmmodInitFailLevel2_ObjectIdentity = ObjectIdentity
pm1004vAlmmodInitFailLevel2 = _Pm1004vAlmmodInitFailLevel2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 194)
)
_Pm1004vAlmLedFail_Type = EkiOnOff
_Pm1004vAlmLedFail_Object = MibScalar
pm1004vAlmLedFail = _Pm1004vAlmLedFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 194, 1),
    _Pm1004vAlmLedFail_Type()
)
pm1004vAlmLedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLedFail.setStatus("current")
_Pm1004vAlmNextColdBootForced_Type = EkiOnOff
_Pm1004vAlmNextColdBootForced_Object = MibScalar
pm1004vAlmNextColdBootForced = _Pm1004vAlmNextColdBootForced_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 194, 2),
    _Pm1004vAlmNextColdBootForced_Type()
)
pm1004vAlmNextColdBootForced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmNextColdBootForced.setStatus("current")
_Pm1004vAlmBootUndone_Type = EkiOnOff
_Pm1004vAlmBootUndone_Object = MibScalar
pm1004vAlmBootUndone = _Pm1004vAlmBootUndone_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 194, 3),
    _Pm1004vAlmBootUndone_Type()
)
pm1004vAlmBootUndone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmBootUndone.setStatus("current")
_Pm1004vAlmResetHwInitFail_Type = EkiOnOff
_Pm1004vAlmResetHwInitFail_Object = MibScalar
pm1004vAlmResetHwInitFail = _Pm1004vAlmResetHwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 194, 4),
    _Pm1004vAlmResetHwInitFail_Type()
)
pm1004vAlmResetHwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmResetHwInitFail.setStatus("current")
_Pm1004vAlmSwInitFail_Type = EkiOnOff
_Pm1004vAlmSwInitFail_Object = MibScalar
pm1004vAlmSwInitFail = _Pm1004vAlmSwInitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 194, 5),
    _Pm1004vAlmSwInitFail_Type()
)
pm1004vAlmSwInitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSwInitFail.setStatus("current")
_Pm1004vAlmmodInitFailLevel3_ObjectIdentity = ObjectIdentity
pm1004vAlmmodInitFailLevel3 = _Pm1004vAlmmodInitFailLevel3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195)
)
_Pm1004vAlmGwIdentFail_Type = EkiOnOff
_Pm1004vAlmGwIdentFail_Object = MibScalar
pm1004vAlmGwIdentFail = _Pm1004vAlmGwIdentFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 1),
    _Pm1004vAlmGwIdentFail_Type()
)
pm1004vAlmGwIdentFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmGwIdentFail.setStatus("current")
_Pm1004vAlmObmTypeReadFail_Type = EkiOnOff
_Pm1004vAlmObmTypeReadFail_Object = MibScalar
pm1004vAlmObmTypeReadFail = _Pm1004vAlmObmTypeReadFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 2),
    _Pm1004vAlmObmTypeReadFail_Type()
)
pm1004vAlmObmTypeReadFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmObmTypeReadFail.setStatus("current")
_Pm1004vAlmInitModuleFail_Type = EkiOnOff
_Pm1004vAlmInitModuleFail_Object = MibScalar
pm1004vAlmInitModuleFail = _Pm1004vAlmInitModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 3),
    _Pm1004vAlmInitModuleFail_Type()
)
pm1004vAlmInitModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmInitModuleFail.setStatus("current")
_Pm1004vAlmXfp1InitFail_Type = EkiOnOff
_Pm1004vAlmXfp1InitFail_Object = MibScalar
pm1004vAlmXfp1InitFail = _Pm1004vAlmXfp1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 5),
    _Pm1004vAlmXfp1InitFail_Type()
)
pm1004vAlmXfp1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmXfp1InitFail.setStatus("current")
_Pm1004vAlmXfp2InitFail_Type = EkiOnOff
_Pm1004vAlmXfp2InitFail_Object = MibScalar
pm1004vAlmXfp2InitFail = _Pm1004vAlmXfp2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 6),
    _Pm1004vAlmXfp2InitFail_Type()
)
pm1004vAlmXfp2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmXfp2InitFail.setStatus("current")
_Pm1004vAlmLine1InitFail_Type = EkiOnOff
_Pm1004vAlmLine1InitFail_Object = MibScalar
pm1004vAlmLine1InitFail = _Pm1004vAlmLine1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 7),
    _Pm1004vAlmLine1InitFail_Type()
)
pm1004vAlmLine1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLine1InitFail.setStatus("current")
_Pm1004vAlmLine2InitFail_Type = EkiOnOff
_Pm1004vAlmLine2InitFail_Object = MibScalar
pm1004vAlmLine2InitFail = _Pm1004vAlmLine2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 8),
    _Pm1004vAlmLine2InitFail_Type()
)
pm1004vAlmLine2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLine2InitFail.setStatus("current")
_Pm1004vAlmClient1InitFail_Type = EkiOnOff
_Pm1004vAlmClient1InitFail_Object = MibScalar
pm1004vAlmClient1InitFail = _Pm1004vAlmClient1InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 9),
    _Pm1004vAlmClient1InitFail_Type()
)
pm1004vAlmClient1InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClient1InitFail.setStatus("current")
_Pm1004vAlmClient2InitFail_Type = EkiOnOff
_Pm1004vAlmClient2InitFail_Object = MibScalar
pm1004vAlmClient2InitFail = _Pm1004vAlmClient2InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 10),
    _Pm1004vAlmClient2InitFail_Type()
)
pm1004vAlmClient2InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClient2InitFail.setStatus("current")
_Pm1004vAlmClient3InitFail_Type = EkiOnOff
_Pm1004vAlmClient3InitFail_Object = MibScalar
pm1004vAlmClient3InitFail = _Pm1004vAlmClient3InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 11),
    _Pm1004vAlmClient3InitFail_Type()
)
pm1004vAlmClient3InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClient3InitFail.setStatus("current")
_Pm1004vAlmClient4InitFail_Type = EkiOnOff
_Pm1004vAlmClient4InitFail_Object = MibScalar
pm1004vAlmClient4InitFail = _Pm1004vAlmClient4InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 12),
    _Pm1004vAlmClient4InitFail_Type()
)
pm1004vAlmClient4InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClient4InitFail.setStatus("current")
_Pm1004vAlmClient5InitFail_Type = EkiOnOff
_Pm1004vAlmClient5InitFail_Object = MibScalar
pm1004vAlmClient5InitFail = _Pm1004vAlmClient5InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 13),
    _Pm1004vAlmClient5InitFail_Type()
)
pm1004vAlmClient5InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClient5InitFail.setStatus("current")
_Pm1004vAlmClient6InitFail_Type = EkiOnOff
_Pm1004vAlmClient6InitFail_Object = MibScalar
pm1004vAlmClient6InitFail = _Pm1004vAlmClient6InitFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 195, 14),
    _Pm1004vAlmClient6InitFail_Type()
)
pm1004vAlmClient6InitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClient6InitFail.setStatus("current")
_Pm1004vAlmclientRxProt_ObjectIdentity = ObjectIdentity
pm1004vAlmclientRxProt = _Pm1004vAlmclientRxProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198)
)
_Pm1004vAlmAdddropClient1West_Type = EkiOnOff
_Pm1004vAlmAdddropClient1West_Object = MibScalar
pm1004vAlmAdddropClient1West = _Pm1004vAlmAdddropClient1West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 1),
    _Pm1004vAlmAdddropClient1West_Type()
)
pm1004vAlmAdddropClient1West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient1West.setStatus("current")
_Pm1004vAlmAdddropClient2West_Type = EkiOnOff
_Pm1004vAlmAdddropClient2West_Object = MibScalar
pm1004vAlmAdddropClient2West = _Pm1004vAlmAdddropClient2West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 2),
    _Pm1004vAlmAdddropClient2West_Type()
)
pm1004vAlmAdddropClient2West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient2West.setStatus("current")
_Pm1004vAlmAdddropClient3West_Type = EkiOnOff
_Pm1004vAlmAdddropClient3West_Object = MibScalar
pm1004vAlmAdddropClient3West = _Pm1004vAlmAdddropClient3West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 3),
    _Pm1004vAlmAdddropClient3West_Type()
)
pm1004vAlmAdddropClient3West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient3West.setStatus("current")
_Pm1004vAlmAdddropClient4West_Type = EkiOnOff
_Pm1004vAlmAdddropClient4West_Object = MibScalar
pm1004vAlmAdddropClient4West = _Pm1004vAlmAdddropClient4West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 4),
    _Pm1004vAlmAdddropClient4West_Type()
)
pm1004vAlmAdddropClient4West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient4West.setStatus("current")
_Pm1004vAlmAdddropClient5West_Type = EkiOnOff
_Pm1004vAlmAdddropClient5West_Object = MibScalar
pm1004vAlmAdddropClient5West = _Pm1004vAlmAdddropClient5West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 5),
    _Pm1004vAlmAdddropClient5West_Type()
)
pm1004vAlmAdddropClient5West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient5West.setStatus("current")
_Pm1004vAlmAdddropClient6West_Type = EkiOnOff
_Pm1004vAlmAdddropClient6West_Object = MibScalar
pm1004vAlmAdddropClient6West = _Pm1004vAlmAdddropClient6West_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 6),
    _Pm1004vAlmAdddropClient6West_Type()
)
pm1004vAlmAdddropClient6West.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient6West.setStatus("current")
_Pm1004vAlmAdddropClient1East_Type = EkiOnOff
_Pm1004vAlmAdddropClient1East_Object = MibScalar
pm1004vAlmAdddropClient1East = _Pm1004vAlmAdddropClient1East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 9),
    _Pm1004vAlmAdddropClient1East_Type()
)
pm1004vAlmAdddropClient1East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient1East.setStatus("current")
_Pm1004vAlmAdddropClient2East_Type = EkiOnOff
_Pm1004vAlmAdddropClient2East_Object = MibScalar
pm1004vAlmAdddropClient2East = _Pm1004vAlmAdddropClient2East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 10),
    _Pm1004vAlmAdddropClient2East_Type()
)
pm1004vAlmAdddropClient2East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient2East.setStatus("current")
_Pm1004vAlmAdddropClient3East_Type = EkiOnOff
_Pm1004vAlmAdddropClient3East_Object = MibScalar
pm1004vAlmAdddropClient3East = _Pm1004vAlmAdddropClient3East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 11),
    _Pm1004vAlmAdddropClient3East_Type()
)
pm1004vAlmAdddropClient3East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient3East.setStatus("current")
_Pm1004vAlmAdddropClient4East_Type = EkiOnOff
_Pm1004vAlmAdddropClient4East_Object = MibScalar
pm1004vAlmAdddropClient4East = _Pm1004vAlmAdddropClient4East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 12),
    _Pm1004vAlmAdddropClient4East_Type()
)
pm1004vAlmAdddropClient4East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient4East.setStatus("current")
_Pm1004vAlmAdddropClient5East_Type = EkiOnOff
_Pm1004vAlmAdddropClient5East_Object = MibScalar
pm1004vAlmAdddropClient5East = _Pm1004vAlmAdddropClient5East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 13),
    _Pm1004vAlmAdddropClient5East_Type()
)
pm1004vAlmAdddropClient5East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient5East.setStatus("current")
_Pm1004vAlmAdddropClient6East_Type = EkiOnOff
_Pm1004vAlmAdddropClient6East_Object = MibScalar
pm1004vAlmAdddropClient6East = _Pm1004vAlmAdddropClient6East_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 2, 198, 14),
    _Pm1004vAlmAdddropClient6East_Type()
)
pm1004vAlmAdddropClient6East.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmAdddropClient6East.setStatus("current")
_Pm1004vAlmOtherCrit_ObjectIdentity = ObjectIdentity
pm1004vAlmOtherCrit = _Pm1004vAlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 3)
)
_Pm1004vAlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm1004vAlmsynthAlm0 = _Pm1004vAlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 3, 0)
)
_Pm1004vAlmModGlobFail_Type = EkiOnOff
_Pm1004vAlmModGlobFail_Object = MibScalar
pm1004vAlmModGlobFail = _Pm1004vAlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 3, 0, 9),
    _Pm1004vAlmModGlobFail_Type()
)
pm1004vAlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmModGlobFail.setStatus("current")
_Pm1004vAlmDefFuseA_Type = EkiOnOff
_Pm1004vAlmDefFuseA_Object = MibScalar
pm1004vAlmDefFuseA = _Pm1004vAlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 3, 0, 15),
    _Pm1004vAlmDefFuseA_Type()
)
pm1004vAlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDefFuseA.setStatus("current")
_Pm1004vAlmDefFuseB_Type = EkiOnOff
_Pm1004vAlmDefFuseB_Object = MibScalar
pm1004vAlmDefFuseB = _Pm1004vAlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 1, 3, 0, 16),
    _Pm1004vAlmDefFuseB_Type()
)
pm1004vAlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDefFuseB.setStatus("current")
_Pm1004vAlmClient_ObjectIdentity = ObjectIdentity
pm1004vAlmClient = _Pm1004vAlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2)
)
_Pm1004vAlmClientNurg_ObjectIdentity = ObjectIdentity
pm1004vAlmClientNurg = _Pm1004vAlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1)
)
_Pm1004vAlmsfpWarnDdmTable_Object = MibTable
pm1004vAlmsfpWarnDdmTable = _Pm1004vAlmsfpWarnDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48)
)
if mibBuilder.loadTexts:
    pm1004vAlmsfpWarnDdmTable.setStatus("current")
_Pm1004vAlmsfpWarnDdmEntry_Object = MibTableRow
pm1004vAlmsfpWarnDdmEntry = _Pm1004vAlmsfpWarnDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1)
)
pm1004vAlmsfpWarnDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmsfpWarnDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmsfpWarnDdmEntry.setStatus("current")


class _Pm1004vAlmsfpWarnDdmIndex_Type(Integer32):
    """Custom type pm1004vAlmsfpWarnDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmsfpWarnDdmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmsfpWarnDdmIndex_Object = MibTableColumn
pm1004vAlmsfpWarnDdmIndex = _Pm1004vAlmsfpWarnDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 1),
    _Pm1004vAlmsfpWarnDdmIndex_Type()
)
pm1004vAlmsfpWarnDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmsfpWarnDdmIndex.setStatus("current")
_Pm1004vAlmTxPwLowWngPortn_Type = EkiOnOff
_Pm1004vAlmTxPwLowWngPortn_Object = MibTableColumn
pm1004vAlmTxPwLowWngPortn = _Pm1004vAlmTxPwLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 2),
    _Pm1004vAlmTxPwLowWngPortn_Type()
)
pm1004vAlmTxPwLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPwLowWngPortn.setStatus("current")
_Pm1004vAlmTxPwrHighWngPortn_Type = EkiOnOff
_Pm1004vAlmTxPwrHighWngPortn_Object = MibTableColumn
pm1004vAlmTxPwrHighWngPortn = _Pm1004vAlmTxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 3),
    _Pm1004vAlmTxPwrHighWngPortn_Type()
)
pm1004vAlmTxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPwrHighWngPortn.setStatus("current")
_Pm1004vAlmTxBiasLowWngPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasLowWngPortn_Object = MibTableColumn
pm1004vAlmTxBiasLowWngPortn = _Pm1004vAlmTxBiasLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 4),
    _Pm1004vAlmTxBiasLowWngPortn_Type()
)
pm1004vAlmTxBiasLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasLowWngPortn.setStatus("current")
_Pm1004vAlmTxBiasHighWngPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasHighWngPortn_Object = MibTableColumn
pm1004vAlmTxBiasHighWngPortn = _Pm1004vAlmTxBiasHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 5),
    _Pm1004vAlmTxBiasHighWngPortn_Type()
)
pm1004vAlmTxBiasHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasHighWngPortn.setStatus("current")
_Pm1004vAlmVccLowWngPortn_Type = EkiOnOff
_Pm1004vAlmVccLowWngPortn_Object = MibTableColumn
pm1004vAlmVccLowWngPortn = _Pm1004vAlmVccLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 6),
    _Pm1004vAlmVccLowWngPortn_Type()
)
pm1004vAlmVccLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVccLowWngPortn.setStatus("current")
_Pm1004vAlmVccHighWngPortn_Type = EkiOnOff
_Pm1004vAlmVccHighWngPortn_Object = MibTableColumn
pm1004vAlmVccHighWngPortn = _Pm1004vAlmVccHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 7),
    _Pm1004vAlmVccHighWngPortn_Type()
)
pm1004vAlmVccHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVccHighWngPortn.setStatus("current")
_Pm1004vAlmTempLowWngPortn_Type = EkiOnOff
_Pm1004vAlmTempLowWngPortn_Object = MibTableColumn
pm1004vAlmTempLowWngPortn = _Pm1004vAlmTempLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 8),
    _Pm1004vAlmTempLowWngPortn_Type()
)
pm1004vAlmTempLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempLowWngPortn.setStatus("current")
_Pm1004vAlmTempHighWngPortn_Type = EkiOnOff
_Pm1004vAlmTempHighWngPortn_Object = MibTableColumn
pm1004vAlmTempHighWngPortn = _Pm1004vAlmTempHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 9),
    _Pm1004vAlmTempHighWngPortn_Type()
)
pm1004vAlmTempHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempHighWngPortn.setStatus("current")
_Pm1004vAlmRxPwrLowWngPortn_Type = EkiOnOff
_Pm1004vAlmRxPwrLowWngPortn_Object = MibTableColumn
pm1004vAlmRxPwrLowWngPortn = _Pm1004vAlmRxPwrLowWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 16),
    _Pm1004vAlmRxPwrLowWngPortn_Type()
)
pm1004vAlmRxPwrLowWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPwrLowWngPortn.setStatus("current")
_Pm1004vAlmRxPwrHighWngPortn_Type = EkiOnOff
_Pm1004vAlmRxPwrHighWngPortn_Object = MibTableColumn
pm1004vAlmRxPwrHighWngPortn = _Pm1004vAlmRxPwrHighWngPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 48, 1, 17),
    _Pm1004vAlmRxPwrHighWngPortn_Type()
)
pm1004vAlmRxPwrHighWngPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPwrHighWngPortn.setStatus("current")
_Pm1004vAlmsfpCritDdmTable_Object = MibTable
pm1004vAlmsfpCritDdmTable = _Pm1004vAlmsfpCritDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56)
)
if mibBuilder.loadTexts:
    pm1004vAlmsfpCritDdmTable.setStatus("current")
_Pm1004vAlmsfpCritDdmEntry_Object = MibTableRow
pm1004vAlmsfpCritDdmEntry = _Pm1004vAlmsfpCritDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56, 1)
)
pm1004vAlmsfpCritDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmsfpCritDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmsfpCritDdmEntry.setStatus("current")


class _Pm1004vAlmsfpCritDdmIndex_Type(Integer32):
    """Custom type pm1004vAlmsfpCritDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmsfpCritDdmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmsfpCritDdmIndex_Object = MibTableColumn
pm1004vAlmsfpCritDdmIndex = _Pm1004vAlmsfpCritDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56, 1, 1),
    _Pm1004vAlmsfpCritDdmIndex_Type()
)
pm1004vAlmsfpCritDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmsfpCritDdmIndex.setStatus("current")
_Pm1004vAlmTxPwrLowCritPortn_Type = EkiOnOff
_Pm1004vAlmTxPwrLowCritPortn_Object = MibTableColumn
pm1004vAlmTxPwrLowCritPortn = _Pm1004vAlmTxPwrLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56, 1, 2),
    _Pm1004vAlmTxPwrLowCritPortn_Type()
)
pm1004vAlmTxPwrLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPwrLowCritPortn.setStatus("current")
_Pm1004vAlmTxPwrHighCritPortn_Type = EkiOnOff
_Pm1004vAlmTxPwrHighCritPortn_Object = MibTableColumn
pm1004vAlmTxPwrHighCritPortn = _Pm1004vAlmTxPwrHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56, 1, 3),
    _Pm1004vAlmTxPwrHighCritPortn_Type()
)
pm1004vAlmTxPwrHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPwrHighCritPortn.setStatus("current")
_Pm1004vAlmRxPwrLowCritPortn_Type = EkiOnOff
_Pm1004vAlmRxPwrLowCritPortn_Object = MibTableColumn
pm1004vAlmRxPwrLowCritPortn = _Pm1004vAlmRxPwrLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56, 1, 16),
    _Pm1004vAlmRxPwrLowCritPortn_Type()
)
pm1004vAlmRxPwrLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPwrLowCritPortn.setStatus("current")
_Pm1004vAlmRxPwrHighCritPortn_Type = EkiOnOff
_Pm1004vAlmRxPwrHighCritPortn_Object = MibTableColumn
pm1004vAlmRxPwrHighCritPortn = _Pm1004vAlmRxPwrHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 1, 56, 1, 17),
    _Pm1004vAlmRxPwrHighCritPortn_Type()
)
pm1004vAlmRxPwrHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPwrHighCritPortn.setStatus("current")
_Pm1004vAlmClientUrg_ObjectIdentity = ObjectIdentity
pm1004vAlmClientUrg = _Pm1004vAlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2)
)
_Pm1004vAlmsfpAlmDdmTable_Object = MibTable
pm1004vAlmsfpAlmDdmTable = _Pm1004vAlmsfpAlmDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004vAlmsfpAlmDdmTable.setStatus("current")
_Pm1004vAlmsfpAlmDdmEntry_Object = MibTableRow
pm1004vAlmsfpAlmDdmEntry = _Pm1004vAlmsfpAlmDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1)
)
pm1004vAlmsfpAlmDdmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmsfpAlmDdmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmsfpAlmDdmEntry.setStatus("current")


class _Pm1004vAlmsfpAlmDdmIndex_Type(Integer32):
    """Custom type pm1004vAlmsfpAlmDdmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmsfpAlmDdmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmsfpAlmDdmIndex_Object = MibTableColumn
pm1004vAlmsfpAlmDdmIndex = _Pm1004vAlmsfpAlmDdmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 1),
    _Pm1004vAlmsfpAlmDdmIndex_Type()
)
pm1004vAlmsfpAlmDdmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmsfpAlmDdmIndex.setStatus("current")
_Pm1004vAlmTxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004vAlmTxPwrLowAlaPortn_Object = MibTableColumn
pm1004vAlmTxPwrLowAlaPortn = _Pm1004vAlmTxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 2),
    _Pm1004vAlmTxPwrLowAlaPortn_Type()
)
pm1004vAlmTxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPwrLowAlaPortn.setStatus("current")
_Pm1004vAlmTxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmTxPwrHighAlaPortn_Object = MibTableColumn
pm1004vAlmTxPwrHighAlaPortn = _Pm1004vAlmTxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 3),
    _Pm1004vAlmTxPwrHighAlaPortn_Type()
)
pm1004vAlmTxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPwrHighAlaPortn.setStatus("current")
_Pm1004vAlmTxBiasLowAlaPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasLowAlaPortn_Object = MibTableColumn
pm1004vAlmTxBiasLowAlaPortn = _Pm1004vAlmTxBiasLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 4),
    _Pm1004vAlmTxBiasLowAlaPortn_Type()
)
pm1004vAlmTxBiasLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasLowAlaPortn.setStatus("current")
_Pm1004vAlmTxBiasHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasHighAlaPortn_Object = MibTableColumn
pm1004vAlmTxBiasHighAlaPortn = _Pm1004vAlmTxBiasHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 5),
    _Pm1004vAlmTxBiasHighAlaPortn_Type()
)
pm1004vAlmTxBiasHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasHighAlaPortn.setStatus("current")
_Pm1004vAlmVccLowAlaPortn_Type = EkiOnOff
_Pm1004vAlmVccLowAlaPortn_Object = MibTableColumn
pm1004vAlmVccLowAlaPortn = _Pm1004vAlmVccLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 6),
    _Pm1004vAlmVccLowAlaPortn_Type()
)
pm1004vAlmVccLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVccLowAlaPortn.setStatus("current")
_Pm1004vAlmVccHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmVccHighAlaPortn_Object = MibTableColumn
pm1004vAlmVccHighAlaPortn = _Pm1004vAlmVccHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 7),
    _Pm1004vAlmVccHighAlaPortn_Type()
)
pm1004vAlmVccHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVccHighAlaPortn.setStatus("current")
_Pm1004vAlmTempLowAlaPortn_Type = EkiOnOff
_Pm1004vAlmTempLowAlaPortn_Object = MibTableColumn
pm1004vAlmTempLowAlaPortn = _Pm1004vAlmTempLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 8),
    _Pm1004vAlmTempLowAlaPortn_Type()
)
pm1004vAlmTempLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempLowAlaPortn.setStatus("current")
_Pm1004vAlmTempHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmTempHighAlaPortn_Object = MibTableColumn
pm1004vAlmTempHighAlaPortn = _Pm1004vAlmTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 9),
    _Pm1004vAlmTempHighAlaPortn_Type()
)
pm1004vAlmTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempHighAlaPortn.setStatus("current")
_Pm1004vAlmRxPwrLowAlaPortn_Type = EkiOnOff
_Pm1004vAlmRxPwrLowAlaPortn_Object = MibTableColumn
pm1004vAlmRxPwrLowAlaPortn = _Pm1004vAlmRxPwrLowAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 16),
    _Pm1004vAlmRxPwrLowAlaPortn_Type()
)
pm1004vAlmRxPwrLowAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPwrLowAlaPortn.setStatus("current")
_Pm1004vAlmRxPwrHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmRxPwrHighAlaPortn_Object = MibTableColumn
pm1004vAlmRxPwrHighAlaPortn = _Pm1004vAlmRxPwrHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 2, 32, 1, 17),
    _Pm1004vAlmRxPwrHighAlaPortn_Type()
)
pm1004vAlmRxPwrHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPwrHighAlaPortn.setStatus("current")
_Pm1004vAlmClientCrit_ObjectIdentity = ObjectIdentity
pm1004vAlmClientCrit = _Pm1004vAlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3)
)
_Pm1004vAlmsynthAlmPortTable_Object = MibTable
pm1004vAlmsynthAlmPortTable = _Pm1004vAlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm1004vAlmsynthAlmPortTable.setStatus("current")
_Pm1004vAlmsynthAlmPortEntry_Object = MibTableRow
pm1004vAlmsynthAlmPortEntry = _Pm1004vAlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1)
)
pm1004vAlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmsynthAlmPortEntry.setStatus("current")


class _Pm1004vAlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm1004vAlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm1004vAlmsynthAlmPortIndex_Object = MibTableColumn
pm1004vAlmsynthAlmPortIndex = _Pm1004vAlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 1),
    _Pm1004vAlmsynthAlmPortIndex_Type()
)
pm1004vAlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmsynthAlmPortIndex.setStatus("current")
_Pm1004vAlmSfpAbsentPortn_Type = EkiOnOff
_Pm1004vAlmSfpAbsentPortn_Object = MibTableColumn
pm1004vAlmSfpAbsentPortn = _Pm1004vAlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 2),
    _Pm1004vAlmSfpAbsentPortn_Type()
)
pm1004vAlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSfpAbsentPortn.setStatus("current")
_Pm1004vAlmDdmAbsentPortn_Type = EkiOnOff
_Pm1004vAlmDdmAbsentPortn_Object = MibTableColumn
pm1004vAlmDdmAbsentPortn = _Pm1004vAlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 3),
    _Pm1004vAlmDdmAbsentPortn_Type()
)
pm1004vAlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDdmAbsentPortn.setStatus("current")
_Pm1004vAlmHwFailAccPortn_Type = EkiOnOff
_Pm1004vAlmHwFailAccPortn_Object = MibTableColumn
pm1004vAlmHwFailAccPortn = _Pm1004vAlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 5),
    _Pm1004vAlmHwFailAccPortn_Type()
)
pm1004vAlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmHwFailAccPortn.setStatus("current")
_Pm1004vAlmDwLsdPortn_Type = EkiOnOff
_Pm1004vAlmDwLsdPortn_Object = MibTableColumn
pm1004vAlmDwLsdPortn = _Pm1004vAlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 6),
    _Pm1004vAlmDwLsdPortn_Type()
)
pm1004vAlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwLsdPortn.setStatus("current")
_Pm1004vAlmClientLocalOosTxPortn_Type = EkiOnOff
_Pm1004vAlmClientLocalOosTxPortn_Object = MibTableColumn
pm1004vAlmClientLocalOosTxPortn = _Pm1004vAlmClientLocalOosTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 7),
    _Pm1004vAlmClientLocalOosTxPortn_Type()
)
pm1004vAlmClientLocalOosTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClientLocalOosTxPortn.setStatus("current")
_Pm1004vAlmClientLocalOosRxPortn_Type = EkiOnOff
_Pm1004vAlmClientLocalOosRxPortn_Object = MibTableColumn
pm1004vAlmClientLocalOosRxPortn = _Pm1004vAlmClientLocalOosRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 8),
    _Pm1004vAlmClientLocalOosRxPortn_Type()
)
pm1004vAlmClientLocalOosRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClientLocalOosRxPortn.setStatus("current")
_Pm1004vAlmDwCaisPortn_Type = EkiOnOff
_Pm1004vAlmDwCaisPortn_Object = MibTableColumn
pm1004vAlmDwCaisPortn = _Pm1004vAlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 9),
    _Pm1004vAlmDwCaisPortn_Type()
)
pm1004vAlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwCaisPortn.setStatus("current")
_Pm1004vAlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm1004vAlmSfpDdmWarningPortn_Object = MibTableColumn
pm1004vAlmSfpDdmWarningPortn = _Pm1004vAlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 10),
    _Pm1004vAlmSfpDdmWarningPortn_Type()
)
pm1004vAlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSfpDdmWarningPortn.setStatus("current")
_Pm1004vAlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm1004vAlmSfpDdmAlmPortn_Object = MibTableColumn
pm1004vAlmSfpDdmAlmPortn = _Pm1004vAlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 11),
    _Pm1004vAlmSfpDdmAlmPortn_Type()
)
pm1004vAlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSfpDdmAlmPortn.setStatus("current")
_Pm1004vAlmSfpDdmCritPortn_Type = EkiOnOff
_Pm1004vAlmSfpDdmCritPortn_Object = MibTableColumn
pm1004vAlmSfpDdmCritPortn = _Pm1004vAlmSfpDdmCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 12),
    _Pm1004vAlmSfpDdmCritPortn_Type()
)
pm1004vAlmSfpDdmCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSfpDdmCritPortn.setStatus("current")
_Pm1004vAlmFailAccPortn_Type = EkiOnOff
_Pm1004vAlmFailAccPortn_Object = MibTableColumn
pm1004vAlmFailAccPortn = _Pm1004vAlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 13),
    _Pm1004vAlmFailAccPortn_Type()
)
pm1004vAlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmFailAccPortn.setStatus("current")
_Pm1004vAlmClientActivePortn_Type = EkiOnOff
_Pm1004vAlmClientActivePortn_Object = MibTableColumn
pm1004vAlmClientActivePortn = _Pm1004vAlmClientActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 16),
    _Pm1004vAlmClientActivePortn_Type()
)
pm1004vAlmClientActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmClientActivePortn.setStatus("current")
_Pm1004vAlmUpCsfPortn_Type = EkiOnOff
_Pm1004vAlmUpCsfPortn_Object = MibTableColumn
pm1004vAlmUpCsfPortn = _Pm1004vAlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 8, 1, 17),
    _Pm1004vAlmUpCsfPortn_Type()
)
pm1004vAlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmUpCsfPortn.setStatus("current")
_Pm1004vAlmaccessioAlmTable_Object = MibTable
pm1004vAlmaccessioAlmTable = _Pm1004vAlmaccessioAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 16)
)
if mibBuilder.loadTexts:
    pm1004vAlmaccessioAlmTable.setStatus("current")
_Pm1004vAlmaccessioAlmEntry_Object = MibTableRow
pm1004vAlmaccessioAlmEntry = _Pm1004vAlmaccessioAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 16, 1)
)
pm1004vAlmaccessioAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmaccessioAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmaccessioAlmEntry.setStatus("current")


class _Pm1004vAlmaccessioAlmIndex_Type(Integer32):
    """Custom type pm1004vAlmaccessioAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmaccessioAlmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmaccessioAlmIndex_Object = MibTableColumn
pm1004vAlmaccessioAlmIndex = _Pm1004vAlmaccessioAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 16, 1, 1),
    _Pm1004vAlmaccessioAlmIndex_Type()
)
pm1004vAlmaccessioAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmaccessioAlmIndex.setStatus("current")
_Pm1004vAlmDwLasFailPortn_Type = EkiOnOff
_Pm1004vAlmDwLasFailPortn_Object = MibTableColumn
pm1004vAlmDwLasFailPortn = _Pm1004vAlmDwLasFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 16, 1, 2),
    _Pm1004vAlmDwLasFailPortn_Type()
)
pm1004vAlmDwLasFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwLasFailPortn.setStatus("current")
_Pm1004vAlmUpLosPortn_Type = EkiOnOff
_Pm1004vAlmUpLosPortn_Object = MibTableColumn
pm1004vAlmUpLosPortn = _Pm1004vAlmUpLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 16, 1, 5),
    _Pm1004vAlmUpLosPortn_Type()
)
pm1004vAlmUpLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmUpLosPortn.setStatus("current")
_Pm1004vAlmmapperDeAlmTable_Object = MibTable
pm1004vAlmmapperDeAlmTable = _Pm1004vAlmmapperDeAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72)
)
if mibBuilder.loadTexts:
    pm1004vAlmmapperDeAlmTable.setStatus("current")
_Pm1004vAlmmapperDeAlmEntry_Object = MibTableRow
pm1004vAlmmapperDeAlmEntry = _Pm1004vAlmmapperDeAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72, 1)
)
pm1004vAlmmapperDeAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmmapperDeAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmmapperDeAlmEntry.setStatus("current")


class _Pm1004vAlmmapperDeAlmIndex_Type(Integer32):
    """Custom type pm1004vAlmmapperDeAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmmapperDeAlmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmmapperDeAlmIndex_Object = MibTableColumn
pm1004vAlmmapperDeAlmIndex = _Pm1004vAlmmapperDeAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72, 1, 1),
    _Pm1004vAlmmapperDeAlmIndex_Type()
)
pm1004vAlmmapperDeAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmmapperDeAlmIndex.setStatus("current")
_Pm1004vAlmUpAccOosPortn_Type = EkiOnOff
_Pm1004vAlmUpAccOosPortn_Object = MibTableColumn
pm1004vAlmUpAccOosPortn = _Pm1004vAlmUpAccOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72, 1, 2),
    _Pm1004vAlmUpAccOosPortn_Type()
)
pm1004vAlmUpAccOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmUpAccOosPortn.setStatus("current")
_Pm1004vAlmUpBufferOvlPortn_Type = EkiOnOff
_Pm1004vAlmUpBufferOvlPortn_Object = MibTableColumn
pm1004vAlmUpBufferOvlPortn = _Pm1004vAlmUpBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72, 1, 11),
    _Pm1004vAlmUpBufferOvlPortn_Type()
)
pm1004vAlmUpBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmUpBufferOvlPortn.setStatus("current")
_Pm1004vAlmDwCsfDetPortn_Type = EkiOnOff
_Pm1004vAlmDwCsfDetPortn_Object = MibTableColumn
pm1004vAlmDwCsfDetPortn = _Pm1004vAlmDwCsfDetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72, 1, 12),
    _Pm1004vAlmDwCsfDetPortn_Type()
)
pm1004vAlmDwCsfDetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwCsfDetPortn.setStatus("current")
_Pm1004vAlmDwBufferOvlPortn_Type = EkiOnOff
_Pm1004vAlmDwBufferOvlPortn_Object = MibTableColumn
pm1004vAlmDwBufferOvlPortn = _Pm1004vAlmDwBufferOvlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 72, 1, 15),
    _Pm1004vAlmDwBufferOvlPortn_Type()
)
pm1004vAlmDwBufferOvlPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwBufferOvlPortn.setStatus("current")
_Pm1004vAlmvideoProtocolStatusTable_Object = MibTable
pm1004vAlmvideoProtocolStatusTable = _Pm1004vAlmvideoProtocolStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112)
)
if mibBuilder.loadTexts:
    pm1004vAlmvideoProtocolStatusTable.setStatus("current")
_Pm1004vAlmvideoProtocolStatusEntry_Object = MibTableRow
pm1004vAlmvideoProtocolStatusEntry = _Pm1004vAlmvideoProtocolStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1)
)
pm1004vAlmvideoProtocolStatusEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmvideoProtocolStatusIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmvideoProtocolStatusEntry.setStatus("current")


class _Pm1004vAlmvideoProtocolStatusIndex_Type(Integer32):
    """Custom type pm1004vAlmvideoProtocolStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmvideoProtocolStatusIndex_Type.__name__ = "Integer32"
_Pm1004vAlmvideoProtocolStatusIndex_Object = MibTableColumn
pm1004vAlmvideoProtocolStatusIndex = _Pm1004vAlmvideoProtocolStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 1),
    _Pm1004vAlmvideoProtocolStatusIndex_Type()
)
pm1004vAlmvideoProtocolStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmvideoProtocolStatusIndex.setStatus("current")
_Pm1004vAlmSdiTxPortn_Type = EkiOnOff
_Pm1004vAlmSdiTxPortn_Object = MibTableColumn
pm1004vAlmSdiTxPortn = _Pm1004vAlmSdiTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 2),
    _Pm1004vAlmSdiTxPortn_Type()
)
pm1004vAlmSdiTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSdiTxPortn.setStatus("current")
_Pm1004vAlmHdSdiPalTxPortn_Type = EkiOnOff
_Pm1004vAlmHdSdiPalTxPortn_Object = MibTableColumn
pm1004vAlmHdSdiPalTxPortn = _Pm1004vAlmHdSdiPalTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 3),
    _Pm1004vAlmHdSdiPalTxPortn_Type()
)
pm1004vAlmHdSdiPalTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmHdSdiPalTxPortn.setStatus("current")
_Pm1004vAlmHdSdiNtscTxPortn_Type = EkiOnOff
_Pm1004vAlmHdSdiNtscTxPortn_Object = MibTableColumn
pm1004vAlmHdSdiNtscTxPortn = _Pm1004vAlmHdSdiNtscTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 4),
    _Pm1004vAlmHdSdiNtscTxPortn_Type()
)
pm1004vAlmHdSdiNtscTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmHdSdiNtscTxPortn.setStatus("current")
_Pm1004vAlmDvbAsiTxPortn_Type = EkiOnOff
_Pm1004vAlmDvbAsiTxPortn_Object = MibTableColumn
pm1004vAlmDvbAsiTxPortn = _Pm1004vAlmDvbAsiTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 5),
    _Pm1004vAlmDvbAsiTxPortn_Type()
)
pm1004vAlmDvbAsiTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDvbAsiTxPortn.setStatus("current")
_Pm1004vAlmFastEtherTxPortn_Type = EkiOnOff
_Pm1004vAlmFastEtherTxPortn_Object = MibTableColumn
pm1004vAlmFastEtherTxPortn = _Pm1004vAlmFastEtherTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 6),
    _Pm1004vAlmFastEtherTxPortn_Type()
)
pm1004vAlmFastEtherTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmFastEtherTxPortn.setStatus("current")
_Pm1004vAlmGbeTxPortn_Type = EkiOnOff
_Pm1004vAlmGbeTxPortn_Object = MibTableColumn
pm1004vAlmGbeTxPortn = _Pm1004vAlmGbeTxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 7),
    _Pm1004vAlmGbeTxPortn_Type()
)
pm1004vAlmGbeTxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmGbeTxPortn.setStatus("current")
_Pm1004vAlmSdiRxPortn_Type = EkiOnOff
_Pm1004vAlmSdiRxPortn_Object = MibTableColumn
pm1004vAlmSdiRxPortn = _Pm1004vAlmSdiRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 10),
    _Pm1004vAlmSdiRxPortn_Type()
)
pm1004vAlmSdiRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmSdiRxPortn.setStatus("current")
_Pm1004vAlmHdSdiPalRxPortn_Type = EkiOnOff
_Pm1004vAlmHdSdiPalRxPortn_Object = MibTableColumn
pm1004vAlmHdSdiPalRxPortn = _Pm1004vAlmHdSdiPalRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 11),
    _Pm1004vAlmHdSdiPalRxPortn_Type()
)
pm1004vAlmHdSdiPalRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmHdSdiPalRxPortn.setStatus("current")
_Pm1004vAlmHdSdiNtscRxPortn_Type = EkiOnOff
_Pm1004vAlmHdSdiNtscRxPortn_Object = MibTableColumn
pm1004vAlmHdSdiNtscRxPortn = _Pm1004vAlmHdSdiNtscRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 12),
    _Pm1004vAlmHdSdiNtscRxPortn_Type()
)
pm1004vAlmHdSdiNtscRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmHdSdiNtscRxPortn.setStatus("current")
_Pm1004vAlmDvbAsiRxPortn_Type = EkiOnOff
_Pm1004vAlmDvbAsiRxPortn_Object = MibTableColumn
pm1004vAlmDvbAsiRxPortn = _Pm1004vAlmDvbAsiRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 13),
    _Pm1004vAlmDvbAsiRxPortn_Type()
)
pm1004vAlmDvbAsiRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDvbAsiRxPortn.setStatus("current")
_Pm1004vAlmFastEtherRxPortn_Type = EkiOnOff
_Pm1004vAlmFastEtherRxPortn_Object = MibTableColumn
pm1004vAlmFastEtherRxPortn = _Pm1004vAlmFastEtherRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 14),
    _Pm1004vAlmFastEtherRxPortn_Type()
)
pm1004vAlmFastEtherRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmFastEtherRxPortn.setStatus("current")
_Pm1004vAlmGbeRxPortn_Type = EkiOnOff
_Pm1004vAlmGbeRxPortn_Object = MibTableColumn
pm1004vAlmGbeRxPortn = _Pm1004vAlmGbeRxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 2, 3, 112, 1, 15),
    _Pm1004vAlmGbeRxPortn_Type()
)
pm1004vAlmGbeRxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmGbeRxPortn.setStatus("current")
_Pm1004vAlmLine_ObjectIdentity = ObjectIdentity
pm1004vAlmLine = _Pm1004vAlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3)
)
_Pm1004vAlmLineNurg_ObjectIdentity = ObjectIdentity
pm1004vAlmLineNurg = _Pm1004vAlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1)
)
_Pm1004vAlmlineXfp1WarningsTable_Object = MibTable
pm1004vAlmlineXfp1WarningsTable = _Pm1004vAlmlineXfp1WarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1WarningsTable.setStatus("current")
_Pm1004vAlmlineXfp1WarningsEntry_Object = MibTableRow
pm1004vAlmlineXfp1WarningsEntry = _Pm1004vAlmlineXfp1WarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1)
)
pm1004vAlmlineXfp1WarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineXfp1WarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1WarningsEntry.setStatus("current")


class _Pm1004vAlmlineXfp1WarningsIndex_Type(Integer32):
    """Custom type pm1004vAlmlineXfp1WarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineXfp1WarningsIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineXfp1WarningsIndex_Object = MibTableColumn
pm1004vAlmlineXfp1WarningsIndex = _Pm1004vAlmlineXfp1WarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 1),
    _Pm1004vAlmlineXfp1WarningsIndex_Type()
)
pm1004vAlmlineXfp1WarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1WarningsIndex.setStatus("current")
_Pm1004vAlmTxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004vAlmTxPowerLowWarningPortn_Object = MibTableColumn
pm1004vAlmTxPowerLowWarningPortn = _Pm1004vAlmTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 2),
    _Pm1004vAlmTxPowerLowWarningPortn_Type()
)
pm1004vAlmTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPowerLowWarningPortn.setStatus("current")
_Pm1004vAlmTxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmTxPowerHighWarningPortn_Object = MibTableColumn
pm1004vAlmTxPowerHighWarningPortn = _Pm1004vAlmTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 3),
    _Pm1004vAlmTxPowerHighWarningPortn_Type()
)
pm1004vAlmTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPowerHighWarningPortn.setStatus("current")
_Pm1004vAlmTxBiasLowWarningPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasLowWarningPortn_Object = MibTableColumn
pm1004vAlmTxBiasLowWarningPortn = _Pm1004vAlmTxBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 4),
    _Pm1004vAlmTxBiasLowWarningPortn_Type()
)
pm1004vAlmTxBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasLowWarningPortn.setStatus("current")
_Pm1004vAlmTxBiasHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasHighWarningPortn_Object = MibTableColumn
pm1004vAlmTxBiasHighWarningPortn = _Pm1004vAlmTxBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 5),
    _Pm1004vAlmTxBiasHighWarningPortn_Type()
)
pm1004vAlmTxBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasHighWarningPortn.setStatus("current")
_Pm1004vAlmTempLowWarningPortn_Type = EkiOnOff
_Pm1004vAlmTempLowWarningPortn_Object = MibTableColumn
pm1004vAlmTempLowWarningPortn = _Pm1004vAlmTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 8),
    _Pm1004vAlmTempLowWarningPortn_Type()
)
pm1004vAlmTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempLowWarningPortn.setStatus("current")
_Pm1004vAlmTempHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmTempHighWarningPortn_Object = MibTableColumn
pm1004vAlmTempHighWarningPortn = _Pm1004vAlmTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 9),
    _Pm1004vAlmTempHighWarningPortn_Type()
)
pm1004vAlmTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempHighWarningPortn.setStatus("current")
_Pm1004vAlmRxPowerLowWarningPortn_Type = EkiOnOff
_Pm1004vAlmRxPowerLowWarningPortn_Object = MibTableColumn
pm1004vAlmRxPowerLowWarningPortn = _Pm1004vAlmRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 16),
    _Pm1004vAlmRxPowerLowWarningPortn_Type()
)
pm1004vAlmRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPowerLowWarningPortn.setStatus("current")
_Pm1004vAlmRxPowerHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmRxPowerHighWarningPortn_Object = MibTableColumn
pm1004vAlmRxPowerHighWarningPortn = _Pm1004vAlmRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 209, 1, 17),
    _Pm1004vAlmRxPowerHighWarningPortn_Type()
)
pm1004vAlmRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPowerHighWarningPortn.setStatus("current")
_Pm1004vAlmlineOtx1TlhWarningsTable_Object = MibTable
pm1004vAlmlineOtx1TlhWarningsTable = _Pm1004vAlmlineOtx1TlhWarningsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineOtx1TlhWarningsTable.setStatus("current")
_Pm1004vAlmlineOtx1TlhWarningsEntry_Object = MibTableRow
pm1004vAlmlineOtx1TlhWarningsEntry = _Pm1004vAlmlineOtx1TlhWarningsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225, 1)
)
pm1004vAlmlineOtx1TlhWarningsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineOtx1TlhWarningsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineOtx1TlhWarningsEntry.setStatus("current")


class _Pm1004vAlmlineOtx1TlhWarningsIndex_Type(Integer32):
    """Custom type pm1004vAlmlineOtx1TlhWarningsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineOtx1TlhWarningsIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineOtx1TlhWarningsIndex_Object = MibTableColumn
pm1004vAlmlineOtx1TlhWarningsIndex = _Pm1004vAlmlineOtx1TlhWarningsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225, 1, 1),
    _Pm1004vAlmlineOtx1TlhWarningsIndex_Type()
)
pm1004vAlmlineOtx1TlhWarningsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineOtx1TlhWarningsIndex.setStatus("current")
_Pm1004vAlmLineModulatorAgingHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmLineModulatorAgingHighWarningPortn_Object = MibTableColumn
pm1004vAlmLineModulatorAgingHighWarningPortn = _Pm1004vAlmLineModulatorAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225, 1, 6),
    _Pm1004vAlmLineModulatorAgingHighWarningPortn_Type()
)
pm1004vAlmLineModulatorAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineModulatorAgingHighWarningPortn.setStatus("current")
_Pm1004vAlmLineAgingHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmLineAgingHighWarningPortn_Object = MibTableColumn
pm1004vAlmLineAgingHighWarningPortn = _Pm1004vAlmLineAgingHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225, 1, 7),
    _Pm1004vAlmLineAgingHighWarningPortn_Type()
)
pm1004vAlmLineAgingHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineAgingHighWarningPortn.setStatus("current")
_Pm1004vAlmLineFreqDevHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmLineFreqDevHighWarningPortn_Object = MibTableColumn
pm1004vAlmLineFreqDevHighWarningPortn = _Pm1004vAlmLineFreqDevHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225, 1, 13),
    _Pm1004vAlmLineFreqDevHighWarningPortn_Type()
)
pm1004vAlmLineFreqDevHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineFreqDevHighWarningPortn.setStatus("current")
_Pm1004vAlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm1004vAlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm1004vAlmLineLaserTempHighWarningPortn = _Pm1004vAlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 1, 225, 1, 15),
    _Pm1004vAlmLineLaserTempHighWarningPortn_Type()
)
pm1004vAlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm1004vAlmLineUrg_ObjectIdentity = ObjectIdentity
pm1004vAlmLineUrg = _Pm1004vAlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2)
)
_Pm1004vAlmlineXfp1AlarmTable_Object = MibTable
pm1004vAlmlineXfp1AlarmTable = _Pm1004vAlmlineXfp1AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1AlarmTable.setStatus("current")
_Pm1004vAlmlineXfp1AlarmEntry_Object = MibTableRow
pm1004vAlmlineXfp1AlarmEntry = _Pm1004vAlmlineXfp1AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1)
)
pm1004vAlmlineXfp1AlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineXfp1AlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1AlarmEntry.setStatus("current")


class _Pm1004vAlmlineXfp1AlarmIndex_Type(Integer32):
    """Custom type pm1004vAlmlineXfp1AlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineXfp1AlarmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineXfp1AlarmIndex_Object = MibTableColumn
pm1004vAlmlineXfp1AlarmIndex = _Pm1004vAlmlineXfp1AlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 1),
    _Pm1004vAlmlineXfp1AlarmIndex_Type()
)
pm1004vAlmlineXfp1AlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1AlarmIndex.setStatus("current")
_Pm1004vAlmTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmTxPowerLowAlarmPortn_Object = MibTableColumn
pm1004vAlmTxPowerLowAlarmPortn = _Pm1004vAlmTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 2),
    _Pm1004vAlmTxPowerLowAlarmPortn_Type()
)
pm1004vAlmTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPowerLowAlarmPortn.setStatus("current")
_Pm1004vAlmTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmTxPowerHighAlarmPortn_Object = MibTableColumn
pm1004vAlmTxPowerHighAlarmPortn = _Pm1004vAlmTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 3),
    _Pm1004vAlmTxPowerHighAlarmPortn_Type()
)
pm1004vAlmTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPowerHighAlarmPortn.setStatus("current")
_Pm1004vAlmTxBiasLowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasLowAlarmPortn_Object = MibTableColumn
pm1004vAlmTxBiasLowAlarmPortn = _Pm1004vAlmTxBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 4),
    _Pm1004vAlmTxBiasLowAlarmPortn_Type()
)
pm1004vAlmTxBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasLowAlarmPortn.setStatus("current")
_Pm1004vAlmTxBiasHighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmTxBiasHighAlarmPortn_Object = MibTableColumn
pm1004vAlmTxBiasHighAlarmPortn = _Pm1004vAlmTxBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 5),
    _Pm1004vAlmTxBiasHighAlarmPortn_Type()
)
pm1004vAlmTxBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxBiasHighAlarmPortn.setStatus("current")
_Pm1004vAlmTempLowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmTempLowAlarmPortn_Object = MibTableColumn
pm1004vAlmTempLowAlarmPortn = _Pm1004vAlmTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 8),
    _Pm1004vAlmTempLowAlarmPortn_Type()
)
pm1004vAlmTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempLowAlarmPortn.setStatus("current")
_Pm1004vAlmTempHighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmTempHighAlarmPortn_Object = MibTableColumn
pm1004vAlmTempHighAlarmPortn = _Pm1004vAlmTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 9),
    _Pm1004vAlmTempHighAlarmPortn_Type()
)
pm1004vAlmTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTempHighAlarmPortn.setStatus("current")
_Pm1004vAlmRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmRxPowerLowAlarmPortn_Object = MibTableColumn
pm1004vAlmRxPowerLowAlarmPortn = _Pm1004vAlmRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 16),
    _Pm1004vAlmRxPowerLowAlarmPortn_Type()
)
pm1004vAlmRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPowerLowAlarmPortn.setStatus("current")
_Pm1004vAlmRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmRxPowerHighAlarmPortn_Object = MibTableColumn
pm1004vAlmRxPowerHighAlarmPortn = _Pm1004vAlmRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 208, 1, 17),
    _Pm1004vAlmRxPowerHighAlarmPortn_Type()
)
pm1004vAlmRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPowerHighAlarmPortn.setStatus("current")
_Pm1004vAlmlineXfp1CritTable_Object = MibTable
pm1004vAlmlineXfp1CritTable = _Pm1004vAlmlineXfp1CritTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1CritTable.setStatus("current")
_Pm1004vAlmlineXfp1CritEntry_Object = MibTableRow
pm1004vAlmlineXfp1CritEntry = _Pm1004vAlmlineXfp1CritEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210, 1)
)
pm1004vAlmlineXfp1CritEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineXfp1CritIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1CritEntry.setStatus("current")


class _Pm1004vAlmlineXfp1CritIndex_Type(Integer32):
    """Custom type pm1004vAlmlineXfp1CritIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineXfp1CritIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineXfp1CritIndex_Object = MibTableColumn
pm1004vAlmlineXfp1CritIndex = _Pm1004vAlmlineXfp1CritIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210, 1, 1),
    _Pm1004vAlmlineXfp1CritIndex_Type()
)
pm1004vAlmlineXfp1CritIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1CritIndex.setStatus("current")
_Pm1004vAlmTxPowerLowCritPortn_Type = EkiOnOff
_Pm1004vAlmTxPowerLowCritPortn_Object = MibTableColumn
pm1004vAlmTxPowerLowCritPortn = _Pm1004vAlmTxPowerLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210, 1, 2),
    _Pm1004vAlmTxPowerLowCritPortn_Type()
)
pm1004vAlmTxPowerLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPowerLowCritPortn.setStatus("current")
_Pm1004vAlmTxPowerHighCritPortn_Type = EkiOnOff
_Pm1004vAlmTxPowerHighCritPortn_Object = MibTableColumn
pm1004vAlmTxPowerHighCritPortn = _Pm1004vAlmTxPowerHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210, 1, 3),
    _Pm1004vAlmTxPowerHighCritPortn_Type()
)
pm1004vAlmTxPowerHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxPowerHighCritPortn.setStatus("current")
_Pm1004vAlmRxPowerLowCritPortn_Type = EkiOnOff
_Pm1004vAlmRxPowerLowCritPortn_Object = MibTableColumn
pm1004vAlmRxPowerLowCritPortn = _Pm1004vAlmRxPowerLowCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210, 1, 16),
    _Pm1004vAlmRxPowerLowCritPortn_Type()
)
pm1004vAlmRxPowerLowCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPowerLowCritPortn.setStatus("current")
_Pm1004vAlmRxPowerHighCritPortn_Type = EkiOnOff
_Pm1004vAlmRxPowerHighCritPortn_Object = MibTableColumn
pm1004vAlmRxPowerHighCritPortn = _Pm1004vAlmRxPowerHighCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 210, 1, 17),
    _Pm1004vAlmRxPowerHighCritPortn_Type()
)
pm1004vAlmRxPowerHighCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxPowerHighCritPortn.setStatus("current")
_Pm1004vAlmlineXfp1SupplyAlarmTable_Object = MibTable
pm1004vAlmlineXfp1SupplyAlarmTable = _Pm1004vAlmlineXfp1SupplyAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1SupplyAlarmTable.setStatus("current")
_Pm1004vAlmlineXfp1SupplyAlarmEntry_Object = MibTableRow
pm1004vAlmlineXfp1SupplyAlarmEntry = _Pm1004vAlmlineXfp1SupplyAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1)
)
pm1004vAlmlineXfp1SupplyAlarmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineXfp1SupplyAlarmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1SupplyAlarmEntry.setStatus("current")


class _Pm1004vAlmlineXfp1SupplyAlarmIndex_Type(Integer32):
    """Custom type pm1004vAlmlineXfp1SupplyAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineXfp1SupplyAlarmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineXfp1SupplyAlarmIndex_Object = MibTableColumn
pm1004vAlmlineXfp1SupplyAlarmIndex = _Pm1004vAlmlineXfp1SupplyAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 1),
    _Pm1004vAlmlineXfp1SupplyAlarmIndex_Type()
)
pm1004vAlmlineXfp1SupplyAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1SupplyAlarmIndex.setStatus("current")
_Pm1004vAlmVee5LowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVee5LowAlarmPortn_Object = MibTableColumn
pm1004vAlmVee5LowAlarmPortn = _Pm1004vAlmVee5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 2),
    _Pm1004vAlmVee5LowAlarmPortn_Type()
)
pm1004vAlmVee5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVee5LowAlarmPortn.setStatus("current")
_Pm1004vAlmVee5HighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVee5HighAlarmPortn_Object = MibTableColumn
pm1004vAlmVee5HighAlarmPortn = _Pm1004vAlmVee5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 3),
    _Pm1004vAlmVee5HighAlarmPortn_Type()
)
pm1004vAlmVee5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVee5HighAlarmPortn.setStatus("current")
_Pm1004vAlmVcc2LowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVcc2LowAlarmPortn_Object = MibTableColumn
pm1004vAlmVcc2LowAlarmPortn = _Pm1004vAlmVcc2LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 4),
    _Pm1004vAlmVcc2LowAlarmPortn_Type()
)
pm1004vAlmVcc2LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc2LowAlarmPortn.setStatus("current")
_Pm1004vAlmVcc2HighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVcc2HighAlarmPortn_Object = MibTableColumn
pm1004vAlmVcc2HighAlarmPortn = _Pm1004vAlmVcc2HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 5),
    _Pm1004vAlmVcc2HighAlarmPortn_Type()
)
pm1004vAlmVcc2HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc2HighAlarmPortn.setStatus("current")
_Pm1004vAlmVcc3LowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVcc3LowAlarmPortn_Object = MibTableColumn
pm1004vAlmVcc3LowAlarmPortn = _Pm1004vAlmVcc3LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 6),
    _Pm1004vAlmVcc3LowAlarmPortn_Type()
)
pm1004vAlmVcc3LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc3LowAlarmPortn.setStatus("current")
_Pm1004vAlmVcc3HighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVcc3HighAlarmPortn_Object = MibTableColumn
pm1004vAlmVcc3HighAlarmPortn = _Pm1004vAlmVcc3HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 7),
    _Pm1004vAlmVcc3HighAlarmPortn_Type()
)
pm1004vAlmVcc3HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc3HighAlarmPortn.setStatus("current")
_Pm1004vAlmVcc5LowAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVcc5LowAlarmPortn_Object = MibTableColumn
pm1004vAlmVcc5LowAlarmPortn = _Pm1004vAlmVcc5LowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 8),
    _Pm1004vAlmVcc5LowAlarmPortn_Type()
)
pm1004vAlmVcc5LowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc5LowAlarmPortn.setStatus("current")
_Pm1004vAlmVcc5HighAlarmPortn_Type = EkiOnOff
_Pm1004vAlmVcc5HighAlarmPortn_Object = MibTableColumn
pm1004vAlmVcc5HighAlarmPortn = _Pm1004vAlmVcc5HighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 9),
    _Pm1004vAlmVcc5HighAlarmPortn_Type()
)
pm1004vAlmVcc5HighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc5HighAlarmPortn.setStatus("current")
_Pm1004vAlmVee5LowWarningPortn_Type = EkiOnOff
_Pm1004vAlmVee5LowWarningPortn_Object = MibTableColumn
pm1004vAlmVee5LowWarningPortn = _Pm1004vAlmVee5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 10),
    _Pm1004vAlmVee5LowWarningPortn_Type()
)
pm1004vAlmVee5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVee5LowWarningPortn.setStatus("current")
_Pm1004vAlmVee5HighWarningPortn_Type = EkiOnOff
_Pm1004vAlmVee5HighWarningPortn_Object = MibTableColumn
pm1004vAlmVee5HighWarningPortn = _Pm1004vAlmVee5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 11),
    _Pm1004vAlmVee5HighWarningPortn_Type()
)
pm1004vAlmVee5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVee5HighWarningPortn.setStatus("current")
_Pm1004vAlmVcc2LowWarningPortn_Type = EkiOnOff
_Pm1004vAlmVcc2LowWarningPortn_Object = MibTableColumn
pm1004vAlmVcc2LowWarningPortn = _Pm1004vAlmVcc2LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 12),
    _Pm1004vAlmVcc2LowWarningPortn_Type()
)
pm1004vAlmVcc2LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc2LowWarningPortn.setStatus("current")
_Pm1004vAlmVcc2HighWarningPortn_Type = EkiOnOff
_Pm1004vAlmVcc2HighWarningPortn_Object = MibTableColumn
pm1004vAlmVcc2HighWarningPortn = _Pm1004vAlmVcc2HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 13),
    _Pm1004vAlmVcc2HighWarningPortn_Type()
)
pm1004vAlmVcc2HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc2HighWarningPortn.setStatus("current")
_Pm1004vAlmVcc3LowWarningPortn_Type = EkiOnOff
_Pm1004vAlmVcc3LowWarningPortn_Object = MibTableColumn
pm1004vAlmVcc3LowWarningPortn = _Pm1004vAlmVcc3LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 14),
    _Pm1004vAlmVcc3LowWarningPortn_Type()
)
pm1004vAlmVcc3LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc3LowWarningPortn.setStatus("current")
_Pm1004vAlmVcc3HighWarningPortn_Type = EkiOnOff
_Pm1004vAlmVcc3HighWarningPortn_Object = MibTableColumn
pm1004vAlmVcc3HighWarningPortn = _Pm1004vAlmVcc3HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 15),
    _Pm1004vAlmVcc3HighWarningPortn_Type()
)
pm1004vAlmVcc3HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc3HighWarningPortn.setStatus("current")
_Pm1004vAlmVcc5LowWarningPortn_Type = EkiOnOff
_Pm1004vAlmVcc5LowWarningPortn_Object = MibTableColumn
pm1004vAlmVcc5LowWarningPortn = _Pm1004vAlmVcc5LowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 16),
    _Pm1004vAlmVcc5LowWarningPortn_Type()
)
pm1004vAlmVcc5LowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc5LowWarningPortn.setStatus("current")
_Pm1004vAlmVcc5HighWarningPortn_Type = EkiOnOff
_Pm1004vAlmVcc5HighWarningPortn_Object = MibTableColumn
pm1004vAlmVcc5HighWarningPortn = _Pm1004vAlmVcc5HighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 212, 1, 17),
    _Pm1004vAlmVcc5HighWarningPortn_Type()
)
pm1004vAlmVcc5HighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmVcc5HighWarningPortn.setStatus("current")
_Pm1004vAlmlineOtx1TlhAlarmsTable_Object = MibTable
pm1004vAlmlineOtx1TlhAlarmsTable = _Pm1004vAlmlineOtx1TlhAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineOtx1TlhAlarmsTable.setStatus("current")
_Pm1004vAlmlineOtx1TlhAlarmsEntry_Object = MibTableRow
pm1004vAlmlineOtx1TlhAlarmsEntry = _Pm1004vAlmlineOtx1TlhAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224, 1)
)
pm1004vAlmlineOtx1TlhAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineOtx1TlhAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineOtx1TlhAlarmsEntry.setStatus("current")


class _Pm1004vAlmlineOtx1TlhAlarmsIndex_Type(Integer32):
    """Custom type pm1004vAlmlineOtx1TlhAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineOtx1TlhAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineOtx1TlhAlarmsIndex_Object = MibTableColumn
pm1004vAlmlineOtx1TlhAlarmsIndex = _Pm1004vAlmlineOtx1TlhAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224, 1, 1),
    _Pm1004vAlmlineOtx1TlhAlarmsIndex_Type()
)
pm1004vAlmlineOtx1TlhAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineOtx1TlhAlarmsIndex.setStatus("current")
_Pm1004vAlmLineModulatorAgingHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmLineModulatorAgingHighAlaPortn_Object = MibTableColumn
pm1004vAlmLineModulatorAgingHighAlaPortn = _Pm1004vAlmLineModulatorAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224, 1, 6),
    _Pm1004vAlmLineModulatorAgingHighAlaPortn_Type()
)
pm1004vAlmLineModulatorAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineModulatorAgingHighAlaPortn.setStatus("current")
_Pm1004vAlmLineAgingHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmLineAgingHighAlaPortn_Object = MibTableColumn
pm1004vAlmLineAgingHighAlaPortn = _Pm1004vAlmLineAgingHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224, 1, 7),
    _Pm1004vAlmLineAgingHighAlaPortn_Type()
)
pm1004vAlmLineAgingHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineAgingHighAlaPortn.setStatus("current")
_Pm1004vAlmLineFreqDevHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmLineFreqDevHighAlaPortn_Object = MibTableColumn
pm1004vAlmLineFreqDevHighAlaPortn = _Pm1004vAlmLineFreqDevHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224, 1, 13),
    _Pm1004vAlmLineFreqDevHighAlaPortn_Type()
)
pm1004vAlmLineFreqDevHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineFreqDevHighAlaPortn.setStatus("current")
_Pm1004vAlmLineLaserTempHighAlaPortn_Type = EkiOnOff
_Pm1004vAlmLineLaserTempHighAlaPortn_Object = MibTableColumn
pm1004vAlmLineLaserTempHighAlaPortn = _Pm1004vAlmLineLaserTempHighAlaPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 2, 224, 1, 15),
    _Pm1004vAlmLineLaserTempHighAlaPortn_Type()
)
pm1004vAlmLineLaserTempHighAlaPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineLaserTempHighAlaPortn.setStatus("current")
_Pm1004vAlmLineCrit_ObjectIdentity = ObjectIdentity
pm1004vAlmLineCrit = _Pm1004vAlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3)
)
_Pm1004vAlmsynthAlmLineTable_Object = MibTable
pm1004vAlmsynthAlmLineTable = _Pm1004vAlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7)
)
if mibBuilder.loadTexts:
    pm1004vAlmsynthAlmLineTable.setStatus("current")
_Pm1004vAlmsynthAlmLineEntry_Object = MibTableRow
pm1004vAlmsynthAlmLineEntry = _Pm1004vAlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1)
)
pm1004vAlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmsynthAlmLineEntry.setStatus("current")


class _Pm1004vAlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm1004vAlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm1004vAlmsynthAlmLineIndex_Object = MibTableColumn
pm1004vAlmsynthAlmLineIndex = _Pm1004vAlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 1),
    _Pm1004vAlmsynthAlmLineIndex_Type()
)
pm1004vAlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmsynthAlmLineIndex.setStatus("current")
_Pm1004vAlmXfpAbsentPortn_Type = EkiOnOff
_Pm1004vAlmXfpAbsentPortn_Object = MibTableColumn
pm1004vAlmXfpAbsentPortn = _Pm1004vAlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 2),
    _Pm1004vAlmXfpAbsentPortn_Type()
)
pm1004vAlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmXfpAbsentPortn.setStatus("current")
_Pm1004vAlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm1004vAlmXfpInitNotComplPortn_Object = MibTableColumn
pm1004vAlmXfpInitNotComplPortn = _Pm1004vAlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 3),
    _Pm1004vAlmXfpInitNotComplPortn_Type()
)
pm1004vAlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmXfpInitNotComplPortn.setStatus("current")
_Pm1004vAlmLineHwFailPortn_Type = EkiOnOff
_Pm1004vAlmLineHwFailPortn_Object = MibTableColumn
pm1004vAlmLineHwFailPortn = _Pm1004vAlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 5),
    _Pm1004vAlmLineHwFailPortn_Type()
)
pm1004vAlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineHwFailPortn.setStatus("current")
_Pm1004vAlmXfpTxOffPortn_Type = EkiOnOff
_Pm1004vAlmXfpTxOffPortn_Object = MibTableColumn
pm1004vAlmXfpTxOffPortn = _Pm1004vAlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 6),
    _Pm1004vAlmXfpTxOffPortn_Type()
)
pm1004vAlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmXfpTxOffPortn.setStatus("current")
_Pm1004vAlmLineLocalOosPortn_Type = EkiOnOff
_Pm1004vAlmLineLocalOosPortn_Object = MibTableColumn
pm1004vAlmLineLocalOosPortn = _Pm1004vAlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 7),
    _Pm1004vAlmLineLocalOosPortn_Type()
)
pm1004vAlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineLocalOosPortn.setStatus("current")
_Pm1004vAlmLineDdmWarningPortn_Type = EkiOnOff
_Pm1004vAlmLineDdmWarningPortn_Object = MibTableColumn
pm1004vAlmLineDdmWarningPortn = _Pm1004vAlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 10),
    _Pm1004vAlmLineDdmWarningPortn_Type()
)
pm1004vAlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineDdmWarningPortn.setStatus("current")
_Pm1004vAlmLineDdmAlmPortn_Type = EkiOnOff
_Pm1004vAlmLineDdmAlmPortn_Object = MibTableColumn
pm1004vAlmLineDdmAlmPortn = _Pm1004vAlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 11),
    _Pm1004vAlmLineDdmAlmPortn_Type()
)
pm1004vAlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineDdmAlmPortn.setStatus("current")
_Pm1004vAlmLineDdmCritPortn_Type = EkiOnOff
_Pm1004vAlmLineDdmCritPortn_Object = MibTableColumn
pm1004vAlmLineDdmCritPortn = _Pm1004vAlmLineDdmCritPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 12),
    _Pm1004vAlmLineDdmCritPortn_Type()
)
pm1004vAlmLineDdmCritPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineDdmCritPortn.setStatus("current")
_Pm1004vAlmLineFailPortn_Type = EkiOnOff
_Pm1004vAlmLineFailPortn_Object = MibTableColumn
pm1004vAlmLineFailPortn = _Pm1004vAlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 13),
    _Pm1004vAlmLineFailPortn_Type()
)
pm1004vAlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineFailPortn.setStatus("current")
_Pm1004vAlmLineActivePortn_Type = EkiOnOff
_Pm1004vAlmLineActivePortn_Object = MibTableColumn
pm1004vAlmLineActivePortn = _Pm1004vAlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 7, 1, 17),
    _Pm1004vAlmLineActivePortn_Type()
)
pm1004vAlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmLineActivePortn.setStatus("current")
_Pm1004vAlmdfrmAlmTable_Object = MibTable
pm1004vAlmdfrmAlmTable = _Pm1004vAlmdfrmAlmTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 128)
)
if mibBuilder.loadTexts:
    pm1004vAlmdfrmAlmTable.setStatus("current")
_Pm1004vAlmdfrmAlmEntry_Object = MibTableRow
pm1004vAlmdfrmAlmEntry = _Pm1004vAlmdfrmAlmEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 128, 1)
)
pm1004vAlmdfrmAlmEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmdfrmAlmIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmdfrmAlmEntry.setStatus("current")


class _Pm1004vAlmdfrmAlmIndex_Type(Integer32):
    """Custom type pm1004vAlmdfrmAlmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmdfrmAlmIndex_Type.__name__ = "Integer32"
_Pm1004vAlmdfrmAlmIndex_Object = MibTableColumn
pm1004vAlmdfrmAlmIndex = _Pm1004vAlmdfrmAlmIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 128, 1, 1),
    _Pm1004vAlmdfrmAlmIndex_Type()
)
pm1004vAlmdfrmAlmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmdfrmAlmIndex.setStatus("current")
_Pm1004vAlmDwLossofsyncPortn_Type = EkiOnOff
_Pm1004vAlmDwLossofsyncPortn_Object = MibTableColumn
pm1004vAlmDwLossofsyncPortn = _Pm1004vAlmDwLossofsyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 128, 1, 5),
    _Pm1004vAlmDwLossofsyncPortn_Type()
)
pm1004vAlmDwLossofsyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwLossofsyncPortn.setStatus("current")
_Pm1004vAlmlineSyncAlarmsTable_Object = MibTable
pm1004vAlmlineSyncAlarmsTable = _Pm1004vAlmlineSyncAlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 133)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineSyncAlarmsTable.setStatus("current")
_Pm1004vAlmlineSyncAlarmsEntry_Object = MibTableRow
pm1004vAlmlineSyncAlarmsEntry = _Pm1004vAlmlineSyncAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 133, 1)
)
pm1004vAlmlineSyncAlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineSyncAlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineSyncAlarmsEntry.setStatus("current")


class _Pm1004vAlmlineSyncAlarmsIndex_Type(Integer32):
    """Custom type pm1004vAlmlineSyncAlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineSyncAlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineSyncAlarmsIndex_Object = MibTableColumn
pm1004vAlmlineSyncAlarmsIndex = _Pm1004vAlmlineSyncAlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 133, 1, 1),
    _Pm1004vAlmlineSyncAlarmsIndex_Type()
)
pm1004vAlmlineSyncAlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineSyncAlarmsIndex.setStatus("current")
_Pm1004vAlmDwLockerrPortn_Type = EkiOnOff
_Pm1004vAlmDwLockerrPortn_Object = MibTableColumn
pm1004vAlmDwLockerrPortn = _Pm1004vAlmDwLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 133, 1, 13),
    _Pm1004vAlmDwLockerrPortn_Type()
)
pm1004vAlmDwLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwLockerrPortn.setStatus("current")
_Pm1004vAlmUpLockerrPortn_Type = EkiOnOff
_Pm1004vAlmUpLockerrPortn_Object = MibTableColumn
pm1004vAlmUpLockerrPortn = _Pm1004vAlmUpLockerrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 133, 1, 14),
    _Pm1004vAlmUpLockerrPortn_Type()
)
pm1004vAlmUpLockerrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmUpLockerrPortn.setStatus("current")
_Pm1004vAlmDwLosPortn_Type = EkiOnOff
_Pm1004vAlmDwLosPortn_Object = MibTableColumn
pm1004vAlmDwLosPortn = _Pm1004vAlmDwLosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 133, 1, 17),
    _Pm1004vAlmDwLosPortn_Type()
)
pm1004vAlmDwLosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmDwLosPortn.setStatus("current")
_Pm1004vAlmlineXfp1AlarmsTable_Object = MibTable
pm1004vAlmlineXfp1AlarmsTable = _Pm1004vAlmlineXfp1AlarmsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1AlarmsTable.setStatus("current")
_Pm1004vAlmlineXfp1AlarmsEntry_Object = MibTableRow
pm1004vAlmlineXfp1AlarmsEntry = _Pm1004vAlmlineXfp1AlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1)
)
pm1004vAlmlineXfp1AlarmsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vAlmlineXfp1AlarmsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1AlarmsEntry.setStatus("current")


class _Pm1004vAlmlineXfp1AlarmsIndex_Type(Integer32):
    """Custom type pm1004vAlmlineXfp1AlarmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vAlmlineXfp1AlarmsIndex_Type.__name__ = "Integer32"
_Pm1004vAlmlineXfp1AlarmsIndex_Object = MibTableColumn
pm1004vAlmlineXfp1AlarmsIndex = _Pm1004vAlmlineXfp1AlarmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 1),
    _Pm1004vAlmlineXfp1AlarmsIndex_Type()
)
pm1004vAlmlineXfp1AlarmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmlineXfp1AlarmsIndex.setStatus("current")
_Pm1004vAlmModNrPortn_Type = EkiOnOff
_Pm1004vAlmModNrPortn_Object = MibTableColumn
pm1004vAlmModNrPortn = _Pm1004vAlmModNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 3),
    _Pm1004vAlmModNrPortn_Type()
)
pm1004vAlmModNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmModNrPortn.setStatus("current")
_Pm1004vAlmRxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004vAlmRxCdrNotLockedPortn_Object = MibTableColumn
pm1004vAlmRxCdrNotLockedPortn = _Pm1004vAlmRxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 4),
    _Pm1004vAlmRxCdrNotLockedPortn_Type()
)
pm1004vAlmRxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxCdrNotLockedPortn.setStatus("current")
_Pm1004vAlmRxNrPortn_Type = EkiOnOff
_Pm1004vAlmRxNrPortn_Object = MibTableColumn
pm1004vAlmRxNrPortn = _Pm1004vAlmRxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 6),
    _Pm1004vAlmRxNrPortn_Type()
)
pm1004vAlmRxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmRxNrPortn.setStatus("current")
_Pm1004vAlmTxCdrNotLockedPortn_Type = EkiOnOff
_Pm1004vAlmTxCdrNotLockedPortn_Object = MibTableColumn
pm1004vAlmTxCdrNotLockedPortn = _Pm1004vAlmTxCdrNotLockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 7),
    _Pm1004vAlmTxCdrNotLockedPortn_Type()
)
pm1004vAlmTxCdrNotLockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxCdrNotLockedPortn.setStatus("current")
_Pm1004vAlmTxFaultPortn_Type = EkiOnOff
_Pm1004vAlmTxFaultPortn_Object = MibTableColumn
pm1004vAlmTxFaultPortn = _Pm1004vAlmTxFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 8),
    _Pm1004vAlmTxFaultPortn_Type()
)
pm1004vAlmTxFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxFaultPortn.setStatus("current")
_Pm1004vAlmTxNrPortn_Type = EkiOnOff
_Pm1004vAlmTxNrPortn_Object = MibTableColumn
pm1004vAlmTxNrPortn = _Pm1004vAlmTxNrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 9),
    _Pm1004vAlmTxNrPortn_Type()
)
pm1004vAlmTxNrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTxNrPortn.setStatus("current")
_Pm1004vAlmWavelengthUnlockedPortn_Type = EkiOnOff
_Pm1004vAlmWavelengthUnlockedPortn_Object = MibTableColumn
pm1004vAlmWavelengthUnlockedPortn = _Pm1004vAlmWavelengthUnlockedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 15),
    _Pm1004vAlmWavelengthUnlockedPortn_Type()
)
pm1004vAlmWavelengthUnlockedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmWavelengthUnlockedPortn.setStatus("current")
_Pm1004vAlmTecFaultPortn_Type = EkiOnOff
_Pm1004vAlmTecFaultPortn_Object = MibTableColumn
pm1004vAlmTecFaultPortn = _Pm1004vAlmTecFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 16),
    _Pm1004vAlmTecFaultPortn_Type()
)
pm1004vAlmTecFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmTecFaultPortn.setStatus("current")
_Pm1004vAlmApdSupplyFaultPortn_Type = EkiOnOff
_Pm1004vAlmApdSupplyFaultPortn_Object = MibTableColumn
pm1004vAlmApdSupplyFaultPortn = _Pm1004vAlmApdSupplyFaultPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 2, 3, 3, 211, 1, 17),
    _Pm1004vAlmApdSupplyFaultPortn_Type()
)
pm1004vAlmApdSupplyFaultPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vAlmApdSupplyFaultPortn.setStatus("current")
_Pm1004vmeasures_ObjectIdentity = ObjectIdentity
pm1004vmeasures = _Pm1004vmeasures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3)
)
_Pm1004vMesrOther_ObjectIdentity = ObjectIdentity
pm1004vMesrOther = _Pm1004vMesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 1)
)
_Pm1004vMesrsynth0_Type = EkiMeasureType
_Pm1004vMesrsynth0_Object = MibScalar
pm1004vMesrsynth0 = _Pm1004vMesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 1, 0),
    _Pm1004vMesrsynth0_Type()
)
pm1004vMesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrsynth0.setStatus("deprecated")
_Pm1004vMesrsynth1_Type = EkiMeasureType
_Pm1004vMesrsynth1_Object = MibScalar
pm1004vMesrsynth1 = _Pm1004vMesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 1, 1),
    _Pm1004vMesrsynth1_Type()
)
pm1004vMesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrsynth1.setStatus("deprecated")
_Pm1004vMesrClient_ObjectIdentity = ObjectIdentity
pm1004vMesrClient = _Pm1004vMesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2)
)
_Pm1004vMesrtempMeasTable_Object = MibTable
pm1004vMesrtempMeasTable = _Pm1004vMesrtempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004vMesrtempMeasTable.setStatus("current")
_Pm1004vMesrtempMeasEntry_Object = MibTableRow
pm1004vMesrtempMeasEntry = _Pm1004vMesrtempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 16, 1)
)
pm1004vMesrtempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrtempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrtempMeasEntry.setStatus("current")


class _Pm1004vMesrtempMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrtempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrtempMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrtempMeasIndex_Object = MibTableColumn
pm1004vMesrtempMeasIndex = _Pm1004vMesrtempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 16, 1, 1),
    _Pm1004vMesrtempMeasIndex_Type()
)
pm1004vMesrtempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrtempMeasIndex.setStatus("current")


class _Pm1004vMesrtempMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrtempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrtempMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrtempMeasPortn_Object = MibTableColumn
pm1004vMesrtempMeasPortn = _Pm1004vMesrtempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 16, 1, 2),
    _Pm1004vMesrtempMeasPortn_Type()
)
pm1004vMesrtempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrtempMeasPortn.setStatus("current")
_Pm1004vMesrvoltMeasTable_Object = MibTable
pm1004vMesrvoltMeasTable = _Pm1004vMesrvoltMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 24)
)
if mibBuilder.loadTexts:
    pm1004vMesrvoltMeasTable.setStatus("current")
_Pm1004vMesrvoltMeasEntry_Object = MibTableRow
pm1004vMesrvoltMeasEntry = _Pm1004vMesrvoltMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 24, 1)
)
pm1004vMesrvoltMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrvoltMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrvoltMeasEntry.setStatus("current")


class _Pm1004vMesrvoltMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrvoltMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrvoltMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrvoltMeasIndex_Object = MibTableColumn
pm1004vMesrvoltMeasIndex = _Pm1004vMesrvoltMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 24, 1, 1),
    _Pm1004vMesrvoltMeasIndex_Type()
)
pm1004vMesrvoltMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrvoltMeasIndex.setStatus("current")


class _Pm1004vMesrvoltMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrvoltMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrvoltMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrvoltMeasPortn_Object = MibTableColumn
pm1004vMesrvoltMeasPortn = _Pm1004vMesrvoltMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 24, 1, 2),
    _Pm1004vMesrvoltMeasPortn_Type()
)
pm1004vMesrvoltMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrvoltMeasPortn.setStatus("current")
_Pm1004vMesrbiasMeasTable_Object = MibTable
pm1004vMesrbiasMeasTable = _Pm1004vMesrbiasMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 32)
)
if mibBuilder.loadTexts:
    pm1004vMesrbiasMeasTable.setStatus("current")
_Pm1004vMesrbiasMeasEntry_Object = MibTableRow
pm1004vMesrbiasMeasEntry = _Pm1004vMesrbiasMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 32, 1)
)
pm1004vMesrbiasMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrbiasMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrbiasMeasEntry.setStatus("current")


class _Pm1004vMesrbiasMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrbiasMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrbiasMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrbiasMeasIndex_Object = MibTableColumn
pm1004vMesrbiasMeasIndex = _Pm1004vMesrbiasMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 32, 1, 1),
    _Pm1004vMesrbiasMeasIndex_Type()
)
pm1004vMesrbiasMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrbiasMeasIndex.setStatus("current")


class _Pm1004vMesrbiasMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrbiasMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrbiasMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrbiasMeasPortn_Object = MibTableColumn
pm1004vMesrbiasMeasPortn = _Pm1004vMesrbiasMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 32, 1, 2),
    _Pm1004vMesrbiasMeasPortn_Type()
)
pm1004vMesrbiasMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrbiasMeasPortn.setStatus("current")
_Pm1004vMesrtxpwrMeasTable_Object = MibTable
pm1004vMesrtxpwrMeasTable = _Pm1004vMesrtxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 40)
)
if mibBuilder.loadTexts:
    pm1004vMesrtxpwrMeasTable.setStatus("current")
_Pm1004vMesrtxpwrMeasEntry_Object = MibTableRow
pm1004vMesrtxpwrMeasEntry = _Pm1004vMesrtxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 40, 1)
)
pm1004vMesrtxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrtxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrtxpwrMeasEntry.setStatus("current")


class _Pm1004vMesrtxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrtxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrtxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrtxpwrMeasIndex_Object = MibTableColumn
pm1004vMesrtxpwrMeasIndex = _Pm1004vMesrtxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 40, 1, 1),
    _Pm1004vMesrtxpwrMeasIndex_Type()
)
pm1004vMesrtxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrtxpwrMeasIndex.setStatus("current")


class _Pm1004vMesrtxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrtxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrtxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrtxpwrMeasPortn_Object = MibTableColumn
pm1004vMesrtxpwrMeasPortn = _Pm1004vMesrtxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 40, 1, 2),
    _Pm1004vMesrtxpwrMeasPortn_Type()
)
pm1004vMesrtxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrtxpwrMeasPortn.setStatus("current")
_Pm1004vMesrrxpwrMeasTable_Object = MibTable
pm1004vMesrrxpwrMeasTable = _Pm1004vMesrrxpwrMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm1004vMesrrxpwrMeasTable.setStatus("current")
_Pm1004vMesrrxpwrMeasEntry_Object = MibTableRow
pm1004vMesrrxpwrMeasEntry = _Pm1004vMesrrxpwrMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 48, 1)
)
pm1004vMesrrxpwrMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrrxpwrMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrrxpwrMeasEntry.setStatus("current")


class _Pm1004vMesrrxpwrMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrrxpwrMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrrxpwrMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrrxpwrMeasIndex_Object = MibTableColumn
pm1004vMesrrxpwrMeasIndex = _Pm1004vMesrrxpwrMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 48, 1, 1),
    _Pm1004vMesrrxpwrMeasIndex_Type()
)
pm1004vMesrrxpwrMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrrxpwrMeasIndex.setStatus("current")


class _Pm1004vMesrrxpwrMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrrxpwrMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrrxpwrMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrrxpwrMeasPortn_Object = MibTableColumn
pm1004vMesrrxpwrMeasPortn = _Pm1004vMesrrxpwrMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 2, 48, 1, 2),
    _Pm1004vMesrrxpwrMeasPortn_Type()
)
pm1004vMesrrxpwrMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrrxpwrMeasPortn.setStatus("current")
_Pm1004vMesrLine_ObjectIdentity = ObjectIdentity
pm1004vMesrLine = _Pm1004vMesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3)
)
_Pm1004vMesrxfp1LxModTempMeasTable_Object = MibTable
pm1004vMesrxfp1LxModTempMeasTable = _Pm1004vMesrxfp1LxModTempMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxModTempMeasTable.setStatus("current")
_Pm1004vMesrxfp1LxModTempMeasEntry_Object = MibTableRow
pm1004vMesrxfp1LxModTempMeasEntry = _Pm1004vMesrxfp1LxModTempMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 208, 1)
)
pm1004vMesrxfp1LxModTempMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1LxModTempMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxModTempMeasEntry.setStatus("current")


class _Pm1004vMesrxfp1LxModTempMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1LxModTempMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1LxModTempMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LxModTempMeasIndex_Object = MibTableColumn
pm1004vMesrxfp1LxModTempMeasIndex = _Pm1004vMesrxfp1LxModTempMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 208, 1, 1),
    _Pm1004vMesrxfp1LxModTempMeasIndex_Type()
)
pm1004vMesrxfp1LxModTempMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxModTempMeasIndex.setStatus("current")


class _Pm1004vMesrxfp1LxModTempMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1LxModTempMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1LxModTempMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LxModTempMeasPortn_Object = MibTableColumn
pm1004vMesrxfp1LxModTempMeasPortn = _Pm1004vMesrxfp1LxModTempMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 208, 1, 2),
    _Pm1004vMesrxfp1LxModTempMeasPortn_Type()
)
pm1004vMesrxfp1LxModTempMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxModTempMeasPortn.setStatus("current")
_Pm1004vMesrxfp1ReservedTable_Object = MibTable
pm1004vMesrxfp1ReservedTable = _Pm1004vMesrxfp1ReservedTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1ReservedTable.setStatus("deprecated")
_Pm1004vMesrxfp1ReservedEntry_Object = MibTableRow
pm1004vMesrxfp1ReservedEntry = _Pm1004vMesrxfp1ReservedEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 209, 1)
)
pm1004vMesrxfp1ReservedEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1ReservedIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1ReservedEntry.setStatus("deprecated")


class _Pm1004vMesrxfp1ReservedIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1ReservedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1ReservedIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1ReservedIndex_Object = MibTableColumn
pm1004vMesrxfp1ReservedIndex = _Pm1004vMesrxfp1ReservedIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 209, 1, 1),
    _Pm1004vMesrxfp1ReservedIndex_Type()
)
pm1004vMesrxfp1ReservedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1ReservedIndex.setStatus("deprecated")


class _Pm1004vMesrxfp1ReservedPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1ReservedPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1ReservedPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1ReservedPortn_Object = MibTableColumn
pm1004vMesrxfp1ReservedPortn = _Pm1004vMesrxfp1ReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 209, 1, 2),
    _Pm1004vMesrxfp1ReservedPortn_Type()
)
pm1004vMesrxfp1ReservedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1ReservedPortn.setStatus("deprecated")
_Pm1004vMesrxfp1LoBiasCurrentMeasTable_Object = MibTable
pm1004vMesrxfp1LoBiasCurrentMeasTable = _Pm1004vMesrxfp1LoBiasCurrentMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoBiasCurrentMeasTable.setStatus("current")
_Pm1004vMesrxfp1LoBiasCurrentMeasEntry_Object = MibTableRow
pm1004vMesrxfp1LoBiasCurrentMeasEntry = _Pm1004vMesrxfp1LoBiasCurrentMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 210, 1)
)
pm1004vMesrxfp1LoBiasCurrentMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1LoBiasCurrentMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoBiasCurrentMeasEntry.setStatus("current")


class _Pm1004vMesrxfp1LoBiasCurrentMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1LoBiasCurrentMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1LoBiasCurrentMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LoBiasCurrentMeasIndex_Object = MibTableColumn
pm1004vMesrxfp1LoBiasCurrentMeasIndex = _Pm1004vMesrxfp1LoBiasCurrentMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 210, 1, 1),
    _Pm1004vMesrxfp1LoBiasCurrentMeasIndex_Type()
)
pm1004vMesrxfp1LoBiasCurrentMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoBiasCurrentMeasIndex.setStatus("current")


class _Pm1004vMesrxfp1LoBiasCurrentMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1LoBiasCurrentMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1LoBiasCurrentMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LoBiasCurrentMeasPortn_Object = MibTableColumn
pm1004vMesrxfp1LoBiasCurrentMeasPortn = _Pm1004vMesrxfp1LoBiasCurrentMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 210, 1, 2),
    _Pm1004vMesrxfp1LoBiasCurrentMeasPortn_Type()
)
pm1004vMesrxfp1LoBiasCurrentMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoBiasCurrentMeasPortn.setStatus("current")
_Pm1004vMesrxfp1LoTxPowerMeasTable_Object = MibTable
pm1004vMesrxfp1LoTxPowerMeasTable = _Pm1004vMesrxfp1LoTxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 211)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoTxPowerMeasTable.setStatus("current")
_Pm1004vMesrxfp1LoTxPowerMeasEntry_Object = MibTableRow
pm1004vMesrxfp1LoTxPowerMeasEntry = _Pm1004vMesrxfp1LoTxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 211, 1)
)
pm1004vMesrxfp1LoTxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1LoTxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoTxPowerMeasEntry.setStatus("current")


class _Pm1004vMesrxfp1LoTxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1LoTxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1LoTxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LoTxPowerMeasIndex_Object = MibTableColumn
pm1004vMesrxfp1LoTxPowerMeasIndex = _Pm1004vMesrxfp1LoTxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 211, 1, 1),
    _Pm1004vMesrxfp1LoTxPowerMeasIndex_Type()
)
pm1004vMesrxfp1LoTxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoTxPowerMeasIndex.setStatus("current")


class _Pm1004vMesrxfp1LoTxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1LoTxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1LoTxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LoTxPowerMeasPortn_Object = MibTableColumn
pm1004vMesrxfp1LoTxPowerMeasPortn = _Pm1004vMesrxfp1LoTxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 211, 1, 2),
    _Pm1004vMesrxfp1LoTxPowerMeasPortn_Type()
)
pm1004vMesrxfp1LoTxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LoTxPowerMeasPortn.setStatus("current")
_Pm1004vMesrxfp1LiRxPowerMeasTable_Object = MibTable
pm1004vMesrxfp1LiRxPowerMeasTable = _Pm1004vMesrxfp1LiRxPowerMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 212)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LiRxPowerMeasTable.setStatus("current")
_Pm1004vMesrxfp1LiRxPowerMeasEntry_Object = MibTableRow
pm1004vMesrxfp1LiRxPowerMeasEntry = _Pm1004vMesrxfp1LiRxPowerMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 212, 1)
)
pm1004vMesrxfp1LiRxPowerMeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1LiRxPowerMeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LiRxPowerMeasEntry.setStatus("current")


class _Pm1004vMesrxfp1LiRxPowerMeasIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1LiRxPowerMeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1LiRxPowerMeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LiRxPowerMeasIndex_Object = MibTableColumn
pm1004vMesrxfp1LiRxPowerMeasIndex = _Pm1004vMesrxfp1LiRxPowerMeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 212, 1, 1),
    _Pm1004vMesrxfp1LiRxPowerMeasIndex_Type()
)
pm1004vMesrxfp1LiRxPowerMeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LiRxPowerMeasIndex.setStatus("current")


class _Pm1004vMesrxfp1LiRxPowerMeasPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1LiRxPowerMeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1LiRxPowerMeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LiRxPowerMeasPortn_Object = MibTableColumn
pm1004vMesrxfp1LiRxPowerMeasPortn = _Pm1004vMesrxfp1LiRxPowerMeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 212, 1, 2),
    _Pm1004vMesrxfp1LiRxPowerMeasPortn_Type()
)
pm1004vMesrxfp1LiRxPowerMeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LiRxPowerMeasPortn.setStatus("current")
_Pm1004vMesrxfp1LxAux1MeasTable_Object = MibTable
pm1004vMesrxfp1LxAux1MeasTable = _Pm1004vMesrxfp1LxAux1MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 213)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux1MeasTable.setStatus("deprecated")
_Pm1004vMesrxfp1LxAux1MeasEntry_Object = MibTableRow
pm1004vMesrxfp1LxAux1MeasEntry = _Pm1004vMesrxfp1LxAux1MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 213, 1)
)
pm1004vMesrxfp1LxAux1MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1LxAux1MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux1MeasEntry.setStatus("deprecated")


class _Pm1004vMesrxfp1LxAux1MeasIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1LxAux1MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1LxAux1MeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LxAux1MeasIndex_Object = MibTableColumn
pm1004vMesrxfp1LxAux1MeasIndex = _Pm1004vMesrxfp1LxAux1MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 213, 1, 1),
    _Pm1004vMesrxfp1LxAux1MeasIndex_Type()
)
pm1004vMesrxfp1LxAux1MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux1MeasIndex.setStatus("deprecated")


class _Pm1004vMesrxfp1LxAux1MeasPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1LxAux1MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1LxAux1MeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LxAux1MeasPortn_Object = MibTableColumn
pm1004vMesrxfp1LxAux1MeasPortn = _Pm1004vMesrxfp1LxAux1MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 213, 1, 2),
    _Pm1004vMesrxfp1LxAux1MeasPortn_Type()
)
pm1004vMesrxfp1LxAux1MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux1MeasPortn.setStatus("deprecated")
_Pm1004vMesrxfp1LxAux2MeasTable_Object = MibTable
pm1004vMesrxfp1LxAux2MeasTable = _Pm1004vMesrxfp1LxAux2MeasTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 214)
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux2MeasTable.setStatus("deprecated")
_Pm1004vMesrxfp1LxAux2MeasEntry_Object = MibTableRow
pm1004vMesrxfp1LxAux2MeasEntry = _Pm1004vMesrxfp1LxAux2MeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 214, 1)
)
pm1004vMesrxfp1LxAux2MeasEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrxfp1LxAux2MeasIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux2MeasEntry.setStatus("deprecated")


class _Pm1004vMesrxfp1LxAux2MeasIndex_Type(Integer32):
    """Custom type pm1004vMesrxfp1LxAux2MeasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrxfp1LxAux2MeasIndex_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LxAux2MeasIndex_Object = MibTableColumn
pm1004vMesrxfp1LxAux2MeasIndex = _Pm1004vMesrxfp1LxAux2MeasIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 214, 1, 1),
    _Pm1004vMesrxfp1LxAux2MeasIndex_Type()
)
pm1004vMesrxfp1LxAux2MeasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux2MeasIndex.setStatus("deprecated")


class _Pm1004vMesrxfp1LxAux2MeasPortn_Type(Integer32):
    """Custom type pm1004vMesrxfp1LxAux2MeasPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrxfp1LxAux2MeasPortn_Type.__name__ = "Integer32"
_Pm1004vMesrxfp1LxAux2MeasPortn_Object = MibTableColumn
pm1004vMesrxfp1LxAux2MeasPortn = _Pm1004vMesrxfp1LxAux2MeasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 214, 1, 2),
    _Pm1004vMesrxfp1LxAux2MeasPortn_Type()
)
pm1004vMesrxfp1LxAux2MeasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrxfp1LxAux2MeasPortn.setStatus("deprecated")
_Pm1004vMesrotx1AgingTable_Object = MibTable
pm1004vMesrotx1AgingTable = _Pm1004vMesrotx1AgingTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 224)
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1AgingTable.setStatus("current")
_Pm1004vMesrotx1AgingEntry_Object = MibTableRow
pm1004vMesrotx1AgingEntry = _Pm1004vMesrotx1AgingEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 224, 1)
)
pm1004vMesrotx1AgingEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrotx1AgingIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1AgingEntry.setStatus("current")


class _Pm1004vMesrotx1AgingIndex_Type(Integer32):
    """Custom type pm1004vMesrotx1AgingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrotx1AgingIndex_Type.__name__ = "Integer32"
_Pm1004vMesrotx1AgingIndex_Object = MibTableColumn
pm1004vMesrotx1AgingIndex = _Pm1004vMesrotx1AgingIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 224, 1, 1),
    _Pm1004vMesrotx1AgingIndex_Type()
)
pm1004vMesrotx1AgingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1AgingIndex.setStatus("current")


class _Pm1004vMesrotx1AgingPortn_Type(Integer32):
    """Custom type pm1004vMesrotx1AgingPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrotx1AgingPortn_Type.__name__ = "Integer32"
_Pm1004vMesrotx1AgingPortn_Object = MibTableColumn
pm1004vMesrotx1AgingPortn = _Pm1004vMesrotx1AgingPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 224, 1, 2),
    _Pm1004vMesrotx1AgingPortn_Type()
)
pm1004vMesrotx1AgingPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1AgingPortn.setStatus("current")
_Pm1004vMesrotx1LaserTemperatureTable_Object = MibTable
pm1004vMesrotx1LaserTemperatureTable = _Pm1004vMesrotx1LaserTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 225)
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserTemperatureTable.setStatus("deprecated")
_Pm1004vMesrotx1LaserTemperatureEntry_Object = MibTableRow
pm1004vMesrotx1LaserTemperatureEntry = _Pm1004vMesrotx1LaserTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 225, 1)
)
pm1004vMesrotx1LaserTemperatureEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrotx1LaserTemperatureIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserTemperatureEntry.setStatus("deprecated")


class _Pm1004vMesrotx1LaserTemperatureIndex_Type(Integer32):
    """Custom type pm1004vMesrotx1LaserTemperatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrotx1LaserTemperatureIndex_Type.__name__ = "Integer32"
_Pm1004vMesrotx1LaserTemperatureIndex_Object = MibTableColumn
pm1004vMesrotx1LaserTemperatureIndex = _Pm1004vMesrotx1LaserTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 225, 1, 1),
    _Pm1004vMesrotx1LaserTemperatureIndex_Type()
)
pm1004vMesrotx1LaserTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserTemperatureIndex.setStatus("deprecated")


class _Pm1004vMesrotx1LaserTemperaturePortn_Type(Integer32):
    """Custom type pm1004vMesrotx1LaserTemperaturePortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrotx1LaserTemperaturePortn_Type.__name__ = "Integer32"
_Pm1004vMesrotx1LaserTemperaturePortn_Object = MibTableColumn
pm1004vMesrotx1LaserTemperaturePortn = _Pm1004vMesrotx1LaserTemperaturePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 225, 1, 2),
    _Pm1004vMesrotx1LaserTemperaturePortn_Type()
)
pm1004vMesrotx1LaserTemperaturePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserTemperaturePortn.setStatus("deprecated")
_Pm1004vMesrotx1FreqDeviationTable_Object = MibTable
pm1004vMesrotx1FreqDeviationTable = _Pm1004vMesrotx1FreqDeviationTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 226)
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1FreqDeviationTable.setStatus("current")
_Pm1004vMesrotx1FreqDeviationEntry_Object = MibTableRow
pm1004vMesrotx1FreqDeviationEntry = _Pm1004vMesrotx1FreqDeviationEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 226, 1)
)
pm1004vMesrotx1FreqDeviationEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrotx1FreqDeviationIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1FreqDeviationEntry.setStatus("current")


class _Pm1004vMesrotx1FreqDeviationIndex_Type(Integer32):
    """Custom type pm1004vMesrotx1FreqDeviationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrotx1FreqDeviationIndex_Type.__name__ = "Integer32"
_Pm1004vMesrotx1FreqDeviationIndex_Object = MibTableColumn
pm1004vMesrotx1FreqDeviationIndex = _Pm1004vMesrotx1FreqDeviationIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 226, 1, 1),
    _Pm1004vMesrotx1FreqDeviationIndex_Type()
)
pm1004vMesrotx1FreqDeviationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1FreqDeviationIndex.setStatus("current")


class _Pm1004vMesrotx1FreqDeviationPortn_Type(Integer32):
    """Custom type pm1004vMesrotx1FreqDeviationPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrotx1FreqDeviationPortn_Type.__name__ = "Integer32"
_Pm1004vMesrotx1FreqDeviationPortn_Object = MibTableColumn
pm1004vMesrotx1FreqDeviationPortn = _Pm1004vMesrotx1FreqDeviationPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 226, 1, 2),
    _Pm1004vMesrotx1FreqDeviationPortn_Type()
)
pm1004vMesrotx1FreqDeviationPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1FreqDeviationPortn.setStatus("current")
_Pm1004vMesrotx1LaserWvlengthTable_Object = MibTable
pm1004vMesrotx1LaserWvlengthTable = _Pm1004vMesrotx1LaserWvlengthTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 227)
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserWvlengthTable.setStatus("current")
_Pm1004vMesrotx1LaserWvlengthEntry_Object = MibTableRow
pm1004vMesrotx1LaserWvlengthEntry = _Pm1004vMesrotx1LaserWvlengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 227, 1)
)
pm1004vMesrotx1LaserWvlengthEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMesrotx1LaserWvlengthIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserWvlengthEntry.setStatus("current")


class _Pm1004vMesrotx1LaserWvlengthIndex_Type(Integer32):
    """Custom type pm1004vMesrotx1LaserWvlengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMesrotx1LaserWvlengthIndex_Type.__name__ = "Integer32"
_Pm1004vMesrotx1LaserWvlengthIndex_Object = MibTableColumn
pm1004vMesrotx1LaserWvlengthIndex = _Pm1004vMesrotx1LaserWvlengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 227, 1, 1),
    _Pm1004vMesrotx1LaserWvlengthIndex_Type()
)
pm1004vMesrotx1LaserWvlengthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserWvlengthIndex.setStatus("current")


class _Pm1004vMesrotx1LaserWvlengthPortn_Type(Integer32):
    """Custom type pm1004vMesrotx1LaserWvlengthPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm1004vMesrotx1LaserWvlengthPortn_Type.__name__ = "Integer32"
_Pm1004vMesrotx1LaserWvlengthPortn_Object = MibTableColumn
pm1004vMesrotx1LaserWvlengthPortn = _Pm1004vMesrotx1LaserWvlengthPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 3, 3, 227, 1, 2),
    _Pm1004vMesrotx1LaserWvlengthPortn_Type()
)
pm1004vMesrotx1LaserWvlengthPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMesrotx1LaserWvlengthPortn.setStatus("current")
_Pm1004vcounters_ObjectIdentity = ObjectIdentity
pm1004vcounters = _Pm1004vcounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4)
)
_Pm1004vCntOther_ObjectIdentity = ObjectIdentity
pm1004vCntOther = _Pm1004vCntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 1)
)
_Pm1004vCntClient_ObjectIdentity = ObjectIdentity
pm1004vCntClient = _Pm1004vCntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 2)
)
_Pm1004vCntLine_ObjectIdentity = ObjectIdentity
pm1004vCntLine = _Pm1004vCntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3)
)
_Pm1004vCntdfrmB1ErrCntTable_Object = MibTable
pm1004vCntdfrmB1ErrCntTable = _Pm1004vCntdfrmB1ErrCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 152)
)
if mibBuilder.loadTexts:
    pm1004vCntdfrmB1ErrCntTable.setStatus("current")
_Pm1004vCntdfrmB1ErrCntEntry_Object = MibTableRow
pm1004vCntdfrmB1ErrCntEntry = _Pm1004vCntdfrmB1ErrCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 152, 1)
)
pm1004vCntdfrmB1ErrCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCntdfrmB1ErrCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCntdfrmB1ErrCntEntry.setStatus("current")


class _Pm1004vCntdfrmB1ErrCntIndex_Type(Integer32):
    """Custom type pm1004vCntdfrmB1ErrCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCntdfrmB1ErrCntIndex_Type.__name__ = "Integer32"
_Pm1004vCntdfrmB1ErrCntIndex_Object = MibTableColumn
pm1004vCntdfrmB1ErrCntIndex = _Pm1004vCntdfrmB1ErrCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 152, 1, 1),
    _Pm1004vCntdfrmB1ErrCntIndex_Type()
)
pm1004vCntdfrmB1ErrCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmB1ErrCntIndex.setStatus("current")
_Pm1004vCntdfrmB1ErrCntValuePortn_Type = Counter32
_Pm1004vCntdfrmB1ErrCntValuePortn_Object = MibTableColumn
pm1004vCntdfrmB1ErrCntValuePortn = _Pm1004vCntdfrmB1ErrCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 152, 1, 2),
    _Pm1004vCntdfrmB1ErrCntValuePortn_Type()
)
pm1004vCntdfrmB1ErrCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmB1ErrCntValuePortn.setStatus("current")
_Pm1004vCntdfrmB1ErrCntErrorPortn_Type = EkiOnOff
_Pm1004vCntdfrmB1ErrCntErrorPortn_Object = MibTableColumn
pm1004vCntdfrmB1ErrCntErrorPortn = _Pm1004vCntdfrmB1ErrCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 152, 1, 3),
    _Pm1004vCntdfrmB1ErrCntErrorPortn_Type()
)
pm1004vCntdfrmB1ErrCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmB1ErrCntErrorPortn.setStatus("current")
_Pm1004vCntdfrmB1ErrCntOverloadPortn_Type = EkiOnOff
_Pm1004vCntdfrmB1ErrCntOverloadPortn_Object = MibTableColumn
pm1004vCntdfrmB1ErrCntOverloadPortn = _Pm1004vCntdfrmB1ErrCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 152, 1, 4),
    _Pm1004vCntdfrmB1ErrCntOverloadPortn_Type()
)
pm1004vCntdfrmB1ErrCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmB1ErrCntOverloadPortn.setStatus("current")
_Pm1004vCntdfrmTimCntTable_Object = MibTable
pm1004vCntdfrmTimCntTable = _Pm1004vCntdfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 153)
)
if mibBuilder.loadTexts:
    pm1004vCntdfrmTimCntTable.setStatus("current")
_Pm1004vCntdfrmTimCntEntry_Object = MibTableRow
pm1004vCntdfrmTimCntEntry = _Pm1004vCntdfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 153, 1)
)
pm1004vCntdfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCntdfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCntdfrmTimCntEntry.setStatus("current")


class _Pm1004vCntdfrmTimCntIndex_Type(Integer32):
    """Custom type pm1004vCntdfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCntdfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm1004vCntdfrmTimCntIndex_Object = MibTableColumn
pm1004vCntdfrmTimCntIndex = _Pm1004vCntdfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 153, 1, 1),
    _Pm1004vCntdfrmTimCntIndex_Type()
)
pm1004vCntdfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmTimCntIndex.setStatus("current")
_Pm1004vCntdfrmTimCntValuePortn_Type = Counter32
_Pm1004vCntdfrmTimCntValuePortn_Object = MibTableColumn
pm1004vCntdfrmTimCntValuePortn = _Pm1004vCntdfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 153, 1, 2),
    _Pm1004vCntdfrmTimCntValuePortn_Type()
)
pm1004vCntdfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmTimCntValuePortn.setStatus("current")
_Pm1004vCntdfrmTimCntErrorPortn_Type = EkiOnOff
_Pm1004vCntdfrmTimCntErrorPortn_Object = MibTableColumn
pm1004vCntdfrmTimCntErrorPortn = _Pm1004vCntdfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 153, 1, 3),
    _Pm1004vCntdfrmTimCntErrorPortn_Type()
)
pm1004vCntdfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmTimCntErrorPortn.setStatus("current")
_Pm1004vCntdfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm1004vCntdfrmTimCntOverloadPortn_Object = MibTableColumn
pm1004vCntdfrmTimCntOverloadPortn = _Pm1004vCntdfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 3, 153, 1, 4),
    _Pm1004vCntdfrmTimCntOverloadPortn_Type()
)
pm1004vCntdfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCntdfrmTimCntOverloadPortn.setStatus("current")
_Pm1004vCntCountersReset_Type = EkiOnOff
_Pm1004vCntCountersReset_Object = MibScalar
pm1004vCntCountersReset = _Pm1004vCntCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 259),
    _Pm1004vCntCountersReset_Type()
)
pm1004vCntCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCntCountersReset.setStatus("current")
_Pm1004vCntCountersStop_Type = EkiOnOff
_Pm1004vCntCountersStop_Object = MibScalar
pm1004vCntCountersStop = _Pm1004vCntCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 4, 260),
    _Pm1004vCntCountersStop_Type()
)
pm1004vCntCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCntCountersStop.setStatus("current")
_Pm1004vcontrolsWrite_ObjectIdentity = ObjectIdentity
pm1004vcontrolsWrite = _Pm1004vcontrolsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6)
)
_Pm1004vCtrlOther_ObjectIdentity = ObjectIdentity
pm1004vCtrlOther = _Pm1004vCtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1)
)
_Pm1004vCtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm1004vCtrlconfMgnt1 = _Pm1004vCtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 1)
)
_Pm1004vCtrlConf1Load1_Type = EkiOnOff
_Pm1004vCtrlConf1Load1_Object = MibScalar
pm1004vCtrlConf1Load1 = _Pm1004vCtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 1, 1),
    _Pm1004vCtrlConf1Load1_Type()
)
pm1004vCtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlConf1Load1.setStatus("current")
_Pm1004vCtrlConf2Load1_Type = EkiOnOff
_Pm1004vCtrlConf2Load1_Object = MibScalar
pm1004vCtrlConf2Load1 = _Pm1004vCtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 1, 2),
    _Pm1004vCtrlConf2Load1_Type()
)
pm1004vCtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlConf2Load1.setStatus("current")
_Pm1004vCtrlConf2Flash1_Type = EkiOnOff
_Pm1004vCtrlConf2Flash1_Object = MibScalar
pm1004vCtrlConf2Flash1 = _Pm1004vCtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 1, 10),
    _Pm1004vCtrlConf2Flash1_Type()
)
pm1004vCtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlConf2Flash1.setStatus("current")
_Pm1004vCtrlConf2Clear1_Type = EkiOnOff
_Pm1004vCtrlConf2Clear1_Object = MibScalar
pm1004vCtrlConf2Clear1 = _Pm1004vCtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 1, 14),
    _Pm1004vCtrlConf2Clear1_Type()
)
pm1004vCtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlConf2Clear1.setStatus("current")
_Pm1004vCtrlsynth4_ObjectIdentity = ObjectIdentity
pm1004vCtrlsynth4 = _Pm1004vCtrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 4)
)
_Pm1004vCtrlCorrelatOn_Type = EkiOnOff
_Pm1004vCtrlCorrelatOn_Object = MibScalar
pm1004vCtrlCorrelatOn = _Pm1004vCtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 4, 1),
    _Pm1004vCtrlCorrelatOn_Type()
)
pm1004vCtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlCorrelatOn.setStatus("current")
_Pm1004vCtrlCorrelatOff_Type = EkiOnOff
_Pm1004vCtrlCorrelatOff_Object = MibScalar
pm1004vCtrlCorrelatOff = _Pm1004vCtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 4, 2),
    _Pm1004vCtrlCorrelatOff_Type()
)
pm1004vCtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlCorrelatOff.setStatus("current")
_Pm1004vCtrlswMgnt_ObjectIdentity = ObjectIdentity
pm1004vCtrlswMgnt = _Pm1004vCtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 5)
)
_Pm1004vCtrlColdReset_Type = EkiOnOff
_Pm1004vCtrlColdReset_Object = MibScalar
pm1004vCtrlColdReset = _Pm1004vCtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 5, 2),
    _Pm1004vCtrlColdReset_Type()
)
pm1004vCtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlColdReset.setStatus("current")
_Pm1004vCtrlWarmReset_Type = EkiOnOff
_Pm1004vCtrlWarmReset_Object = MibScalar
pm1004vCtrlWarmReset = _Pm1004vCtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 5, 3),
    _Pm1004vCtrlWarmReset_Type()
)
pm1004vCtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlWarmReset.setStatus("current")
_Pm1004vCtrlLoadSwBank1_Type = EkiOnOff
_Pm1004vCtrlLoadSwBank1_Object = MibScalar
pm1004vCtrlLoadSwBank1 = _Pm1004vCtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 5, 5),
    _Pm1004vCtrlLoadSwBank1_Type()
)
pm1004vCtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLoadSwBank1.setStatus("current")
_Pm1004vCtrlLoadSwBank2_Type = EkiOnOff
_Pm1004vCtrlLoadSwBank2_Object = MibScalar
pm1004vCtrlLoadSwBank2 = _Pm1004vCtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 5, 6),
    _Pm1004vCtrlLoadSwBank2_Type()
)
pm1004vCtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLoadSwBank2.setStatus("current")
_Pm1004vCtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm1004vCtrlgwMgnt = _Pm1004vCtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 6)
)
_Pm1004vCtrlCurrentGwReset_Type = EkiOnOff
_Pm1004vCtrlCurrentGwReset_Object = MibScalar
pm1004vCtrlCurrentGwReset = _Pm1004vCtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 6, 1),
    _Pm1004vCtrlCurrentGwReset_Type()
)
pm1004vCtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlCurrentGwReset.setStatus("current")
_Pm1004vCtrlLoadGwBank1_Type = EkiOnOff
_Pm1004vCtrlLoadGwBank1_Object = MibScalar
pm1004vCtrlLoadGwBank1 = _Pm1004vCtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 6, 5),
    _Pm1004vCtrlLoadGwBank1_Type()
)
pm1004vCtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLoadGwBank1.setStatus("current")
_Pm1004vCtrlLoadGwBank2_Type = EkiOnOff
_Pm1004vCtrlLoadGwBank2_Object = MibScalar
pm1004vCtrlLoadGwBank2 = _Pm1004vCtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 6, 6),
    _Pm1004vCtrlLoadGwBank2_Type()
)
pm1004vCtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLoadGwBank2.setStatus("current")
_Pm1004vCtrlLoadGwBank3_Type = EkiOnOff
_Pm1004vCtrlLoadGwBank3_Object = MibScalar
pm1004vCtrlLoadGwBank3 = _Pm1004vCtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 6, 7),
    _Pm1004vCtrlLoadGwBank3_Type()
)
pm1004vCtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLoadGwBank3.setStatus("current")
_Pm1004vCtrlLoadGwBank4_Type = EkiOnOff
_Pm1004vCtrlLoadGwBank4_Object = MibScalar
pm1004vCtrlLoadGwBank4 = _Pm1004vCtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 6, 8),
    _Pm1004vCtrlLoadGwBank4_Type()
)
pm1004vCtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLoadGwBank4.setStatus("current")
_Pm1004vCtrlledTest_ObjectIdentity = ObjectIdentity
pm1004vCtrlledTest = _Pm1004vCtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 192)
)
_Pm1004vCtrlGreenLed_Type = EkiOnOff
_Pm1004vCtrlGreenLed_Object = MibScalar
pm1004vCtrlGreenLed = _Pm1004vCtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 192, 1),
    _Pm1004vCtrlGreenLed_Type()
)
pm1004vCtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlGreenLed.setStatus("current")
_Pm1004vCtrlRedLed_Type = EkiOnOff
_Pm1004vCtrlRedLed_Object = MibScalar
pm1004vCtrlRedLed = _Pm1004vCtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 192, 2),
    _Pm1004vCtrlRedLed_Type()
)
pm1004vCtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlRedLed.setStatus("current")
_Pm1004vCtrlLedOff_Type = EkiOnOff
_Pm1004vCtrlLedOff_Object = MibScalar
pm1004vCtrlLedOff = _Pm1004vCtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 192, 3),
    _Pm1004vCtrlLedOff_Type()
)
pm1004vCtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLedOff.setStatus("current")
_Pm1004vCtrlmoduleOosMode_ObjectIdentity = ObjectIdentity
pm1004vCtrlmoduleOosMode = _Pm1004vCtrlmoduleOosMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 193)
)
_Pm1004vCtrlModuleOosMode_Type = EkiOnOff
_Pm1004vCtrlModuleOosMode_Object = MibScalar
pm1004vCtrlModuleOosMode = _Pm1004vCtrlModuleOosMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 193, 1),
    _Pm1004vCtrlModuleOosMode_Type()
)
pm1004vCtrlModuleOosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlModuleOosMode.setStatus("current")
_Pm1004vCtrlmaintenanceMode_ObjectIdentity = ObjectIdentity
pm1004vCtrlmaintenanceMode = _Pm1004vCtrlmaintenanceMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 197)
)
_Pm1004vCtrlMaintenanceMode_Type = EkiOnOff
_Pm1004vCtrlMaintenanceMode_Object = MibScalar
pm1004vCtrlMaintenanceMode = _Pm1004vCtrlMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 1, 197, 1),
    _Pm1004vCtrlMaintenanceMode_Type()
)
pm1004vCtrlMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlMaintenanceMode.setStatus("current")
_Pm1004vCtrlClient_ObjectIdentity = ObjectIdentity
pm1004vCtrlClient = _Pm1004vCtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2)
)
_Pm1004vCtrlaccessLoopTable_Object = MibTable
pm1004vCtrlaccessLoopTable = _Pm1004vCtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm1004vCtrlaccessLoopTable.setStatus("current")
_Pm1004vCtrlaccessLoopEntry_Object = MibTableRow
pm1004vCtrlaccessLoopEntry = _Pm1004vCtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 16, 1)
)
pm1004vCtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlaccessLoopEntry.setStatus("current")


class _Pm1004vCtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm1004vCtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlaccessLoopIndex_Object = MibTableColumn
pm1004vCtrlaccessLoopIndex = _Pm1004vCtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 16, 1, 1),
    _Pm1004vCtrlaccessLoopIndex_Type()
)
pm1004vCtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlaccessLoopIndex.setStatus("current")
_Pm1004vCtrlaccessLoopPortn_Type = EkiState
_Pm1004vCtrlaccessLoopPortn_Object = MibTableColumn
pm1004vCtrlaccessLoopPortn = _Pm1004vCtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 16, 1, 2),
    _Pm1004vCtrlaccessLoopPortn_Type()
)
pm1004vCtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlaccessLoopPortn.setStatus("current")
_Pm1004vCtrlportOosModeTable_Object = MibTable
pm1004vCtrlportOosModeTable = _Pm1004vCtrlportOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 18)
)
if mibBuilder.loadTexts:
    pm1004vCtrlportOosModeTable.setStatus("current")
_Pm1004vCtrlportOosModeEntry_Object = MibTableRow
pm1004vCtrlportOosModeEntry = _Pm1004vCtrlportOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 18, 1)
)
pm1004vCtrlportOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlportOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlportOosModeEntry.setStatus("current")


class _Pm1004vCtrlportOosModeIndex_Type(Integer32):
    """Custom type pm1004vCtrlportOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlportOosModeIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlportOosModeIndex_Object = MibTableColumn
pm1004vCtrlportOosModeIndex = _Pm1004vCtrlportOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 18, 1, 1),
    _Pm1004vCtrlportOosModeIndex_Type()
)
pm1004vCtrlportOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlportOosModeIndex.setStatus("current")
_Pm1004vCtrlportOosModePortn_Type = Pm1004vClientOosMode
_Pm1004vCtrlportOosModePortn_Object = MibTableColumn
pm1004vCtrlportOosModePortn = _Pm1004vCtrlportOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 18, 1, 2),
    _Pm1004vCtrlportOosModePortn_Type()
)
pm1004vCtrlportOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlportOosModePortn.setStatus("current")
_Pm1004vCtrlsfpOffCtrlTable_Object = MibTable
pm1004vCtrlsfpOffCtrlTable = _Pm1004vCtrlsfpOffCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 20)
)
if mibBuilder.loadTexts:
    pm1004vCtrlsfpOffCtrlTable.setStatus("current")
_Pm1004vCtrlsfpOffCtrlEntry_Object = MibTableRow
pm1004vCtrlsfpOffCtrlEntry = _Pm1004vCtrlsfpOffCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 20, 1)
)
pm1004vCtrlsfpOffCtrlEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlsfpOffCtrlIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlsfpOffCtrlEntry.setStatus("current")


class _Pm1004vCtrlsfpOffCtrlIndex_Type(Integer32):
    """Custom type pm1004vCtrlsfpOffCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlsfpOffCtrlIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlsfpOffCtrlIndex_Object = MibTableColumn
pm1004vCtrlsfpOffCtrlIndex = _Pm1004vCtrlsfpOffCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 20, 1, 1),
    _Pm1004vCtrlsfpOffCtrlIndex_Type()
)
pm1004vCtrlsfpOffCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlsfpOffCtrlIndex.setStatus("current")
_Pm1004vCtrlsfpOffCtrlPortn_Type = EkiState
_Pm1004vCtrlsfpOffCtrlPortn_Object = MibTableColumn
pm1004vCtrlsfpOffCtrlPortn = _Pm1004vCtrlsfpOffCtrlPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 20, 1, 2),
    _Pm1004vCtrlsfpOffCtrlPortn_Type()
)
pm1004vCtrlsfpOffCtrlPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlsfpOffCtrlPortn.setStatus("current")
_Pm1004vCtrlcsfUpInsTable_Object = MibTable
pm1004vCtrlcsfUpInsTable = _Pm1004vCtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm1004vCtrlcsfUpInsTable.setStatus("current")
_Pm1004vCtrlcsfUpInsEntry_Object = MibTableRow
pm1004vCtrlcsfUpInsEntry = _Pm1004vCtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 21, 1)
)
pm1004vCtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlcsfUpInsEntry.setStatus("current")


class _Pm1004vCtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm1004vCtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlcsfUpInsIndex_Object = MibTableColumn
pm1004vCtrlcsfUpInsIndex = _Pm1004vCtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 21, 1, 1),
    _Pm1004vCtrlcsfUpInsIndex_Type()
)
pm1004vCtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlcsfUpInsIndex.setStatus("current")
_Pm1004vCtrlcsfUpInsPortn_Type = EkiState
_Pm1004vCtrlcsfUpInsPortn_Object = MibTableColumn
pm1004vCtrlcsfUpInsPortn = _Pm1004vCtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 21, 1, 2),
    _Pm1004vCtrlcsfUpInsPortn_Type()
)
pm1004vCtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlcsfUpInsPortn.setStatus("current")
_Pm1004vCtrlcaisDwInsTable_Object = MibTable
pm1004vCtrlcaisDwInsTable = _Pm1004vCtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm1004vCtrlcaisDwInsTable.setStatus("current")
_Pm1004vCtrlcaisDwInsEntry_Object = MibTableRow
pm1004vCtrlcaisDwInsEntry = _Pm1004vCtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 22, 1)
)
pm1004vCtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlcaisDwInsEntry.setStatus("current")


class _Pm1004vCtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm1004vCtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlcaisDwInsIndex_Object = MibTableColumn
pm1004vCtrlcaisDwInsIndex = _Pm1004vCtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 22, 1, 1),
    _Pm1004vCtrlcaisDwInsIndex_Type()
)
pm1004vCtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlcaisDwInsIndex.setStatus("current")
_Pm1004vCtrlcaisDwInsPortn_Type = EkiState
_Pm1004vCtrlcaisDwInsPortn_Object = MibTableColumn
pm1004vCtrlcaisDwInsPortn = _Pm1004vCtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 22, 1, 2),
    _Pm1004vCtrlcaisDwInsPortn_Type()
)
pm1004vCtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlcaisDwInsPortn.setStatus("current")
_Pm1004vCtrlclientAccessTermLoopTable_Object = MibTable
pm1004vCtrlclientAccessTermLoopTable = _Pm1004vCtrlclientAccessTermLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 26)
)
if mibBuilder.loadTexts:
    pm1004vCtrlclientAccessTermLoopTable.setStatus("current")
_Pm1004vCtrlclientAccessTermLoopEntry_Object = MibTableRow
pm1004vCtrlclientAccessTermLoopEntry = _Pm1004vCtrlclientAccessTermLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 26, 1)
)
pm1004vCtrlclientAccessTermLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlclientAccessTermLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlclientAccessTermLoopEntry.setStatus("current")


class _Pm1004vCtrlclientAccessTermLoopIndex_Type(Integer32):
    """Custom type pm1004vCtrlclientAccessTermLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlclientAccessTermLoopIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlclientAccessTermLoopIndex_Object = MibTableColumn
pm1004vCtrlclientAccessTermLoopIndex = _Pm1004vCtrlclientAccessTermLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 26, 1, 1),
    _Pm1004vCtrlclientAccessTermLoopIndex_Type()
)
pm1004vCtrlclientAccessTermLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlclientAccessTermLoopIndex.setStatus("current")
_Pm1004vCtrlclientAccessTermLoopPortn_Type = EkiState
_Pm1004vCtrlclientAccessTermLoopPortn_Object = MibTableColumn
pm1004vCtrlclientAccessTermLoopPortn = _Pm1004vCtrlclientAccessTermLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 26, 1, 2),
    _Pm1004vCtrlclientAccessTermLoopPortn_Type()
)
pm1004vCtrlclientAccessTermLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlclientAccessTermLoopPortn.setStatus("current")
_Pm1004vCtrlrxVideoProtocolTable_Object = MibTable
pm1004vCtrlrxVideoProtocolTable = _Pm1004vCtrlrxVideoProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 43)
)
if mibBuilder.loadTexts:
    pm1004vCtrlrxVideoProtocolTable.setStatus("current")
_Pm1004vCtrlrxVideoProtocolEntry_Object = MibTableRow
pm1004vCtrlrxVideoProtocolEntry = _Pm1004vCtrlrxVideoProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 43, 1)
)
pm1004vCtrlrxVideoProtocolEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlrxVideoProtocolIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlrxVideoProtocolEntry.setStatus("current")


class _Pm1004vCtrlrxVideoProtocolIndex_Type(Integer32):
    """Custom type pm1004vCtrlrxVideoProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlrxVideoProtocolIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlrxVideoProtocolIndex_Object = MibTableColumn
pm1004vCtrlrxVideoProtocolIndex = _Pm1004vCtrlrxVideoProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 43, 1, 1),
    _Pm1004vCtrlrxVideoProtocolIndex_Type()
)
pm1004vCtrlrxVideoProtocolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlrxVideoProtocolIndex.setStatus("current")
_Pm1004vCtrlrxVideoProtocolPortn_Type = EkiState
_Pm1004vCtrlrxVideoProtocolPortn_Object = MibTableColumn
pm1004vCtrlrxVideoProtocolPortn = _Pm1004vCtrlrxVideoProtocolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 43, 1, 2),
    _Pm1004vCtrlrxVideoProtocolPortn_Type()
)
pm1004vCtrlrxVideoProtocolPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlrxVideoProtocolPortn.setStatus("current")
_Pm1004vCtrladddropClientRxProtectTable_Object = MibTable
pm1004vCtrladddropClientRxProtectTable = _Pm1004vCtrladddropClientRxProtectTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 128)
)
if mibBuilder.loadTexts:
    pm1004vCtrladddropClientRxProtectTable.setStatus("current")
_Pm1004vCtrladddropClientRxProtectEntry_Object = MibTableRow
pm1004vCtrladddropClientRxProtectEntry = _Pm1004vCtrladddropClientRxProtectEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 128, 1)
)
pm1004vCtrladddropClientRxProtectEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrladddropClientRxProtectIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrladddropClientRxProtectEntry.setStatus("current")


class _Pm1004vCtrladddropClientRxProtectIndex_Type(Integer32):
    """Custom type pm1004vCtrladddropClientRxProtectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrladddropClientRxProtectIndex_Type.__name__ = "Integer32"
_Pm1004vCtrladddropClientRxProtectIndex_Object = MibTableColumn
pm1004vCtrladddropClientRxProtectIndex = _Pm1004vCtrladddropClientRxProtectIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 128, 1, 1),
    _Pm1004vCtrladddropClientRxProtectIndex_Type()
)
pm1004vCtrladddropClientRxProtectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrladddropClientRxProtectIndex.setStatus("current")
_Pm1004vCtrladddropClientRxProtectPortn_Type = Pm1004vProtectionTimeSlot
_Pm1004vCtrladddropClientRxProtectPortn_Object = MibTableColumn
pm1004vCtrladddropClientRxProtectPortn = _Pm1004vCtrladddropClientRxProtectPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 128, 1, 2),
    _Pm1004vCtrladddropClientRxProtectPortn_Type()
)
pm1004vCtrladddropClientRxProtectPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrladddropClientRxProtectPortn.setStatus("current")
_Pm1004vCtrladddropTsClientModeTable_Object = MibTable
pm1004vCtrladddropTsClientModeTable = _Pm1004vCtrladddropTsClientModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 136)
)
if mibBuilder.loadTexts:
    pm1004vCtrladddropTsClientModeTable.setStatus("current")
_Pm1004vCtrladddropTsClientModeEntry_Object = MibTableRow
pm1004vCtrladddropTsClientModeEntry = _Pm1004vCtrladddropTsClientModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 136, 1)
)
pm1004vCtrladddropTsClientModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrladddropTsClientModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrladddropTsClientModeEntry.setStatus("current")


class _Pm1004vCtrladddropTsClientModeIndex_Type(Integer32):
    """Custom type pm1004vCtrladddropTsClientModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrladddropTsClientModeIndex_Type.__name__ = "Integer32"
_Pm1004vCtrladddropTsClientModeIndex_Object = MibTableColumn
pm1004vCtrladddropTsClientModeIndex = _Pm1004vCtrladddropTsClientModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 136, 1, 1),
    _Pm1004vCtrladddropTsClientModeIndex_Type()
)
pm1004vCtrladddropTsClientModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrladddropTsClientModeIndex.setStatus("current")
_Pm1004vCtrladddropTsClientModePortn_Type = Pm1004vModeTimeSlot
_Pm1004vCtrladddropTsClientModePortn_Object = MibTableColumn
pm1004vCtrladddropTsClientModePortn = _Pm1004vCtrladddropTsClientModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 2, 136, 1, 2),
    _Pm1004vCtrladddropTsClientModePortn_Type()
)
pm1004vCtrladddropTsClientModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrladddropTsClientModePortn.setStatus("current")
_Pm1004vCtrlLine_ObjectIdentity = ObjectIdentity
pm1004vCtrlLine = _Pm1004vCtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3)
)
_Pm1004vCtrlcommAccessLoop_ObjectIdentity = ObjectIdentity
pm1004vCtrlcommAccessLoop = _Pm1004vCtrlcommAccessLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 64)
)
_Pm1004vCtrlCommAccessloop_Type = EkiOnOff
_Pm1004vCtrlCommAccessloop_Object = MibScalar
pm1004vCtrlCommAccessloop = _Pm1004vCtrlCommAccessloop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 64, 1),
    _Pm1004vCtrlCommAccessloop_Type()
)
pm1004vCtrlCommAccessloop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlCommAccessloop.setStatus("deprecated")
_Pm1004vCtrllineLoop_ObjectIdentity = ObjectIdentity
pm1004vCtrllineLoop = _Pm1004vCtrllineLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 66)
)
_Pm1004vCtrlLineLoop_Type = EkiOnOff
_Pm1004vCtrlLineLoop_Object = MibScalar
pm1004vCtrlLineLoop = _Pm1004vCtrlLineLoop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 66, 1),
    _Pm1004vCtrlLineLoop_Type()
)
pm1004vCtrlLineLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLineLoop.setStatus("deprecated")
_Pm1004vCtrlProtMgnt_ObjectIdentity = ObjectIdentity
pm1004vCtrlProtMgnt = _Pm1004vCtrlProtMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 73)
)


class _Pm1004vCtrlLineNumber_Type(Unsigned32):
    """Custom type pm1004vCtrlLineNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Pm1004vCtrlLineNumber_Type.__name__ = "Unsigned32"
_Pm1004vCtrlLineNumber_Object = MibScalar
pm1004vCtrlLineNumber = _Pm1004vCtrlLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 73, 1),
    _Pm1004vCtrlLineNumber_Type()
)
pm1004vCtrlLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlLineNumber.setStatus("current")
_Pm1004vCtrlProtMode_Type = EkiMode
_Pm1004vCtrlProtMode_Object = MibScalar
pm1004vCtrlProtMode = _Pm1004vCtrlProtMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 73, 2),
    _Pm1004vCtrlProtMode_Type()
)
pm1004vCtrlProtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlProtMode.setStatus("current")
_Pm1004vCtrllineOosModeTable_Object = MibTable
pm1004vCtrllineOosModeTable = _Pm1004vCtrllineOosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 74)
)
if mibBuilder.loadTexts:
    pm1004vCtrllineOosModeTable.setStatus("current")
_Pm1004vCtrllineOosModeEntry_Object = MibTableRow
pm1004vCtrllineOosModeEntry = _Pm1004vCtrllineOosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 74, 1)
)
pm1004vCtrllineOosModeEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrllineOosModeIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrllineOosModeEntry.setStatus("current")


class _Pm1004vCtrllineOosModeIndex_Type(Integer32):
    """Custom type pm1004vCtrllineOosModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrllineOosModeIndex_Type.__name__ = "Integer32"
_Pm1004vCtrllineOosModeIndex_Object = MibTableColumn
pm1004vCtrllineOosModeIndex = _Pm1004vCtrllineOosModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 74, 1, 1),
    _Pm1004vCtrllineOosModeIndex_Type()
)
pm1004vCtrllineOosModeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrllineOosModeIndex.setStatus("current")
_Pm1004vCtrllineOosModePortn_Type = EkiState
_Pm1004vCtrllineOosModePortn_Object = MibTableColumn
pm1004vCtrllineOosModePortn = _Pm1004vCtrllineOosModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 74, 1, 2),
    _Pm1004vCtrllineOosModePortn_Type()
)
pm1004vCtrllineOosModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrllineOosModePortn.setStatus("current")
_Pm1004vCtrldccEnableTable_Object = MibTable
pm1004vCtrldccEnableTable = _Pm1004vCtrldccEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 198)
)
if mibBuilder.loadTexts:
    pm1004vCtrldccEnableTable.setStatus("current")
_Pm1004vCtrldccEnableEntry_Object = MibTableRow
pm1004vCtrldccEnableEntry = _Pm1004vCtrldccEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 198, 1)
)
pm1004vCtrldccEnableEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrldccEnableIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrldccEnableEntry.setStatus("current")


class _Pm1004vCtrldccEnableIndex_Type(Integer32):
    """Custom type pm1004vCtrldccEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrldccEnableIndex_Type.__name__ = "Integer32"
_Pm1004vCtrldccEnableIndex_Object = MibTableColumn
pm1004vCtrldccEnableIndex = _Pm1004vCtrldccEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 198, 1, 1),
    _Pm1004vCtrldccEnableIndex_Type()
)
pm1004vCtrldccEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrldccEnableIndex.setStatus("current")
_Pm1004vCtrldccEnablePortn_Type = EkiState
_Pm1004vCtrldccEnablePortn_Object = MibTableColumn
pm1004vCtrldccEnablePortn = _Pm1004vCtrldccEnablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 198, 1, 2),
    _Pm1004vCtrldccEnablePortn_Type()
)
pm1004vCtrldccEnablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrldccEnablePortn.setStatus("current")
_Pm1004vCtrlxfpOnoffTable_Object = MibTable
pm1004vCtrlxfpOnoffTable = _Pm1004vCtrlxfpOnoffTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 208)
)
if mibBuilder.loadTexts:
    pm1004vCtrlxfpOnoffTable.setStatus("current")
_Pm1004vCtrlxfpOnoffEntry_Object = MibTableRow
pm1004vCtrlxfpOnoffEntry = _Pm1004vCtrlxfpOnoffEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 208, 1)
)
pm1004vCtrlxfpOnoffEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlxfpOnoffIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlxfpOnoffEntry.setStatus("current")


class _Pm1004vCtrlxfpOnoffIndex_Type(Integer32):
    """Custom type pm1004vCtrlxfpOnoffIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlxfpOnoffIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlxfpOnoffIndex_Object = MibTableColumn
pm1004vCtrlxfpOnoffIndex = _Pm1004vCtrlxfpOnoffIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 208, 1, 1),
    _Pm1004vCtrlxfpOnoffIndex_Type()
)
pm1004vCtrlxfpOnoffIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlxfpOnoffIndex.setStatus("current")
_Pm1004vCtrlxfpOnoffPortn_Type = EkiState
_Pm1004vCtrlxfpOnoffPortn_Object = MibTableColumn
pm1004vCtrlxfpOnoffPortn = _Pm1004vCtrlxfpOnoffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 208, 1, 2),
    _Pm1004vCtrlxfpOnoffPortn_Type()
)
pm1004vCtrlxfpOnoffPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlxfpOnoffPortn.setStatus("current")
_Pm1004vCtrlxfpLineLoopTable_Object = MibTable
pm1004vCtrlxfpLineLoopTable = _Pm1004vCtrlxfpLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm1004vCtrlxfpLineLoopTable.setStatus("current")
_Pm1004vCtrlxfpLineLoopEntry_Object = MibTableRow
pm1004vCtrlxfpLineLoopEntry = _Pm1004vCtrlxfpLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 209, 1)
)
pm1004vCtrlxfpLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlxfpLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlxfpLineLoopEntry.setStatus("current")


class _Pm1004vCtrlxfpLineLoopIndex_Type(Integer32):
    """Custom type pm1004vCtrlxfpLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlxfpLineLoopIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlxfpLineLoopIndex_Object = MibTableColumn
pm1004vCtrlxfpLineLoopIndex = _Pm1004vCtrlxfpLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 209, 1, 1),
    _Pm1004vCtrlxfpLineLoopIndex_Type()
)
pm1004vCtrlxfpLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlxfpLineLoopIndex.setStatus("current")
_Pm1004vCtrlxfpLineLoopPortn_Type = EkiState
_Pm1004vCtrlxfpLineLoopPortn_Object = MibTableColumn
pm1004vCtrlxfpLineLoopPortn = _Pm1004vCtrlxfpLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 209, 1, 2),
    _Pm1004vCtrlxfpLineLoopPortn_Type()
)
pm1004vCtrlxfpLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlxfpLineLoopPortn.setStatus("current")
_Pm1004vCtrlxfpXfiLoopTable_Object = MibTable
pm1004vCtrlxfpXfiLoopTable = _Pm1004vCtrlxfpXfiLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm1004vCtrlxfpXfiLoopTable.setStatus("current")
_Pm1004vCtrlxfpXfiLoopEntry_Object = MibTableRow
pm1004vCtrlxfpXfiLoopEntry = _Pm1004vCtrlxfpXfiLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 210, 1)
)
pm1004vCtrlxfpXfiLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCtrlxfpXfiLoopIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCtrlxfpXfiLoopEntry.setStatus("current")


class _Pm1004vCtrlxfpXfiLoopIndex_Type(Integer32):
    """Custom type pm1004vCtrlxfpXfiLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCtrlxfpXfiLoopIndex_Type.__name__ = "Integer32"
_Pm1004vCtrlxfpXfiLoopIndex_Object = MibTableColumn
pm1004vCtrlxfpXfiLoopIndex = _Pm1004vCtrlxfpXfiLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 210, 1, 1),
    _Pm1004vCtrlxfpXfiLoopIndex_Type()
)
pm1004vCtrlxfpXfiLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCtrlxfpXfiLoopIndex.setStatus("current")
_Pm1004vCtrlxfpXfiLoopPortn_Type = EkiState
_Pm1004vCtrlxfpXfiLoopPortn_Object = MibTableColumn
pm1004vCtrlxfpXfiLoopPortn = _Pm1004vCtrlxfpXfiLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 6, 3, 210, 1, 2),
    _Pm1004vCtrlxfpXfiLoopPortn_Type()
)
pm1004vCtrlxfpXfiLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCtrlxfpXfiLoopPortn.setStatus("current")
_Pm1004vri_ObjectIdentity = ObjectIdentity
pm1004vri = _Pm1004vri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7)
)
_Pm1004vriTable_ObjectIdentity = ObjectIdentity
pm1004vriTable = _Pm1004vriTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1)
)
_Pm1004vRinvSfpTable_Object = MibTable
pm1004vRinvSfpTable = _Pm1004vRinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004vRinvSfpTable.setStatus("current")
_Pm1004vRinvSfpEntry_Object = MibTableRow
pm1004vRinvSfpEntry = _Pm1004vRinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 1, 1)
)
pm1004vRinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vRinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004vRinvSfpEntry.setStatus("current")


class _Pm1004vRinvSfpIndex_Type(Integer32):
    """Custom type pm1004vRinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004vRinvSfpIndex_Type.__name__ = "Integer32"
_Pm1004vRinvSfpIndex_Object = MibTableColumn
pm1004vRinvSfpIndex = _Pm1004vRinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 1, 1, 1),
    _Pm1004vRinvSfpIndex_Type()
)
pm1004vRinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvSfpIndex.setStatus("current")
_Pm1004vRinvsfp_Type = DisplayString
_Pm1004vRinvsfp_Object = MibTableColumn
pm1004vRinvsfp = _Pm1004vRinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 1, 1, 2),
    _Pm1004vRinvsfp_Type()
)
pm1004vRinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvsfp.setStatus("current")
_Pm1004vRinvLineTable_Object = MibTable
pm1004vRinvLineTable = _Pm1004vRinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm1004vRinvLineTable.setStatus("current")
_Pm1004vRinvLineEntry_Object = MibTableRow
pm1004vRinvLineEntry = _Pm1004vRinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 2, 1)
)
pm1004vRinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vRinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vRinvLineEntry.setStatus("current")


class _Pm1004vRinvLineIndex_Type(Integer32):
    """Custom type pm1004vRinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm1004vRinvLineIndex_Type.__name__ = "Integer32"
_Pm1004vRinvLineIndex_Object = MibTableColumn
pm1004vRinvLineIndex = _Pm1004vRinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 2, 1, 1),
    _Pm1004vRinvLineIndex_Type()
)
pm1004vRinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvLineIndex.setStatus("current")
_Pm1004vRinvxfpLine_Type = DisplayString
_Pm1004vRinvxfpLine_Object = MibTableColumn
pm1004vRinvxfpLine = _Pm1004vRinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 1, 2, 1, 2),
    _Pm1004vRinvxfpLine_Type()
)
pm1004vRinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvxfpLine.setStatus("current")
_Pm1004vRinvReloadInventory_Type = EkiOnOff
_Pm1004vRinvReloadInventory_Object = MibScalar
pm1004vRinvReloadInventory = _Pm1004vRinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 2),
    _Pm1004vRinvReloadInventory_Type()
)
pm1004vRinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vRinvReloadInventory.setStatus("current")
_Pm1004vRinvHwPlatform_Type = DisplayString
_Pm1004vRinvHwPlatform_Object = MibScalar
pm1004vRinvHwPlatform = _Pm1004vRinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 3),
    _Pm1004vRinvHwPlatform_Type()
)
pm1004vRinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvHwPlatform.setStatus("current")
_Pm1004vRinvModulePlatform_Type = DisplayString
_Pm1004vRinvModulePlatform_Object = MibScalar
pm1004vRinvModulePlatform = _Pm1004vRinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 4),
    _Pm1004vRinvModulePlatform_Type()
)
pm1004vRinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvModulePlatform.setStatus("current")
_Pm1004vRinvSwPlatform_Type = DisplayString
_Pm1004vRinvSwPlatform_Object = MibScalar
pm1004vRinvSwPlatform = _Pm1004vRinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 5),
    _Pm1004vRinvSwPlatform_Type()
)
pm1004vRinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvSwPlatform.setStatus("current")
_Pm1004vRinvGwPlatform_Type = DisplayString
_Pm1004vRinvGwPlatform_Object = MibScalar
pm1004vRinvGwPlatform = _Pm1004vRinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 7, 6),
    _Pm1004vRinvGwPlatform_Type()
)
pm1004vRinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vRinvGwPlatform.setStatus("current")
_Pm1004vdownload_ObjectIdentity = ObjectIdentity
pm1004vdownload = _Pm1004vdownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8)
)
_Pm1004vDwlOther_ObjectIdentity = ObjectIdentity
pm1004vDwlOther = _Pm1004vDwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1)
)
_Pm1004vDwlrestartProcess_ObjectIdentity = ObjectIdentity
pm1004vDwlrestartProcess = _Pm1004vDwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 0)
)
_Pm1004vDwlWarmRestartProcessed_Type = EkiOnOff
_Pm1004vDwlWarmRestartProcessed_Object = MibScalar
pm1004vDwlWarmRestartProcessed = _Pm1004vDwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 0, 1),
    _Pm1004vDwlWarmRestartProcessed_Type()
)
pm1004vDwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlWarmRestartProcessed.setStatus("current")
_Pm1004vDwlColdRestartProcessed_Type = EkiOnOff
_Pm1004vDwlColdRestartProcessed_Object = MibScalar
pm1004vDwlColdRestartProcessed = _Pm1004vDwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 0, 2),
    _Pm1004vDwlColdRestartProcessed_Type()
)
pm1004vDwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlColdRestartProcessed.setStatus("current")
_Pm1004vDwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm1004vDwlswBanksUsed = _Pm1004vDwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 1)
)
_Pm1004vDwlSwBank1Used_Type = EkiOnOff
_Pm1004vDwlSwBank1Used_Object = MibScalar
pm1004vDwlSwBank1Used = _Pm1004vDwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 1, 1),
    _Pm1004vDwlSwBank1Used_Type()
)
pm1004vDwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlSwBank1Used.setStatus("current")
_Pm1004vDwlSwBank2Used_Type = EkiOnOff
_Pm1004vDwlSwBank2Used_Object = MibScalar
pm1004vDwlSwBank2Used = _Pm1004vDwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 1, 2),
    _Pm1004vDwlSwBank2Used_Type()
)
pm1004vDwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlSwBank2Used.setStatus("current")
_Pm1004vDwlSwBank1Notempty_Type = EkiOnOff
_Pm1004vDwlSwBank1Notempty_Object = MibScalar
pm1004vDwlSwBank1Notempty = _Pm1004vDwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 1, 5),
    _Pm1004vDwlSwBank1Notempty_Type()
)
pm1004vDwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlSwBank1Notempty.setStatus("current")
_Pm1004vDwlSwBank2Notempty_Type = EkiOnOff
_Pm1004vDwlSwBank2Notempty_Object = MibScalar
pm1004vDwlSwBank2Notempty = _Pm1004vDwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 1, 6),
    _Pm1004vDwlSwBank2Notempty_Type()
)
pm1004vDwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlSwBank2Notempty.setStatus("current")
_Pm1004vDwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm1004vDwlgwBanksUsed = _Pm1004vDwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2)
)
_Pm1004vDwlGwBank1Used_Type = EkiOnOff
_Pm1004vDwlGwBank1Used_Object = MibScalar
pm1004vDwlGwBank1Used = _Pm1004vDwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 1),
    _Pm1004vDwlGwBank1Used_Type()
)
pm1004vDwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank1Used.setStatus("current")
_Pm1004vDwlGwBank2Used_Type = EkiOnOff
_Pm1004vDwlGwBank2Used_Object = MibScalar
pm1004vDwlGwBank2Used = _Pm1004vDwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 2),
    _Pm1004vDwlGwBank2Used_Type()
)
pm1004vDwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank2Used.setStatus("current")
_Pm1004vDwlGwBank3Used_Type = EkiOnOff
_Pm1004vDwlGwBank3Used_Object = MibScalar
pm1004vDwlGwBank3Used = _Pm1004vDwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 3),
    _Pm1004vDwlGwBank3Used_Type()
)
pm1004vDwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank3Used.setStatus("current")
_Pm1004vDwlGwBank4Used_Type = EkiOnOff
_Pm1004vDwlGwBank4Used_Object = MibScalar
pm1004vDwlGwBank4Used = _Pm1004vDwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 4),
    _Pm1004vDwlGwBank4Used_Type()
)
pm1004vDwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank4Used.setStatus("current")
_Pm1004vDwlGwBank1Notempty_Type = EkiOnOff
_Pm1004vDwlGwBank1Notempty_Object = MibScalar
pm1004vDwlGwBank1Notempty = _Pm1004vDwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 5),
    _Pm1004vDwlGwBank1Notempty_Type()
)
pm1004vDwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank1Notempty.setStatus("current")
_Pm1004vDwlGwBank2Notempty_Type = EkiOnOff
_Pm1004vDwlGwBank2Notempty_Object = MibScalar
pm1004vDwlGwBank2Notempty = _Pm1004vDwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 6),
    _Pm1004vDwlGwBank2Notempty_Type()
)
pm1004vDwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank2Notempty.setStatus("current")
_Pm1004vDwlGwBank3Notempty_Type = EkiOnOff
_Pm1004vDwlGwBank3Notempty_Object = MibScalar
pm1004vDwlGwBank3Notempty = _Pm1004vDwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 7),
    _Pm1004vDwlGwBank3Notempty_Type()
)
pm1004vDwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank3Notempty.setStatus("current")
_Pm1004vDwlGwBank4Notempty_Type = EkiOnOff
_Pm1004vDwlGwBank4Notempty_Object = MibScalar
pm1004vDwlGwBank4Notempty = _Pm1004vDwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 1, 2, 8),
    _Pm1004vDwlGwBank4Notempty_Type()
)
pm1004vDwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vDwlGwBank4Notempty.setStatus("current")
_Pm1004vDwlClient_ObjectIdentity = ObjectIdentity
pm1004vDwlClient = _Pm1004vDwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 2)
)
_Pm1004vDwlLine_ObjectIdentity = ObjectIdentity
pm1004vDwlLine = _Pm1004vDwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 8, 3)
)
_Pm1004vConfig_ObjectIdentity = ObjectIdentity
pm1004vConfig = _Pm1004vConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9)
)
_Pm1004vCfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm1004vCfgAccessCAisCsf = _Pm1004vCfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1)
)
_Pm1004vCfgClientcaiscsfTable_Object = MibTable
pm1004vCfgClientcaiscsfTable = _Pm1004vCfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm1004vCfgClientcaiscsfTable.setStatus("current")
_Pm1004vCfgClientcaiscsfEntry_Object = MibTableRow
pm1004vCfgClientcaiscsfEntry = _Pm1004vCfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1)
)
pm1004vCfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgClientcaiscsfEntry.setStatus("current")


class _Pm1004vCfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm1004vCfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm1004vCfgClientcaiscsfIndex_Object = MibTableColumn
pm1004vCfgClientcaiscsfIndex = _Pm1004vCfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 1),
    _Pm1004vCfgClientcaiscsfIndex_Type()
)
pm1004vCfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgClientcaiscsfIndex.setStatus("current")


class _Pm1004vCfgCAisModePortn_Type(Unsigned32):
    """Custom type pm1004vCfgCAisModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgCAisModePortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgCAisModePortn_Object = MibTableColumn
pm1004vCfgCAisModePortn = _Pm1004vCfgCAisModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 3),
    _Pm1004vCfgCAisModePortn_Type()
)
pm1004vCfgCAisModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgCAisModePortn.setStatus("current")


class _Pm1004vCfgUpAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004vCfgUpAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgUpAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgUpAccessioAlmPortn_Object = MibTableColumn
pm1004vCfgUpAccessioAlmPortn = _Pm1004vCfgUpAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 9),
    _Pm1004vCfgUpAccessioAlmPortn_Type()
)
pm1004vCfgUpAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgUpAccessioAlmPortn.setStatus("current")


class _Pm1004vCfgUpMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004vCfgUpMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgUpMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgUpMapperDeAlmPortn_Object = MibTableColumn
pm1004vCfgUpMapperDeAlmPortn = _Pm1004vCfgUpMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 10),
    _Pm1004vCfgUpMapperDeAlmPortn_Type()
)
pm1004vCfgUpMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgUpMapperDeAlmPortn.setStatus("current")


class _Pm1004vCfgDownAccessioAlmPortn_Type(Unsigned32):
    """Custom type pm1004vCfgDownAccessioAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgDownAccessioAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgDownAccessioAlmPortn_Object = MibTableColumn
pm1004vCfgDownAccessioAlmPortn = _Pm1004vCfgDownAccessioAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 17),
    _Pm1004vCfgDownAccessioAlmPortn_Type()
)
pm1004vCfgDownAccessioAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgDownAccessioAlmPortn.setStatus("current")


class _Pm1004vCfgDownMapperDeAlmPortn_Type(Unsigned32):
    """Custom type pm1004vCfgDownMapperDeAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgDownMapperDeAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgDownMapperDeAlmPortn_Object = MibTableColumn
pm1004vCfgDownMapperDeAlmPortn = _Pm1004vCfgDownMapperDeAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 18),
    _Pm1004vCfgDownMapperDeAlmPortn_Type()
)
pm1004vCfgDownMapperDeAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgDownMapperDeAlmPortn.setStatus("current")


class _Pm1004vCfgDownDfrmAlmPortn_Type(Unsigned32):
    """Custom type pm1004vCfgDownDfrmAlmPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgDownDfrmAlmPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgDownDfrmAlmPortn_Object = MibTableColumn
pm1004vCfgDownDfrmAlmPortn = _Pm1004vCfgDownDfrmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 19),
    _Pm1004vCfgDownDfrmAlmPortn_Type()
)
pm1004vCfgDownDfrmAlmPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgDownDfrmAlmPortn.setStatus("current")


class _Pm1004vCfgDownLineSyncAlarmsPortn_Type(Unsigned32):
    """Custom type pm1004vCfgDownLineSyncAlarmsPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgDownLineSyncAlarmsPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgDownLineSyncAlarmsPortn_Object = MibTableColumn
pm1004vCfgDownLineSyncAlarmsPortn = _Pm1004vCfgDownLineSyncAlarmsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 1, 1, 1, 20),
    _Pm1004vCfgDownLineSyncAlarmsPortn_Type()
)
pm1004vCfgDownLineSyncAlarmsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgDownLineSyncAlarmsPortn.setStatus("deprecated")
_Pm1004vCfgStartup_ObjectIdentity = ObjectIdentity
pm1004vCfgStartup = _Pm1004vCfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2)
)
_Pm1004vCfgClientStartupTable_Object = MibTable
pm1004vCfgClientStartupTable = _Pm1004vCfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm1004vCfgClientStartupTable.setStatus("current")
_Pm1004vCfgClientStartupEntry_Object = MibTableRow
pm1004vCfgClientStartupEntry = _Pm1004vCfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 1, 1)
)
pm1004vCfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgClientStartupEntry.setStatus("current")


class _Pm1004vCfgClientStartupIndex_Type(Integer32):
    """Custom type pm1004vCfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm1004vCfgClientStartupIndex_Object = MibTableColumn
pm1004vCfgClientStartupIndex = _Pm1004vCfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 1, 1, 1),
    _Pm1004vCfgClientStartupIndex_Type()
)
pm1004vCfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgClientStartupIndex.setStatus("current")


class _Pm1004vCfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vCfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgSystConfPortPortn_Object = MibTableColumn
pm1004vCfgSystConfPortPortn = _Pm1004vCfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 1, 1, 3),
    _Pm1004vCfgSystConfPortPortn_Type()
)
pm1004vCfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgSystConfPortPortn.setStatus("current")


class _Pm1004vCfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vCfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgNetConfPortPortn_Object = MibTableColumn
pm1004vCfgNetConfPortPortn = _Pm1004vCfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 1, 1, 4),
    _Pm1004vCfgNetConfPortPortn_Type()
)
pm1004vCfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgNetConfPortPortn.setStatus("current")


class _Pm1004vCfgAdddropConfPortPortn_Type(Unsigned32):
    """Custom type pm1004vCfgAdddropConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgAdddropConfPortPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgAdddropConfPortPortn_Object = MibTableColumn
pm1004vCfgAdddropConfPortPortn = _Pm1004vCfgAdddropConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 1, 1, 5),
    _Pm1004vCfgAdddropConfPortPortn_Type()
)
pm1004vCfgAdddropConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgAdddropConfPortPortn.setStatus("deprecated")
_Pm1004vtablelineStartup_ObjectIdentity = ObjectIdentity
pm1004vtablelineStartup = _Pm1004vtablelineStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 2)
)


class _Pm1004vCfgsystConfLine1_Type(Unsigned32):
    """Custom type pm1004vCfgsystConfLine1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgsystConfLine1_Type.__name__ = "Unsigned32"
_Pm1004vCfgsystConfLine1_Object = MibScalar
pm1004vCfgsystConfLine1 = _Pm1004vCfgsystConfLine1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 2, 2),
    _Pm1004vCfgsystConfLine1_Type()
)
pm1004vCfgsystConfLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgsystConfLine1.setStatus("current")


class _Pm1004vCfglineOptions1_Type(Unsigned32):
    """Custom type pm1004vCfglineOptions1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfglineOptions1_Type.__name__ = "Unsigned32"
_Pm1004vCfglineOptions1_Object = MibScalar
pm1004vCfglineOptions1 = _Pm1004vCfglineOptions1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 2, 5),
    _Pm1004vCfglineOptions1_Type()
)
pm1004vCfglineOptions1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfglineOptions1.setStatus("current")


class _Pm1004vCfgsystConfLine2_Type(Unsigned32):
    """Custom type pm1004vCfgsystConfLine2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgsystConfLine2_Type.__name__ = "Unsigned32"
_Pm1004vCfgsystConfLine2_Object = MibScalar
pm1004vCfgsystConfLine2 = _Pm1004vCfgsystConfLine2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 2, 6),
    _Pm1004vCfgsystConfLine2_Type()
)
pm1004vCfgsystConfLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgsystConfLine2.setStatus("current")


class _Pm1004vCfglineSelection_Type(Unsigned32):
    """Custom type pm1004vCfglineSelection based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfglineSelection_Type.__name__ = "Unsigned32"
_Pm1004vCfglineSelection_Object = MibScalar
pm1004vCfglineSelection = _Pm1004vCfglineSelection_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 2, 7),
    _Pm1004vCfglineSelection_Type()
)
pm1004vCfglineSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfglineSelection.setStatus("current")


class _Pm1004vCfglineOptions2_Type(Unsigned32):
    """Custom type pm1004vCfglineOptions2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfglineOptions2_Type.__name__ = "Unsigned32"
_Pm1004vCfglineOptions2_Object = MibScalar
pm1004vCfglineOptions2 = _Pm1004vCfglineOptions2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 2, 9),
    _Pm1004vCfglineOptions2_Type()
)
pm1004vCfglineOptions2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfglineOptions2.setStatus("current")
_Pm1004vCfgXfpTable_Object = MibTable
pm1004vCfgXfpTable = _Pm1004vCfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm1004vCfgXfpTable.setStatus("current")
_Pm1004vCfgXfpEntry_Object = MibTableRow
pm1004vCfgXfpEntry = _Pm1004vCfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 3, 1)
)
pm1004vCfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgXfpEntry.setStatus("current")


class _Pm1004vCfgXfpIndex_Type(Integer32):
    """Custom type pm1004vCfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgXfpIndex_Type.__name__ = "Integer32"
_Pm1004vCfgXfpIndex_Object = MibTableColumn
pm1004vCfgXfpIndex = _Pm1004vCfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 3, 1, 1),
    _Pm1004vCfgXfpIndex_Type()
)
pm1004vCfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgXfpIndex.setStatus("current")


class _Pm1004vCfgSystConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004vCfgSystConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgSystConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgSystConfXfpPortn_Object = MibTableColumn
pm1004vCfgSystConfXfpPortn = _Pm1004vCfgSystConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 3, 1, 3),
    _Pm1004vCfgSystConfXfpPortn_Type()
)
pm1004vCfgSystConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgSystConfXfpPortn.setStatus("current")


class _Pm1004vCfgDataRateConfXfpPortn_Type(Unsigned32):
    """Custom type pm1004vCfgDataRateConfXfpPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgDataRateConfXfpPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgDataRateConfXfpPortn_Object = MibTableColumn
pm1004vCfgDataRateConfXfpPortn = _Pm1004vCfgDataRateConfXfpPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 2, 3, 1, 4),
    _Pm1004vCfgDataRateConfXfpPortn_Type()
)
pm1004vCfgDataRateConfXfpPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgDataRateConfXfpPortn.setStatus("deprecated")
_Pm1004vCfgLabels_ObjectIdentity = ObjectIdentity
pm1004vCfgLabels = _Pm1004vCfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3)
)
_Pm1004vCfgLabelclientTable_Object = MibTable
pm1004vCfgLabelclientTable = _Pm1004vCfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm1004vCfgLabelclientTable.setStatus("current")
_Pm1004vCfgLabelclientEntry_Object = MibTableRow
pm1004vCfgLabelclientEntry = _Pm1004vCfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 1, 1)
)
pm1004vCfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgLabelclientEntry.setStatus("current")


class _Pm1004vCfgLabelclientIndex_Type(Integer32):
    """Custom type pm1004vCfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm1004vCfgLabelclientIndex_Object = MibTableColumn
pm1004vCfgLabelclientIndex = _Pm1004vCfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 1, 1, 1),
    _Pm1004vCfgLabelclientIndex_Type()
)
pm1004vCfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgLabelclientIndex.setStatus("current")


class _Pm1004vCfgLabelclientPortn_Type(DisplayString):
    """Custom type pm1004vCfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004vCfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm1004vCfgLabelclientPortn_Object = MibTableColumn
pm1004vCfgLabelclientPortn = _Pm1004vCfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 1, 1, 3),
    _Pm1004vCfgLabelclientPortn_Type()
)
pm1004vCfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLabelclientPortn.setStatus("current")
_Pm1004vCfgLabellineTable_Object = MibTable
pm1004vCfgLabellineTable = _Pm1004vCfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm1004vCfgLabellineTable.setStatus("current")
_Pm1004vCfgLabellineEntry_Object = MibTableRow
pm1004vCfgLabellineEntry = _Pm1004vCfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 2, 1)
)
pm1004vCfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgLabellineEntry.setStatus("current")


class _Pm1004vCfgLabellineIndex_Type(Integer32):
    """Custom type pm1004vCfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgLabellineIndex_Type.__name__ = "Integer32"
_Pm1004vCfgLabellineIndex_Object = MibTableColumn
pm1004vCfgLabellineIndex = _Pm1004vCfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 2, 1, 1),
    _Pm1004vCfgLabellineIndex_Type()
)
pm1004vCfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgLabellineIndex.setStatus("current")


class _Pm1004vCfgLabellinePortn_Type(DisplayString):
    """Custom type pm1004vCfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm1004vCfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm1004vCfgLabellinePortn_Object = MibTableColumn
pm1004vCfgLabellinePortn = _Pm1004vCfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 3, 2, 1, 3),
    _Pm1004vCfgLabellinePortn_Type()
)
pm1004vCfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLabellinePortn.setStatus("current")
_Pm1004vCfgStartupthresholds_ObjectIdentity = ObjectIdentity
pm1004vCfgStartupthresholds = _Pm1004vCfgStartupthresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4)
)
_Pm1004vCfgClientStartupThreshTable_Object = MibTable
pm1004vCfgClientStartupThreshTable = _Pm1004vCfgClientStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm1004vCfgClientStartupThreshTable.setStatus("current")
_Pm1004vCfgClientStartupThreshEntry_Object = MibTableRow
pm1004vCfgClientStartupThreshEntry = _Pm1004vCfgClientStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1, 1)
)
pm1004vCfgClientStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgClientStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgClientStartupThreshEntry.setStatus("current")


class _Pm1004vCfgClientStartupThreshIndex_Type(Integer32):
    """Custom type pm1004vCfgClientStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgClientStartupThreshIndex_Type.__name__ = "Integer32"
_Pm1004vCfgClientStartupThreshIndex_Object = MibTableColumn
pm1004vCfgClientStartupThreshIndex = _Pm1004vCfgClientStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1, 1, 1),
    _Pm1004vCfgClientStartupThreshIndex_Type()
)
pm1004vCfgClientStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgClientStartupThreshIndex.setStatus("current")


class _Pm1004vCfgClientThreshtxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vCfgClientThreshtxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgClientThreshtxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgClientThreshtxpowhighPortn_Object = MibTableColumn
pm1004vCfgClientThreshtxpowhighPortn = _Pm1004vCfgClientThreshtxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1, 1, 15),
    _Pm1004vCfgClientThreshtxpowhighPortn_Type()
)
pm1004vCfgClientThreshtxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgClientThreshtxpowhighPortn.setStatus("current")


class _Pm1004vCfgClientThreshtxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vCfgClientThreshtxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgClientThreshtxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgClientThreshtxpowlowPortn_Object = MibTableColumn
pm1004vCfgClientThreshtxpowlowPortn = _Pm1004vCfgClientThreshtxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1, 1, 16),
    _Pm1004vCfgClientThreshtxpowlowPortn_Type()
)
pm1004vCfgClientThreshtxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgClientThreshtxpowlowPortn.setStatus("current")


class _Pm1004vCfgClientThreshrxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vCfgClientThreshrxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgClientThreshrxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgClientThreshrxpowhighPortn_Object = MibTableColumn
pm1004vCfgClientThreshrxpowhighPortn = _Pm1004vCfgClientThreshrxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1, 1, 19),
    _Pm1004vCfgClientThreshrxpowhighPortn_Type()
)
pm1004vCfgClientThreshrxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgClientThreshrxpowhighPortn.setStatus("current")


class _Pm1004vCfgClientThreshrxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vCfgClientThreshrxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgClientThreshrxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgClientThreshrxpowlowPortn_Object = MibTableColumn
pm1004vCfgClientThreshrxpowlowPortn = _Pm1004vCfgClientThreshrxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 1, 1, 20),
    _Pm1004vCfgClientThreshrxpowlowPortn_Type()
)
pm1004vCfgClientThreshrxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgClientThreshrxpowlowPortn.setStatus("current")
_Pm1004vCfgLineStartupThreshTable_Object = MibTable
pm1004vCfgLineStartupThreshTable = _Pm1004vCfgLineStartupThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2)
)
if mibBuilder.loadTexts:
    pm1004vCfgLineStartupThreshTable.setStatus("current")
_Pm1004vCfgLineStartupThreshEntry_Object = MibTableRow
pm1004vCfgLineStartupThreshEntry = _Pm1004vCfgLineStartupThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2, 1)
)
pm1004vCfgLineStartupThreshEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgLineStartupThreshIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgLineStartupThreshEntry.setStatus("current")


class _Pm1004vCfgLineStartupThreshIndex_Type(Integer32):
    """Custom type pm1004vCfgLineStartupThreshIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgLineStartupThreshIndex_Type.__name__ = "Integer32"
_Pm1004vCfgLineStartupThreshIndex_Object = MibTableColumn
pm1004vCfgLineStartupThreshIndex = _Pm1004vCfgLineStartupThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2, 1, 1),
    _Pm1004vCfgLineStartupThreshIndex_Type()
)
pm1004vCfgLineStartupThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgLineStartupThreshIndex.setStatus("current")


class _Pm1004vCfgLineThreshtxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineThreshtxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineThreshtxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineThreshtxpowhighPortn_Object = MibTableColumn
pm1004vCfgLineThreshtxpowhighPortn = _Pm1004vCfgLineThreshtxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2, 1, 15),
    _Pm1004vCfgLineThreshtxpowhighPortn_Type()
)
pm1004vCfgLineThreshtxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineThreshtxpowhighPortn.setStatus("current")


class _Pm1004vCfgLineThreshtxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineThreshtxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineThreshtxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineThreshtxpowlowPortn_Object = MibTableColumn
pm1004vCfgLineThreshtxpowlowPortn = _Pm1004vCfgLineThreshtxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2, 1, 16),
    _Pm1004vCfgLineThreshtxpowlowPortn_Type()
)
pm1004vCfgLineThreshtxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineThreshtxpowlowPortn.setStatus("current")


class _Pm1004vCfgLineThreshrxpowhighPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineThreshrxpowhighPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineThreshrxpowhighPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineThreshrxpowhighPortn_Object = MibTableColumn
pm1004vCfgLineThreshrxpowhighPortn = _Pm1004vCfgLineThreshrxpowhighPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2, 1, 19),
    _Pm1004vCfgLineThreshrxpowhighPortn_Type()
)
pm1004vCfgLineThreshrxpowhighPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineThreshrxpowhighPortn.setStatus("current")


class _Pm1004vCfgLineThreshrxpowlowPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineThreshrxpowlowPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineThreshrxpowlowPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineThreshrxpowlowPortn_Object = MibTableColumn
pm1004vCfgLineThreshrxpowlowPortn = _Pm1004vCfgLineThreshrxpowlowPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 4, 2, 1, 20),
    _Pm1004vCfgLineThreshrxpowlowPortn_Type()
)
pm1004vCfgLineThreshrxpowlowPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineThreshrxpowlowPortn.setStatus("current")
_Pm1004vCfgStartuptlh_ObjectIdentity = ObjectIdentity
pm1004vCfgStartuptlh = _Pm1004vCfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5)
)
_Pm1004vCfgOtxtlhTable_Object = MibTable
pm1004vCfgOtxtlhTable = _Pm1004vCfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1)
)
if mibBuilder.loadTexts:
    pm1004vCfgOtxtlhTable.setStatus("current")
_Pm1004vCfgOtxtlhEntry_Object = MibTableRow
pm1004vCfgOtxtlhEntry = _Pm1004vCfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1)
)
pm1004vCfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgOtxtlhEntry.setStatus("current")


class _Pm1004vCfgOtxtlhIndex_Type(Integer32):
    """Custom type pm1004vCfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm1004vCfgOtxtlhIndex_Object = MibTableColumn
pm1004vCfgOtxtlhIndex = _Pm1004vCfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 1),
    _Pm1004vCfgOtxtlhIndex_Type()
)
pm1004vCfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgOtxtlhIndex.setStatus("current")


class _Pm1004vCfgNuPortn_Type(Unsigned32):
    """Custom type pm1004vCfgNuPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgNuPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgNuPortn_Object = MibTableColumn
pm1004vCfgNuPortn = _Pm1004vCfgNuPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 3),
    _Pm1004vCfgNuPortn_Type()
)
pm1004vCfgNuPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgNuPortn.setStatus("deprecated")


class _Pm1004vCfgLineDitherRatePortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineDitherRatePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineDitherRatePortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineDitherRatePortn_Object = MibTableColumn
pm1004vCfgLineDitherRatePortn = _Pm1004vCfgLineDitherRatePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 4),
    _Pm1004vCfgLineDitherRatePortn_Type()
)
pm1004vCfgLineDitherRatePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineDitherRatePortn.setStatus("current")


class _Pm1004vCfgLineDitherFhzPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineDitherFhzPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineDitherFhzPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineDitherFhzPortn_Object = MibTableColumn
pm1004vCfgLineDitherFhzPortn = _Pm1004vCfgLineDitherFhzPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 5),
    _Pm1004vCfgLineDitherFhzPortn_Type()
)
pm1004vCfgLineDitherFhzPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineDitherFhzPortn.setStatus("current")


class _Pm1004vCfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLinePwrLaserPortn_Object = MibTableColumn
pm1004vCfgLinePwrLaserPortn = _Pm1004vCfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 6),
    _Pm1004vCfgLinePwrLaserPortn_Type()
)
pm1004vCfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLinePwrLaserPortn.setStatus("current")


class _Pm1004vCfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineFCurrentPortn_Object = MibTableColumn
pm1004vCfgLineFCurrentPortn = _Pm1004vCfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 7),
    _Pm1004vCfgLineFCurrentPortn_Type()
)
pm1004vCfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineFCurrentPortn.setStatus("current")


class _Pm1004vCfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLineGridCurrentPortn_Object = MibTableColumn
pm1004vCfgLineGridCurrentPortn = _Pm1004vCfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 8),
    _Pm1004vCfgLineGridCurrentPortn_Type()
)
pm1004vCfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLineGridCurrentPortn.setStatus("current")


class _Pm1004vCfgFPortn_Type(Unsigned32):
    """Custom type pm1004vCfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgFPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgFPortn_Object = MibTableColumn
pm1004vCfgFPortn = _Pm1004vCfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 9),
    _Pm1004vCfgFPortn_Type()
)
pm1004vCfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgFPortn.setStatus("current")


class _Pm1004vCfgReservedPortn_Type(Unsigned32):
    """Custom type pm1004vCfgReservedPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgReservedPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgReservedPortn_Object = MibTableColumn
pm1004vCfgReservedPortn = _Pm1004vCfgReservedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 10),
    _Pm1004vCfgReservedPortn_Type()
)
pm1004vCfgReservedPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgReservedPortn.setStatus("deprecated")


class _Pm1004vCfgLinePhotodiodeModePortn_Type(Unsigned32):
    """Custom type pm1004vCfgLinePhotodiodeModePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLinePhotodiodeModePortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLinePhotodiodeModePortn_Object = MibTableColumn
pm1004vCfgLinePhotodiodeModePortn = _Pm1004vCfgLinePhotodiodeModePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 11),
    _Pm1004vCfgLinePhotodiodeModePortn_Type()
)
pm1004vCfgLinePhotodiodeModePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLinePhotodiodeModePortn.setStatus("current")


class _Pm1004vCfgLinePhotodiodeValuePortn_Type(Unsigned32):
    """Custom type pm1004vCfgLinePhotodiodeValuePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLinePhotodiodeValuePortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLinePhotodiodeValuePortn_Object = MibTableColumn
pm1004vCfgLinePhotodiodeValuePortn = _Pm1004vCfgLinePhotodiodeValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 5, 1, 1, 12),
    _Pm1004vCfgLinePhotodiodeValuePortn_Type()
)
pm1004vCfgLinePhotodiodeValuePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgLinePhotodiodeValuePortn.setStatus("current")
_Pm1004vCfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm1004vCfgStartuptablefive = _Pm1004vCfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6)
)
_Pm1004vCfgOtxtlhcapabilitiesTable_Object = MibTable
pm1004vCfgOtxtlhcapabilitiesTable = _Pm1004vCfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm1004vCfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm1004vCfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm1004vCfgOtxtlhcapabilitiesEntry = _Pm1004vCfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1)
)
pm1004vCfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vCfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm1004vCfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm1004vCfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm1004vCfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vCfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm1004vCfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm1004vCfgOtxtlhcapabilitiesIndex = _Pm1004vCfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1, 1),
    _Pm1004vCfgOtxtlhcapabilitiesIndex_Type()
)
pm1004vCfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm1004vCfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm1004vCfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgComponentTypePortn_Object = MibTableColumn
pm1004vCfgComponentTypePortn = _Pm1004vCfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1, 3),
    _Pm1004vCfgComponentTypePortn_Type()
)
pm1004vCfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgComponentTypePortn.setStatus("current")


class _Pm1004vCfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm1004vCfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgMiscellaneousPortn_Object = MibTableColumn
pm1004vCfgMiscellaneousPortn = _Pm1004vCfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1, 4),
    _Pm1004vCfgMiscellaneousPortn_Type()
)
pm1004vCfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgMiscellaneousPortn.setStatus("current")


class _Pm1004vCfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm1004vCfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgFirstChannelPortn_Object = MibTableColumn
pm1004vCfgFirstChannelPortn = _Pm1004vCfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1, 5),
    _Pm1004vCfgFirstChannelPortn_Type()
)
pm1004vCfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgFirstChannelPortn.setStatus("current")


class _Pm1004vCfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm1004vCfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgLastChannelPortn_Object = MibTableColumn
pm1004vCfgLastChannelPortn = _Pm1004vCfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1, 6),
    _Pm1004vCfgLastChannelPortn_Type()
)
pm1004vCfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgLastChannelPortn.setStatus("current")


class _Pm1004vCfgGridPortn_Type(Unsigned32):
    """Custom type pm1004vCfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm1004vCfgGridPortn_Type.__name__ = "Unsigned32"
_Pm1004vCfgGridPortn_Object = MibTableColumn
pm1004vCfgGridPortn = _Pm1004vCfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 6, 1, 1, 7),
    _Pm1004vCfgGridPortn_Type()
)
pm1004vCfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vCfgGridPortn.setStatus("current")
_Pm1004vCfgWriteConfiguration_Type = EkiOnOff
_Pm1004vCfgWriteConfiguration_Object = MibScalar
pm1004vCfgWriteConfiguration = _Pm1004vCfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 9, 257),
    _Pm1004vCfgWriteConfiguration_Type()
)
pm1004vCfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vCfgWriteConfiguration.setStatus("current")
_Pm1004vtraps_ObjectIdentity = ObjectIdentity
pm1004vtraps = _Pm1004vtraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10)
)


class _Pm1004vtrapPortNumber_Type(Integer32):
    """Custom type pm1004vtrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004vtrapPortNumber_Type.__name__ = "Integer32"
_Pm1004vtrapPortNumber_Object = MibScalar
pm1004vtrapPortNumber = _Pm1004vtrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 2),
    _Pm1004vtrapPortNumber_Type()
)
pm1004vtrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vtrapPortNumber.setStatus("current")


class _Pm1004vtrapLineNumber_Type(Integer32):
    """Custom type pm1004vtrapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004vtrapLineNumber_Type.__name__ = "Integer32"
_Pm1004vtrapLineNumber_Object = MibScalar
pm1004vtrapLineNumber = _Pm1004vtrapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 3),
    _Pm1004vtrapLineNumber_Type()
)
pm1004vtrapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vtrapLineNumber.setStatus("current")


class _Pm1004vtrapBoardNumber_Type(Integer32):
    """Custom type pm1004vtrapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm1004vtrapBoardNumber_Type.__name__ = "Integer32"
_Pm1004vtrapBoardNumber_Object = MibScalar
pm1004vtrapBoardNumber = _Pm1004vtrapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 4),
    _Pm1004vtrapBoardNumber_Type()
)
pm1004vtrapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vtrapBoardNumber.setStatus("current")
_Pm1004vMonitoring_ObjectIdentity = ObjectIdentity
pm1004vMonitoring = _Pm1004vMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11)
)
_Pm1004vMonOther_ObjectIdentity = ObjectIdentity
pm1004vMonOther = _Pm1004vMonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 1)
)
_Pm1004vMonRmon_ObjectIdentity = ObjectIdentity
pm1004vMonRmon = _Pm1004vMonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 1, 3)
)
_Pm1004vMonCountersReset_Type = EkiOnOff
_Pm1004vMonCountersReset_Object = MibScalar
pm1004vMonCountersReset = _Pm1004vMonCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 1, 3, 359),
    _Pm1004vMonCountersReset_Type()
)
pm1004vMonCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vMonCountersReset.setStatus("current")
_Pm1004vMonCountersStop_Type = EkiOnOff
_Pm1004vMonCountersStop_Object = MibScalar
pm1004vMonCountersStop = _Pm1004vMonCountersStop_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 1, 3, 360),
    _Pm1004vMonCountersStop_Type()
)
pm1004vMonCountersStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm1004vMonCountersStop.setStatus("current")
_Pm1004vMonClient_ObjectIdentity = ObjectIdentity
pm1004vMonClient = _Pm1004vMonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2)
)
_Pm1004vMonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm1004vMonClientRmonCounter = _Pm1004vMonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4)
)
_Pm1004vMonupRmonByteCntTable_Object = MibTable
pm1004vMonupRmonByteCntTable = _Pm1004vMonupRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonByteCntTable.setStatus("current")
_Pm1004vMonupRmonByteCntEntry_Object = MibTableRow
pm1004vMonupRmonByteCntEntry = _Pm1004vMonupRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 16, 1)
)
pm1004vMonupRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonByteCntEntry.setStatus("current")


class _Pm1004vMonupRmonByteCntIndex_Type(Integer32):
    """Custom type pm1004vMonupRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupRmonByteCntIndex_Object = MibTableColumn
pm1004vMonupRmonByteCntIndex = _Pm1004vMonupRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 16, 1, 1),
    _Pm1004vMonupRmonByteCntIndex_Type()
)
pm1004vMonupRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonByteCntIndex.setStatus("current")
_Pm1004vMonupRmonByteCntValuePortn_Type = Counter64
_Pm1004vMonupRmonByteCntValuePortn_Object = MibTableColumn
pm1004vMonupRmonByteCntValuePortn = _Pm1004vMonupRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 16, 1, 2),
    _Pm1004vMonupRmonByteCntValuePortn_Type()
)
pm1004vMonupRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonByteCntValuePortn.setStatus("current")
_Pm1004vMonupRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupRmonByteCntErrorPortn_Object = MibTableColumn
pm1004vMonupRmonByteCntErrorPortn = _Pm1004vMonupRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 16, 1, 3),
    _Pm1004vMonupRmonByteCntErrorPortn_Type()
)
pm1004vMonupRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonByteCntErrorPortn.setStatus("current")
_Pm1004vMonupRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupRmonByteCntOverloadPortn_Object = MibTableColumn
pm1004vMonupRmonByteCntOverloadPortn = _Pm1004vMonupRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 16, 1, 4),
    _Pm1004vMonupRmonByteCntOverloadPortn_Type()
)
pm1004vMonupRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonByteCntOverloadPortn.setStatus("current")
_Pm1004vMonupRmonCrcErrorCntTable_Object = MibTable
pm1004vMonupRmonCrcErrorCntTable = _Pm1004vMonupRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 24)
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonCrcErrorCntTable.setStatus("current")
_Pm1004vMonupRmonCrcErrorCntEntry_Object = MibTableRow
pm1004vMonupRmonCrcErrorCntEntry = _Pm1004vMonupRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 24, 1)
)
pm1004vMonupRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonCrcErrorCntEntry.setStatus("current")


class _Pm1004vMonupRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1004vMonupRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupRmonCrcErrorCntIndex_Object = MibTableColumn
pm1004vMonupRmonCrcErrorCntIndex = _Pm1004vMonupRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 24, 1, 1),
    _Pm1004vMonupRmonCrcErrorCntIndex_Type()
)
pm1004vMonupRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonCrcErrorCntIndex.setStatus("current")
_Pm1004vMonupRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1004vMonupRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1004vMonupRmonCrcErrorCntValuePortn = _Pm1004vMonupRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 24, 1, 2),
    _Pm1004vMonupRmonCrcErrorCntValuePortn_Type()
)
pm1004vMonupRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1004vMonupRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1004vMonupRmonCrcErrorCntErrorPortn = _Pm1004vMonupRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 24, 1, 3),
    _Pm1004vMonupRmonCrcErrorCntErrorPortn_Type()
)
pm1004vMonupRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1004vMonupRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1004vMonupRmonCrcErrorCntOverloadPortn = _Pm1004vMonupRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 24, 1, 4),
    _Pm1004vMonupRmonCrcErrorCntOverloadPortn_Type()
)
pm1004vMonupRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1004vMonupRmonPacketsCntTable_Object = MibTable
pm1004vMonupRmonPacketsCntTable = _Pm1004vMonupRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 32)
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonPacketsCntTable.setStatus("current")
_Pm1004vMonupRmonPacketsCntEntry_Object = MibTableRow
pm1004vMonupRmonPacketsCntEntry = _Pm1004vMonupRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 32, 1)
)
pm1004vMonupRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonPacketsCntEntry.setStatus("current")


class _Pm1004vMonupRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1004vMonupRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupRmonPacketsCntIndex_Object = MibTableColumn
pm1004vMonupRmonPacketsCntIndex = _Pm1004vMonupRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 32, 1, 1),
    _Pm1004vMonupRmonPacketsCntIndex_Type()
)
pm1004vMonupRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonPacketsCntIndex.setStatus("current")
_Pm1004vMonupRmonPacketsCntValuePortn_Type = Counter64
_Pm1004vMonupRmonPacketsCntValuePortn_Object = MibTableColumn
pm1004vMonupRmonPacketsCntValuePortn = _Pm1004vMonupRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 32, 1, 2),
    _Pm1004vMonupRmonPacketsCntValuePortn_Type()
)
pm1004vMonupRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonPacketsCntValuePortn.setStatus("current")
_Pm1004vMonupRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1004vMonupRmonPacketsCntErrorPortn = _Pm1004vMonupRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 32, 1, 3),
    _Pm1004vMonupRmonPacketsCntErrorPortn_Type()
)
pm1004vMonupRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonPacketsCntErrorPortn.setStatus("current")
_Pm1004vMonupRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1004vMonupRmonPacketsCntOverloadPortn = _Pm1004vMonupRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 32, 1, 4),
    _Pm1004vMonupRmonPacketsCntOverloadPortn_Type()
)
pm1004vMonupRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1004vMonupRmonBroadcastCntTable_Object = MibTable
pm1004vMonupRmonBroadcastCntTable = _Pm1004vMonupRmonBroadcastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 40)
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonBroadcastCntTable.setStatus("current")
_Pm1004vMonupRmonBroadcastCntEntry_Object = MibTableRow
pm1004vMonupRmonBroadcastCntEntry = _Pm1004vMonupRmonBroadcastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 40, 1)
)
pm1004vMonupRmonBroadcastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupRmonBroadcastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonBroadcastCntEntry.setStatus("current")


class _Pm1004vMonupRmonBroadcastCntIndex_Type(Integer32):
    """Custom type pm1004vMonupRmonBroadcastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupRmonBroadcastCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupRmonBroadcastCntIndex_Object = MibTableColumn
pm1004vMonupRmonBroadcastCntIndex = _Pm1004vMonupRmonBroadcastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 40, 1, 1),
    _Pm1004vMonupRmonBroadcastCntIndex_Type()
)
pm1004vMonupRmonBroadcastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonBroadcastCntIndex.setStatus("current")
_Pm1004vMonupRmonBroadcastCntValuePortn_Type = Counter64
_Pm1004vMonupRmonBroadcastCntValuePortn_Object = MibTableColumn
pm1004vMonupRmonBroadcastCntValuePortn = _Pm1004vMonupRmonBroadcastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 40, 1, 2),
    _Pm1004vMonupRmonBroadcastCntValuePortn_Type()
)
pm1004vMonupRmonBroadcastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonBroadcastCntValuePortn.setStatus("current")
_Pm1004vMonupRmonBroadcastCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupRmonBroadcastCntErrorPortn_Object = MibTableColumn
pm1004vMonupRmonBroadcastCntErrorPortn = _Pm1004vMonupRmonBroadcastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 40, 1, 3),
    _Pm1004vMonupRmonBroadcastCntErrorPortn_Type()
)
pm1004vMonupRmonBroadcastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonBroadcastCntErrorPortn.setStatus("current")
_Pm1004vMonupRmonBroadcastCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupRmonBroadcastCntOverloadPortn_Object = MibTableColumn
pm1004vMonupRmonBroadcastCntOverloadPortn = _Pm1004vMonupRmonBroadcastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 40, 1, 4),
    _Pm1004vMonupRmonBroadcastCntOverloadPortn_Type()
)
pm1004vMonupRmonBroadcastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonBroadcastCntOverloadPortn.setStatus("current")
_Pm1004vMonupRmonMulticastCntTable_Object = MibTable
pm1004vMonupRmonMulticastCntTable = _Pm1004vMonupRmonMulticastCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonMulticastCntTable.setStatus("current")
_Pm1004vMonupRmonMulticastCntEntry_Object = MibTableRow
pm1004vMonupRmonMulticastCntEntry = _Pm1004vMonupRmonMulticastCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 48, 1)
)
pm1004vMonupRmonMulticastCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupRmonMulticastCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupRmonMulticastCntEntry.setStatus("current")


class _Pm1004vMonupRmonMulticastCntIndex_Type(Integer32):
    """Custom type pm1004vMonupRmonMulticastCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupRmonMulticastCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupRmonMulticastCntIndex_Object = MibTableColumn
pm1004vMonupRmonMulticastCntIndex = _Pm1004vMonupRmonMulticastCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 48, 1, 1),
    _Pm1004vMonupRmonMulticastCntIndex_Type()
)
pm1004vMonupRmonMulticastCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonMulticastCntIndex.setStatus("current")
_Pm1004vMonupRmonMulticastCntValuePortn_Type = Counter64
_Pm1004vMonupRmonMulticastCntValuePortn_Object = MibTableColumn
pm1004vMonupRmonMulticastCntValuePortn = _Pm1004vMonupRmonMulticastCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 48, 1, 2),
    _Pm1004vMonupRmonMulticastCntValuePortn_Type()
)
pm1004vMonupRmonMulticastCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonMulticastCntValuePortn.setStatus("current")
_Pm1004vMonupRmonMulticastCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupRmonMulticastCntErrorPortn_Object = MibTableColumn
pm1004vMonupRmonMulticastCntErrorPortn = _Pm1004vMonupRmonMulticastCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 48, 1, 3),
    _Pm1004vMonupRmonMulticastCntErrorPortn_Type()
)
pm1004vMonupRmonMulticastCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonMulticastCntErrorPortn.setStatus("current")
_Pm1004vMonupRmonMulticastCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupRmonMulticastCntOverloadPortn_Object = MibTableColumn
pm1004vMonupRmonMulticastCntOverloadPortn = _Pm1004vMonupRmonMulticastCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 48, 1, 4),
    _Pm1004vMonupRmonMulticastCntOverloadPortn_Type()
)
pm1004vMonupRmonMulticastCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupRmonMulticastCntOverloadPortn.setStatus("current")
_Pm1004vMonupLineRmonByteCntTable_Object = MibTable
pm1004vMonupLineRmonByteCntTable = _Pm1004vMonupLineRmonByteCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 208)
)
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonByteCntTable.setStatus("current")
_Pm1004vMonupLineRmonByteCntEntry_Object = MibTableRow
pm1004vMonupLineRmonByteCntEntry = _Pm1004vMonupLineRmonByteCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 208, 1)
)
pm1004vMonupLineRmonByteCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupLineRmonByteCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonByteCntEntry.setStatus("current")


class _Pm1004vMonupLineRmonByteCntIndex_Type(Integer32):
    """Custom type pm1004vMonupLineRmonByteCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupLineRmonByteCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupLineRmonByteCntIndex_Object = MibTableColumn
pm1004vMonupLineRmonByteCntIndex = _Pm1004vMonupLineRmonByteCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 208, 1, 1),
    _Pm1004vMonupLineRmonByteCntIndex_Type()
)
pm1004vMonupLineRmonByteCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonByteCntIndex.setStatus("current")
_Pm1004vMonupLineRmonByteCntValuePortn_Type = Counter64
_Pm1004vMonupLineRmonByteCntValuePortn_Object = MibTableColumn
pm1004vMonupLineRmonByteCntValuePortn = _Pm1004vMonupLineRmonByteCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 208, 1, 2),
    _Pm1004vMonupLineRmonByteCntValuePortn_Type()
)
pm1004vMonupLineRmonByteCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonByteCntValuePortn.setStatus("current")
_Pm1004vMonupLineRmonByteCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupLineRmonByteCntErrorPortn_Object = MibTableColumn
pm1004vMonupLineRmonByteCntErrorPortn = _Pm1004vMonupLineRmonByteCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 208, 1, 3),
    _Pm1004vMonupLineRmonByteCntErrorPortn_Type()
)
pm1004vMonupLineRmonByteCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonByteCntErrorPortn.setStatus("current")
_Pm1004vMonupLineRmonByteCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupLineRmonByteCntOverloadPortn_Object = MibTableColumn
pm1004vMonupLineRmonByteCntOverloadPortn = _Pm1004vMonupLineRmonByteCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 208, 1, 4),
    _Pm1004vMonupLineRmonByteCntOverloadPortn_Type()
)
pm1004vMonupLineRmonByteCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonByteCntOverloadPortn.setStatus("current")
_Pm1004vMonupLineRmonCrcErrorCntTable_Object = MibTable
pm1004vMonupLineRmonCrcErrorCntTable = _Pm1004vMonupLineRmonCrcErrorCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 209)
)
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonCrcErrorCntTable.setStatus("current")
_Pm1004vMonupLineRmonCrcErrorCntEntry_Object = MibTableRow
pm1004vMonupLineRmonCrcErrorCntEntry = _Pm1004vMonupLineRmonCrcErrorCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 209, 1)
)
pm1004vMonupLineRmonCrcErrorCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupLineRmonCrcErrorCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonCrcErrorCntEntry.setStatus("current")


class _Pm1004vMonupLineRmonCrcErrorCntIndex_Type(Integer32):
    """Custom type pm1004vMonupLineRmonCrcErrorCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupLineRmonCrcErrorCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupLineRmonCrcErrorCntIndex_Object = MibTableColumn
pm1004vMonupLineRmonCrcErrorCntIndex = _Pm1004vMonupLineRmonCrcErrorCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 209, 1, 1),
    _Pm1004vMonupLineRmonCrcErrorCntIndex_Type()
)
pm1004vMonupLineRmonCrcErrorCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonCrcErrorCntIndex.setStatus("current")
_Pm1004vMonupLineRmonCrcErrorCntValuePortn_Type = Counter64
_Pm1004vMonupLineRmonCrcErrorCntValuePortn_Object = MibTableColumn
pm1004vMonupLineRmonCrcErrorCntValuePortn = _Pm1004vMonupLineRmonCrcErrorCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 209, 1, 2),
    _Pm1004vMonupLineRmonCrcErrorCntValuePortn_Type()
)
pm1004vMonupLineRmonCrcErrorCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonCrcErrorCntValuePortn.setStatus("current")
_Pm1004vMonupLineRmonCrcErrorCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupLineRmonCrcErrorCntErrorPortn_Object = MibTableColumn
pm1004vMonupLineRmonCrcErrorCntErrorPortn = _Pm1004vMonupLineRmonCrcErrorCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 209, 1, 3),
    _Pm1004vMonupLineRmonCrcErrorCntErrorPortn_Type()
)
pm1004vMonupLineRmonCrcErrorCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonCrcErrorCntErrorPortn.setStatus("current")
_Pm1004vMonupLineRmonCrcErrorCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupLineRmonCrcErrorCntOverloadPortn_Object = MibTableColumn
pm1004vMonupLineRmonCrcErrorCntOverloadPortn = _Pm1004vMonupLineRmonCrcErrorCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 209, 1, 4),
    _Pm1004vMonupLineRmonCrcErrorCntOverloadPortn_Type()
)
pm1004vMonupLineRmonCrcErrorCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonCrcErrorCntOverloadPortn.setStatus("current")
_Pm1004vMonupLineRmonPacketsCntTable_Object = MibTable
pm1004vMonupLineRmonPacketsCntTable = _Pm1004vMonupLineRmonPacketsCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 210)
)
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonPacketsCntTable.setStatus("current")
_Pm1004vMonupLineRmonPacketsCntEntry_Object = MibTableRow
pm1004vMonupLineRmonPacketsCntEntry = _Pm1004vMonupLineRmonPacketsCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 210, 1)
)
pm1004vMonupLineRmonPacketsCntEntry.setIndexNames(
    (0, "EKINOPS-Pm1004V-MIB", "pm1004vMonupLineRmonPacketsCntIndex"),
)
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonPacketsCntEntry.setStatus("current")


class _Pm1004vMonupLineRmonPacketsCntIndex_Type(Integer32):
    """Custom type pm1004vMonupLineRmonPacketsCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm1004vMonupLineRmonPacketsCntIndex_Type.__name__ = "Integer32"
_Pm1004vMonupLineRmonPacketsCntIndex_Object = MibTableColumn
pm1004vMonupLineRmonPacketsCntIndex = _Pm1004vMonupLineRmonPacketsCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 210, 1, 1),
    _Pm1004vMonupLineRmonPacketsCntIndex_Type()
)
pm1004vMonupLineRmonPacketsCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonPacketsCntIndex.setStatus("current")
_Pm1004vMonupLineRmonPacketsCntValuePortn_Type = Counter64
_Pm1004vMonupLineRmonPacketsCntValuePortn_Object = MibTableColumn
pm1004vMonupLineRmonPacketsCntValuePortn = _Pm1004vMonupLineRmonPacketsCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 210, 1, 2),
    _Pm1004vMonupLineRmonPacketsCntValuePortn_Type()
)
pm1004vMonupLineRmonPacketsCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonPacketsCntValuePortn.setStatus("current")
_Pm1004vMonupLineRmonPacketsCntErrorPortn_Type = EkiOnOff
_Pm1004vMonupLineRmonPacketsCntErrorPortn_Object = MibTableColumn
pm1004vMonupLineRmonPacketsCntErrorPortn = _Pm1004vMonupLineRmonPacketsCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 210, 1, 3),
    _Pm1004vMonupLineRmonPacketsCntErrorPortn_Type()
)
pm1004vMonupLineRmonPacketsCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonPacketsCntErrorPortn.setStatus("current")
_Pm1004vMonupLineRmonPacketsCntOverloadPortn_Type = EkiOnOff
_Pm1004vMonupLineRmonPacketsCntOverloadPortn_Object = MibTableColumn
pm1004vMonupLineRmonPacketsCntOverloadPortn = _Pm1004vMonupLineRmonPacketsCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 2, 4, 210, 1, 4),
    _Pm1004vMonupLineRmonPacketsCntOverloadPortn_Type()
)
pm1004vMonupLineRmonPacketsCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1004vMonupLineRmonPacketsCntOverloadPortn.setStatus("current")
_Pm1004vMonLine_ObjectIdentity = ObjectIdentity
pm1004vMonLine = _Pm1004vMonLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 3)
)
_Pm1004vMonLineRmonCounter_ObjectIdentity = ObjectIdentity
pm1004vMonLineRmonCounter = _Pm1004vMonLineRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 32, 11, 3, 4)
)

# Managed Objects groups


# Notification objects

pm1004vLineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 30)
)
pm1004vLineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapLineNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vLineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004vLineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 31)
)
pm1004vLineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineDdmWarningPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapLineNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vLineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004vLineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 32)
)
pm1004vLineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapLineNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vLineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vLineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 33)
)
pm1004vLineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineDdmAlmPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapLineNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vLineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004vLineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 34)
)
pm1004vLineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineFailPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapLineNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vLineTrapCritGoesOn.setStatus(
        "current"
    )

pm1004vLineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 35)
)
pm1004vLineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineFailPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vAlmLineHwFailPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapLineNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vLineTrapCritGoesOff.setStatus(
        "current"
    )

pm1004vClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 40)
)
pm1004vClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapPortNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm1004vClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 41)
)
pm1004vClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapPortNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm1004vClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 42)
)
pm1004vClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapPortNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 43)
)
pm1004vClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapPortNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm1004vClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 44)
)
pm1004vClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmFailAccPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapPortNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vClientTrapCritGoesOn.setStatus(
        "current"
    )

pm1004vClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 45)
)
pm1004vClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmFailAccPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vAlmHwFailAccPortn"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapPortNumber"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vClientTrapCritGoesOff.setStatus(
        "current"
    )

pm1004vPowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 50)
)
pm1004vPowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmDefFuseB"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vAlmDefFuseA"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vPowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm1004vPowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 32, 10, 51)
)
pm1004vPowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm1004V-MIB", "pm1004vAlmDefFuseB"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vAlmDefFuseA"),
        ("EKINOPS-Pm1004V-MIB", "pm1004vtrapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm1004vPowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm1004V-MIB",
    **{"Pm1004vModeTimeSlot": Pm1004vModeTimeSlot,
       "Pm1004vModeAddDrop": Pm1004vModeAddDrop,
       "Pm1004vProtectionTimeSlot": Pm1004vProtectionTimeSlot,
       "Pm1004vProtectionStartUp": Pm1004vProtectionStartUp,
       "Pm1004vDccMode": Pm1004vDccMode,
       "Pm1004vClientOosMode": Pm1004vClientOosMode,
       "Pm1004vOtxMode": Pm1004vOtxMode,
       "Pm1004vOtxGrid": Pm1004vOtxGrid,
       "Pm1004vAdjustValue": Pm1004vAdjustValue,
       "Pm1004vOtxChannel": Pm1004vOtxChannel,
       "modulePm1004v": modulePm1004v,
       "pm1004valarms": pm1004valarms,
       "pm1004vAlmOther": pm1004vAlmOther,
       "pm1004vAlmOtherNurg": pm1004vAlmOtherNurg,
       "pm1004vAlmsynthAlm2": pm1004vAlmsynthAlm2,
       "pm1004vAlmConfTableSave": pm1004vAlmConfTableSave,
       "pm1004vAlmInvUpload": pm1004vAlmInvUpload,
       "pm1004vAlmConfTableLoad": pm1004vAlmConfTableLoad,
       "pm1004vAlmCorrelatOff": pm1004vAlmCorrelatOff,
       "pm1004vAlmMaintenanceOn": pm1004vAlmMaintenanceOn,
       "pm1004vAlmOtherUrg": pm1004vAlmOtherUrg,
       "pm1004vAlmmodInitFailLevel2": pm1004vAlmmodInitFailLevel2,
       "pm1004vAlmLedFail": pm1004vAlmLedFail,
       "pm1004vAlmNextColdBootForced": pm1004vAlmNextColdBootForced,
       "pm1004vAlmBootUndone": pm1004vAlmBootUndone,
       "pm1004vAlmResetHwInitFail": pm1004vAlmResetHwInitFail,
       "pm1004vAlmSwInitFail": pm1004vAlmSwInitFail,
       "pm1004vAlmmodInitFailLevel3": pm1004vAlmmodInitFailLevel3,
       "pm1004vAlmGwIdentFail": pm1004vAlmGwIdentFail,
       "pm1004vAlmObmTypeReadFail": pm1004vAlmObmTypeReadFail,
       "pm1004vAlmInitModuleFail": pm1004vAlmInitModuleFail,
       "pm1004vAlmXfp1InitFail": pm1004vAlmXfp1InitFail,
       "pm1004vAlmXfp2InitFail": pm1004vAlmXfp2InitFail,
       "pm1004vAlmLine1InitFail": pm1004vAlmLine1InitFail,
       "pm1004vAlmLine2InitFail": pm1004vAlmLine2InitFail,
       "pm1004vAlmClient1InitFail": pm1004vAlmClient1InitFail,
       "pm1004vAlmClient2InitFail": pm1004vAlmClient2InitFail,
       "pm1004vAlmClient3InitFail": pm1004vAlmClient3InitFail,
       "pm1004vAlmClient4InitFail": pm1004vAlmClient4InitFail,
       "pm1004vAlmClient5InitFail": pm1004vAlmClient5InitFail,
       "pm1004vAlmClient6InitFail": pm1004vAlmClient6InitFail,
       "pm1004vAlmclientRxProt": pm1004vAlmclientRxProt,
       "pm1004vAlmAdddropClient1West": pm1004vAlmAdddropClient1West,
       "pm1004vAlmAdddropClient2West": pm1004vAlmAdddropClient2West,
       "pm1004vAlmAdddropClient3West": pm1004vAlmAdddropClient3West,
       "pm1004vAlmAdddropClient4West": pm1004vAlmAdddropClient4West,
       "pm1004vAlmAdddropClient5West": pm1004vAlmAdddropClient5West,
       "pm1004vAlmAdddropClient6West": pm1004vAlmAdddropClient6West,
       "pm1004vAlmAdddropClient1East": pm1004vAlmAdddropClient1East,
       "pm1004vAlmAdddropClient2East": pm1004vAlmAdddropClient2East,
       "pm1004vAlmAdddropClient3East": pm1004vAlmAdddropClient3East,
       "pm1004vAlmAdddropClient4East": pm1004vAlmAdddropClient4East,
       "pm1004vAlmAdddropClient5East": pm1004vAlmAdddropClient5East,
       "pm1004vAlmAdddropClient6East": pm1004vAlmAdddropClient6East,
       "pm1004vAlmOtherCrit": pm1004vAlmOtherCrit,
       "pm1004vAlmsynthAlm0": pm1004vAlmsynthAlm0,
       "pm1004vAlmModGlobFail": pm1004vAlmModGlobFail,
       "pm1004vAlmDefFuseA": pm1004vAlmDefFuseA,
       "pm1004vAlmDefFuseB": pm1004vAlmDefFuseB,
       "pm1004vAlmClient": pm1004vAlmClient,
       "pm1004vAlmClientNurg": pm1004vAlmClientNurg,
       "pm1004vAlmsfpWarnDdmTable": pm1004vAlmsfpWarnDdmTable,
       "pm1004vAlmsfpWarnDdmEntry": pm1004vAlmsfpWarnDdmEntry,
       "pm1004vAlmsfpWarnDdmIndex": pm1004vAlmsfpWarnDdmIndex,
       "pm1004vAlmTxPwLowWngPortn": pm1004vAlmTxPwLowWngPortn,
       "pm1004vAlmTxPwrHighWngPortn": pm1004vAlmTxPwrHighWngPortn,
       "pm1004vAlmTxBiasLowWngPortn": pm1004vAlmTxBiasLowWngPortn,
       "pm1004vAlmTxBiasHighWngPortn": pm1004vAlmTxBiasHighWngPortn,
       "pm1004vAlmVccLowWngPortn": pm1004vAlmVccLowWngPortn,
       "pm1004vAlmVccHighWngPortn": pm1004vAlmVccHighWngPortn,
       "pm1004vAlmTempLowWngPortn": pm1004vAlmTempLowWngPortn,
       "pm1004vAlmTempHighWngPortn": pm1004vAlmTempHighWngPortn,
       "pm1004vAlmRxPwrLowWngPortn": pm1004vAlmRxPwrLowWngPortn,
       "pm1004vAlmRxPwrHighWngPortn": pm1004vAlmRxPwrHighWngPortn,
       "pm1004vAlmsfpCritDdmTable": pm1004vAlmsfpCritDdmTable,
       "pm1004vAlmsfpCritDdmEntry": pm1004vAlmsfpCritDdmEntry,
       "pm1004vAlmsfpCritDdmIndex": pm1004vAlmsfpCritDdmIndex,
       "pm1004vAlmTxPwrLowCritPortn": pm1004vAlmTxPwrLowCritPortn,
       "pm1004vAlmTxPwrHighCritPortn": pm1004vAlmTxPwrHighCritPortn,
       "pm1004vAlmRxPwrLowCritPortn": pm1004vAlmRxPwrLowCritPortn,
       "pm1004vAlmRxPwrHighCritPortn": pm1004vAlmRxPwrHighCritPortn,
       "pm1004vAlmClientUrg": pm1004vAlmClientUrg,
       "pm1004vAlmsfpAlmDdmTable": pm1004vAlmsfpAlmDdmTable,
       "pm1004vAlmsfpAlmDdmEntry": pm1004vAlmsfpAlmDdmEntry,
       "pm1004vAlmsfpAlmDdmIndex": pm1004vAlmsfpAlmDdmIndex,
       "pm1004vAlmTxPwrLowAlaPortn": pm1004vAlmTxPwrLowAlaPortn,
       "pm1004vAlmTxPwrHighAlaPortn": pm1004vAlmTxPwrHighAlaPortn,
       "pm1004vAlmTxBiasLowAlaPortn": pm1004vAlmTxBiasLowAlaPortn,
       "pm1004vAlmTxBiasHighAlaPortn": pm1004vAlmTxBiasHighAlaPortn,
       "pm1004vAlmVccLowAlaPortn": pm1004vAlmVccLowAlaPortn,
       "pm1004vAlmVccHighAlaPortn": pm1004vAlmVccHighAlaPortn,
       "pm1004vAlmTempLowAlaPortn": pm1004vAlmTempLowAlaPortn,
       "pm1004vAlmTempHighAlaPortn": pm1004vAlmTempHighAlaPortn,
       "pm1004vAlmRxPwrLowAlaPortn": pm1004vAlmRxPwrLowAlaPortn,
       "pm1004vAlmRxPwrHighAlaPortn": pm1004vAlmRxPwrHighAlaPortn,
       "pm1004vAlmClientCrit": pm1004vAlmClientCrit,
       "pm1004vAlmsynthAlmPortTable": pm1004vAlmsynthAlmPortTable,
       "pm1004vAlmsynthAlmPortEntry": pm1004vAlmsynthAlmPortEntry,
       "pm1004vAlmsynthAlmPortIndex": pm1004vAlmsynthAlmPortIndex,
       "pm1004vAlmSfpAbsentPortn": pm1004vAlmSfpAbsentPortn,
       "pm1004vAlmDdmAbsentPortn": pm1004vAlmDdmAbsentPortn,
       "pm1004vAlmHwFailAccPortn": pm1004vAlmHwFailAccPortn,
       "pm1004vAlmDwLsdPortn": pm1004vAlmDwLsdPortn,
       "pm1004vAlmClientLocalOosTxPortn": pm1004vAlmClientLocalOosTxPortn,
       "pm1004vAlmClientLocalOosRxPortn": pm1004vAlmClientLocalOosRxPortn,
       "pm1004vAlmDwCaisPortn": pm1004vAlmDwCaisPortn,
       "pm1004vAlmSfpDdmWarningPortn": pm1004vAlmSfpDdmWarningPortn,
       "pm1004vAlmSfpDdmAlmPortn": pm1004vAlmSfpDdmAlmPortn,
       "pm1004vAlmSfpDdmCritPortn": pm1004vAlmSfpDdmCritPortn,
       "pm1004vAlmFailAccPortn": pm1004vAlmFailAccPortn,
       "pm1004vAlmClientActivePortn": pm1004vAlmClientActivePortn,
       "pm1004vAlmUpCsfPortn": pm1004vAlmUpCsfPortn,
       "pm1004vAlmaccessioAlmTable": pm1004vAlmaccessioAlmTable,
       "pm1004vAlmaccessioAlmEntry": pm1004vAlmaccessioAlmEntry,
       "pm1004vAlmaccessioAlmIndex": pm1004vAlmaccessioAlmIndex,
       "pm1004vAlmDwLasFailPortn": pm1004vAlmDwLasFailPortn,
       "pm1004vAlmUpLosPortn": pm1004vAlmUpLosPortn,
       "pm1004vAlmmapperDeAlmTable": pm1004vAlmmapperDeAlmTable,
       "pm1004vAlmmapperDeAlmEntry": pm1004vAlmmapperDeAlmEntry,
       "pm1004vAlmmapperDeAlmIndex": pm1004vAlmmapperDeAlmIndex,
       "pm1004vAlmUpAccOosPortn": pm1004vAlmUpAccOosPortn,
       "pm1004vAlmUpBufferOvlPortn": pm1004vAlmUpBufferOvlPortn,
       "pm1004vAlmDwCsfDetPortn": pm1004vAlmDwCsfDetPortn,
       "pm1004vAlmDwBufferOvlPortn": pm1004vAlmDwBufferOvlPortn,
       "pm1004vAlmvideoProtocolStatusTable": pm1004vAlmvideoProtocolStatusTable,
       "pm1004vAlmvideoProtocolStatusEntry": pm1004vAlmvideoProtocolStatusEntry,
       "pm1004vAlmvideoProtocolStatusIndex": pm1004vAlmvideoProtocolStatusIndex,
       "pm1004vAlmSdiTxPortn": pm1004vAlmSdiTxPortn,
       "pm1004vAlmHdSdiPalTxPortn": pm1004vAlmHdSdiPalTxPortn,
       "pm1004vAlmHdSdiNtscTxPortn": pm1004vAlmHdSdiNtscTxPortn,
       "pm1004vAlmDvbAsiTxPortn": pm1004vAlmDvbAsiTxPortn,
       "pm1004vAlmFastEtherTxPortn": pm1004vAlmFastEtherTxPortn,
       "pm1004vAlmGbeTxPortn": pm1004vAlmGbeTxPortn,
       "pm1004vAlmSdiRxPortn": pm1004vAlmSdiRxPortn,
       "pm1004vAlmHdSdiPalRxPortn": pm1004vAlmHdSdiPalRxPortn,
       "pm1004vAlmHdSdiNtscRxPortn": pm1004vAlmHdSdiNtscRxPortn,
       "pm1004vAlmDvbAsiRxPortn": pm1004vAlmDvbAsiRxPortn,
       "pm1004vAlmFastEtherRxPortn": pm1004vAlmFastEtherRxPortn,
       "pm1004vAlmGbeRxPortn": pm1004vAlmGbeRxPortn,
       "pm1004vAlmLine": pm1004vAlmLine,
       "pm1004vAlmLineNurg": pm1004vAlmLineNurg,
       "pm1004vAlmlineXfp1WarningsTable": pm1004vAlmlineXfp1WarningsTable,
       "pm1004vAlmlineXfp1WarningsEntry": pm1004vAlmlineXfp1WarningsEntry,
       "pm1004vAlmlineXfp1WarningsIndex": pm1004vAlmlineXfp1WarningsIndex,
       "pm1004vAlmTxPowerLowWarningPortn": pm1004vAlmTxPowerLowWarningPortn,
       "pm1004vAlmTxPowerHighWarningPortn": pm1004vAlmTxPowerHighWarningPortn,
       "pm1004vAlmTxBiasLowWarningPortn": pm1004vAlmTxBiasLowWarningPortn,
       "pm1004vAlmTxBiasHighWarningPortn": pm1004vAlmTxBiasHighWarningPortn,
       "pm1004vAlmTempLowWarningPortn": pm1004vAlmTempLowWarningPortn,
       "pm1004vAlmTempHighWarningPortn": pm1004vAlmTempHighWarningPortn,
       "pm1004vAlmRxPowerLowWarningPortn": pm1004vAlmRxPowerLowWarningPortn,
       "pm1004vAlmRxPowerHighWarningPortn": pm1004vAlmRxPowerHighWarningPortn,
       "pm1004vAlmlineOtx1TlhWarningsTable": pm1004vAlmlineOtx1TlhWarningsTable,
       "pm1004vAlmlineOtx1TlhWarningsEntry": pm1004vAlmlineOtx1TlhWarningsEntry,
       "pm1004vAlmlineOtx1TlhWarningsIndex": pm1004vAlmlineOtx1TlhWarningsIndex,
       "pm1004vAlmLineModulatorAgingHighWarningPortn": pm1004vAlmLineModulatorAgingHighWarningPortn,
       "pm1004vAlmLineAgingHighWarningPortn": pm1004vAlmLineAgingHighWarningPortn,
       "pm1004vAlmLineFreqDevHighWarningPortn": pm1004vAlmLineFreqDevHighWarningPortn,
       "pm1004vAlmLineLaserTempHighWarningPortn": pm1004vAlmLineLaserTempHighWarningPortn,
       "pm1004vAlmLineUrg": pm1004vAlmLineUrg,
       "pm1004vAlmlineXfp1AlarmTable": pm1004vAlmlineXfp1AlarmTable,
       "pm1004vAlmlineXfp1AlarmEntry": pm1004vAlmlineXfp1AlarmEntry,
       "pm1004vAlmlineXfp1AlarmIndex": pm1004vAlmlineXfp1AlarmIndex,
       "pm1004vAlmTxPowerLowAlarmPortn": pm1004vAlmTxPowerLowAlarmPortn,
       "pm1004vAlmTxPowerHighAlarmPortn": pm1004vAlmTxPowerHighAlarmPortn,
       "pm1004vAlmTxBiasLowAlarmPortn": pm1004vAlmTxBiasLowAlarmPortn,
       "pm1004vAlmTxBiasHighAlarmPortn": pm1004vAlmTxBiasHighAlarmPortn,
       "pm1004vAlmTempLowAlarmPortn": pm1004vAlmTempLowAlarmPortn,
       "pm1004vAlmTempHighAlarmPortn": pm1004vAlmTempHighAlarmPortn,
       "pm1004vAlmRxPowerLowAlarmPortn": pm1004vAlmRxPowerLowAlarmPortn,
       "pm1004vAlmRxPowerHighAlarmPortn": pm1004vAlmRxPowerHighAlarmPortn,
       "pm1004vAlmlineXfp1CritTable": pm1004vAlmlineXfp1CritTable,
       "pm1004vAlmlineXfp1CritEntry": pm1004vAlmlineXfp1CritEntry,
       "pm1004vAlmlineXfp1CritIndex": pm1004vAlmlineXfp1CritIndex,
       "pm1004vAlmTxPowerLowCritPortn": pm1004vAlmTxPowerLowCritPortn,
       "pm1004vAlmTxPowerHighCritPortn": pm1004vAlmTxPowerHighCritPortn,
       "pm1004vAlmRxPowerLowCritPortn": pm1004vAlmRxPowerLowCritPortn,
       "pm1004vAlmRxPowerHighCritPortn": pm1004vAlmRxPowerHighCritPortn,
       "pm1004vAlmlineXfp1SupplyAlarmTable": pm1004vAlmlineXfp1SupplyAlarmTable,
       "pm1004vAlmlineXfp1SupplyAlarmEntry": pm1004vAlmlineXfp1SupplyAlarmEntry,
       "pm1004vAlmlineXfp1SupplyAlarmIndex": pm1004vAlmlineXfp1SupplyAlarmIndex,
       "pm1004vAlmVee5LowAlarmPortn": pm1004vAlmVee5LowAlarmPortn,
       "pm1004vAlmVee5HighAlarmPortn": pm1004vAlmVee5HighAlarmPortn,
       "pm1004vAlmVcc2LowAlarmPortn": pm1004vAlmVcc2LowAlarmPortn,
       "pm1004vAlmVcc2HighAlarmPortn": pm1004vAlmVcc2HighAlarmPortn,
       "pm1004vAlmVcc3LowAlarmPortn": pm1004vAlmVcc3LowAlarmPortn,
       "pm1004vAlmVcc3HighAlarmPortn": pm1004vAlmVcc3HighAlarmPortn,
       "pm1004vAlmVcc5LowAlarmPortn": pm1004vAlmVcc5LowAlarmPortn,
       "pm1004vAlmVcc5HighAlarmPortn": pm1004vAlmVcc5HighAlarmPortn,
       "pm1004vAlmVee5LowWarningPortn": pm1004vAlmVee5LowWarningPortn,
       "pm1004vAlmVee5HighWarningPortn": pm1004vAlmVee5HighWarningPortn,
       "pm1004vAlmVcc2LowWarningPortn": pm1004vAlmVcc2LowWarningPortn,
       "pm1004vAlmVcc2HighWarningPortn": pm1004vAlmVcc2HighWarningPortn,
       "pm1004vAlmVcc3LowWarningPortn": pm1004vAlmVcc3LowWarningPortn,
       "pm1004vAlmVcc3HighWarningPortn": pm1004vAlmVcc3HighWarningPortn,
       "pm1004vAlmVcc5LowWarningPortn": pm1004vAlmVcc5LowWarningPortn,
       "pm1004vAlmVcc5HighWarningPortn": pm1004vAlmVcc5HighWarningPortn,
       "pm1004vAlmlineOtx1TlhAlarmsTable": pm1004vAlmlineOtx1TlhAlarmsTable,
       "pm1004vAlmlineOtx1TlhAlarmsEntry": pm1004vAlmlineOtx1TlhAlarmsEntry,
       "pm1004vAlmlineOtx1TlhAlarmsIndex": pm1004vAlmlineOtx1TlhAlarmsIndex,
       "pm1004vAlmLineModulatorAgingHighAlaPortn": pm1004vAlmLineModulatorAgingHighAlaPortn,
       "pm1004vAlmLineAgingHighAlaPortn": pm1004vAlmLineAgingHighAlaPortn,
       "pm1004vAlmLineFreqDevHighAlaPortn": pm1004vAlmLineFreqDevHighAlaPortn,
       "pm1004vAlmLineLaserTempHighAlaPortn": pm1004vAlmLineLaserTempHighAlaPortn,
       "pm1004vAlmLineCrit": pm1004vAlmLineCrit,
       "pm1004vAlmsynthAlmLineTable": pm1004vAlmsynthAlmLineTable,
       "pm1004vAlmsynthAlmLineEntry": pm1004vAlmsynthAlmLineEntry,
       "pm1004vAlmsynthAlmLineIndex": pm1004vAlmsynthAlmLineIndex,
       "pm1004vAlmXfpAbsentPortn": pm1004vAlmXfpAbsentPortn,
       "pm1004vAlmXfpInitNotComplPortn": pm1004vAlmXfpInitNotComplPortn,
       "pm1004vAlmLineHwFailPortn": pm1004vAlmLineHwFailPortn,
       "pm1004vAlmXfpTxOffPortn": pm1004vAlmXfpTxOffPortn,
       "pm1004vAlmLineLocalOosPortn": pm1004vAlmLineLocalOosPortn,
       "pm1004vAlmLineDdmWarningPortn": pm1004vAlmLineDdmWarningPortn,
       "pm1004vAlmLineDdmAlmPortn": pm1004vAlmLineDdmAlmPortn,
       "pm1004vAlmLineDdmCritPortn": pm1004vAlmLineDdmCritPortn,
       "pm1004vAlmLineFailPortn": pm1004vAlmLineFailPortn,
       "pm1004vAlmLineActivePortn": pm1004vAlmLineActivePortn,
       "pm1004vAlmdfrmAlmTable": pm1004vAlmdfrmAlmTable,
       "pm1004vAlmdfrmAlmEntry": pm1004vAlmdfrmAlmEntry,
       "pm1004vAlmdfrmAlmIndex": pm1004vAlmdfrmAlmIndex,
       "pm1004vAlmDwLossofsyncPortn": pm1004vAlmDwLossofsyncPortn,
       "pm1004vAlmlineSyncAlarmsTable": pm1004vAlmlineSyncAlarmsTable,
       "pm1004vAlmlineSyncAlarmsEntry": pm1004vAlmlineSyncAlarmsEntry,
       "pm1004vAlmlineSyncAlarmsIndex": pm1004vAlmlineSyncAlarmsIndex,
       "pm1004vAlmDwLockerrPortn": pm1004vAlmDwLockerrPortn,
       "pm1004vAlmUpLockerrPortn": pm1004vAlmUpLockerrPortn,
       "pm1004vAlmDwLosPortn": pm1004vAlmDwLosPortn,
       "pm1004vAlmlineXfp1AlarmsTable": pm1004vAlmlineXfp1AlarmsTable,
       "pm1004vAlmlineXfp1AlarmsEntry": pm1004vAlmlineXfp1AlarmsEntry,
       "pm1004vAlmlineXfp1AlarmsIndex": pm1004vAlmlineXfp1AlarmsIndex,
       "pm1004vAlmModNrPortn": pm1004vAlmModNrPortn,
       "pm1004vAlmRxCdrNotLockedPortn": pm1004vAlmRxCdrNotLockedPortn,
       "pm1004vAlmRxNrPortn": pm1004vAlmRxNrPortn,
       "pm1004vAlmTxCdrNotLockedPortn": pm1004vAlmTxCdrNotLockedPortn,
       "pm1004vAlmTxFaultPortn": pm1004vAlmTxFaultPortn,
       "pm1004vAlmTxNrPortn": pm1004vAlmTxNrPortn,
       "pm1004vAlmWavelengthUnlockedPortn": pm1004vAlmWavelengthUnlockedPortn,
       "pm1004vAlmTecFaultPortn": pm1004vAlmTecFaultPortn,
       "pm1004vAlmApdSupplyFaultPortn": pm1004vAlmApdSupplyFaultPortn,
       "pm1004vmeasures": pm1004vmeasures,
       "pm1004vMesrOther": pm1004vMesrOther,
       "pm1004vMesrsynth0": pm1004vMesrsynth0,
       "pm1004vMesrsynth1": pm1004vMesrsynth1,
       "pm1004vMesrClient": pm1004vMesrClient,
       "pm1004vMesrtempMeasTable": pm1004vMesrtempMeasTable,
       "pm1004vMesrtempMeasEntry": pm1004vMesrtempMeasEntry,
       "pm1004vMesrtempMeasIndex": pm1004vMesrtempMeasIndex,
       "pm1004vMesrtempMeasPortn": pm1004vMesrtempMeasPortn,
       "pm1004vMesrvoltMeasTable": pm1004vMesrvoltMeasTable,
       "pm1004vMesrvoltMeasEntry": pm1004vMesrvoltMeasEntry,
       "pm1004vMesrvoltMeasIndex": pm1004vMesrvoltMeasIndex,
       "pm1004vMesrvoltMeasPortn": pm1004vMesrvoltMeasPortn,
       "pm1004vMesrbiasMeasTable": pm1004vMesrbiasMeasTable,
       "pm1004vMesrbiasMeasEntry": pm1004vMesrbiasMeasEntry,
       "pm1004vMesrbiasMeasIndex": pm1004vMesrbiasMeasIndex,
       "pm1004vMesrbiasMeasPortn": pm1004vMesrbiasMeasPortn,
       "pm1004vMesrtxpwrMeasTable": pm1004vMesrtxpwrMeasTable,
       "pm1004vMesrtxpwrMeasEntry": pm1004vMesrtxpwrMeasEntry,
       "pm1004vMesrtxpwrMeasIndex": pm1004vMesrtxpwrMeasIndex,
       "pm1004vMesrtxpwrMeasPortn": pm1004vMesrtxpwrMeasPortn,
       "pm1004vMesrrxpwrMeasTable": pm1004vMesrrxpwrMeasTable,
       "pm1004vMesrrxpwrMeasEntry": pm1004vMesrrxpwrMeasEntry,
       "pm1004vMesrrxpwrMeasIndex": pm1004vMesrrxpwrMeasIndex,
       "pm1004vMesrrxpwrMeasPortn": pm1004vMesrrxpwrMeasPortn,
       "pm1004vMesrLine": pm1004vMesrLine,
       "pm1004vMesrxfp1LxModTempMeasTable": pm1004vMesrxfp1LxModTempMeasTable,
       "pm1004vMesrxfp1LxModTempMeasEntry": pm1004vMesrxfp1LxModTempMeasEntry,
       "pm1004vMesrxfp1LxModTempMeasIndex": pm1004vMesrxfp1LxModTempMeasIndex,
       "pm1004vMesrxfp1LxModTempMeasPortn": pm1004vMesrxfp1LxModTempMeasPortn,
       "pm1004vMesrxfp1ReservedTable": pm1004vMesrxfp1ReservedTable,
       "pm1004vMesrxfp1ReservedEntry": pm1004vMesrxfp1ReservedEntry,
       "pm1004vMesrxfp1ReservedIndex": pm1004vMesrxfp1ReservedIndex,
       "pm1004vMesrxfp1ReservedPortn": pm1004vMesrxfp1ReservedPortn,
       "pm1004vMesrxfp1LoBiasCurrentMeasTable": pm1004vMesrxfp1LoBiasCurrentMeasTable,
       "pm1004vMesrxfp1LoBiasCurrentMeasEntry": pm1004vMesrxfp1LoBiasCurrentMeasEntry,
       "pm1004vMesrxfp1LoBiasCurrentMeasIndex": pm1004vMesrxfp1LoBiasCurrentMeasIndex,
       "pm1004vMesrxfp1LoBiasCurrentMeasPortn": pm1004vMesrxfp1LoBiasCurrentMeasPortn,
       "pm1004vMesrxfp1LoTxPowerMeasTable": pm1004vMesrxfp1LoTxPowerMeasTable,
       "pm1004vMesrxfp1LoTxPowerMeasEntry": pm1004vMesrxfp1LoTxPowerMeasEntry,
       "pm1004vMesrxfp1LoTxPowerMeasIndex": pm1004vMesrxfp1LoTxPowerMeasIndex,
       "pm1004vMesrxfp1LoTxPowerMeasPortn": pm1004vMesrxfp1LoTxPowerMeasPortn,
       "pm1004vMesrxfp1LiRxPowerMeasTable": pm1004vMesrxfp1LiRxPowerMeasTable,
       "pm1004vMesrxfp1LiRxPowerMeasEntry": pm1004vMesrxfp1LiRxPowerMeasEntry,
       "pm1004vMesrxfp1LiRxPowerMeasIndex": pm1004vMesrxfp1LiRxPowerMeasIndex,
       "pm1004vMesrxfp1LiRxPowerMeasPortn": pm1004vMesrxfp1LiRxPowerMeasPortn,
       "pm1004vMesrxfp1LxAux1MeasTable": pm1004vMesrxfp1LxAux1MeasTable,
       "pm1004vMesrxfp1LxAux1MeasEntry": pm1004vMesrxfp1LxAux1MeasEntry,
       "pm1004vMesrxfp1LxAux1MeasIndex": pm1004vMesrxfp1LxAux1MeasIndex,
       "pm1004vMesrxfp1LxAux1MeasPortn": pm1004vMesrxfp1LxAux1MeasPortn,
       "pm1004vMesrxfp1LxAux2MeasTable": pm1004vMesrxfp1LxAux2MeasTable,
       "pm1004vMesrxfp1LxAux2MeasEntry": pm1004vMesrxfp1LxAux2MeasEntry,
       "pm1004vMesrxfp1LxAux2MeasIndex": pm1004vMesrxfp1LxAux2MeasIndex,
       "pm1004vMesrxfp1LxAux2MeasPortn": pm1004vMesrxfp1LxAux2MeasPortn,
       "pm1004vMesrotx1AgingTable": pm1004vMesrotx1AgingTable,
       "pm1004vMesrotx1AgingEntry": pm1004vMesrotx1AgingEntry,
       "pm1004vMesrotx1AgingIndex": pm1004vMesrotx1AgingIndex,
       "pm1004vMesrotx1AgingPortn": pm1004vMesrotx1AgingPortn,
       "pm1004vMesrotx1LaserTemperatureTable": pm1004vMesrotx1LaserTemperatureTable,
       "pm1004vMesrotx1LaserTemperatureEntry": pm1004vMesrotx1LaserTemperatureEntry,
       "pm1004vMesrotx1LaserTemperatureIndex": pm1004vMesrotx1LaserTemperatureIndex,
       "pm1004vMesrotx1LaserTemperaturePortn": pm1004vMesrotx1LaserTemperaturePortn,
       "pm1004vMesrotx1FreqDeviationTable": pm1004vMesrotx1FreqDeviationTable,
       "pm1004vMesrotx1FreqDeviationEntry": pm1004vMesrotx1FreqDeviationEntry,
       "pm1004vMesrotx1FreqDeviationIndex": pm1004vMesrotx1FreqDeviationIndex,
       "pm1004vMesrotx1FreqDeviationPortn": pm1004vMesrotx1FreqDeviationPortn,
       "pm1004vMesrotx1LaserWvlengthTable": pm1004vMesrotx1LaserWvlengthTable,
       "pm1004vMesrotx1LaserWvlengthEntry": pm1004vMesrotx1LaserWvlengthEntry,
       "pm1004vMesrotx1LaserWvlengthIndex": pm1004vMesrotx1LaserWvlengthIndex,
       "pm1004vMesrotx1LaserWvlengthPortn": pm1004vMesrotx1LaserWvlengthPortn,
       "pm1004vcounters": pm1004vcounters,
       "pm1004vCntOther": pm1004vCntOther,
       "pm1004vCntClient": pm1004vCntClient,
       "pm1004vCntLine": pm1004vCntLine,
       "pm1004vCntdfrmB1ErrCntTable": pm1004vCntdfrmB1ErrCntTable,
       "pm1004vCntdfrmB1ErrCntEntry": pm1004vCntdfrmB1ErrCntEntry,
       "pm1004vCntdfrmB1ErrCntIndex": pm1004vCntdfrmB1ErrCntIndex,
       "pm1004vCntdfrmB1ErrCntValuePortn": pm1004vCntdfrmB1ErrCntValuePortn,
       "pm1004vCntdfrmB1ErrCntErrorPortn": pm1004vCntdfrmB1ErrCntErrorPortn,
       "pm1004vCntdfrmB1ErrCntOverloadPortn": pm1004vCntdfrmB1ErrCntOverloadPortn,
       "pm1004vCntdfrmTimCntTable": pm1004vCntdfrmTimCntTable,
       "pm1004vCntdfrmTimCntEntry": pm1004vCntdfrmTimCntEntry,
       "pm1004vCntdfrmTimCntIndex": pm1004vCntdfrmTimCntIndex,
       "pm1004vCntdfrmTimCntValuePortn": pm1004vCntdfrmTimCntValuePortn,
       "pm1004vCntdfrmTimCntErrorPortn": pm1004vCntdfrmTimCntErrorPortn,
       "pm1004vCntdfrmTimCntOverloadPortn": pm1004vCntdfrmTimCntOverloadPortn,
       "pm1004vCntCountersReset": pm1004vCntCountersReset,
       "pm1004vCntCountersStop": pm1004vCntCountersStop,
       "pm1004vcontrolsWrite": pm1004vcontrolsWrite,
       "pm1004vCtrlOther": pm1004vCtrlOther,
       "pm1004vCtrlconfMgnt1": pm1004vCtrlconfMgnt1,
       "pm1004vCtrlConf1Load1": pm1004vCtrlConf1Load1,
       "pm1004vCtrlConf2Load1": pm1004vCtrlConf2Load1,
       "pm1004vCtrlConf2Flash1": pm1004vCtrlConf2Flash1,
       "pm1004vCtrlConf2Clear1": pm1004vCtrlConf2Clear1,
       "pm1004vCtrlsynth4": pm1004vCtrlsynth4,
       "pm1004vCtrlCorrelatOn": pm1004vCtrlCorrelatOn,
       "pm1004vCtrlCorrelatOff": pm1004vCtrlCorrelatOff,
       "pm1004vCtrlswMgnt": pm1004vCtrlswMgnt,
       "pm1004vCtrlColdReset": pm1004vCtrlColdReset,
       "pm1004vCtrlWarmReset": pm1004vCtrlWarmReset,
       "pm1004vCtrlLoadSwBank1": pm1004vCtrlLoadSwBank1,
       "pm1004vCtrlLoadSwBank2": pm1004vCtrlLoadSwBank2,
       "pm1004vCtrlgwMgnt": pm1004vCtrlgwMgnt,
       "pm1004vCtrlCurrentGwReset": pm1004vCtrlCurrentGwReset,
       "pm1004vCtrlLoadGwBank1": pm1004vCtrlLoadGwBank1,
       "pm1004vCtrlLoadGwBank2": pm1004vCtrlLoadGwBank2,
       "pm1004vCtrlLoadGwBank3": pm1004vCtrlLoadGwBank3,
       "pm1004vCtrlLoadGwBank4": pm1004vCtrlLoadGwBank4,
       "pm1004vCtrlledTest": pm1004vCtrlledTest,
       "pm1004vCtrlGreenLed": pm1004vCtrlGreenLed,
       "pm1004vCtrlRedLed": pm1004vCtrlRedLed,
       "pm1004vCtrlLedOff": pm1004vCtrlLedOff,
       "pm1004vCtrlmoduleOosMode": pm1004vCtrlmoduleOosMode,
       "pm1004vCtrlModuleOosMode": pm1004vCtrlModuleOosMode,
       "pm1004vCtrlmaintenanceMode": pm1004vCtrlmaintenanceMode,
       "pm1004vCtrlMaintenanceMode": pm1004vCtrlMaintenanceMode,
       "pm1004vCtrlClient": pm1004vCtrlClient,
       "pm1004vCtrlaccessLoopTable": pm1004vCtrlaccessLoopTable,
       "pm1004vCtrlaccessLoopEntry": pm1004vCtrlaccessLoopEntry,
       "pm1004vCtrlaccessLoopIndex": pm1004vCtrlaccessLoopIndex,
       "pm1004vCtrlaccessLoopPortn": pm1004vCtrlaccessLoopPortn,
       "pm1004vCtrlportOosModeTable": pm1004vCtrlportOosModeTable,
       "pm1004vCtrlportOosModeEntry": pm1004vCtrlportOosModeEntry,
       "pm1004vCtrlportOosModeIndex": pm1004vCtrlportOosModeIndex,
       "pm1004vCtrlportOosModePortn": pm1004vCtrlportOosModePortn,
       "pm1004vCtrlsfpOffCtrlTable": pm1004vCtrlsfpOffCtrlTable,
       "pm1004vCtrlsfpOffCtrlEntry": pm1004vCtrlsfpOffCtrlEntry,
       "pm1004vCtrlsfpOffCtrlIndex": pm1004vCtrlsfpOffCtrlIndex,
       "pm1004vCtrlsfpOffCtrlPortn": pm1004vCtrlsfpOffCtrlPortn,
       "pm1004vCtrlcsfUpInsTable": pm1004vCtrlcsfUpInsTable,
       "pm1004vCtrlcsfUpInsEntry": pm1004vCtrlcsfUpInsEntry,
       "pm1004vCtrlcsfUpInsIndex": pm1004vCtrlcsfUpInsIndex,
       "pm1004vCtrlcsfUpInsPortn": pm1004vCtrlcsfUpInsPortn,
       "pm1004vCtrlcaisDwInsTable": pm1004vCtrlcaisDwInsTable,
       "pm1004vCtrlcaisDwInsEntry": pm1004vCtrlcaisDwInsEntry,
       "pm1004vCtrlcaisDwInsIndex": pm1004vCtrlcaisDwInsIndex,
       "pm1004vCtrlcaisDwInsPortn": pm1004vCtrlcaisDwInsPortn,
       "pm1004vCtrlclientAccessTermLoopTable": pm1004vCtrlclientAccessTermLoopTable,
       "pm1004vCtrlclientAccessTermLoopEntry": pm1004vCtrlclientAccessTermLoopEntry,
       "pm1004vCtrlclientAccessTermLoopIndex": pm1004vCtrlclientAccessTermLoopIndex,
       "pm1004vCtrlclientAccessTermLoopPortn": pm1004vCtrlclientAccessTermLoopPortn,
       "pm1004vCtrlrxVideoProtocolTable": pm1004vCtrlrxVideoProtocolTable,
       "pm1004vCtrlrxVideoProtocolEntry": pm1004vCtrlrxVideoProtocolEntry,
       "pm1004vCtrlrxVideoProtocolIndex": pm1004vCtrlrxVideoProtocolIndex,
       "pm1004vCtrlrxVideoProtocolPortn": pm1004vCtrlrxVideoProtocolPortn,
       "pm1004vCtrladddropClientRxProtectTable": pm1004vCtrladddropClientRxProtectTable,
       "pm1004vCtrladddropClientRxProtectEntry": pm1004vCtrladddropClientRxProtectEntry,
       "pm1004vCtrladddropClientRxProtectIndex": pm1004vCtrladddropClientRxProtectIndex,
       "pm1004vCtrladddropClientRxProtectPortn": pm1004vCtrladddropClientRxProtectPortn,
       "pm1004vCtrladddropTsClientModeTable": pm1004vCtrladddropTsClientModeTable,
       "pm1004vCtrladddropTsClientModeEntry": pm1004vCtrladddropTsClientModeEntry,
       "pm1004vCtrladddropTsClientModeIndex": pm1004vCtrladddropTsClientModeIndex,
       "pm1004vCtrladddropTsClientModePortn": pm1004vCtrladddropTsClientModePortn,
       "pm1004vCtrlLine": pm1004vCtrlLine,
       "pm1004vCtrlcommAccessLoop": pm1004vCtrlcommAccessLoop,
       "pm1004vCtrlCommAccessloop": pm1004vCtrlCommAccessloop,
       "pm1004vCtrllineLoop": pm1004vCtrllineLoop,
       "pm1004vCtrlLineLoop": pm1004vCtrlLineLoop,
       "pm1004vCtrlProtMgnt": pm1004vCtrlProtMgnt,
       "pm1004vCtrlLineNumber": pm1004vCtrlLineNumber,
       "pm1004vCtrlProtMode": pm1004vCtrlProtMode,
       "pm1004vCtrllineOosModeTable": pm1004vCtrllineOosModeTable,
       "pm1004vCtrllineOosModeEntry": pm1004vCtrllineOosModeEntry,
       "pm1004vCtrllineOosModeIndex": pm1004vCtrllineOosModeIndex,
       "pm1004vCtrllineOosModePortn": pm1004vCtrllineOosModePortn,
       "pm1004vCtrldccEnableTable": pm1004vCtrldccEnableTable,
       "pm1004vCtrldccEnableEntry": pm1004vCtrldccEnableEntry,
       "pm1004vCtrldccEnableIndex": pm1004vCtrldccEnableIndex,
       "pm1004vCtrldccEnablePortn": pm1004vCtrldccEnablePortn,
       "pm1004vCtrlxfpOnoffTable": pm1004vCtrlxfpOnoffTable,
       "pm1004vCtrlxfpOnoffEntry": pm1004vCtrlxfpOnoffEntry,
       "pm1004vCtrlxfpOnoffIndex": pm1004vCtrlxfpOnoffIndex,
       "pm1004vCtrlxfpOnoffPortn": pm1004vCtrlxfpOnoffPortn,
       "pm1004vCtrlxfpLineLoopTable": pm1004vCtrlxfpLineLoopTable,
       "pm1004vCtrlxfpLineLoopEntry": pm1004vCtrlxfpLineLoopEntry,
       "pm1004vCtrlxfpLineLoopIndex": pm1004vCtrlxfpLineLoopIndex,
       "pm1004vCtrlxfpLineLoopPortn": pm1004vCtrlxfpLineLoopPortn,
       "pm1004vCtrlxfpXfiLoopTable": pm1004vCtrlxfpXfiLoopTable,
       "pm1004vCtrlxfpXfiLoopEntry": pm1004vCtrlxfpXfiLoopEntry,
       "pm1004vCtrlxfpXfiLoopIndex": pm1004vCtrlxfpXfiLoopIndex,
       "pm1004vCtrlxfpXfiLoopPortn": pm1004vCtrlxfpXfiLoopPortn,
       "pm1004vri": pm1004vri,
       "pm1004vriTable": pm1004vriTable,
       "pm1004vRinvSfpTable": pm1004vRinvSfpTable,
       "pm1004vRinvSfpEntry": pm1004vRinvSfpEntry,
       "pm1004vRinvSfpIndex": pm1004vRinvSfpIndex,
       "pm1004vRinvsfp": pm1004vRinvsfp,
       "pm1004vRinvLineTable": pm1004vRinvLineTable,
       "pm1004vRinvLineEntry": pm1004vRinvLineEntry,
       "pm1004vRinvLineIndex": pm1004vRinvLineIndex,
       "pm1004vRinvxfpLine": pm1004vRinvxfpLine,
       "pm1004vRinvReloadInventory": pm1004vRinvReloadInventory,
       "pm1004vRinvHwPlatform": pm1004vRinvHwPlatform,
       "pm1004vRinvModulePlatform": pm1004vRinvModulePlatform,
       "pm1004vRinvSwPlatform": pm1004vRinvSwPlatform,
       "pm1004vRinvGwPlatform": pm1004vRinvGwPlatform,
       "pm1004vdownload": pm1004vdownload,
       "pm1004vDwlOther": pm1004vDwlOther,
       "pm1004vDwlrestartProcess": pm1004vDwlrestartProcess,
       "pm1004vDwlWarmRestartProcessed": pm1004vDwlWarmRestartProcessed,
       "pm1004vDwlColdRestartProcessed": pm1004vDwlColdRestartProcessed,
       "pm1004vDwlswBanksUsed": pm1004vDwlswBanksUsed,
       "pm1004vDwlSwBank1Used": pm1004vDwlSwBank1Used,
       "pm1004vDwlSwBank2Used": pm1004vDwlSwBank2Used,
       "pm1004vDwlSwBank1Notempty": pm1004vDwlSwBank1Notempty,
       "pm1004vDwlSwBank2Notempty": pm1004vDwlSwBank2Notempty,
       "pm1004vDwlgwBanksUsed": pm1004vDwlgwBanksUsed,
       "pm1004vDwlGwBank1Used": pm1004vDwlGwBank1Used,
       "pm1004vDwlGwBank2Used": pm1004vDwlGwBank2Used,
       "pm1004vDwlGwBank3Used": pm1004vDwlGwBank3Used,
       "pm1004vDwlGwBank4Used": pm1004vDwlGwBank4Used,
       "pm1004vDwlGwBank1Notempty": pm1004vDwlGwBank1Notempty,
       "pm1004vDwlGwBank2Notempty": pm1004vDwlGwBank2Notempty,
       "pm1004vDwlGwBank3Notempty": pm1004vDwlGwBank3Notempty,
       "pm1004vDwlGwBank4Notempty": pm1004vDwlGwBank4Notempty,
       "pm1004vDwlClient": pm1004vDwlClient,
       "pm1004vDwlLine": pm1004vDwlLine,
       "pm1004vConfig": pm1004vConfig,
       "pm1004vCfgAccessCAisCsf": pm1004vCfgAccessCAisCsf,
       "pm1004vCfgClientcaiscsfTable": pm1004vCfgClientcaiscsfTable,
       "pm1004vCfgClientcaiscsfEntry": pm1004vCfgClientcaiscsfEntry,
       "pm1004vCfgClientcaiscsfIndex": pm1004vCfgClientcaiscsfIndex,
       "pm1004vCfgCAisModePortn": pm1004vCfgCAisModePortn,
       "pm1004vCfgUpAccessioAlmPortn": pm1004vCfgUpAccessioAlmPortn,
       "pm1004vCfgUpMapperDeAlmPortn": pm1004vCfgUpMapperDeAlmPortn,
       "pm1004vCfgDownAccessioAlmPortn": pm1004vCfgDownAccessioAlmPortn,
       "pm1004vCfgDownMapperDeAlmPortn": pm1004vCfgDownMapperDeAlmPortn,
       "pm1004vCfgDownDfrmAlmPortn": pm1004vCfgDownDfrmAlmPortn,
       "pm1004vCfgDownLineSyncAlarmsPortn": pm1004vCfgDownLineSyncAlarmsPortn,
       "pm1004vCfgStartup": pm1004vCfgStartup,
       "pm1004vCfgClientStartupTable": pm1004vCfgClientStartupTable,
       "pm1004vCfgClientStartupEntry": pm1004vCfgClientStartupEntry,
       "pm1004vCfgClientStartupIndex": pm1004vCfgClientStartupIndex,
       "pm1004vCfgSystConfPortPortn": pm1004vCfgSystConfPortPortn,
       "pm1004vCfgNetConfPortPortn": pm1004vCfgNetConfPortPortn,
       "pm1004vCfgAdddropConfPortPortn": pm1004vCfgAdddropConfPortPortn,
       "pm1004vtablelineStartup": pm1004vtablelineStartup,
       "pm1004vCfgsystConfLine1": pm1004vCfgsystConfLine1,
       "pm1004vCfglineOptions1": pm1004vCfglineOptions1,
       "pm1004vCfgsystConfLine2": pm1004vCfgsystConfLine2,
       "pm1004vCfglineSelection": pm1004vCfglineSelection,
       "pm1004vCfglineOptions2": pm1004vCfglineOptions2,
       "pm1004vCfgXfpTable": pm1004vCfgXfpTable,
       "pm1004vCfgXfpEntry": pm1004vCfgXfpEntry,
       "pm1004vCfgXfpIndex": pm1004vCfgXfpIndex,
       "pm1004vCfgSystConfXfpPortn": pm1004vCfgSystConfXfpPortn,
       "pm1004vCfgDataRateConfXfpPortn": pm1004vCfgDataRateConfXfpPortn,
       "pm1004vCfgLabels": pm1004vCfgLabels,
       "pm1004vCfgLabelclientTable": pm1004vCfgLabelclientTable,
       "pm1004vCfgLabelclientEntry": pm1004vCfgLabelclientEntry,
       "pm1004vCfgLabelclientIndex": pm1004vCfgLabelclientIndex,
       "pm1004vCfgLabelclientPortn": pm1004vCfgLabelclientPortn,
       "pm1004vCfgLabellineTable": pm1004vCfgLabellineTable,
       "pm1004vCfgLabellineEntry": pm1004vCfgLabellineEntry,
       "pm1004vCfgLabellineIndex": pm1004vCfgLabellineIndex,
       "pm1004vCfgLabellinePortn": pm1004vCfgLabellinePortn,
       "pm1004vCfgStartupthresholds": pm1004vCfgStartupthresholds,
       "pm1004vCfgClientStartupThreshTable": pm1004vCfgClientStartupThreshTable,
       "pm1004vCfgClientStartupThreshEntry": pm1004vCfgClientStartupThreshEntry,
       "pm1004vCfgClientStartupThreshIndex": pm1004vCfgClientStartupThreshIndex,
       "pm1004vCfgClientThreshtxpowhighPortn": pm1004vCfgClientThreshtxpowhighPortn,
       "pm1004vCfgClientThreshtxpowlowPortn": pm1004vCfgClientThreshtxpowlowPortn,
       "pm1004vCfgClientThreshrxpowhighPortn": pm1004vCfgClientThreshrxpowhighPortn,
       "pm1004vCfgClientThreshrxpowlowPortn": pm1004vCfgClientThreshrxpowlowPortn,
       "pm1004vCfgLineStartupThreshTable": pm1004vCfgLineStartupThreshTable,
       "pm1004vCfgLineStartupThreshEntry": pm1004vCfgLineStartupThreshEntry,
       "pm1004vCfgLineStartupThreshIndex": pm1004vCfgLineStartupThreshIndex,
       "pm1004vCfgLineThreshtxpowhighPortn": pm1004vCfgLineThreshtxpowhighPortn,
       "pm1004vCfgLineThreshtxpowlowPortn": pm1004vCfgLineThreshtxpowlowPortn,
       "pm1004vCfgLineThreshrxpowhighPortn": pm1004vCfgLineThreshrxpowhighPortn,
       "pm1004vCfgLineThreshrxpowlowPortn": pm1004vCfgLineThreshrxpowlowPortn,
       "pm1004vCfgStartuptlh": pm1004vCfgStartuptlh,
       "pm1004vCfgOtxtlhTable": pm1004vCfgOtxtlhTable,
       "pm1004vCfgOtxtlhEntry": pm1004vCfgOtxtlhEntry,
       "pm1004vCfgOtxtlhIndex": pm1004vCfgOtxtlhIndex,
       "pm1004vCfgNuPortn": pm1004vCfgNuPortn,
       "pm1004vCfgLineDitherRatePortn": pm1004vCfgLineDitherRatePortn,
       "pm1004vCfgLineDitherFhzPortn": pm1004vCfgLineDitherFhzPortn,
       "pm1004vCfgLinePwrLaserPortn": pm1004vCfgLinePwrLaserPortn,
       "pm1004vCfgLineFCurrentPortn": pm1004vCfgLineFCurrentPortn,
       "pm1004vCfgLineGridCurrentPortn": pm1004vCfgLineGridCurrentPortn,
       "pm1004vCfgFPortn": pm1004vCfgFPortn,
       "pm1004vCfgReservedPortn": pm1004vCfgReservedPortn,
       "pm1004vCfgLinePhotodiodeModePortn": pm1004vCfgLinePhotodiodeModePortn,
       "pm1004vCfgLinePhotodiodeValuePortn": pm1004vCfgLinePhotodiodeValuePortn,
       "pm1004vCfgStartuptablefive": pm1004vCfgStartuptablefive,
       "pm1004vCfgOtxtlhcapabilitiesTable": pm1004vCfgOtxtlhcapabilitiesTable,
       "pm1004vCfgOtxtlhcapabilitiesEntry": pm1004vCfgOtxtlhcapabilitiesEntry,
       "pm1004vCfgOtxtlhcapabilitiesIndex": pm1004vCfgOtxtlhcapabilitiesIndex,
       "pm1004vCfgComponentTypePortn": pm1004vCfgComponentTypePortn,
       "pm1004vCfgMiscellaneousPortn": pm1004vCfgMiscellaneousPortn,
       "pm1004vCfgFirstChannelPortn": pm1004vCfgFirstChannelPortn,
       "pm1004vCfgLastChannelPortn": pm1004vCfgLastChannelPortn,
       "pm1004vCfgGridPortn": pm1004vCfgGridPortn,
       "pm1004vCfgWriteConfiguration": pm1004vCfgWriteConfiguration,
       "pm1004vtraps": pm1004vtraps,
       "pm1004vtrapPortNumber": pm1004vtrapPortNumber,
       "pm1004vtrapLineNumber": pm1004vtrapLineNumber,
       "pm1004vtrapBoardNumber": pm1004vtrapBoardNumber,
       "pm1004vLineTrapNotUrgentGoesOn": pm1004vLineTrapNotUrgentGoesOn,
       "pm1004vLineTrapNotUrgentGoesOff": pm1004vLineTrapNotUrgentGoesOff,
       "pm1004vLineTrapUrgentGoesOn": pm1004vLineTrapUrgentGoesOn,
       "pm1004vLineTrapUrgentGoesOff": pm1004vLineTrapUrgentGoesOff,
       "pm1004vLineTrapCritGoesOn": pm1004vLineTrapCritGoesOn,
       "pm1004vLineTrapCritGoesOff": pm1004vLineTrapCritGoesOff,
       "pm1004vClientTrapNotUrgentGoesOn": pm1004vClientTrapNotUrgentGoesOn,
       "pm1004vClientTrapNotUrgentGoesOff": pm1004vClientTrapNotUrgentGoesOff,
       "pm1004vClientTrapUrgentGoesOn": pm1004vClientTrapUrgentGoesOn,
       "pm1004vClientTrapUrgentGoesOff": pm1004vClientTrapUrgentGoesOff,
       "pm1004vClientTrapCritGoesOn": pm1004vClientTrapCritGoesOn,
       "pm1004vClientTrapCritGoesOff": pm1004vClientTrapCritGoesOff,
       "pm1004vPowerTrapUrgentGoesOn": pm1004vPowerTrapUrgentGoesOn,
       "pm1004vPowerTrapUrgentGoesOff": pm1004vPowerTrapUrgentGoesOff,
       "pm1004vMonitoring": pm1004vMonitoring,
       "pm1004vMonOther": pm1004vMonOther,
       "pm1004vMonRmon": pm1004vMonRmon,
       "pm1004vMonCountersReset": pm1004vMonCountersReset,
       "pm1004vMonCountersStop": pm1004vMonCountersStop,
       "pm1004vMonClient": pm1004vMonClient,
       "pm1004vMonClientRmonCounter": pm1004vMonClientRmonCounter,
       "pm1004vMonupRmonByteCntTable": pm1004vMonupRmonByteCntTable,
       "pm1004vMonupRmonByteCntEntry": pm1004vMonupRmonByteCntEntry,
       "pm1004vMonupRmonByteCntIndex": pm1004vMonupRmonByteCntIndex,
       "pm1004vMonupRmonByteCntValuePortn": pm1004vMonupRmonByteCntValuePortn,
       "pm1004vMonupRmonByteCntErrorPortn": pm1004vMonupRmonByteCntErrorPortn,
       "pm1004vMonupRmonByteCntOverloadPortn": pm1004vMonupRmonByteCntOverloadPortn,
       "pm1004vMonupRmonCrcErrorCntTable": pm1004vMonupRmonCrcErrorCntTable,
       "pm1004vMonupRmonCrcErrorCntEntry": pm1004vMonupRmonCrcErrorCntEntry,
       "pm1004vMonupRmonCrcErrorCntIndex": pm1004vMonupRmonCrcErrorCntIndex,
       "pm1004vMonupRmonCrcErrorCntValuePortn": pm1004vMonupRmonCrcErrorCntValuePortn,
       "pm1004vMonupRmonCrcErrorCntErrorPortn": pm1004vMonupRmonCrcErrorCntErrorPortn,
       "pm1004vMonupRmonCrcErrorCntOverloadPortn": pm1004vMonupRmonCrcErrorCntOverloadPortn,
       "pm1004vMonupRmonPacketsCntTable": pm1004vMonupRmonPacketsCntTable,
       "pm1004vMonupRmonPacketsCntEntry": pm1004vMonupRmonPacketsCntEntry,
       "pm1004vMonupRmonPacketsCntIndex": pm1004vMonupRmonPacketsCntIndex,
       "pm1004vMonupRmonPacketsCntValuePortn": pm1004vMonupRmonPacketsCntValuePortn,
       "pm1004vMonupRmonPacketsCntErrorPortn": pm1004vMonupRmonPacketsCntErrorPortn,
       "pm1004vMonupRmonPacketsCntOverloadPortn": pm1004vMonupRmonPacketsCntOverloadPortn,
       "pm1004vMonupRmonBroadcastCntTable": pm1004vMonupRmonBroadcastCntTable,
       "pm1004vMonupRmonBroadcastCntEntry": pm1004vMonupRmonBroadcastCntEntry,
       "pm1004vMonupRmonBroadcastCntIndex": pm1004vMonupRmonBroadcastCntIndex,
       "pm1004vMonupRmonBroadcastCntValuePortn": pm1004vMonupRmonBroadcastCntValuePortn,
       "pm1004vMonupRmonBroadcastCntErrorPortn": pm1004vMonupRmonBroadcastCntErrorPortn,
       "pm1004vMonupRmonBroadcastCntOverloadPortn": pm1004vMonupRmonBroadcastCntOverloadPortn,
       "pm1004vMonupRmonMulticastCntTable": pm1004vMonupRmonMulticastCntTable,
       "pm1004vMonupRmonMulticastCntEntry": pm1004vMonupRmonMulticastCntEntry,
       "pm1004vMonupRmonMulticastCntIndex": pm1004vMonupRmonMulticastCntIndex,
       "pm1004vMonupRmonMulticastCntValuePortn": pm1004vMonupRmonMulticastCntValuePortn,
       "pm1004vMonupRmonMulticastCntErrorPortn": pm1004vMonupRmonMulticastCntErrorPortn,
       "pm1004vMonupRmonMulticastCntOverloadPortn": pm1004vMonupRmonMulticastCntOverloadPortn,
       "pm1004vMonupLineRmonByteCntTable": pm1004vMonupLineRmonByteCntTable,
       "pm1004vMonupLineRmonByteCntEntry": pm1004vMonupLineRmonByteCntEntry,
       "pm1004vMonupLineRmonByteCntIndex": pm1004vMonupLineRmonByteCntIndex,
       "pm1004vMonupLineRmonByteCntValuePortn": pm1004vMonupLineRmonByteCntValuePortn,
       "pm1004vMonupLineRmonByteCntErrorPortn": pm1004vMonupLineRmonByteCntErrorPortn,
       "pm1004vMonupLineRmonByteCntOverloadPortn": pm1004vMonupLineRmonByteCntOverloadPortn,
       "pm1004vMonupLineRmonCrcErrorCntTable": pm1004vMonupLineRmonCrcErrorCntTable,
       "pm1004vMonupLineRmonCrcErrorCntEntry": pm1004vMonupLineRmonCrcErrorCntEntry,
       "pm1004vMonupLineRmonCrcErrorCntIndex": pm1004vMonupLineRmonCrcErrorCntIndex,
       "pm1004vMonupLineRmonCrcErrorCntValuePortn": pm1004vMonupLineRmonCrcErrorCntValuePortn,
       "pm1004vMonupLineRmonCrcErrorCntErrorPortn": pm1004vMonupLineRmonCrcErrorCntErrorPortn,
       "pm1004vMonupLineRmonCrcErrorCntOverloadPortn": pm1004vMonupLineRmonCrcErrorCntOverloadPortn,
       "pm1004vMonupLineRmonPacketsCntTable": pm1004vMonupLineRmonPacketsCntTable,
       "pm1004vMonupLineRmonPacketsCntEntry": pm1004vMonupLineRmonPacketsCntEntry,
       "pm1004vMonupLineRmonPacketsCntIndex": pm1004vMonupLineRmonPacketsCntIndex,
       "pm1004vMonupLineRmonPacketsCntValuePortn": pm1004vMonupLineRmonPacketsCntValuePortn,
       "pm1004vMonupLineRmonPacketsCntErrorPortn": pm1004vMonupLineRmonPacketsCntErrorPortn,
       "pm1004vMonupLineRmonPacketsCntOverloadPortn": pm1004vMonupLineRmonPacketsCntOverloadPortn,
       "pm1004vMonLine": pm1004vMonLine,
       "pm1004vMonLineRmonCounter": pm1004vMonLineRmonCounter}
)
