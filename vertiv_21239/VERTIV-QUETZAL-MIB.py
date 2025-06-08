# SNMP MIB module (VERTIV-QUETZAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_21239/VERTIV-QUETZAL-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:17:19 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

vertiv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21239)
)
if mibBuilder.loadTexts:
    vertiv.setRevisions(
        ("2019-08-30 00:00",
         "2019-06-06 00:00",
         "2018-01-19 00:00",
         "2016-06-29 00:00",
         "2012-09-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DeviceSerial(TextualConvention, OctetString):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class DeviceStatus(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("notFound", 2),
          ("ioError", 3),
          ("unknown", 4),
          ("deleted", 5))
    )



class DeviceLabel(TextualConvention, OctetString):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class TemperatureUnits(TextualConvention, Integer32):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fahrenheit", 1),
          ("celsius", 2))
    )



class TemperatureValue(TextualConvention, Integer32):
    status = "deprecated"
    displayHint = "d-1"


class DeciAmps(TextualConvention, Gauge32):
    status = "deprecated"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_Quetzal_ObjectIdentity = ObjectIdentity
quetzal = _Quetzal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6)
)
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1)
)
_Rtafhd3_ObjectIdentity = ObjectIdentity
rtafhd3 = _Rtafhd3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3)
)
_Rtafhd3Table_Object = MibTable
rtafhd3Table = _Rtafhd3Table_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rtafhd3Table.setStatus("deprecated")
_Rtafhd3Entry_Object = MibTableRow
rtafhd3Entry = _Rtafhd3Entry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1)
)
rtafhd3Entry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "rtafhd3Index"),
)
if mibBuilder.loadTexts:
    rtafhd3Entry.setStatus("deprecated")


class _Rtafhd3Index_Type(Unsigned32):
    """Custom type rtafhd3Index based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Rtafhd3Index_Type.__name__ = "Unsigned32"
_Rtafhd3Index_Object = MibTableColumn
rtafhd3Index = _Rtafhd3Index_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 1),
    _Rtafhd3Index_Type()
)
rtafhd3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtafhd3Index.setStatus("deprecated")
_Rtafhd3Serial_Type = DeviceSerial
_Rtafhd3Serial_Object = MibTableColumn
rtafhd3Serial = _Rtafhd3Serial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 2),
    _Rtafhd3Serial_Type()
)
rtafhd3Serial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3Serial.setStatus("deprecated")
_Rtafhd3Label_Type = DeviceLabel
_Rtafhd3Label_Object = MibTableColumn
rtafhd3Label = _Rtafhd3Label_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 3),
    _Rtafhd3Label_Type()
)
rtafhd3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtafhd3Label.setStatus("deprecated")
_Rtafhd3Status_Type = DeviceStatus
_Rtafhd3Status_Object = MibTableColumn
rtafhd3Status = _Rtafhd3Status_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 4),
    _Rtafhd3Status_Type()
)
rtafhd3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3Status.setStatus("deprecated")
_Rtafhd3Airflow_Type = Gauge32
_Rtafhd3Airflow_Object = MibTableColumn
rtafhd3Airflow = _Rtafhd3Airflow_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 5),
    _Rtafhd3Airflow_Type()
)
rtafhd3Airflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3Airflow.setStatus("deprecated")
_Rtafhd3Humidity_Type = Gauge32
_Rtafhd3Humidity_Object = MibTableColumn
rtafhd3Humidity = _Rtafhd3Humidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 6),
    _Rtafhd3Humidity_Type()
)
rtafhd3Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3Humidity.setStatus("deprecated")
_Rtafhd3Temp_Type = TemperatureValue
_Rtafhd3Temp_Object = MibTableColumn
rtafhd3Temp = _Rtafhd3Temp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 7),
    _Rtafhd3Temp_Type()
)
rtafhd3Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3Temp.setStatus("deprecated")
_Rtafhd3DewPoint_Type = TemperatureValue
_Rtafhd3DewPoint_Object = MibTableColumn
rtafhd3DewPoint = _Rtafhd3DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 8),
    _Rtafhd3DewPoint_Type()
)
rtafhd3DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3DewPoint.setStatus("deprecated")
_Rtafhd3TDUnits_Type = TemperatureUnits
_Rtafhd3TDUnits_Object = MibTableColumn
rtafhd3TDUnits = _Rtafhd3TDUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 3, 1, 1, 9),
    _Rtafhd3TDUnits_Type()
)
rtafhd3TDUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtafhd3TDUnits.setStatus("deprecated")
_Rt_ObjectIdentity = ObjectIdentity
rt = _Rt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8)
)
_RtTable_Object = MibTable
rtTable = _RtTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1)
)
if mibBuilder.loadTexts:
    rtTable.setStatus("deprecated")
_RtEntry_Object = MibTableRow
rtEntry = _RtEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1)
)
rtEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "rtIndex"),
)
if mibBuilder.loadTexts:
    rtEntry.setStatus("deprecated")


class _RtIndex_Type(Unsigned32):
    """Custom type rtIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RtIndex_Type.__name__ = "Unsigned32"
_RtIndex_Object = MibTableColumn
rtIndex = _RtIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1, 1),
    _RtIndex_Type()
)
rtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtIndex.setStatus("deprecated")
_RtSerial_Type = DeviceSerial
_RtSerial_Object = MibTableColumn
rtSerial = _RtSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1, 2),
    _RtSerial_Type()
)
rtSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtSerial.setStatus("deprecated")
_RtLabel_Type = DeviceLabel
_RtLabel_Object = MibTableColumn
rtLabel = _RtLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1, 3),
    _RtLabel_Type()
)
rtLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtLabel.setStatus("deprecated")
_RtStatus_Type = DeviceStatus
_RtStatus_Object = MibTableColumn
rtStatus = _RtStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1, 4),
    _RtStatus_Type()
)
rtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtStatus.setStatus("deprecated")
_RtTemp_Type = TemperatureValue
_RtTemp_Object = MibTableColumn
rtTemp = _RtTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1, 5),
    _RtTemp_Type()
)
rtTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtTemp.setStatus("deprecated")
_RtUnits_Type = TemperatureUnits
_RtUnits_Object = MibTableColumn
rtUnits = _RtUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 8, 1, 1, 6),
    _RtUnits_Type()
)
rtUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtUnits.setStatus("deprecated")
_T3hd_ObjectIdentity = ObjectIdentity
t3hd = _T3hd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9)
)
_T3hdTable_Object = MibTable
t3hdTable = _T3hdTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1)
)
if mibBuilder.loadTexts:
    t3hdTable.setStatus("deprecated")
