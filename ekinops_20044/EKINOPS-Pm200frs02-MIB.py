# SNMP MIB module (EKINOPS-Pm200frs02-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ekinops_20044/EKINOPS-Pm200frs02-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 12:01:48 2025
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

modulePm200frs02 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90)
)
if mibBuilder.loadTexts:
    modulePm200frs02.setRevisions(
        ("2017-07-25 00:00",
         "2017-09-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Pm200frs02MultiRate(TextualConvention, Integer32):
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



class Pm200frs02OtxMode(TextualConvention, Integer32):
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



class Pm200frs02OtxGrid(TextualConvention, Integer32):
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



class Pm200frs02AdjustValue(TextualConvention, Integer32):
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



class Pm200frs02ClientProtocol(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("protocolclientvalue0", 0),
          ("protocolclientvalue1", 1),
          ("protocolclientvalue2", 2),
          ("protocolclientvalue3", 3),
          ("protocolclientvalue4", 4),
          ("protocolclientvalue5", 5),
          ("protocolclientvalue6", 6),
          ("protocolclientvalue7", 7),
          ("protocolclientvalue8", 8))
    )



class Pm200frs02ModuleMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("modulemodevalue0", 0),
          ("modulemodevalue1", 1),
          ("modulemodevalue2", 2),
          ("modulemodevalue3", 3),
          ("modulemodevalue4", 4),
          ("modulemodevalue5", 5))
    )



class Pm200frs02OtxChannel(TextualConvention, Integer32):
    status = "current"


class Pm200frs02OrxChannel(TextualConvention, Integer32):
    status = "current"


class Pm200frs02DccMode(TextualConvention, Integer32):
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
        *(("dccNo", 0),
          ("dccLine1", 1),
          ("dccLine2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Pm200frs02alarms_ObjectIdentity = ObjectIdentity
pm200frs02alarms = _Pm200frs02alarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2)
)
_Pm200frs02AlmOther_ObjectIdentity = ObjectIdentity
pm200frs02AlmOther = _Pm200frs02AlmOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1)
)
_Pm200frs02AlmOtherNurg_ObjectIdentity = ObjectIdentity
pm200frs02AlmOtherNurg = _Pm200frs02AlmOtherNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1)
)
_Pm200frs02AlmsynthAlm2_ObjectIdentity = ObjectIdentity
pm200frs02AlmsynthAlm2 = _Pm200frs02AlmsynthAlm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 2)
)
_Pm200frs02AlmConfTableSave_Type = EkiOnOff
_Pm200frs02AlmConfTableSave_Object = MibScalar
pm200frs02AlmConfTableSave = _Pm200frs02AlmConfTableSave_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 2, 1),
    _Pm200frs02AlmConfTableSave_Type()
)
pm200frs02AlmConfTableSave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmConfTableSave.setStatus("current")
_Pm200frs02AlmInvUpload_Type = EkiOnOff
_Pm200frs02AlmInvUpload_Object = MibScalar
pm200frs02AlmInvUpload = _Pm200frs02AlmInvUpload_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 2, 2),
    _Pm200frs02AlmInvUpload_Type()
)
pm200frs02AlmInvUpload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmInvUpload.setStatus("current")
_Pm200frs02AlmConfTableLoad_Type = EkiOnOff
_Pm200frs02AlmConfTableLoad_Object = MibScalar
pm200frs02AlmConfTableLoad = _Pm200frs02AlmConfTableLoad_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 2, 3),
    _Pm200frs02AlmConfTableLoad_Type()
)
pm200frs02AlmConfTableLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmConfTableLoad.setStatus("current")
_Pm200frs02AlmCorrelatOff_Type = EkiOnOff
_Pm200frs02AlmCorrelatOff_Object = MibScalar
pm200frs02AlmCorrelatOff = _Pm200frs02AlmCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 2, 4),
    _Pm200frs02AlmCorrelatOff_Type()
)
pm200frs02AlmCorrelatOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmCorrelatOff.setStatus("current")
_Pm200frs02AlmMaintenanceOn_Type = EkiOnOff
_Pm200frs02AlmMaintenanceOn_Object = MibScalar
pm200frs02AlmMaintenanceOn = _Pm200frs02AlmMaintenanceOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 2, 5),
    _Pm200frs02AlmMaintenanceOn_Type()
)
pm200frs02AlmMaintenanceOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMaintenanceOn.setStatus("current")
_Pm200frs02AlmclientQsfpWarnDdm_ObjectIdentity = ObjectIdentity
pm200frs02AlmclientQsfpWarnDdm = _Pm200frs02AlmclientQsfpWarnDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338)
)
_Pm200frs02AlmTrscv1VccLowWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv1VccLowWng1_Object = MibScalar
pm200frs02AlmTrscv1VccLowWng1 = _Pm200frs02AlmTrscv1VccLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 1),
    _Pm200frs02AlmTrscv1VccLowWng1_Type()
)
pm200frs02AlmTrscv1VccLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1VccLowWng1.setStatus("current")
_Pm200frs02AlmTrscv1VccHighWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv1VccHighWng1_Object = MibScalar
pm200frs02AlmTrscv1VccHighWng1 = _Pm200frs02AlmTrscv1VccHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 2),
    _Pm200frs02AlmTrscv1VccHighWng1_Type()
)
pm200frs02AlmTrscv1VccHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1VccHighWng1.setStatus("current")
_Pm200frs02AlmTrscv1TempLowWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv1TempLowWng1_Object = MibScalar
pm200frs02AlmTrscv1TempLowWng1 = _Pm200frs02AlmTrscv1TempLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 3),
    _Pm200frs02AlmTrscv1TempLowWng1_Type()
)
pm200frs02AlmTrscv1TempLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1TempLowWng1.setStatus("current")
_Pm200frs02AlmTrscv1TempHighWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv1TempHighWng1_Object = MibScalar
pm200frs02AlmTrscv1TempHighWng1 = _Pm200frs02AlmTrscv1TempHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 4),
    _Pm200frs02AlmTrscv1TempHighWng1_Type()
)
pm200frs02AlmTrscv1TempHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1TempHighWng1.setStatus("current")
_Pm200frs02AlmTrscv2VccLowWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv2VccLowWng1_Object = MibScalar
pm200frs02AlmTrscv2VccLowWng1 = _Pm200frs02AlmTrscv2VccLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 5),
    _Pm200frs02AlmTrscv2VccLowWng1_Type()
)
pm200frs02AlmTrscv2VccLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2VccLowWng1.setStatus("current")
_Pm200frs02AlmTrscv2VccHighWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv2VccHighWng1_Object = MibScalar
pm200frs02AlmTrscv2VccHighWng1 = _Pm200frs02AlmTrscv2VccHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 6),
    _Pm200frs02AlmTrscv2VccHighWng1_Type()
)
pm200frs02AlmTrscv2VccHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2VccHighWng1.setStatus("current")
_Pm200frs02AlmTrscv2TempLowWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv2TempLowWng1_Object = MibScalar
pm200frs02AlmTrscv2TempLowWng1 = _Pm200frs02AlmTrscv2TempLowWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 7),
    _Pm200frs02AlmTrscv2TempLowWng1_Type()
)
pm200frs02AlmTrscv2TempLowWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2TempLowWng1.setStatus("current")
_Pm200frs02AlmTrscv2TempHighWng1_Type = EkiOnOff
_Pm200frs02AlmTrscv2TempHighWng1_Object = MibScalar
pm200frs02AlmTrscv2TempHighWng1 = _Pm200frs02AlmTrscv2TempHighWng1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 1, 338, 8),
    _Pm200frs02AlmTrscv2TempHighWng1_Type()
)
pm200frs02AlmTrscv2TempHighWng1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2TempHighWng1.setStatus("current")
_Pm200frs02AlmOtherUrg_ObjectIdentity = ObjectIdentity
pm200frs02AlmOtherUrg = _Pm200frs02AlmOtherUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2)
)
_Pm200frs02AlmclientQsfpAlarmDdm_ObjectIdentity = ObjectIdentity
pm200frs02AlmclientQsfpAlarmDdm = _Pm200frs02AlmclientQsfpAlarmDdm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337)
)
_Pm200frs02AlmTrscv1VccLowAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv1VccLowAla1_Object = MibScalar
pm200frs02AlmTrscv1VccLowAla1 = _Pm200frs02AlmTrscv1VccLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 1),
    _Pm200frs02AlmTrscv1VccLowAla1_Type()
)
pm200frs02AlmTrscv1VccLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1VccLowAla1.setStatus("current")
_Pm200frs02AlmTrscv1VccHighAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv1VccHighAla1_Object = MibScalar
pm200frs02AlmTrscv1VccHighAla1 = _Pm200frs02AlmTrscv1VccHighAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 2),
    _Pm200frs02AlmTrscv1VccHighAla1_Type()
)
pm200frs02AlmTrscv1VccHighAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1VccHighAla1.setStatus("current")
_Pm200frs02AlmTrscv1TempLowAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv1TempLowAla1_Object = MibScalar
pm200frs02AlmTrscv1TempLowAla1 = _Pm200frs02AlmTrscv1TempLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 3),
    _Pm200frs02AlmTrscv1TempLowAla1_Type()
)
pm200frs02AlmTrscv1TempLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1TempLowAla1.setStatus("current")
_Pm200frs02AlmTrscv1TempHighAla_Type = EkiOnOff
_Pm200frs02AlmTrscv1TempHighAla_Object = MibScalar
pm200frs02AlmTrscv1TempHighAla = _Pm200frs02AlmTrscv1TempHighAla_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 4),
    _Pm200frs02AlmTrscv1TempHighAla_Type()
)
pm200frs02AlmTrscv1TempHighAla.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv1TempHighAla.setStatus("current")
_Pm200frs02AlmTrscv2VccLowAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv2VccLowAla1_Object = MibScalar
pm200frs02AlmTrscv2VccLowAla1 = _Pm200frs02AlmTrscv2VccLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 5),
    _Pm200frs02AlmTrscv2VccLowAla1_Type()
)
pm200frs02AlmTrscv2VccLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2VccLowAla1.setStatus("current")
_Pm200frs02AlmTrscv2VccHighAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv2VccHighAla1_Object = MibScalar
pm200frs02AlmTrscv2VccHighAla1 = _Pm200frs02AlmTrscv2VccHighAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 6),
    _Pm200frs02AlmTrscv2VccHighAla1_Type()
)
pm200frs02AlmTrscv2VccHighAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2VccHighAla1.setStatus("current")
_Pm200frs02AlmTrscv2TempLowAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv2TempLowAla1_Object = MibScalar
pm200frs02AlmTrscv2TempLowAla1 = _Pm200frs02AlmTrscv2TempLowAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 7),
    _Pm200frs02AlmTrscv2TempLowAla1_Type()
)
pm200frs02AlmTrscv2TempLowAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2TempLowAla1.setStatus("current")
_Pm200frs02AlmTrscv2TempHighAla1_Type = EkiOnOff
_Pm200frs02AlmTrscv2TempHighAla1_Object = MibScalar
pm200frs02AlmTrscv2TempHighAla1 = _Pm200frs02AlmTrscv2TempHighAla1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 2, 337, 8),
    _Pm200frs02AlmTrscv2TempHighAla1_Type()
)
pm200frs02AlmTrscv2TempHighAla1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTrscv2TempHighAla1.setStatus("current")
_Pm200frs02AlmOtherCrit_ObjectIdentity = ObjectIdentity
pm200frs02AlmOtherCrit = _Pm200frs02AlmOtherCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3)
)
_Pm200frs02AlmsynthAlm0_ObjectIdentity = ObjectIdentity
pm200frs02AlmsynthAlm0 = _Pm200frs02AlmsynthAlm0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 0)
)
_Pm200frs02AlmFailFan_Type = EkiOnOff
_Pm200frs02AlmFailFan_Object = MibScalar
pm200frs02AlmFailFan = _Pm200frs02AlmFailFan_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 0, 2),
    _Pm200frs02AlmFailFan_Type()
)
pm200frs02AlmFailFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmFailFan.setStatus("current")
_Pm200frs02AlmModGlobFail_Type = EkiOnOff
_Pm200frs02AlmModGlobFail_Object = MibScalar
pm200frs02AlmModGlobFail = _Pm200frs02AlmModGlobFail_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 0, 9),
    _Pm200frs02AlmModGlobFail_Type()
)
pm200frs02AlmModGlobFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmModGlobFail.setStatus("current")
_Pm200frs02AlmDefFuseA_Type = EkiOnOff
_Pm200frs02AlmDefFuseA_Object = MibScalar
pm200frs02AlmDefFuseA = _Pm200frs02AlmDefFuseA_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 0, 15),
    _Pm200frs02AlmDefFuseA_Type()
)
pm200frs02AlmDefFuseA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmDefFuseA.setStatus("current")
_Pm200frs02AlmDefFuseB_Type = EkiOnOff
_Pm200frs02AlmDefFuseB_Object = MibScalar
pm200frs02AlmDefFuseB = _Pm200frs02AlmDefFuseB_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 0, 16),
    _Pm200frs02AlmDefFuseB_Type()
)
pm200frs02AlmDefFuseB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmDefFuseB.setStatus("current")
_Pm200frs02AlmmsaModuleState_ObjectIdentity = ObjectIdentity
pm200frs02AlmmsaModuleState = _Pm200frs02AlmmsaModuleState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78)
)
_Pm200frs02AlmMsaInitialize_Type = EkiOnOff
_Pm200frs02AlmMsaInitialize_Object = MibScalar
pm200frs02AlmMsaInitialize = _Pm200frs02AlmMsaInitialize_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 1),
    _Pm200frs02AlmMsaInitialize_Type()
)
pm200frs02AlmMsaInitialize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaInitialize.setStatus("current")
_Pm200frs02AlmMsaLowPower_Type = EkiOnOff
_Pm200frs02AlmMsaLowPower_Object = MibScalar
pm200frs02AlmMsaLowPower = _Pm200frs02AlmMsaLowPower_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 2),
    _Pm200frs02AlmMsaLowPower_Type()
)
pm200frs02AlmMsaLowPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaLowPower.setStatus("current")
_Pm200frs02AlmMsaHighPowerUp_Type = EkiOnOff
_Pm200frs02AlmMsaHighPowerUp_Object = MibScalar
pm200frs02AlmMsaHighPowerUp = _Pm200frs02AlmMsaHighPowerUp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 3),
    _Pm200frs02AlmMsaHighPowerUp_Type()
)
pm200frs02AlmMsaHighPowerUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaHighPowerUp.setStatus("current")
_Pm200frs02AlmMsaTxOff_Type = EkiOnOff
_Pm200frs02AlmMsaTxOff_Object = MibScalar
pm200frs02AlmMsaTxOff = _Pm200frs02AlmMsaTxOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 4),
    _Pm200frs02AlmMsaTxOff_Type()
)
pm200frs02AlmMsaTxOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaTxOff.setStatus("current")
_Pm200frs02AlmMsaTxTurnOn_Type = EkiOnOff
_Pm200frs02AlmMsaTxTurnOn_Object = MibScalar
pm200frs02AlmMsaTxTurnOn = _Pm200frs02AlmMsaTxTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 5),
    _Pm200frs02AlmMsaTxTurnOn_Type()
)
pm200frs02AlmMsaTxTurnOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaTxTurnOn.setStatus("current")
_Pm200frs02AlmMsaReady_Type = EkiOnOff
_Pm200frs02AlmMsaReady_Object = MibScalar
pm200frs02AlmMsaReady = _Pm200frs02AlmMsaReady_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 6),
    _Pm200frs02AlmMsaReady_Type()
)
pm200frs02AlmMsaReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaReady.setStatus("current")
_Pm200frs02AlmMsaFault_Type = EkiOnOff
_Pm200frs02AlmMsaFault_Object = MibScalar
pm200frs02AlmMsaFault = _Pm200frs02AlmMsaFault_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 7),
    _Pm200frs02AlmMsaFault_Type()
)
pm200frs02AlmMsaFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaFault.setStatus("current")
_Pm200frs02AlmMsaTxTurnOff_Type = EkiOnOff
_Pm200frs02AlmMsaTxTurnOff_Object = MibScalar
pm200frs02AlmMsaTxTurnOff = _Pm200frs02AlmMsaTxTurnOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 8),
    _Pm200frs02AlmMsaTxTurnOff_Type()
)
pm200frs02AlmMsaTxTurnOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaTxTurnOff.setStatus("current")
_Pm200frs02AlmMsaHighPowerDown_Type = EkiOnOff
_Pm200frs02AlmMsaHighPowerDown_Object = MibScalar
pm200frs02AlmMsaHighPowerDown = _Pm200frs02AlmMsaHighPowerDown_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 1, 3, 78, 9),
    _Pm200frs02AlmMsaHighPowerDown_Type()
)
pm200frs02AlmMsaHighPowerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmMsaHighPowerDown.setStatus("current")
_Pm200frs02AlmClient_ObjectIdentity = ObjectIdentity
pm200frs02AlmClient = _Pm200frs02AlmClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2)
)
_Pm200frs02AlmClientNurg_ObjectIdentity = ObjectIdentity
pm200frs02AlmClientNurg = _Pm200frs02AlmClientNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 1)
)
_Pm200frs02AlmClientUrg_ObjectIdentity = ObjectIdentity
pm200frs02AlmClientUrg = _Pm200frs02AlmClientUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2)
)
_Pm200frs02AlmclientHostLaneFaultTable_Object = MibTable
pm200frs02AlmclientHostLaneFaultTable = _Pm200frs02AlmclientHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152)
)
if mibBuilder.loadTexts:
    pm200frs02AlmclientHostLaneFaultTable.setStatus("current")
_Pm200frs02AlmclientHostLaneFaultEntry_Object = MibTableRow
pm200frs02AlmclientHostLaneFaultEntry = _Pm200frs02AlmclientHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1)
)
pm200frs02AlmclientHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02AlmclientHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02AlmclientHostLaneFaultEntry.setStatus("current")


class _Pm200frs02AlmclientHostLaneFaultIndex_Type(Integer32):
    """Custom type pm200frs02AlmclientHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02AlmclientHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm200frs02AlmclientHostLaneFaultIndex_Object = MibTableColumn
pm200frs02AlmclientHostLaneFaultIndex = _Pm200frs02AlmclientHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 1),
    _Pm200frs02AlmclientHostLaneFaultIndex_Type()
)
pm200frs02AlmclientHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmclientHostLaneFaultIndex.setStatus("current")
_Pm200frs02AlmClientLossOfSyncPortn_Type = EkiOnOff
_Pm200frs02AlmClientLossOfSyncPortn_Object = MibTableColumn
pm200frs02AlmClientLossOfSyncPortn = _Pm200frs02AlmClientLossOfSyncPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 2),
    _Pm200frs02AlmClientLossOfSyncPortn_Type()
)
pm200frs02AlmClientLossOfSyncPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientLossOfSyncPortn.setStatus("current")
_Pm200frs02AlmClientInputLossOfSigPortn_Type = EkiOnOff
_Pm200frs02AlmClientInputLossOfSigPortn_Object = MibTableColumn
pm200frs02AlmClientInputLossOfSigPortn = _Pm200frs02AlmClientInputLossOfSigPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 3),
    _Pm200frs02AlmClientInputLossOfSigPortn_Type()
)
pm200frs02AlmClientInputLossOfSigPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientInputLossOfSigPortn.setStatus("current")
_Pm200frs02AlmClientLanesMarkerUnlockPortn_Type = EkiOnOff
_Pm200frs02AlmClientLanesMarkerUnlockPortn_Object = MibTableColumn
pm200frs02AlmClientLanesMarkerUnlockPortn = _Pm200frs02AlmClientLanesMarkerUnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 4),
    _Pm200frs02AlmClientLanesMarkerUnlockPortn_Type()
)
pm200frs02AlmClientLanesMarkerUnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientLanesMarkerUnlockPortn.setStatus("current")
_Pm200frs02AlmClientLanes6466UnlockPortn_Type = EkiOnOff
_Pm200frs02AlmClientLanes6466UnlockPortn_Object = MibTableColumn
pm200frs02AlmClientLanes6466UnlockPortn = _Pm200frs02AlmClientLanes6466UnlockPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 5),
    _Pm200frs02AlmClientLanes6466UnlockPortn_Type()
)
pm200frs02AlmClientLanes6466UnlockPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientLanes6466UnlockPortn.setStatus("current")
_Pm200frs02AlmClientLanesNotAlignedPortn_Type = EkiOnOff
_Pm200frs02AlmClientLanesNotAlignedPortn_Object = MibTableColumn
pm200frs02AlmClientLanesNotAlignedPortn = _Pm200frs02AlmClientLanesNotAlignedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 6),
    _Pm200frs02AlmClientLanesNotAlignedPortn_Type()
)
pm200frs02AlmClientLanesNotAlignedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientLanesNotAlignedPortn.setStatus("current")
_Pm200frs02AlmClientCsfDetectedPortn_Type = EkiOnOff
_Pm200frs02AlmClientCsfDetectedPortn_Object = MibTableColumn
pm200frs02AlmClientCsfDetectedPortn = _Pm200frs02AlmClientCsfDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 7),
    _Pm200frs02AlmClientCsfDetectedPortn_Type()
)
pm200frs02AlmClientCsfDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientCsfDetectedPortn.setStatus("current")
_Pm200frs02AlmClientTxHostLolPortn_Type = EkiOnOff
_Pm200frs02AlmClientTxHostLolPortn_Object = MibTableColumn
pm200frs02AlmClientTxHostLolPortn = _Pm200frs02AlmClientTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 10),
    _Pm200frs02AlmClientTxHostLolPortn_Type()
)
pm200frs02AlmClientTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientTxHostLolPortn.setStatus("current")
_Pm200frs02AlmClientLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm200frs02AlmClientLaneTxFifoErrorPortn_Object = MibTableColumn
pm200frs02AlmClientLaneTxFifoErrorPortn = _Pm200frs02AlmClientLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 2, 152, 1, 11),
    _Pm200frs02AlmClientLaneTxFifoErrorPortn_Type()
)
pm200frs02AlmClientLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientLaneTxFifoErrorPortn.setStatus("current")
_Pm200frs02AlmClientCrit_ObjectIdentity = ObjectIdentity
pm200frs02AlmClientCrit = _Pm200frs02AlmClientCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3)
)
_Pm200frs02AlmsynthAlmPortTable_Object = MibTable
pm200frs02AlmsynthAlmPortTable = _Pm200frs02AlmsynthAlmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    pm200frs02AlmsynthAlmPortTable.setStatus("current")
_Pm200frs02AlmsynthAlmPortEntry_Object = MibTableRow
pm200frs02AlmsynthAlmPortEntry = _Pm200frs02AlmsynthAlmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1)
)
pm200frs02AlmsynthAlmPortEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02AlmsynthAlmPortIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02AlmsynthAlmPortEntry.setStatus("current")


class _Pm200frs02AlmsynthAlmPortIndex_Type(Integer32):
    """Custom type pm200frs02AlmsynthAlmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02AlmsynthAlmPortIndex_Type.__name__ = "Integer32"
_Pm200frs02AlmsynthAlmPortIndex_Object = MibTableColumn
pm200frs02AlmsynthAlmPortIndex = _Pm200frs02AlmsynthAlmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 1),
    _Pm200frs02AlmsynthAlmPortIndex_Type()
)
pm200frs02AlmsynthAlmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmsynthAlmPortIndex.setStatus("current")
_Pm200frs02AlmSfpAbsentPortn_Type = EkiOnOff
_Pm200frs02AlmSfpAbsentPortn_Object = MibTableColumn
pm200frs02AlmSfpAbsentPortn = _Pm200frs02AlmSfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 2),
    _Pm200frs02AlmSfpAbsentPortn_Type()
)
pm200frs02AlmSfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmSfpAbsentPortn.setStatus("current")
_Pm200frs02AlmDdmAbsentPortn_Type = EkiOnOff
_Pm200frs02AlmDdmAbsentPortn_Object = MibTableColumn
pm200frs02AlmDdmAbsentPortn = _Pm200frs02AlmDdmAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 3),
    _Pm200frs02AlmDdmAbsentPortn_Type()
)
pm200frs02AlmDdmAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmDdmAbsentPortn.setStatus("current")
_Pm200frs02AlmHwFailAccPortn_Type = EkiOnOff
_Pm200frs02AlmHwFailAccPortn_Object = MibTableColumn
pm200frs02AlmHwFailAccPortn = _Pm200frs02AlmHwFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 5),
    _Pm200frs02AlmHwFailAccPortn_Type()
)
pm200frs02AlmHwFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmHwFailAccPortn.setStatus("current")
_Pm200frs02AlmDwLsdPortn_Type = EkiOnOff
_Pm200frs02AlmDwLsdPortn_Object = MibTableColumn
pm200frs02AlmDwLsdPortn = _Pm200frs02AlmDwLsdPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 6),
    _Pm200frs02AlmDwLsdPortn_Type()
)
pm200frs02AlmDwLsdPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmDwLsdPortn.setStatus("current")
_Pm200frs02AlmClientLocalOosPortn_Type = EkiOnOff
_Pm200frs02AlmClientLocalOosPortn_Object = MibTableColumn
pm200frs02AlmClientLocalOosPortn = _Pm200frs02AlmClientLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 7),
    _Pm200frs02AlmClientLocalOosPortn_Type()
)
pm200frs02AlmClientLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientLocalOosPortn.setStatus("current")
_Pm200frs02AlmClientRemoteOosPortn_Type = EkiOnOff
_Pm200frs02AlmClientRemoteOosPortn_Object = MibTableColumn
pm200frs02AlmClientRemoteOosPortn = _Pm200frs02AlmClientRemoteOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 8),
    _Pm200frs02AlmClientRemoteOosPortn_Type()
)
pm200frs02AlmClientRemoteOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmClientRemoteOosPortn.setStatus("current")
_Pm200frs02AlmDwCaisPortn_Type = EkiOnOff
_Pm200frs02AlmDwCaisPortn_Object = MibTableColumn
pm200frs02AlmDwCaisPortn = _Pm200frs02AlmDwCaisPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 9),
    _Pm200frs02AlmDwCaisPortn_Type()
)
pm200frs02AlmDwCaisPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmDwCaisPortn.setStatus("current")
_Pm200frs02AlmSfpDdmWarningPortn_Type = EkiOnOff
_Pm200frs02AlmSfpDdmWarningPortn_Object = MibTableColumn
pm200frs02AlmSfpDdmWarningPortn = _Pm200frs02AlmSfpDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 10),
    _Pm200frs02AlmSfpDdmWarningPortn_Type()
)
pm200frs02AlmSfpDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmSfpDdmWarningPortn.setStatus("current")
_Pm200frs02AlmSfpDdmAlmPortn_Type = EkiOnOff
_Pm200frs02AlmSfpDdmAlmPortn_Object = MibTableColumn
pm200frs02AlmSfpDdmAlmPortn = _Pm200frs02AlmSfpDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 11),
    _Pm200frs02AlmSfpDdmAlmPortn_Type()
)
pm200frs02AlmSfpDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmSfpDdmAlmPortn.setStatus("current")
_Pm200frs02AlmFailAccPortn_Type = EkiOnOff
_Pm200frs02AlmFailAccPortn_Object = MibTableColumn
pm200frs02AlmFailAccPortn = _Pm200frs02AlmFailAccPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 13),
    _Pm200frs02AlmFailAccPortn_Type()
)
pm200frs02AlmFailAccPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmFailAccPortn.setStatus("current")
_Pm200frs02AlmUpCsfPortn_Type = EkiOnOff
_Pm200frs02AlmUpCsfPortn_Object = MibTableColumn
pm200frs02AlmUpCsfPortn = _Pm200frs02AlmUpCsfPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 2, 3, 8, 1, 17),
    _Pm200frs02AlmUpCsfPortn_Type()
)
pm200frs02AlmUpCsfPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmUpCsfPortn.setStatus("current")
_Pm200frs02AlmLine_ObjectIdentity = ObjectIdentity
pm200frs02AlmLine = _Pm200frs02AlmLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3)
)
_Pm200frs02AlmLineNurg_ObjectIdentity = ObjectIdentity
pm200frs02AlmLineNurg = _Pm200frs02AlmLineNurg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1)
)
_Pm200frs02AlmlineNetworkLaneAlarmWarning1Table_Object = MibTable
pm200frs02AlmlineNetworkLaneAlarmWarning1Table = _Pm200frs02AlmlineNetworkLaneAlarmWarning1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184)
)
if mibBuilder.loadTexts:
    pm200frs02AlmlineNetworkLaneAlarmWarning1Table.setStatus("current")
_Pm200frs02AlmlineNetworkLaneAlarmWarning1Entry_Object = MibTableRow
pm200frs02AlmlineNetworkLaneAlarmWarning1Entry = _Pm200frs02AlmlineNetworkLaneAlarmWarning1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1)
)
pm200frs02AlmlineNetworkLaneAlarmWarning1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02AlmlineNetworkLaneAlarmWarning1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02AlmlineNetworkLaneAlarmWarning1Entry.setStatus("current")


class _Pm200frs02AlmlineNetworkLaneAlarmWarning1Index_Type(Integer32):
    """Custom type pm200frs02AlmlineNetworkLaneAlarmWarning1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02AlmlineNetworkLaneAlarmWarning1Index_Type.__name__ = "Integer32"
_Pm200frs02AlmlineNetworkLaneAlarmWarning1Index_Object = MibTableColumn
pm200frs02AlmlineNetworkLaneAlarmWarning1Index = _Pm200frs02AlmlineNetworkLaneAlarmWarning1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 1),
    _Pm200frs02AlmlineNetworkLaneAlarmWarning1Index_Type()
)
pm200frs02AlmlineNetworkLaneAlarmWarning1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmlineNetworkLaneAlarmWarning1Index.setStatus("current")
_Pm200frs02AlmLineRxPowerLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineRxPowerLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineRxPowerLowAlarmPortn = _Pm200frs02AlmLineRxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 2),
    _Pm200frs02AlmLineRxPowerLowAlarmPortn_Type()
)
pm200frs02AlmLineRxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineRxPowerLowAlarmPortn.setStatus("current")
_Pm200frs02AlmLineRxPowerLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineRxPowerLowWarningPortn_Object = MibTableColumn
pm200frs02AlmLineRxPowerLowWarningPortn = _Pm200frs02AlmLineRxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 3),
    _Pm200frs02AlmLineRxPowerLowWarningPortn_Type()
)
pm200frs02AlmLineRxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineRxPowerLowWarningPortn.setStatus("current")
_Pm200frs02AlmLineRxPowerHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineRxPowerHighWarningPortn_Object = MibTableColumn
pm200frs02AlmLineRxPowerHighWarningPortn = _Pm200frs02AlmLineRxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 4),
    _Pm200frs02AlmLineRxPowerHighWarningPortn_Type()
)
pm200frs02AlmLineRxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineRxPowerHighWarningPortn.setStatus("current")
_Pm200frs02AlmLineRxPowerHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineRxPowerHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineRxPowerHighAlarmPortn = _Pm200frs02AlmLineRxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 5),
    _Pm200frs02AlmLineRxPowerHighAlarmPortn_Type()
)
pm200frs02AlmLineRxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineRxPowerHighAlarmPortn.setStatus("current")
_Pm200frs02AlmLineLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineLaserTempLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineLaserTempLowAlarmPortn = _Pm200frs02AlmLineLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 6),
    _Pm200frs02AlmLineLaserTempLowAlarmPortn_Type()
)
pm200frs02AlmLineLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLaserTempLowAlarmPortn.setStatus("current")
_Pm200frs02AlmLineLaserTempLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineLaserTempLowWarningPortn_Object = MibTableColumn
pm200frs02AlmLineLaserTempLowWarningPortn = _Pm200frs02AlmLineLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 7),
    _Pm200frs02AlmLineLaserTempLowWarningPortn_Type()
)
pm200frs02AlmLineLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLaserTempLowWarningPortn.setStatus("current")
_Pm200frs02AlmLineLaserTempHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineLaserTempHighWarningPortn_Object = MibTableColumn
pm200frs02AlmLineLaserTempHighWarningPortn = _Pm200frs02AlmLineLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 8),
    _Pm200frs02AlmLineLaserTempHighWarningPortn_Type()
)
pm200frs02AlmLineLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLaserTempHighWarningPortn.setStatus("current")
_Pm200frs02AlmLineLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineLaserTempHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineLaserTempHighAlarmPortn = _Pm200frs02AlmLineLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 9),
    _Pm200frs02AlmLineLaserTempHighAlarmPortn_Type()
)
pm200frs02AlmLineLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLaserTempHighAlarmPortn.setStatus("current")
_Pm200frs02AlmLineTxPowerLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineTxPowerLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineTxPowerLowAlarmPortn = _Pm200frs02AlmLineTxPowerLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 10),
    _Pm200frs02AlmLineTxPowerLowAlarmPortn_Type()
)
pm200frs02AlmLineTxPowerLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineTxPowerLowAlarmPortn.setStatus("current")
_Pm200frs02AlmLineTxPowerLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineTxPowerLowWarningPortn_Object = MibTableColumn
pm200frs02AlmLineTxPowerLowWarningPortn = _Pm200frs02AlmLineTxPowerLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 11),
    _Pm200frs02AlmLineTxPowerLowWarningPortn_Type()
)
pm200frs02AlmLineTxPowerLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineTxPowerLowWarningPortn.setStatus("current")
_Pm200frs02AlmLineTxPowerHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineTxPowerHighWarningPortn_Object = MibTableColumn
pm200frs02AlmLineTxPowerHighWarningPortn = _Pm200frs02AlmLineTxPowerHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 12),
    _Pm200frs02AlmLineTxPowerHighWarningPortn_Type()
)
pm200frs02AlmLineTxPowerHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineTxPowerHighWarningPortn.setStatus("current")
_Pm200frs02AlmLineTxPowerHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineTxPowerHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineTxPowerHighAlarmPortn = _Pm200frs02AlmLineTxPowerHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 13),
    _Pm200frs02AlmLineTxPowerHighAlarmPortn_Type()
)
pm200frs02AlmLineTxPowerHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineTxPowerHighAlarmPortn.setStatus("current")
_Pm200frs02AlmLineBiasLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineBiasLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineBiasLowAlarmPortn = _Pm200frs02AlmLineBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 14),
    _Pm200frs02AlmLineBiasLowAlarmPortn_Type()
)
pm200frs02AlmLineBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineBiasLowAlarmPortn.setStatus("current")
_Pm200frs02AlmLineBiasLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineBiasLowWarningPortn_Object = MibTableColumn
pm200frs02AlmLineBiasLowWarningPortn = _Pm200frs02AlmLineBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 15),
    _Pm200frs02AlmLineBiasLowWarningPortn_Type()
)
pm200frs02AlmLineBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineBiasLowWarningPortn.setStatus("current")
_Pm200frs02AlmLineBiasHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineBiasHighWarningPortn_Object = MibTableColumn
pm200frs02AlmLineBiasHighWarningPortn = _Pm200frs02AlmLineBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 16),
    _Pm200frs02AlmLineBiasHighWarningPortn_Type()
)
pm200frs02AlmLineBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineBiasHighWarningPortn.setStatus("current")
_Pm200frs02AlmLineBiasHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmLineBiasHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmLineBiasHighAlarmPortn = _Pm200frs02AlmLineBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 184, 1, 17),
    _Pm200frs02AlmLineBiasHighAlarmPortn_Type()
)
pm200frs02AlmLineBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineBiasHighAlarmPortn.setStatus("current")
_Pm200frs02AlmlineNetworkLaneAlarmWarning2Table_Object = MibTable
pm200frs02AlmlineNetworkLaneAlarmWarning2Table = _Pm200frs02AlmlineNetworkLaneAlarmWarning2Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188)
)
if mibBuilder.loadTexts:
    pm200frs02AlmlineNetworkLaneAlarmWarning2Table.setStatus("current")
_Pm200frs02AlmlineNetworkLaneAlarmWarning2Entry_Object = MibTableRow
pm200frs02AlmlineNetworkLaneAlarmWarning2Entry = _Pm200frs02AlmlineNetworkLaneAlarmWarning2Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1)
)
pm200frs02AlmlineNetworkLaneAlarmWarning2Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02AlmlineNetworkLaneAlarmWarning2Index"),
)
if mibBuilder.loadTexts:
    pm200frs02AlmlineNetworkLaneAlarmWarning2Entry.setStatus("current")


class _Pm200frs02AlmlineNetworkLaneAlarmWarning2Index_Type(Integer32):
    """Custom type pm200frs02AlmlineNetworkLaneAlarmWarning2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02AlmlineNetworkLaneAlarmWarning2Index_Type.__name__ = "Integer32"
