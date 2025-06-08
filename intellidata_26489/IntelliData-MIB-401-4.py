# SNMP MIB module (IntelliData-MIB-401-4) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/intellidata_26489/IntelliData-MIB-401-4.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:49:33 2025
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IntelliData_ObjectIdentity = ObjectIdentity
intelliData = _IntelliData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26489)
)
_IdsDevices_ObjectIdentity = ObjectIdentity
idsDevices = _IdsDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26489, 1)
)
_IdsIdent_ObjectIdentity = ObjectIdentity
idsIdent = _IdsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26489, 1, 1)
)
_IdsIdentFirmwareRev_Type = DisplayString
_IdsIdentFirmwareRev_Object = MibScalar
idsIdentFirmwareRev = _IdsIdentFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 26489, 1, 1, 1),
    _IdsIdentFirmwareRev_Type()
)
idsIdentFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIdentFirmwareRev.setStatus("mandatory")
_IdsIdentSerialNumber_Type = Integer32
_IdsIdentSerialNumber_Object = MibScalar
idsIdentSerialNumber = _IdsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 26489, 1, 1, 2),
    _IdsIdentSerialNumber_Type()
)
idsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsIdentSerialNumber.setStatus("mandatory")


class _IdsIdentUnitName_Type(DisplayString):
    """Custom type idsIdentUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_IdsIdentUnitName_Type.__name__ = "DisplayString"
_IdsIdentUnitName_Object = MibScalar
idsIdentUnitName = _IdsIdentUnitName_Object(
    (1, 3, 6, 1, 4, 1, 26489, 1, 1, 3),
    _IdsIdentUnitName_Type()
)
idsIdentUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idsIdentUnitName.setStatus("mandatory")
_IdsArgs_ObjectIdentity = ObjectIdentity
idsArgs = _IdsArgs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 26489, 3)
)
_IdsArgsLocation_Type = DisplayString
_IdsArgsLocation_Object = MibScalar
idsArgsLocation = _IdsArgsLocation_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 1),
    _IdsArgsLocation_Type()
)
idsArgsLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsLocation.setStatus("mandatory")
_IdsArgsFeed_Type = DisplayString
_IdsArgsFeed_Object = MibScalar
idsArgsFeed = _IdsArgsFeed_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 2),
    _IdsArgsFeed_Type()
)
idsArgsFeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsFeed.setStatus("mandatory")
_IdsArgsCurrent_Type = Integer32
_IdsArgsCurrent_Object = MibScalar
idsArgsCurrent = _IdsArgsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 3),
    _IdsArgsCurrent_Type()
)
idsArgsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsCurrent.setStatus("mandatory")
_IdsArgsTemperature_Type = Integer32
_IdsArgsTemperature_Object = MibScalar
idsArgsTemperature = _IdsArgsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 4),
    _IdsArgsTemperature_Type()
)
idsArgsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsTemperature.setStatus("mandatory")
_IdsArgsHumidity_Type = Integer32
_IdsArgsHumidity_Object = MibScalar
idsArgsHumidity = _IdsArgsHumidity_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 5),
    _IdsArgsHumidity_Type()
)
idsArgsHumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsHumidity.setStatus("mandatory")
_IdsArgsInteger_Type = Integer32
_IdsArgsInteger_Object = MibScalar
idsArgsInteger = _IdsArgsInteger_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 6),
    _IdsArgsInteger_Type()
)
idsArgsInteger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsInteger.setStatus("mandatory")
_IdsArgsIpAddress_Type = IpAddress
_IdsArgsIpAddress_Object = MibScalar
idsArgsIpAddress = _IdsArgsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 7),
    _IdsArgsIpAddress_Type()
)
idsArgsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsIpAddress.setStatus("mandatory")
_IdsArgsString_Type = DisplayString
_IdsArgsString_Object = MibScalar
idsArgsString = _IdsArgsString_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 8),
    _IdsArgsString_Type()
)
idsArgsString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsString.setStatus("mandatory")
_IdsArgsGauge_Type = Gauge32
_IdsArgsGauge_Object = MibScalar
idsArgsGauge = _IdsArgsGauge_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 9),
    _IdsArgsGauge_Type()
)
idsArgsGauge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsGauge.setStatus("mandatory")
_IdsArgsTimeTicks_Type = TimeTicks
_IdsArgsTimeTicks_Object = MibScalar
idsArgsTimeTicks = _IdsArgsTimeTicks_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 10),
    _IdsArgsTimeTicks_Type()
)
idsArgsTimeTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsTimeTicks.setStatus("mandatory")
_IdsArgsOutletIndex_Type = Integer32
_IdsArgsOutletIndex_Object = MibScalar
idsArgsOutletIndex = _IdsArgsOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 26489, 3, 12),
    _IdsArgsOutletIndex_Type()
)
idsArgsOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idsArgsOutletIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects

communicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 2)
)
communicationLost.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsTimeTicks"))
)
if mibBuilder.loadTexts:
    communicationLost.setStatus(
        ""
    )

communicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 3)
)
communicationEstablished.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsTimeTicks"))
)
if mibBuilder.loadTexts:
    communicationEstablished.setStatus(
        ""
    )

outletReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 4)
)
outletReboot.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsOutletIndex"))
)
if mibBuilder.loadTexts:
    outletReboot.setStatus(
        ""
    )

currentThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 5)
)
currentThresholdViolation.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsCurrent"))
)
if mibBuilder.loadTexts:
    currentThresholdViolation.setStatus(
        ""
    )

currentThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 6)
)
currentThresholdViolationCleared.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsCurrent"))
)
if mibBuilder.loadTexts:
    currentThresholdViolationCleared.setStatus(
        ""
    )

currentUnderThresholdViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 7)
)
currentUnderThresholdViolation.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsCurrent"))
)
if mibBuilder.loadTexts:
    currentUnderThresholdViolation.setStatus(
        ""
    )

currentUnderThresholdViolationCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 8)
)
currentUnderThresholdViolationCleared.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsCurrent"))
)
if mibBuilder.loadTexts:
    currentUnderThresholdViolationCleared.setStatus(
        ""
    )

tempThreshHiAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 9)
)
tempThreshHiAlarmTrap.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsTemperature"))
)
if mibBuilder.loadTexts:
    tempThreshHiAlarmTrap.setStatus(
        ""
    )

tempThreshHiAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 10)
)
tempThreshHiAlarmClearedTrap.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsTemperature"))
)
if mibBuilder.loadTexts:
    tempThreshHiAlarmClearedTrap.setStatus(
        ""
    )

tempThreshLoAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 11)
)
tempThreshLoAlarmTrap.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsTemperature"))
)
if mibBuilder.loadTexts:
    tempThreshLoAlarmTrap.setStatus(
        ""
    )

tempThreshLoAlarmClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 26489, 0, 12)
)
tempThreshLoAlarmClearedTrap.setObjects(
      *(("IntelliData-MIB-401-4", "idsArgsLocation"),
        ("IntelliData-MIB-401-4", "idsArgsFeed"),
        ("IntelliData-MIB-401-4", "idsArgsTemperature"))
)
if mibBuilder.loadTexts:
    tempThreshLoAlarmClearedTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IntelliData-MIB-401-4",
    **{"intelliData": intelliData,
       "communicationLost": communicationLost,
       "communicationEstablished": communicationEstablished,
       "outletReboot": outletReboot,
       "currentThresholdViolation": currentThresholdViolation,
       "currentThresholdViolationCleared": currentThresholdViolationCleared,
       "currentUnderThresholdViolation": currentUnderThresholdViolation,
       "currentUnderThresholdViolationCleared": currentUnderThresholdViolationCleared,
       "tempThreshHiAlarmTrap": tempThreshHiAlarmTrap,
       "tempThreshHiAlarmClearedTrap": tempThreshHiAlarmClearedTrap,
       "tempThreshLoAlarmTrap": tempThreshLoAlarmTrap,
       "tempThreshLoAlarmClearedTrap": tempThreshLoAlarmClearedTrap,
       "idsDevices": idsDevices,
       "idsIdent": idsIdent,
       "idsIdentFirmwareRev": idsIdentFirmwareRev,
       "idsIdentSerialNumber": idsIdentSerialNumber,
       "idsIdentUnitName": idsIdentUnitName,
       "idsArgs": idsArgs,
       "idsArgsLocation": idsArgsLocation,
       "idsArgsFeed": idsArgsFeed,
       "idsArgsCurrent": idsArgsCurrent,
       "idsArgsTemperature": idsArgsTemperature,
       "idsArgsHumidity": idsArgsHumidity,
       "idsArgsInteger": idsArgsInteger,
       "idsArgsIpAddress": idsArgsIpAddress,
       "idsArgsString": idsArgsString,
       "idsArgsGauge": idsArgsGauge,
       "idsArgsTimeTicks": idsArgsTimeTicks,
       "idsArgsOutletIndex": idsArgsOutletIndex}
)