_T3hdEntry_Object = MibTableRow
t3hdEntry = _T3hdEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1)
)
t3hdEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "t3hdIndex"),
)
if mibBuilder.loadTexts:
    t3hdEntry.setStatus("deprecated")


class _T3hdIndex_Type(Unsigned32):
    """Custom type t3hdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_T3hdIndex_Type.__name__ = "Unsigned32"
_T3hdIndex_Object = MibTableColumn
t3hdIndex = _T3hdIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 1),
    _T3hdIndex_Type()
)
t3hdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t3hdIndex.setStatus("deprecated")
_T3hdSerial_Type = DeviceSerial
_T3hdSerial_Object = MibTableColumn
t3hdSerial = _T3hdSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 2),
    _T3hdSerial_Type()
)
t3hdSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdSerial.setStatus("deprecated")
_T3hdLabel_Type = DeviceLabel
_T3hdLabel_Object = MibTableColumn
t3hdLabel = _T3hdLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 3),
    _T3hdLabel_Type()
)
t3hdLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdLabel.setStatus("deprecated")
_T3hdStatus_Type = DeviceStatus
_T3hdStatus_Object = MibTableColumn
t3hdStatus = _T3hdStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 4),
    _T3hdStatus_Type()
)
t3hdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdStatus.setStatus("deprecated")
_T3hdMainLabel_Type = DeviceLabel
_T3hdMainLabel_Object = MibTableColumn
t3hdMainLabel = _T3hdMainLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 5),
    _T3hdMainLabel_Type()
)
t3hdMainLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdMainLabel.setStatus("deprecated")
_T3hdMainTemp_Type = TemperatureValue
_T3hdMainTemp_Object = MibTableColumn
t3hdMainTemp = _T3hdMainTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 6),
    _T3hdMainTemp_Type()
)
t3hdMainTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdMainTemp.setStatus("deprecated")
_T3hdMainHumidity_Type = Gauge32
_T3hdMainHumidity_Object = MibTableColumn
t3hdMainHumidity = _T3hdMainHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 7),
    _T3hdMainHumidity_Type()
)
t3hdMainHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdMainHumidity.setStatus("deprecated")
_T3hdMainDewPoint_Type = TemperatureValue
_T3hdMainDewPoint_Object = MibTableColumn
t3hdMainDewPoint = _T3hdMainDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 8),
    _T3hdMainDewPoint_Type()
)
t3hdMainDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdMainDewPoint.setStatus("deprecated")


class _T3hdExt1Status_Type(Integer32):
    """Custom type t3hdExt1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unplugged", 0),
          ("normal", 1),
          ("error", 2))
    )


_T3hdExt1Status_Type.__name__ = "Integer32"
_T3hdExt1Status_Object = MibTableColumn
t3hdExt1Status = _T3hdExt1Status_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 9),
    _T3hdExt1Status_Type()
)
t3hdExt1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdExt1Status.setStatus("deprecated")
_T3hdExt1Label_Type = DeviceLabel
_T3hdExt1Label_Object = MibTableColumn
t3hdExt1Label = _T3hdExt1Label_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 10),
    _T3hdExt1Label_Type()
)
t3hdExt1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdExt1Label.setStatus("deprecated")
_T3hdExt1Temp_Type = TemperatureValue
_T3hdExt1Temp_Object = MibTableColumn
t3hdExt1Temp = _T3hdExt1Temp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 11),
    _T3hdExt1Temp_Type()
)
t3hdExt1Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdExt1Temp.setStatus("deprecated")


class _T3hdExt2Status_Type(Integer32):
    """Custom type t3hdExt2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unplugged", 0),
          ("normal", 1),
          ("error", 2))
    )


_T3hdExt2Status_Type.__name__ = "Integer32"
_T3hdExt2Status_Object = MibTableColumn
t3hdExt2Status = _T3hdExt2Status_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 12),
    _T3hdExt2Status_Type()
)
t3hdExt2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdExt2Status.setStatus("deprecated")
_T3hdExt2Label_Type = DeviceLabel
_T3hdExt2Label_Object = MibTableColumn
t3hdExt2Label = _T3hdExt2Label_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 13),
    _T3hdExt2Label_Type()
)
t3hdExt2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t3hdExt2Label.setStatus("deprecated")
_T3hdExt2Temp_Type = TemperatureValue
_T3hdExt2Temp_Object = MibTableColumn
t3hdExt2Temp = _T3hdExt2Temp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 14),
    _T3hdExt2Temp_Type()
)
t3hdExt2Temp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdExt2Temp.setStatus("deprecated")
_T3hdTDUnits_Type = TemperatureUnits
_T3hdTDUnits_Object = MibTableColumn
t3hdTDUnits = _T3hdTDUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 9, 1, 1, 15),
    _T3hdTDUnits_Type()
)
t3hdTDUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3hdTDUnits.setStatus("deprecated")
_Thd_ObjectIdentity = ObjectIdentity
thd = _Thd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10)
)
_ThdTable_Object = MibTable
thdTable = _ThdTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1)
)
if mibBuilder.loadTexts:
    thdTable.setStatus("deprecated")
_ThdEntry_Object = MibTableRow
thdEntry = _ThdEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1)
)
thdEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "thdIndex"),
)
if mibBuilder.loadTexts:
    thdEntry.setStatus("deprecated")


class _ThdIndex_Type(Unsigned32):
    """Custom type thdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ThdIndex_Type.__name__ = "Unsigned32"
