# SNMP MIB module (BIGSWITCH-SWITCHLIGHT-PLATFORM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/bigswitch_37538/BIGSWITCH-SWITCHLIGHT-PLATFORM-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:48:03 2025
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

(bsn,) = mibBuilder.importSymbols(
    "BIGSWITCH-MIB",
    "bsn")

(bsnSwitchlight,) = mibBuilder.importSymbols(
    "BIGSWITCH-SWITCHLIGHT-MIB",
    "bsnSwitchlight")

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

informationTree = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000)
)
if mibBuilder.loadTexts:
    informationTree.setRevisions(
        ("2014-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_General_ObjectIdentity = ObjectIdentity
General = _General_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1)
)
_System_ObjectIdentity = ObjectIdentity
System = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1)
)
_SystemProductName_Type = DisplayString
_SystemProductName_Object = MibScalar
systemProductName = _SystemProductName_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 1),
    _SystemProductName_Type()
)
systemProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProductName.setStatus("current")
_SystemPartNumber_Type = DisplayString
_SystemPartNumber_Object = MibScalar
systemPartNumber = _SystemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 2),
    _SystemPartNumber_Type()
)
systemPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPartNumber.setStatus("current")
_SystemSerialNumber_Type = DisplayString
_SystemSerialNumber_Object = MibScalar
systemSerialNumber = _SystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 3),
    _SystemSerialNumber_Type()
)
systemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemSerialNumber.setStatus("current")
_SystemMAC_Type = DisplayString
_SystemMAC_Object = MibScalar
systemMAC = _SystemMAC_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 4),
    _SystemMAC_Type()
)
systemMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMAC.setStatus("current")
_SystemMACRange_Type = DisplayString
_SystemMACRange_Object = MibScalar
systemMACRange = _SystemMACRange_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 5),
    _SystemMACRange_Type()
)
systemMACRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemMACRange.setStatus("current")
_SystemManufacturer_Type = DisplayString
_SystemManufacturer_Object = MibScalar
systemManufacturer = _SystemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 6),
    _SystemManufacturer_Type()
)
systemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManufacturer.setStatus("current")
_SystemManufactureDate_Type = DisplayString
_SystemManufactureDate_Object = MibScalar
systemManufactureDate = _SystemManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 7),
    _SystemManufactureDate_Type()
)
systemManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemManufactureDate.setStatus("current")
_SystemVendor_Type = DisplayString
_SystemVendor_Object = MibScalar
systemVendor = _SystemVendor_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 8),
    _SystemVendor_Type()
)
systemVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemVendor.setStatus("current")
_SystemPlatformName_Type = DisplayString
_SystemPlatformName_Object = MibScalar
systemPlatformName = _SystemPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 9),
    _SystemPlatformName_Type()
)
systemPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemPlatformName.setStatus("current")
_SystemDeviceVersion_Type = DisplayString
_SystemDeviceVersion_Object = MibScalar
systemDeviceVersion = _SystemDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 10),
    _SystemDeviceVersion_Type()
)
systemDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDeviceVersion.setStatus("current")
_SystemLabelRevision_Type = DisplayString
_SystemLabelRevision_Object = MibScalar
systemLabelRevision = _SystemLabelRevision_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 11),
    _SystemLabelRevision_Type()
)
systemLabelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemLabelRevision.setStatus("current")
_SystemCountryCode_Type = DisplayString
_SystemCountryCode_Object = MibScalar
systemCountryCode = _SystemCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 12),
    _SystemCountryCode_Type()
)
systemCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemCountryCode.setStatus("current")
_SystemDiagVersion_Type = DisplayString
_SystemDiagVersion_Object = MibScalar
systemDiagVersion = _SystemDiagVersion_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 13),
    _SystemDiagVersion_Type()
)
systemDiagVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDiagVersion.setStatus("current")
_SystemServiceTag_Type = DisplayString
_SystemServiceTag_Object = MibScalar
systemServiceTag = _SystemServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 14),
    _SystemServiceTag_Type()
)
systemServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemServiceTag.setStatus("current")
_SystemONIEVersion_Type = DisplayString
_SystemONIEVersion_Object = MibScalar
systemONIEVersion = _SystemONIEVersion_Object(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 1, 1, 15),
    _SystemONIEVersion_Type()
)
systemONIEVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemONIEVersion.setStatus("current")
_Vendor_ObjectIdentity = ObjectIdentity
vendor = _Vendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2)
)
_Accton_ObjectIdentity = ObjectIdentity
accton = _Accton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2, 259)
)
_Dell_ObjectIdentity = ObjectIdentity
dell = _Dell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2, 674)
)
_Dni_ObjectIdentity = ObjectIdentity
dni = _Dni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2, 5324)
)
_Quanta_ObjectIdentity = ObjectIdentity
quanta = _Quanta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2, 7244)
)
_Debian_ObjectIdentity = ObjectIdentity
debian = _Debian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2, 9586)
)
_Bsn_ObjectIdentity = ObjectIdentity
bsn = _Bsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37538, 2, 1000, 2, 37538)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIGSWITCH-SWITCHLIGHT-PLATFORM-MIB",
    **{"informationTree": informationTree,
       "General": General,
       "System": System,
       "systemProductName": systemProductName,
       "systemPartNumber": systemPartNumber,
       "systemSerialNumber": systemSerialNumber,
       "systemMAC": systemMAC,
       "systemMACRange": systemMACRange,
       "systemManufacturer": systemManufacturer,
       "systemManufactureDate": systemManufactureDate,
       "systemVendor": systemVendor,
       "systemPlatformName": systemPlatformName,
       "systemDeviceVersion": systemDeviceVersion,
       "systemLabelRevision": systemLabelRevision,
       "systemCountryCode": systemCountryCode,
       "systemDiagVersion": systemDiagVersion,
       "systemServiceTag": systemServiceTag,
       "systemONIEVersion": systemONIEVersion,
       "vendor": vendor,
       "accton": accton,
       "dell": dell,
       "dni": dni,
       "quanta": quanta,
       "debian": debian,
       "bsn": bsn}
)
