# SNMP MIB module (CNM-SENSORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/s30labs_34225/CNM-SENSORS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:09:28 2025
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S30labs_ObjectIdentity = ObjectIdentity
s30labs = _S30labs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225)
)
_S30Products_ObjectIdentity = ObjectIdentity
s30Products = _S30Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 99)
)
_CnmSensorTH2_ObjectIdentity = ObjectIdentity
cnmSensorTH2 = _CnmSensorTH2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 99, 1)
)
_CnmSensors_ObjectIdentity = ObjectIdentity
cnmSensors = _CnmSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 200)
)
_CnmSensorsT_ObjectIdentity = ObjectIdentity
cnmSensorsT = _CnmSensorsT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 200, 1)
)
_CnmSensorsTH_ObjectIdentity = ObjectIdentity
cnmSensorsTH = _CnmSensorsTH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2)
)
_CnmSensorsTHA_ObjectIdentity = ObjectIdentity
cnmSensorsTHA = _CnmSensorsTHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 1)
)
_CnmSensorTH01AModel_Type = DisplayString
_CnmSensorTH01AModel_Object = MibScalar
cnmSensorTH01AModel = _CnmSensorTH01AModel_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 1, 1),
    _CnmSensorTH01AModel_Type()
)
cnmSensorTH01AModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01AModel.setStatus("current")


class _CnmSensorTH01AStatus_Type(Integer32):
    """Custom type cnmSensorTH01AStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("error", 1))
    )


_CnmSensorTH01AStatus_Type.__name__ = "Integer32"
_CnmSensorTH01AStatus_Object = MibScalar
cnmSensorTH01AStatus = _CnmSensorTH01AStatus_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 1, 2),
    _CnmSensorTH01AStatus_Type()
)
cnmSensorTH01AStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01AStatus.setStatus("current")


class _CnmSensorTH01ATemperature_Type(Integer32):
    """Custom type cnmSensorTH01ATemperature based on Integer32"""
    defaultValue = 0


_CnmSensorTH01ATemperature_Type.__name__ = "Integer32"
_CnmSensorTH01ATemperature_Object = MibScalar
cnmSensorTH01ATemperature = _CnmSensorTH01ATemperature_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 1, 3),
    _CnmSensorTH01ATemperature_Type()
)
cnmSensorTH01ATemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01ATemperature.setStatus("current")


class _CnmSensorTH01AHumidity_Type(Integer32):
    """Custom type cnmSensorTH01AHumidity based on Integer32"""
    defaultValue = 0


_CnmSensorTH01AHumidity_Type.__name__ = "Integer32"
_CnmSensorTH01AHumidity_Object = MibScalar
cnmSensorTH01AHumidity = _CnmSensorTH01AHumidity_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 1, 4),
    _CnmSensorTH01AHumidity_Type()
)
cnmSensorTH01AHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01AHumidity.setStatus("current")
_CnmSensorsTHB_ObjectIdentity = ObjectIdentity
cnmSensorsTHB = _CnmSensorsTHB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 2)
)
_CnmSensorTH01BModel_Type = DisplayString
_CnmSensorTH01BModel_Object = MibScalar
cnmSensorTH01BModel = _CnmSensorTH01BModel_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 2, 1),
    _CnmSensorTH01BModel_Type()
)
cnmSensorTH01BModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01BModel.setStatus("current")


class _CnmSensorTH01BStatus_Type(Integer32):
    """Custom type cnmSensorTH01BStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("error", 1))
    )


_CnmSensorTH01BStatus_Type.__name__ = "Integer32"
_CnmSensorTH01BStatus_Object = MibScalar
cnmSensorTH01BStatus = _CnmSensorTH01BStatus_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 2, 2),
    _CnmSensorTH01BStatus_Type()
)
cnmSensorTH01BStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01BStatus.setStatus("current")


class _CnmSensorTH01BTemperature_Type(Integer32):
    """Custom type cnmSensorTH01BTemperature based on Integer32"""
    defaultValue = 0


_CnmSensorTH01BTemperature_Type.__name__ = "Integer32"
_CnmSensorTH01BTemperature_Object = MibScalar
cnmSensorTH01BTemperature = _CnmSensorTH01BTemperature_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 2, 3),
    _CnmSensorTH01BTemperature_Type()
)
cnmSensorTH01BTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01BTemperature.setStatus("current")


class _CnmSensorTH01BHumidity_Type(Integer32):
    """Custom type cnmSensorTH01BHumidity based on Integer32"""
    defaultValue = 0


_CnmSensorTH01BHumidity_Type.__name__ = "Integer32"
_CnmSensorTH01BHumidity_Object = MibScalar
cnmSensorTH01BHumidity = _CnmSensorTH01BHumidity_Object(
    (1, 3, 6, 1, 4, 1, 34225, 200, 2, 2, 4),
    _CnmSensorTH01BHumidity_Type()
)
cnmSensorTH01BHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnmSensorTH01BHumidity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CNM-SENSORS-MIB",
    **{"DisplayString": DisplayString,
       "s30labs": s30labs,
       "s30Products": s30Products,
       "cnmSensorTH2": cnmSensorTH2,
       "cnmSensors": cnmSensors,
       "cnmSensorsT": cnmSensorsT,
       "cnmSensorsTH": cnmSensorsTH,
       "cnmSensorsTHA": cnmSensorsTHA,
       "cnmSensorTH01AModel": cnmSensorTH01AModel,
       "cnmSensorTH01AStatus": cnmSensorTH01AStatus,
       "cnmSensorTH01ATemperature": cnmSensorTH01ATemperature,
       "cnmSensorTH01AHumidity": cnmSensorTH01AHumidity,
       "cnmSensorsTHB": cnmSensorsTHB,
       "cnmSensorTH01BModel": cnmSensorTH01BModel,
       "cnmSensorTH01BStatus": cnmSensorTH01BStatus,
       "cnmSensorTH01BTemperature": cnmSensorTH01BTemperature,
       "cnmSensorTH01BHumidity": cnmSensorTH01BHumidity}
)