_ThdIndex_Object = MibTableColumn
thdIndex = _ThdIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 1),
    _ThdIndex_Type()
)
thdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thdIndex.setStatus("deprecated")
_ThdSerial_Type = DeviceSerial
_ThdSerial_Object = MibTableColumn
thdSerial = _ThdSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 2),
    _ThdSerial_Type()
)
thdSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdSerial.setStatus("deprecated")
_ThdLabel_Type = DeviceLabel
_ThdLabel_Object = MibTableColumn
thdLabel = _ThdLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 3),
    _ThdLabel_Type()
)
thdLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thdLabel.setStatus("deprecated")
_ThdStatus_Type = DeviceStatus
_ThdStatus_Object = MibTableColumn
thdStatus = _ThdStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 4),
    _ThdStatus_Type()
)
thdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdStatus.setStatus("deprecated")
_ThdTemp_Type = TemperatureValue
_ThdTemp_Object = MibTableColumn
thdTemp = _ThdTemp_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 5),
    _ThdTemp_Type()
)
thdTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdTemp.setStatus("deprecated")
_ThdHumidity_Type = Gauge32
_ThdHumidity_Object = MibTableColumn
thdHumidity = _ThdHumidity_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 6),
    _ThdHumidity_Type()
)
thdHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdHumidity.setStatus("deprecated")
_ThdDewPoint_Type = TemperatureValue
_ThdDewPoint_Object = MibTableColumn
thdDewPoint = _ThdDewPoint_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 7),
    _ThdDewPoint_Type()
)
thdDewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdDewPoint.setStatus("deprecated")
_ThdTDUnits_Type = TemperatureUnits
_ThdTDUnits_Object = MibTableColumn
thdTDUnits = _ThdTDUnits_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 10, 1, 1, 8),
    _ThdTDUnits_Type()
)
thdTDUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thdTDUnits.setStatus("deprecated")
_LegacyPDU_ObjectIdentity = ObjectIdentity
legacyPDU = _LegacyPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99)
)
_PduBaseDeltaTable_Object = MibTable
pduBaseDeltaTable = _PduBaseDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1)
)
if mibBuilder.loadTexts:
    pduBaseDeltaTable.setStatus("deprecated")
_PduBaseDeltaEntry_Object = MibTableRow
pduBaseDeltaEntry = _PduBaseDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1)
)
pduBaseDeltaEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduBaseDeltaIndex"),
)
if mibBuilder.loadTexts:
    pduBaseDeltaEntry.setStatus("deprecated")


class _PduBaseDeltaIndex_Type(Unsigned32):
    """Custom type pduBaseDeltaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PduBaseDeltaIndex_Type.__name__ = "Unsigned32"
_PduBaseDeltaIndex_Object = MibTableColumn
pduBaseDeltaIndex = _PduBaseDeltaIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 1),
    _PduBaseDeltaIndex_Type()
)
pduBaseDeltaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduBaseDeltaIndex.setStatus("deprecated")
_PduBaseDeltaSerial_Type = DeviceSerial
_PduBaseDeltaSerial_Object = MibTableColumn
pduBaseDeltaSerial = _PduBaseDeltaSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 2),
    _PduBaseDeltaSerial_Type()
)
pduBaseDeltaSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaSerial.setStatus("deprecated")
_PduBaseDeltaLabel_Type = DeviceLabel
_PduBaseDeltaLabel_Object = MibTableColumn
pduBaseDeltaLabel = _PduBaseDeltaLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 3),
    _PduBaseDeltaLabel_Type()
)
pduBaseDeltaLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBaseDeltaLabel.setStatus("deprecated")
_PduBaseDeltaStatus_Type = DeviceStatus
_PduBaseDeltaStatus_Object = MibTableColumn
pduBaseDeltaStatus = _PduBaseDeltaStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 4),
    _PduBaseDeltaStatus_Type()
)
pduBaseDeltaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaStatus.setStatus("deprecated")
_PduBaseDeltaKWattHrsTotal_Type = Gauge32
_PduBaseDeltaKWattHrsTotal_Object = MibTableColumn
pduBaseDeltaKWattHrsTotal = _PduBaseDeltaKWattHrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 5),
    _PduBaseDeltaKWattHrsTotal_Type()
)
pduBaseDeltaKWattHrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaKWattHrsTotal.setStatus("deprecated")
_PduBaseDeltaRealPowerTotal_Type = Gauge32
_PduBaseDeltaRealPowerTotal_Object = MibTableColumn
pduBaseDeltaRealPowerTotal = _PduBaseDeltaRealPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 6),
    _PduBaseDeltaRealPowerTotal_Type()
)
pduBaseDeltaRealPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaRealPowerTotal.setStatus("deprecated")
_PduBaseDeltaAmpsA_Type = DeciAmps
_PduBaseDeltaAmpsA_Object = MibTableColumn
pduBaseDeltaAmpsA = _PduBaseDeltaAmpsA_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 7),
    _PduBaseDeltaAmpsA_Type()
)
pduBaseDeltaAmpsA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaAmpsA.setStatus("deprecated")
_PduBaseDeltaAmpsB_Type = DeciAmps
_PduBaseDeltaAmpsB_Object = MibTableColumn
pduBaseDeltaAmpsB = _PduBaseDeltaAmpsB_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 8),
    _PduBaseDeltaAmpsB_Type()
)
pduBaseDeltaAmpsB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaAmpsB.setStatus("deprecated")
_PduBaseDeltaAmpsC_Type = DeciAmps
_PduBaseDeltaAmpsC_Object = MibTableColumn
pduBaseDeltaAmpsC = _PduBaseDeltaAmpsC_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 1, 1, 9),
    _PduBaseDeltaAmpsC_Type()
)
pduBaseDeltaAmpsC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseDeltaAmpsC.setStatus("deprecated")
_PduBaseWyeTable_Object = MibTable
pduBaseWyeTable = _PduBaseWyeTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2)
)
if mibBuilder.loadTexts:
    pduBaseWyeTable.setStatus("deprecated")
_PduBaseWyeEntry_Object = MibTableRow
pduBaseWyeEntry = _PduBaseWyeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1)
)
pduBaseWyeEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduBaseWyeIndex"),
)
if mibBuilder.loadTexts:
    pduBaseWyeEntry.setStatus("deprecated")


class _PduBaseWyeIndex_Type(Unsigned32):
    """Custom type pduBaseWyeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PduBaseWyeIndex_Type.__name__ = "Unsigned32"