_Pm200frs02AlmlineNetworkLaneAlarmWarning2Index_Object = MibTableColumn
pm200frs02AlmlineNetworkLaneAlarmWarning2Index = _Pm200frs02AlmlineNetworkLaneAlarmWarning2Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 1),
    _Pm200frs02AlmlineNetworkLaneAlarmWarning2Index_Type()
)
pm200frs02AlmlineNetworkLaneAlarmWarning2Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmlineNetworkLaneAlarmWarning2Index.setStatus("current")
_Pm200frs02AlmTxModulatorBiasLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmTxModulatorBiasLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmTxModulatorBiasLowAlarmPortn = _Pm200frs02AlmTxModulatorBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 2),
    _Pm200frs02AlmTxModulatorBiasLowAlarmPortn_Type()
)
pm200frs02AlmTxModulatorBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTxModulatorBiasLowAlarmPortn.setStatus("current")
_Pm200frs02AlmTxModulatorBiasLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmTxModulatorBiasLowWarningPortn_Object = MibTableColumn
pm200frs02AlmTxModulatorBiasLowWarningPortn = _Pm200frs02AlmTxModulatorBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 3),
    _Pm200frs02AlmTxModulatorBiasLowWarningPortn_Type()
)
pm200frs02AlmTxModulatorBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTxModulatorBiasLowWarningPortn.setStatus("current")
_Pm200frs02AlmTxModulatorBiasHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmTxModulatorBiasHighWarningPortn_Object = MibTableColumn
pm200frs02AlmTxModulatorBiasHighWarningPortn = _Pm200frs02AlmTxModulatorBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 4),
    _Pm200frs02AlmTxModulatorBiasHighWarningPortn_Type()
)
pm200frs02AlmTxModulatorBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTxModulatorBiasHighWarningPortn.setStatus("current")
_Pm200frs02AlmTxModulatorBiasHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmTxModulatorBiasHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmTxModulatorBiasHighAlarmPortn = _Pm200frs02AlmTxModulatorBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 5),
    _Pm200frs02AlmTxModulatorBiasHighAlarmPortn_Type()
)
pm200frs02AlmTxModulatorBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmTxModulatorBiasHighAlarmPortn.setStatus("current")
_Pm200frs02AlmRxLaserTempLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserTempLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmRxLaserTempLowAlarmPortn = _Pm200frs02AlmRxLaserTempLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 6),
    _Pm200frs02AlmRxLaserTempLowAlarmPortn_Type()
)
pm200frs02AlmRxLaserTempLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserTempLowAlarmPortn.setStatus("current")
_Pm200frs02AlmRxLaserTempLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserTempLowWarningPortn_Object = MibTableColumn
pm200frs02AlmRxLaserTempLowWarningPortn = _Pm200frs02AlmRxLaserTempLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 7),
    _Pm200frs02AlmRxLaserTempLowWarningPortn_Type()
)
pm200frs02AlmRxLaserTempLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserTempLowWarningPortn.setStatus("current")
_Pm200frs02AlmRxLaserTempHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserTempHighWarningPortn_Object = MibTableColumn
pm200frs02AlmRxLaserTempHighWarningPortn = _Pm200frs02AlmRxLaserTempHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 8),
    _Pm200frs02AlmRxLaserTempHighWarningPortn_Type()
)
pm200frs02AlmRxLaserTempHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserTempHighWarningPortn.setStatus("current")
_Pm200frs02AlmRxLaserTempHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserTempHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmRxLaserTempHighAlarmPortn = _Pm200frs02AlmRxLaserTempHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 9),
    _Pm200frs02AlmRxLaserTempHighAlarmPortn_Type()
)
pm200frs02AlmRxLaserTempHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserTempHighAlarmPortn.setStatus("current")
_Pm200frs02AlmRxLaserOutputLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserOutputLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmRxLaserOutputLowAlarmPortn = _Pm200frs02AlmRxLaserOutputLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 10),
    _Pm200frs02AlmRxLaserOutputLowAlarmPortn_Type()
)
pm200frs02AlmRxLaserOutputLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserOutputLowAlarmPortn.setStatus("current")
_Pm200frs02AlmRxLaserOutputLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserOutputLowWarningPortn_Object = MibTableColumn
pm200frs02AlmRxLaserOutputLowWarningPortn = _Pm200frs02AlmRxLaserOutputLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 11),
    _Pm200frs02AlmRxLaserOutputLowWarningPortn_Type()
)
pm200frs02AlmRxLaserOutputLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserOutputLowWarningPortn.setStatus("current")
_Pm200frs02AlmRxLaserOutputHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserOutputHighWarningPortn_Object = MibTableColumn
pm200frs02AlmRxLaserOutputHighWarningPortn = _Pm200frs02AlmRxLaserOutputHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 12),
    _Pm200frs02AlmRxLaserOutputHighWarningPortn_Type()
)
pm200frs02AlmRxLaserOutputHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserOutputHighWarningPortn.setStatus("current")
_Pm200frs02AlmRxLaserOutputHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserOutputHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmRxLaserOutputHighAlarmPortn = _Pm200frs02AlmRxLaserOutputHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 13),
    _Pm200frs02AlmRxLaserOutputHighAlarmPortn_Type()
)
pm200frs02AlmRxLaserOutputHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserOutputHighAlarmPortn.setStatus("current")
_Pm200frs02AlmRxLaserBiasLowAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserBiasLowAlarmPortn_Object = MibTableColumn
pm200frs02AlmRxLaserBiasLowAlarmPortn = _Pm200frs02AlmRxLaserBiasLowAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 14),
    _Pm200frs02AlmRxLaserBiasLowAlarmPortn_Type()
)
pm200frs02AlmRxLaserBiasLowAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserBiasLowAlarmPortn.setStatus("current")
_Pm200frs02AlmRxLaserBiasLowWarningPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserBiasLowWarningPortn_Object = MibTableColumn
pm200frs02AlmRxLaserBiasLowWarningPortn = _Pm200frs02AlmRxLaserBiasLowWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 15),
    _Pm200frs02AlmRxLaserBiasLowWarningPortn_Type()
)
pm200frs02AlmRxLaserBiasLowWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserBiasLowWarningPortn.setStatus("current")
_Pm200frs02AlmRxLaserBiasHighWarningPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserBiasHighWarningPortn_Object = MibTableColumn
pm200frs02AlmRxLaserBiasHighWarningPortn = _Pm200frs02AlmRxLaserBiasHighWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 16),
    _Pm200frs02AlmRxLaserBiasHighWarningPortn_Type()
)
pm200frs02AlmRxLaserBiasHighWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserBiasHighWarningPortn.setStatus("current")
_Pm200frs02AlmRxLaserBiasHighAlarmPortn_Type = EkiOnOff
_Pm200frs02AlmRxLaserBiasHighAlarmPortn_Object = MibTableColumn
pm200frs02AlmRxLaserBiasHighAlarmPortn = _Pm200frs02AlmRxLaserBiasHighAlarmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 1, 188, 1, 17),
    _Pm200frs02AlmRxLaserBiasHighAlarmPortn_Type()
)
pm200frs02AlmRxLaserBiasHighAlarmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmRxLaserBiasHighAlarmPortn.setStatus("current")
_Pm200frs02AlmLineUrg_ObjectIdentity = ObjectIdentity
pm200frs02AlmLineUrg = _Pm200frs02AlmLineUrg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2)
)
_Pm200frs02AlmlineHostLaneFaultTable_Object = MibTable
pm200frs02AlmlineHostLaneFaultTable = _Pm200frs02AlmlineHostLaneFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196)
)
if mibBuilder.loadTexts:
    pm200frs02AlmlineHostLaneFaultTable.setStatus("current")
_Pm200frs02AlmlineHostLaneFaultEntry_Object = MibTableRow
pm200frs02AlmlineHostLaneFaultEntry = _Pm200frs02AlmlineHostLaneFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1)
)
pm200frs02AlmlineHostLaneFaultEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02AlmlineHostLaneFaultIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02AlmlineHostLaneFaultEntry.setStatus("current")


class _Pm200frs02AlmlineHostLaneFaultIndex_Type(Integer32):
    """Custom type pm200frs02AlmlineHostLaneFaultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02AlmlineHostLaneFaultIndex_Type.__name__ = "Integer32"
_Pm200frs02AlmlineHostLaneFaultIndex_Object = MibTableColumn
pm200frs02AlmlineHostLaneFaultIndex = _Pm200frs02AlmlineHostLaneFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 1),
    _Pm200frs02AlmlineHostLaneFaultIndex_Type()
)
pm200frs02AlmlineHostLaneFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmlineHostLaneFaultIndex.setStatus("current")
_Pm200frs02AlmLineInputLossOfSignalPortn_Type = EkiOnOff
_Pm200frs02AlmLineInputLossOfSignalPortn_Object = MibTableColumn
pm200frs02AlmLineInputLossOfSignalPortn = _Pm200frs02AlmLineInputLossOfSignalPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 2),
    _Pm200frs02AlmLineInputLossOfSignalPortn_Type()
)
pm200frs02AlmLineInputLossOfSignalPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineInputLossOfSignalPortn.setStatus("current")
_Pm200frs02AlmLineLossOfFramePortn_Type = EkiOnOff
_Pm200frs02AlmLineLossOfFramePortn_Object = MibTableColumn
pm200frs02AlmLineLossOfFramePortn = _Pm200frs02AlmLineLossOfFramePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 3),
    _Pm200frs02AlmLineLossOfFramePortn_Type()
)
pm200frs02AlmLineLossOfFramePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLossOfFramePortn.setStatus("current")
_Pm200frs02AlmLineSmBdiInsertedPortn_Type = EkiOnOff
_Pm200frs02AlmLineSmBdiInsertedPortn_Object = MibTableColumn
pm200frs02AlmLineSmBdiInsertedPortn = _Pm200frs02AlmLineSmBdiInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 4),
    _Pm200frs02AlmLineSmBdiInsertedPortn_Type()
)
pm200frs02AlmLineSmBdiInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineSmBdiInsertedPortn.setStatus("current")
_Pm200frs02AlmLineSmBdiDetectedPortn_Type = EkiOnOff
_Pm200frs02AlmLineSmBdiDetectedPortn_Object = MibTableColumn
pm200frs02AlmLineSmBdiDetectedPortn = _Pm200frs02AlmLineSmBdiDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 5),
    _Pm200frs02AlmLineSmBdiDetectedPortn_Type()
)
pm200frs02AlmLineSmBdiDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineSmBdiDetectedPortn.setStatus("current")
_Pm200frs02AlmLineSmIaeInsertedPortn_Type = EkiOnOff
_Pm200frs02AlmLineSmIaeInsertedPortn_Object = MibTableColumn
pm200frs02AlmLineSmIaeInsertedPortn = _Pm200frs02AlmLineSmIaeInsertedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 6),
    _Pm200frs02AlmLineSmIaeInsertedPortn_Type()
)
pm200frs02AlmLineSmIaeInsertedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineSmIaeInsertedPortn.setStatus("current")
_Pm200frs02AlmLineSmIaeDetectedPortn_Type = EkiOnOff
_Pm200frs02AlmLineSmIaeDetectedPortn_Object = MibTableColumn
pm200frs02AlmLineSmIaeDetectedPortn = _Pm200frs02AlmLineSmIaeDetectedPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 7),
    _Pm200frs02AlmLineSmIaeDetectedPortn_Type()
)
pm200frs02AlmLineSmIaeDetectedPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineSmIaeDetectedPortn.setStatus("current")
_Pm200frs02AlmLineTxHostLolPortn_Type = EkiOnOff
_Pm200frs02AlmLineTxHostLolPortn_Object = MibTableColumn
pm200frs02AlmLineTxHostLolPortn = _Pm200frs02AlmLineTxHostLolPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 10),
    _Pm200frs02AlmLineTxHostLolPortn_Type()
)
pm200frs02AlmLineTxHostLolPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineTxHostLolPortn.setStatus("current")
_Pm200frs02AlmLineLaneTxFifoErrorPortn_Type = EkiOnOff
_Pm200frs02AlmLineLaneTxFifoErrorPortn_Object = MibTableColumn
pm200frs02AlmLineLaneTxFifoErrorPortn = _Pm200frs02AlmLineLaneTxFifoErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 2, 196, 1, 11),
    _Pm200frs02AlmLineLaneTxFifoErrorPortn_Type()
)
pm200frs02AlmLineLaneTxFifoErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLaneTxFifoErrorPortn.setStatus("current")
_Pm200frs02AlmLineCrit_ObjectIdentity = ObjectIdentity
pm200frs02AlmLineCrit = _Pm200frs02AlmLineCrit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3)
)
_Pm200frs02AlmsynthAlmLineTable_Object = MibTable
pm200frs02AlmsynthAlmLineTable = _Pm200frs02AlmsynthAlmLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40)
)
if mibBuilder.loadTexts:
    pm200frs02AlmsynthAlmLineTable.setStatus("current")
_Pm200frs02AlmsynthAlmLineEntry_Object = MibTableRow
pm200frs02AlmsynthAlmLineEntry = _Pm200frs02AlmsynthAlmLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1)
)
pm200frs02AlmsynthAlmLineEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02AlmsynthAlmLineIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02AlmsynthAlmLineEntry.setStatus("current")


class _Pm200frs02AlmsynthAlmLineIndex_Type(Integer32):
    """Custom type pm200frs02AlmsynthAlmLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02AlmsynthAlmLineIndex_Type.__name__ = "Integer32"
_Pm200frs02AlmsynthAlmLineIndex_Object = MibTableColumn
pm200frs02AlmsynthAlmLineIndex = _Pm200frs02AlmsynthAlmLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 1),
    _Pm200frs02AlmsynthAlmLineIndex_Type()
)
pm200frs02AlmsynthAlmLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmsynthAlmLineIndex.setStatus("current")
_Pm200frs02AlmXfpAbsentPortn_Type = EkiOnOff
_Pm200frs02AlmXfpAbsentPortn_Object = MibTableColumn
pm200frs02AlmXfpAbsentPortn = _Pm200frs02AlmXfpAbsentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 2),
    _Pm200frs02AlmXfpAbsentPortn_Type()
)
pm200frs02AlmXfpAbsentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmXfpAbsentPortn.setStatus("current")
_Pm200frs02AlmXfpInitNotComplPortn_Type = EkiOnOff
_Pm200frs02AlmXfpInitNotComplPortn_Object = MibTableColumn
pm200frs02AlmXfpInitNotComplPortn = _Pm200frs02AlmXfpInitNotComplPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 3),
    _Pm200frs02AlmXfpInitNotComplPortn_Type()
)
pm200frs02AlmXfpInitNotComplPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmXfpInitNotComplPortn.setStatus("current")
_Pm200frs02AlmLineHwFailPortn_Type = EkiOnOff
_Pm200frs02AlmLineHwFailPortn_Object = MibTableColumn
pm200frs02AlmLineHwFailPortn = _Pm200frs02AlmLineHwFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 5),
    _Pm200frs02AlmLineHwFailPortn_Type()
)
pm200frs02AlmLineHwFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineHwFailPortn.setStatus("current")
_Pm200frs02AlmXfpTxOffPortn_Type = EkiOnOff
_Pm200frs02AlmXfpTxOffPortn_Object = MibTableColumn
pm200frs02AlmXfpTxOffPortn = _Pm200frs02AlmXfpTxOffPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 6),
    _Pm200frs02AlmXfpTxOffPortn_Type()
)
pm200frs02AlmXfpTxOffPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmXfpTxOffPortn.setStatus("current")
_Pm200frs02AlmLineLocalOosPortn_Type = EkiOnOff
_Pm200frs02AlmLineLocalOosPortn_Object = MibTableColumn
pm200frs02AlmLineLocalOosPortn = _Pm200frs02AlmLineLocalOosPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 7),
    _Pm200frs02AlmLineLocalOosPortn_Type()
)
pm200frs02AlmLineLocalOosPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineLocalOosPortn.setStatus("current")
_Pm200frs02AlmUpRdiInsPortn_Type = EkiOnOff
_Pm200frs02AlmUpRdiInsPortn_Object = MibTableColumn
pm200frs02AlmUpRdiInsPortn = _Pm200frs02AlmUpRdiInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 9),
    _Pm200frs02AlmUpRdiInsPortn_Type()
)
pm200frs02AlmUpRdiInsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmUpRdiInsPortn.setStatus("current")
_Pm200frs02AlmLineDdmWarningPortn_Type = EkiOnOff
_Pm200frs02AlmLineDdmWarningPortn_Object = MibTableColumn
pm200frs02AlmLineDdmWarningPortn = _Pm200frs02AlmLineDdmWarningPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 10),
    _Pm200frs02AlmLineDdmWarningPortn_Type()
)
pm200frs02AlmLineDdmWarningPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineDdmWarningPortn.setStatus("current")
_Pm200frs02AlmLineDdmAlmPortn_Type = EkiOnOff
_Pm200frs02AlmLineDdmAlmPortn_Object = MibTableColumn
pm200frs02AlmLineDdmAlmPortn = _Pm200frs02AlmLineDdmAlmPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 11),
    _Pm200frs02AlmLineDdmAlmPortn_Type()
)
pm200frs02AlmLineDdmAlmPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineDdmAlmPortn.setStatus("current")
_Pm200frs02AlmLineFailPortn_Type = EkiOnOff
_Pm200frs02AlmLineFailPortn_Object = MibTableColumn
pm200frs02AlmLineFailPortn = _Pm200frs02AlmLineFailPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 13),
    _Pm200frs02AlmLineFailPortn_Type()
)
pm200frs02AlmLineFailPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineFailPortn.setStatus("current")
_Pm200frs02AlmLineActivePortn_Type = EkiOnOff
_Pm200frs02AlmLineActivePortn_Object = MibTableColumn
pm200frs02AlmLineActivePortn = _Pm200frs02AlmLineActivePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 2, 3, 3, 40, 1, 17),
    _Pm200frs02AlmLineActivePortn_Type()
)
pm200frs02AlmLineActivePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02AlmLineActivePortn.setStatus("current")
_Pm200frs02measures_ObjectIdentity = ObjectIdentity
pm200frs02measures = _Pm200frs02measures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3)
)
_Pm200frs02MesrOther_ObjectIdentity = ObjectIdentity
pm200frs02MesrOther = _Pm200frs02MesrOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1)
)
_Pm200frs02Mesrsynth0_Type = EkiMeasureType
_Pm200frs02Mesrsynth0_Object = MibScalar
pm200frs02Mesrsynth0 = _Pm200frs02Mesrsynth0_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 0),
    _Pm200frs02Mesrsynth0_Type()
)
pm200frs02Mesrsynth0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Mesrsynth0.setStatus("deprecated")
_Pm200frs02Mesrsynth1_Type = EkiMeasureType
_Pm200frs02Mesrsynth1_Object = MibScalar
pm200frs02Mesrsynth1 = _Pm200frs02Mesrsynth1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 1),
    _Pm200frs02Mesrsynth1_Type()
)
pm200frs02Mesrsynth1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Mesrsynth1.setStatus("deprecated")


class _Pm200frs02MesrpmIntervalNumber_Type(Unsigned32):
    """Custom type pm200frs02MesrpmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrpmIntervalNumber_Type.__name__ = "Unsigned32"
_Pm200frs02MesrpmIntervalNumber_Object = MibScalar
pm200frs02MesrpmIntervalNumber = _Pm200frs02MesrpmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 7),
    _Pm200frs02MesrpmIntervalNumber_Type()
)
pm200frs02MesrpmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrpmIntervalNumber.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserOutputPwrAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxLaserOutputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserOutputPwrAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxLaserOutputPwrAverage_Object = MibScalar
pm200frs02MesrlineNetTxLaserOutputPwrAverage = _Pm200frs02MesrlineNetTxLaserOutputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 196),
    _Pm200frs02MesrlineNetTxLaserOutputPwrAverage_Type()
)
pm200frs02MesrlineNetTxLaserOutputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrAverage.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserTempAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxLaserTempAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserTempAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxLaserTempAverage_Object = MibScalar
pm200frs02MesrlineNetTxLaserTempAverage = _Pm200frs02MesrlineNetTxLaserTempAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 197),
    _Pm200frs02MesrlineNetTxLaserTempAverage_Type()
)
pm200frs02MesrlineNetTxLaserTempAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempAverage.setStatus("current")


class _Pm200frs02MesrlineNetTxBiasCurrentAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxBiasCurrentAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxBiasCurrentAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxBiasCurrentAverage_Object = MibScalar
pm200frs02MesrlineNetTxBiasCurrentAverage = _Pm200frs02MesrlineNetTxBiasCurrentAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 198),
    _Pm200frs02MesrlineNetTxBiasCurrentAverage_Type()
)
pm200frs02MesrlineNetTxBiasCurrentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentAverage.setStatus("current")


class _Pm200frs02MesrlineNetRxInputPwrAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetRxInputPwrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetRxInputPwrAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetRxInputPwrAverage_Object = MibScalar
pm200frs02MesrlineNetRxInputPwrAverage = _Pm200frs02MesrlineNetRxInputPwrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 199),
    _Pm200frs02MesrlineNetRxInputPwrAverage_Type()
)
pm200frs02MesrlineNetRxInputPwrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrAverage.setStatus("current")


class _Pm200frs02MesrlineResidualChromaticDispAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineResidualChromaticDispAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineResidualChromaticDispAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineResidualChromaticDispAverage_Object = MibScalar
pm200frs02MesrlineResidualChromaticDispAverage = _Pm200frs02MesrlineResidualChromaticDispAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 200),
    _Pm200frs02MesrlineResidualChromaticDispAverage_Type()
)
pm200frs02MesrlineResidualChromaticDispAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispAverage.setStatus("current")


class _Pm200frs02MesrlineDiffGroupDelayAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineDiffGroupDelayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineDiffGroupDelayAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineDiffGroupDelayAverage_Object = MibScalar
pm200frs02MesrlineDiffGroupDelayAverage = _Pm200frs02MesrlineDiffGroupDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 201),
    _Pm200frs02MesrlineDiffGroupDelayAverage_Type()
)
pm200frs02MesrlineDiffGroupDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayAverage.setStatus("current")


class _Pm200frs02MesrlineQFactorAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineQFactorAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineQFactorAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineQFactorAverage_Object = MibScalar
pm200frs02MesrlineQFactorAverage = _Pm200frs02MesrlineQFactorAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 202),
    _Pm200frs02MesrlineQFactorAverage_Type()
)
pm200frs02MesrlineQFactorAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorAverage.setStatus("current")


class _Pm200frs02MesrlineCarrierFreqOffsetAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineCarrierFreqOffsetAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineCarrierFreqOffsetAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineCarrierFreqOffsetAverage_Object = MibScalar
pm200frs02MesrlineCarrierFreqOffsetAverage = _Pm200frs02MesrlineCarrierFreqOffsetAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 203),
    _Pm200frs02MesrlineCarrierFreqOffsetAverage_Type()
)
pm200frs02MesrlineCarrierFreqOffsetAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetAverage.setStatus("current")


class _Pm200frs02MesrlineOsnrAverage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineOsnrAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineOsnrAverage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineOsnrAverage_Object = MibScalar
pm200frs02MesrlineOsnrAverage = _Pm200frs02MesrlineOsnrAverage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 204),
    _Pm200frs02MesrlineOsnrAverage_Type()
)
pm200frs02MesrlineOsnrAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrAverage.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserOutputPwrMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxLaserOutputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserOutputPwrMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxLaserOutputPwrMin_Object = MibScalar
pm200frs02MesrlineNetTxLaserOutputPwrMin = _Pm200frs02MesrlineNetTxLaserOutputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 212),
    _Pm200frs02MesrlineNetTxLaserOutputPwrMin_Type()
)
pm200frs02MesrlineNetTxLaserOutputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrMin.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserTempMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxLaserTempMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserTempMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxLaserTempMin_Object = MibScalar
pm200frs02MesrlineNetTxLaserTempMin = _Pm200frs02MesrlineNetTxLaserTempMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 213),
    _Pm200frs02MesrlineNetTxLaserTempMin_Type()
)
pm200frs02MesrlineNetTxLaserTempMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempMin.setStatus("current")


class _Pm200frs02MesrlineNetTxBiasCurrentMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxBiasCurrentMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxBiasCurrentMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxBiasCurrentMin_Object = MibScalar
pm200frs02MesrlineNetTxBiasCurrentMin = _Pm200frs02MesrlineNetTxBiasCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 214),
    _Pm200frs02MesrlineNetTxBiasCurrentMin_Type()
)
pm200frs02MesrlineNetTxBiasCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentMin.setStatus("current")


class _Pm200frs02MesrlineNetRxInputPwrMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetRxInputPwrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetRxInputPwrMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetRxInputPwrMin_Object = MibScalar
pm200frs02MesrlineNetRxInputPwrMin = _Pm200frs02MesrlineNetRxInputPwrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 215),
    _Pm200frs02MesrlineNetRxInputPwrMin_Type()
)
pm200frs02MesrlineNetRxInputPwrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrMin.setStatus("current")


class _Pm200frs02MesrlineResidualChromaticDispMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineResidualChromaticDispMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineResidualChromaticDispMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineResidualChromaticDispMin_Object = MibScalar
pm200frs02MesrlineResidualChromaticDispMin = _Pm200frs02MesrlineResidualChromaticDispMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 216),
    _Pm200frs02MesrlineResidualChromaticDispMin_Type()
)
pm200frs02MesrlineResidualChromaticDispMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispMin.setStatus("current")


class _Pm200frs02MesrlineDiffGroupDelayMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineDiffGroupDelayMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineDiffGroupDelayMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineDiffGroupDelayMin_Object = MibScalar
pm200frs02MesrlineDiffGroupDelayMin = _Pm200frs02MesrlineDiffGroupDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 217),
    _Pm200frs02MesrlineDiffGroupDelayMin_Type()
)
pm200frs02MesrlineDiffGroupDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayMin.setStatus("current")


class _Pm200frs02MesrlineQFactorMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineQFactorMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineQFactorMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineQFactorMin_Object = MibScalar
pm200frs02MesrlineQFactorMin = _Pm200frs02MesrlineQFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 218),
    _Pm200frs02MesrlineQFactorMin_Type()
)
pm200frs02MesrlineQFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorMin.setStatus("current")


class _Pm200frs02MesrlineCarrierFreqOffsetMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineCarrierFreqOffsetMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineCarrierFreqOffsetMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineCarrierFreqOffsetMin_Object = MibScalar
pm200frs02MesrlineCarrierFreqOffsetMin = _Pm200frs02MesrlineCarrierFreqOffsetMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 219),
    _Pm200frs02MesrlineCarrierFreqOffsetMin_Type()
)
pm200frs02MesrlineCarrierFreqOffsetMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetMin.setStatus("current")


class _Pm200frs02MesrlineOsnrMin_Type(Unsigned32):
    """Custom type pm200frs02MesrlineOsnrMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineOsnrMin_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineOsnrMin_Object = MibScalar
pm200frs02MesrlineOsnrMin = _Pm200frs02MesrlineOsnrMin_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 220),
    _Pm200frs02MesrlineOsnrMin_Type()
)
pm200frs02MesrlineOsnrMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrMin.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserOutputPwrMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxLaserOutputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserOutputPwrMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxLaserOutputPwrMax_Object = MibScalar
pm200frs02MesrlineNetTxLaserOutputPwrMax = _Pm200frs02MesrlineNetTxLaserOutputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 228),
    _Pm200frs02MesrlineNetTxLaserOutputPwrMax_Type()
)
pm200frs02MesrlineNetTxLaserOutputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrMax.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserTempMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxLaserTempMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserTempMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxLaserTempMax_Object = MibScalar
pm200frs02MesrlineNetTxLaserTempMax = _Pm200frs02MesrlineNetTxLaserTempMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 229),
    _Pm200frs02MesrlineNetTxLaserTempMax_Type()
)
pm200frs02MesrlineNetTxLaserTempMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempMax.setStatus("current")


class _Pm200frs02MesrlineNetTxBiasCurrentMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetTxBiasCurrentMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxBiasCurrentMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetTxBiasCurrentMax_Object = MibScalar
pm200frs02MesrlineNetTxBiasCurrentMax = _Pm200frs02MesrlineNetTxBiasCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 230),
    _Pm200frs02MesrlineNetTxBiasCurrentMax_Type()
)
pm200frs02MesrlineNetTxBiasCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentMax.setStatus("current")


class _Pm200frs02MesrlineNetRxInputPwrMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineNetRxInputPwrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetRxInputPwrMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineNetRxInputPwrMax_Object = MibScalar
pm200frs02MesrlineNetRxInputPwrMax = _Pm200frs02MesrlineNetRxInputPwrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 231),
    _Pm200frs02MesrlineNetRxInputPwrMax_Type()
)
pm200frs02MesrlineNetRxInputPwrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrMax.setStatus("current")


class _Pm200frs02MesrlineResidualChromaticDispMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineResidualChromaticDispMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineResidualChromaticDispMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineResidualChromaticDispMax_Object = MibScalar
pm200frs02MesrlineResidualChromaticDispMax = _Pm200frs02MesrlineResidualChromaticDispMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 232),
    _Pm200frs02MesrlineResidualChromaticDispMax_Type()
)
pm200frs02MesrlineResidualChromaticDispMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispMax.setStatus("current")


class _Pm200frs02MesrlineDiffGroupDelayMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineDiffGroupDelayMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineDiffGroupDelayMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineDiffGroupDelayMax_Object = MibScalar
pm200frs02MesrlineDiffGroupDelayMax = _Pm200frs02MesrlineDiffGroupDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 233),
    _Pm200frs02MesrlineDiffGroupDelayMax_Type()
)
pm200frs02MesrlineDiffGroupDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayMax.setStatus("current")


class _Pm200frs02MesrlineQFactorMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineQFactorMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineQFactorMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineQFactorMax_Object = MibScalar
pm200frs02MesrlineQFactorMax = _Pm200frs02MesrlineQFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 234),
    _Pm200frs02MesrlineQFactorMax_Type()
)
pm200frs02MesrlineQFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorMax.setStatus("current")


class _Pm200frs02MesrlineCarrierFreqOffsetMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineCarrierFreqOffsetMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineCarrierFreqOffsetMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineCarrierFreqOffsetMax_Object = MibScalar
pm200frs02MesrlineCarrierFreqOffsetMax = _Pm200frs02MesrlineCarrierFreqOffsetMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 235),
    _Pm200frs02MesrlineCarrierFreqOffsetMax_Type()
)
pm200frs02MesrlineCarrierFreqOffsetMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetMax.setStatus("current")


class _Pm200frs02MesrlineOsnrMax_Type(Unsigned32):
    """Custom type pm200frs02MesrlineOsnrMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineOsnrMax_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineOsnrMax_Object = MibScalar
pm200frs02MesrlineOsnrMax = _Pm200frs02MesrlineOsnrMax_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 236),
    _Pm200frs02MesrlineOsnrMax_Type()
)
pm200frs02MesrlineOsnrMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrMax.setStatus("current")


class _Pm200frs02MesrregVoltage_Type(Unsigned32):
    """Custom type pm200frs02MesrregVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrregVoltage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrregVoltage_Object = MibScalar
pm200frs02MesrregVoltage = _Pm200frs02MesrregVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 249),
    _Pm200frs02MesrregVoltage_Type()
)
pm200frs02MesrregVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrregVoltage.setStatus("current")


class _Pm200frs02MesrregCurrent_Type(Unsigned32):
    """Custom type pm200frs02MesrregCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrregCurrent_Type.__name__ = "Unsigned32"
_Pm200frs02MesrregCurrent_Object = MibScalar
pm200frs02MesrregCurrent = _Pm200frs02MesrregCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 250),
    _Pm200frs02MesrregCurrent_Type()
)
pm200frs02MesrregCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrregCurrent.setStatus("current")


class _Pm200frs02MesrregTemp_Type(Unsigned32):
    """Custom type pm200frs02MesrregTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrregTemp_Type.__name__ = "Unsigned32"
_Pm200frs02MesrregTemp_Object = MibScalar
pm200frs02MesrregTemp = _Pm200frs02MesrregTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 251),
    _Pm200frs02MesrregTemp_Type()
)
pm200frs02MesrregTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrregTemp.setStatus("current")


class _Pm200frs02Mesrtrscv1Temp_Type(Unsigned32):
    """Custom type pm200frs02Mesrtrscv1Temp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02Mesrtrscv1Temp_Type.__name__ = "Unsigned32"
_Pm200frs02Mesrtrscv1Temp_Object = MibScalar
pm200frs02Mesrtrscv1Temp = _Pm200frs02Mesrtrscv1Temp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 252),
    _Pm200frs02Mesrtrscv1Temp_Type()
)
pm200frs02Mesrtrscv1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Mesrtrscv1Temp.setStatus("current")


class _Pm200frs02Mesrtrscv2Temp_Type(Unsigned32):
    """Custom type pm200frs02Mesrtrscv2Temp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02Mesrtrscv2Temp_Type.__name__ = "Unsigned32"
_Pm200frs02Mesrtrscv2Temp_Object = MibScalar
pm200frs02Mesrtrscv2Temp = _Pm200frs02Mesrtrscv2Temp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 253),
    _Pm200frs02Mesrtrscv2Temp_Type()
)
pm200frs02Mesrtrscv2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Mesrtrscv2Temp.setStatus("current")


class _Pm200frs02Mesrtrscv1PowerSupply_Type(Unsigned32):
    """Custom type pm200frs02Mesrtrscv1PowerSupply based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02Mesrtrscv1PowerSupply_Type.__name__ = "Unsigned32"
_Pm200frs02Mesrtrscv1PowerSupply_Object = MibScalar
pm200frs02Mesrtrscv1PowerSupply = _Pm200frs02Mesrtrscv1PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 254),
    _Pm200frs02Mesrtrscv1PowerSupply_Type()
)
pm200frs02Mesrtrscv1PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Mesrtrscv1PowerSupply.setStatus("current")


class _Pm200frs02Mesrtrscv2PowerSupply_Type(Unsigned32):
    """Custom type pm200frs02Mesrtrscv2PowerSupply based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02Mesrtrscv2PowerSupply_Type.__name__ = "Unsigned32"
_Pm200frs02Mesrtrscv2PowerSupply_Object = MibScalar
pm200frs02Mesrtrscv2PowerSupply = _Pm200frs02Mesrtrscv2PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 1, 255),
    _Pm200frs02Mesrtrscv2PowerSupply_Type()
)
pm200frs02Mesrtrscv2PowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Mesrtrscv2PowerSupply.setStatus("current")
_Pm200frs02MesrClient_ObjectIdentity = ObjectIdentity
pm200frs02MesrClient = _Pm200frs02MesrClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2)
)


class _Pm200frs02MesrclientCfpTemp_Type(Unsigned32):
    """Custom type pm200frs02MesrclientCfpTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientCfpTemp_Type.__name__ = "Unsigned32"
_Pm200frs02MesrclientCfpTemp_Object = MibScalar
pm200frs02MesrclientCfpTemp = _Pm200frs02MesrclientCfpTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 8),
    _Pm200frs02MesrclientCfpTemp_Type()
)
pm200frs02MesrclientCfpTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientCfpTemp.setStatus("current")


class _Pm200frs02MesrclientCfp3v3Voltage_Type(Unsigned32):
    """Custom type pm200frs02MesrclientCfp3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientCfp3v3Voltage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrclientCfp3v3Voltage_Object = MibScalar
pm200frs02MesrclientCfp3v3Voltage = _Pm200frs02MesrclientCfp3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 9),
    _Pm200frs02MesrclientCfp3v3Voltage_Type()
)
pm200frs02MesrclientCfp3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientCfp3v3Voltage.setStatus("current")


class _Pm200frs02MesrclientSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm200frs02MesrclientSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm200frs02MesrclientSoaBiasCurrent_Object = MibScalar
pm200frs02MesrclientSoaBiasCurrent = _Pm200frs02MesrclientSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 10),
    _Pm200frs02MesrclientSoaBiasCurrent_Type()
)
pm200frs02MesrclientSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientSoaBiasCurrent.setStatus("current")
_Pm200frs02MesrclientTxPwrMinTable_Object = MibTable
pm200frs02MesrclientTxPwrMinTable = _Pm200frs02MesrclientTxPwrMinTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 16)
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMinTable.setStatus("current")
_Pm200frs02MesrclientTxPwrMinEntry_Object = MibTableRow
pm200frs02MesrclientTxPwrMinEntry = _Pm200frs02MesrclientTxPwrMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 16, 1)
)
pm200frs02MesrclientTxPwrMinEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrclientTxPwrMinIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMinEntry.setStatus("current")


class _Pm200frs02MesrclientTxPwrMinIndex_Type(Integer32):
    """Custom type pm200frs02MesrclientTxPwrMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrclientTxPwrMinIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrclientTxPwrMinIndex_Object = MibTableColumn
pm200frs02MesrclientTxPwrMinIndex = _Pm200frs02MesrclientTxPwrMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 16, 1, 1),
    _Pm200frs02MesrclientTxPwrMinIndex_Type()
)
pm200frs02MesrclientTxPwrMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMinIndex.setStatus("current")


class _Pm200frs02MesrclientTxPwrMinPortn_Type(Integer32):
    """Custom type pm200frs02MesrclientTxPwrMinPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientTxPwrMinPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrclientTxPwrMinPortn_Object = MibTableColumn
pm200frs02MesrclientTxPwrMinPortn = _Pm200frs02MesrclientTxPwrMinPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 16, 1, 2),
    _Pm200frs02MesrclientTxPwrMinPortn_Type()
)
pm200frs02MesrclientTxPwrMinPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMinPortn.setStatus("current")
_Pm200frs02MesrclientRxPwrMinTable_Object = MibTable
pm200frs02MesrclientRxPwrMinTable = _Pm200frs02MesrclientRxPwrMinTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 48)
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMinTable.setStatus("current")
_Pm200frs02MesrclientRxPwrMinEntry_Object = MibTableRow
pm200frs02MesrclientRxPwrMinEntry = _Pm200frs02MesrclientRxPwrMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 48, 1)
)
pm200frs02MesrclientRxPwrMinEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrclientRxPwrMinIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMinEntry.setStatus("current")