_PduBaseWyeIndex_Object = MibTableColumn
pduBaseWyeIndex = _PduBaseWyeIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 1),
    _PduBaseWyeIndex_Type()
)
pduBaseWyeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduBaseWyeIndex.setStatus("deprecated")
_PduBaseWyeSerial_Type = DeviceSerial
_PduBaseWyeSerial_Object = MibTableColumn
pduBaseWyeSerial = _PduBaseWyeSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 2),
    _PduBaseWyeSerial_Type()
)
pduBaseWyeSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseWyeSerial.setStatus("deprecated")
_PduBaseWyeLabel_Type = DeviceLabel
_PduBaseWyeLabel_Object = MibTableColumn
pduBaseWyeLabel = _PduBaseWyeLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 3),
    _PduBaseWyeLabel_Type()
)
pduBaseWyeLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduBaseWyeLabel.setStatus("deprecated")
_PduBaseWyeStatus_Type = DeviceStatus
_PduBaseWyeStatus_Object = MibTableColumn
pduBaseWyeStatus = _PduBaseWyeStatus_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 4),
    _PduBaseWyeStatus_Type()
)
pduBaseWyeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseWyeStatus.setStatus("deprecated")
_PduBaseWyeKWattHrsTotal_Type = Gauge32
_PduBaseWyeKWattHrsTotal_Object = MibTableColumn
pduBaseWyeKWattHrsTotal = _PduBaseWyeKWattHrsTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 5),
    _PduBaseWyeKWattHrsTotal_Type()
)
pduBaseWyeKWattHrsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseWyeKWattHrsTotal.setStatus("deprecated")
_PduBaseWyeRealPowerTotal_Type = Gauge32
_PduBaseWyeRealPowerTotal_Object = MibTableColumn
pduBaseWyeRealPowerTotal = _PduBaseWyeRealPowerTotal_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 6),
    _PduBaseWyeRealPowerTotal_Type()
)
pduBaseWyeRealPowerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseWyeRealPowerTotal.setStatus("deprecated")


class _PduBaseWyeChannelCount_Type(Unsigned32):
    """Custom type pduBaseWyeChannelCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PduBaseWyeChannelCount_Type.__name__ = "Unsigned32"
_PduBaseWyeChannelCount_Object = MibTableColumn
pduBaseWyeChannelCount = _PduBaseWyeChannelCount_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 2, 1, 7),
    _PduBaseWyeChannelCount_Type()
)
pduBaseWyeChannelCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduBaseWyeChannelCount.setStatus("deprecated")
_PduChannelDeltaTable_Object = MibTable
pduChannelDeltaTable = _PduChannelDeltaTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3)
)
if mibBuilder.loadTexts:
    pduChannelDeltaTable.setStatus("deprecated")
_PduChannelDeltaEntry_Object = MibTableRow
pduChannelDeltaEntry = _PduChannelDeltaEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1)
)
pduChannelDeltaEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduBaseDeltaIndex"),
    (0, "VERTIV-QUETZAL-MIB", "pduChannelDeltaID"),
)
if mibBuilder.loadTexts:
    pduChannelDeltaEntry.setStatus("deprecated")


class _PduChannelDeltaID_Type(Unsigned32):
    """Custom type pduChannelDeltaID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PduChannelDeltaID_Type.__name__ = "Unsigned32"
_PduChannelDeltaID_Object = MibTableColumn
pduChannelDeltaID = _PduChannelDeltaID_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 1),
    _PduChannelDeltaID_Type()
)
pduChannelDeltaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaID.setStatus("deprecated")
_PduChannelDeltaLabel_Type = DeviceLabel
_PduChannelDeltaLabel_Object = MibTableColumn
pduChannelDeltaLabel = _PduChannelDeltaLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 2),
    _PduChannelDeltaLabel_Type()
)
pduChannelDeltaLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduChannelDeltaLabel.setStatus("deprecated")
_PduChannelDeltaName_Type = DisplayString
_PduChannelDeltaName_Object = MibTableColumn
pduChannelDeltaName = _PduChannelDeltaName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 3),
    _PduChannelDeltaName_Type()
)
pduChannelDeltaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaName.setStatus("deprecated")
_PduChannelDeltaKWattHrs_Type = Gauge32
_PduChannelDeltaKWattHrs_Object = MibTableColumn
pduChannelDeltaKWattHrs = _PduChannelDeltaKWattHrs_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 4),
    _PduChannelDeltaKWattHrs_Type()
)
pduChannelDeltaKWattHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaKWattHrs.setStatus("deprecated")
_PduChannelDeltaVolts_Type = Gauge32
_PduChannelDeltaVolts_Object = MibTableColumn
pduChannelDeltaVolts = _PduChannelDeltaVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 5),
    _PduChannelDeltaVolts_Type()
)
pduChannelDeltaVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaVolts.setStatus("deprecated")
_PduChannelDeltaRealPower_Type = Gauge32
_PduChannelDeltaRealPower_Object = MibTableColumn
pduChannelDeltaRealPower = _PduChannelDeltaRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 7),
    _PduChannelDeltaRealPower_Type()
)
pduChannelDeltaRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaRealPower.setStatus("deprecated")
_PduChannelDeltaApparentPower_Type = Gauge32
_PduChannelDeltaApparentPower_Object = MibTableColumn
pduChannelDeltaApparentPower = _PduChannelDeltaApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 8),
    _PduChannelDeltaApparentPower_Type()
)
pduChannelDeltaApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaApparentPower.setStatus("deprecated")
_PduChannelDeltaPowerFactor_Type = Gauge32
_PduChannelDeltaPowerFactor_Object = MibTableColumn
pduChannelDeltaPowerFactor = _PduChannelDeltaPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 9),
    _PduChannelDeltaPowerFactor_Type()
)
pduChannelDeltaPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaPowerFactor.setStatus("deprecated")
_PduChannelDeltaAmps_Type = DeciAmps
_PduChannelDeltaAmps_Object = MibTableColumn
pduChannelDeltaAmps = _PduChannelDeltaAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 3, 1, 10),
    _PduChannelDeltaAmps_Type()
)
pduChannelDeltaAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelDeltaAmps.setStatus("deprecated")
_PduChannelWyeTable_Object = MibTable
pduChannelWyeTable = _PduChannelWyeTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4)
)
if mibBuilder.loadTexts:
    pduChannelWyeTable.setStatus("deprecated")
_PduChannelWyeEntry_Object = MibTableRow
pduChannelWyeEntry = _PduChannelWyeEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1)
)
pduChannelWyeEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduBaseWyeIndex"),
    (0, "VERTIV-QUETZAL-MIB", "pduChannelWyeID"),
)
if mibBuilder.loadTexts:
    pduChannelWyeEntry.setStatus("deprecated")


class _PduChannelWyeID_Type(Unsigned32):
    """Custom type pduChannelWyeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PduChannelWyeID_Type.__name__ = "Unsigned32"
_PduChannelWyeID_Object = MibTableColumn
pduChannelWyeID = _PduChannelWyeID_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 1),
    _PduChannelWyeID_Type()
)
pduChannelWyeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeID.setStatus("deprecated")
_PduChannelWyeLabel_Type = DeviceLabel
_PduChannelWyeLabel_Object = MibTableColumn
pduChannelWyeLabel = _PduChannelWyeLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 2),
    _PduChannelWyeLabel_Type()
)
pduChannelWyeLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduChannelWyeLabel.setStatus("deprecated")
_PduChannelWyeName_Type = DisplayString
_PduChannelWyeName_Object = MibTableColumn
pduChannelWyeName = _PduChannelWyeName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 3),
    _PduChannelWyeName_Type()
)
pduChannelWyeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeName.setStatus("deprecated")
_PduChannelWyeKWattHrs_Type = Gauge32
_PduChannelWyeKWattHrs_Object = MibTableColumn
pduChannelWyeKWattHrs = _PduChannelWyeKWattHrs_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 4),
    _PduChannelWyeKWattHrs_Type()
)
pduChannelWyeKWattHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeKWattHrs.setStatus("deprecated")
_PduChannelWyeVolts_Type = Gauge32
_PduChannelWyeVolts_Object = MibTableColumn
pduChannelWyeVolts = _PduChannelWyeVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 5),
    _PduChannelWyeVolts_Type()
)
pduChannelWyeVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeVolts.setStatus("deprecated")
_PduChannelWyeAmps_Type = DeciAmps
_PduChannelWyeAmps_Object = MibTableColumn
pduChannelWyeAmps = _PduChannelWyeAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 7),
    _PduChannelWyeAmps_Type()
)
pduChannelWyeAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeAmps.setStatus("deprecated")
_PduChannelWyeRealPower_Type = Gauge32
_PduChannelWyeRealPower_Object = MibTableColumn
pduChannelWyeRealPower = _PduChannelWyeRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 9),
    _PduChannelWyeRealPower_Type()
)
pduChannelWyeRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeRealPower.setStatus("deprecated")
_PduChannelWyeApparentPower_Type = Gauge32
_PduChannelWyeApparentPower_Object = MibTableColumn
pduChannelWyeApparentPower = _PduChannelWyeApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 10),
    _PduChannelWyeApparentPower_Type()
)
pduChannelWyeApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyeApparentPower.setStatus("deprecated")
_PduChannelWyePowerFactor_Type = Gauge32
_PduChannelWyePowerFactor_Object = MibTableColumn
pduChannelWyePowerFactor = _PduChannelWyePowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 4, 1, 11),
    _PduChannelWyePowerFactor_Type()
)
pduChannelWyePowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduChannelWyePowerFactor.setStatus("deprecated")
_PduGroupTable_Object = MibTable
pduGroupTable = _PduGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5)
)
if mibBuilder.loadTexts:
    pduGroupTable.setStatus("deprecated")
_PduGroupEntry_Object = MibTableRow
pduGroupEntry = _PduGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1)
)
pduGroupEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduGroupIndex"),
    (0, "VERTIV-QUETZAL-MIB", "pduGroupID"),
)
if mibBuilder.loadTexts:
    pduGroupEntry.setStatus("deprecated")


class _PduGroupIndex_Type(Unsigned32):
    """Custom type pduGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PduGroupIndex_Type.__name__ = "Unsigned32"
_PduGroupIndex_Object = MibTableColumn
pduGroupIndex = _PduGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 1),
    _PduGroupIndex_Type()
)
pduGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduGroupIndex.setStatus("deprecated")
_PduGroupSerial_Type = DeviceSerial
_PduGroupSerial_Object = MibTableColumn
pduGroupSerial = _PduGroupSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 2),
    _PduGroupSerial_Type()
)
pduGroupSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupSerial.setStatus("deprecated")


class _PduGroupID_Type(Unsigned32):
    """Custom type pduGroupID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_PduGroupID_Type.__name__ = "Unsigned32"
_PduGroupID_Object = MibTableColumn
pduGroupID = _PduGroupID_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 3),
    _PduGroupID_Type()
)
pduGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupID.setStatus("deprecated")
_PduGroupLabel_Type = DeviceLabel
_PduGroupLabel_Object = MibTableColumn
pduGroupLabel = _PduGroupLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 4),
    _PduGroupLabel_Type()
)
pduGroupLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduGroupLabel.setStatus("deprecated")
_PduGroupName_Type = DisplayString
_PduGroupName_Object = MibTableColumn
pduGroupName = _PduGroupName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 5),
    _PduGroupName_Type()
)
pduGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupName.setStatus("deprecated")
_PduGroupAmps_Type = DeciAmps
_PduGroupAmps_Object = MibTableColumn
pduGroupAmps = _PduGroupAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 6),
    _PduGroupAmps_Type()
)
pduGroupAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupAmps.setStatus("deprecated")
_PduGroupApparentPower_Type = Gauge32
_PduGroupApparentPower_Object = MibTableColumn
pduGroupApparentPower = _PduGroupApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 8),
    _PduGroupApparentPower_Type()
)
pduGroupApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupApparentPower.setStatus("deprecated")
_PduGroupPowerFactor_Type = Gauge32
_PduGroupPowerFactor_Object = MibTableColumn
pduGroupPowerFactor = _PduGroupPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 9),
    _PduGroupPowerFactor_Type()
)
pduGroupPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupPowerFactor.setStatus("deprecated")
_PduGroupRealPower_Type = Gauge32
_PduGroupRealPower_Object = MibTableColumn
pduGroupRealPower = _PduGroupRealPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 10),
    _PduGroupRealPower_Type()
)
pduGroupRealPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupRealPower.setStatus("deprecated")
_PduGroupVolts_Type = Gauge32
_PduGroupVolts_Object = MibTableColumn
pduGroupVolts = _PduGroupVolts_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 11),
    _PduGroupVolts_Type()
)
pduGroupVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupVolts.setStatus("deprecated")
_PduGroupWattHours_Type = Gauge32
_PduGroupWattHours_Object = MibTableColumn
pduGroupWattHours = _PduGroupWattHours_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 5, 1, 13),
    _PduGroupWattHours_Type()
)
pduGroupWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduGroupWattHours.setStatus("deprecated")
_PduOutletMainTable_Object = MibTable
pduOutletMainTable = _PduOutletMainTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6)
)
if mibBuilder.loadTexts:
    pduOutletMainTable.setStatus("deprecated")
_PduOutletMainEntry_Object = MibTableRow
pduOutletMainEntry = _PduOutletMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1)
)
pduOutletMainEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduOutletMainIndex"),
    (0, "VERTIV-QUETZAL-MIB", "pduOutletMainID"),
)
if mibBuilder.loadTexts:
    pduOutletMainEntry.setStatus("deprecated")


class _PduOutletMainIndex_Type(Unsigned32):
    """Custom type pduOutletMainIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PduOutletMainIndex_Type.__name__ = "Unsigned32"