class _Pm200frs02MesrclientRxPwrMinIndex_Type(Integer32):
    """Custom type pm200frs02MesrclientRxPwrMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrclientRxPwrMinIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrclientRxPwrMinIndex_Object = MibTableColumn
pm200frs02MesrclientRxPwrMinIndex = _Pm200frs02MesrclientRxPwrMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 48, 1, 1),
    _Pm200frs02MesrclientRxPwrMinIndex_Type()
)
pm200frs02MesrclientRxPwrMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMinIndex.setStatus("current")


class _Pm200frs02MesrclientRxPwrMinPortn_Type(Integer32):
    """Custom type pm200frs02MesrclientRxPwrMinPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientRxPwrMinPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrclientRxPwrMinPortn_Object = MibTableColumn
pm200frs02MesrclientRxPwrMinPortn = _Pm200frs02MesrclientRxPwrMinPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 48, 1, 2),
    _Pm200frs02MesrclientRxPwrMinPortn_Type()
)
pm200frs02MesrclientRxPwrMinPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMinPortn.setStatus("current")
_Pm200frs02MesrclientTxPwrMaxTable_Object = MibTable
pm200frs02MesrclientTxPwrMaxTable = _Pm200frs02MesrclientTxPwrMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 80)
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMaxTable.setStatus("current")
_Pm200frs02MesrclientTxPwrMaxEntry_Object = MibTableRow
pm200frs02MesrclientTxPwrMaxEntry = _Pm200frs02MesrclientTxPwrMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 80, 1)
)
pm200frs02MesrclientTxPwrMaxEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrclientTxPwrMaxIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMaxEntry.setStatus("current")


class _Pm200frs02MesrclientTxPwrMaxIndex_Type(Integer32):
    """Custom type pm200frs02MesrclientTxPwrMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrclientTxPwrMaxIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrclientTxPwrMaxIndex_Object = MibTableColumn
pm200frs02MesrclientTxPwrMaxIndex = _Pm200frs02MesrclientTxPwrMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 80, 1, 1),
    _Pm200frs02MesrclientTxPwrMaxIndex_Type()
)
pm200frs02MesrclientTxPwrMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMaxIndex.setStatus("current")


class _Pm200frs02MesrclientTxPwrMaxPortn_Type(Integer32):
    """Custom type pm200frs02MesrclientTxPwrMaxPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientTxPwrMaxPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrclientTxPwrMaxPortn_Object = MibTableColumn
pm200frs02MesrclientTxPwrMaxPortn = _Pm200frs02MesrclientTxPwrMaxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 80, 1, 2),
    _Pm200frs02MesrclientTxPwrMaxPortn_Type()
)
pm200frs02MesrclientTxPwrMaxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxPwrMaxPortn.setStatus("current")
_Pm200frs02MesrclientRxPwrMaxTable_Object = MibTable
pm200frs02MesrclientRxPwrMaxTable = _Pm200frs02MesrclientRxPwrMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 112)
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMaxTable.setStatus("current")
_Pm200frs02MesrclientRxPwrMaxEntry_Object = MibTableRow
pm200frs02MesrclientRxPwrMaxEntry = _Pm200frs02MesrclientRxPwrMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 112, 1)
)
pm200frs02MesrclientRxPwrMaxEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrclientRxPwrMaxIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMaxEntry.setStatus("current")


class _Pm200frs02MesrclientRxPwrMaxIndex_Type(Integer32):
    """Custom type pm200frs02MesrclientRxPwrMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrclientRxPwrMaxIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrclientRxPwrMaxIndex_Object = MibTableColumn
pm200frs02MesrclientRxPwrMaxIndex = _Pm200frs02MesrclientRxPwrMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 112, 1, 1),
    _Pm200frs02MesrclientRxPwrMaxIndex_Type()
)
pm200frs02MesrclientRxPwrMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMaxIndex.setStatus("current")


class _Pm200frs02MesrclientRxPwrMaxPortn_Type(Integer32):
    """Custom type pm200frs02MesrclientRxPwrMaxPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientRxPwrMaxPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrclientRxPwrMaxPortn_Object = MibTableColumn
pm200frs02MesrclientRxPwrMaxPortn = _Pm200frs02MesrclientRxPwrMaxPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 112, 1, 2),
    _Pm200frs02MesrclientRxPwrMaxPortn_Type()
)
pm200frs02MesrclientRxPwrMaxPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxPwrMaxPortn.setStatus("current")
_Pm200frs02MesrclientTxCompositePwrTable_Object = MibTable
pm200frs02MesrclientTxCompositePwrTable = _Pm200frs02MesrclientTxCompositePwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 256)
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxCompositePwrTable.setStatus("current")
_Pm200frs02MesrclientTxCompositePwrEntry_Object = MibTableRow
pm200frs02MesrclientTxCompositePwrEntry = _Pm200frs02MesrclientTxCompositePwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 256, 1)
)
pm200frs02MesrclientTxCompositePwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrclientTxCompositePwrIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxCompositePwrEntry.setStatus("current")


class _Pm200frs02MesrclientTxCompositePwrIndex_Type(Integer32):
    """Custom type pm200frs02MesrclientTxCompositePwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrclientTxCompositePwrIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrclientTxCompositePwrIndex_Object = MibTableColumn
pm200frs02MesrclientTxCompositePwrIndex = _Pm200frs02MesrclientTxCompositePwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 256, 1, 1),
    _Pm200frs02MesrclientTxCompositePwrIndex_Type()
)
pm200frs02MesrclientTxCompositePwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxCompositePwrIndex.setStatus("current")


class _Pm200frs02MesrclientTxCompositePwrPortn_Type(Integer32):
    """Custom type pm200frs02MesrclientTxCompositePwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientTxCompositePwrPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrclientTxCompositePwrPortn_Object = MibTableColumn
pm200frs02MesrclientTxCompositePwrPortn = _Pm200frs02MesrclientTxCompositePwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 256, 1, 2),
    _Pm200frs02MesrclientTxCompositePwrPortn_Type()
)
pm200frs02MesrclientTxCompositePwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientTxCompositePwrPortn.setStatus("current")
_Pm200frs02MesrclientRxCompositePwrTable_Object = MibTable
pm200frs02MesrclientRxCompositePwrTable = _Pm200frs02MesrclientRxCompositePwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 288)
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxCompositePwrTable.setStatus("current")
_Pm200frs02MesrclientRxCompositePwrEntry_Object = MibTableRow
pm200frs02MesrclientRxCompositePwrEntry = _Pm200frs02MesrclientRxCompositePwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 288, 1)
)
pm200frs02MesrclientRxCompositePwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrclientRxCompositePwrIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxCompositePwrEntry.setStatus("current")


class _Pm200frs02MesrclientRxCompositePwrIndex_Type(Integer32):
    """Custom type pm200frs02MesrclientRxCompositePwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrclientRxCompositePwrIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrclientRxCompositePwrIndex_Object = MibTableColumn
pm200frs02MesrclientRxCompositePwrIndex = _Pm200frs02MesrclientRxCompositePwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 288, 1, 1),
    _Pm200frs02MesrclientRxCompositePwrIndex_Type()
)
pm200frs02MesrclientRxCompositePwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxCompositePwrIndex.setStatus("current")


class _Pm200frs02MesrclientRxCompositePwrPortn_Type(Integer32):
    """Custom type pm200frs02MesrclientRxCompositePwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrclientRxCompositePwrPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrclientRxCompositePwrPortn_Object = MibTableColumn
pm200frs02MesrclientRxCompositePwrPortn = _Pm200frs02MesrclientRxCompositePwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 2, 288, 1, 2),
    _Pm200frs02MesrclientRxCompositePwrPortn_Type()
)
pm200frs02MesrclientRxCompositePwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrclientRxCompositePwrPortn.setStatus("current")
_Pm200frs02MesrLine_ObjectIdentity = ObjectIdentity
pm200frs02MesrLine = _Pm200frs02MesrLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3)
)


class _Pm200frs02MesrlineMsaTemp_Type(Unsigned32):
    """Custom type pm200frs02MesrlineMsaTemp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineMsaTemp_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineMsaTemp_Object = MibScalar
pm200frs02MesrlineMsaTemp = _Pm200frs02MesrlineMsaTemp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 12),
    _Pm200frs02MesrlineMsaTemp_Type()
)
pm200frs02MesrlineMsaTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineMsaTemp.setStatus("current")


class _Pm200frs02MesrlineMsa3v3Voltage_Type(Unsigned32):
    """Custom type pm200frs02MesrlineMsa3v3Voltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineMsa3v3Voltage_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineMsa3v3Voltage_Object = MibScalar
pm200frs02MesrlineMsa3v3Voltage = _Pm200frs02MesrlineMsa3v3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 13),
    _Pm200frs02MesrlineMsa3v3Voltage_Type()
)
pm200frs02MesrlineMsa3v3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineMsa3v3Voltage.setStatus("current")


class _Pm200frs02MesrlineSoaBiasCurrent_Type(Unsigned32):
    """Custom type pm200frs02MesrlineSoaBiasCurrent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineSoaBiasCurrent_Type.__name__ = "Unsigned32"
_Pm200frs02MesrlineSoaBiasCurrent_Object = MibScalar
pm200frs02MesrlineSoaBiasCurrent = _Pm200frs02MesrlineSoaBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 14),
    _Pm200frs02MesrlineSoaBiasCurrent_Type()
)
pm200frs02MesrlineSoaBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineSoaBiasCurrent.setStatus("current")
_Pm200frs02MesrlineNetTxLaserOutputPwrTable_Object = MibTable
pm200frs02MesrlineNetTxLaserOutputPwrTable = _Pm200frs02MesrlineNetTxLaserOutputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 144)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrTable.setStatus("current")
_Pm200frs02MesrlineNetTxLaserOutputPwrEntry_Object = MibTableRow
pm200frs02MesrlineNetTxLaserOutputPwrEntry = _Pm200frs02MesrlineNetTxLaserOutputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 144, 1)
)
pm200frs02MesrlineNetTxLaserOutputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineNetTxLaserOutputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrEntry.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserOutputPwrIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineNetTxLaserOutputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineNetTxLaserOutputPwrIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetTxLaserOutputPwrIndex_Object = MibTableColumn
pm200frs02MesrlineNetTxLaserOutputPwrIndex = _Pm200frs02MesrlineNetTxLaserOutputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 144, 1, 1),
    _Pm200frs02MesrlineNetTxLaserOutputPwrIndex_Type()
)
pm200frs02MesrlineNetTxLaserOutputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrIndex.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserOutputPwrPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineNetTxLaserOutputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserOutputPwrPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetTxLaserOutputPwrPortn_Object = MibTableColumn
pm200frs02MesrlineNetTxLaserOutputPwrPortn = _Pm200frs02MesrlineNetTxLaserOutputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 144, 1, 2),
    _Pm200frs02MesrlineNetTxLaserOutputPwrPortn_Type()
)
pm200frs02MesrlineNetTxLaserOutputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserOutputPwrPortn.setStatus("current")
_Pm200frs02MesrlineNetTxLaserTempTable_Object = MibTable
pm200frs02MesrlineNetTxLaserTempTable = _Pm200frs02MesrlineNetTxLaserTempTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 148)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempTable.setStatus("current")
_Pm200frs02MesrlineNetTxLaserTempEntry_Object = MibTableRow
pm200frs02MesrlineNetTxLaserTempEntry = _Pm200frs02MesrlineNetTxLaserTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 148, 1)
)
pm200frs02MesrlineNetTxLaserTempEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineNetTxLaserTempIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempEntry.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserTempIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineNetTxLaserTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineNetTxLaserTempIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetTxLaserTempIndex_Object = MibTableColumn
pm200frs02MesrlineNetTxLaserTempIndex = _Pm200frs02MesrlineNetTxLaserTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 148, 1, 1),
    _Pm200frs02MesrlineNetTxLaserTempIndex_Type()
)
pm200frs02MesrlineNetTxLaserTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempIndex.setStatus("current")


class _Pm200frs02MesrlineNetTxLaserTempPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineNetTxLaserTempPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxLaserTempPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetTxLaserTempPortn_Object = MibTableColumn
pm200frs02MesrlineNetTxLaserTempPortn = _Pm200frs02MesrlineNetTxLaserTempPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 148, 1, 2),
    _Pm200frs02MesrlineNetTxLaserTempPortn_Type()
)
pm200frs02MesrlineNetTxLaserTempPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxLaserTempPortn.setStatus("current")
_Pm200frs02MesrlineNetTxBiasCurrentTable_Object = MibTable
pm200frs02MesrlineNetTxBiasCurrentTable = _Pm200frs02MesrlineNetTxBiasCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 152)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentTable.setStatus("current")
_Pm200frs02MesrlineNetTxBiasCurrentEntry_Object = MibTableRow
pm200frs02MesrlineNetTxBiasCurrentEntry = _Pm200frs02MesrlineNetTxBiasCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 152, 1)
)
pm200frs02MesrlineNetTxBiasCurrentEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineNetTxBiasCurrentIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentEntry.setStatus("current")


class _Pm200frs02MesrlineNetTxBiasCurrentIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineNetTxBiasCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineNetTxBiasCurrentIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetTxBiasCurrentIndex_Object = MibTableColumn
pm200frs02MesrlineNetTxBiasCurrentIndex = _Pm200frs02MesrlineNetTxBiasCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 152, 1, 1),
    _Pm200frs02MesrlineNetTxBiasCurrentIndex_Type()
)
pm200frs02MesrlineNetTxBiasCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentIndex.setStatus("current")


class _Pm200frs02MesrlineNetTxBiasCurrentPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineNetTxBiasCurrentPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetTxBiasCurrentPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetTxBiasCurrentPortn_Object = MibTableColumn
pm200frs02MesrlineNetTxBiasCurrentPortn = _Pm200frs02MesrlineNetTxBiasCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 152, 1, 2),
    _Pm200frs02MesrlineNetTxBiasCurrentPortn_Type()
)
pm200frs02MesrlineNetTxBiasCurrentPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetTxBiasCurrentPortn.setStatus("current")
_Pm200frs02MesrlineNetRxInputPwrTable_Object = MibTable
pm200frs02MesrlineNetRxInputPwrTable = _Pm200frs02MesrlineNetRxInputPwrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 156)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrTable.setStatus("current")
_Pm200frs02MesrlineNetRxInputPwrEntry_Object = MibTableRow
pm200frs02MesrlineNetRxInputPwrEntry = _Pm200frs02MesrlineNetRxInputPwrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 156, 1)
)
pm200frs02MesrlineNetRxInputPwrEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineNetRxInputPwrIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrEntry.setStatus("current")


class _Pm200frs02MesrlineNetRxInputPwrIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineNetRxInputPwrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineNetRxInputPwrIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetRxInputPwrIndex_Object = MibTableColumn
pm200frs02MesrlineNetRxInputPwrIndex = _Pm200frs02MesrlineNetRxInputPwrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 156, 1, 1),
    _Pm200frs02MesrlineNetRxInputPwrIndex_Type()
)
pm200frs02MesrlineNetRxInputPwrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrIndex.setStatus("current")


class _Pm200frs02MesrlineNetRxInputPwrPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineNetRxInputPwrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineNetRxInputPwrPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineNetRxInputPwrPortn_Object = MibTableColumn
pm200frs02MesrlineNetRxInputPwrPortn = _Pm200frs02MesrlineNetRxInputPwrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 156, 1, 2),
    _Pm200frs02MesrlineNetRxInputPwrPortn_Type()
)
pm200frs02MesrlineNetRxInputPwrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineNetRxInputPwrPortn.setStatus("current")
_Pm200frs02MesrlineResidualChromaticDispTable_Object = MibTable
pm200frs02MesrlineResidualChromaticDispTable = _Pm200frs02MesrlineResidualChromaticDispTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 160)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispTable.setStatus("current")
_Pm200frs02MesrlineResidualChromaticDispEntry_Object = MibTableRow
pm200frs02MesrlineResidualChromaticDispEntry = _Pm200frs02MesrlineResidualChromaticDispEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 160, 1)
)
pm200frs02MesrlineResidualChromaticDispEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineResidualChromaticDispIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispEntry.setStatus("current")


class _Pm200frs02MesrlineResidualChromaticDispIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineResidualChromaticDispIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineResidualChromaticDispIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineResidualChromaticDispIndex_Object = MibTableColumn
pm200frs02MesrlineResidualChromaticDispIndex = _Pm200frs02MesrlineResidualChromaticDispIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 160, 1, 1),
    _Pm200frs02MesrlineResidualChromaticDispIndex_Type()
)
pm200frs02MesrlineResidualChromaticDispIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispIndex.setStatus("current")


class _Pm200frs02MesrlineResidualChromaticDispPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineResidualChromaticDispPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineResidualChromaticDispPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineResidualChromaticDispPortn_Object = MibTableColumn
pm200frs02MesrlineResidualChromaticDispPortn = _Pm200frs02MesrlineResidualChromaticDispPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 160, 1, 2),
    _Pm200frs02MesrlineResidualChromaticDispPortn_Type()
)
pm200frs02MesrlineResidualChromaticDispPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineResidualChromaticDispPortn.setStatus("current")
_Pm200frs02MesrlineDiffGroupDelayTable_Object = MibTable
pm200frs02MesrlineDiffGroupDelayTable = _Pm200frs02MesrlineDiffGroupDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 164)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayTable.setStatus("current")
_Pm200frs02MesrlineDiffGroupDelayEntry_Object = MibTableRow
pm200frs02MesrlineDiffGroupDelayEntry = _Pm200frs02MesrlineDiffGroupDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 164, 1)
)
pm200frs02MesrlineDiffGroupDelayEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineDiffGroupDelayIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayEntry.setStatus("current")


class _Pm200frs02MesrlineDiffGroupDelayIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineDiffGroupDelayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineDiffGroupDelayIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineDiffGroupDelayIndex_Object = MibTableColumn
pm200frs02MesrlineDiffGroupDelayIndex = _Pm200frs02MesrlineDiffGroupDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 164, 1, 1),
    _Pm200frs02MesrlineDiffGroupDelayIndex_Type()
)
pm200frs02MesrlineDiffGroupDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayIndex.setStatus("current")


class _Pm200frs02MesrlineDiffGroupDelayPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineDiffGroupDelayPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineDiffGroupDelayPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineDiffGroupDelayPortn_Object = MibTableColumn
pm200frs02MesrlineDiffGroupDelayPortn = _Pm200frs02MesrlineDiffGroupDelayPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 164, 1, 2),
    _Pm200frs02MesrlineDiffGroupDelayPortn_Type()
)
pm200frs02MesrlineDiffGroupDelayPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineDiffGroupDelayPortn.setStatus("current")
_Pm200frs02MesrlineQFactorTable_Object = MibTable
pm200frs02MesrlineQFactorTable = _Pm200frs02MesrlineQFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 168)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorTable.setStatus("current")
_Pm200frs02MesrlineQFactorEntry_Object = MibTableRow
pm200frs02MesrlineQFactorEntry = _Pm200frs02MesrlineQFactorEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 168, 1)
)
pm200frs02MesrlineQFactorEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineQFactorIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorEntry.setStatus("current")


class _Pm200frs02MesrlineQFactorIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineQFactorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineQFactorIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineQFactorIndex_Object = MibTableColumn
pm200frs02MesrlineQFactorIndex = _Pm200frs02MesrlineQFactorIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 168, 1, 1),
    _Pm200frs02MesrlineQFactorIndex_Type()
)
pm200frs02MesrlineQFactorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorIndex.setStatus("current")


class _Pm200frs02MesrlineQFactorPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineQFactorPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineQFactorPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineQFactorPortn_Object = MibTableColumn
pm200frs02MesrlineQFactorPortn = _Pm200frs02MesrlineQFactorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 168, 1, 2),
    _Pm200frs02MesrlineQFactorPortn_Type()
)
pm200frs02MesrlineQFactorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineQFactorPortn.setStatus("current")
_Pm200frs02MesrlineCarrierFreqOffsetTable_Object = MibTable
pm200frs02MesrlineCarrierFreqOffsetTable = _Pm200frs02MesrlineCarrierFreqOffsetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 172)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetTable.setStatus("current")
_Pm200frs02MesrlineCarrierFreqOffsetEntry_Object = MibTableRow
pm200frs02MesrlineCarrierFreqOffsetEntry = _Pm200frs02MesrlineCarrierFreqOffsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 172, 1)
)
pm200frs02MesrlineCarrierFreqOffsetEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineCarrierFreqOffsetIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetEntry.setStatus("current")


class _Pm200frs02MesrlineCarrierFreqOffsetIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineCarrierFreqOffsetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineCarrierFreqOffsetIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineCarrierFreqOffsetIndex_Object = MibTableColumn
pm200frs02MesrlineCarrierFreqOffsetIndex = _Pm200frs02MesrlineCarrierFreqOffsetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 172, 1, 1),
    _Pm200frs02MesrlineCarrierFreqOffsetIndex_Type()
)
pm200frs02MesrlineCarrierFreqOffsetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetIndex.setStatus("current")


class _Pm200frs02MesrlineCarrierFreqOffsetPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineCarrierFreqOffsetPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineCarrierFreqOffsetPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineCarrierFreqOffsetPortn_Object = MibTableColumn
pm200frs02MesrlineCarrierFreqOffsetPortn = _Pm200frs02MesrlineCarrierFreqOffsetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 172, 1, 2),
    _Pm200frs02MesrlineCarrierFreqOffsetPortn_Type()
)
pm200frs02MesrlineCarrierFreqOffsetPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineCarrierFreqOffsetPortn.setStatus("current")
_Pm200frs02MesrlineOsnrTable_Object = MibTable
pm200frs02MesrlineOsnrTable = _Pm200frs02MesrlineOsnrTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 176)
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrTable.setStatus("current")
_Pm200frs02MesrlineOsnrEntry_Object = MibTableRow
pm200frs02MesrlineOsnrEntry = _Pm200frs02MesrlineOsnrEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 176, 1)
)
pm200frs02MesrlineOsnrEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MesrlineOsnrIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrEntry.setStatus("current")


class _Pm200frs02MesrlineOsnrIndex_Type(Integer32):
    """Custom type pm200frs02MesrlineOsnrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MesrlineOsnrIndex_Type.__name__ = "Integer32"
_Pm200frs02MesrlineOsnrIndex_Object = MibTableColumn
pm200frs02MesrlineOsnrIndex = _Pm200frs02MesrlineOsnrIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 176, 1, 1),
    _Pm200frs02MesrlineOsnrIndex_Type()
)
pm200frs02MesrlineOsnrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrIndex.setStatus("current")


class _Pm200frs02MesrlineOsnrPortn_Type(Integer32):
    """Custom type pm200frs02MesrlineOsnrPortn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Pm200frs02MesrlineOsnrPortn_Type.__name__ = "Integer32"
_Pm200frs02MesrlineOsnrPortn_Object = MibTableColumn
pm200frs02MesrlineOsnrPortn = _Pm200frs02MesrlineOsnrPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 3, 3, 176, 1, 2),
    _Pm200frs02MesrlineOsnrPortn_Type()
)
pm200frs02MesrlineOsnrPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MesrlineOsnrPortn.setStatus("current")
_Pm200frs02counters_ObjectIdentity = ObjectIdentity
pm200frs02counters = _Pm200frs02counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4)
)
_Pm200frs02CntOther_ObjectIdentity = ObjectIdentity
pm200frs02CntOther = _Pm200frs02CntOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 1)
)
_Pm200frs02CntClient_ObjectIdentity = ObjectIdentity
pm200frs02CntClient = _Pm200frs02CntClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2)
)
_Pm200frs02CntclientInputErrorCounterTable_Object = MibTable
pm200frs02CntclientInputErrorCounterTable = _Pm200frs02CntclientInputErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 112)
)
if mibBuilder.loadTexts:
    pm200frs02CntclientInputErrorCounterTable.setStatus("current")
_Pm200frs02CntclientInputErrorCounterEntry_Object = MibTableRow
pm200frs02CntclientInputErrorCounterEntry = _Pm200frs02CntclientInputErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 112, 1)
)
pm200frs02CntclientInputErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntclientInputErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntclientInputErrorCounterEntry.setStatus("current")


class _Pm200frs02CntclientInputErrorCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntclientInputErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntclientInputErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntclientInputErrorCounterIndex_Object = MibTableColumn
pm200frs02CntclientInputErrorCounterIndex = _Pm200frs02CntclientInputErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 112, 1, 1),
    _Pm200frs02CntclientInputErrorCounterIndex_Type()
)
pm200frs02CntclientInputErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientInputErrorCounterIndex.setStatus("current")
_Pm200frs02CntclientInputErrorCounterValuePortn_Type = Counter32
_Pm200frs02CntclientInputErrorCounterValuePortn_Object = MibTableColumn
pm200frs02CntclientInputErrorCounterValuePortn = _Pm200frs02CntclientInputErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 112, 1, 2),
    _Pm200frs02CntclientInputErrorCounterValuePortn_Type()
)
pm200frs02CntclientInputErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientInputErrorCounterValuePortn.setStatus("current")
_Pm200frs02CntclientInputErrorCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntclientInputErrorCounterErrorPortn_Object = MibTableColumn
pm200frs02CntclientInputErrorCounterErrorPortn = _Pm200frs02CntclientInputErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 112, 1, 3),
    _Pm200frs02CntclientInputErrorCounterErrorPortn_Type()
)
pm200frs02CntclientInputErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientInputErrorCounterErrorPortn.setStatus("current")
_Pm200frs02CntclientInputErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntclientInputErrorCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntclientInputErrorCounterOverloadPortn = _Pm200frs02CntclientInputErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 112, 1, 4),
    _Pm200frs02CntclientInputErrorCounterOverloadPortn_Type()
)
pm200frs02CntclientInputErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientInputErrorCounterOverloadPortn.setStatus("current")
_Pm200frs02CntclientCbipCounterTable_Object = MibTable
pm200frs02CntclientCbipCounterTable = _Pm200frs02CntclientCbipCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 144)
)
if mibBuilder.loadTexts:
    pm200frs02CntclientCbipCounterTable.setStatus("current")
_Pm200frs02CntclientCbipCounterEntry_Object = MibTableRow
pm200frs02CntclientCbipCounterEntry = _Pm200frs02CntclientCbipCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 144, 1)
)
pm200frs02CntclientCbipCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntclientCbipCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntclientCbipCounterEntry.setStatus("current")


class _Pm200frs02CntclientCbipCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntclientCbipCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntclientCbipCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntclientCbipCounterIndex_Object = MibTableColumn
pm200frs02CntclientCbipCounterIndex = _Pm200frs02CntclientCbipCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 144, 1, 1),
    _Pm200frs02CntclientCbipCounterIndex_Type()
)
pm200frs02CntclientCbipCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientCbipCounterIndex.setStatus("current")
_Pm200frs02CntclientCbipCounterValuePortn_Type = Counter32
_Pm200frs02CntclientCbipCounterValuePortn_Object = MibTableColumn
pm200frs02CntclientCbipCounterValuePortn = _Pm200frs02CntclientCbipCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 144, 1, 2),
    _Pm200frs02CntclientCbipCounterValuePortn_Type()
)
pm200frs02CntclientCbipCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientCbipCounterValuePortn.setStatus("current")
_Pm200frs02CntclientCbipCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntclientCbipCounterErrorPortn_Object = MibTableColumn
pm200frs02CntclientCbipCounterErrorPortn = _Pm200frs02CntclientCbipCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 144, 1, 3),
    _Pm200frs02CntclientCbipCounterErrorPortn_Type()
)
pm200frs02CntclientCbipCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientCbipCounterErrorPortn.setStatus("current")
_Pm200frs02CntclientCbipCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntclientCbipCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntclientCbipCounterOverloadPortn = _Pm200frs02CntclientCbipCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 2, 144, 1, 4),
    _Pm200frs02CntclientCbipCounterOverloadPortn_Type()
)
pm200frs02CntclientCbipCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntclientCbipCounterOverloadPortn.setStatus("current")
_Pm200frs02CntLine_ObjectIdentity = ObjectIdentity
pm200frs02CntLine = _Pm200frs02CntLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3)
)
_Pm200frs02CntlocalLineSmBip8ErrorCounterTable_Object = MibTable
pm200frs02CntlocalLineSmBip8ErrorCounterTable = _Pm200frs02CntlocalLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 192)
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineSmBip8ErrorCounterTable.setStatus("current")
_Pm200frs02CntlocalLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm200frs02CntlocalLineSmBip8ErrorCounterEntry = _Pm200frs02CntlocalLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 192, 1)
)
pm200frs02CntlocalLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlocalLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm200frs02CntlocalLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntlocalLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlocalLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlocalLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm200frs02CntlocalLineSmBip8ErrorCounterIndex = _Pm200frs02CntlocalLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 192, 1, 1),
    _Pm200frs02CntlocalLineSmBip8ErrorCounterIndex_Type()
)
pm200frs02CntlocalLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn = _Pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 192, 1, 2),
    _Pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn_Type()
)
pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn = _Pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 192, 1, 3),
    _Pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn_Type()
)
pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn = _Pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 192, 1, 4),
    _Pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterTable_Object = MibTable
pm200frs02CntlocalLineFecCorrectedErrorsCounterTable = _Pm200frs02CntlocalLineFecCorrectedErrorsCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 193)
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineFecCorrectedErrorsCounterTable.setStatus("current")
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry_Object = MibTableRow
pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry = _Pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 193, 1)
)
pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry.setStatus("current")


class _Pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex_Object = MibTableColumn
pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex = _Pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 193, 1, 1),
    _Pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex_Type()
)
pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex.setStatus("current")
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn_Type = Counter64
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn_Object = MibTableColumn
pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn = _Pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 193, 1, 2),
    _Pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn_Type()
)
pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn.setStatus("current")
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object = MibTableColumn
pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn = _Pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 193, 1, 3),
    _Pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn_Type()
)
pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn.setStatus("current")
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn = _Pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 193, 1, 4),
    _Pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn_Type()
)
pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn.setStatus("current")
_Pm200frs02CntremoteLineSmBip8ErrorCounterTable_Object = MibTable
pm200frs02CntremoteLineSmBip8ErrorCounterTable = _Pm200frs02CntremoteLineSmBip8ErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 194)
)
if mibBuilder.loadTexts:
    pm200frs02CntremoteLineSmBip8ErrorCounterTable.setStatus("current")
_Pm200frs02CntremoteLineSmBip8ErrorCounterEntry_Object = MibTableRow
pm200frs02CntremoteLineSmBip8ErrorCounterEntry = _Pm200frs02CntremoteLineSmBip8ErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 194, 1)
)
pm200frs02CntremoteLineSmBip8ErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntremoteLineSmBip8ErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntremoteLineSmBip8ErrorCounterEntry.setStatus("current")


class _Pm200frs02CntremoteLineSmBip8ErrorCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntremoteLineSmBip8ErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntremoteLineSmBip8ErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntremoteLineSmBip8ErrorCounterIndex_Object = MibTableColumn
pm200frs02CntremoteLineSmBip8ErrorCounterIndex = _Pm200frs02CntremoteLineSmBip8ErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 194, 1, 1),
    _Pm200frs02CntremoteLineSmBip8ErrorCounterIndex_Type()
)
pm200frs02CntremoteLineSmBip8ErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntremoteLineSmBip8ErrorCounterIndex.setStatus("current")
_Pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn_Type = Counter64
_Pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn_Object = MibTableColumn
pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn = _Pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 194, 1, 2),
    _Pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn_Type()
)
pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn.setStatus("current")
_Pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn_Object = MibTableColumn
pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn = _Pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 194, 1, 3),
    _Pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn_Type()
)
pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn.setStatus("current")
_Pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn = _Pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 194, 1, 4),
    _Pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn_Type()
)
pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn.setStatus("current")
_Pm200frs02CntlineDfrmTimCntTable_Object = MibTable
pm200frs02CntlineDfrmTimCntTable = _Pm200frs02CntlineDfrmTimCntTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 195)
)
if mibBuilder.loadTexts:
    pm200frs02CntlineDfrmTimCntTable.setStatus("current")
_Pm200frs02CntlineDfrmTimCntEntry_Object = MibTableRow
pm200frs02CntlineDfrmTimCntEntry = _Pm200frs02CntlineDfrmTimCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 195, 1)
)
pm200frs02CntlineDfrmTimCntEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlineDfrmTimCntIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlineDfrmTimCntEntry.setStatus("current")


class _Pm200frs02CntlineDfrmTimCntIndex_Type(Integer32):
    """Custom type pm200frs02CntlineDfrmTimCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlineDfrmTimCntIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlineDfrmTimCntIndex_Object = MibTableColumn
pm200frs02CntlineDfrmTimCntIndex = _Pm200frs02CntlineDfrmTimCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 195, 1, 1),
    _Pm200frs02CntlineDfrmTimCntIndex_Type()
)
pm200frs02CntlineDfrmTimCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlineDfrmTimCntIndex.setStatus("current")
_Pm200frs02CntlineDfrmTimCntValuePortn_Type = Counter64
_Pm200frs02CntlineDfrmTimCntValuePortn_Object = MibTableColumn
pm200frs02CntlineDfrmTimCntValuePortn = _Pm200frs02CntlineDfrmTimCntValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 195, 1, 2),
    _Pm200frs02CntlineDfrmTimCntValuePortn_Type()
)
pm200frs02CntlineDfrmTimCntValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlineDfrmTimCntValuePortn.setStatus("current")
_Pm200frs02CntlineDfrmTimCntErrorPortn_Type = EkiOnOff
_Pm200frs02CntlineDfrmTimCntErrorPortn_Object = MibTableColumn
pm200frs02CntlineDfrmTimCntErrorPortn = _Pm200frs02CntlineDfrmTimCntErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 195, 1, 3),
    _Pm200frs02CntlineDfrmTimCntErrorPortn_Type()
)
pm200frs02CntlineDfrmTimCntErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlineDfrmTimCntErrorPortn.setStatus("current")
_Pm200frs02CntlineDfrmTimCntOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlineDfrmTimCntOverloadPortn_Object = MibTableColumn
pm200frs02CntlineDfrmTimCntOverloadPortn = _Pm200frs02CntlineDfrmTimCntOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 195, 1, 4),
    _Pm200frs02CntlineDfrmTimCntOverloadPortn_Type()
)
pm200frs02CntlineDfrmTimCntOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlineDfrmTimCntOverloadPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterTable_Object = MibTable
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterTable = _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 196)
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecErrorCounterTable.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry_Object = MibTableRow
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry = _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 196, 1)
)
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry.setStatus("current")


class _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex = _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 196, 1, 1),
    _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type = Counter64
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn = _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 196, 1, 2),
    _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn = _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 196, 1, 3),
    _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn = _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 196, 1, 4),
    _Pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object = MibTable
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterTable = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 197)
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterTable.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object = MibTableRow
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 197, 1)
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry.setStatus("current")


class _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 197, 1, 1),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type = Counter64
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 197, 1, 2),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 197, 1, 3),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 197, 1, 4),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterTable_Object = MibTable
pm200frs02CntlocalLineTrscvPreSdFecBitCounterTable = _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 198)
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecBitCounterTable.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry_Object = MibTableRow
pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry = _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 198, 1)
)
pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry.setStatus("current")


class _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex = _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 198, 1, 1),
    _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn_Type = Counter64
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn = _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 198, 1, 2),
    _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn = _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 198, 1, 3),
    _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn = _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 198, 1, 4),
    _Pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn_Type()
)
pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object = MibTable
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterTable = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 199)
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterTable.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object = MibTableRow
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 199, 1)
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry.setStatus("current")