_PduOutletMainIndex_Object = MibTableColumn
pduOutletMainIndex = _PduOutletMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 1),
    _PduOutletMainIndex_Type()
)
pduOutletMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMainIndex.setStatus("deprecated")
_PduOutletMainSerial_Type = DeviceSerial
_PduOutletMainSerial_Object = MibTableColumn
pduOutletMainSerial = _PduOutletMainSerial_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 2),
    _PduOutletMainSerial_Type()
)
pduOutletMainSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMainSerial.setStatus("deprecated")


class _PduOutletMainID_Type(Unsigned32):
    """Custom type pduOutletMainID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PduOutletMainID_Type.__name__ = "Unsigned32"
_PduOutletMainID_Object = MibTableColumn
pduOutletMainID = _PduOutletMainID_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 3),
    _PduOutletMainID_Type()
)
pduOutletMainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMainID.setStatus("deprecated")
_PduOutletMainLabel_Type = DeviceLabel
_PduOutletMainLabel_Object = MibTableColumn
pduOutletMainLabel = _PduOutletMainLabel_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 4),
    _PduOutletMainLabel_Type()
)
pduOutletMainLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMainLabel.setStatus("deprecated")
_PduOutletMainName_Type = DisplayString
_PduOutletMainName_Object = MibTableColumn
pduOutletMainName = _PduOutletMainName_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 5),
    _PduOutletMainName_Type()
)
pduOutletMainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMainName.setStatus("deprecated")
_PduOutletMainGroup_Type = DisplayString
_PduOutletMainGroup_Object = MibTableColumn
pduOutletMainGroup = _PduOutletMainGroup_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 6),
    _PduOutletMainGroup_Type()
)
pduOutletMainGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMainGroup.setStatus("deprecated")
_PduOutletMainURL_Type = DisplayString
_PduOutletMainURL_Object = MibTableColumn
pduOutletMainURL = _PduOutletMainURL_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 6, 1, 7),
    _PduOutletMainURL_Type()
)
pduOutletMainURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMainURL.setStatus("deprecated")
_PduOutletSwitchTable_Object = MibTable
pduOutletSwitchTable = _PduOutletSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7)
)
if mibBuilder.loadTexts:
    pduOutletSwitchTable.setStatus("deprecated")
_PduOutletSwitchEntry_Object = MibTableRow
pduOutletSwitchEntry = _PduOutletSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1)
)
pduOutletSwitchEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduOutletMainIndex"),
    (0, "VERTIV-QUETZAL-MIB", "pduOutletMainID"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchEntry.setStatus("deprecated")


class _PduOutletSwitchState_Type(Integer32):
    """Custom type pduOutletSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outletOff", 0),
          ("outletOn", 1),
          ("outletError", 2))
    )


_PduOutletSwitchState_Type.__name__ = "Integer32"
_PduOutletSwitchState_Object = MibTableColumn
pduOutletSwitchState = _PduOutletSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 1),
    _PduOutletSwitchState_Type()
)
pduOutletSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchState.setStatus("deprecated")
_PduOutletSwitchStateChangeTime_Type = Unsigned32
_PduOutletSwitchStateChangeTime_Object = MibTableColumn
pduOutletSwitchStateChangeTime = _PduOutletSwitchStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 2),
    _PduOutletSwitchStateChangeTime_Type()
)
pduOutletSwitchStateChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchStateChangeTime.setStatus("deprecated")


class _PduOutletSwitchCurrentAction_Type(Integer32):
    """Custom type pduOutletSwitchCurrentAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("reboot", 2),
          ("startUp", 3),
          ("other", 4))
    )


_PduOutletSwitchCurrentAction_Type.__name__ = "Integer32"
_PduOutletSwitchCurrentAction_Object = MibTableColumn
pduOutletSwitchCurrentAction = _PduOutletSwitchCurrentAction_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 3),
    _PduOutletSwitchCurrentAction_Type()
)
pduOutletSwitchCurrentAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchCurrentAction.setStatus("deprecated")
_PduOutletSwitchOnDelay_Type = Unsigned32
_PduOutletSwitchOnDelay_Object = MibTableColumn
pduOutletSwitchOnDelay = _PduOutletSwitchOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 4),
    _PduOutletSwitchOnDelay_Type()
)
pduOutletSwitchOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchOnDelay.setStatus("deprecated")
_PduOutletSwitchOffDelay_Type = Unsigned32
_PduOutletSwitchOffDelay_Object = MibTableColumn
pduOutletSwitchOffDelay = _PduOutletSwitchOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 5),
    _PduOutletSwitchOffDelay_Type()
)
pduOutletSwitchOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchOffDelay.setStatus("deprecated")
_PduOutletSwitchRebootDelay_Type = Unsigned32
_PduOutletSwitchRebootDelay_Object = MibTableColumn
pduOutletSwitchRebootDelay = _PduOutletSwitchRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 6),
    _PduOutletSwitchRebootDelay_Type()
)
pduOutletSwitchRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchRebootDelay.setStatus("deprecated")
_PduOutletSwitchRebootHold_Type = Unsigned32
_PduOutletSwitchRebootHold_Object = MibTableColumn
pduOutletSwitchRebootHold = _PduOutletSwitchRebootHold_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 7),
    _PduOutletSwitchRebootHold_Type()
)
pduOutletSwitchRebootHold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchRebootHold.setStatus("deprecated")


class _PduOutletSwitchStartupAction_Type(Integer32):
    """Custom type pduOutletSwitchStartupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("startOff", 0),
          ("startOn", 1),
          ("lastKnown", 2))
    )