class _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type(Integer32):
    """Custom type pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type.__name__ = "Integer32"
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 199, 1, 1),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type = Counter64
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 199, 1, 2),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 199, 1, 3),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn.setStatus("current")
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type = EkiOnOff
_Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object = MibTableColumn
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn = _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 4, 3, 199, 1, 4),
    _Pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn_Type()
)
pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn.setStatus("current")
_Pm200frs02controlsWrite_ObjectIdentity = ObjectIdentity
pm200frs02controlsWrite = _Pm200frs02controlsWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6)
)
_Pm200frs02CtrlOther_ObjectIdentity = ObjectIdentity
pm200frs02CtrlOther = _Pm200frs02CtrlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1)
)
_Pm200frs02CtrlconfMgnt1_ObjectIdentity = ObjectIdentity
pm200frs02CtrlconfMgnt1 = _Pm200frs02CtrlconfMgnt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 1)
)
_Pm200frs02CtrlConf1Load1_Type = EkiOnOff
_Pm200frs02CtrlConf1Load1_Object = MibScalar
pm200frs02CtrlConf1Load1 = _Pm200frs02CtrlConf1Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 1, 1),
    _Pm200frs02CtrlConf1Load1_Type()
)
pm200frs02CtrlConf1Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlConf1Load1.setStatus("current")
_Pm200frs02CtrlConf2Load1_Type = EkiOnOff
_Pm200frs02CtrlConf2Load1_Object = MibScalar
pm200frs02CtrlConf2Load1 = _Pm200frs02CtrlConf2Load1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 1, 2),
    _Pm200frs02CtrlConf2Load1_Type()
)
pm200frs02CtrlConf2Load1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlConf2Load1.setStatus("current")
_Pm200frs02CtrlConf2Flash1_Type = EkiOnOff
_Pm200frs02CtrlConf2Flash1_Object = MibScalar
pm200frs02CtrlConf2Flash1 = _Pm200frs02CtrlConf2Flash1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 1, 10),
    _Pm200frs02CtrlConf2Flash1_Type()
)
pm200frs02CtrlConf2Flash1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlConf2Flash1.setStatus("current")
_Pm200frs02CtrlConf2Clear1_Type = EkiOnOff
_Pm200frs02CtrlConf2Clear1_Object = MibScalar
pm200frs02CtrlConf2Clear1 = _Pm200frs02CtrlConf2Clear1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 1, 14),
    _Pm200frs02CtrlConf2Clear1_Type()
)
pm200frs02CtrlConf2Clear1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlConf2Clear1.setStatus("current")
_Pm200frs02Ctrlsynth4_ObjectIdentity = ObjectIdentity
pm200frs02Ctrlsynth4 = _Pm200frs02Ctrlsynth4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 4)
)
_Pm200frs02CtrlCorrelatOn_Type = EkiOnOff
_Pm200frs02CtrlCorrelatOn_Object = MibScalar
pm200frs02CtrlCorrelatOn = _Pm200frs02CtrlCorrelatOn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 4, 1),
    _Pm200frs02CtrlCorrelatOn_Type()
)
pm200frs02CtrlCorrelatOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlCorrelatOn.setStatus("current")
_Pm200frs02CtrlCorrelatOff_Type = EkiOnOff
_Pm200frs02CtrlCorrelatOff_Object = MibScalar
pm200frs02CtrlCorrelatOff = _Pm200frs02CtrlCorrelatOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 4, 2),
    _Pm200frs02CtrlCorrelatOff_Type()
)
pm200frs02CtrlCorrelatOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlCorrelatOff.setStatus("current")
_Pm200frs02CtrlswMgnt_ObjectIdentity = ObjectIdentity
pm200frs02CtrlswMgnt = _Pm200frs02CtrlswMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 5)
)
_Pm200frs02CtrlColdReset_Type = EkiOnOff
_Pm200frs02CtrlColdReset_Object = MibScalar
pm200frs02CtrlColdReset = _Pm200frs02CtrlColdReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 5, 2),
    _Pm200frs02CtrlColdReset_Type()
)
pm200frs02CtrlColdReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlColdReset.setStatus("current")
_Pm200frs02CtrlWarmReset_Type = EkiOnOff
_Pm200frs02CtrlWarmReset_Object = MibScalar
pm200frs02CtrlWarmReset = _Pm200frs02CtrlWarmReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 5, 3),
    _Pm200frs02CtrlWarmReset_Type()
)
pm200frs02CtrlWarmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlWarmReset.setStatus("current")
_Pm200frs02CtrlLoadSwBank1_Type = EkiOnOff
_Pm200frs02CtrlLoadSwBank1_Object = MibScalar
pm200frs02CtrlLoadSwBank1 = _Pm200frs02CtrlLoadSwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 5, 5),
    _Pm200frs02CtrlLoadSwBank1_Type()
)
pm200frs02CtrlLoadSwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLoadSwBank1.setStatus("current")
_Pm200frs02CtrlLoadSwBank2_Type = EkiOnOff
_Pm200frs02CtrlLoadSwBank2_Object = MibScalar
pm200frs02CtrlLoadSwBank2 = _Pm200frs02CtrlLoadSwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 5, 6),
    _Pm200frs02CtrlLoadSwBank2_Type()
)
pm200frs02CtrlLoadSwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLoadSwBank2.setStatus("current")
_Pm200frs02CtrlgwMgnt_ObjectIdentity = ObjectIdentity
pm200frs02CtrlgwMgnt = _Pm200frs02CtrlgwMgnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 6)
)
_Pm200frs02CtrlCurrentGwReset_Type = EkiOnOff
_Pm200frs02CtrlCurrentGwReset_Object = MibScalar
pm200frs02CtrlCurrentGwReset = _Pm200frs02CtrlCurrentGwReset_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 6, 1),
    _Pm200frs02CtrlCurrentGwReset_Type()
)
pm200frs02CtrlCurrentGwReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlCurrentGwReset.setStatus("current")
_Pm200frs02CtrlLoadGwBank1_Type = EkiOnOff
_Pm200frs02CtrlLoadGwBank1_Object = MibScalar
pm200frs02CtrlLoadGwBank1 = _Pm200frs02CtrlLoadGwBank1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 6, 5),
    _Pm200frs02CtrlLoadGwBank1_Type()
)
pm200frs02CtrlLoadGwBank1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLoadGwBank1.setStatus("current")
_Pm200frs02CtrlLoadGwBank2_Type = EkiOnOff
_Pm200frs02CtrlLoadGwBank2_Object = MibScalar
pm200frs02CtrlLoadGwBank2 = _Pm200frs02CtrlLoadGwBank2_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 6, 6),
    _Pm200frs02CtrlLoadGwBank2_Type()
)
pm200frs02CtrlLoadGwBank2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLoadGwBank2.setStatus("current")
_Pm200frs02CtrlLoadGwBank3_Type = EkiOnOff
_Pm200frs02CtrlLoadGwBank3_Object = MibScalar
pm200frs02CtrlLoadGwBank3 = _Pm200frs02CtrlLoadGwBank3_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 6, 7),
    _Pm200frs02CtrlLoadGwBank3_Type()
)
pm200frs02CtrlLoadGwBank3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLoadGwBank3.setStatus("current")
_Pm200frs02CtrlLoadGwBank4_Type = EkiOnOff
_Pm200frs02CtrlLoadGwBank4_Object = MibScalar
pm200frs02CtrlLoadGwBank4 = _Pm200frs02CtrlLoadGwBank4_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 6, 8),
    _Pm200frs02CtrlLoadGwBank4_Type()
)
pm200frs02CtrlLoadGwBank4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLoadGwBank4.setStatus("current")
_Pm200frs02CtrlledTest_ObjectIdentity = ObjectIdentity
pm200frs02CtrlledTest = _Pm200frs02CtrlledTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 192)
)
_Pm200frs02CtrlGreenLed_Type = EkiOnOff
_Pm200frs02CtrlGreenLed_Object = MibScalar
pm200frs02CtrlGreenLed = _Pm200frs02CtrlGreenLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 192, 1),
    _Pm200frs02CtrlGreenLed_Type()
)
pm200frs02CtrlGreenLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlGreenLed.setStatus("current")
_Pm200frs02CtrlRedLed_Type = EkiOnOff
_Pm200frs02CtrlRedLed_Object = MibScalar
pm200frs02CtrlRedLed = _Pm200frs02CtrlRedLed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 192, 2),
    _Pm200frs02CtrlRedLed_Type()
)
pm200frs02CtrlRedLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlRedLed.setStatus("current")
_Pm200frs02CtrlLedOff_Type = EkiOnOff
_Pm200frs02CtrlLedOff_Object = MibScalar
pm200frs02CtrlLedOff = _Pm200frs02CtrlLedOff_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 192, 3),
    _Pm200frs02CtrlLedOff_Type()
)
pm200frs02CtrlLedOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlLedOff.setStatus("current")
_Pm200frs02CtrlinitSwitchMarvell_ObjectIdentity = ObjectIdentity
pm200frs02CtrlinitSwitchMarvell = _Pm200frs02CtrlinitSwitchMarvell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 201)
)
_Pm200frs02CtrlInitSwitchMarvell_Type = EkiOnOff
_Pm200frs02CtrlInitSwitchMarvell_Object = MibScalar
pm200frs02CtrlInitSwitchMarvell = _Pm200frs02CtrlInitSwitchMarvell_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 201, 1),
    _Pm200frs02CtrlInitSwitchMarvell_Type()
)
pm200frs02CtrlInitSwitchMarvell.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlInitSwitchMarvell.setStatus("current")
_Pm200frs02CtrlresetCount_ObjectIdentity = ObjectIdentity
pm200frs02CtrlresetCount = _Pm200frs02CtrlresetCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 259)
)
_Pm200frs02CtrlResetcount_Type = EkiOnOff
_Pm200frs02CtrlResetcount_Object = MibScalar
pm200frs02CtrlResetcount = _Pm200frs02CtrlResetcount_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 259, 1),
    _Pm200frs02CtrlResetcount_Type()
)
pm200frs02CtrlResetcount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlResetcount.setStatus("current")
_Pm200frs02CtrlresetRmon_ObjectIdentity = ObjectIdentity
pm200frs02CtrlresetRmon = _Pm200frs02CtrlresetRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 260)
)
_Pm200frs02CtrlResetrmon_Type = EkiOnOff
_Pm200frs02CtrlResetrmon_Object = MibScalar
pm200frs02CtrlResetrmon = _Pm200frs02CtrlResetrmon_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 260, 1),
    _Pm200frs02CtrlResetrmon_Type()
)
pm200frs02CtrlResetrmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlResetrmon.setStatus("current")
_Pm200frs02CtrlresetMeasurements_ObjectIdentity = ObjectIdentity
pm200frs02CtrlresetMeasurements = _Pm200frs02CtrlresetMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 261)
)
_Pm200frs02CtrlResetmeasurements_Type = EkiOnOff
_Pm200frs02CtrlResetmeasurements_Object = MibScalar
pm200frs02CtrlResetmeasurements = _Pm200frs02CtrlResetmeasurements_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 1, 261, 1),
    _Pm200frs02CtrlResetmeasurements_Type()
)
pm200frs02CtrlResetmeasurements.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlResetmeasurements.setStatus("current")
_Pm200frs02CtrlClient_ObjectIdentity = ObjectIdentity
pm200frs02CtrlClient = _Pm200frs02CtrlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2)
)
_Pm200frs02CtrlaccessLoopTable_Object = MibTable
pm200frs02CtrlaccessLoopTable = _Pm200frs02CtrlaccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 16)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlaccessLoopTable.setStatus("current")
_Pm200frs02CtrlaccessLoopEntry_Object = MibTableRow
pm200frs02CtrlaccessLoopEntry = _Pm200frs02CtrlaccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 16, 1)
)
pm200frs02CtrlaccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlaccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlaccessLoopEntry.setStatus("current")


class _Pm200frs02CtrlaccessLoopIndex_Type(Integer32):
    """Custom type pm200frs02CtrlaccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlaccessLoopIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlaccessLoopIndex_Object = MibTableColumn
pm200frs02CtrlaccessLoopIndex = _Pm200frs02CtrlaccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 16, 1, 1),
    _Pm200frs02CtrlaccessLoopIndex_Type()
)
pm200frs02CtrlaccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlaccessLoopIndex.setStatus("current")
_Pm200frs02CtrlaccessLoopPortn_Type = EkiState
_Pm200frs02CtrlaccessLoopPortn_Object = MibTableColumn
pm200frs02CtrlaccessLoopPortn = _Pm200frs02CtrlaccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 16, 1, 2),
    _Pm200frs02CtrlaccessLoopPortn_Type()
)
pm200frs02CtrlaccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlaccessLoopPortn.setStatus("current")
_Pm200frs02CtrlclientLoopToLineTable_Object = MibTable
pm200frs02CtrlclientLoopToLineTable = _Pm200frs02CtrlclientLoopToLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 17)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlclientLoopToLineTable.setStatus("current")
_Pm200frs02CtrlclientLoopToLineEntry_Object = MibTableRow
pm200frs02CtrlclientLoopToLineEntry = _Pm200frs02CtrlclientLoopToLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 17, 1)
)
pm200frs02CtrlclientLoopToLineEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlclientLoopToLineIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlclientLoopToLineEntry.setStatus("current")


class _Pm200frs02CtrlclientLoopToLineIndex_Type(Integer32):
    """Custom type pm200frs02CtrlclientLoopToLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlclientLoopToLineIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlclientLoopToLineIndex_Object = MibTableColumn
pm200frs02CtrlclientLoopToLineIndex = _Pm200frs02CtrlclientLoopToLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 17, 1, 1),
    _Pm200frs02CtrlclientLoopToLineIndex_Type()
)
pm200frs02CtrlclientLoopToLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlclientLoopToLineIndex.setStatus("current")
_Pm200frs02CtrlclientLoopToLinePortn_Type = EkiState
_Pm200frs02CtrlclientLoopToLinePortn_Object = MibTableColumn
pm200frs02CtrlclientLoopToLinePortn = _Pm200frs02CtrlclientLoopToLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 17, 1, 2),
    _Pm200frs02CtrlclientLoopToLinePortn_Type()
)
pm200frs02CtrlclientLoopToLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlclientLoopToLinePortn.setStatus("current")
_Pm200frs02CtrlcsfUpInsTable_Object = MibTable
pm200frs02CtrlcsfUpInsTable = _Pm200frs02CtrlcsfUpInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 21)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlcsfUpInsTable.setStatus("current")
_Pm200frs02CtrlcsfUpInsEntry_Object = MibTableRow
pm200frs02CtrlcsfUpInsEntry = _Pm200frs02CtrlcsfUpInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 21, 1)
)
pm200frs02CtrlcsfUpInsEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlcsfUpInsIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlcsfUpInsEntry.setStatus("current")


class _Pm200frs02CtrlcsfUpInsIndex_Type(Integer32):
    """Custom type pm200frs02CtrlcsfUpInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlcsfUpInsIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlcsfUpInsIndex_Object = MibTableColumn
pm200frs02CtrlcsfUpInsIndex = _Pm200frs02CtrlcsfUpInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 21, 1, 1),
    _Pm200frs02CtrlcsfUpInsIndex_Type()
)
pm200frs02CtrlcsfUpInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlcsfUpInsIndex.setStatus("current")
_Pm200frs02CtrlcsfUpInsPortn_Type = EkiState
_Pm200frs02CtrlcsfUpInsPortn_Object = MibTableColumn
pm200frs02CtrlcsfUpInsPortn = _Pm200frs02CtrlcsfUpInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 21, 1, 2),
    _Pm200frs02CtrlcsfUpInsPortn_Type()
)
pm200frs02CtrlcsfUpInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlcsfUpInsPortn.setStatus("current")
_Pm200frs02CtrlcaisDwInsTable_Object = MibTable
pm200frs02CtrlcaisDwInsTable = _Pm200frs02CtrlcaisDwInsTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 22)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlcaisDwInsTable.setStatus("current")
_Pm200frs02CtrlcaisDwInsEntry_Object = MibTableRow
pm200frs02CtrlcaisDwInsEntry = _Pm200frs02CtrlcaisDwInsEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 22, 1)
)
pm200frs02CtrlcaisDwInsEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlcaisDwInsIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlcaisDwInsEntry.setStatus("current")


class _Pm200frs02CtrlcaisDwInsIndex_Type(Integer32):
    """Custom type pm200frs02CtrlcaisDwInsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlcaisDwInsIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlcaisDwInsIndex_Object = MibTableColumn
pm200frs02CtrlcaisDwInsIndex = _Pm200frs02CtrlcaisDwInsIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 22, 1, 1),
    _Pm200frs02CtrlcaisDwInsIndex_Type()
)
pm200frs02CtrlcaisDwInsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlcaisDwInsIndex.setStatus("current")
_Pm200frs02CtrlcaisDwInsPortn_Type = EkiState
_Pm200frs02CtrlcaisDwInsPortn_Object = MibTableColumn
pm200frs02CtrlcaisDwInsPortn = _Pm200frs02CtrlcaisDwInsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 22, 1, 2),
    _Pm200frs02CtrlcaisDwInsPortn_Type()
)
pm200frs02CtrlcaisDwInsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlcaisDwInsPortn.setStatus("current")
_Pm200frs02CtrlclientResetAllCountTable_Object = MibTable
pm200frs02CtrlclientResetAllCountTable = _Pm200frs02CtrlclientResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 262)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlclientResetAllCountTable.setStatus("current")
_Pm200frs02CtrlclientResetAllCountEntry_Object = MibTableRow
pm200frs02CtrlclientResetAllCountEntry = _Pm200frs02CtrlclientResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 262, 1)
)
pm200frs02CtrlclientResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlclientResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlclientResetAllCountEntry.setStatus("current")


class _Pm200frs02CtrlclientResetAllCountIndex_Type(Integer32):
    """Custom type pm200frs02CtrlclientResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlclientResetAllCountIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlclientResetAllCountIndex_Object = MibTableColumn
pm200frs02CtrlclientResetAllCountIndex = _Pm200frs02CtrlclientResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 262, 1, 1),
    _Pm200frs02CtrlclientResetAllCountIndex_Type()
)
pm200frs02CtrlclientResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlclientResetAllCountIndex.setStatus("current")
_Pm200frs02CtrlclientResetAllCountsPortn_Type = EkiState
_Pm200frs02CtrlclientResetAllCountsPortn_Object = MibTableColumn
pm200frs02CtrlclientResetAllCountsPortn = _Pm200frs02CtrlclientResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 2, 262, 1, 2),
    _Pm200frs02CtrlclientResetAllCountsPortn_Type()
)
pm200frs02CtrlclientResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlclientResetAllCountsPortn.setStatus("current")
_Pm200frs02CtrlLine_ObjectIdentity = ObjectIdentity
pm200frs02CtrlLine = _Pm200frs02CtrlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3)
)
_Pm200frs02CtrlcommAccessLoopTable_Object = MibTable
pm200frs02CtrlcommAccessLoopTable = _Pm200frs02CtrlcommAccessLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 64)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlcommAccessLoopTable.setStatus("current")
_Pm200frs02CtrlcommAccessLoopEntry_Object = MibTableRow
pm200frs02CtrlcommAccessLoopEntry = _Pm200frs02CtrlcommAccessLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 64, 1)
)
pm200frs02CtrlcommAccessLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlcommAccessLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlcommAccessLoopEntry.setStatus("current")


class _Pm200frs02CtrlcommAccessLoopIndex_Type(Integer32):
    """Custom type pm200frs02CtrlcommAccessLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlcommAccessLoopIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlcommAccessLoopIndex_Object = MibTableColumn
pm200frs02CtrlcommAccessLoopIndex = _Pm200frs02CtrlcommAccessLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 64, 1, 1),
    _Pm200frs02CtrlcommAccessLoopIndex_Type()
)
pm200frs02CtrlcommAccessLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlcommAccessLoopIndex.setStatus("current")
_Pm200frs02CtrlcommAccessLoopPortn_Type = EkiState
_Pm200frs02CtrlcommAccessLoopPortn_Object = MibTableColumn
pm200frs02CtrlcommAccessLoopPortn = _Pm200frs02CtrlcommAccessLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 64, 1, 2),
    _Pm200frs02CtrlcommAccessLoopPortn_Type()
)
pm200frs02CtrlcommAccessLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlcommAccessLoopPortn.setStatus("current")
_Pm200frs02CtrllineLoopTable_Object = MibTable
pm200frs02CtrllineLoopTable = _Pm200frs02CtrllineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 66)
)
if mibBuilder.loadTexts:
    pm200frs02CtrllineLoopTable.setStatus("current")
_Pm200frs02CtrllineLoopEntry_Object = MibTableRow
pm200frs02CtrllineLoopEntry = _Pm200frs02CtrllineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 66, 1)
)
pm200frs02CtrllineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrllineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrllineLoopEntry.setStatus("current")


class _Pm200frs02CtrllineLoopIndex_Type(Integer32):
    """Custom type pm200frs02CtrllineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrllineLoopIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrllineLoopIndex_Object = MibTableColumn
pm200frs02CtrllineLoopIndex = _Pm200frs02CtrllineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 66, 1, 1),
    _Pm200frs02CtrllineLoopIndex_Type()
)
pm200frs02CtrllineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrllineLoopIndex.setStatus("current")
_Pm200frs02CtrllineLoopPortn_Type = EkiState
_Pm200frs02CtrllineLoopPortn_Object = MibTableColumn
pm200frs02CtrllineLoopPortn = _Pm200frs02CtrllineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 66, 1, 2),
    _Pm200frs02CtrllineLoopPortn_Type()
)
pm200frs02CtrllineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrllineLoopPortn.setStatus("current")
_Pm200frs02CtrlfecDisableTable_Object = MibTable
pm200frs02CtrlfecDisableTable = _Pm200frs02CtrlfecDisableTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 69)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlfecDisableTable.setStatus("current")
_Pm200frs02CtrlfecDisableEntry_Object = MibTableRow
pm200frs02CtrlfecDisableEntry = _Pm200frs02CtrlfecDisableEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 69, 1)
)
pm200frs02CtrlfecDisableEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlfecDisableIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlfecDisableEntry.setStatus("current")


class _Pm200frs02CtrlfecDisableIndex_Type(Integer32):
    """Custom type pm200frs02CtrlfecDisableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlfecDisableIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlfecDisableIndex_Object = MibTableColumn
pm200frs02CtrlfecDisableIndex = _Pm200frs02CtrlfecDisableIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 69, 1, 1),
    _Pm200frs02CtrlfecDisableIndex_Type()
)
pm200frs02CtrlfecDisableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlfecDisableIndex.setStatus("current")
_Pm200frs02CtrlfecDisablePortn_Type = EkiState
_Pm200frs02CtrlfecDisablePortn_Object = MibTableColumn
pm200frs02CtrlfecDisablePortn = _Pm200frs02CtrlfecDisablePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 69, 1, 2),
    _Pm200frs02CtrlfecDisablePortn_Type()
)
pm200frs02CtrlfecDisablePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlfecDisablePortn.setStatus("current")
_Pm200frs02CtrlmsaLineLoopTable_Object = MibTable
pm200frs02CtrlmsaLineLoopTable = _Pm200frs02CtrlmsaLineLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 209)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaLineLoopTable.setStatus("current")
_Pm200frs02CtrlmsaLineLoopEntry_Object = MibTableRow
pm200frs02CtrlmsaLineLoopEntry = _Pm200frs02CtrlmsaLineLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 209, 1)
)
pm200frs02CtrlmsaLineLoopEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlmsaLineLoopIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaLineLoopEntry.setStatus("current")


class _Pm200frs02CtrlmsaLineLoopIndex_Type(Integer32):
    """Custom type pm200frs02CtrlmsaLineLoopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlmsaLineLoopIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlmsaLineLoopIndex_Object = MibTableColumn
pm200frs02CtrlmsaLineLoopIndex = _Pm200frs02CtrlmsaLineLoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 209, 1, 1),
    _Pm200frs02CtrlmsaLineLoopIndex_Type()
)
pm200frs02CtrlmsaLineLoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaLineLoopIndex.setStatus("current")
_Pm200frs02CtrlmsaLineLoopPortn_Type = EkiState
_Pm200frs02CtrlmsaLineLoopPortn_Object = MibTableColumn
pm200frs02CtrlmsaLineLoopPortn = _Pm200frs02CtrlmsaLineLoopPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 209, 1, 2),
    _Pm200frs02CtrlmsaLineLoopPortn_Type()
)
pm200frs02CtrlmsaLineLoopPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaLineLoopPortn.setStatus("current")
_Pm200frs02CtrlmsaTxResetTable_Object = MibTable
pm200frs02CtrlmsaTxResetTable = _Pm200frs02CtrlmsaTxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 210)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaTxResetTable.setStatus("current")
_Pm200frs02CtrlmsaTxResetEntry_Object = MibTableRow
pm200frs02CtrlmsaTxResetEntry = _Pm200frs02CtrlmsaTxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 210, 1)
)
pm200frs02CtrlmsaTxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlmsaTxResetIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaTxResetEntry.setStatus("current")


class _Pm200frs02CtrlmsaTxResetIndex_Type(Integer32):
    """Custom type pm200frs02CtrlmsaTxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlmsaTxResetIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlmsaTxResetIndex_Object = MibTableColumn
pm200frs02CtrlmsaTxResetIndex = _Pm200frs02CtrlmsaTxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 210, 1, 1),
    _Pm200frs02CtrlmsaTxResetIndex_Type()
)
pm200frs02CtrlmsaTxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaTxResetIndex.setStatus("current")
_Pm200frs02CtrlmsaTxResetPortn_Type = EkiState
_Pm200frs02CtrlmsaTxResetPortn_Object = MibTableColumn
pm200frs02CtrlmsaTxResetPortn = _Pm200frs02CtrlmsaTxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 210, 1, 2),
    _Pm200frs02CtrlmsaTxResetPortn_Type()
)
pm200frs02CtrlmsaTxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaTxResetPortn.setStatus("current")
_Pm200frs02CtrlmsaRxResetTable_Object = MibTable
pm200frs02CtrlmsaRxResetTable = _Pm200frs02CtrlmsaRxResetTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 211)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaRxResetTable.setStatus("current")
_Pm200frs02CtrlmsaRxResetEntry_Object = MibTableRow
pm200frs02CtrlmsaRxResetEntry = _Pm200frs02CtrlmsaRxResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 211, 1)
)
pm200frs02CtrlmsaRxResetEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlmsaRxResetIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaRxResetEntry.setStatus("current")


class _Pm200frs02CtrlmsaRxResetIndex_Type(Integer32):
    """Custom type pm200frs02CtrlmsaRxResetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlmsaRxResetIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlmsaRxResetIndex_Object = MibTableColumn
pm200frs02CtrlmsaRxResetIndex = _Pm200frs02CtrlmsaRxResetIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 211, 1, 1),
    _Pm200frs02CtrlmsaRxResetIndex_Type()
)
pm200frs02CtrlmsaRxResetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaRxResetIndex.setStatus("current")
_Pm200frs02CtrlmsaRxResetPortn_Type = EkiState
_Pm200frs02CtrlmsaRxResetPortn_Object = MibTableColumn
pm200frs02CtrlmsaRxResetPortn = _Pm200frs02CtrlmsaRxResetPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 211, 1, 2),
    _Pm200frs02CtrlmsaRxResetPortn_Type()
)
pm200frs02CtrlmsaRxResetPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaRxResetPortn.setStatus("current")
_Pm200frs02CtrlmsaShutdownTable_Object = MibTable
pm200frs02CtrlmsaShutdownTable = _Pm200frs02CtrlmsaShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 212)
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaShutdownTable.setStatus("current")
_Pm200frs02CtrlmsaShutdownEntry_Object = MibTableRow
pm200frs02CtrlmsaShutdownEntry = _Pm200frs02CtrlmsaShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 212, 1)
)
pm200frs02CtrlmsaShutdownEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrlmsaShutdownIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaShutdownEntry.setStatus("current")


class _Pm200frs02CtrlmsaShutdownIndex_Type(Integer32):
    """Custom type pm200frs02CtrlmsaShutdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrlmsaShutdownIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrlmsaShutdownIndex_Object = MibTableColumn
pm200frs02CtrlmsaShutdownIndex = _Pm200frs02CtrlmsaShutdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 212, 1, 1),
    _Pm200frs02CtrlmsaShutdownIndex_Type()
)
pm200frs02CtrlmsaShutdownIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaShutdownIndex.setStatus("current")
_Pm200frs02CtrlmsaShutdownPortn_Type = EkiState
_Pm200frs02CtrlmsaShutdownPortn_Object = MibTableColumn
pm200frs02CtrlmsaShutdownPortn = _Pm200frs02CtrlmsaShutdownPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 212, 1, 2),
    _Pm200frs02CtrlmsaShutdownPortn_Type()
)
pm200frs02CtrlmsaShutdownPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrlmsaShutdownPortn.setStatus("current")
_Pm200frs02CtrllineResetAllCountTable_Object = MibTable
pm200frs02CtrllineResetAllCountTable = _Pm200frs02CtrllineResetAllCountTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 263)
)
if mibBuilder.loadTexts:
    pm200frs02CtrllineResetAllCountTable.setStatus("current")
_Pm200frs02CtrllineResetAllCountEntry_Object = MibTableRow
pm200frs02CtrllineResetAllCountEntry = _Pm200frs02CtrllineResetAllCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 263, 1)
)
pm200frs02CtrllineResetAllCountEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CtrllineResetAllCountIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CtrllineResetAllCountEntry.setStatus("current")


class _Pm200frs02CtrllineResetAllCountIndex_Type(Integer32):
    """Custom type pm200frs02CtrllineResetAllCountIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CtrllineResetAllCountIndex_Type.__name__ = "Integer32"
_Pm200frs02CtrllineResetAllCountIndex_Object = MibTableColumn
pm200frs02CtrllineResetAllCountIndex = _Pm200frs02CtrllineResetAllCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 263, 1, 1),
    _Pm200frs02CtrllineResetAllCountIndex_Type()
)
pm200frs02CtrllineResetAllCountIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CtrllineResetAllCountIndex.setStatus("current")
_Pm200frs02CtrllineResetAllCountsPortn_Type = EkiState
_Pm200frs02CtrllineResetAllCountsPortn_Object = MibTableColumn
pm200frs02CtrllineResetAllCountsPortn = _Pm200frs02CtrllineResetAllCountsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 6, 3, 263, 1, 2),
    _Pm200frs02CtrllineResetAllCountsPortn_Type()
)
pm200frs02CtrllineResetAllCountsPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CtrllineResetAllCountsPortn.setStatus("current")
_Pm200frs02ri_ObjectIdentity = ObjectIdentity
pm200frs02ri = _Pm200frs02ri_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7)
)
_Pm200frs02riTable_ObjectIdentity = ObjectIdentity
pm200frs02riTable = _Pm200frs02riTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1)
)
_Pm200frs02RinvSfpTable_Object = MibTable
pm200frs02RinvSfpTable = _Pm200frs02RinvSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 1)
)
if mibBuilder.loadTexts:
    pm200frs02RinvSfpTable.setStatus("current")
_Pm200frs02RinvSfpEntry_Object = MibTableRow
pm200frs02RinvSfpEntry = _Pm200frs02RinvSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 1, 1)
)
pm200frs02RinvSfpEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02RinvSfpIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02RinvSfpEntry.setStatus("current")


class _Pm200frs02RinvSfpIndex_Type(Integer32):
    """Custom type pm200frs02RinvSfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm200frs02RinvSfpIndex_Type.__name__ = "Integer32"
_Pm200frs02RinvSfpIndex_Object = MibTableColumn
pm200frs02RinvSfpIndex = _Pm200frs02RinvSfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 1, 1, 1),
    _Pm200frs02RinvSfpIndex_Type()
)
pm200frs02RinvSfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvSfpIndex.setStatus("current")
_Pm200frs02Rinvsfp_Type = DisplayString
_Pm200frs02Rinvsfp_Object = MibTableColumn
pm200frs02Rinvsfp = _Pm200frs02Rinvsfp_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 1, 1, 2),
    _Pm200frs02Rinvsfp_Type()
)
pm200frs02Rinvsfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02Rinvsfp.setStatus("current")
_Pm200frs02RinvLineTable_Object = MibTable
pm200frs02RinvLineTable = _Pm200frs02RinvLineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 2)
)
if mibBuilder.loadTexts:
    pm200frs02RinvLineTable.setStatus("current")
_Pm200frs02RinvLineEntry_Object = MibTableRow
pm200frs02RinvLineEntry = _Pm200frs02RinvLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 2, 1)
)
pm200frs02RinvLineEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02RinvLineIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02RinvLineEntry.setStatus("current")


class _Pm200frs02RinvLineIndex_Type(Integer32):
    """Custom type pm200frs02RinvLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pm200frs02RinvLineIndex_Type.__name__ = "Integer32"
_Pm200frs02RinvLineIndex_Object = MibTableColumn
pm200frs02RinvLineIndex = _Pm200frs02RinvLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 2, 1, 1),
    _Pm200frs02RinvLineIndex_Type()
)
pm200frs02RinvLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvLineIndex.setStatus("current")
_Pm200frs02RinvxfpLine_Type = DisplayString
_Pm200frs02RinvxfpLine_Object = MibTableColumn
pm200frs02RinvxfpLine = _Pm200frs02RinvxfpLine_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 1, 2, 1, 2),
    _Pm200frs02RinvxfpLine_Type()
)
pm200frs02RinvxfpLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvxfpLine.setStatus("current")
_Pm200frs02RinvReloadInventory_Type = EkiOnOff
_Pm200frs02RinvReloadInventory_Object = MibScalar
pm200frs02RinvReloadInventory = _Pm200frs02RinvReloadInventory_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 2),
    _Pm200frs02RinvReloadInventory_Type()
)
pm200frs02RinvReloadInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02RinvReloadInventory.setStatus("current")
_Pm200frs02RinvHwPlatform_Type = DisplayString
_Pm200frs02RinvHwPlatform_Object = MibScalar
pm200frs02RinvHwPlatform = _Pm200frs02RinvHwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 3),
    _Pm200frs02RinvHwPlatform_Type()
)
pm200frs02RinvHwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvHwPlatform.setStatus("current")
_Pm200frs02RinvModulePlatform_Type = DisplayString
_Pm200frs02RinvModulePlatform_Object = MibScalar
pm200frs02RinvModulePlatform = _Pm200frs02RinvModulePlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 4),
    _Pm200frs02RinvModulePlatform_Type()
)
pm200frs02RinvModulePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvModulePlatform.setStatus("current")
_Pm200frs02RinvSwPlatform_Type = DisplayString
_Pm200frs02RinvSwPlatform_Object = MibScalar
pm200frs02RinvSwPlatform = _Pm200frs02RinvSwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 5),
    _Pm200frs02RinvSwPlatform_Type()
)
pm200frs02RinvSwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvSwPlatform.setStatus("current")
_Pm200frs02RinvGwPlatform_Type = DisplayString
_Pm200frs02RinvGwPlatform_Object = MibScalar
pm200frs02RinvGwPlatform = _Pm200frs02RinvGwPlatform_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 7, 6),
    _Pm200frs02RinvGwPlatform_Type()
)
pm200frs02RinvGwPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02RinvGwPlatform.setStatus("current")
_Pm200frs02download_ObjectIdentity = ObjectIdentity
pm200frs02download = _Pm200frs02download_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8)
)
_Pm200frs02DwlOther_ObjectIdentity = ObjectIdentity
pm200frs02DwlOther = _Pm200frs02DwlOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1)
)
_Pm200frs02DwlrestartProcess_ObjectIdentity = ObjectIdentity
pm200frs02DwlrestartProcess = _Pm200frs02DwlrestartProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 0)
)
_Pm200frs02DwlWarmRestartProcessed_Type = EkiOnOff
_Pm200frs02DwlWarmRestartProcessed_Object = MibScalar
pm200frs02DwlWarmRestartProcessed = _Pm200frs02DwlWarmRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 0, 1),
    _Pm200frs02DwlWarmRestartProcessed_Type()
)
pm200frs02DwlWarmRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlWarmRestartProcessed.setStatus("current")
_Pm200frs02DwlColdRestartProcessed_Type = EkiOnOff
_Pm200frs02DwlColdRestartProcessed_Object = MibScalar
pm200frs02DwlColdRestartProcessed = _Pm200frs02DwlColdRestartProcessed_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 0, 2),
    _Pm200frs02DwlColdRestartProcessed_Type()
)
pm200frs02DwlColdRestartProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlColdRestartProcessed.setStatus("current")
_Pm200frs02DwlswBanksUsed_ObjectIdentity = ObjectIdentity
pm200frs02DwlswBanksUsed = _Pm200frs02DwlswBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 1)
)
_Pm200frs02DwlSwBank1Used_Type = EkiOnOff
_Pm200frs02DwlSwBank1Used_Object = MibScalar
pm200frs02DwlSwBank1Used = _Pm200frs02DwlSwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 1, 1),
    _Pm200frs02DwlSwBank1Used_Type()
)
pm200frs02DwlSwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlSwBank1Used.setStatus("current")
_Pm200frs02DwlSwBank2Used_Type = EkiOnOff
_Pm200frs02DwlSwBank2Used_Object = MibScalar
pm200frs02DwlSwBank2Used = _Pm200frs02DwlSwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 1, 2),
    _Pm200frs02DwlSwBank2Used_Type()
)
pm200frs02DwlSwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlSwBank2Used.setStatus("current")
_Pm200frs02DwlSwBank1Notempty_Type = EkiOnOff
_Pm200frs02DwlSwBank1Notempty_Object = MibScalar
pm200frs02DwlSwBank1Notempty = _Pm200frs02DwlSwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 1, 5),
    _Pm200frs02DwlSwBank1Notempty_Type()
)
pm200frs02DwlSwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlSwBank1Notempty.setStatus("current")
_Pm200frs02DwlSwBank2Notempty_Type = EkiOnOff
_Pm200frs02DwlSwBank2Notempty_Object = MibScalar
pm200frs02DwlSwBank2Notempty = _Pm200frs02DwlSwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 1, 6),
    _Pm200frs02DwlSwBank2Notempty_Type()
)
pm200frs02DwlSwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlSwBank2Notempty.setStatus("current")
_Pm200frs02DwlgwBanksUsed_ObjectIdentity = ObjectIdentity
pm200frs02DwlgwBanksUsed = _Pm200frs02DwlgwBanksUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2)
)
_Pm200frs02DwlGwBank1Used_Type = EkiOnOff
_Pm200frs02DwlGwBank1Used_Object = MibScalar
pm200frs02DwlGwBank1Used = _Pm200frs02DwlGwBank1Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 1),
    _Pm200frs02DwlGwBank1Used_Type()
)
pm200frs02DwlGwBank1Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank1Used.setStatus("current")
_Pm200frs02DwlGwBank2Used_Type = EkiOnOff
_Pm200frs02DwlGwBank2Used_Object = MibScalar
pm200frs02DwlGwBank2Used = _Pm200frs02DwlGwBank2Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 2),
    _Pm200frs02DwlGwBank2Used_Type()
)
pm200frs02DwlGwBank2Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank2Used.setStatus("current")
_Pm200frs02DwlGwBank3Used_Type = EkiOnOff
_Pm200frs02DwlGwBank3Used_Object = MibScalar
pm200frs02DwlGwBank3Used = _Pm200frs02DwlGwBank3Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 3),
    _Pm200frs02DwlGwBank3Used_Type()
)
pm200frs02DwlGwBank3Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank3Used.setStatus("current")
_Pm200frs02DwlGwBank4Used_Type = EkiOnOff
_Pm200frs02DwlGwBank4Used_Object = MibScalar
pm200frs02DwlGwBank4Used = _Pm200frs02DwlGwBank4Used_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 4),
    _Pm200frs02DwlGwBank4Used_Type()
)
pm200frs02DwlGwBank4Used.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank4Used.setStatus("current")
_Pm200frs02DwlGwBank1Notempty_Type = EkiOnOff
_Pm200frs02DwlGwBank1Notempty_Object = MibScalar
pm200frs02DwlGwBank1Notempty = _Pm200frs02DwlGwBank1Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 5),
    _Pm200frs02DwlGwBank1Notempty_Type()
)
pm200frs02DwlGwBank1Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank1Notempty.setStatus("current")
_Pm200frs02DwlGwBank2Notempty_Type = EkiOnOff
_Pm200frs02DwlGwBank2Notempty_Object = MibScalar
pm200frs02DwlGwBank2Notempty = _Pm200frs02DwlGwBank2Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 6),
    _Pm200frs02DwlGwBank2Notempty_Type()
)
pm200frs02DwlGwBank2Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank2Notempty.setStatus("current")
_Pm200frs02DwlGwBank3Notempty_Type = EkiOnOff
_Pm200frs02DwlGwBank3Notempty_Object = MibScalar
pm200frs02DwlGwBank3Notempty = _Pm200frs02DwlGwBank3Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 7),
    _Pm200frs02DwlGwBank3Notempty_Type()
)
pm200frs02DwlGwBank3Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank3Notempty.setStatus("current")
_Pm200frs02DwlGwBank4Notempty_Type = EkiOnOff
_Pm200frs02DwlGwBank4Notempty_Object = MibScalar
pm200frs02DwlGwBank4Notempty = _Pm200frs02DwlGwBank4Notempty_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 1, 2, 8),
    _Pm200frs02DwlGwBank4Notempty_Type()
)
pm200frs02DwlGwBank4Notempty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02DwlGwBank4Notempty.setStatus("current")
_Pm200frs02DwlClient_ObjectIdentity = ObjectIdentity
pm200frs02DwlClient = _Pm200frs02DwlClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 2)
)
_Pm200frs02DwlLine_ObjectIdentity = ObjectIdentity
pm200frs02DwlLine = _Pm200frs02DwlLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 8, 3)
)
_Pm200frs02Config_ObjectIdentity = ObjectIdentity
pm200frs02Config = _Pm200frs02Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9)
)
_Pm200frs02CfgAccessCAisCsf_ObjectIdentity = ObjectIdentity
pm200frs02CfgAccessCAisCsf = _Pm200frs02CfgAccessCAisCsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 1)
)
_Pm200frs02CfgClientcaiscsfTable_Object = MibTable
pm200frs02CfgClientcaiscsfTable = _Pm200frs02CfgClientcaiscsfTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 1, 1)
)
if mibBuilder.loadTexts:
    pm200frs02CfgClientcaiscsfTable.setStatus("current")
_Pm200frs02CfgClientcaiscsfEntry_Object = MibTableRow
pm200frs02CfgClientcaiscsfEntry = _Pm200frs02CfgClientcaiscsfEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 1, 1, 1)
)
pm200frs02CfgClientcaiscsfEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgClientcaiscsfIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgClientcaiscsfEntry.setStatus("current")


class _Pm200frs02CfgClientcaiscsfIndex_Type(Integer32):
    """Custom type pm200frs02CfgClientcaiscsfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgClientcaiscsfIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgClientcaiscsfIndex_Object = MibTableColumn
pm200frs02CfgClientcaiscsfIndex = _Pm200frs02CfgClientcaiscsfIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 1, 1, 1, 1),
    _Pm200frs02CfgClientcaiscsfIndex_Type()
)
pm200frs02CfgClientcaiscsfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgClientcaiscsfIndex.setStatus("current")


class _Pm200frs02CfgReservePortn_Type(Unsigned32):
    """Custom type pm200frs02CfgReservePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgReservePortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgReservePortn_Object = MibTableColumn
pm200frs02CfgReservePortn = _Pm200frs02CfgReservePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 1, 1, 1, 3),
    _Pm200frs02CfgReservePortn_Type()
)
pm200frs02CfgReservePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgReservePortn.setStatus("current")
_Pm200frs02CfgStartup_ObjectIdentity = ObjectIdentity
pm200frs02CfgStartup = _Pm200frs02CfgStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2)
)
_Pm200frs02CfgClientStartupTable_Object = MibTable
pm200frs02CfgClientStartupTable = _Pm200frs02CfgClientStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 1)
)
if mibBuilder.loadTexts:
    pm200frs02CfgClientStartupTable.setStatus("current")
_Pm200frs02CfgClientStartupEntry_Object = MibTableRow
pm200frs02CfgClientStartupEntry = _Pm200frs02CfgClientStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 1, 1)
)
pm200frs02CfgClientStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgClientStartupIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgClientStartupEntry.setStatus("current")


class _Pm200frs02CfgClientStartupIndex_Type(Integer32):
    """Custom type pm200frs02CfgClientStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgClientStartupIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgClientStartupIndex_Object = MibTableColumn
pm200frs02CfgClientStartupIndex = _Pm200frs02CfgClientStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 1, 1, 1),
    _Pm200frs02CfgClientStartupIndex_Type()
)
pm200frs02CfgClientStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgClientStartupIndex.setStatus("current")


class _Pm200frs02CfgSystConfPortPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgSystConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgSystConfPortPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgSystConfPortPortn_Object = MibTableColumn
pm200frs02CfgSystConfPortPortn = _Pm200frs02CfgSystConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 1, 1, 3),
    _Pm200frs02CfgSystConfPortPortn_Type()
)
pm200frs02CfgSystConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgSystConfPortPortn.setStatus("current")


class _Pm200frs02CfgNetConfPortPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgNetConfPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgNetConfPortPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgNetConfPortPortn_Object = MibTableColumn
pm200frs02CfgNetConfPortPortn = _Pm200frs02CfgNetConfPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 1, 1, 4),
    _Pm200frs02CfgNetConfPortPortn_Type()
)
pm200frs02CfgNetConfPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgNetConfPortPortn.setStatus("current")


class _Pm200frs02CfgOptionsPortPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgOptionsPortPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgOptionsPortPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgOptionsPortPortn_Object = MibTableColumn
pm200frs02CfgOptionsPortPortn = _Pm200frs02CfgOptionsPortPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 1, 1, 14),
    _Pm200frs02CfgOptionsPortPortn_Type()
)
pm200frs02CfgOptionsPortPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgOptionsPortPortn.setStatus("current")
_Pm200frs02CfgLineStartupTable_Object = MibTable
pm200frs02CfgLineStartupTable = _Pm200frs02CfgLineStartupTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 2)
)
if mibBuilder.loadTexts:
    pm200frs02CfgLineStartupTable.setStatus("current")
_Pm200frs02CfgLineStartupEntry_Object = MibTableRow
pm200frs02CfgLineStartupEntry = _Pm200frs02CfgLineStartupEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 2, 1)
)
pm200frs02CfgLineStartupEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgLineStartupIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgLineStartupEntry.setStatus("current")


class _Pm200frs02CfgLineStartupIndex_Type(Integer32):
    """Custom type pm200frs02CfgLineStartupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgLineStartupIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgLineStartupIndex_Object = MibTableColumn
pm200frs02CfgLineStartupIndex = _Pm200frs02CfgLineStartupIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 2, 1, 1),
    _Pm200frs02CfgLineStartupIndex_Type()
)
pm200frs02CfgLineStartupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgLineStartupIndex.setStatus("current")


class _Pm200frs02CfgSystConfLinePortn_Type(Unsigned32):
    """Custom type pm200frs02CfgSystConfLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgSystConfLinePortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgSystConfLinePortn_Object = MibTableColumn
pm200frs02CfgSystConfLinePortn = _Pm200frs02CfgSystConfLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 2, 1, 3),
    _Pm200frs02CfgSystConfLinePortn_Type()
)
pm200frs02CfgSystConfLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgSystConfLinePortn.setStatus("current")


class _Pm200frs02CfgOptionsLinePortn_Type(Unsigned32):
    """Custom type pm200frs02CfgOptionsLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgOptionsLinePortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgOptionsLinePortn_Object = MibTableColumn
pm200frs02CfgOptionsLinePortn = _Pm200frs02CfgOptionsLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 2, 1, 14),
    _Pm200frs02CfgOptionsLinePortn_Type()
)
pm200frs02CfgOptionsLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgOptionsLinePortn.setStatus("current")
_Pm200frs02CfgXfpTable_Object = MibTable
pm200frs02CfgXfpTable = _Pm200frs02CfgXfpTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 3)
)
if mibBuilder.loadTexts:
    pm200frs02CfgXfpTable.setStatus("current")
_Pm200frs02CfgXfpEntry_Object = MibTableRow
pm200frs02CfgXfpEntry = _Pm200frs02CfgXfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 3, 1)
)
pm200frs02CfgXfpEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgXfpIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgXfpEntry.setStatus("current")


class _Pm200frs02CfgXfpIndex_Type(Integer32):
    """Custom type pm200frs02CfgXfpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgXfpIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgXfpIndex_Object = MibTableColumn
pm200frs02CfgXfpIndex = _Pm200frs02CfgXfpIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 3, 1, 1),
    _Pm200frs02CfgXfpIndex_Type()
)
pm200frs02CfgXfpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgXfpIndex.setStatus("current")


class _Pm200frs02CfgSystConfMsaLinePortn_Type(Unsigned32):
    """Custom type pm200frs02CfgSystConfMsaLinePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgSystConfMsaLinePortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgSystConfMsaLinePortn_Object = MibTableColumn
pm200frs02CfgSystConfMsaLinePortn = _Pm200frs02CfgSystConfMsaLinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 2, 3, 1, 3),
    _Pm200frs02CfgSystConfMsaLinePortn_Type()
)
pm200frs02CfgSystConfMsaLinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgSystConfMsaLinePortn.setStatus("current")
_Pm200frs02CfgLabels_ObjectIdentity = ObjectIdentity
pm200frs02CfgLabels = _Pm200frs02CfgLabels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3)
)
_Pm200frs02CfgLabelclientTable_Object = MibTable
pm200frs02CfgLabelclientTable = _Pm200frs02CfgLabelclientTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 1)
)
if mibBuilder.loadTexts:
    pm200frs02CfgLabelclientTable.setStatus("current")
_Pm200frs02CfgLabelclientEntry_Object = MibTableRow
pm200frs02CfgLabelclientEntry = _Pm200frs02CfgLabelclientEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 1, 1)
)
pm200frs02CfgLabelclientEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgLabelclientIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgLabelclientEntry.setStatus("current")


class _Pm200frs02CfgLabelclientIndex_Type(Integer32):
    """Custom type pm200frs02CfgLabelclientIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgLabelclientIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgLabelclientIndex_Object = MibTableColumn
pm200frs02CfgLabelclientIndex = _Pm200frs02CfgLabelclientIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 1, 1, 1),
    _Pm200frs02CfgLabelclientIndex_Type()
)
pm200frs02CfgLabelclientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgLabelclientIndex.setStatus("current")


class _Pm200frs02CfgLabelclientPortn_Type(DisplayString):
    """Custom type pm200frs02CfgLabelclientPortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm200frs02CfgLabelclientPortn_Type.__name__ = "DisplayString"
_Pm200frs02CfgLabelclientPortn_Object = MibTableColumn
pm200frs02CfgLabelclientPortn = _Pm200frs02CfgLabelclientPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 1, 1, 3),
    _Pm200frs02CfgLabelclientPortn_Type()
)
pm200frs02CfgLabelclientPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgLabelclientPortn.setStatus("current")
_Pm200frs02CfgLabellineTable_Object = MibTable
pm200frs02CfgLabellineTable = _Pm200frs02CfgLabellineTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 2)
)
if mibBuilder.loadTexts:
    pm200frs02CfgLabellineTable.setStatus("current")
_Pm200frs02CfgLabellineEntry_Object = MibTableRow
pm200frs02CfgLabellineEntry = _Pm200frs02CfgLabellineEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 2, 1)
)
pm200frs02CfgLabellineEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgLabellineIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgLabellineEntry.setStatus("current")


class _Pm200frs02CfgLabellineIndex_Type(Integer32):
    """Custom type pm200frs02CfgLabellineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgLabellineIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgLabellineIndex_Object = MibTableColumn
pm200frs02CfgLabellineIndex = _Pm200frs02CfgLabellineIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 2, 1, 1),
    _Pm200frs02CfgLabellineIndex_Type()
)
pm200frs02CfgLabellineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgLabellineIndex.setStatus("current")


class _Pm200frs02CfgLabellinePortn_Type(DisplayString):
    """Custom type pm200frs02CfgLabellinePortn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Pm200frs02CfgLabellinePortn_Type.__name__ = "DisplayString"
_Pm200frs02CfgLabellinePortn_Object = MibTableColumn
pm200frs02CfgLabellinePortn = _Pm200frs02CfgLabellinePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 3, 2, 1, 3),
    _Pm200frs02CfgLabellinePortn_Type()
)
pm200frs02CfgLabellinePortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgLabellinePortn.setStatus("current")
_Pm200frs02CfgStartuptlh_ObjectIdentity = ObjectIdentity
pm200frs02CfgStartuptlh = _Pm200frs02CfgStartuptlh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4)
)
_Pm200frs02CfgOtxtlhTable_Object = MibTable
pm200frs02CfgOtxtlhTable = _Pm200frs02CfgOtxtlhTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1)
)
if mibBuilder.loadTexts:
    pm200frs02CfgOtxtlhTable.setStatus("current")
_Pm200frs02CfgOtxtlhEntry_Object = MibTableRow
pm200frs02CfgOtxtlhEntry = _Pm200frs02CfgOtxtlhEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1)
)
pm200frs02CfgOtxtlhEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgOtxtlhIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgOtxtlhEntry.setStatus("current")


class _Pm200frs02CfgOtxtlhIndex_Type(Integer32):
    """Custom type pm200frs02CfgOtxtlhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgOtxtlhIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgOtxtlhIndex_Object = MibTableColumn
pm200frs02CfgOtxtlhIndex = _Pm200frs02CfgOtxtlhIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1, 1),
    _Pm200frs02CfgOtxtlhIndex_Type()
)
pm200frs02CfgOtxtlhIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgOtxtlhIndex.setStatus("current")


class _Pm200frs02CfgLinePwrLaserPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgLinePwrLaserPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgLinePwrLaserPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgLinePwrLaserPortn_Object = MibTableColumn
pm200frs02CfgLinePwrLaserPortn = _Pm200frs02CfgLinePwrLaserPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1, 6),
    _Pm200frs02CfgLinePwrLaserPortn_Type()
)
pm200frs02CfgLinePwrLaserPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgLinePwrLaserPortn.setStatus("current")


class _Pm200frs02CfgLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgLineFCurrentPortn_Object = MibTableColumn
pm200frs02CfgLineFCurrentPortn = _Pm200frs02CfgLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1, 7),
    _Pm200frs02CfgLineFCurrentPortn_Type()
)
pm200frs02CfgLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgLineFCurrentPortn.setStatus("current")


class _Pm200frs02CfgLineGridCurrentPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgLineGridCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgLineGridCurrentPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgLineGridCurrentPortn_Object = MibTableColumn
pm200frs02CfgLineGridCurrentPortn = _Pm200frs02CfgLineGridCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1, 8),
    _Pm200frs02CfgLineGridCurrentPortn_Type()
)
pm200frs02CfgLineGridCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgLineGridCurrentPortn.setStatus("current")


class _Pm200frs02CfgFPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgFPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgFPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgFPortn_Object = MibTableColumn
pm200frs02CfgFPortn = _Pm200frs02CfgFPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1, 9),
    _Pm200frs02CfgFPortn_Type()
)
pm200frs02CfgFPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgFPortn.setStatus("current")


class _Pm200frs02CfgRxLineFCurrentPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgRxLineFCurrentPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgRxLineFCurrentPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgRxLineFCurrentPortn_Object = MibTableColumn
pm200frs02CfgRxLineFCurrentPortn = _Pm200frs02CfgRxLineFCurrentPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 4, 1, 1, 10),
    _Pm200frs02CfgRxLineFCurrentPortn_Type()
)
pm200frs02CfgRxLineFCurrentPortn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgRxLineFCurrentPortn.setStatus("current")
_Pm200frs02CfgOther_ObjectIdentity = ObjectIdentity
pm200frs02CfgOther = _Pm200frs02CfgOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 5)
)
_Pm200frs02tablemoduleOther_ObjectIdentity = ObjectIdentity
pm200frs02tablemoduleOther = _Pm200frs02tablemoduleOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 5, 1)
)


class _Pm200frs02Cfgmode_Type(Unsigned32):
    """Custom type pm200frs02Cfgmode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02Cfgmode_Type.__name__ = "Unsigned32"
_Pm200frs02Cfgmode_Object = MibScalar
pm200frs02Cfgmode = _Pm200frs02Cfgmode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 5, 1, 2),
    _Pm200frs02Cfgmode_Type()
)
pm200frs02Cfgmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Cfgmode.setStatus("current")


class _Pm200frs02CfgfanLowSpeedThreshold_Type(Unsigned32):
    """Custom type pm200frs02CfgfanLowSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgfanLowSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm200frs02CfgfanLowSpeedThreshold_Object = MibScalar
pm200frs02CfgfanLowSpeedThreshold = _Pm200frs02CfgfanLowSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 5, 1, 3),
    _Pm200frs02CfgfanLowSpeedThreshold_Type()
)
pm200frs02CfgfanLowSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgfanLowSpeedThreshold.setStatus("current")


class _Pm200frs02CfgfanHighSpeedThreshold_Type(Unsigned32):
    """Custom type pm200frs02CfgfanHighSpeedThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgfanHighSpeedThreshold_Type.__name__ = "Unsigned32"
_Pm200frs02CfgfanHighSpeedThreshold_Object = MibScalar
pm200frs02CfgfanHighSpeedThreshold = _Pm200frs02CfgfanHighSpeedThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 5, 1, 4),
    _Pm200frs02CfgfanHighSpeedThreshold_Type()
)
pm200frs02CfgfanHighSpeedThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgfanHighSpeedThreshold.setStatus("current")


class _Pm200frs02CfgmoduleMode_Type(Unsigned32):
    """Custom type pm200frs02CfgmoduleMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgmoduleMode_Type.__name__ = "Unsigned32"
_Pm200frs02CfgmoduleMode_Object = MibScalar
pm200frs02CfgmoduleMode = _Pm200frs02CfgmoduleMode_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 5, 1, 5),
    _Pm200frs02CfgmoduleMode_Type()
)
pm200frs02CfgmoduleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgmoduleMode.setStatus("current")
_Pm200frs02CfgStartuptablefive_ObjectIdentity = ObjectIdentity
pm200frs02CfgStartuptablefive = _Pm200frs02CfgStartuptablefive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6)
)
_Pm200frs02CfgOtxtlhcapabilitiesTable_Object = MibTable
pm200frs02CfgOtxtlhcapabilitiesTable = _Pm200frs02CfgOtxtlhcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1)
)
if mibBuilder.loadTexts:
    pm200frs02CfgOtxtlhcapabilitiesTable.setStatus("current")
_Pm200frs02CfgOtxtlhcapabilitiesEntry_Object = MibTableRow
pm200frs02CfgOtxtlhcapabilitiesEntry = _Pm200frs02CfgOtxtlhcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1)
)
pm200frs02CfgOtxtlhcapabilitiesEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02CfgOtxtlhcapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02CfgOtxtlhcapabilitiesEntry.setStatus("current")


class _Pm200frs02CfgOtxtlhcapabilitiesIndex_Type(Integer32):
    """Custom type pm200frs02CfgOtxtlhcapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02CfgOtxtlhcapabilitiesIndex_Type.__name__ = "Integer32"
_Pm200frs02CfgOtxtlhcapabilitiesIndex_Object = MibTableColumn
pm200frs02CfgOtxtlhcapabilitiesIndex = _Pm200frs02CfgOtxtlhcapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1, 1),
    _Pm200frs02CfgOtxtlhcapabilitiesIndex_Type()
)
pm200frs02CfgOtxtlhcapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgOtxtlhcapabilitiesIndex.setStatus("current")


class _Pm200frs02CfgComponentTypePortn_Type(Unsigned32):
    """Custom type pm200frs02CfgComponentTypePortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgComponentTypePortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgComponentTypePortn_Object = MibTableColumn
pm200frs02CfgComponentTypePortn = _Pm200frs02CfgComponentTypePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1, 3),
    _Pm200frs02CfgComponentTypePortn_Type()
)
pm200frs02CfgComponentTypePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgComponentTypePortn.setStatus("current")


class _Pm200frs02CfgMiscellaneousPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgMiscellaneousPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgMiscellaneousPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgMiscellaneousPortn_Object = MibTableColumn
pm200frs02CfgMiscellaneousPortn = _Pm200frs02CfgMiscellaneousPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1, 4),
    _Pm200frs02CfgMiscellaneousPortn_Type()
)
pm200frs02CfgMiscellaneousPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgMiscellaneousPortn.setStatus("current")


class _Pm200frs02CfgFirstChannelPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgFirstChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgFirstChannelPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgFirstChannelPortn_Object = MibTableColumn
pm200frs02CfgFirstChannelPortn = _Pm200frs02CfgFirstChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1, 5),
    _Pm200frs02CfgFirstChannelPortn_Type()
)
pm200frs02CfgFirstChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgFirstChannelPortn.setStatus("current")


class _Pm200frs02CfgLastChannelPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgLastChannelPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgLastChannelPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgLastChannelPortn_Object = MibTableColumn
pm200frs02CfgLastChannelPortn = _Pm200frs02CfgLastChannelPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1, 6),
    _Pm200frs02CfgLastChannelPortn_Type()
)
pm200frs02CfgLastChannelPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgLastChannelPortn.setStatus("current")


class _Pm200frs02CfgGridPortn_Type(Unsigned32):
    """Custom type pm200frs02CfgGridPortn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Pm200frs02CfgGridPortn_Type.__name__ = "Unsigned32"
_Pm200frs02CfgGridPortn_Object = MibTableColumn
pm200frs02CfgGridPortn = _Pm200frs02CfgGridPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 6, 1, 1, 7),
    _Pm200frs02CfgGridPortn_Type()
)
pm200frs02CfgGridPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02CfgGridPortn.setStatus("current")
_Pm200frs02CfgWriteConfiguration_Type = EkiOnOff
_Pm200frs02CfgWriteConfiguration_Object = MibScalar
pm200frs02CfgWriteConfiguration = _Pm200frs02CfgWriteConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 9, 257),
    _Pm200frs02CfgWriteConfiguration_Type()
)
pm200frs02CfgWriteConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02CfgWriteConfiguration.setStatus("current")
_Pm200frs02traps_ObjectIdentity = ObjectIdentity
pm200frs02traps = _Pm200frs02traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10)
)


class _Pm200frs02trapPortNumber_Type(Integer32):
    """Custom type pm200frs02trapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm200frs02trapPortNumber_Type.__name__ = "Integer32"
_Pm200frs02trapPortNumber_Object = MibScalar
pm200frs02trapPortNumber = _Pm200frs02trapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 2),
    _Pm200frs02trapPortNumber_Type()
)
pm200frs02trapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02trapPortNumber.setStatus("current")


class _Pm200frs02trapLineNumber_Type(Integer32):
    """Custom type pm200frs02trapLineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm200frs02trapLineNumber_Type.__name__ = "Integer32"
_Pm200frs02trapLineNumber_Object = MibScalar
pm200frs02trapLineNumber = _Pm200frs02trapLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 3),
    _Pm200frs02trapLineNumber_Type()
)
pm200frs02trapLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02trapLineNumber.setStatus("current")


class _Pm200frs02trapBoardNumber_Type(Integer32):
    """Custom type pm200frs02trapBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Pm200frs02trapBoardNumber_Type.__name__ = "Integer32"
_Pm200frs02trapBoardNumber_Object = MibScalar
pm200frs02trapBoardNumber = _Pm200frs02trapBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 4),
    _Pm200frs02trapBoardNumber_Type()
)
pm200frs02trapBoardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02trapBoardNumber.setStatus("current")
_Pm200frs02Monitoring_ObjectIdentity = ObjectIdentity
pm200frs02Monitoring = _Pm200frs02Monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11)
)
_Pm200frs02MonOther_ObjectIdentity = ObjectIdentity
pm200frs02MonOther = _Pm200frs02MonOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 1)
)
_Pm200frs02MonRmon_ObjectIdentity = ObjectIdentity
pm200frs02MonRmon = _Pm200frs02MonRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 1, 3)
)
_Pm200frs02MonClient_ObjectIdentity = ObjectIdentity
pm200frs02MonClient = _Pm200frs02MonClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2)
)
_Pm200frs02MonClientRmonCounter_ObjectIdentity = ObjectIdentity
pm200frs02MonClientRmonCounter = _Pm200frs02MonClientRmonCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4)
)
_Pm200frs02MonupRmonBytesCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonBytesCounterClientInputTable = _Pm200frs02MonupRmonBytesCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 16)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBytesCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonBytesCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonBytesCounterClientInputEntry = _Pm200frs02MonupRmonBytesCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 16, 1)
)
pm200frs02MonupRmonBytesCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonBytesCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBytesCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonBytesCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonBytesCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonBytesCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonBytesCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonBytesCounterClientInputIndex = _Pm200frs02MonupRmonBytesCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 16, 1, 1),
    _Pm200frs02MonupRmonBytesCounterClientInputIndex_Type()
)
pm200frs02MonupRmonBytesCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBytesCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonBytesCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonBytesCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonBytesCounterClientInputValuePortn = _Pm200frs02MonupRmonBytesCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 16, 1, 2),
    _Pm200frs02MonupRmonBytesCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonBytesCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBytesCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonBytesCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonBytesCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonBytesCounterClientInputErrorPortn = _Pm200frs02MonupRmonBytesCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 16, 1, 3),
    _Pm200frs02MonupRmonBytesCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonBytesCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBytesCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonBytesCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonBytesCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonBytesCounterClientInputOverloadPortn = _Pm200frs02MonupRmonBytesCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 16, 1, 4),
    _Pm200frs02MonupRmonBytesCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonBytesCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBytesCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonCrcErrorsCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonCrcErrorsCounterClientInputTable = _Pm200frs02MonupRmonCrcErrorsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 48)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonCrcErrorsCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonCrcErrorsCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonCrcErrorsCounterClientInputEntry = _Pm200frs02MonupRmonCrcErrorsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 48, 1)
)
pm200frs02MonupRmonCrcErrorsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonCrcErrorsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonCrcErrorsCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonCrcErrorsCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonCrcErrorsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonCrcErrorsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonCrcErrorsCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonCrcErrorsCounterClientInputIndex = _Pm200frs02MonupRmonCrcErrorsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 48, 1, 1),
    _Pm200frs02MonupRmonCrcErrorsCounterClientInputIndex_Type()
)
pm200frs02MonupRmonCrcErrorsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonCrcErrorsCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn = _Pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 48, 1, 2),
    _Pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn = _Pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 48, 1, 3),
    _Pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn = _Pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 48, 1, 4),
    _Pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonPacketsCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonPacketsCounterClientInputTable = _Pm200frs02MonupRmonPacketsCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 80)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPacketsCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonPacketsCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonPacketsCounterClientInputEntry = _Pm200frs02MonupRmonPacketsCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 80, 1)
)
pm200frs02MonupRmonPacketsCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonPacketsCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPacketsCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonPacketsCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonPacketsCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonPacketsCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonPacketsCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonPacketsCounterClientInputIndex = _Pm200frs02MonupRmonPacketsCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 80, 1, 1),
    _Pm200frs02MonupRmonPacketsCounterClientInputIndex_Type()
)
pm200frs02MonupRmonPacketsCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPacketsCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonPacketsCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonPacketsCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonPacketsCounterClientInputValuePortn = _Pm200frs02MonupRmonPacketsCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 80, 1, 2),
    _Pm200frs02MonupRmonPacketsCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonPacketsCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPacketsCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonPacketsCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonPacketsCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonPacketsCounterClientInputErrorPortn = _Pm200frs02MonupRmonPacketsCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 80, 1, 3),
    _Pm200frs02MonupRmonPacketsCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonPacketsCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPacketsCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn = _Pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 80, 1, 4),
    _Pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonBroadcastCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonBroadcastCounterClientInputTable = _Pm200frs02MonupRmonBroadcastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 112)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBroadcastCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonBroadcastCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonBroadcastCounterClientInputEntry = _Pm200frs02MonupRmonBroadcastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 112, 1)
)
pm200frs02MonupRmonBroadcastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonBroadcastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBroadcastCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonBroadcastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonBroadcastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonBroadcastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonBroadcastCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonBroadcastCounterClientInputIndex = _Pm200frs02MonupRmonBroadcastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 112, 1, 1),
    _Pm200frs02MonupRmonBroadcastCounterClientInputIndex_Type()
)
pm200frs02MonupRmonBroadcastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBroadcastCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonBroadcastCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonBroadcastCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonBroadcastCounterClientInputValuePortn = _Pm200frs02MonupRmonBroadcastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 112, 1, 2),
    _Pm200frs02MonupRmonBroadcastCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonBroadcastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBroadcastCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn = _Pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 112, 1, 3),
    _Pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn = _Pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 112, 1, 4),
    _Pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonMulticastCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonMulticastCounterClientInputTable = _Pm200frs02MonupRmonMulticastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 144)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonMulticastCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonMulticastCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonMulticastCounterClientInputEntry = _Pm200frs02MonupRmonMulticastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 144, 1)
)
pm200frs02MonupRmonMulticastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonMulticastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonMulticastCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonMulticastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonMulticastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonMulticastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonMulticastCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonMulticastCounterClientInputIndex = _Pm200frs02MonupRmonMulticastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 144, 1, 1),
    _Pm200frs02MonupRmonMulticastCounterClientInputIndex_Type()
)
pm200frs02MonupRmonMulticastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonMulticastCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonMulticastCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonMulticastCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonMulticastCounterClientInputValuePortn = _Pm200frs02MonupRmonMulticastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 144, 1, 2),
    _Pm200frs02MonupRmonMulticastCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonMulticastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonMulticastCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonMulticastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonMulticastCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonMulticastCounterClientInputErrorPortn = _Pm200frs02MonupRmonMulticastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 144, 1, 3),
    _Pm200frs02MonupRmonMulticastCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonMulticastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonMulticastCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn = _Pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 144, 1, 4),
    _Pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonPauseFrameCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonPauseFrameCounterClientInputTable = _Pm200frs02MonupRmonPauseFrameCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 176)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPauseFrameCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonPauseFrameCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonPauseFrameCounterClientInputEntry = _Pm200frs02MonupRmonPauseFrameCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 176, 1)
)
pm200frs02MonupRmonPauseFrameCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonPauseFrameCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPauseFrameCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonPauseFrameCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonPauseFrameCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonPauseFrameCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonPauseFrameCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonPauseFrameCounterClientInputIndex = _Pm200frs02MonupRmonPauseFrameCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 176, 1, 1),
    _Pm200frs02MonupRmonPauseFrameCounterClientInputIndex_Type()
)
pm200frs02MonupRmonPauseFrameCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPauseFrameCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn = _Pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 176, 1, 2),
    _Pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn = _Pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 176, 1, 3),
    _Pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn = _Pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 176, 1, 4),
    _Pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonUnicastCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonUnicastCounterClientInputTable = _Pm200frs02MonupRmonUnicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 304)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonUnicastCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonUnicastCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonUnicastCounterClientInputEntry = _Pm200frs02MonupRmonUnicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 304, 1)
)
pm200frs02MonupRmonUnicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonUnicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonUnicastCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonUnicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonUnicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonUnicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonUnicastCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonUnicastCounterClientInputIndex = _Pm200frs02MonupRmonUnicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 304, 1, 1),
    _Pm200frs02MonupRmonUnicastCounterClientInputIndex_Type()
)
pm200frs02MonupRmonUnicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonUnicastCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonUnicastCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonUnicastCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonUnicastCounterClientInputValuePortn = _Pm200frs02MonupRmonUnicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 304, 1, 2),
    _Pm200frs02MonupRmonUnicastCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonUnicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonUnicastCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonUnicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonUnicastCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonUnicastCounterClientInputErrorPortn = _Pm200frs02MonupRmonUnicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 304, 1, 3),
    _Pm200frs02MonupRmonUnicastCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonUnicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonUnicastCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn = _Pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 304, 1, 4),
    _Pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MonupRmonNonunicastCounterClientInputTable_Object = MibTable
pm200frs02MonupRmonNonunicastCounterClientInputTable = _Pm200frs02MonupRmonNonunicastCounterClientInputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 336)
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonNonunicastCounterClientInputTable.setStatus("current")
_Pm200frs02MonupRmonNonunicastCounterClientInputEntry_Object = MibTableRow
pm200frs02MonupRmonNonunicastCounterClientInputEntry = _Pm200frs02MonupRmonNonunicastCounterClientInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 336, 1)
)
pm200frs02MonupRmonNonunicastCounterClientInputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MonupRmonNonunicastCounterClientInputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MonupRmonNonunicastCounterClientInputEntry.setStatus("current")


class _Pm200frs02MonupRmonNonunicastCounterClientInputIndex_Type(Integer32):
    """Custom type pm200frs02MonupRmonNonunicastCounterClientInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MonupRmonNonunicastCounterClientInputIndex_Type.__name__ = "Integer32"