_PduOutletSwitchStartupAction_Type.__name__ = "Integer32"
_PduOutletSwitchStartupAction_Object = MibTableColumn
pduOutletSwitchStartupAction = _PduOutletSwitchStartupAction_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 8),
    _PduOutletSwitchStartupAction_Type()
)
pduOutletSwitchStartupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchStartupAction.setStatus("deprecated")
_PduOutletSwitchStartupStateDelay_Type = Unsigned32
_PduOutletSwitchStartupStateDelay_Object = MibTableColumn
pduOutletSwitchStartupStateDelay = _PduOutletSwitchStartupStateDelay_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 9),
    _PduOutletSwitchStartupStateDelay_Type()
)
pduOutletSwitchStartupStateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchStartupStateDelay.setStatus("deprecated")


class _PduOutletSwitchControl_Type(Integer32):
    """Custom type pduOutletSwitchControl based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cancelActions", 1),
          ("onNoDelay", 2),
          ("onDelay", 3),
          ("offNoDelay", 4),
          ("offDelay", 5),
          ("rebootNoDelay", 6),
          ("rebootDelay", 7))
    )


_PduOutletSwitchControl_Type.__name__ = "Integer32"
_PduOutletSwitchControl_Object = MibTableColumn
pduOutletSwitchControl = _PduOutletSwitchControl_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 7, 1, 10),
    _PduOutletSwitchControl_Type()
)
pduOutletSwitchControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchControl.setStatus("deprecated")
_PduOutletMeterTable_Object = MibTable
pduOutletMeterTable = _PduOutletMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 8)
)
if mibBuilder.loadTexts:
    pduOutletMeterTable.setStatus("deprecated")
_PduOutletMeterEntry_Object = MibTableRow
pduOutletMeterEntry = _PduOutletMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 8, 1)
)
pduOutletMeterEntry.setIndexNames(
    (0, "VERTIV-QUETZAL-MIB", "pduOutletMainIndex"),
    (0, "VERTIV-QUETZAL-MIB", "pduOutletMainID"),
)
if mibBuilder.loadTexts:
    pduOutletMeterEntry.setStatus("deprecated")
_PduOutletMeterKWattHrs_Type = Gauge32
_PduOutletMeterKWattHrs_Object = MibTableColumn
pduOutletMeterKWattHrs = _PduOutletMeterKWattHrs_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 8, 1, 1),
    _PduOutletMeterKWattHrs_Type()
)
pduOutletMeterKWattHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterKWattHrs.setStatus("deprecated")
_PduOutletMeterAmps_Type = DeciAmps
_PduOutletMeterAmps_Object = MibTableColumn
pduOutletMeterAmps = _PduOutletMeterAmps_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 8, 1, 2),
    _PduOutletMeterAmps_Type()
)
pduOutletMeterAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterAmps.setStatus("deprecated")
_PduOutletMeterPower_Type = Gauge32
_PduOutletMeterPower_Object = MibTableColumn
pduOutletMeterPower = _PduOutletMeterPower_Object(
    (1, 3, 6, 1, 4, 1, 21239, 6, 1, 99, 8, 1, 3),
    _PduOutletMeterPower_Type()
)
pduOutletMeterPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeterPower.setStatus("deprecated")
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42)
)
_Identity_ObjectIdentity = ObjectIdentity
identity = _Identity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42, 1)
)
_R05_ObjectIdentity = ObjectIdentity
r05 = _R05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42, 1, 15)
)
if mibBuilder.loadTexts:
    r05.setStatus("current")
_I03_ObjectIdentity = ObjectIdentity
i03 = _I03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21239, 42, 1, 53)
)
if mibBuilder.loadTexts:
    i03.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTIV-QUETZAL-MIB",
    **{"DeviceSerial": DeviceSerial,
       "DeviceStatus": DeviceStatus,
       "DeviceLabel": DeviceLabel,
       "TemperatureUnits": TemperatureUnits,
       "TemperatureValue": TemperatureValue,
       "DeciAmps": DeciAmps,
       "vertiv": vertiv,
       "quetzal": quetzal,
       "devices": devices,
       "rtafhd3": rtafhd3,
       "rtafhd3Table": rtafhd3Table,
       "rtafhd3Entry": rtafhd3Entry,
       "rtafhd3Index": rtafhd3Index,
       "rtafhd3Serial": rtafhd3Serial,
       "rtafhd3Label": rtafhd3Label,
       "rtafhd3Status": rtafhd3Status,
       "rtafhd3Airflow": rtafhd3Airflow,
       "rtafhd3Humidity": rtafhd3Humidity,
       "rtafhd3Temp": rtafhd3Temp,
       "rtafhd3DewPoint": rtafhd3DewPoint,
       "rtafhd3TDUnits": rtafhd3TDUnits,
       "rt": rt,
       "rtTable": rtTable,
       "rtEntry": rtEntry,
       "rtIndex": rtIndex,
       "rtSerial": rtSerial,
       "rtLabel": rtLabel,
       "rtStatus": rtStatus,
       "rtTemp": rtTemp,
       "rtUnits": rtUnits,
       "t3hd": t3hd,
       "t3hdTable": t3hdTable,
       "t3hdEntry": t3hdEntry,
       "t3hdIndex": t3hdIndex,
       "t3hdSerial": t3hdSerial,
       "t3hdLabel": t3hdLabel,
       "t3hdStatus": t3hdStatus,
       "t3hdMainLabel": t3hdMainLabel,
       "t3hdMainTemp": t3hdMainTemp,
       "t3hdMainHumidity": t3hdMainHumidity,
       "t3hdMainDewPoint": t3hdMainDewPoint,
       "t3hdExt1Status": t3hdExt1Status,
       "t3hdExt1Label": t3hdExt1Label,
       "t3hdExt1Temp": t3hdExt1Temp,
       "t3hdExt2Status": t3hdExt2Status,
       "t3hdExt2Label": t3hdExt2Label,
       "t3hdExt2Temp": t3hdExt2Temp,
       "t3hdTDUnits": t3hdTDUnits,
       "thd": thd,
       "thdTable": thdTable,
       "thdEntry": thdEntry,
       "thdIndex": thdIndex,
       "thdSerial": thdSerial,
       "thdLabel": thdLabel,
       "thdStatus": thdStatus,
       "thdTemp": thdTemp,
       "thdHumidity": thdHumidity,
       "thdDewPoint": thdDewPoint,
       "thdTDUnits": thdTDUnits,
       "legacyPDU": legacyPDU,
       "pduBaseDeltaTable": pduBaseDeltaTable,
       "pduBaseDeltaEntry": pduBaseDeltaEntry,
       "pduBaseDeltaIndex": pduBaseDeltaIndex,
       "pduBaseDeltaSerial": pduBaseDeltaSerial,
       "pduBaseDeltaLabel": pduBaseDeltaLabel,
       "pduBaseDeltaStatus": pduBaseDeltaStatus,
       "pduBaseDeltaKWattHrsTotal": pduBaseDeltaKWattHrsTotal,
       "pduBaseDeltaRealPowerTotal": pduBaseDeltaRealPowerTotal,
       "pduBaseDeltaAmpsA": pduBaseDeltaAmpsA,
       "pduBaseDeltaAmpsB": pduBaseDeltaAmpsB,
       "pduBaseDeltaAmpsC": pduBaseDeltaAmpsC,
       "pduBaseWyeTable": pduBaseWyeTable,
       "pduBaseWyeEntry": pduBaseWyeEntry,
       "pduBaseWyeIndex": pduBaseWyeIndex,
       "pduBaseWyeSerial": pduBaseWyeSerial,
       "pduBaseWyeLabel": pduBaseWyeLabel,
       "pduBaseWyeStatus": pduBaseWyeStatus,
       "pduBaseWyeKWattHrsTotal": pduBaseWyeKWattHrsTotal,
       "pduBaseWyeRealPowerTotal": pduBaseWyeRealPowerTotal,
       "pduBaseWyeChannelCount": pduBaseWyeChannelCount,
       "pduChannelDeltaTable": pduChannelDeltaTable,
       "pduChannelDeltaEntry": pduChannelDeltaEntry,
       "pduChannelDeltaID": pduChannelDeltaID,
       "pduChannelDeltaLabel": pduChannelDeltaLabel,
       "pduChannelDeltaName": pduChannelDeltaName,
       "pduChannelDeltaKWattHrs": pduChannelDeltaKWattHrs,
       "pduChannelDeltaVolts": pduChannelDeltaVolts,
       "pduChannelDeltaRealPower": pduChannelDeltaRealPower,
       "pduChannelDeltaApparentPower": pduChannelDeltaApparentPower,
       "pduChannelDeltaPowerFactor": pduChannelDeltaPowerFactor,
       "pduChannelDeltaAmps": pduChannelDeltaAmps,
       "pduChannelWyeTable": pduChannelWyeTable,
       "pduChannelWyeEntry": pduChannelWyeEntry,
       "pduChannelWyeID": pduChannelWyeID,
       "pduChannelWyeLabel": pduChannelWyeLabel,
       "pduChannelWyeName": pduChannelWyeName,
       "pduChannelWyeKWattHrs": pduChannelWyeKWattHrs,
       "pduChannelWyeVolts": pduChannelWyeVolts,
       "pduChannelWyeAmps": pduChannelWyeAmps,
       "pduChannelWyeRealPower": pduChannelWyeRealPower,
       "pduChannelWyeApparentPower": pduChannelWyeApparentPower,
       "pduChannelWyePowerFactor": pduChannelWyePowerFactor,
       "pduGroupTable": pduGroupTable,
       "pduGroupEntry": pduGroupEntry,
       "pduGroupIndex": pduGroupIndex,
       "pduGroupSerial": pduGroupSerial,
       "pduGroupID": pduGroupID,
       "pduGroupLabel": pduGroupLabel,
       "pduGroupName": pduGroupName,
       "pduGroupAmps": pduGroupAmps,
       "pduGroupApparentPower": pduGroupApparentPower,
       "pduGroupPowerFactor": pduGroupPowerFactor,
       "pduGroupRealPower": pduGroupRealPower,
       "pduGroupVolts": pduGroupVolts,
       "pduGroupWattHours": pduGroupWattHours,
       "pduOutletMainTable": pduOutletMainTable,
       "pduOutletMainEntry": pduOutletMainEntry,
       "pduOutletMainIndex": pduOutletMainIndex,
       "pduOutletMainSerial": pduOutletMainSerial,
       "pduOutletMainID": pduOutletMainID,
       "pduOutletMainLabel": pduOutletMainLabel,
       "pduOutletMainName": pduOutletMainName,
       "pduOutletMainGroup": pduOutletMainGroup,
       "pduOutletMainURL": pduOutletMainURL,
       "pduOutletSwitchTable": pduOutletSwitchTable,
       "pduOutletSwitchEntry": pduOutletSwitchEntry,
       "pduOutletSwitchState": pduOutletSwitchState,
       "pduOutletSwitchStateChangeTime": pduOutletSwitchStateChangeTime,
       "pduOutletSwitchCurrentAction": pduOutletSwitchCurrentAction,
       "pduOutletSwitchOnDelay": pduOutletSwitchOnDelay,
       "pduOutletSwitchOffDelay": pduOutletSwitchOffDelay,
       "pduOutletSwitchRebootDelay": pduOutletSwitchRebootDelay,
       "pduOutletSwitchRebootHold": pduOutletSwitchRebootHold,
       "pduOutletSwitchStartupAction": pduOutletSwitchStartupAction,
       "pduOutletSwitchStartupStateDelay": pduOutletSwitchStartupStateDelay,
       "pduOutletSwitchControl": pduOutletSwitchControl,
       "pduOutletMeterTable": pduOutletMeterTable,
       "pduOutletMeterEntry": pduOutletMeterEntry,
       "pduOutletMeterKWattHrs": pduOutletMeterKWattHrs,
       "pduOutletMeterAmps": pduOutletMeterAmps,
       "pduOutletMeterPower": pduOutletMeterPower,
       "common": common,
       "identity": identity,
       "r05": r05,
       "i03": i03}
)