_Pm200frs02MonupRmonNonunicastCounterClientInputIndex_Object = MibTableColumn
pm200frs02MonupRmonNonunicastCounterClientInputIndex = _Pm200frs02MonupRmonNonunicastCounterClientInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 336, 1, 1),
    _Pm200frs02MonupRmonNonunicastCounterClientInputIndex_Type()
)
pm200frs02MonupRmonNonunicastCounterClientInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonNonunicastCounterClientInputIndex.setStatus("current")
_Pm200frs02MonupRmonNonunicastCounterClientInputValuePortn_Type = Counter64
_Pm200frs02MonupRmonNonunicastCounterClientInputValuePortn_Object = MibTableColumn
pm200frs02MonupRmonNonunicastCounterClientInputValuePortn = _Pm200frs02MonupRmonNonunicastCounterClientInputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 336, 1, 2),
    _Pm200frs02MonupRmonNonunicastCounterClientInputValuePortn_Type()
)
pm200frs02MonupRmonNonunicastCounterClientInputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonNonunicastCounterClientInputValuePortn.setStatus("current")
_Pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn_Type = EkiOnOff
_Pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn_Object = MibTableColumn
pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn = _Pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 336, 1, 3),
    _Pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn_Type()
)
pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn.setStatus("current")
_Pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn_Type = EkiOnOff
_Pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn_Object = MibTableColumn
pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn = _Pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 336, 1, 4),
    _Pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn_Type()
)
pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonBytesCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonBytesCounterClientOutputTable = _Pm200frs02MondownRmonBytesCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 400)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBytesCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonBytesCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonBytesCounterClientOutputEntry = _Pm200frs02MondownRmonBytesCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 400, 1)
)
pm200frs02MondownRmonBytesCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonBytesCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBytesCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonBytesCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonBytesCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonBytesCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonBytesCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonBytesCounterClientOutputIndex = _Pm200frs02MondownRmonBytesCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 400, 1, 1),
    _Pm200frs02MondownRmonBytesCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonBytesCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBytesCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonBytesCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonBytesCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonBytesCounterClientOutputValuePortn = _Pm200frs02MondownRmonBytesCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 400, 1, 2),
    _Pm200frs02MondownRmonBytesCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonBytesCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBytesCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonBytesCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonBytesCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonBytesCounterClientOutputErrorPortn = _Pm200frs02MondownRmonBytesCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 400, 1, 3),
    _Pm200frs02MondownRmonBytesCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonBytesCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBytesCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 400, 1, 4),
    _Pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonCrcErrorsCounterClientOutputTable = _Pm200frs02MondownRmonCrcErrorsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 432)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonCrcErrorsCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry = _Pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 432, 1)
)
pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex = _Pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 432, 1, 1),
    _Pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn = _Pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 432, 1, 2),
    _Pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn = _Pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 432, 1, 3),
    _Pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 432, 1, 4),
    _Pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonPacketsCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonPacketsCounterClientOutputTable = _Pm200frs02MondownRmonPacketsCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 464)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPacketsCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonPacketsCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonPacketsCounterClientOutputEntry = _Pm200frs02MondownRmonPacketsCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 464, 1)
)
pm200frs02MondownRmonPacketsCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonPacketsCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPacketsCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonPacketsCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonPacketsCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonPacketsCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonPacketsCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonPacketsCounterClientOutputIndex = _Pm200frs02MondownRmonPacketsCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 464, 1, 1),
    _Pm200frs02MondownRmonPacketsCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonPacketsCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPacketsCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonPacketsCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonPacketsCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonPacketsCounterClientOutputValuePortn = _Pm200frs02MondownRmonPacketsCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 464, 1, 2),
    _Pm200frs02MondownRmonPacketsCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonPacketsCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPacketsCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn = _Pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 464, 1, 3),
    _Pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 464, 1, 4),
    _Pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonBroadcastCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonBroadcastCounterClientOutputTable = _Pm200frs02MondownRmonBroadcastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 496)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBroadcastCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonBroadcastCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonBroadcastCounterClientOutputEntry = _Pm200frs02MondownRmonBroadcastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 496, 1)
)
pm200frs02MondownRmonBroadcastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonBroadcastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBroadcastCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonBroadcastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonBroadcastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonBroadcastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonBroadcastCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonBroadcastCounterClientOutputIndex = _Pm200frs02MondownRmonBroadcastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 496, 1, 1),
    _Pm200frs02MondownRmonBroadcastCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonBroadcastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBroadcastCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn = _Pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 496, 1, 2),
    _Pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn = _Pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 496, 1, 3),
    _Pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 496, 1, 4),
    _Pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonMulticastCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonMulticastCounterClientOutputTable = _Pm200frs02MondownRmonMulticastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 528)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonMulticastCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonMulticastCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonMulticastCounterClientOutputEntry = _Pm200frs02MondownRmonMulticastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 528, 1)
)
pm200frs02MondownRmonMulticastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonMulticastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonMulticastCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonMulticastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonMulticastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonMulticastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonMulticastCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonMulticastCounterClientOutputIndex = _Pm200frs02MondownRmonMulticastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 528, 1, 1),
    _Pm200frs02MondownRmonMulticastCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonMulticastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonMulticastCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonMulticastCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonMulticastCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonMulticastCounterClientOutputValuePortn = _Pm200frs02MondownRmonMulticastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 528, 1, 2),
    _Pm200frs02MondownRmonMulticastCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonMulticastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonMulticastCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn = _Pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 528, 1, 3),
    _Pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 528, 1, 4),
    _Pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonPauseFrameCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonPauseFrameCounterClientOutputTable = _Pm200frs02MondownRmonPauseFrameCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 560)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPauseFrameCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonPauseFrameCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonPauseFrameCounterClientOutputEntry = _Pm200frs02MondownRmonPauseFrameCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 560, 1)
)
pm200frs02MondownRmonPauseFrameCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonPauseFrameCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPauseFrameCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonPauseFrameCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonPauseFrameCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonPauseFrameCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonPauseFrameCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonPauseFrameCounterClientOutputIndex = _Pm200frs02MondownRmonPauseFrameCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 560, 1, 1),
    _Pm200frs02MondownRmonPauseFrameCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonPauseFrameCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPauseFrameCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn = _Pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 560, 1, 2),
    _Pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn = _Pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 560, 1, 3),
    _Pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 560, 1, 4),
    _Pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonUnicastCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonUnicastCounterClientOutputTable = _Pm200frs02MondownRmonUnicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 688)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonUnicastCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonUnicastCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonUnicastCounterClientOutputEntry = _Pm200frs02MondownRmonUnicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 688, 1)
)
pm200frs02MondownRmonUnicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonUnicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonUnicastCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonUnicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonUnicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonUnicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonUnicastCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonUnicastCounterClientOutputIndex = _Pm200frs02MondownRmonUnicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 688, 1, 1),
    _Pm200frs02MondownRmonUnicastCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonUnicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonUnicastCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonUnicastCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonUnicastCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonUnicastCounterClientOutputValuePortn = _Pm200frs02MondownRmonUnicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 688, 1, 2),
    _Pm200frs02MondownRmonUnicastCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonUnicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonUnicastCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn = _Pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 688, 1, 3),
    _Pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 688, 1, 4),
    _Pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MondownRmonNonunicastCounterClientOutputTable_Object = MibTable
pm200frs02MondownRmonNonunicastCounterClientOutputTable = _Pm200frs02MondownRmonNonunicastCounterClientOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 720)
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonNonunicastCounterClientOutputTable.setStatus("current")
_Pm200frs02MondownRmonNonunicastCounterClientOutputEntry_Object = MibTableRow
pm200frs02MondownRmonNonunicastCounterClientOutputEntry = _Pm200frs02MondownRmonNonunicastCounterClientOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 720, 1)
)
pm200frs02MondownRmonNonunicastCounterClientOutputEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02MondownRmonNonunicastCounterClientOutputIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02MondownRmonNonunicastCounterClientOutputEntry.setStatus("current")


class _Pm200frs02MondownRmonNonunicastCounterClientOutputIndex_Type(Integer32):
    """Custom type pm200frs02MondownRmonNonunicastCounterClientOutputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02MondownRmonNonunicastCounterClientOutputIndex_Type.__name__ = "Integer32"
_Pm200frs02MondownRmonNonunicastCounterClientOutputIndex_Object = MibTableColumn
pm200frs02MondownRmonNonunicastCounterClientOutputIndex = _Pm200frs02MondownRmonNonunicastCounterClientOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 720, 1, 1),
    _Pm200frs02MondownRmonNonunicastCounterClientOutputIndex_Type()
)
pm200frs02MondownRmonNonunicastCounterClientOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonNonunicastCounterClientOutputIndex.setStatus("current")
_Pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn_Type = Counter64
_Pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn_Object = MibTableColumn
pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn = _Pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 720, 1, 2),
    _Pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn_Type()
)
pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn.setStatus("current")
_Pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn_Type = EkiOnOff
_Pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn_Object = MibTableColumn
pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn = _Pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 720, 1, 3),
    _Pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn_Type()
)
pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn.setStatus("current")
_Pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn_Type = EkiOnOff
_Pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn_Object = MibTableColumn
pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn = _Pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 2, 4, 720, 1, 4),
    _Pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn_Type()
)
pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn.setStatus("current")
_Pm200frs02MonPerfOther_ObjectIdentity = ObjectIdentity
pm200frs02MonPerfOther = _Pm200frs02MonPerfOther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5)
)
_Pm200frs02MonPerfSync_ObjectIdentity = ObjectIdentity
pm200frs02MonPerfSync = _Pm200frs02MonPerfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 1)
)
_Pm200frs02PerfEnable_Type = EkiOnOff
_Pm200frs02PerfEnable_Object = MibScalar
pm200frs02PerfEnable = _Pm200frs02PerfEnable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 1, 257),
    _Pm200frs02PerfEnable_Type()
)
pm200frs02PerfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02PerfEnable.setStatus("current")
_Pm200frs02Perf15minSync_Type = EkiOnOff
_Pm200frs02Perf15minSync_Object = MibScalar
pm200frs02Perf15minSync = _Pm200frs02Perf15minSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 1, 259),
    _Pm200frs02Perf15minSync_Type()
)
pm200frs02Perf15minSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Perf15minSync.setStatus("current")
_Pm200frs02Perf24hSync_Type = EkiOnOff
_Pm200frs02Perf24hSync_Object = MibScalar
pm200frs02Perf24hSync = _Pm200frs02Perf24hSync_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 1, 260),
    _Pm200frs02Perf24hSync_Type()
)
pm200frs02Perf24hSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Perf24hSync.setStatus("current")
_Pm200frs02MonPerfTimeStamp_ObjectIdentity = ObjectIdentity
pm200frs02MonPerfTimeStamp = _Pm200frs02MonPerfTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2)
)
_Pm200frs02Perf15MinShort_Type = EkiOnOff
_Pm200frs02Perf15MinShort_Object = MibScalar
pm200frs02Perf15MinShort = _Pm200frs02Perf15MinShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2, 1),
    _Pm200frs02Perf15MinShort_Type()
)
pm200frs02Perf15MinShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Perf15MinShort.setStatus("current")
_Pm200frs02Perf15MinLong_Type = EkiOnOff
_Pm200frs02Perf15MinLong_Object = MibScalar
pm200frs02Perf15MinLong = _Pm200frs02Perf15MinLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2, 2),
    _Pm200frs02Perf15MinLong_Type()
)
pm200frs02Perf15MinLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Perf15MinLong.setStatus("current")
_Pm200frs02Perf24HoursShort_Type = Counter32
_Pm200frs02Perf24HoursShort_Object = MibScalar
pm200frs02Perf24HoursShort = _Pm200frs02Perf24HoursShort_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2, 5),
    _Pm200frs02Perf24HoursShort_Type()
)
pm200frs02Perf24HoursShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Perf24HoursShort.setStatus("current")
_Pm200frs02Perf24HoursLong_Type = Counter32
_Pm200frs02Perf24HoursLong_Object = MibScalar
pm200frs02Perf24HoursLong = _Pm200frs02Perf24HoursLong_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2, 6),
    _Pm200frs02Perf24HoursLong_Type()
)
pm200frs02Perf24HoursLong.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02Perf24HoursLong.setStatus("current")
_Pm200frs02PerfCurrent15MinElapsedTime_Type = Counter32
_Pm200frs02PerfCurrent15MinElapsedTime_Object = MibScalar
pm200frs02PerfCurrent15MinElapsedTime = _Pm200frs02PerfCurrent15MinElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2, 7),
    _Pm200frs02PerfCurrent15MinElapsedTime_Type()
)
pm200frs02PerfCurrent15MinElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02PerfCurrent15MinElapsedTime.setStatus("current")
_Pm200frs02PerfCurrent24HoursElapsedTime_Type = Counter32
_Pm200frs02PerfCurrent24HoursElapsedTime_Object = MibScalar
pm200frs02PerfCurrent24HoursElapsedTime = _Pm200frs02PerfCurrent24HoursElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 5, 2, 8),
    _Pm200frs02PerfCurrent24HoursElapsedTime_Type()
)
pm200frs02PerfCurrent24HoursElapsedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pm200frs02PerfCurrent24HoursElapsedTime.setStatus("current")
_Pm200frs02MonPerfClient_ObjectIdentity = ObjectIdentity
pm200frs02MonPerfClient = _Pm200frs02MonPerfClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6)
)
_Pm200frs02PerfTelecomInputClientCurrent15StatTable_Object = MibTable
pm200frs02PerfTelecomInputClientCurrent15StatTable = _Pm200frs02PerfTelecomInputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatTable.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatEntry_Object = MibTableRow
pm200frs02PerfTelecomInputClientCurrent15StatEntry = _Pm200frs02PerfTelecomInputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1)
)
pm200frs02PerfTelecomInputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomInputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomInputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomInputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomInputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomInputClientCurrent15StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatIndex = _Pm200frs02PerfTelecomInputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 1),
    _Pm200frs02PerfTelecomInputClientCurrent15StatIndex_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatIndex.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn = _Pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 2),
    _Pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn = _Pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 3),
    _Pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn = _Pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 4),
    _Pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn = _Pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 5),
    _Pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn = _Pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 6),
    _Pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn = _Pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 7),
    _Pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn = _Pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 8),
    _Pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn = _Pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 9),
    _Pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn = _Pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 10),
    _Pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn = _Pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 16, 1, 11),
    _Pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Table = _Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry = _Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1)
)
pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index = _Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 1),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 2),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 3),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 4),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 5),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 6),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 7),
    _Pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 8),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 9),
    _Pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 10),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1 = _Pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 48, 1, 11),
    _Pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatTable_Object = MibTable
pm200frs02PerfTelecomInputClientCurrent24StatTable = _Pm200frs02PerfTelecomInputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatTable.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatEntry_Object = MibTableRow
pm200frs02PerfTelecomInputClientCurrent24StatEntry = _Pm200frs02PerfTelecomInputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1)
)
pm200frs02PerfTelecomInputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomInputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomInputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomInputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomInputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomInputClientCurrent24StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatIndex = _Pm200frs02PerfTelecomInputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 1),
    _Pm200frs02PerfTelecomInputClientCurrent24StatIndex_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatIndex.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn = _Pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 2),
    _Pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn = _Pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 3),
    _Pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn = _Pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 4),
    _Pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn = _Pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 5),
    _Pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn = _Pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 6),
    _Pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn = _Pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 7),
    _Pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn = _Pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 8),
    _Pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn = _Pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 9),
    _Pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn = _Pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 10),
    _Pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn = _Pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 80, 1, 11),
    _Pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn_Type()
)
pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Table = _Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry = _Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1)
)
pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index = _Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 1),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 2),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 3),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 4),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 5),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 6),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 7),
    _Pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 8),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 9),
    _Pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 10),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1 = _Pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 112, 1, 11),
    _Pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1_Type()
)
pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatTable_Object = MibTable
pm200frs02PerfTelecomOutputClientCurrent15StatTable = _Pm200frs02PerfTelecomOutputClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatTable.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatEntry_Object = MibTableRow
pm200frs02PerfTelecomOutputClientCurrent15StatEntry = _Pm200frs02PerfTelecomOutputClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1)
)
pm200frs02PerfTelecomOutputClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomOutputClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomOutputClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomOutputClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomOutputClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomOutputClientCurrent15StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatIndex = _Pm200frs02PerfTelecomOutputClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 1),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatIndex_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatIndex.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 2),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 3),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 4),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 5),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 6),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 7),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 8),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 9),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 10),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 144, 1, 11),
    _Pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Table = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1)
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 1),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 2),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 3),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 4),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 5),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 6),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 7),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 8),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 9),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 10),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1 = _Pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 176, 1, 11),
    _Pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatTable_Object = MibTable
pm200frs02PerfTelecomOutputClientCurrent24StatTable = _Pm200frs02PerfTelecomOutputClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatTable.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatEntry_Object = MibTableRow
pm200frs02PerfTelecomOutputClientCurrent24StatEntry = _Pm200frs02PerfTelecomOutputClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1)
)
pm200frs02PerfTelecomOutputClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomOutputClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomOutputClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomOutputClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomOutputClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomOutputClientCurrent24StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatIndex = _Pm200frs02PerfTelecomOutputClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 1),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatIndex_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatIndex.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 2),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 3),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 4),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 5),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 6),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 7),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 8),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 9),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 10),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn = _Pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 208, 1, 11),
    _Pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn_Type()
)
pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Table = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1)
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 1),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 2),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 3),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 4),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 5),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 6),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 7),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 8),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 9),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 10),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1.setStatus("current")
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1 = _Pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 240, 1, 11),
    _Pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1_Type()
)
pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1.setStatus("current")
_Pm200frs02PerfDatacomClientCurrent15StatTable_Object = MibTable
pm200frs02PerfDatacomClientCurrent15StatTable = _Pm200frs02PerfDatacomClientCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848)
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientCurrent15StatTable.setStatus("current")
_Pm200frs02PerfDatacomClientCurrent15StatEntry_Object = MibTableRow
pm200frs02PerfDatacomClientCurrent15StatEntry = _Pm200frs02PerfDatacomClientCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1)
)
pm200frs02PerfDatacomClientCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfDatacomClientCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientCurrent15StatEntry.setStatus("current")


class _Pm200frs02PerfDatacomClientCurrent15StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfDatacomClientCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfDatacomClientCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfDatacomClientCurrent15StatIndex_Object = MibTableColumn
pm200frs02PerfDatacomClientCurrent15StatIndex = _Pm200frs02PerfDatacomClientCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 1),
    _Pm200frs02PerfDatacomClientCurrent15StatIndex_Type()
)
pm200frs02PerfDatacomClientCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientCurrent15StatIndex.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn = _Pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 4),
    _Pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn = _Pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 5),
    _Pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn = _Pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 6),
    _Pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn = _Pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 7),
    _Pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn = _Pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 28),
    _Pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn = _Pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 29),
    _Pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn = _Pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 30),
    _Pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn = _Pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 848, 1, 31),
    _Pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn.setStatus("current")
_Pm200frs02PerfDatacomClientPast15StatHistoryPort1Table_Object = MibTable
pm200frs02PerfDatacomClientPast15StatHistoryPort1Table = _Pm200frs02PerfDatacomClientPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880)
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientPast15StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry = _Pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1)
)
pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfDatacomClientPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfDatacomClientPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfDatacomClientPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfDatacomClientPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfDatacomClientPast15StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfDatacomClientPast15StatHistoryPort1Index = _Pm200frs02PerfDatacomClientPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 1),
    _Pm200frs02PerfDatacomClientPast15StatHistoryPort1Index_Type()
)
pm200frs02PerfDatacomClientPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientPast15StatHistoryPort1Index.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1 = _Pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 4),
    _Pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatInCrcCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast15StatInCrcCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatInCrcCountPort1 = _Pm200frs02perfdatacomclientPast15StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 5),
    _Pm200frs02perfdatacomclientPast15StatInCrcCountPort1_Type()
)
pm200frs02perfdatacomclientPast15StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatInCrcCountPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1 = _Pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 6),
    _Pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatInPacketCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast15StatInPacketCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatInPacketCountPort1 = _Pm200frs02perfdatacomclientPast15StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 7),
    _Pm200frs02perfdatacomclientPast15StatInPacketCountPort1_Type()
)
pm200frs02perfdatacomclientPast15StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatInPacketCountPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1 = _Pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 28),
    _Pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatOutCrcCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast15StatOutCrcCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatOutCrcCountPort1 = _Pm200frs02perfdatacomclientPast15StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 29),
    _Pm200frs02perfdatacomclientPast15StatOutCrcCountPort1_Type()
)
pm200frs02perfdatacomclientPast15StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatOutCrcCountPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1 = _Pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 30),
    _Pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast15StatOutPacketCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast15StatOutPacketCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast15StatOutPacketCountPort1 = _Pm200frs02perfdatacomclientPast15StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 880, 1, 31),
    _Pm200frs02perfdatacomclientPast15StatOutPacketCountPort1_Type()
)
pm200frs02perfdatacomclientPast15StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast15StatOutPacketCountPort1.setStatus("current")
_Pm200frs02PerfDatacomClientCurrent24StatTable_Object = MibTable
pm200frs02PerfDatacomClientCurrent24StatTable = _Pm200frs02PerfDatacomClientCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912)
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientCurrent24StatTable.setStatus("current")
_Pm200frs02PerfDatacomClientCurrent24StatEntry_Object = MibTableRow
pm200frs02PerfDatacomClientCurrent24StatEntry = _Pm200frs02PerfDatacomClientCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1)
)
pm200frs02PerfDatacomClientCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfDatacomClientCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientCurrent24StatEntry.setStatus("current")


class _Pm200frs02PerfDatacomClientCurrent24StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfDatacomClientCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfDatacomClientCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfDatacomClientCurrent24StatIndex_Object = MibTableColumn
pm200frs02PerfDatacomClientCurrent24StatIndex = _Pm200frs02PerfDatacomClientCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 1),
    _Pm200frs02PerfDatacomClientCurrent24StatIndex_Type()
)
pm200frs02PerfDatacomClientCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientCurrent24StatIndex.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn = _Pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 4),
    _Pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn = _Pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 5),
    _Pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn = _Pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 6),
    _Pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn = _Pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 7),
    _Pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn = _Pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 28),
    _Pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn = _Pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 29),
    _Pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type = EkiOnOff
_Pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn = _Pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 30),
    _Pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn.setStatus("current")
_Pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn_Type = Counter64
_Pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn_Object = MibTableColumn
pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn = _Pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 912, 1, 31),
    _Pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn_Type()
)
pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn.setStatus("current")
_Pm200frs02PerfDatacomClientPast24StatHistoryPort1Table_Object = MibTable
pm200frs02PerfDatacomClientPast24StatHistoryPort1Table = _Pm200frs02PerfDatacomClientPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944)
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientPast24StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry = _Pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1)
)
pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfDatacomClientPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfDatacomClientPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfDatacomClientPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfDatacomClientPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfDatacomClientPast24StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfDatacomClientPast24StatHistoryPort1Index = _Pm200frs02PerfDatacomClientPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 1),
    _Pm200frs02PerfDatacomClientPast24StatHistoryPort1Index_Type()
)
pm200frs02PerfDatacomClientPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfDatacomClientPast24StatHistoryPort1Index.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1 = _Pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 4),
    _Pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatInCrcCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast24StatInCrcCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatInCrcCountPort1 = _Pm200frs02perfdatacomclientPast24StatInCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 5),
    _Pm200frs02perfdatacomclientPast24StatInCrcCountPort1_Type()
)
pm200frs02perfdatacomclientPast24StatInCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatInCrcCountPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1 = _Pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 6),
    _Pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatInPacketCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast24StatInPacketCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatInPacketCountPort1 = _Pm200frs02perfdatacomclientPast24StatInPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 7),
    _Pm200frs02perfdatacomclientPast24StatInPacketCountPort1_Type()
)
pm200frs02perfdatacomclientPast24StatInPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatInPacketCountPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1 = _Pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 28),
    _Pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatOutCrcCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast24StatOutCrcCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatOutCrcCountPort1 = _Pm200frs02perfdatacomclientPast24StatOutCrcCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 29),
    _Pm200frs02perfdatacomclientPast24StatOutCrcCountPort1_Type()
)
pm200frs02perfdatacomclientPast24StatOutCrcCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatOutCrcCountPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1_Type = EkiOnOff
_Pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1 = _Pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 30),
    _Pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1_Type()
)
pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1.setStatus("current")
_Pm200frs02perfdatacomclientPast24StatOutPacketCountPort1_Type = Counter64
_Pm200frs02perfdatacomclientPast24StatOutPacketCountPort1_Object = MibTableColumn
pm200frs02perfdatacomclientPast24StatOutPacketCountPort1 = _Pm200frs02perfdatacomclientPast24StatOutPacketCountPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 6, 944, 1, 31),
    _Pm200frs02perfdatacomclientPast24StatOutPacketCountPort1_Type()
)
pm200frs02perfdatacomclientPast24StatOutPacketCountPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02perfdatacomclientPast24StatOutPacketCountPort1.setStatus("current")
_Pm200frs02MonPerfLine_ObjectIdentity = ObjectIdentity
pm200frs02MonPerfLine = _Pm200frs02MonPerfLine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7)
)
_Pm200frs02PerfTelecomLinePostFecCurrent15StatTable_Object = MibTable
pm200frs02PerfTelecomLinePostFecCurrent15StatTable = _Pm200frs02PerfTelecomLinePostFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatTable.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatEntry_Object = MibTableRow
pm200frs02PerfTelecomLinePostFecCurrent15StatEntry = _Pm200frs02PerfTelecomLinePostFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1)
)
pm200frs02PerfTelecomLinePostFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomLinePostFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomLinePostFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomLinePostFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomLinePostFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomLinePostFecCurrent15StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatIndex = _Pm200frs02PerfTelecomLinePostFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 1),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatIndex_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatIndex.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 2),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 3),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 4),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 5),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 6),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 7),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 8),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 9),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 10),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 336, 1, 11),
    _Pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Table = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1)
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 1),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 2),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 3),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 4),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 5),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 6),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 7),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 8),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 9),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 10),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 337, 1, 11),
    _Pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatTable_Object = MibTable
pm200frs02PerfTelecomLinePostFecCurrent24StatTable = _Pm200frs02PerfTelecomLinePostFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatTable.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatEntry_Object = MibTableRow
pm200frs02PerfTelecomLinePostFecCurrent24StatEntry = _Pm200frs02PerfTelecomLinePostFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1)
)
pm200frs02PerfTelecomLinePostFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomLinePostFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomLinePostFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomLinePostFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomLinePostFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomLinePostFecCurrent24StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatIndex = _Pm200frs02PerfTelecomLinePostFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 1),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatIndex_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatIndex.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 2),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 3),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 4),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 5),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 6),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 7),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 8),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 9),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 10),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn = _Pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 338, 1, 11),
    _Pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn_Type()
)
pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Table = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1)
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 1),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 2),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 3),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 4),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 5),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 6),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 7),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 8),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 9),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 10),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1.setStatus("current")
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1 = _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 339, 1, 11),
    _Pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1_Type()
)
pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatTable_Object = MibTable
pm200frs02PerfTelecomBerLinePreFecCurrent15StatTable = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatTable.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry_Object = MibTableRow
pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1)
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 1),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 2),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 3),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 4),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 5),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 6),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 352, 1, 7),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Table = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1)
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 1),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1 = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 2),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1 = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 3),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1 = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 4),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1 = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 5),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1 = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 6),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1 = _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 353, 1, 7),
    _Pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatTable_Object = MibTable
pm200frs02PerfTelecomBerLinePreFecCurrent24StatTable = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatTable_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatTable.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry_Object = MibTableRow
pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1)
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry.setStatus("current")


class _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex_Type(Integer32):
    """Custom type pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 1),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 2),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 3),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 4),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 5),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 6),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn = _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 354, 1, 7),
    _Pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn_Type()
)
pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object = MibTable
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Table = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Table_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355)
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Table.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object = MibTableRow
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1)
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setIndexNames(
    (0, "EKINOPS-Pm200frs02-MIB", "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index"),
)
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry.setStatus("current")


class _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type(Integer32):
    """Custom type pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type.__name__ = "Integer32"
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 1),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1 = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 2),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1 = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 3),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1 = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 4),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1 = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 5),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type = EkiOnOff
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1 = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 6),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1.setStatus("current")
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type = Unsigned32
_Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object = MibTableColumn
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1 = _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Object(
    (1, 3, 6, 1, 4, 1, 20044, 90, 11, 7, 355, 1, 7),
    _Pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1_Type()
)
pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1.setStatus("current")

# Managed Objects groups


# Notification objects

pm200frs02LineTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 30)
)
pm200frs02LineTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapLineNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02LineTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm200frs02LineTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 31)
)
pm200frs02LineTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineDdmWarningPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapLineNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02LineTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm200frs02LineTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 32)
)
pm200frs02LineTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapLineNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02LineTrapUrgentGoesOn.setStatus(
        "current"
    )

pm200frs02LineTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 33)
)
pm200frs02LineTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineDdmAlmPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapLineNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02LineTrapUrgentGoesOff.setStatus(
        "current"
    )

pm200frs02LineTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 34)
)
pm200frs02LineTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineFailPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineHwFailPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapLineNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02LineTrapCritGoesOn.setStatus(
        "current"
    )

pm200frs02LineTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 35)
)
pm200frs02LineTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineFailPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmLineHwFailPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapLineNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02LineTrapCritGoesOff.setStatus(
        "current"
    )

pm200frs02ClientTrapNotUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 40)
)
pm200frs02ClientTrapNotUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapPortNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02ClientTrapNotUrgentGoesOn.setStatus(
        "current"
    )

pm200frs02ClientTrapNotUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 41)
)
pm200frs02ClientTrapNotUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmSfpDdmWarningPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapPortNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02ClientTrapNotUrgentGoesOff.setStatus(
        "current"
    )

pm200frs02ClientTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 42)
)
pm200frs02ClientTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapPortNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02ClientTrapUrgentGoesOn.setStatus(
        "current"
    )

pm200frs02ClientTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 43)
)
pm200frs02ClientTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmSfpDdmAlmPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapPortNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02ClientTrapUrgentGoesOff.setStatus(
        "current"
    )

pm200frs02ClientTrapCritGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 44)
)
pm200frs02ClientTrapCritGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmFailAccPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmHwFailAccPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapPortNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02ClientTrapCritGoesOn.setStatus(
        "current"
    )

pm200frs02ClientTrapCritGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 45)
)
pm200frs02ClientTrapCritGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmFailAccPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmHwFailAccPortn"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapPortNumber"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02ClientTrapCritGoesOff.setStatus(
        "current"
    )

pm200frs02PowerTrapUrgentGoesOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 50)
)
pm200frs02PowerTrapUrgentGoesOn.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmDefFuseB"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmDefFuseA"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02PowerTrapUrgentGoesOn.setStatus(
        "current"
    )

pm200frs02PowerTrapUrgentGoesOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 20044, 90, 10, 51)
)
pm200frs02PowerTrapUrgentGoesOff.setObjects(
      *(("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmDefFuseB"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02AlmDefFuseA"),
        ("EKINOPS-Pm200frs02-MIB", "pm200frs02trapBoardNumber"))
)
if mibBuilder.loadTexts:
    pm200frs02PowerTrapUrgentGoesOff.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EKINOPS-Pm200frs02-MIB",
    **{"Pm200frs02MultiRate": Pm200frs02MultiRate,
       "Pm200frs02OtxMode": Pm200frs02OtxMode,
       "Pm200frs02OtxGrid": Pm200frs02OtxGrid,
       "Pm200frs02AdjustValue": Pm200frs02AdjustValue,
       "Pm200frs02ClientProtocol": Pm200frs02ClientProtocol,
       "Pm200frs02ModuleMode": Pm200frs02ModuleMode,
       "Pm200frs02OtxChannel": Pm200frs02OtxChannel,
       "Pm200frs02OrxChannel": Pm200frs02OrxChannel,
       "Pm200frs02DccMode": Pm200frs02DccMode,
       "modulePm200frs02": modulePm200frs02,
       "pm200frs02alarms": pm200frs02alarms,
       "pm200frs02AlmOther": pm200frs02AlmOther,
       "pm200frs02AlmOtherNurg": pm200frs02AlmOtherNurg,
       "pm200frs02AlmsynthAlm2": pm200frs02AlmsynthAlm2,
       "pm200frs02AlmConfTableSave": pm200frs02AlmConfTableSave,
       "pm200frs02AlmInvUpload": pm200frs02AlmInvUpload,
       "pm200frs02AlmConfTableLoad": pm200frs02AlmConfTableLoad,
       "pm200frs02AlmCorrelatOff": pm200frs02AlmCorrelatOff,
       "pm200frs02AlmMaintenanceOn": pm200frs02AlmMaintenanceOn,
       "pm200frs02AlmclientQsfpWarnDdm": pm200frs02AlmclientQsfpWarnDdm,
       "pm200frs02AlmTrscv1VccLowWng1": pm200frs02AlmTrscv1VccLowWng1,
       "pm200frs02AlmTrscv1VccHighWng1": pm200frs02AlmTrscv1VccHighWng1,
       "pm200frs02AlmTrscv1TempLowWng1": pm200frs02AlmTrscv1TempLowWng1,
       "pm200frs02AlmTrscv1TempHighWng1": pm200frs02AlmTrscv1TempHighWng1,
       "pm200frs02AlmTrscv2VccLowWng1": pm200frs02AlmTrscv2VccLowWng1,
       "pm200frs02AlmTrscv2VccHighWng1": pm200frs02AlmTrscv2VccHighWng1,
       "pm200frs02AlmTrscv2TempLowWng1": pm200frs02AlmTrscv2TempLowWng1,
       "pm200frs02AlmTrscv2TempHighWng1": pm200frs02AlmTrscv2TempHighWng1,
       "pm200frs02AlmOtherUrg": pm200frs02AlmOtherUrg,
       "pm200frs02AlmclientQsfpAlarmDdm": pm200frs02AlmclientQsfpAlarmDdm,
       "pm200frs02AlmTrscv1VccLowAla1": pm200frs02AlmTrscv1VccLowAla1,
       "pm200frs02AlmTrscv1VccHighAla1": pm200frs02AlmTrscv1VccHighAla1,
       "pm200frs02AlmTrscv1TempLowAla1": pm200frs02AlmTrscv1TempLowAla1,
       "pm200frs02AlmTrscv1TempHighAla": pm200frs02AlmTrscv1TempHighAla,
       "pm200frs02AlmTrscv2VccLowAla1": pm200frs02AlmTrscv2VccLowAla1,
       "pm200frs02AlmTrscv2VccHighAla1": pm200frs02AlmTrscv2VccHighAla1,
       "pm200frs02AlmTrscv2TempLowAla1": pm200frs02AlmTrscv2TempLowAla1,
       "pm200frs02AlmTrscv2TempHighAla1": pm200frs02AlmTrscv2TempHighAla1,
       "pm200frs02AlmOtherCrit": pm200frs02AlmOtherCrit,
       "pm200frs02AlmsynthAlm0": pm200frs02AlmsynthAlm0,
       "pm200frs02AlmFailFan": pm200frs02AlmFailFan,
       "pm200frs02AlmModGlobFail": pm200frs02AlmModGlobFail,
       "pm200frs02AlmDefFuseA": pm200frs02AlmDefFuseA,
       "pm200frs02AlmDefFuseB": pm200frs02AlmDefFuseB,
       "pm200frs02AlmmsaModuleState": pm200frs02AlmmsaModuleState,
       "pm200frs02AlmMsaInitialize": pm200frs02AlmMsaInitialize,
       "pm200frs02AlmMsaLowPower": pm200frs02AlmMsaLowPower,
       "pm200frs02AlmMsaHighPowerUp": pm200frs02AlmMsaHighPowerUp,
       "pm200frs02AlmMsaTxOff": pm200frs02AlmMsaTxOff,
       "pm200frs02AlmMsaTxTurnOn": pm200frs02AlmMsaTxTurnOn,
       "pm200frs02AlmMsaReady": pm200frs02AlmMsaReady,
       "pm200frs02AlmMsaFault": pm200frs02AlmMsaFault,
       "pm200frs02AlmMsaTxTurnOff": pm200frs02AlmMsaTxTurnOff,
       "pm200frs02AlmMsaHighPowerDown": pm200frs02AlmMsaHighPowerDown,
       "pm200frs02AlmClient": pm200frs02AlmClient,
       "pm200frs02AlmClientNurg": pm200frs02AlmClientNurg,
       "pm200frs02AlmClientUrg": pm200frs02AlmClientUrg,
       "pm200frs02AlmclientHostLaneFaultTable": pm200frs02AlmclientHostLaneFaultTable,
       "pm200frs02AlmclientHostLaneFaultEntry": pm200frs02AlmclientHostLaneFaultEntry,
       "pm200frs02AlmclientHostLaneFaultIndex": pm200frs02AlmclientHostLaneFaultIndex,
       "pm200frs02AlmClientLossOfSyncPortn": pm200frs02AlmClientLossOfSyncPortn,
       "pm200frs02AlmClientInputLossOfSigPortn": pm200frs02AlmClientInputLossOfSigPortn,
       "pm200frs02AlmClientLanesMarkerUnlockPortn": pm200frs02AlmClientLanesMarkerUnlockPortn,
       "pm200frs02AlmClientLanes6466UnlockPortn": pm200frs02AlmClientLanes6466UnlockPortn,
       "pm200frs02AlmClientLanesNotAlignedPortn": pm200frs02AlmClientLanesNotAlignedPortn,
       "pm200frs02AlmClientCsfDetectedPortn": pm200frs02AlmClientCsfDetectedPortn,
       "pm200frs02AlmClientTxHostLolPortn": pm200frs02AlmClientTxHostLolPortn,
       "pm200frs02AlmClientLaneTxFifoErrorPortn": pm200frs02AlmClientLaneTxFifoErrorPortn,
       "pm200frs02AlmClientCrit": pm200frs02AlmClientCrit,
       "pm200frs02AlmsynthAlmPortTable": pm200frs02AlmsynthAlmPortTable,
       "pm200frs02AlmsynthAlmPortEntry": pm200frs02AlmsynthAlmPortEntry,
       "pm200frs02AlmsynthAlmPortIndex": pm200frs02AlmsynthAlmPortIndex,
       "pm200frs02AlmSfpAbsentPortn": pm200frs02AlmSfpAbsentPortn,
       "pm200frs02AlmDdmAbsentPortn": pm200frs02AlmDdmAbsentPortn,
       "pm200frs02AlmHwFailAccPortn": pm200frs02AlmHwFailAccPortn,
       "pm200frs02AlmDwLsdPortn": pm200frs02AlmDwLsdPortn,
       "pm200frs02AlmClientLocalOosPortn": pm200frs02AlmClientLocalOosPortn,
       "pm200frs02AlmClientRemoteOosPortn": pm200frs02AlmClientRemoteOosPortn,
       "pm200frs02AlmDwCaisPortn": pm200frs02AlmDwCaisPortn,
       "pm200frs02AlmSfpDdmWarningPortn": pm200frs02AlmSfpDdmWarningPortn,
       "pm200frs02AlmSfpDdmAlmPortn": pm200frs02AlmSfpDdmAlmPortn,
       "pm200frs02AlmFailAccPortn": pm200frs02AlmFailAccPortn,
       "pm200frs02AlmUpCsfPortn": pm200frs02AlmUpCsfPortn,
       "pm200frs02AlmLine": pm200frs02AlmLine,
       "pm200frs02AlmLineNurg": pm200frs02AlmLineNurg,
       "pm200frs02AlmlineNetworkLaneAlarmWarning1Table": pm200frs02AlmlineNetworkLaneAlarmWarning1Table,
       "pm200frs02AlmlineNetworkLaneAlarmWarning1Entry": pm200frs02AlmlineNetworkLaneAlarmWarning1Entry,
       "pm200frs02AlmlineNetworkLaneAlarmWarning1Index": pm200frs02AlmlineNetworkLaneAlarmWarning1Index,
       "pm200frs02AlmLineRxPowerLowAlarmPortn": pm200frs02AlmLineRxPowerLowAlarmPortn,
       "pm200frs02AlmLineRxPowerLowWarningPortn": pm200frs02AlmLineRxPowerLowWarningPortn,
       "pm200frs02AlmLineRxPowerHighWarningPortn": pm200frs02AlmLineRxPowerHighWarningPortn,
       "pm200frs02AlmLineRxPowerHighAlarmPortn": pm200frs02AlmLineRxPowerHighAlarmPortn,
       "pm200frs02AlmLineLaserTempLowAlarmPortn": pm200frs02AlmLineLaserTempLowAlarmPortn,
       "pm200frs02AlmLineLaserTempLowWarningPortn": pm200frs02AlmLineLaserTempLowWarningPortn,
       "pm200frs02AlmLineLaserTempHighWarningPortn": pm200frs02AlmLineLaserTempHighWarningPortn,
       "pm200frs02AlmLineLaserTempHighAlarmPortn": pm200frs02AlmLineLaserTempHighAlarmPortn,
       "pm200frs02AlmLineTxPowerLowAlarmPortn": pm200frs02AlmLineTxPowerLowAlarmPortn,
       "pm200frs02AlmLineTxPowerLowWarningPortn": pm200frs02AlmLineTxPowerLowWarningPortn,
       "pm200frs02AlmLineTxPowerHighWarningPortn": pm200frs02AlmLineTxPowerHighWarningPortn,
       "pm200frs02AlmLineTxPowerHighAlarmPortn": pm200frs02AlmLineTxPowerHighAlarmPortn,
       "pm200frs02AlmLineBiasLowAlarmPortn": pm200frs02AlmLineBiasLowAlarmPortn,
       "pm200frs02AlmLineBiasLowWarningPortn": pm200frs02AlmLineBiasLowWarningPortn,
       "pm200frs02AlmLineBiasHighWarningPortn": pm200frs02AlmLineBiasHighWarningPortn,
       "pm200frs02AlmLineBiasHighAlarmPortn": pm200frs02AlmLineBiasHighAlarmPortn,
       "pm200frs02AlmlineNetworkLaneAlarmWarning2Table": pm200frs02AlmlineNetworkLaneAlarmWarning2Table,
       "pm200frs02AlmlineNetworkLaneAlarmWarning2Entry": pm200frs02AlmlineNetworkLaneAlarmWarning2Entry,
       "pm200frs02AlmlineNetworkLaneAlarmWarning2Index": pm200frs02AlmlineNetworkLaneAlarmWarning2Index,
       "pm200frs02AlmTxModulatorBiasLowAlarmPortn": pm200frs02AlmTxModulatorBiasLowAlarmPortn,
       "pm200frs02AlmTxModulatorBiasLowWarningPortn": pm200frs02AlmTxModulatorBiasLowWarningPortn,
       "pm200frs02AlmTxModulatorBiasHighWarningPortn": pm200frs02AlmTxModulatorBiasHighWarningPortn,
       "pm200frs02AlmTxModulatorBiasHighAlarmPortn": pm200frs02AlmTxModulatorBiasHighAlarmPortn,
       "pm200frs02AlmRxLaserTempLowAlarmPortn": pm200frs02AlmRxLaserTempLowAlarmPortn,
       "pm200frs02AlmRxLaserTempLowWarningPortn": pm200frs02AlmRxLaserTempLowWarningPortn,
       "pm200frs02AlmRxLaserTempHighWarningPortn": pm200frs02AlmRxLaserTempHighWarningPortn,
       "pm200frs02AlmRxLaserTempHighAlarmPortn": pm200frs02AlmRxLaserTempHighAlarmPortn,
       "pm200frs02AlmRxLaserOutputLowAlarmPortn": pm200frs02AlmRxLaserOutputLowAlarmPortn,
       "pm200frs02AlmRxLaserOutputLowWarningPortn": pm200frs02AlmRxLaserOutputLowWarningPortn,
       "pm200frs02AlmRxLaserOutputHighWarningPortn": pm200frs02AlmRxLaserOutputHighWarningPortn,
       "pm200frs02AlmRxLaserOutputHighAlarmPortn": pm200frs02AlmRxLaserOutputHighAlarmPortn,
       "pm200frs02AlmRxLaserBiasLowAlarmPortn": pm200frs02AlmRxLaserBiasLowAlarmPortn,
       "pm200frs02AlmRxLaserBiasLowWarningPortn": pm200frs02AlmRxLaserBiasLowWarningPortn,
       "pm200frs02AlmRxLaserBiasHighWarningPortn": pm200frs02AlmRxLaserBiasHighWarningPortn,
       "pm200frs02AlmRxLaserBiasHighAlarmPortn": pm200frs02AlmRxLaserBiasHighAlarmPortn,
       "pm200frs02AlmLineUrg": pm200frs02AlmLineUrg,
       "pm200frs02AlmlineHostLaneFaultTable": pm200frs02AlmlineHostLaneFaultTable,
       "pm200frs02AlmlineHostLaneFaultEntry": pm200frs02AlmlineHostLaneFaultEntry,
       "pm200frs02AlmlineHostLaneFaultIndex": pm200frs02AlmlineHostLaneFaultIndex,
       "pm200frs02AlmLineInputLossOfSignalPortn": pm200frs02AlmLineInputLossOfSignalPortn,
       "pm200frs02AlmLineLossOfFramePortn": pm200frs02AlmLineLossOfFramePortn,
       "pm200frs02AlmLineSmBdiInsertedPortn": pm200frs02AlmLineSmBdiInsertedPortn,
       "pm200frs02AlmLineSmBdiDetectedPortn": pm200frs02AlmLineSmBdiDetectedPortn,
       "pm200frs02AlmLineSmIaeInsertedPortn": pm200frs02AlmLineSmIaeInsertedPortn,
       "pm200frs02AlmLineSmIaeDetectedPortn": pm200frs02AlmLineSmIaeDetectedPortn,
       "pm200frs02AlmLineTxHostLolPortn": pm200frs02AlmLineTxHostLolPortn,
       "pm200frs02AlmLineLaneTxFifoErrorPortn": pm200frs02AlmLineLaneTxFifoErrorPortn,
       "pm200frs02AlmLineCrit": pm200frs02AlmLineCrit,
       "pm200frs02AlmsynthAlmLineTable": pm200frs02AlmsynthAlmLineTable,
       "pm200frs02AlmsynthAlmLineEntry": pm200frs02AlmsynthAlmLineEntry,
       "pm200frs02AlmsynthAlmLineIndex": pm200frs02AlmsynthAlmLineIndex,
       "pm200frs02AlmXfpAbsentPortn": pm200frs02AlmXfpAbsentPortn,
       "pm200frs02AlmXfpInitNotComplPortn": pm200frs02AlmXfpInitNotComplPortn,
       "pm200frs02AlmLineHwFailPortn": pm200frs02AlmLineHwFailPortn,
       "pm200frs02AlmXfpTxOffPortn": pm200frs02AlmXfpTxOffPortn,
       "pm200frs02AlmLineLocalOosPortn": pm200frs02AlmLineLocalOosPortn,
       "pm200frs02AlmUpRdiInsPortn": pm200frs02AlmUpRdiInsPortn,
       "pm200frs02AlmLineDdmWarningPortn": pm200frs02AlmLineDdmWarningPortn,
       "pm200frs02AlmLineDdmAlmPortn": pm200frs02AlmLineDdmAlmPortn,
       "pm200frs02AlmLineFailPortn": pm200frs02AlmLineFailPortn,
       "pm200frs02AlmLineActivePortn": pm200frs02AlmLineActivePortn,
       "pm200frs02measures": pm200frs02measures,
       "pm200frs02MesrOther": pm200frs02MesrOther,
       "pm200frs02Mesrsynth0": pm200frs02Mesrsynth0,
       "pm200frs02Mesrsynth1": pm200frs02Mesrsynth1,
       "pm200frs02MesrpmIntervalNumber": pm200frs02MesrpmIntervalNumber,
       "pm200frs02MesrlineNetTxLaserOutputPwrAverage": pm200frs02MesrlineNetTxLaserOutputPwrAverage,
       "pm200frs02MesrlineNetTxLaserTempAverage": pm200frs02MesrlineNetTxLaserTempAverage,
       "pm200frs02MesrlineNetTxBiasCurrentAverage": pm200frs02MesrlineNetTxBiasCurrentAverage,
       "pm200frs02MesrlineNetRxInputPwrAverage": pm200frs02MesrlineNetRxInputPwrAverage,
       "pm200frs02MesrlineResidualChromaticDispAverage": pm200frs02MesrlineResidualChromaticDispAverage,
       "pm200frs02MesrlineDiffGroupDelayAverage": pm200frs02MesrlineDiffGroupDelayAverage,
       "pm200frs02MesrlineQFactorAverage": pm200frs02MesrlineQFactorAverage,
       "pm200frs02MesrlineCarrierFreqOffsetAverage": pm200frs02MesrlineCarrierFreqOffsetAverage,
       "pm200frs02MesrlineOsnrAverage": pm200frs02MesrlineOsnrAverage,
       "pm200frs02MesrlineNetTxLaserOutputPwrMin": pm200frs02MesrlineNetTxLaserOutputPwrMin,
       "pm200frs02MesrlineNetTxLaserTempMin": pm200frs02MesrlineNetTxLaserTempMin,
       "pm200frs02MesrlineNetTxBiasCurrentMin": pm200frs02MesrlineNetTxBiasCurrentMin,
       "pm200frs02MesrlineNetRxInputPwrMin": pm200frs02MesrlineNetRxInputPwrMin,
       "pm200frs02MesrlineResidualChromaticDispMin": pm200frs02MesrlineResidualChromaticDispMin,
       "pm200frs02MesrlineDiffGroupDelayMin": pm200frs02MesrlineDiffGroupDelayMin,
       "pm200frs02MesrlineQFactorMin": pm200frs02MesrlineQFactorMin,
       "pm200frs02MesrlineCarrierFreqOffsetMin": pm200frs02MesrlineCarrierFreqOffsetMin,
       "pm200frs02MesrlineOsnrMin": pm200frs02MesrlineOsnrMin,
       "pm200frs02MesrlineNetTxLaserOutputPwrMax": pm200frs02MesrlineNetTxLaserOutputPwrMax,
       "pm200frs02MesrlineNetTxLaserTempMax": pm200frs02MesrlineNetTxLaserTempMax,
       "pm200frs02MesrlineNetTxBiasCurrentMax": pm200frs02MesrlineNetTxBiasCurrentMax,
       "pm200frs02MesrlineNetRxInputPwrMax": pm200frs02MesrlineNetRxInputPwrMax,
       "pm200frs02MesrlineResidualChromaticDispMax": pm200frs02MesrlineResidualChromaticDispMax,
       "pm200frs02MesrlineDiffGroupDelayMax": pm200frs02MesrlineDiffGroupDelayMax,
       "pm200frs02MesrlineQFactorMax": pm200frs02MesrlineQFactorMax,
       "pm200frs02MesrlineCarrierFreqOffsetMax": pm200frs02MesrlineCarrierFreqOffsetMax,
       "pm200frs02MesrlineOsnrMax": pm200frs02MesrlineOsnrMax,
       "pm200frs02MesrregVoltage": pm200frs02MesrregVoltage,
       "pm200frs02MesrregCurrent": pm200frs02MesrregCurrent,
       "pm200frs02MesrregTemp": pm200frs02MesrregTemp,
       "pm200frs02Mesrtrscv1Temp": pm200frs02Mesrtrscv1Temp,
       "pm200frs02Mesrtrscv2Temp": pm200frs02Mesrtrscv2Temp,
       "pm200frs02Mesrtrscv1PowerSupply": pm200frs02Mesrtrscv1PowerSupply,
       "pm200frs02Mesrtrscv2PowerSupply": pm200frs02Mesrtrscv2PowerSupply,
       "pm200frs02MesrClient": pm200frs02MesrClient,
       "pm200frs02MesrclientCfpTemp": pm200frs02MesrclientCfpTemp,
       "pm200frs02MesrclientCfp3v3Voltage": pm200frs02MesrclientCfp3v3Voltage,
       "pm200frs02MesrclientSoaBiasCurrent": pm200frs02MesrclientSoaBiasCurrent,
       "pm200frs02MesrclientTxPwrMinTable": pm200frs02MesrclientTxPwrMinTable,
       "pm200frs02MesrclientTxPwrMinEntry": pm200frs02MesrclientTxPwrMinEntry,
       "pm200frs02MesrclientTxPwrMinIndex": pm200frs02MesrclientTxPwrMinIndex,
       "pm200frs02MesrclientTxPwrMinPortn": pm200frs02MesrclientTxPwrMinPortn,
       "pm200frs02MesrclientRxPwrMinTable": pm200frs02MesrclientRxPwrMinTable,
       "pm200frs02MesrclientRxPwrMinEntry": pm200frs02MesrclientRxPwrMinEntry,
       "pm200frs02MesrclientRxPwrMinIndex": pm200frs02MesrclientRxPwrMinIndex,
       "pm200frs02MesrclientRxPwrMinPortn": pm200frs02MesrclientRxPwrMinPortn,
       "pm200frs02MesrclientTxPwrMaxTable": pm200frs02MesrclientTxPwrMaxTable,
       "pm200frs02MesrclientTxPwrMaxEntry": pm200frs02MesrclientTxPwrMaxEntry,
       "pm200frs02MesrclientTxPwrMaxIndex": pm200frs02MesrclientTxPwrMaxIndex,
       "pm200frs02MesrclientTxPwrMaxPortn": pm200frs02MesrclientTxPwrMaxPortn,
       "pm200frs02MesrclientRxPwrMaxTable": pm200frs02MesrclientRxPwrMaxTable,
       "pm200frs02MesrclientRxPwrMaxEntry": pm200frs02MesrclientRxPwrMaxEntry,
       "pm200frs02MesrclientRxPwrMaxIndex": pm200frs02MesrclientRxPwrMaxIndex,
       "pm200frs02MesrclientRxPwrMaxPortn": pm200frs02MesrclientRxPwrMaxPortn,
       "pm200frs02MesrclientTxCompositePwrTable": pm200frs02MesrclientTxCompositePwrTable,
       "pm200frs02MesrclientTxCompositePwrEntry": pm200frs02MesrclientTxCompositePwrEntry,
       "pm200frs02MesrclientTxCompositePwrIndex": pm200frs02MesrclientTxCompositePwrIndex,
       "pm200frs02MesrclientTxCompositePwrPortn": pm200frs02MesrclientTxCompositePwrPortn,
       "pm200frs02MesrclientRxCompositePwrTable": pm200frs02MesrclientRxCompositePwrTable,
       "pm200frs02MesrclientRxCompositePwrEntry": pm200frs02MesrclientRxCompositePwrEntry,
       "pm200frs02MesrclientRxCompositePwrIndex": pm200frs02MesrclientRxCompositePwrIndex,
       "pm200frs02MesrclientRxCompositePwrPortn": pm200frs02MesrclientRxCompositePwrPortn,
       "pm200frs02MesrLine": pm200frs02MesrLine,
       "pm200frs02MesrlineMsaTemp": pm200frs02MesrlineMsaTemp,
       "pm200frs02MesrlineMsa3v3Voltage": pm200frs02MesrlineMsa3v3Voltage,
       "pm200frs02MesrlineSoaBiasCurrent": pm200frs02MesrlineSoaBiasCurrent,
       "pm200frs02MesrlineNetTxLaserOutputPwrTable": pm200frs02MesrlineNetTxLaserOutputPwrTable,
       "pm200frs02MesrlineNetTxLaserOutputPwrEntry": pm200frs02MesrlineNetTxLaserOutputPwrEntry,
       "pm200frs02MesrlineNetTxLaserOutputPwrIndex": pm200frs02MesrlineNetTxLaserOutputPwrIndex,
       "pm200frs02MesrlineNetTxLaserOutputPwrPortn": pm200frs02MesrlineNetTxLaserOutputPwrPortn,
       "pm200frs02MesrlineNetTxLaserTempTable": pm200frs02MesrlineNetTxLaserTempTable,
       "pm200frs02MesrlineNetTxLaserTempEntry": pm200frs02MesrlineNetTxLaserTempEntry,
       "pm200frs02MesrlineNetTxLaserTempIndex": pm200frs02MesrlineNetTxLaserTempIndex,
       "pm200frs02MesrlineNetTxLaserTempPortn": pm200frs02MesrlineNetTxLaserTempPortn,
       "pm200frs02MesrlineNetTxBiasCurrentTable": pm200frs02MesrlineNetTxBiasCurrentTable,
       "pm200frs02MesrlineNetTxBiasCurrentEntry": pm200frs02MesrlineNetTxBiasCurrentEntry,
       "pm200frs02MesrlineNetTxBiasCurrentIndex": pm200frs02MesrlineNetTxBiasCurrentIndex,
       "pm200frs02MesrlineNetTxBiasCurrentPortn": pm200frs02MesrlineNetTxBiasCurrentPortn,
       "pm200frs02MesrlineNetRxInputPwrTable": pm200frs02MesrlineNetRxInputPwrTable,
       "pm200frs02MesrlineNetRxInputPwrEntry": pm200frs02MesrlineNetRxInputPwrEntry,
       "pm200frs02MesrlineNetRxInputPwrIndex": pm200frs02MesrlineNetRxInputPwrIndex,
       "pm200frs02MesrlineNetRxInputPwrPortn": pm200frs02MesrlineNetRxInputPwrPortn,
       "pm200frs02MesrlineResidualChromaticDispTable": pm200frs02MesrlineResidualChromaticDispTable,
       "pm200frs02MesrlineResidualChromaticDispEntry": pm200frs02MesrlineResidualChromaticDispEntry,
       "pm200frs02MesrlineResidualChromaticDispIndex": pm200frs02MesrlineResidualChromaticDispIndex,
       "pm200frs02MesrlineResidualChromaticDispPortn": pm200frs02MesrlineResidualChromaticDispPortn,
       "pm200frs02MesrlineDiffGroupDelayTable": pm200frs02MesrlineDiffGroupDelayTable,
       "pm200frs02MesrlineDiffGroupDelayEntry": pm200frs02MesrlineDiffGroupDelayEntry,
       "pm200frs02MesrlineDiffGroupDelayIndex": pm200frs02MesrlineDiffGroupDelayIndex,
       "pm200frs02MesrlineDiffGroupDelayPortn": pm200frs02MesrlineDiffGroupDelayPortn,
       "pm200frs02MesrlineQFactorTable": pm200frs02MesrlineQFactorTable,
       "pm200frs02MesrlineQFactorEntry": pm200frs02MesrlineQFactorEntry,
       "pm200frs02MesrlineQFactorIndex": pm200frs02MesrlineQFactorIndex,
       "pm200frs02MesrlineQFactorPortn": pm200frs02MesrlineQFactorPortn,
       "pm200frs02MesrlineCarrierFreqOffsetTable": pm200frs02MesrlineCarrierFreqOffsetTable,
       "pm200frs02MesrlineCarrierFreqOffsetEntry": pm200frs02MesrlineCarrierFreqOffsetEntry,
       "pm200frs02MesrlineCarrierFreqOffsetIndex": pm200frs02MesrlineCarrierFreqOffsetIndex,
       "pm200frs02MesrlineCarrierFreqOffsetPortn": pm200frs02MesrlineCarrierFreqOffsetPortn,
       "pm200frs02MesrlineOsnrTable": pm200frs02MesrlineOsnrTable,
       "pm200frs02MesrlineOsnrEntry": pm200frs02MesrlineOsnrEntry,
       "pm200frs02MesrlineOsnrIndex": pm200frs02MesrlineOsnrIndex,
       "pm200frs02MesrlineOsnrPortn": pm200frs02MesrlineOsnrPortn,
       "pm200frs02counters": pm200frs02counters,
       "pm200frs02CntOther": pm200frs02CntOther,
       "pm200frs02CntClient": pm200frs02CntClient,
       "pm200frs02CntclientInputErrorCounterTable": pm200frs02CntclientInputErrorCounterTable,
       "pm200frs02CntclientInputErrorCounterEntry": pm200frs02CntclientInputErrorCounterEntry,
       "pm200frs02CntclientInputErrorCounterIndex": pm200frs02CntclientInputErrorCounterIndex,
       "pm200frs02CntclientInputErrorCounterValuePortn": pm200frs02CntclientInputErrorCounterValuePortn,
       "pm200frs02CntclientInputErrorCounterErrorPortn": pm200frs02CntclientInputErrorCounterErrorPortn,
       "pm200frs02CntclientInputErrorCounterOverloadPortn": pm200frs02CntclientInputErrorCounterOverloadPortn,
       "pm200frs02CntclientCbipCounterTable": pm200frs02CntclientCbipCounterTable,
       "pm200frs02CntclientCbipCounterEntry": pm200frs02CntclientCbipCounterEntry,
       "pm200frs02CntclientCbipCounterIndex": pm200frs02CntclientCbipCounterIndex,
       "pm200frs02CntclientCbipCounterValuePortn": pm200frs02CntclientCbipCounterValuePortn,
       "pm200frs02CntclientCbipCounterErrorPortn": pm200frs02CntclientCbipCounterErrorPortn,
       "pm200frs02CntclientCbipCounterOverloadPortn": pm200frs02CntclientCbipCounterOverloadPortn,
       "pm200frs02CntLine": pm200frs02CntLine,
       "pm200frs02CntlocalLineSmBip8ErrorCounterTable": pm200frs02CntlocalLineSmBip8ErrorCounterTable,
       "pm200frs02CntlocalLineSmBip8ErrorCounterEntry": pm200frs02CntlocalLineSmBip8ErrorCounterEntry,
       "pm200frs02CntlocalLineSmBip8ErrorCounterIndex": pm200frs02CntlocalLineSmBip8ErrorCounterIndex,
       "pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn": pm200frs02CntlocalLineSmBip8ErrorCounterValuePortn,
       "pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn": pm200frs02CntlocalLineSmBip8ErrorCounterErrorPortn,
       "pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn": pm200frs02CntlocalLineSmBip8ErrorCounterOverloadPortn,
       "pm200frs02CntlocalLineFecCorrectedErrorsCounterTable": pm200frs02CntlocalLineFecCorrectedErrorsCounterTable,
       "pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry": pm200frs02CntlocalLineFecCorrectedErrorsCounterEntry,
       "pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex": pm200frs02CntlocalLineFecCorrectedErrorsCounterIndex,
       "pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn": pm200frs02CntlocalLineFecCorrectedErrorsCounterValuePortn,
       "pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn": pm200frs02CntlocalLineFecCorrectedErrorsCounterErrorPortn,
       "pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn": pm200frs02CntlocalLineFecCorrectedErrorsCounterOverloadPortn,
       "pm200frs02CntremoteLineSmBip8ErrorCounterTable": pm200frs02CntremoteLineSmBip8ErrorCounterTable,
       "pm200frs02CntremoteLineSmBip8ErrorCounterEntry": pm200frs02CntremoteLineSmBip8ErrorCounterEntry,
       "pm200frs02CntremoteLineSmBip8ErrorCounterIndex": pm200frs02CntremoteLineSmBip8ErrorCounterIndex,
       "pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn": pm200frs02CntremoteLineSmBip8ErrorCounterValuePortn,
       "pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn": pm200frs02CntremoteLineSmBip8ErrorCounterErrorPortn,
       "pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn": pm200frs02CntremoteLineSmBip8ErrorCounterOverloadPortn,
       "pm200frs02CntlineDfrmTimCntTable": pm200frs02CntlineDfrmTimCntTable,
       "pm200frs02CntlineDfrmTimCntEntry": pm200frs02CntlineDfrmTimCntEntry,
       "pm200frs02CntlineDfrmTimCntIndex": pm200frs02CntlineDfrmTimCntIndex,
       "pm200frs02CntlineDfrmTimCntValuePortn": pm200frs02CntlineDfrmTimCntValuePortn,
       "pm200frs02CntlineDfrmTimCntErrorPortn": pm200frs02CntlineDfrmTimCntErrorPortn,
       "pm200frs02CntlineDfrmTimCntOverloadPortn": pm200frs02CntlineDfrmTimCntOverloadPortn,
       "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterTable": pm200frs02CntlocalLineTrscvPreSdFecErrorCounterTable,
       "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry": pm200frs02CntlocalLineTrscvPreSdFecErrorCounterEntry,
       "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex": pm200frs02CntlocalLineTrscvPreSdFecErrorCounterIndex,
       "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn": pm200frs02CntlocalLineTrscvPreSdFecErrorCounterValuePortn,
       "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn": pm200frs02CntlocalLineTrscvPreSdFecErrorCounterErrorPortn,
       "pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn": pm200frs02CntlocalLineTrscvPreSdFecErrorCounterOverloadPortn,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterTable": pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterTable,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry": pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterEntry,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex": pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterIndex,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn": pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterValuePortn,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn": pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterErrorPortn,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn": pm200frs02CntlocalLineTrscvUncorrectedSdFecErrorCounterOverloadPortn,
       "pm200frs02CntlocalLineTrscvPreSdFecBitCounterTable": pm200frs02CntlocalLineTrscvPreSdFecBitCounterTable,
       "pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry": pm200frs02CntlocalLineTrscvPreSdFecBitCounterEntry,
       "pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex": pm200frs02CntlocalLineTrscvPreSdFecBitCounterIndex,
       "pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn": pm200frs02CntlocalLineTrscvPreSdFecBitCounterValuePortn,
       "pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn": pm200frs02CntlocalLineTrscvPreSdFecBitCounterErrorPortn,
       "pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn": pm200frs02CntlocalLineTrscvPreSdFecBitCounterOverloadPortn,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterTable": pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterTable,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry": pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterEntry,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex": pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterIndex,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn": pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterValuePortn,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn": pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterErrorPortn,
       "pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn": pm200frs02CntlocalLineTrscvUncorrectedSdFecBitCounterOverloadPortn,
       "pm200frs02controlsWrite": pm200frs02controlsWrite,
       "pm200frs02CtrlOther": pm200frs02CtrlOther,
       "pm200frs02CtrlconfMgnt1": pm200frs02CtrlconfMgnt1,
       "pm200frs02CtrlConf1Load1": pm200frs02CtrlConf1Load1,
       "pm200frs02CtrlConf2Load1": pm200frs02CtrlConf2Load1,
       "pm200frs02CtrlConf2Flash1": pm200frs02CtrlConf2Flash1,
       "pm200frs02CtrlConf2Clear1": pm200frs02CtrlConf2Clear1,
       "pm200frs02Ctrlsynth4": pm200frs02Ctrlsynth4,
       "pm200frs02CtrlCorrelatOn": pm200frs02CtrlCorrelatOn,
       "pm200frs02CtrlCorrelatOff": pm200frs02CtrlCorrelatOff,
       "pm200frs02CtrlswMgnt": pm200frs02CtrlswMgnt,
       "pm200frs02CtrlColdReset": pm200frs02CtrlColdReset,
       "pm200frs02CtrlWarmReset": pm200frs02CtrlWarmReset,
       "pm200frs02CtrlLoadSwBank1": pm200frs02CtrlLoadSwBank1,
       "pm200frs02CtrlLoadSwBank2": pm200frs02CtrlLoadSwBank2,
       "pm200frs02CtrlgwMgnt": pm200frs02CtrlgwMgnt,
       "pm200frs02CtrlCurrentGwReset": pm200frs02CtrlCurrentGwReset,
       "pm200frs02CtrlLoadGwBank1": pm200frs02CtrlLoadGwBank1,
       "pm200frs02CtrlLoadGwBank2": pm200frs02CtrlLoadGwBank2,
       "pm200frs02CtrlLoadGwBank3": pm200frs02CtrlLoadGwBank3,
       "pm200frs02CtrlLoadGwBank4": pm200frs02CtrlLoadGwBank4,
       "pm200frs02CtrlledTest": pm200frs02CtrlledTest,
       "pm200frs02CtrlGreenLed": pm200frs02CtrlGreenLed,
       "pm200frs02CtrlRedLed": pm200frs02CtrlRedLed,
       "pm200frs02CtrlLedOff": pm200frs02CtrlLedOff,
       "pm200frs02CtrlinitSwitchMarvell": pm200frs02CtrlinitSwitchMarvell,
       "pm200frs02CtrlInitSwitchMarvell": pm200frs02CtrlInitSwitchMarvell,
       "pm200frs02CtrlresetCount": pm200frs02CtrlresetCount,
       "pm200frs02CtrlResetcount": pm200frs02CtrlResetcount,
       "pm200frs02CtrlresetRmon": pm200frs02CtrlresetRmon,
       "pm200frs02CtrlResetrmon": pm200frs02CtrlResetrmon,
       "pm200frs02CtrlresetMeasurements": pm200frs02CtrlresetMeasurements,
       "pm200frs02CtrlResetmeasurements": pm200frs02CtrlResetmeasurements,
       "pm200frs02CtrlClient": pm200frs02CtrlClient,
       "pm200frs02CtrlaccessLoopTable": pm200frs02CtrlaccessLoopTable,
       "pm200frs02CtrlaccessLoopEntry": pm200frs02CtrlaccessLoopEntry,
       "pm200frs02CtrlaccessLoopIndex": pm200frs02CtrlaccessLoopIndex,
       "pm200frs02CtrlaccessLoopPortn": pm200frs02CtrlaccessLoopPortn,
       "pm200frs02CtrlclientLoopToLineTable": pm200frs02CtrlclientLoopToLineTable,
       "pm200frs02CtrlclientLoopToLineEntry": pm200frs02CtrlclientLoopToLineEntry,
       "pm200frs02CtrlclientLoopToLineIndex": pm200frs02CtrlclientLoopToLineIndex,
       "pm200frs02CtrlclientLoopToLinePortn": pm200frs02CtrlclientLoopToLinePortn,
       "pm200frs02CtrlcsfUpInsTable": pm200frs02CtrlcsfUpInsTable,
       "pm200frs02CtrlcsfUpInsEntry": pm200frs02CtrlcsfUpInsEntry,
       "pm200frs02CtrlcsfUpInsIndex": pm200frs02CtrlcsfUpInsIndex,
       "pm200frs02CtrlcsfUpInsPortn": pm200frs02CtrlcsfUpInsPortn,
       "pm200frs02CtrlcaisDwInsTable": pm200frs02CtrlcaisDwInsTable,
       "pm200frs02CtrlcaisDwInsEntry": pm200frs02CtrlcaisDwInsEntry,
       "pm200frs02CtrlcaisDwInsIndex": pm200frs02CtrlcaisDwInsIndex,
       "pm200frs02CtrlcaisDwInsPortn": pm200frs02CtrlcaisDwInsPortn,
       "pm200frs02CtrlclientResetAllCountTable": pm200frs02CtrlclientResetAllCountTable,
       "pm200frs02CtrlclientResetAllCountEntry": pm200frs02CtrlclientResetAllCountEntry,
       "pm200frs02CtrlclientResetAllCountIndex": pm200frs02CtrlclientResetAllCountIndex,
       "pm200frs02CtrlclientResetAllCountsPortn": pm200frs02CtrlclientResetAllCountsPortn,
       "pm200frs02CtrlLine": pm200frs02CtrlLine,
       "pm200frs02CtrlcommAccessLoopTable": pm200frs02CtrlcommAccessLoopTable,
       "pm200frs02CtrlcommAccessLoopEntry": pm200frs02CtrlcommAccessLoopEntry,
       "pm200frs02CtrlcommAccessLoopIndex": pm200frs02CtrlcommAccessLoopIndex,
       "pm200frs02CtrlcommAccessLoopPortn": pm200frs02CtrlcommAccessLoopPortn,
       "pm200frs02CtrllineLoopTable": pm200frs02CtrllineLoopTable,
       "pm200frs02CtrllineLoopEntry": pm200frs02CtrllineLoopEntry,
       "pm200frs02CtrllineLoopIndex": pm200frs02CtrllineLoopIndex,
       "pm200frs02CtrllineLoopPortn": pm200frs02CtrllineLoopPortn,
       "pm200frs02CtrlfecDisableTable": pm200frs02CtrlfecDisableTable,
       "pm200frs02CtrlfecDisableEntry": pm200frs02CtrlfecDisableEntry,
       "pm200frs02CtrlfecDisableIndex": pm200frs02CtrlfecDisableIndex,
       "pm200frs02CtrlfecDisablePortn": pm200frs02CtrlfecDisablePortn,
       "pm200frs02CtrlmsaLineLoopTable": pm200frs02CtrlmsaLineLoopTable,
       "pm200frs02CtrlmsaLineLoopEntry": pm200frs02CtrlmsaLineLoopEntry,
       "pm200frs02CtrlmsaLineLoopIndex": pm200frs02CtrlmsaLineLoopIndex,
       "pm200frs02CtrlmsaLineLoopPortn": pm200frs02CtrlmsaLineLoopPortn,
       "pm200frs02CtrlmsaTxResetTable": pm200frs02CtrlmsaTxResetTable,
       "pm200frs02CtrlmsaTxResetEntry": pm200frs02CtrlmsaTxResetEntry,
       "pm200frs02CtrlmsaTxResetIndex": pm200frs02CtrlmsaTxResetIndex,
       "pm200frs02CtrlmsaTxResetPortn": pm200frs02CtrlmsaTxResetPortn,
       "pm200frs02CtrlmsaRxResetTable": pm200frs02CtrlmsaRxResetTable,
       "pm200frs02CtrlmsaRxResetEntry": pm200frs02CtrlmsaRxResetEntry,
       "pm200frs02CtrlmsaRxResetIndex": pm200frs02CtrlmsaRxResetIndex,
       "pm200frs02CtrlmsaRxResetPortn": pm200frs02CtrlmsaRxResetPortn,
       "pm200frs02CtrlmsaShutdownTable": pm200frs02CtrlmsaShutdownTable,
       "pm200frs02CtrlmsaShutdownEntry": pm200frs02CtrlmsaShutdownEntry,
       "pm200frs02CtrlmsaShutdownIndex": pm200frs02CtrlmsaShutdownIndex,
       "pm200frs02CtrlmsaShutdownPortn": pm200frs02CtrlmsaShutdownPortn,
       "pm200frs02CtrllineResetAllCountTable": pm200frs02CtrllineResetAllCountTable,
       "pm200frs02CtrllineResetAllCountEntry": pm200frs02CtrllineResetAllCountEntry,
       "pm200frs02CtrllineResetAllCountIndex": pm200frs02CtrllineResetAllCountIndex,
       "pm200frs02CtrllineResetAllCountsPortn": pm200frs02CtrllineResetAllCountsPortn,
       "pm200frs02ri": pm200frs02ri,
       "pm200frs02riTable": pm200frs02riTable,
       "pm200frs02RinvSfpTable": pm200frs02RinvSfpTable,
       "pm200frs02RinvSfpEntry": pm200frs02RinvSfpEntry,
       "pm200frs02RinvSfpIndex": pm200frs02RinvSfpIndex,
       "pm200frs02Rinvsfp": pm200frs02Rinvsfp,
       "pm200frs02RinvLineTable": pm200frs02RinvLineTable,
       "pm200frs02RinvLineEntry": pm200frs02RinvLineEntry,
       "pm200frs02RinvLineIndex": pm200frs02RinvLineIndex,
       "pm200frs02RinvxfpLine": pm200frs02RinvxfpLine,
       "pm200frs02RinvReloadInventory": pm200frs02RinvReloadInventory,
       "pm200frs02RinvHwPlatform": pm200frs02RinvHwPlatform,
       "pm200frs02RinvModulePlatform": pm200frs02RinvModulePlatform,
       "pm200frs02RinvSwPlatform": pm200frs02RinvSwPlatform,
       "pm200frs02RinvGwPlatform": pm200frs02RinvGwPlatform,
       "pm200frs02download": pm200frs02download,
       "pm200frs02DwlOther": pm200frs02DwlOther,
       "pm200frs02DwlrestartProcess": pm200frs02DwlrestartProcess,
       "pm200frs02DwlWarmRestartProcessed": pm200frs02DwlWarmRestartProcessed,
       "pm200frs02DwlColdRestartProcessed": pm200frs02DwlColdRestartProcessed,
       "pm200frs02DwlswBanksUsed": pm200frs02DwlswBanksUsed,
       "pm200frs02DwlSwBank1Used": pm200frs02DwlSwBank1Used,
       "pm200frs02DwlSwBank2Used": pm200frs02DwlSwBank2Used,
       "pm200frs02DwlSwBank1Notempty": pm200frs02DwlSwBank1Notempty,
       "pm200frs02DwlSwBank2Notempty": pm200frs02DwlSwBank2Notempty,
       "pm200frs02DwlgwBanksUsed": pm200frs02DwlgwBanksUsed,
       "pm200frs02DwlGwBank1Used": pm200frs02DwlGwBank1Used,
       "pm200frs02DwlGwBank2Used": pm200frs02DwlGwBank2Used,
       "pm200frs02DwlGwBank3Used": pm200frs02DwlGwBank3Used,
       "pm200frs02DwlGwBank4Used": pm200frs02DwlGwBank4Used,
       "pm200frs02DwlGwBank1Notempty": pm200frs02DwlGwBank1Notempty,
       "pm200frs02DwlGwBank2Notempty": pm200frs02DwlGwBank2Notempty,
       "pm200frs02DwlGwBank3Notempty": pm200frs02DwlGwBank3Notempty,
       "pm200frs02DwlGwBank4Notempty": pm200frs02DwlGwBank4Notempty,
       "pm200frs02DwlClient": pm200frs02DwlClient,
       "pm200frs02DwlLine": pm200frs02DwlLine,
       "pm200frs02Config": pm200frs02Config,
       "pm200frs02CfgAccessCAisCsf": pm200frs02CfgAccessCAisCsf,
       "pm200frs02CfgClientcaiscsfTable": pm200frs02CfgClientcaiscsfTable,
       "pm200frs02CfgClientcaiscsfEntry": pm200frs02CfgClientcaiscsfEntry,
       "pm200frs02CfgClientcaiscsfIndex": pm200frs02CfgClientcaiscsfIndex,
       "pm200frs02CfgReservePortn": pm200frs02CfgReservePortn,
       "pm200frs02CfgStartup": pm200frs02CfgStartup,
       "pm200frs02CfgClientStartupTable": pm200frs02CfgClientStartupTable,
       "pm200frs02CfgClientStartupEntry": pm200frs02CfgClientStartupEntry,
       "pm200frs02CfgClientStartupIndex": pm200frs02CfgClientStartupIndex,
       "pm200frs02CfgSystConfPortPortn": pm200frs02CfgSystConfPortPortn,
       "pm200frs02CfgNetConfPortPortn": pm200frs02CfgNetConfPortPortn,
       "pm200frs02CfgOptionsPortPortn": pm200frs02CfgOptionsPortPortn,
       "pm200frs02CfgLineStartupTable": pm200frs02CfgLineStartupTable,
       "pm200frs02CfgLineStartupEntry": pm200frs02CfgLineStartupEntry,
       "pm200frs02CfgLineStartupIndex": pm200frs02CfgLineStartupIndex,
       "pm200frs02CfgSystConfLinePortn": pm200frs02CfgSystConfLinePortn,
       "pm200frs02CfgOptionsLinePortn": pm200frs02CfgOptionsLinePortn,
       "pm200frs02CfgXfpTable": pm200frs02CfgXfpTable,
       "pm200frs02CfgXfpEntry": pm200frs02CfgXfpEntry,
       "pm200frs02CfgXfpIndex": pm200frs02CfgXfpIndex,
       "pm200frs02CfgSystConfMsaLinePortn": pm200frs02CfgSystConfMsaLinePortn,
       "pm200frs02CfgLabels": pm200frs02CfgLabels,
       "pm200frs02CfgLabelclientTable": pm200frs02CfgLabelclientTable,
       "pm200frs02CfgLabelclientEntry": pm200frs02CfgLabelclientEntry,
       "pm200frs02CfgLabelclientIndex": pm200frs02CfgLabelclientIndex,
       "pm200frs02CfgLabelclientPortn": pm200frs02CfgLabelclientPortn,
       "pm200frs02CfgLabellineTable": pm200frs02CfgLabellineTable,
       "pm200frs02CfgLabellineEntry": pm200frs02CfgLabellineEntry,
       "pm200frs02CfgLabellineIndex": pm200frs02CfgLabellineIndex,
       "pm200frs02CfgLabellinePortn": pm200frs02CfgLabellinePortn,
       "pm200frs02CfgStartuptlh": pm200frs02CfgStartuptlh,
       "pm200frs02CfgOtxtlhTable": pm200frs02CfgOtxtlhTable,
       "pm200frs02CfgOtxtlhEntry": pm200frs02CfgOtxtlhEntry,
       "pm200frs02CfgOtxtlhIndex": pm200frs02CfgOtxtlhIndex,
       "pm200frs02CfgLinePwrLaserPortn": pm200frs02CfgLinePwrLaserPortn,
       "pm200frs02CfgLineFCurrentPortn": pm200frs02CfgLineFCurrentPortn,
       "pm200frs02CfgLineGridCurrentPortn": pm200frs02CfgLineGridCurrentPortn,
       "pm200frs02CfgFPortn": pm200frs02CfgFPortn,
       "pm200frs02CfgRxLineFCurrentPortn": pm200frs02CfgRxLineFCurrentPortn,
       "pm200frs02CfgOther": pm200frs02CfgOther,
       "pm200frs02tablemoduleOther": pm200frs02tablemoduleOther,
       "pm200frs02Cfgmode": pm200frs02Cfgmode,
       "pm200frs02CfgfanLowSpeedThreshold": pm200frs02CfgfanLowSpeedThreshold,
       "pm200frs02CfgfanHighSpeedThreshold": pm200frs02CfgfanHighSpeedThreshold,
       "pm200frs02CfgmoduleMode": pm200frs02CfgmoduleMode,
       "pm200frs02CfgStartuptablefive": pm200frs02CfgStartuptablefive,
       "pm200frs02CfgOtxtlhcapabilitiesTable": pm200frs02CfgOtxtlhcapabilitiesTable,
       "pm200frs02CfgOtxtlhcapabilitiesEntry": pm200frs02CfgOtxtlhcapabilitiesEntry,
       "pm200frs02CfgOtxtlhcapabilitiesIndex": pm200frs02CfgOtxtlhcapabilitiesIndex,
       "pm200frs02CfgComponentTypePortn": pm200frs02CfgComponentTypePortn,
       "pm200frs02CfgMiscellaneousPortn": pm200frs02CfgMiscellaneousPortn,
       "pm200frs02CfgFirstChannelPortn": pm200frs02CfgFirstChannelPortn,
       "pm200frs02CfgLastChannelPortn": pm200frs02CfgLastChannelPortn,
       "pm200frs02CfgGridPortn": pm200frs02CfgGridPortn,
       "pm200frs02CfgWriteConfiguration": pm200frs02CfgWriteConfiguration,
       "pm200frs02traps": pm200frs02traps,
       "pm200frs02trapPortNumber": pm200frs02trapPortNumber,
       "pm200frs02trapLineNumber": pm200frs02trapLineNumber,
       "pm200frs02trapBoardNumber": pm200frs02trapBoardNumber,
       "pm200frs02LineTrapNotUrgentGoesOn": pm200frs02LineTrapNotUrgentGoesOn,
       "pm200frs02LineTrapNotUrgentGoesOff": pm200frs02LineTrapNotUrgentGoesOff,
       "pm200frs02LineTrapUrgentGoesOn": pm200frs02LineTrapUrgentGoesOn,
       "pm200frs02LineTrapUrgentGoesOff": pm200frs02LineTrapUrgentGoesOff,
       "pm200frs02LineTrapCritGoesOn": pm200frs02LineTrapCritGoesOn,
       "pm200frs02LineTrapCritGoesOff": pm200frs02LineTrapCritGoesOff,
       "pm200frs02ClientTrapNotUrgentGoesOn": pm200frs02ClientTrapNotUrgentGoesOn,
       "pm200frs02ClientTrapNotUrgentGoesOff": pm200frs02ClientTrapNotUrgentGoesOff,
       "pm200frs02ClientTrapUrgentGoesOn": pm200frs02ClientTrapUrgentGoesOn,
       "pm200frs02ClientTrapUrgentGoesOff": pm200frs02ClientTrapUrgentGoesOff,
       "pm200frs02ClientTrapCritGoesOn": pm200frs02ClientTrapCritGoesOn,
       "pm200frs02ClientTrapCritGoesOff": pm200frs02ClientTrapCritGoesOff,
       "pm200frs02PowerTrapUrgentGoesOn": pm200frs02PowerTrapUrgentGoesOn,
       "pm200frs02PowerTrapUrgentGoesOff": pm200frs02PowerTrapUrgentGoesOff,
       "pm200frs02Monitoring": pm200frs02Monitoring,
       "pm200frs02MonOther": pm200frs02MonOther,
       "pm200frs02MonRmon": pm200frs02MonRmon,
       "pm200frs02MonClient": pm200frs02MonClient,
       "pm200frs02MonClientRmonCounter": pm200frs02MonClientRmonCounter,
       "pm200frs02MonupRmonBytesCounterClientInputTable": pm200frs02MonupRmonBytesCounterClientInputTable,
       "pm200frs02MonupRmonBytesCounterClientInputEntry": pm200frs02MonupRmonBytesCounterClientInputEntry,
       "pm200frs02MonupRmonBytesCounterClientInputIndex": pm200frs02MonupRmonBytesCounterClientInputIndex,
       "pm200frs02MonupRmonBytesCounterClientInputValuePortn": pm200frs02MonupRmonBytesCounterClientInputValuePortn,
       "pm200frs02MonupRmonBytesCounterClientInputErrorPortn": pm200frs02MonupRmonBytesCounterClientInputErrorPortn,
       "pm200frs02MonupRmonBytesCounterClientInputOverloadPortn": pm200frs02MonupRmonBytesCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonCrcErrorsCounterClientInputTable": pm200frs02MonupRmonCrcErrorsCounterClientInputTable,
       "pm200frs02MonupRmonCrcErrorsCounterClientInputEntry": pm200frs02MonupRmonCrcErrorsCounterClientInputEntry,
       "pm200frs02MonupRmonCrcErrorsCounterClientInputIndex": pm200frs02MonupRmonCrcErrorsCounterClientInputIndex,
       "pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn": pm200frs02MonupRmonCrcErrorsCounterClientInputValuePortn,
       "pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn": pm200frs02MonupRmonCrcErrorsCounterClientInputErrorPortn,
       "pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn": pm200frs02MonupRmonCrcErrorsCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonPacketsCounterClientInputTable": pm200frs02MonupRmonPacketsCounterClientInputTable,
       "pm200frs02MonupRmonPacketsCounterClientInputEntry": pm200frs02MonupRmonPacketsCounterClientInputEntry,
       "pm200frs02MonupRmonPacketsCounterClientInputIndex": pm200frs02MonupRmonPacketsCounterClientInputIndex,
       "pm200frs02MonupRmonPacketsCounterClientInputValuePortn": pm200frs02MonupRmonPacketsCounterClientInputValuePortn,
       "pm200frs02MonupRmonPacketsCounterClientInputErrorPortn": pm200frs02MonupRmonPacketsCounterClientInputErrorPortn,
       "pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn": pm200frs02MonupRmonPacketsCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonBroadcastCounterClientInputTable": pm200frs02MonupRmonBroadcastCounterClientInputTable,
       "pm200frs02MonupRmonBroadcastCounterClientInputEntry": pm200frs02MonupRmonBroadcastCounterClientInputEntry,
       "pm200frs02MonupRmonBroadcastCounterClientInputIndex": pm200frs02MonupRmonBroadcastCounterClientInputIndex,
       "pm200frs02MonupRmonBroadcastCounterClientInputValuePortn": pm200frs02MonupRmonBroadcastCounterClientInputValuePortn,
       "pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn": pm200frs02MonupRmonBroadcastCounterClientInputErrorPortn,
       "pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn": pm200frs02MonupRmonBroadcastCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonMulticastCounterClientInputTable": pm200frs02MonupRmonMulticastCounterClientInputTable,
       "pm200frs02MonupRmonMulticastCounterClientInputEntry": pm200frs02MonupRmonMulticastCounterClientInputEntry,
       "pm200frs02MonupRmonMulticastCounterClientInputIndex": pm200frs02MonupRmonMulticastCounterClientInputIndex,
       "pm200frs02MonupRmonMulticastCounterClientInputValuePortn": pm200frs02MonupRmonMulticastCounterClientInputValuePortn,
       "pm200frs02MonupRmonMulticastCounterClientInputErrorPortn": pm200frs02MonupRmonMulticastCounterClientInputErrorPortn,
       "pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn": pm200frs02MonupRmonMulticastCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonPauseFrameCounterClientInputTable": pm200frs02MonupRmonPauseFrameCounterClientInputTable,
       "pm200frs02MonupRmonPauseFrameCounterClientInputEntry": pm200frs02MonupRmonPauseFrameCounterClientInputEntry,
       "pm200frs02MonupRmonPauseFrameCounterClientInputIndex": pm200frs02MonupRmonPauseFrameCounterClientInputIndex,
       "pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn": pm200frs02MonupRmonPauseFrameCounterClientInputValuePortn,
       "pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn": pm200frs02MonupRmonPauseFrameCounterClientInputErrorPortn,
       "pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn": pm200frs02MonupRmonPauseFrameCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonUnicastCounterClientInputTable": pm200frs02MonupRmonUnicastCounterClientInputTable,
       "pm200frs02MonupRmonUnicastCounterClientInputEntry": pm200frs02MonupRmonUnicastCounterClientInputEntry,
       "pm200frs02MonupRmonUnicastCounterClientInputIndex": pm200frs02MonupRmonUnicastCounterClientInputIndex,
       "pm200frs02MonupRmonUnicastCounterClientInputValuePortn": pm200frs02MonupRmonUnicastCounterClientInputValuePortn,
       "pm200frs02MonupRmonUnicastCounterClientInputErrorPortn": pm200frs02MonupRmonUnicastCounterClientInputErrorPortn,
       "pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn": pm200frs02MonupRmonUnicastCounterClientInputOverloadPortn,
       "pm200frs02MonupRmonNonunicastCounterClientInputTable": pm200frs02MonupRmonNonunicastCounterClientInputTable,
       "pm200frs02MonupRmonNonunicastCounterClientInputEntry": pm200frs02MonupRmonNonunicastCounterClientInputEntry,
       "pm200frs02MonupRmonNonunicastCounterClientInputIndex": pm200frs02MonupRmonNonunicastCounterClientInputIndex,
       "pm200frs02MonupRmonNonunicastCounterClientInputValuePortn": pm200frs02MonupRmonNonunicastCounterClientInputValuePortn,
       "pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn": pm200frs02MonupRmonNonunicastCounterClientInputErrorPortn,
       "pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn": pm200frs02MonupRmonNonunicastCounterClientInputOverloadPortn,
       "pm200frs02MondownRmonBytesCounterClientOutputTable": pm200frs02MondownRmonBytesCounterClientOutputTable,
       "pm200frs02MondownRmonBytesCounterClientOutputEntry": pm200frs02MondownRmonBytesCounterClientOutputEntry,
       "pm200frs02MondownRmonBytesCounterClientOutputIndex": pm200frs02MondownRmonBytesCounterClientOutputIndex,
       "pm200frs02MondownRmonBytesCounterClientOutputValuePortn": pm200frs02MondownRmonBytesCounterClientOutputValuePortn,
       "pm200frs02MondownRmonBytesCounterClientOutputErrorPortn": pm200frs02MondownRmonBytesCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn": pm200frs02MondownRmonBytesCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonCrcErrorsCounterClientOutputTable": pm200frs02MondownRmonCrcErrorsCounterClientOutputTable,
       "pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry": pm200frs02MondownRmonCrcErrorsCounterClientOutputEntry,
       "pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex": pm200frs02MondownRmonCrcErrorsCounterClientOutputIndex,
       "pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn": pm200frs02MondownRmonCrcErrorsCounterClientOutputValuePortn,
       "pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn": pm200frs02MondownRmonCrcErrorsCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn": pm200frs02MondownRmonCrcErrorsCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonPacketsCounterClientOutputTable": pm200frs02MondownRmonPacketsCounterClientOutputTable,
       "pm200frs02MondownRmonPacketsCounterClientOutputEntry": pm200frs02MondownRmonPacketsCounterClientOutputEntry,
       "pm200frs02MondownRmonPacketsCounterClientOutputIndex": pm200frs02MondownRmonPacketsCounterClientOutputIndex,
       "pm200frs02MondownRmonPacketsCounterClientOutputValuePortn": pm200frs02MondownRmonPacketsCounterClientOutputValuePortn,
       "pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn": pm200frs02MondownRmonPacketsCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn": pm200frs02MondownRmonPacketsCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonBroadcastCounterClientOutputTable": pm200frs02MondownRmonBroadcastCounterClientOutputTable,
       "pm200frs02MondownRmonBroadcastCounterClientOutputEntry": pm200frs02MondownRmonBroadcastCounterClientOutputEntry,
       "pm200frs02MondownRmonBroadcastCounterClientOutputIndex": pm200frs02MondownRmonBroadcastCounterClientOutputIndex,
       "pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn": pm200frs02MondownRmonBroadcastCounterClientOutputValuePortn,
       "pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn": pm200frs02MondownRmonBroadcastCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn": pm200frs02MondownRmonBroadcastCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonMulticastCounterClientOutputTable": pm200frs02MondownRmonMulticastCounterClientOutputTable,
       "pm200frs02MondownRmonMulticastCounterClientOutputEntry": pm200frs02MondownRmonMulticastCounterClientOutputEntry,
       "pm200frs02MondownRmonMulticastCounterClientOutputIndex": pm200frs02MondownRmonMulticastCounterClientOutputIndex,
       "pm200frs02MondownRmonMulticastCounterClientOutputValuePortn": pm200frs02MondownRmonMulticastCounterClientOutputValuePortn,
       "pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn": pm200frs02MondownRmonMulticastCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn": pm200frs02MondownRmonMulticastCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonPauseFrameCounterClientOutputTable": pm200frs02MondownRmonPauseFrameCounterClientOutputTable,
       "pm200frs02MondownRmonPauseFrameCounterClientOutputEntry": pm200frs02MondownRmonPauseFrameCounterClientOutputEntry,
       "pm200frs02MondownRmonPauseFrameCounterClientOutputIndex": pm200frs02MondownRmonPauseFrameCounterClientOutputIndex,
       "pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn": pm200frs02MondownRmonPauseFrameCounterClientOutputValuePortn,
       "pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn": pm200frs02MondownRmonPauseFrameCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn": pm200frs02MondownRmonPauseFrameCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonUnicastCounterClientOutputTable": pm200frs02MondownRmonUnicastCounterClientOutputTable,
       "pm200frs02MondownRmonUnicastCounterClientOutputEntry": pm200frs02MondownRmonUnicastCounterClientOutputEntry,
       "pm200frs02MondownRmonUnicastCounterClientOutputIndex": pm200frs02MondownRmonUnicastCounterClientOutputIndex,
       "pm200frs02MondownRmonUnicastCounterClientOutputValuePortn": pm200frs02MondownRmonUnicastCounterClientOutputValuePortn,
       "pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn": pm200frs02MondownRmonUnicastCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn": pm200frs02MondownRmonUnicastCounterClientOutputOverloadPortn,
       "pm200frs02MondownRmonNonunicastCounterClientOutputTable": pm200frs02MondownRmonNonunicastCounterClientOutputTable,
       "pm200frs02MondownRmonNonunicastCounterClientOutputEntry": pm200frs02MondownRmonNonunicastCounterClientOutputEntry,
       "pm200frs02MondownRmonNonunicastCounterClientOutputIndex": pm200frs02MondownRmonNonunicastCounterClientOutputIndex,
       "pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn": pm200frs02MondownRmonNonunicastCounterClientOutputValuePortn,
       "pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn": pm200frs02MondownRmonNonunicastCounterClientOutputErrorPortn,
       "pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn": pm200frs02MondownRmonNonunicastCounterClientOutputOverloadPortn,
       "pm200frs02MonPerfOther": pm200frs02MonPerfOther,
       "pm200frs02MonPerfSync": pm200frs02MonPerfSync,
       "pm200frs02PerfEnable": pm200frs02PerfEnable,
       "pm200frs02Perf15minSync": pm200frs02Perf15minSync,
       "pm200frs02Perf24hSync": pm200frs02Perf24hSync,
       "pm200frs02MonPerfTimeStamp": pm200frs02MonPerfTimeStamp,
       "pm200frs02Perf15MinShort": pm200frs02Perf15MinShort,
       "pm200frs02Perf15MinLong": pm200frs02Perf15MinLong,
       "pm200frs02Perf24HoursShort": pm200frs02Perf24HoursShort,
       "pm200frs02Perf24HoursLong": pm200frs02Perf24HoursLong,
       "pm200frs02PerfCurrent15MinElapsedTime": pm200frs02PerfCurrent15MinElapsedTime,
       "pm200frs02PerfCurrent24HoursElapsedTime": pm200frs02PerfCurrent24HoursElapsedTime,
       "pm200frs02MonPerfClient": pm200frs02MonPerfClient,
       "pm200frs02PerfTelecomInputClientCurrent15StatTable": pm200frs02PerfTelecomInputClientCurrent15StatTable,
       "pm200frs02PerfTelecomInputClientCurrent15StatEntry": pm200frs02PerfTelecomInputClientCurrent15StatEntry,
       "pm200frs02PerfTelecomInputClientCurrent15StatIndex": pm200frs02PerfTelecomInputClientCurrent15StatIndex,
       "pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn": pm200frs02PerfTelecomInputClientCurrent15StatInvCvPortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn": pm200frs02PerfTelecomInputClientCurrent15StatCvValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn": pm200frs02PerfTelecomInputClientCurrent15StatInvEsPortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn": pm200frs02PerfTelecomInputClientCurrent15StatEsValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn": pm200frs02PerfTelecomInputClientCurrent15StatInvSesPortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn": pm200frs02PerfTelecomInputClientCurrent15StatSesValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn": pm200frs02PerfTelecomInputClientCurrent15StatInvSefsPortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn": pm200frs02PerfTelecomInputClientCurrent15StatSefsValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn": pm200frs02PerfTelecomInputClientCurrent15StatInvUasPortn,
       "pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn": pm200frs02PerfTelecomInputClientCurrent15StatUasValuePortn,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Table": pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Table,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry": pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Entry,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index": pm200frs02PerfTelecomInputClientPast15StatHistoryPort1Index,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1": pm200frs02PerfTelecomInputClientPast15StatHistoryInvCvPort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1": pm200frs02PerfTelecomInputClientPast15StatHistoryCvValuePort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1": pm200frs02PerfTelecomInputClientPast15StatHistoryInvEsPort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1": pm200frs02PerfTelecomInputClientPast15StatHistoryEsValuePort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1": pm200frs02PerfTelecomInputClientPast15StatHistoryInvSesPort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1": pm200frs02PerfTelecomInputClientPast15StatHistorySesValuePort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1": pm200frs02PerfTelecomInputClientPast15StatHistoryInvSefsPort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1": pm200frs02PerfTelecomInputClientPast15StatHistorySefsValuePort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1": pm200frs02PerfTelecomInputClientPast15StatHistoryInvUasPort1,
       "pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1": pm200frs02PerfTelecomInputClientPast15StatHistoryUasValuePort1,
       "pm200frs02PerfTelecomInputClientCurrent24StatTable": pm200frs02PerfTelecomInputClientCurrent24StatTable,
       "pm200frs02PerfTelecomInputClientCurrent24StatEntry": pm200frs02PerfTelecomInputClientCurrent24StatEntry,
       "pm200frs02PerfTelecomInputClientCurrent24StatIndex": pm200frs02PerfTelecomInputClientCurrent24StatIndex,
       "pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn": pm200frs02PerfTelecomInputClientCurrent24StatInvCvPortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn": pm200frs02PerfTelecomInputClientCurrent24StatCvValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn": pm200frs02PerfTelecomInputClientCurrent24StatInvEsPortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn": pm200frs02PerfTelecomInputClientCurrent24StatEsValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn": pm200frs02PerfTelecomInputClientCurrent24StatInvSesPortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn": pm200frs02PerfTelecomInputClientCurrent24StatSesValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn": pm200frs02PerfTelecomInputClientCurrent24StatInvSefsPortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn": pm200frs02PerfTelecomInputClientCurrent24StatSefsValuePortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn": pm200frs02PerfTelecomInputClientCurrent24StatInvUasPortn,
       "pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn": pm200frs02PerfTelecomInputClientCurrent24StatUasValuePortn,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Table": pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Table,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry": pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Entry,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index": pm200frs02PerfTelecomInputClientPast24StatHistoryPort1Index,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1": pm200frs02PerfTelecomInputClientPast24StatHistoryInvCvPort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1": pm200frs02PerfTelecomInputClientPast24StatHistoryCvValuePort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1": pm200frs02PerfTelecomInputClientPast24StatHistoryInvEsPort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1": pm200frs02PerfTelecomInputClientPast24StatHistoryEsValuePort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1": pm200frs02PerfTelecomInputClientPast24StatHistoryInvSesPort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1": pm200frs02PerfTelecomInputClientPast24StatHistorySesValuePort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1": pm200frs02PerfTelecomInputClientPast24StatHistoryInvSefsPort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1": pm200frs02PerfTelecomInputClientPast24StatHistorySefsValuePort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1": pm200frs02PerfTelecomInputClientPast24StatHistoryInvUasPort1,
       "pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1": pm200frs02PerfTelecomInputClientPast24StatHistoryUasValuePort1,
       "pm200frs02PerfTelecomOutputClientCurrent15StatTable": pm200frs02PerfTelecomOutputClientCurrent15StatTable,
       "pm200frs02PerfTelecomOutputClientCurrent15StatEntry": pm200frs02PerfTelecomOutputClientCurrent15StatEntry,
       "pm200frs02PerfTelecomOutputClientCurrent15StatIndex": pm200frs02PerfTelecomOutputClientCurrent15StatIndex,
       "pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn": pm200frs02PerfTelecomOutputClientCurrent15StatInvCvPortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn": pm200frs02PerfTelecomOutputClientCurrent15StatCvValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn": pm200frs02PerfTelecomOutputClientCurrent15StatInvEsPortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn": pm200frs02PerfTelecomOutputClientCurrent15StatEsValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn": pm200frs02PerfTelecomOutputClientCurrent15StatInvSesPortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn": pm200frs02PerfTelecomOutputClientCurrent15StatSesValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn": pm200frs02PerfTelecomOutputClientCurrent15StatInvSefsPortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn": pm200frs02PerfTelecomOutputClientCurrent15StatSefsValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn": pm200frs02PerfTelecomOutputClientCurrent15StatInvUasPortn,
       "pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn": pm200frs02PerfTelecomOutputClientCurrent15StatUasValuePortn,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Table": pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Table,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry": pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Entry,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index": pm200frs02PerfTelecomOutputClientPast15StatHistoryPort1Index,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryInvCvPort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryCvValuePort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryInvEsPort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryEsValuePort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSesPort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1": pm200frs02PerfTelecomOutputClientPast15StatHistorySesValuePort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryInvSefsPort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1": pm200frs02PerfTelecomOutputClientPast15StatHistorySefsValuePort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryInvUasPort1,
       "pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1": pm200frs02PerfTelecomOutputClientPast15StatHistoryUasValuePort1,
       "pm200frs02PerfTelecomOutputClientCurrent24StatTable": pm200frs02PerfTelecomOutputClientCurrent24StatTable,
       "pm200frs02PerfTelecomOutputClientCurrent24StatEntry": pm200frs02PerfTelecomOutputClientCurrent24StatEntry,
       "pm200frs02PerfTelecomOutputClientCurrent24StatIndex": pm200frs02PerfTelecomOutputClientCurrent24StatIndex,
       "pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn": pm200frs02PerfTelecomOutputClientCurrent24StatInvCvPortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn": pm200frs02PerfTelecomOutputClientCurrent24StatCvValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn": pm200frs02PerfTelecomOutputClientCurrent24StatInvEsPortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn": pm200frs02PerfTelecomOutputClientCurrent24StatEsValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn": pm200frs02PerfTelecomOutputClientCurrent24StatInvSesPortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn": pm200frs02PerfTelecomOutputClientCurrent24StatSesValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn": pm200frs02PerfTelecomOutputClientCurrent24StatInvSefsPortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn": pm200frs02PerfTelecomOutputClientCurrent24StatSefsValuePortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn": pm200frs02PerfTelecomOutputClientCurrent24StatInvUasPortn,
       "pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn": pm200frs02PerfTelecomOutputClientCurrent24StatUasValuePortn,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Table": pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Table,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry": pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Entry,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index": pm200frs02PerfTelecomOutputClientPast24StatHistoryPort1Index,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryInvCvPort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryCvValuePort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryInvEsPort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryEsValuePort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSesPort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1": pm200frs02PerfTelecomOutputClientPast24StatHistorySesValuePort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryInvSefsPort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1": pm200frs02PerfTelecomOutputClientPast24StatHistorySefsValuePort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryInvUasPort1,
       "pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1": pm200frs02PerfTelecomOutputClientPast24StatHistoryUasValuePort1,
       "pm200frs02PerfDatacomClientCurrent15StatTable": pm200frs02PerfDatacomClientCurrent15StatTable,
       "pm200frs02PerfDatacomClientCurrent15StatEntry": pm200frs02PerfDatacomClientCurrent15StatEntry,
       "pm200frs02PerfDatacomClientCurrent15StatIndex": pm200frs02PerfDatacomClientCurrent15StatIndex,
       "pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn": pm200frs02perfdatacomclientCurrent15StatInCrcCountInvPortn,
       "pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn": pm200frs02perfdatacomclientCurrent15StatInCrcCountPortn,
       "pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn": pm200frs02perfdatacomclientCurrent15StatInPacketCountInvPortn,
       "pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn": pm200frs02perfdatacomclientCurrent15StatInPacketCountPortn,
       "pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn": pm200frs02perfdatacomclientCurrent15StatOutCrcCountInvPortn,
       "pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn": pm200frs02perfdatacomclientCurrent15StatOutCrcCountPortn,
       "pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn": pm200frs02perfdatacomclientCurrent15StatOutPacketCountInvPortn,
       "pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn": pm200frs02perfdatacomclientCurrent15StatOutPacketCountPortn,
       "pm200frs02PerfDatacomClientPast15StatHistoryPort1Table": pm200frs02PerfDatacomClientPast15StatHistoryPort1Table,
       "pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry": pm200frs02PerfDatacomClientPast15StatHistoryPort1Entry,
       "pm200frs02PerfDatacomClientPast15StatHistoryPort1Index": pm200frs02PerfDatacomClientPast15StatHistoryPort1Index,
       "pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1": pm200frs02perfdatacomclientPast15StatInCrcCountInvPort1,
       "pm200frs02perfdatacomclientPast15StatInCrcCountPort1": pm200frs02perfdatacomclientPast15StatInCrcCountPort1,
       "pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1": pm200frs02perfdatacomclientPast15StatInPacketCountInvPort1,
       "pm200frs02perfdatacomclientPast15StatInPacketCountPort1": pm200frs02perfdatacomclientPast15StatInPacketCountPort1,
       "pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1": pm200frs02perfdatacomclientPast15StatOutCrcCountInvPort1,
       "pm200frs02perfdatacomclientPast15StatOutCrcCountPort1": pm200frs02perfdatacomclientPast15StatOutCrcCountPort1,
       "pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1": pm200frs02perfdatacomclientPast15StatOutPacketCountInvPort1,
       "pm200frs02perfdatacomclientPast15StatOutPacketCountPort1": pm200frs02perfdatacomclientPast15StatOutPacketCountPort1,
       "pm200frs02PerfDatacomClientCurrent24StatTable": pm200frs02PerfDatacomClientCurrent24StatTable,
       "pm200frs02PerfDatacomClientCurrent24StatEntry": pm200frs02PerfDatacomClientCurrent24StatEntry,
       "pm200frs02PerfDatacomClientCurrent24StatIndex": pm200frs02PerfDatacomClientCurrent24StatIndex,
       "pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn": pm200frs02perfdatacomclientCurrent24StatInCrcCountInvPortn,
       "pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn": pm200frs02perfdatacomclientCurrent24StatInCrcCountPortn,
       "pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn": pm200frs02perfdatacomclientCurrent24StatInPacketCountInvPortn,
       "pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn": pm200frs02perfdatacomclientCurrent24StatInPacketCountPortn,
       "pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn": pm200frs02perfdatacomclientCurrent24StatOutCrcCountInvPortn,
       "pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn": pm200frs02perfdatacomclientCurrent24StatOutCrcCountPortn,
       "pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn": pm200frs02perfdatacomclientCurrent24StatOutPacketCountInvPortn,
       "pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn": pm200frs02perfdatacomclientCurrent24StatOutPacketCountPortn,
       "pm200frs02PerfDatacomClientPast24StatHistoryPort1Table": pm200frs02PerfDatacomClientPast24StatHistoryPort1Table,
       "pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry": pm200frs02PerfDatacomClientPast24StatHistoryPort1Entry,
       "pm200frs02PerfDatacomClientPast24StatHistoryPort1Index": pm200frs02PerfDatacomClientPast24StatHistoryPort1Index,
       "pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1": pm200frs02perfdatacomclientPast24StatInCrcCountInvPort1,
       "pm200frs02perfdatacomclientPast24StatInCrcCountPort1": pm200frs02perfdatacomclientPast24StatInCrcCountPort1,
       "pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1": pm200frs02perfdatacomclientPast24StatInPacketCountInvPort1,
       "pm200frs02perfdatacomclientPast24StatInPacketCountPort1": pm200frs02perfdatacomclientPast24StatInPacketCountPort1,
       "pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1": pm200frs02perfdatacomclientPast24StatOutCrcCountInvPort1,
       "pm200frs02perfdatacomclientPast24StatOutCrcCountPort1": pm200frs02perfdatacomclientPast24StatOutCrcCountPort1,
       "pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1": pm200frs02perfdatacomclientPast24StatOutPacketCountInvPort1,
       "pm200frs02perfdatacomclientPast24StatOutPacketCountPort1": pm200frs02perfdatacomclientPast24StatOutPacketCountPort1,
       "pm200frs02MonPerfLine": pm200frs02MonPerfLine,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatTable": pm200frs02PerfTelecomLinePostFecCurrent15StatTable,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatEntry": pm200frs02PerfTelecomLinePostFecCurrent15StatEntry,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatIndex": pm200frs02PerfTelecomLinePostFecCurrent15StatIndex,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn": pm200frs02PerfTelecomLinePostFecCurrent15StatInvCvPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn": pm200frs02PerfTelecomLinePostFecCurrent15StatCvValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn": pm200frs02PerfTelecomLinePostFecCurrent15StatInvEsPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn": pm200frs02PerfTelecomLinePostFecCurrent15StatEsValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn": pm200frs02PerfTelecomLinePostFecCurrent15StatInvSesPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn": pm200frs02PerfTelecomLinePostFecCurrent15StatSesValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn": pm200frs02PerfTelecomLinePostFecCurrent15StatInvSefsPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn": pm200frs02PerfTelecomLinePostFecCurrent15StatSefsValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn": pm200frs02PerfTelecomLinePostFecCurrent15StatInvUasPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn": pm200frs02PerfTelecomLinePostFecCurrent15StatUasValuePortn,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Table": pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Table,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry": pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Entry,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index": pm200frs02PerfTelecomLinePostFecPast15StatHistoryPort1Index,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvCvPort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryCvValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvEsPort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryEsValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSesPort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1": pm200frs02PerfTelecomLinePostFecPast15StatHistorySesValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvSefsPort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1": pm200frs02PerfTelecomLinePostFecPast15StatHistorySefsValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryInvUasPort1,
       "pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1": pm200frs02PerfTelecomLinePostFecPast15StatHistoryUasValuePort1,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatTable": pm200frs02PerfTelecomLinePostFecCurrent24StatTable,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatEntry": pm200frs02PerfTelecomLinePostFecCurrent24StatEntry,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatIndex": pm200frs02PerfTelecomLinePostFecCurrent24StatIndex,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn": pm200frs02PerfTelecomLinePostFecCurrent24StatInvCvPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn": pm200frs02PerfTelecomLinePostFecCurrent24StatCvValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn": pm200frs02PerfTelecomLinePostFecCurrent24StatInvEsPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn": pm200frs02PerfTelecomLinePostFecCurrent24StatEsValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn": pm200frs02PerfTelecomLinePostFecCurrent24StatInvSesPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn": pm200frs02PerfTelecomLinePostFecCurrent24StatSesValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn": pm200frs02PerfTelecomLinePostFecCurrent24StatInvSefsPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn": pm200frs02PerfTelecomLinePostFecCurrent24StatSefsValuePortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn": pm200frs02PerfTelecomLinePostFecCurrent24StatInvUasPortn,
       "pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn": pm200frs02PerfTelecomLinePostFecCurrent24StatUasValuePortn,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Table": pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Table,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry": pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Entry,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index": pm200frs02PerfTelecomLinePostFecPast24StatHistoryPort1Index,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvCvPort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryCvValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvEsPort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryEsValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSesPort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1": pm200frs02PerfTelecomLinePostFecPast24StatHistorySesValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvSefsPort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1": pm200frs02PerfTelecomLinePostFecPast24StatHistorySefsValuePort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryInvUasPort1,
       "pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1": pm200frs02PerfTelecomLinePostFecPast24StatHistoryUasValuePort1,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatTable": pm200frs02PerfTelecomBerLinePreFecCurrent15StatTable,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry": pm200frs02PerfTelecomBerLinePreFecCurrent15StatEntry,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex": pm200frs02PerfTelecomBerLinePreFecCurrent15StatIndex,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn": pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvBerPortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn": pm200frs02PerfTelecomBerLinePreFecCurrent15StatBerValuePortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn": pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMinBerPortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn": pm200frs02PerfTelecomBerLinePreFecCurrent15StatMinBerValuePortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn": pm200frs02PerfTelecomBerLinePreFecCurrent15StatInvMaxBerPortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn": pm200frs02PerfTelecomBerLinePreFecCurrent15StatMaxBerValuePortn,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Table": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Table,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Entry,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryPort1Index,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvBerPort1,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryBerValuePort1,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMinBerPort1,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMinBerValuePort1,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryInvMaxBerPort1,
       "pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1": pm200frs02PerfTelecomBerLinePreFecPast15StatHistoryMaxBerValuePort1,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatTable": pm200frs02PerfTelecomBerLinePreFecCurrent24StatTable,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry": pm200frs02PerfTelecomBerLinePreFecCurrent24StatEntry,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex": pm200frs02PerfTelecomBerLinePreFecCurrent24StatIndex,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn": pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvBerPortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn": pm200frs02PerfTelecomBerLinePreFecCurrent24StatBerValuePortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn": pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMinBerPortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn": pm200frs02PerfTelecomBerLinePreFecCurrent24StatMinBerValuePortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn": pm200frs02PerfTelecomBerLinePreFecCurrent24StatInvMaxBerPortn,
       "pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn": pm200frs02PerfTelecomBerLinePreFecCurrent24StatMaxBerValuePortn,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Table": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Table,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Entry,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryPort1Index,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvBerPort1,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryBerValuePort1,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMinBerPort1,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMinBerValuePort1,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryInvMaxBerPort1,
       "pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1": pm200frs02PerfTelecomBerLinePreFecPast24StatHistoryMaxBerValuePort1}
)
