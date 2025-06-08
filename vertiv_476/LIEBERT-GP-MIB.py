# SNMP MIB module (LIEBERT-GP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_476/LIEBERT-GP-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:21:43 2025
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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

liebertGlobalProductsRegistrationModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsRegistrationModule.setRevisions(
        ("2009-04-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2006-02-22 00:00")
    )

liebertAgentModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    liebertAgentModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-02-22 00:00")
    )

liebertGlobalProductsConditionsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsConditionsModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-08-15 00:00",
         "2006-02-22 00:00")
    )

liebertGlobalProductsNotificationsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsNotificationsModule.setRevisions(
        ("2008-07-02 00:00",
         "2008-05-15 00:00",
         "2008-01-10 00:00",
         "2006-08-15 00:00",
         "2006-02-22 00:00")
    )

liebertGlobalProductsEnvironmentalModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 5, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsEnvironmentalModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-08-15 00:00",
         "2006-02-22 00:00")
    )

liebertGlobalProductsPowerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 6, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsPowerModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2006-02-22 00:00")
    )

liebertControllerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7, 1)
)
if mibBuilder.loadTexts:
    liebertControllerModule.setRevisions(
        ("2008-07-02 00:00",
         "2008-01-10 00:00",
         "2006-02-22 00:00")
    )

liebertSystemModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8, 1)
)
if mibBuilder.loadTexts:
    liebertSystemModule.setRevisions(
        ("2008-11-17 00:00",
         "2008-07-02 00:00",
         "2008-01-10 00:00",
         "2007-05-29 00:00",
         "2006-02-22 00:00")
    )

liebertGlobalProductsPduModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 9, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsPduModule.setRevisions(
        ("2008-07-02 00:00",)
    )

liebertGlobalProductsFlexibleModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 10, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsFlexibleModule.setRevisions(
        ("2010-01-04 00:00",)
    )

liebertGlobalProductsFlexibleConditionsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 11, 1)
)
if mibBuilder.loadTexts:
    liebertGlobalProductsFlexibleConditionsModule.setRevisions(
        ("2011-07-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
if mibBuilder.loadTexts:
    emerson.setStatus("current")
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
if mibBuilder.loadTexts:
    liebertCorp.setStatus("current")
_LiebertGlobalProducts_ObjectIdentity = ObjectIdentity
liebertGlobalProducts = _LiebertGlobalProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42)
)
if mibBuilder.loadTexts:
    liebertGlobalProducts.setStatus("current")
_LgpModuleReg_ObjectIdentity = ObjectIdentity
lgpModuleReg = _LgpModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1)
)
if mibBuilder.loadTexts:
    lgpModuleReg.setStatus("current")
_LiebertModuleReg_ObjectIdentity = ObjectIdentity
liebertModuleReg = _LiebertModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 1)
)
if mibBuilder.loadTexts:
    liebertModuleReg.setStatus("current")
_LiebertAgentModuleReg_ObjectIdentity = ObjectIdentity
liebertAgentModuleReg = _LiebertAgentModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 2)
)
if mibBuilder.loadTexts:
    liebertAgentModuleReg.setStatus("current")
_LiebertConditionsModuleReg_ObjectIdentity = ObjectIdentity
liebertConditionsModuleReg = _LiebertConditionsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 3)
)
if mibBuilder.loadTexts:
    liebertConditionsModuleReg.setStatus("current")
_LiebertNotificationsModuleReg_ObjectIdentity = ObjectIdentity
liebertNotificationsModuleReg = _LiebertNotificationsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4)
)
if mibBuilder.loadTexts:
    liebertNotificationsModuleReg.setStatus("current")
_LiebertEnvironmentalModuleReg_ObjectIdentity = ObjectIdentity
liebertEnvironmentalModuleReg = _LiebertEnvironmentalModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 5)
)
if mibBuilder.loadTexts:
    liebertEnvironmentalModuleReg.setStatus("current")
_LiebertPowerModuleReg_ObjectIdentity = ObjectIdentity
liebertPowerModuleReg = _LiebertPowerModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 6)
)
if mibBuilder.loadTexts:
    liebertPowerModuleReg.setStatus("current")
_LiebertControllerModuleReg_ObjectIdentity = ObjectIdentity
liebertControllerModuleReg = _LiebertControllerModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 7)
)
if mibBuilder.loadTexts:
    liebertControllerModuleReg.setStatus("current")
_LiebertSystemModuleReg_ObjectIdentity = ObjectIdentity
liebertSystemModuleReg = _LiebertSystemModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8)
)
if mibBuilder.loadTexts:
    liebertSystemModuleReg.setStatus("current")
_LiebertPduModuleReg_ObjectIdentity = ObjectIdentity
liebertPduModuleReg = _LiebertPduModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 9)
)
if mibBuilder.loadTexts:
    liebertPduModuleReg.setStatus("current")
_LiebertFlexibleModuleReg_ObjectIdentity = ObjectIdentity
liebertFlexibleModuleReg = _LiebertFlexibleModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 10)
)
if mibBuilder.loadTexts:
    liebertFlexibleModuleReg.setStatus("current")
_LiebertFlexibleConditionsModuleReg_ObjectIdentity = ObjectIdentity
liebertFlexibleConditionsModuleReg = _LiebertFlexibleConditionsModuleReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 11)
)
if mibBuilder.loadTexts:
    liebertFlexibleConditionsModuleReg.setStatus("current")
_LgpAgent_ObjectIdentity = ObjectIdentity
lgpAgent = _LgpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2)
)
if mibBuilder.loadTexts:
    lgpAgent.setStatus("current")
_LgpAgentIdent_ObjectIdentity = ObjectIdentity
lgpAgentIdent = _LgpAgentIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1)
)
if mibBuilder.loadTexts:
    lgpAgentIdent.setStatus("current")


class _LgpAgentIdentManufacturer_Type(DisplayString):
    """Custom type lgpAgentIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpAgentIdentManufacturer_Type.__name__ = "DisplayString"
_LgpAgentIdentManufacturer_Object = MibScalar
lgpAgentIdentManufacturer = _LgpAgentIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 1),
    _LgpAgentIdentManufacturer_Type()
)
lgpAgentIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentManufacturer.setStatus("current")


class _LgpAgentIdentModel_Type(DisplayString):
    """Custom type lgpAgentIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpAgentIdentModel_Type.__name__ = "DisplayString"
_LgpAgentIdentModel_Object = MibScalar
lgpAgentIdentModel = _LgpAgentIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 2),
    _LgpAgentIdentModel_Type()
)
lgpAgentIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentModel.setStatus("current")


class _LgpAgentIdentFirmwareVersion_Type(DisplayString):
    """Custom type lgpAgentIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_LgpAgentIdentFirmwareVersion_Type.__name__ = "DisplayString"
_LgpAgentIdentFirmwareVersion_Object = MibScalar
lgpAgentIdentFirmwareVersion = _LgpAgentIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 3),
    _LgpAgentIdentFirmwareVersion_Type()
)
lgpAgentIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentFirmwareVersion.setStatus("current")


class _LgpAgentIdentSerialNumber_Type(DisplayString):
    """Custom type lgpAgentIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_LgpAgentIdentSerialNumber_Type.__name__ = "DisplayString"
_LgpAgentIdentSerialNumber_Object = MibScalar
lgpAgentIdentSerialNumber = _LgpAgentIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 4),
    _LgpAgentIdentSerialNumber_Type()
)
lgpAgentIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentSerialNumber.setStatus("current")


class _LgpAgentIdentPartNumber_Type(DisplayString):
    """Custom type lgpAgentIdentPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpAgentIdentPartNumber_Type.__name__ = "DisplayString"
_LgpAgentIdentPartNumber_Object = MibScalar
lgpAgentIdentPartNumber = _LgpAgentIdentPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 5),
    _LgpAgentIdentPartNumber_Type()
)
lgpAgentIdentPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentIdentPartNumber.setStatus("current")
_LgpAgentConnectedDeviceCount_Type = Unsigned32
_LgpAgentConnectedDeviceCount_Object = MibScalar
lgpAgentConnectedDeviceCount = _LgpAgentConnectedDeviceCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 1, 6),
    _LgpAgentConnectedDeviceCount_Type()
)
lgpAgentConnectedDeviceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentConnectedDeviceCount.setStatus("current")
_LgpAgentNotifications_ObjectIdentity = ObjectIdentity
lgpAgentNotifications = _LgpAgentNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3)
)
if mibBuilder.loadTexts:
    lgpAgentNotifications.setStatus("current")
_LgpAgentEventNotifications_ObjectIdentity = ObjectIdentity
lgpAgentEventNotifications = _LgpAgentEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0)
)
if mibBuilder.loadTexts:
    lgpAgentEventNotifications.setStatus("current")
_LgpAgentDevice_ObjectIdentity = ObjectIdentity
lgpAgentDevice = _LgpAgentDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4)
)
if mibBuilder.loadTexts:
    lgpAgentDevice.setStatus("current")
_LgpAgentManagedDeviceTable_Object = MibTable
lgpAgentManagedDeviceTable = _LgpAgentManagedDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lgpAgentManagedDeviceTable.setStatus("current")
_LgpAgentManagedDeviceEntry_Object = MibTableRow
lgpAgentManagedDeviceEntry = _LgpAgentManagedDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1)
)
lgpAgentManagedDeviceEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpAgentDeviceIndex"),
)
if mibBuilder.loadTexts:
    lgpAgentManagedDeviceEntry.setStatus("current")


class _LgpAgentDeviceIndex_Type(Integer32):
    """Custom type lgpAgentDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LgpAgentDeviceIndex_Type.__name__ = "Integer32"
_LgpAgentDeviceIndex_Object = MibTableColumn
lgpAgentDeviceIndex = _LgpAgentDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 1),
    _LgpAgentDeviceIndex_Type()
)
lgpAgentDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceIndex.setStatus("current")
_LgpAgentDeviceId_Type = ObjectIdentifier
_LgpAgentDeviceId_Object = MibTableColumn
lgpAgentDeviceId = _LgpAgentDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 2),
    _LgpAgentDeviceId_Type()
)
lgpAgentDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceId.setStatus("current")


class _LgpAgentDeviceManufacturer_Type(DisplayString):
    """Custom type lgpAgentDeviceManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpAgentDeviceManufacturer_Type.__name__ = "DisplayString"
_LgpAgentDeviceManufacturer_Object = MibTableColumn
lgpAgentDeviceManufacturer = _LgpAgentDeviceManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 3),
    _LgpAgentDeviceManufacturer_Type()
)
lgpAgentDeviceManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceManufacturer.setStatus("current")


class _LgpAgentDeviceModel_Type(DisplayString):
    """Custom type lgpAgentDeviceModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpAgentDeviceModel_Type.__name__ = "DisplayString"
_LgpAgentDeviceModel_Object = MibTableColumn
lgpAgentDeviceModel = _LgpAgentDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 4),
    _LgpAgentDeviceModel_Type()
)
lgpAgentDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceModel.setStatus("current")


class _LgpAgentDeviceFirmwareVersion_Type(DisplayString):
    """Custom type lgpAgentDeviceFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_LgpAgentDeviceFirmwareVersion_Type.__name__ = "DisplayString"
_LgpAgentDeviceFirmwareVersion_Object = MibTableColumn
lgpAgentDeviceFirmwareVersion = _LgpAgentDeviceFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 5),
    _LgpAgentDeviceFirmwareVersion_Type()
)
lgpAgentDeviceFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceFirmwareVersion.setStatus("current")
_LgpAgentDeviceUnitNumber_Type = Integer32
_LgpAgentDeviceUnitNumber_Object = MibTableColumn
lgpAgentDeviceUnitNumber = _LgpAgentDeviceUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 6),
    _LgpAgentDeviceUnitNumber_Type()
)
lgpAgentDeviceUnitNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceUnitNumber.setStatus("current")


class _LgpAgentDeviceSerialNumber_Type(DisplayString):
    """Custom type lgpAgentDeviceSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_LgpAgentDeviceSerialNumber_Type.__name__ = "DisplayString"
_LgpAgentDeviceSerialNumber_Object = MibTableColumn
lgpAgentDeviceSerialNumber = _LgpAgentDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 7),
    _LgpAgentDeviceSerialNumber_Type()
)
lgpAgentDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceSerialNumber.setStatus("current")


class _LgpAgentDeviceManufactureDate_Type(DisplayString):
    """Custom type lgpAgentDeviceManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_LgpAgentDeviceManufactureDate_Type.__name__ = "DisplayString"
_LgpAgentDeviceManufactureDate_Object = MibTableColumn
lgpAgentDeviceManufactureDate = _LgpAgentDeviceManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 8),
    _LgpAgentDeviceManufactureDate_Type()
)
lgpAgentDeviceManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpAgentDeviceManufactureDate.setStatus("current")


class _LgpAgentDeviceServiceContact_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceContact_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceContact_Object = MibTableColumn
lgpAgentDeviceServiceContact = _LgpAgentDeviceServiceContact_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 9),
    _LgpAgentDeviceServiceContact_Type()
)
lgpAgentDeviceServiceContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceContact.setStatus("current")


class _LgpAgentDeviceServicePhoneNumber_Type(DisplayString):
    """Custom type lgpAgentDeviceServicePhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServicePhoneNumber_Type.__name__ = "DisplayString"
_LgpAgentDeviceServicePhoneNumber_Object = MibTableColumn
lgpAgentDeviceServicePhoneNumber = _LgpAgentDeviceServicePhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 10),
    _LgpAgentDeviceServicePhoneNumber_Type()
)
lgpAgentDeviceServicePhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServicePhoneNumber.setStatus("current")


class _LgpAgentDeviceServiceAddrLine1_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine1_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine1_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine1 = _LgpAgentDeviceServiceAddrLine1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 11),
    _LgpAgentDeviceServiceAddrLine1_Type()
)
lgpAgentDeviceServiceAddrLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine1.setStatus("current")


class _LgpAgentDeviceServiceAddrLine2_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine2_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine2_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine2 = _LgpAgentDeviceServiceAddrLine2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 12),
    _LgpAgentDeviceServiceAddrLine2_Type()
)
lgpAgentDeviceServiceAddrLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine2.setStatus("current")


class _LgpAgentDeviceServiceAddrLine3_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine3_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine3_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine3 = _LgpAgentDeviceServiceAddrLine3_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 13),
    _LgpAgentDeviceServiceAddrLine3_Type()
)
lgpAgentDeviceServiceAddrLine3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine3.setStatus("current")


class _LgpAgentDeviceServiceAddrLine4_Type(DisplayString):
    """Custom type lgpAgentDeviceServiceAddrLine4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceServiceAddrLine4_Type.__name__ = "DisplayString"
_LgpAgentDeviceServiceAddrLine4_Object = MibTableColumn
lgpAgentDeviceServiceAddrLine4 = _LgpAgentDeviceServiceAddrLine4_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 14),
    _LgpAgentDeviceServiceAddrLine4_Type()
)
lgpAgentDeviceServiceAddrLine4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceServiceAddrLine4.setStatus("current")


class _LgpAgentDeviceUnitName_Type(DisplayString):
    """Custom type lgpAgentDeviceUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_LgpAgentDeviceUnitName_Type.__name__ = "DisplayString"
_LgpAgentDeviceUnitName_Object = MibTableColumn
lgpAgentDeviceUnitName = _LgpAgentDeviceUnitName_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 15),
    _LgpAgentDeviceUnitName_Type()
)
lgpAgentDeviceUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceUnitName.setStatus("current")


class _LgpAgentDeviceSiteIdentifier_Type(DisplayString):
    """Custom type lgpAgentDeviceSiteIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceSiteIdentifier_Type.__name__ = "DisplayString"
_LgpAgentDeviceSiteIdentifier_Object = MibTableColumn
lgpAgentDeviceSiteIdentifier = _LgpAgentDeviceSiteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 16),
    _LgpAgentDeviceSiteIdentifier_Type()
)
lgpAgentDeviceSiteIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceSiteIdentifier.setStatus("current")


class _LgpAgentDeviceTagNumber_Type(DisplayString):
    """Custom type lgpAgentDeviceTagNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceTagNumber_Type.__name__ = "DisplayString"
_LgpAgentDeviceTagNumber_Object = MibTableColumn
lgpAgentDeviceTagNumber = _LgpAgentDeviceTagNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 17),
    _LgpAgentDeviceTagNumber_Type()
)
lgpAgentDeviceTagNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceTagNumber.setStatus("current")


class _LgpAgentDeviceOrderLine1_Type(DisplayString):
    """Custom type lgpAgentDeviceOrderLine1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceOrderLine1_Type.__name__ = "DisplayString"
_LgpAgentDeviceOrderLine1_Object = MibTableColumn
lgpAgentDeviceOrderLine1 = _LgpAgentDeviceOrderLine1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 18),
    _LgpAgentDeviceOrderLine1_Type()
)
lgpAgentDeviceOrderLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceOrderLine1.setStatus("current")


class _LgpAgentDeviceOrderLine2_Type(DisplayString):
    """Custom type lgpAgentDeviceOrderLine2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LgpAgentDeviceOrderLine2_Type.__name__ = "DisplayString"
_LgpAgentDeviceOrderLine2_Object = MibTableColumn
lgpAgentDeviceOrderLine2 = _LgpAgentDeviceOrderLine2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 4, 2, 1, 19),
    _LgpAgentDeviceOrderLine2_Type()
)
lgpAgentDeviceOrderLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentDeviceOrderLine2.setStatus("current")
_LgpAgentControl_ObjectIdentity = ObjectIdentity
lgpAgentControl = _LgpAgentControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5)
)
if mibBuilder.loadTexts:
    lgpAgentControl.setStatus("current")
_LgpAgentReboot_Type = Integer32
_LgpAgentReboot_Object = MibScalar
lgpAgentReboot = _LgpAgentReboot_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 5, 1),
    _LgpAgentReboot_Type()
)
lgpAgentReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpAgentReboot.setStatus("current")
_LgpFoundation_ObjectIdentity = ObjectIdentity
lgpFoundation = _LgpFoundation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3)
)
if mibBuilder.loadTexts:
    lgpFoundation.setStatus("current")
_LgpConditions_ObjectIdentity = ObjectIdentity
lgpConditions = _LgpConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2)
)
if mibBuilder.loadTexts:
    lgpConditions.setStatus("current")
_LgpConditionsWellKnown_ObjectIdentity = ObjectIdentity
lgpConditionsWellKnown = _LgpConditionsWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1)
)
_LgpConditionHighTemperature_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperature = _LgpConditionHighTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperature.setStatus("current")
_LgpConditionLowTemperature_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperature = _LgpConditionLowTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperature.setStatus("current")
_LgpConditionHighHumidity_ObjectIdentity = ObjectIdentity
lgpConditionHighHumidity = _LgpConditionHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumidity.setStatus("current")
_LgpConditionLowHumidity_ObjectIdentity = ObjectIdentity
lgpConditionLowHumidity = _LgpConditionLowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumidity.setStatus("current")
_LgpConditionLossOfAirflow_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflow = _LgpConditionLossOfAirflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflow.setStatus("current")
_LgpConditionLossOfAirflow1_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflow1 = _LgpConditionLossOfAirflow1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflow1.setStatus("current")
_LgpConditionLossOfAirflow2_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflow2 = _LgpConditionLossOfAirflow2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflow2.setStatus("current")
_LgpConditionLossOfAirflowBlower1_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflowBlower1 = _LgpConditionLossOfAirflowBlower1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 3)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflowBlower1.setStatus("current")
_LgpConditionLossOfAirflowAllBlowers_ObjectIdentity = ObjectIdentity
lgpConditionLossOfAirflowAllBlowers = _LgpConditionLossOfAirflowAllBlowers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfAirflowAllBlowers.setStatus("current")
_LgpConditionChangeFilter_ObjectIdentity = ObjectIdentity
lgpConditionChangeFilter = _LgpConditionChangeFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lgpConditionChangeFilter.setStatus("current")
_LgpConditionCompressorHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorHighHeadPressure = _LgpConditionCompressorHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorHighHeadPressure.setStatus("current")
_LgpConditionCompressor1HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1HighHeadPressure = _LgpConditionCompressor1HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1HighHeadPressure.setStatus("current")
_LgpConditionCompressor1AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1AHighHeadPressure = _LgpConditionCompressor1AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1AHighHeadPressure.setStatus("current")
_LgpConditionCompressor1BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1BHighHeadPressure = _LgpConditionCompressor1BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1BHighHeadPressure.setStatus("current")
_LgpConditionCompressor2HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2HighHeadPressure = _LgpConditionCompressor2HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2HighHeadPressure.setStatus("current")
_LgpConditionCompressor2AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2AHighHeadPressure = _LgpConditionCompressor2AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2AHighHeadPressure.setStatus("current")
_LgpConditionCompressor2BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2BHighHeadPressure = _LgpConditionCompressor2BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2BHighHeadPressure.setStatus("current")
_LgpConditionCompressor3HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor3HighHeadPressure = _LgpConditionCompressor3HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor3HighHeadPressure.setStatus("current")
_LgpConditionCompressor4HighHeadPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor4HighHeadPressure = _LgpConditionCompressor4HighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 7, 4)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor4HighHeadPressure.setStatus("current")
_LgpConditionCompressorOverload_ObjectIdentity = ObjectIdentity
lgpConditionCompressorOverload = _LgpConditionCompressorOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 8)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorOverload.setStatus("current")
_LgpConditionCompressor1Overload_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1Overload = _LgpConditionCompressor1Overload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1Overload.setStatus("current")
_LgpConditionCompressor2Overload_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2Overload = _LgpConditionCompressor2Overload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2Overload.setStatus("current")
_LgpConditionCompressorShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressorShortCycle = _LgpConditionCompressorShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorShortCycle.setStatus("current")
_LgpConditionCompressor1ShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1ShortCycle = _LgpConditionCompressor1ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1ShortCycle.setStatus("current")
_LgpConditionCompressor1AShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1AShortCycle = _LgpConditionCompressor1AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1AShortCycle.setStatus("current")
_LgpConditionCompressor1BShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1BShortCycle = _LgpConditionCompressor1BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1BShortCycle.setStatus("current")
_LgpConditionCompressor2ShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2ShortCycle = _LgpConditionCompressor2ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2ShortCycle.setStatus("current")
_LgpConditionCompressor2AShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2AShortCycle = _LgpConditionCompressor2AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2AShortCycle.setStatus("current")
_LgpConditionCompressor2BShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2BShortCycle = _LgpConditionCompressor2BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 9, 2, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2BShortCycle.setStatus("current")
_LgpConditionCompressorLowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorLowSuctionPressure = _LgpConditionCompressorLowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 10)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorLowSuctionPressure.setStatus("current")
_LgpConditionCompressor1LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1LowSuctionPressure = _LgpConditionCompressor1LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1LowSuctionPressure.setStatus("current")
_LgpConditionCompressor2LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2LowSuctionPressure = _LgpConditionCompressor2LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2LowSuctionPressure.setStatus("current")
_LgpConditionMainFanOverLoad_ObjectIdentity = ObjectIdentity
lgpConditionMainFanOverLoad = _LgpConditionMainFanOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 11)
)
if mibBuilder.loadTexts:
    lgpConditionMainFanOverLoad.setStatus("current")
_LgpConditionManualOverride_ObjectIdentity = ObjectIdentity
lgpConditionManualOverride = _LgpConditionManualOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 12)
)
if mibBuilder.loadTexts:
    lgpConditionManualOverride.setStatus("current")
_LgpConditionStandbyGlycoolPumpOn_ObjectIdentity = ObjectIdentity
lgpConditionStandbyGlycoolPumpOn = _LgpConditionStandbyGlycoolPumpOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 13)
)
if mibBuilder.loadTexts:
    lgpConditionStandbyGlycoolPumpOn.setStatus("current")
_LgpConditionWaterUnderFloor_ObjectIdentity = ObjectIdentity
lgpConditionWaterUnderFloor = _LgpConditionWaterUnderFloor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 14)
)
if mibBuilder.loadTexts:
    lgpConditionWaterUnderFloor.setStatus("current")
_LgpConditionHumidifierProblem_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierProblem = _LgpConditionHumidifierProblem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 15)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierProblem.setStatus("current")
_LgpConditionLowWaterInHumidifier_ObjectIdentity = ObjectIdentity
lgpConditionLowWaterInHumidifier = _LgpConditionLowWaterInHumidifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 16)
)
if mibBuilder.loadTexts:
    lgpConditionLowWaterInHumidifier.setStatus("current")
_LgpConditionSmokeDetected_ObjectIdentity = ObjectIdentity
lgpConditionSmokeDetected = _LgpConditionSmokeDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 17)
)
if mibBuilder.loadTexts:
    lgpConditionSmokeDetected.setStatus("current")
_LgpConditionLowWaterFlow_ObjectIdentity = ObjectIdentity
lgpConditionLowWaterFlow = _LgpConditionLowWaterFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 18)
)
if mibBuilder.loadTexts:
    lgpConditionLowWaterFlow.setStatus("current")
_LgpConditionLostPower_ObjectIdentity = ObjectIdentity
lgpConditionLostPower = _LgpConditionLostPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 19)
)
if mibBuilder.loadTexts:
    lgpConditionLostPower.setStatus("current")
_LgpGeneralFault_ObjectIdentity = ObjectIdentity
lgpGeneralFault = _LgpGeneralFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 20)
)
if mibBuilder.loadTexts:
    lgpGeneralFault.setStatus("current")
_LgpConditionLocalAlarm_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm = _LgpConditionLocalAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm.setStatus("current")
_LgpConditionLocalAlarm1_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm1 = _LgpConditionLocalAlarm1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm1.setStatus("current")
_LgpConditionLocalAlarm2_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm2 = _LgpConditionLocalAlarm2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm2.setStatus("current")
_LgpConditionLocalAlarm3_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm3 = _LgpConditionLocalAlarm3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 3)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm3.setStatus("current")
_LgpConditionLocalAlarm4_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm4 = _LgpConditionLocalAlarm4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm4.setStatus("current")
_LgpConditionLocalAlarm5_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm5 = _LgpConditionLocalAlarm5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm5.setStatus("current")
_LgpConditionLocalAlarm6_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm6 = _LgpConditionLocalAlarm6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 6)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm6.setStatus("current")
_LgpConditionLocalAlarm7_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm7 = _LgpConditionLocalAlarm7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 7)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm7.setStatus("current")
_LgpConditionLocalAlarm8_ObjectIdentity = ObjectIdentity
lgpConditionLocalAlarm8 = _LgpConditionLocalAlarm8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 21, 8)
)
if mibBuilder.loadTexts:
    lgpConditionLocalAlarm8.setStatus("current")
_LgpConditionStandbyUnitOn_ObjectIdentity = ObjectIdentity
lgpConditionStandbyUnitOn = _LgpConditionStandbyUnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 22)
)
if mibBuilder.loadTexts:
    lgpConditionStandbyUnitOn.setStatus("current")
_LgpConditionCompressorLowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorLowPressure = _LgpConditionCompressorLowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorLowPressure.setStatus("current")
_LgpConditionCompressor1LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1LowPressure = _LgpConditionCompressor1LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1LowPressure.setStatus("current")
_LgpConditionTandemCompressorCircuit1LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionTandemCompressorCircuit1LowPressure = _LgpConditionTandemCompressorCircuit1LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionTandemCompressorCircuit1LowPressure.setStatus("current")
_LgpConditionCompressor2LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2LowPressure = _LgpConditionCompressor2LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2LowPressure.setStatus("current")
_LgpConditionTandemCompressorCircuit2LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionTandemCompressorCircuit2LowPressure = _LgpConditionTandemCompressorCircuit2LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 2, 1)
)
if mibBuilder.loadTexts:
    lgpConditionTandemCompressorCircuit2LowPressure.setStatus("current")
_LgpConditionCompressor3LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor3LowPressure = _LgpConditionCompressor3LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor3LowPressure.setStatus("current")
_LgpConditionCompressor4LowPressure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor4LowPressure = _LgpConditionCompressor4LowPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 23, 4)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor4LowPressure.setStatus("current")
_LgpConditionHighWaterInPan_ObjectIdentity = ObjectIdentity
lgpConditionHighWaterInPan = _LgpConditionHighWaterInPan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 24)
)
if mibBuilder.loadTexts:
    lgpConditionHighWaterInPan.setStatus("current")
_LgpConditionFaultySensor_ObjectIdentity = ObjectIdentity
lgpConditionFaultySensor = _LgpConditionFaultySensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 25)
)
if mibBuilder.loadTexts:
    lgpConditionFaultySensor.setStatus("current")
_LgpConditionServiceCooling_ObjectIdentity = ObjectIdentity
lgpConditionServiceCooling = _LgpConditionServiceCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 26)
)
if mibBuilder.loadTexts:
    lgpConditionServiceCooling.setStatus("current")
_LgpConditionServiceHumidifier_ObjectIdentity = ObjectIdentity
lgpConditionServiceHumidifier = _LgpConditionServiceHumidifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 27)
)
if mibBuilder.loadTexts:
    lgpConditionServiceHumidifier.setStatus("current")
_LgpConditionSystemControlBatteryLow_ObjectIdentity = ObjectIdentity
lgpConditionSystemControlBatteryLow = _LgpConditionSystemControlBatteryLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 28)
)
if mibBuilder.loadTexts:
    lgpConditionSystemControlBatteryLow.setStatus("current")
_LgpConditionGroundSystemFault_ObjectIdentity = ObjectIdentity
lgpConditionGroundSystemFault = _LgpConditionGroundSystemFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 29)
)
if mibBuilder.loadTexts:
    lgpConditionGroundSystemFault.setStatus("current")
_LgpConditionGroundFailure_ObjectIdentity = ObjectIdentity
lgpConditionGroundFailure = _LgpConditionGroundFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 30)
)
if mibBuilder.loadTexts:
    lgpConditionGroundFailure.setStatus("current")
_LgpConditionSecurityBreach_ObjectIdentity = ObjectIdentity
lgpConditionSecurityBreach = _LgpConditionSecurityBreach_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 31)
)
if mibBuilder.loadTexts:
    lgpConditionSecurityBreach.setStatus("current")
_LgpConditionEmergencyShutdown_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyShutdown = _LgpConditionEmergencyShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 32)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyShutdown.setStatus("current")
_LgpConditionOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionOnBypass = _LgpConditionOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33)
)
if mibBuilder.loadTexts:
    lgpConditionOnBypass.setStatus("current")
_LgpConditionLoadOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnBypass = _LgpConditionLoadOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnBypass.setStatus("obsolete")
_LgpConditionLoadOnMaintenceBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnMaintenceBypass = _LgpConditionLoadOnMaintenceBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnMaintenceBypass.setStatus("current")
_LgpConditionParallelSysLoadOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysLoadOnBypass = _LgpConditionParallelSysLoadOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 3)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysLoadOnBypass.setStatus("current")
_LgpConditionLoadOnBypassByImpact_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnBypassByImpact = _LgpConditionLoadOnBypassByImpact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnBypassByImpact.setStatus("current")
_LgpConditionLoadTransferedToBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadTransferedToBypass = _LgpConditionLoadTransferedToBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLoadTransferedToBypass.setStatus("current")
_LgpConditionEmergencyTransferToBypass_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyTransferToBypass = _LgpConditionEmergencyTransferToBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 33, 6)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyTransferToBypass.setStatus("current")
_LgpConditionOutputToLoadVoltTHD_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadVoltTHD = _LgpConditionOutputToLoadVoltTHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 34)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadVoltTHD.setStatus("current")
_LgpConditionLogicFailure_ObjectIdentity = ObjectIdentity
lgpConditionLogicFailure = _LgpConditionLogicFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 35)
)
if mibBuilder.loadTexts:
    lgpConditionLogicFailure.setStatus("current")
_LgpConditionPowerSupplyFault_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupplyFault = _LgpConditionPowerSupplyFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 36)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupplyFault.setStatus("current")
_LgpConditionPowerSupply1Fault_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply1Fault = _LgpConditionPowerSupply1Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 36, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply1Fault.setStatus("current")
_LgpConditionPowerSupply2Fault_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply2Fault = _LgpConditionPowerSupply2Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 36, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply2Fault.setStatus("current")
_LgpConditionPowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupplyFailure = _LgpConditionPowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupplyFailure.setStatus("current")
_LgpConditionPowerSupply1Failure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply1Failure = _LgpConditionPowerSupply1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply1Failure.setStatus("current")
_LgpConditionPowerSupply2Failure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupply2Failure = _LgpConditionPowerSupply2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupply2Failure.setStatus("current")
_LgpConditionSource1PowerSupplyInputFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1PowerSupplyInputFailure = _LgpConditionSource1PowerSupplyInputFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PowerSupplyInputFailure.setStatus("current")
_LgpConditionSource2PowerSupplyInputFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2PowerSupplyInputFailure = _LgpConditionSource2PowerSupplyInputFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PowerSupplyInputFailure.setStatus("current")
_LgpConditionPowerSupplyLogicFailure_ObjectIdentity = ObjectIdentity
lgpConditionPowerSupplyLogicFailure = _LgpConditionPowerSupplyLogicFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 5)
)
if mibBuilder.loadTexts:
    lgpConditionPowerSupplyLogicFailure.setStatus("current")
_LgpConditionCompressorPowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorPowerSupplyFailure = _LgpConditionCompressorPowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 37, 6)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorPowerSupplyFailure.setStatus("current")
_LgpConditionOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionOverVoltage = _LgpConditionOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38)
)
if mibBuilder.loadTexts:
    lgpConditionOverVoltage.setStatus("current")
_LgpConditionSource1OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource1OverVoltage = _LgpConditionSource1OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1OverVoltage.setStatus("current")
_LgpConditionSource2OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource2OverVoltage = _LgpConditionSource2OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2OverVoltage.setStatus("current")
_LgpConditionOutputToLoadOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverVoltage = _LgpConditionOutputToLoadOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverVoltage.setStatus("current")
_LgpConditionInputOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionInputOverVoltage = _LgpConditionInputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInputOverVoltage.setStatus("current")
_LgpConditionBypassOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBypassOverVoltage = _LgpConditionBypassOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBypassOverVoltage.setStatus("current")
_LgpConditionBypassOverVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionBypassOverVoltageFailure = _LgpConditionBypassOverVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 6)
)
if mibBuilder.loadTexts:
    lgpConditionBypassOverVoltageFailure.setStatus("current")
_LgpConditionBatteryOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBatteryOverVoltage = _LgpConditionBatteryOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryOverVoltage.setStatus("current")
_LgpConditionDcBusOverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBusOverVoltage = _LgpConditionDcBusOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8)
)
if mibBuilder.loadTexts:
    lgpConditionDcBusOverVoltage.setStatus("current")
_LgpConditionDcBus1OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1OverVoltage = _LgpConditionDcBus1OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 1)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1OverVoltage.setStatus("current")
_LgpConditionDcBus2OverVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2OverVoltage = _LgpConditionDcBus2OverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 2)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2OverVoltage.setStatus("current")
_LgpConditionDcBus1OverVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1OverVoltageFailure = _LgpConditionDcBus1OverVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 3)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1OverVoltageFailure.setStatus("current")
_LgpConditionDcBus2OverVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2OverVoltageFailure = _LgpConditionDcBus2OverVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 38, 8, 4)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2OverVoltageFailure.setStatus("current")
_LgpConditionUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionUnderVoltage = _LgpConditionUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39)
)
if mibBuilder.loadTexts:
    lgpConditionUnderVoltage.setStatus("current")
_LgpConditionSource1UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource1UnderVoltage = _LgpConditionSource1UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1UnderVoltage.setStatus("current")
_LgpConditionSource2UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionSource2UnderVoltage = _LgpConditionSource2UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2UnderVoltage.setStatus("current")
_LgpConditionOutputToLoadUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadUnderVoltage = _LgpConditionOutputToLoadUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadUnderVoltage.setStatus("current")
_LgpConditionSource1UnderVoltageRMS_ObjectIdentity = ObjectIdentity
lgpConditionSource1UnderVoltageRMS = _LgpConditionSource1UnderVoltageRMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource1UnderVoltageRMS.setStatus("current")
_LgpConditionSource2UnderVoltageRMS_ObjectIdentity = ObjectIdentity
lgpConditionSource2UnderVoltageRMS = _LgpConditionSource2UnderVoltageRMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource2UnderVoltageRMS.setStatus("current")
_LgpConditionInputUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionInputUnderVoltage = _LgpConditionInputUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 6)
)
if mibBuilder.loadTexts:
    lgpConditionInputUnderVoltage.setStatus("current")
_LgpConditionBypassUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBypassUnderVoltage = _LgpConditionBypassUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBypassUnderVoltage.setStatus("current")
_LgpConditionBypassUnderVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionBypassUnderVoltageFailure = _LgpConditionBypassUnderVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBypassUnderVoltageFailure.setStatus("current")
_LgpConditionBatteryUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionBatteryUnderVoltage = _LgpConditionBatteryUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 9)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryUnderVoltage.setStatus("current")
_LgpConditionDcBusUnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBusUnderVoltage = _LgpConditionDcBusUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10)
)
if mibBuilder.loadTexts:
    lgpConditionDcBusUnderVoltage.setStatus("current")
_LgpConditionDcBus1UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1UnderVoltage = _LgpConditionDcBus1UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 1)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1UnderVoltage.setStatus("current")
_LgpConditionDcBus2UnderVoltage_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2UnderVoltage = _LgpConditionDcBus2UnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 2)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2UnderVoltage.setStatus("current")
_LgpConditionDcBus1UnderVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus1UnderVoltageFailure = _LgpConditionDcBus1UnderVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 3)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus1UnderVoltageFailure.setStatus("current")
_LgpConditionDcBus2UnderVoltageFailure_ObjectIdentity = ObjectIdentity
lgpConditionDcBus2UnderVoltageFailure = _LgpConditionDcBus2UnderVoltageFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 39, 10, 4)
)
if mibBuilder.loadTexts:
    lgpConditionDcBus2UnderVoltageFailure.setStatus("current")
_LgpConditionOverload_ObjectIdentity = ObjectIdentity
lgpConditionOverload = _LgpConditionOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40)
)
if mibBuilder.loadTexts:
    lgpConditionOverload.setStatus("current")
_LgpConditionSource1Overload_ObjectIdentity = ObjectIdentity
lgpConditionSource1Overload = _LgpConditionSource1Overload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1Overload.setStatus("current")
_LgpConditionSystemOverload_ObjectIdentity = ObjectIdentity
lgpConditionSystemOverload = _LgpConditionSystemOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOverload.setStatus("current")
_LgpConditionSource1PeakCurrentOverLoad_ObjectIdentity = ObjectIdentity
lgpConditionSource1PeakCurrentOverLoad = _LgpConditionSource1PeakCurrentOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PeakCurrentOverLoad.setStatus("current")
_LgpConditionSource2PeakCurrentOverLoad_ObjectIdentity = ObjectIdentity
lgpConditionSource2PeakCurrentOverLoad = _LgpConditionSource2PeakCurrentOverLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PeakCurrentOverLoad.setStatus("current")
_LgpConditionOutputToLoadOverLimit_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverLimit = _LgpConditionOutputToLoadOverLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 5)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverLimit.setStatus("current")
_LgpConditionOutputToLoadOverload_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverload = _LgpConditionOutputToLoadOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 6)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverload.setStatus("current")
_LgpConditionParallelSysOverload_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysOverload = _LgpConditionParallelSysOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 7)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysOverload.setStatus("current")
_LgpConditionBypassCurrentOverload_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverload = _LgpConditionBypassCurrentOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverload.setStatus("current")
_LgpConditionBypassCurrentOverloadPhsA_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverloadPhsA = _LgpConditionBypassCurrentOverloadPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverloadPhsA.setStatus("current")
_LgpConditionBypassCurrentOverloadPhsB_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverloadPhsB = _LgpConditionBypassCurrentOverloadPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8, 2)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverloadPhsB.setStatus("current")
_LgpConditionBypassCurrentOverloadPhsC_ObjectIdentity = ObjectIdentity
lgpConditionBypassCurrentOverloadPhsC = _LgpConditionBypassCurrentOverloadPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 40, 8, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassCurrentOverloadPhsC.setStatus("current")
_LgpConditionScrShort_ObjectIdentity = ObjectIdentity
lgpConditionScrShort = _LgpConditionScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41)
)
if mibBuilder.loadTexts:
    lgpConditionScrShort.setStatus("current")
_LgpConditionSource1ScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource1ScrShort = _LgpConditionSource1ScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1ScrShort.setStatus("current")
_LgpConditionSource2ScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource2ScrShort = _LgpConditionSource2ScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2ScrShort.setStatus("current")
_LgpConditionBypassScrShort_ObjectIdentity = ObjectIdentity
lgpConditionBypassScrShort = _LgpConditionBypassScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassScrShort.setStatus("current")
_LgpConditionInvStaticSwScrShort_ObjectIdentity = ObjectIdentity
lgpConditionInvStaticSwScrShort = _LgpConditionInvStaticSwScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInvStaticSwScrShort.setStatus("current")
_LgpConditionSource1NeutralScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource1NeutralScrShort = _LgpConditionSource1NeutralScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource1NeutralScrShort.setStatus("current")
_LgpConditionSource2NeutralScrShort_ObjectIdentity = ObjectIdentity
lgpConditionSource2NeutralScrShort = _LgpConditionSource2NeutralScrShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 41, 6)
)
if mibBuilder.loadTexts:
    lgpConditionSource2NeutralScrShort.setStatus("current")
_LgpConditionScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionScrOpen = _LgpConditionScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42)
)
if mibBuilder.loadTexts:
    lgpConditionScrOpen.setStatus("current")
_LgpConditionSource1ScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1ScrOpen = _LgpConditionSource1ScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1ScrOpen.setStatus("current")
_LgpConditionSource2ScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2ScrOpen = _LgpConditionSource2ScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2ScrOpen.setStatus("current")
_LgpConditionBypassScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionBypassScrOpen = _LgpConditionBypassScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassScrOpen.setStatus("current")
_LgpConditionSource1NeutralScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1NeutralScrOpen = _LgpConditionSource1NeutralScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource1NeutralScrOpen.setStatus("current")
_LgpConditionSource2NeutralScrOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2NeutralScrOpen = _LgpConditionSource2NeutralScrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 42, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource2NeutralScrOpen.setStatus("current")
_LgpConditionFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionFanFailure = _LgpConditionFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43)
)
if mibBuilder.loadTexts:
    lgpConditionFanFailure.setStatus("current")
_LgpConditionFan1Failure_ObjectIdentity = ObjectIdentity
lgpConditionFan1Failure = _LgpConditionFan1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 1)
)
if mibBuilder.loadTexts:
    lgpConditionFan1Failure.setStatus("current")
_LgpConditionRedundantFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionRedundantFanFailure = _LgpConditionRedundantFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantFanFailure.setStatus("current")
_LgpConditionMultipleFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionMultipleFanFailure = _LgpConditionMultipleFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 3)
)
if mibBuilder.loadTexts:
    lgpConditionMultipleFanFailure.setStatus("current")
_LgpConditionBlowerFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionBlowerFanFailure = _LgpConditionBlowerFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 4)
)
if mibBuilder.loadTexts:
    lgpConditionBlowerFanFailure.setStatus("current")
_LgpConditionBottomBlowerFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionBottomBlowerFanFailure = _LgpConditionBottomBlowerFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 4, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBottomBlowerFanFailure.setStatus("current")
_LgpConditionTopBlowerFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionTopBlowerFanFailure = _LgpConditionTopBlowerFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 4, 2)
)
if mibBuilder.loadTexts:
    lgpConditionTopBlowerFanFailure.setStatus("current")
_LgpConditionCondenserFanVFDFailure_ObjectIdentity = ObjectIdentity
lgpConditionCondenserFanVFDFailure = _LgpConditionCondenserFanVFDFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 5)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserFanVFDFailure.setStatus("current")
_LgpConditionFanPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionFanPowerFailure = _LgpConditionFanPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 43, 6)
)
if mibBuilder.loadTexts:
    lgpConditionFanPowerFailure.setStatus("current")
_LgpConditionTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionTransferInhibited = _LgpConditionTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 44)
)
if mibBuilder.loadTexts:
    lgpConditionTransferInhibited.setStatus("current")
_LgpConditionAutoReTransferPrimed_ObjectIdentity = ObjectIdentity
lgpConditionAutoReTransferPrimed = _LgpConditionAutoReTransferPrimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 45)
)
if mibBuilder.loadTexts:
    lgpConditionAutoReTransferPrimed.setStatus("current")
_LgpConditionSourcesOutOfSync_ObjectIdentity = ObjectIdentity
lgpConditionSourcesOutOfSync = _LgpConditionSourcesOutOfSync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 46)
)
if mibBuilder.loadTexts:
    lgpConditionSourcesOutOfSync.setStatus("current")
_LgpConditionSourceFailure_ObjectIdentity = ObjectIdentity
lgpConditionSourceFailure = _LgpConditionSourceFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 47)
)
if mibBuilder.loadTexts:
    lgpConditionSourceFailure.setStatus("current")
_LgpConditionSource1Failure_ObjectIdentity = ObjectIdentity
lgpConditionSource1Failure = _LgpConditionSource1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 47, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1Failure.setStatus("current")
_LgpConditionSource2Failure_ObjectIdentity = ObjectIdentity
lgpConditionSource2Failure = _LgpConditionSource2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 47, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2Failure.setStatus("current")
_LgpConditionAutoReTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionAutoReTransferInhibited = _LgpConditionAutoReTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 48)
)
if mibBuilder.loadTexts:
    lgpConditionAutoReTransferInhibited.setStatus("current")
_LgpConditionAutoReTransferFailed_ObjectIdentity = ObjectIdentity
lgpConditionAutoReTransferFailed = _LgpConditionAutoReTransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 49)
)
if mibBuilder.loadTexts:
    lgpConditionAutoReTransferFailed.setStatus("current")
_LgpConditionFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionFuseOpen = _LgpConditionFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50)
)
if mibBuilder.loadTexts:
    lgpConditionFuseOpen.setStatus("current")
_LgpConditionControlFuse1Open_ObjectIdentity = ObjectIdentity
lgpConditionControlFuse1Open = _LgpConditionControlFuse1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 1)
)
if mibBuilder.loadTexts:
    lgpConditionControlFuse1Open.setStatus("current")
_LgpConditionControlFuse2Open_ObjectIdentity = ObjectIdentity
lgpConditionControlFuse2Open = _LgpConditionControlFuse2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 2)
)
if mibBuilder.loadTexts:
    lgpConditionControlFuse2Open.setStatus("current")
_LgpConditionRectifierFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionRectifierFuseOpen = _LgpConditionRectifierFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 3)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierFuseOpen.setStatus("current")
_LgpConditionInverterFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionInverterFuseOpen = _LgpConditionInverterFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInverterFuseOpen.setStatus("current")
_LgpConditionOutputToLoadFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadFuseOpen = _LgpConditionOutputToLoadFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 5)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadFuseOpen.setStatus("current")
_LgpConditionDcCapacitorFuseOpen_ObjectIdentity = ObjectIdentity
lgpConditionDcCapacitorFuseOpen = _LgpConditionDcCapacitorFuseOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 50, 6)
)
if mibBuilder.loadTexts:
    lgpConditionDcCapacitorFuseOpen.setStatus("current")
_LgpConditionDisconnect_ObjectIdentity = ObjectIdentity
lgpConditionDisconnect = _LgpConditionDisconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51)
)
if mibBuilder.loadTexts:
    lgpConditionDisconnect.setStatus("current")
_LgpConditionSource1DisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1DisconnectOpen = _LgpConditionSource1DisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1DisconnectOpen.setStatus("current")
_LgpConditionSource2DisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2DisconnectOpen = _LgpConditionSource2DisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2DisconnectOpen.setStatus("current")
_LgpConditionSource1PduDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource1PduDisconnectOpen = _LgpConditionSource1PduDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PduDisconnectOpen.setStatus("current")
_LgpConditionSource2PduDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionSource2PduDisconnectOpen = _LgpConditionSource2PduDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PduDisconnectOpen.setStatus("current")
_LgpConditionOutputToLoadDisconnect1Open_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadDisconnect1Open = _LgpConditionOutputToLoadDisconnect1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 5)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadDisconnect1Open.setStatus("current")
_LgpConditionOutputToLoadDisconnect2Open_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadDisconnect2Open = _LgpConditionOutputToLoadDisconnect2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 6)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadDisconnect2Open.setStatus("current")
_LgpConditionSource1BypassDisconnectClosed_ObjectIdentity = ObjectIdentity
lgpConditionSource1BypassDisconnectClosed = _LgpConditionSource1BypassDisconnectClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 7)
)
if mibBuilder.loadTexts:
    lgpConditionSource1BypassDisconnectClosed.setStatus("current")
_LgpConditionSource2BypassDisconnectClosed_ObjectIdentity = ObjectIdentity
lgpConditionSource2BypassDisconnectClosed = _LgpConditionSource2BypassDisconnectClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 8)
)
if mibBuilder.loadTexts:
    lgpConditionSource2BypassDisconnectClosed.setStatus("current")
_LgpConditionOutputToLoadNeutralDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadNeutralDisconnectOpen = _LgpConditionOutputToLoadNeutralDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 9)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadNeutralDisconnectOpen.setStatus("current")
_LgpConditionBatteryDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDisconnectOpen = _LgpConditionBatteryDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDisconnectOpen.setStatus("current")
_LgpConditionBatteryDiscOpenCab01_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab01 = _LgpConditionBatteryDiscOpenCab01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab01.setStatus("current")
_LgpConditionBatteryDiscOpenCab02_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab02 = _LgpConditionBatteryDiscOpenCab02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 2)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab02.setStatus("current")
_LgpConditionBatteryDiscOpenCab03_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab03 = _LgpConditionBatteryDiscOpenCab03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab03.setStatus("current")
_LgpConditionBatteryDiscOpenCab04_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab04 = _LgpConditionBatteryDiscOpenCab04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 4)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab04.setStatus("current")
_LgpConditionBatteryDiscOpenCab05_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab05 = _LgpConditionBatteryDiscOpenCab05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab05.setStatus("current")
_LgpConditionBatteryDiscOpenCab06_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab06 = _LgpConditionBatteryDiscOpenCab06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 6)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab06.setStatus("current")
_LgpConditionBatteryDiscOpenCab07_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab07 = _LgpConditionBatteryDiscOpenCab07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab07.setStatus("current")
_LgpConditionBatteryDiscOpenCab08_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDiscOpenCab08 = _LgpConditionBatteryDiscOpenCab08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 10, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDiscOpenCab08.setStatus("current")
_LgpConditionInputDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionInputDisconnectOpen = _LgpConditionInputDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 11)
)
if mibBuilder.loadTexts:
    lgpConditionInputDisconnectOpen.setStatus("current")
_LgpConditionOutputToLoadDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadDisconnectOpen = _LgpConditionOutputToLoadDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 12)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadDisconnectOpen.setStatus("current")
_LgpConditionBypassDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionBypassDisconnectOpen = _LgpConditionBypassDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 13)
)
if mibBuilder.loadTexts:
    lgpConditionBypassDisconnectOpen.setStatus("current")
_LgpConditionStaticSwitchDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpConditionStaticSwitchDisconnectOpen = _LgpConditionStaticSwitchDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 14)
)
if mibBuilder.loadTexts:
    lgpConditionStaticSwitchDisconnectOpen.setStatus("current")
_LgpConditionBreakerOpenFailure_ObjectIdentity = ObjectIdentity
lgpConditionBreakerOpenFailure = _LgpConditionBreakerOpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 15)
)
if mibBuilder.loadTexts:
    lgpConditionBreakerOpenFailure.setStatus("current")
_LgpConditionBreakerCloseFailure_ObjectIdentity = ObjectIdentity
lgpConditionBreakerCloseFailure = _LgpConditionBreakerCloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 51, 16)
)
if mibBuilder.loadTexts:
    lgpConditionBreakerCloseFailure.setStatus("current")
_LgpConditionFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionFrequencyDeviation = _LgpConditionFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52)
)
if mibBuilder.loadTexts:
    lgpConditionFrequencyDeviation.setStatus("current")
_LgpConditionSource1FrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionSource1FrequencyDeviation = _LgpConditionSource1FrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1FrequencyDeviation.setStatus("current")
_LgpConditionSource2FrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionSource2FrequencyDeviation = _LgpConditionSource2FrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2FrequencyDeviation.setStatus("current")
_LgpConditionInputFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionInputFrequencyDeviation = _LgpConditionInputFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 3)
)
if mibBuilder.loadTexts:
    lgpConditionInputFrequencyDeviation.setStatus("current")
_LgpConditionOutputToLoadFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadFrequencyDeviation = _LgpConditionOutputToLoadFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 4)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadFrequencyDeviation.setStatus("current")
_LgpConditionBypassFrequencyDeviation_ObjectIdentity = ObjectIdentity
lgpConditionBypassFrequencyDeviation = _LgpConditionBypassFrequencyDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 52, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBypassFrequencyDeviation.setStatus("current")
_LgpConditionOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionOverCurrent = _LgpConditionOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53)
)
if mibBuilder.loadTexts:
    lgpConditionOverCurrent.setStatus("current")
_LgpConditionSource1OverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource1OverCurrent = _LgpConditionSource1OverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1OverCurrent.setStatus("current")
_LgpConditionSource2OverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource2OverCurrent = _LgpConditionSource2OverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2OverCurrent.setStatus("current")
_LgpConditionOutputToLoadOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrent = _LgpConditionOutputToLoadOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrent.setStatus("current")
_LgpConditionOutputToLoadOverCurrentPhsA_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrentPhsA = _LgpConditionOutputToLoadOverCurrentPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3, 1)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrentPhsA.setStatus("current")
_LgpConditionOutputToLoadOverCurrentPhsB_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrentPhsB = _LgpConditionOutputToLoadOverCurrentPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3, 2)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrentPhsB.setStatus("current")
_LgpConditionOutputToLoadOverCurrentPhsC_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOverCurrentPhsC = _LgpConditionOutputToLoadOverCurrentPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 3, 3)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOverCurrentPhsC.setStatus("current")
_LgpConditionGroundOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionGroundOverCurrent = _LgpConditionGroundOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 4)
)
if mibBuilder.loadTexts:
    lgpConditionGroundOverCurrent.setStatus("current")
_LgpConditionRectifierOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionRectifierOverCurrent = _LgpConditionRectifierOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 5)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierOverCurrent.setStatus("current")
_LgpConditionInverterOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrent = _LgpConditionInverterOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrent.setStatus("current")
_LgpConditionInverterOverCurrentPhsA_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrentPhsA = _LgpConditionInverterOverCurrentPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6, 1)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrentPhsA.setStatus("current")
_LgpConditionInverterOverCurrentPhsB_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrentPhsB = _LgpConditionInverterOverCurrentPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6, 2)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrentPhsB.setStatus("current")
_LgpConditionInverterOverCurrentPhsC_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverCurrentPhsC = _LgpConditionInverterOverCurrentPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 6, 3)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverCurrentPhsC.setStatus("current")
_LgpConditionBatteryConverterOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionBatteryConverterOverCurrent = _LgpConditionBatteryConverterOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 7)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryConverterOverCurrent.setStatus("current")
_LgpConditionBatteryBalancerOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionBatteryBalancerOverCurrent = _LgpConditionBatteryBalancerOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 8)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryBalancerOverCurrent.setStatus("current")
_LgpConditionHumidifierOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierOverCurrent = _LgpConditionHumidifierOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 9)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierOverCurrent.setStatus("current")
_LgpConditionInputOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionInputOverCurrent = _LgpConditionInputOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 10)
)
if mibBuilder.loadTexts:
    lgpConditionInputOverCurrent.setStatus("current")
_LgpConditionSource1NeutralOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource1NeutralOverCurrent = _LgpConditionSource1NeutralOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 11)
)
if mibBuilder.loadTexts:
    lgpConditionSource1NeutralOverCurrent.setStatus("current")
_LgpConditionSource2NeutralOverCurrent_ObjectIdentity = ObjectIdentity
lgpConditionSource2NeutralOverCurrent = _LgpConditionSource2NeutralOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 53, 12)
)
if mibBuilder.loadTexts:
    lgpConditionSource2NeutralOverCurrent.setStatus("current")
_LgpConditionSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSensorFailure = _LgpConditionSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54)
)
if mibBuilder.loadTexts:
    lgpConditionSensorFailure.setStatus("current")
_LgpConditionOutputToLoadVoltageSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadVoltageSensorFailure = _LgpConditionOutputToLoadVoltageSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 1)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadVoltageSensorFailure.setStatus("current")
_LgpConditionSource1VoltageSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1VoltageSensorFailure = _LgpConditionSource1VoltageSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource1VoltageSensorFailure.setStatus("current")
_LgpConditionSource2VoltageSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2VoltageSensorFailure = _LgpConditionSource2VoltageSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource2VoltageSensorFailure.setStatus("current")
_LgpConditionSource1ScrSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1ScrSensorFailure = _LgpConditionSource1ScrSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 4)
)
if mibBuilder.loadTexts:
    lgpConditionSource1ScrSensorFailure.setStatus("current")
_LgpConditionSource2ScrSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2ScrSensorFailure = _LgpConditionSource2ScrSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 5)
)
if mibBuilder.loadTexts:
    lgpConditionSource2ScrSensorFailure.setStatus("current")
_LgpConditionSource1CurrentSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1CurrentSensorFailure = _LgpConditionSource1CurrentSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 6)
)
if mibBuilder.loadTexts:
    lgpConditionSource1CurrentSensorFailure.setStatus("current")
_LgpConditionSource2CurrentSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2CurrentSensorFailure = _LgpConditionSource2CurrentSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 7)
)
if mibBuilder.loadTexts:
    lgpConditionSource2CurrentSensorFailure.setStatus("current")
_LgpConditionRoomTempHumiditySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRoomTempHumiditySensorFailure = _LgpConditionRoomTempHumiditySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 8)
)
if mibBuilder.loadTexts:
    lgpConditionRoomTempHumiditySensorFailure.setStatus("current")
_LgpConditionGlycolTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionGlycolTempSensorFailure = _LgpConditionGlycolTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 9)
)
if mibBuilder.loadTexts:
    lgpConditionGlycolTempSensorFailure.setStatus("current")
_LgpConditionLocal1SensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionLocal1SensorFailure = _LgpConditionLocal1SensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 10)
)
if mibBuilder.loadTexts:
    lgpConditionLocal1SensorFailure.setStatus("current")
_LgpConditionCompressor1SensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1SensorFailure = _LgpConditionCompressor1SensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 11)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1SensorFailure.setStatus("current")
_LgpConditionCompressor2SensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor2SensorFailure = _LgpConditionCompressor2SensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 12)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor2SensorFailure.setStatus("current")
_LgpConditionSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionSupplySensorFailure = _LgpConditionSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 13)
)
if mibBuilder.loadTexts:
    lgpConditionSupplySensorFailure.setStatus("current")
_LgpConditionCabinetTemperatureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCabinetTemperatureSensorFailure = _LgpConditionCabinetTemperatureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 14)
)
if mibBuilder.loadTexts:
    lgpConditionCabinetTemperatureSensorFailure.setStatus("current")
_LgpConditionCabinetHumiditySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCabinetHumiditySensorFailure = _LgpConditionCabinetHumiditySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 15)
)
if mibBuilder.loadTexts:
    lgpConditionCabinetHumiditySensorFailure.setStatus("current")
_LgpConditionRoomTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRoomTempSensorFailure = _LgpConditionRoomTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 16)
)
if mibBuilder.loadTexts:
    lgpConditionRoomTempSensorFailure.setStatus("current")
_LgpConditionBatteryTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTempSensorFailure = _LgpConditionBatteryTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 17)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTempSensorFailure.setStatus("current")
_LgpConditionAirSensorAFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirSensorAFailure = _LgpConditionAirSensorAFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 18)
)
if mibBuilder.loadTexts:
    lgpConditionAirSensorAFailure.setStatus("current")
_LgpConditionAirSensorBFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirSensorBFailure = _LgpConditionAirSensorBFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 19)
)
if mibBuilder.loadTexts:
    lgpConditionAirSensorBFailure.setStatus("current")
_LgpConditionChilledWaterSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterSupplySensorFailure = _LgpConditionChilledWaterSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 20)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterSupplySensorFailure.setStatus("current")
_LgpConditionRefrigerantSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRefrigerantSupplySensorFailure = _LgpConditionRefrigerantSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 21)
)
if mibBuilder.loadTexts:
    lgpConditionRefrigerantSupplySensorFailure.setStatus("current")
_LgpConditionFluidSupplySensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionFluidSupplySensorFailure = _LgpConditionFluidSupplySensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 22)
)
if mibBuilder.loadTexts:
    lgpConditionFluidSupplySensorFailure.setStatus("current")
_LgpConditionCompressorLowPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorLowPressureSensorFailure = _LgpConditionCompressorLowPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 23)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorLowPressureSensorFailure.setStatus("current")
_LgpConditionCompressor1LowPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressor1LowPressureSensorFailure = _LgpConditionCompressor1LowPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 23, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCompressor1LowPressureSensorFailure.setStatus("current")
_LgpConditionRemoteSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionRemoteSensorFailure = _LgpConditionRemoteSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 24)
)
if mibBuilder.loadTexts:
    lgpConditionRemoteSensorFailure.setStatus("current")
_LgpConditionAirSupplyTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirSupplyTempSensorFailure = _LgpConditionAirSupplyTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 25)
)
if mibBuilder.loadTexts:
    lgpConditionAirSupplyTempSensorFailure.setStatus("current")
_LgpConditionAirReturnTempSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionAirReturnTempSensorFailure = _LgpConditionAirReturnTempSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 26)
)
if mibBuilder.loadTexts:
    lgpConditionAirReturnTempSensorFailure.setStatus("current")
_LgpConditionCompressorHighPressureSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompressorHighPressureSensorFailure = _LgpConditionCompressorHighPressureSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 54, 27)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorHighPressureSensorFailure.setStatus("current")
_LgpConditionInternalCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionInternalCommunicationFailure = _LgpConditionInternalCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 55)
)
if mibBuilder.loadTexts:
    lgpConditionInternalCommunicationFailure.setStatus("current")
_LgpConditionExternalCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionExternalCommunicationFailure = _LgpConditionExternalCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 56)
)
if mibBuilder.loadTexts:
    lgpConditionExternalCommunicationFailure.setStatus("current")
_LgpConditionSourceGateDriveFailure_ObjectIdentity = ObjectIdentity
lgpConditionSourceGateDriveFailure = _LgpConditionSourceGateDriveFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 57)
)
if mibBuilder.loadTexts:
    lgpConditionSourceGateDriveFailure.setStatus("current")
_LgpConditionSource1GateDriveFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1GateDriveFailure = _LgpConditionSource1GateDriveFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 57, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1GateDriveFailure.setStatus("current")
_LgpConditionSource2GateDriveFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2GateDriveFailure = _LgpConditionSource2GateDriveFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 57, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2GateDriveFailure.setStatus("current")
_LgpConditionDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionDisconnectFailure = _LgpConditionDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58)
)
if mibBuilder.loadTexts:
    lgpConditionDisconnectFailure.setStatus("current")
_LgpConditionOutputToLoadNeutralDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadNeutralDisconnectFailure = _LgpConditionOutputToLoadNeutralDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 1)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadNeutralDisconnectFailure.setStatus("current")
_LgpConditionSource1DisconnectShuntTripFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource1DisconnectShuntTripFailure = _LgpConditionSource1DisconnectShuntTripFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource1DisconnectShuntTripFailure.setStatus("current")
_LgpConditionSource2DisconnectShuntTripFailure_ObjectIdentity = ObjectIdentity
lgpConditionSource2DisconnectShuntTripFailure = _LgpConditionSource2DisconnectShuntTripFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSource2DisconnectShuntTripFailure.setStatus("current")
_LgpConditionInverterDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionInverterDisconnectFailure = _LgpConditionInverterDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInverterDisconnectFailure.setStatus("current")
_LgpConditionBatteryDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryDisconnectFailure = _LgpConditionBatteryDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryDisconnectFailure.setStatus("current")
_LgpConditionRectifierDisconnectFailure_ObjectIdentity = ObjectIdentity
lgpConditionRectifierDisconnectFailure = _LgpConditionRectifierDisconnectFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 58, 6)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierDisconnectFailure.setStatus("current")
_LgpConditionOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionOverTemperature = _LgpConditionOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59)
)
if mibBuilder.loadTexts:
    lgpConditionOverTemperature.setStatus("current")
_LgpConditionHeatSink1OverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionHeatSink1OverTemperature = _LgpConditionHeatSink1OverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHeatSink1OverTemperature.setStatus("current")
_LgpConditionAmbient1OverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionAmbient1OverTemperature = _LgpConditionAmbient1OverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 2)
)
if mibBuilder.loadTexts:
    lgpConditionAmbient1OverTemperature.setStatus("current")
_LgpConditionSystemOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionSystemOverTemperature = _LgpConditionSystemOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 3)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOverTemperature.setStatus("current")
_LgpConditionTransformerOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionTransformerOverTemperature = _LgpConditionTransformerOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 4)
)
if mibBuilder.loadTexts:
    lgpConditionTransformerOverTemperature.setStatus("current")
_LgpConditionBatteryOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionBatteryOverTemperature = _LgpConditionBatteryOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 5)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryOverTemperature.setStatus("current")
_LgpConditionRectifierOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionRectifierOverTemperature = _LgpConditionRectifierOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 6)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierOverTemperature.setStatus("current")
_LgpConditionInverterOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionInverterOverTemperature = _LgpConditionInverterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 7)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOverTemperature.setStatus("current")
_LgpConditionRectifierInductorOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionRectifierInductorOverTemperature = _LgpConditionRectifierInductorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 8)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierInductorOverTemperature.setStatus("current")
_LgpConditionInverterInductorOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionInverterInductorOverTemperature = _LgpConditionInverterInductorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 9)
)
if mibBuilder.loadTexts:
    lgpConditionInverterInductorOverTemperature.setStatus("current")
_LgpConditionBatteryConverterOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionBatteryConverterOverTemperature = _LgpConditionBatteryConverterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 10)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryConverterOverTemperature.setStatus("current")
_LgpConditionBatteryBalancerInductorOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionBatteryBalancerInductorOverTemperature = _LgpConditionBatteryBalancerInductorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 11)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryBalancerInductorOverTemperature.setStatus("current")
_LgpConditionChilledWaterOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterOverTemperature = _LgpConditionChilledWaterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 12)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterOverTemperature.setStatus("current")
_LgpConditionElectricHeatersOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionElectricHeatersOverTemperature = _LgpConditionElectricHeatersOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 13)
)
if mibBuilder.loadTexts:
    lgpConditionElectricHeatersOverTemperature.setStatus("current")
_LgpConditionInletAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpConditionInletAirOverTemperature = _LgpConditionInletAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 14)
)
if mibBuilder.loadTexts:
    lgpConditionInletAirOverTemperature.setStatus("current")
_LgpConditionSystemOverTempWarning_ObjectIdentity = ObjectIdentity
lgpConditionSystemOverTempWarning = _LgpConditionSystemOverTempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 15)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOverTempWarning.setStatus("current")
_LgpConditionHighTemperatureBattString_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureBattString = _LgpConditionHighTemperatureBattString_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 59, 16)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureBattString.setStatus("current")
_LgpConditionLoadOnAlternateSource_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnAlternateSource = _LgpConditionLoadOnAlternateSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 60)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnAlternateSource.setStatus("current")
_LgpConditionPhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionPhaseRotationError = _LgpConditionPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61)
)
if mibBuilder.loadTexts:
    lgpConditionPhaseRotationError.setStatus("current")
_LgpConditionSource1PhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionSource1PhaseRotationError = _LgpConditionSource1PhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 1)
)
if mibBuilder.loadTexts:
    lgpConditionSource1PhaseRotationError.setStatus("current")
_LgpConditionSource2PhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionSource2PhaseRotationError = _LgpConditionSource2PhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 2)
)
if mibBuilder.loadTexts:
    lgpConditionSource2PhaseRotationError.setStatus("current")
_LgpConditionBypassPhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionBypassPhaseRotationError = _LgpConditionBypassPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 3)
)
if mibBuilder.loadTexts:
    lgpConditionBypassPhaseRotationError.setStatus("current")
_LgpConditionInputPhaseRotationError_ObjectIdentity = ObjectIdentity
lgpConditionInputPhaseRotationError = _LgpConditionInputPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 61, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInputPhaseRotationError.setStatus("current")
_LgpConditionControlModuleFailure_ObjectIdentity = ObjectIdentity
lgpConditionControlModuleFailure = _LgpConditionControlModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 62)
)
if mibBuilder.loadTexts:
    lgpConditionControlModuleFailure.setStatus("current")
_LgpConditionControlModule1Failure_ObjectIdentity = ObjectIdentity
lgpConditionControlModule1Failure = _LgpConditionControlModule1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 62, 1)
)
if mibBuilder.loadTexts:
    lgpConditionControlModule1Failure.setStatus("current")
_LgpConditionHistoryLogFull_ObjectIdentity = ObjectIdentity
lgpConditionHistoryLogFull = _LgpConditionHistoryLogFull_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 63)
)
if mibBuilder.loadTexts:
    lgpConditionHistoryLogFull.setStatus("current")
_LgpConditionConfigurationModified_ObjectIdentity = ObjectIdentity
lgpConditionConfigurationModified = _LgpConditionConfigurationModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 64)
)
if mibBuilder.loadTexts:
    lgpConditionConfigurationModified.setStatus("current")
_LgpConditionPasswordModified_ObjectIdentity = ObjectIdentity
lgpConditionPasswordModified = _LgpConditionPasswordModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 65)
)
if mibBuilder.loadTexts:
    lgpConditionPasswordModified.setStatus("current")
_LgpConditionTimeModified_ObjectIdentity = ObjectIdentity
lgpConditionTimeModified = _LgpConditionTimeModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 66)
)
if mibBuilder.loadTexts:
    lgpConditionTimeModified.setStatus("current")
_LgpConditionDateModified_ObjectIdentity = ObjectIdentity
lgpConditionDateModified = _LgpConditionDateModified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 67)
)
if mibBuilder.loadTexts:
    lgpConditionDateModified.setStatus("current")
_LgpConditionEventLogCleared_ObjectIdentity = ObjectIdentity
lgpConditionEventLogCleared = _LgpConditionEventLogCleared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 68)
)
if mibBuilder.loadTexts:
    lgpConditionEventLogCleared.setStatus("current")
_LgpConditionHistoryLogCleared_ObjectIdentity = ObjectIdentity
lgpConditionHistoryLogCleared = _LgpConditionHistoryLogCleared_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 69)
)
if mibBuilder.loadTexts:
    lgpConditionHistoryLogCleared.setStatus("current")
_LgpConditionUtilityFailure_ObjectIdentity = ObjectIdentity
lgpConditionUtilityFailure = _LgpConditionUtilityFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 70)
)
if mibBuilder.loadTexts:
    lgpConditionUtilityFailure.setStatus("current")
_LgpConditionBatteryTestInProgress_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTestInProgress = _LgpConditionBatteryTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 71)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTestInProgress.setStatus("current")
_LgpConditionLoadOnBattery_ObjectIdentity = ObjectIdentity
lgpConditionLoadOnBattery = _LgpConditionLoadOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 72)
)
if mibBuilder.loadTexts:
    lgpConditionLoadOnBattery.setStatus("current")
_LgpConditionReplaceBattery_ObjectIdentity = ObjectIdentity
lgpConditionReplaceBattery = _LgpConditionReplaceBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 74)
)
if mibBuilder.loadTexts:
    lgpConditionReplaceBattery.setStatus("current")
_LgpConditionUpsShutdownPending_ObjectIdentity = ObjectIdentity
lgpConditionUpsShutdownPending = _LgpConditionUpsShutdownPending_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 75)
)
if mibBuilder.loadTexts:
    lgpConditionUpsShutdownPending.setStatus("current")
_LgpConditionBatteryChargerFailed_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargerFailed = _LgpConditionBatteryChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 76)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargerFailed.setStatus("current")
_LgpConditionBypassVoltageUnqualified_ObjectIdentity = ObjectIdentity
lgpConditionBypassVoltageUnqualified = _LgpConditionBypassVoltageUnqualified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 77)
)
if mibBuilder.loadTexts:
    lgpConditionBypassVoltageUnqualified.setStatus("current")
_LgpConditionCheckAirFilter_ObjectIdentity = ObjectIdentity
lgpConditionCheckAirFilter = _LgpConditionCheckAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 78)
)
if mibBuilder.loadTexts:
    lgpConditionCheckAirFilter.setStatus("current")
_LgpConditionBrownOut_ObjectIdentity = ObjectIdentity
lgpConditionBrownOut = _LgpConditionBrownOut_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 79)
)
if mibBuilder.loadTexts:
    lgpConditionBrownOut.setStatus("current")
_LgpConditionMultipleTransferLockout_ObjectIdentity = ObjectIdentity
lgpConditionMultipleTransferLockout = _LgpConditionMultipleTransferLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 80)
)
if mibBuilder.loadTexts:
    lgpConditionMultipleTransferLockout.setStatus("current")
_LgpConditionBypassPhaseLost_ObjectIdentity = ObjectIdentity
lgpConditionBypassPhaseLost = _LgpConditionBypassPhaseLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 81)
)
if mibBuilder.loadTexts:
    lgpConditionBypassPhaseLost.setStatus("current")
_LgpConditionMaintenceBypassInhibited_ObjectIdentity = ObjectIdentity
lgpConditionMaintenceBypassInhibited = _LgpConditionMaintenceBypassInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 82)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenceBypassInhibited.setStatus("current")
_LgpConditionLoadLockedOnBypass_ObjectIdentity = ObjectIdentity
lgpConditionLoadLockedOnBypass = _LgpConditionLoadLockedOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 83)
)
if mibBuilder.loadTexts:
    lgpConditionLoadLockedOnBypass.setStatus("current")
_LgpConditionOutputToLoadShort_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadShort = _LgpConditionOutputToLoadShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 84)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadShort.setStatus("current")
_LgpConditionEmergencyTransferToInverter_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyTransferToInverter = _LgpConditionEmergencyTransferToInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 85)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyTransferToInverter.setStatus("current")
_LgpConditonEmergencyPowerOff_ObjectIdentity = ObjectIdentity
lgpConditonEmergencyPowerOff = _LgpConditonEmergencyPowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 86)
)
if mibBuilder.loadTexts:
    lgpConditonEmergencyPowerOff.setStatus("current")
_LgpConditionInverterBackFeed_ObjectIdentity = ObjectIdentity
lgpConditionInverterBackFeed = _LgpConditionInverterBackFeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 87)
)
if mibBuilder.loadTexts:
    lgpConditionInverterBackFeed.setStatus("current")
_LgpConditionDcGroundFault_ObjectIdentity = ObjectIdentity
lgpConditionDcGroundFault = _LgpConditionDcGroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 88)
)
if mibBuilder.loadTexts:
    lgpConditionDcGroundFault.setStatus("current")
_LgpConditionDcGroundFaultPos_ObjectIdentity = ObjectIdentity
lgpConditionDcGroundFaultPos = _LgpConditionDcGroundFaultPos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 88, 1)
)
if mibBuilder.loadTexts:
    lgpConditionDcGroundFaultPos.setStatus("current")
_LgpConditionDcGroundFaultNeg_ObjectIdentity = ObjectIdentity
lgpConditionDcGroundFaultNeg = _LgpConditionDcGroundFaultNeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 88, 2)
)
if mibBuilder.loadTexts:
    lgpConditionDcGroundFaultNeg.setStatus("current")
_LgpConditionStaticTransferSwitchInhibited_ObjectIdentity = ObjectIdentity
lgpConditionStaticTransferSwitchInhibited = _LgpConditionStaticTransferSwitchInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 89)
)
if mibBuilder.loadTexts:
    lgpConditionStaticTransferSwitchInhibited.setStatus("current")
_LgpConditionBatteryLogFullWarning_ObjectIdentity = ObjectIdentity
lgpConditionBatteryLogFullWarning = _LgpConditionBatteryLogFullWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 90)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryLogFullWarning.setStatus("current")
_LgpConditionInputCurrentUnbalanced_ObjectIdentity = ObjectIdentity
lgpConditionInputCurrentUnbalanced = _LgpConditionInputCurrentUnbalanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 91)
)
if mibBuilder.loadTexts:
    lgpConditionInputCurrentUnbalanced.setStatus("current")
_LgpConditionSelfTestFailed_ObjectIdentity = ObjectIdentity
lgpConditionSelfTestFailed = _LgpConditionSelfTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 92)
)
if mibBuilder.loadTexts:
    lgpConditionSelfTestFailed.setStatus("current")
_LgpConditionInverterOutOfSynchronization_ObjectIdentity = ObjectIdentity
lgpConditionInverterOutOfSynchronization = _LgpConditionInverterOutOfSynchronization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 93)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOutOfSynchronization.setStatus("current")
_LgpConditionModuleAlarm_ObjectIdentity = ObjectIdentity
lgpConditionModuleAlarm = _LgpConditionModuleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94)
)
if mibBuilder.loadTexts:
    lgpConditionModuleAlarm.setStatus("current")
_LgpConditioniModuleUnit1Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit1Alarm = _LgpConditioniModuleUnit1Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 1)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit1Alarm.setStatus("current")
_LgpConditioniModuleUnit2Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit2Alarm = _LgpConditioniModuleUnit2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 2)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit2Alarm.setStatus("current")
_LgpConditioniModuleUnit3Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit3Alarm = _LgpConditioniModuleUnit3Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 3)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit3Alarm.setStatus("current")
_LgpConditioniModuleUnit4Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit4Alarm = _LgpConditioniModuleUnit4Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 4)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit4Alarm.setStatus("current")
_LgpConditioniModuleUnit5Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit5Alarm = _LgpConditioniModuleUnit5Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 5)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit5Alarm.setStatus("current")
_LgpConditioniModuleUnit6Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit6Alarm = _LgpConditioniModuleUnit6Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 6)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit6Alarm.setStatus("current")
_LgpConditioniModuleUnit7Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit7Alarm = _LgpConditioniModuleUnit7Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 7)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit7Alarm.setStatus("current")
_LgpConditioniModuleUnit8Alarm_ObjectIdentity = ObjectIdentity
lgpConditioniModuleUnit8Alarm = _LgpConditioniModuleUnit8Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 94, 8)
)
if mibBuilder.loadTexts:
    lgpConditioniModuleUnit8Alarm.setStatus("current")
_LgpConditionActiveModuleAlarm_ObjectIdentity = ObjectIdentity
lgpConditionActiveModuleAlarm = _LgpConditionActiveModuleAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 95)
)
if mibBuilder.loadTexts:
    lgpConditionActiveModuleAlarm.setStatus("current")
_LgpConditionControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionControlFailure = _LgpConditionControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96)
)
if mibBuilder.loadTexts:
    lgpConditionControlFailure.setStatus("current")
_LgpConditionMainControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionMainControlFailure = _LgpConditionMainControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMainControlFailure.setStatus("current")
_LgpConditionRedundantControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionRedundantControlFailure = _LgpConditionRedundantControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantControlFailure.setStatus("current")
_LgpConditionParallelSysControlFailure_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysControlFailure = _LgpConditionParallelSysControlFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 3)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysControlFailure.setStatus("current")
_LgpConditionMainControlCommFailure_ObjectIdentity = ObjectIdentity
lgpConditionMainControlCommFailure = _LgpConditionMainControlCommFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 4)
)
if mibBuilder.loadTexts:
    lgpConditionMainControlCommFailure.setStatus("current")
_LgpConditionControlBoardFailure_ObjectIdentity = ObjectIdentity
lgpConditionControlBoardFailure = _LgpConditionControlBoardFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 5)
)
if mibBuilder.loadTexts:
    lgpConditionControlBoardFailure.setStatus("current")
_LgpConditionHumidifierControlBdFailure_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierControlBdFailure = _LgpConditionHumidifierControlBdFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 96, 5, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierControlBdFailure.setStatus("current")
_LgpConditionControlWarning_ObjectIdentity = ObjectIdentity
lgpConditionControlWarning = _LgpConditionControlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 97)
)
if mibBuilder.loadTexts:
    lgpConditionControlWarning.setStatus("current")
_LgpConditionMainControlWarning_ObjectIdentity = ObjectIdentity
lgpConditionMainControlWarning = _LgpConditionMainControlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 97, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMainControlWarning.setStatus("current")
_LgpConditionRedundantControlWarning_ObjectIdentity = ObjectIdentity
lgpConditionRedundantControlWarning = _LgpConditionRedundantControlWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 97, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantControlWarning.setStatus("current")
_LgpConditionUserInterfaceFailure_ObjectIdentity = ObjectIdentity
lgpConditionUserInterfaceFailure = _LgpConditionUserInterfaceFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 98)
)
if mibBuilder.loadTexts:
    lgpConditionUserInterfaceFailure.setStatus("current")
_LgpConditionLostPowerRedundancy_ObjectIdentity = ObjectIdentity
lgpConditionLostPowerRedundancy = _LgpConditionLostPowerRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 99)
)
if mibBuilder.loadTexts:
    lgpConditionLostPowerRedundancy.setStatus("current")
_LgpConditionPowerModuleFailure_ObjectIdentity = ObjectIdentity
lgpConditionPowerModuleFailure = _LgpConditionPowerModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 100)
)
if mibBuilder.loadTexts:
    lgpConditionPowerModuleFailure.setStatus("current")
_LgpConditionBatteryModuleFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryModuleFailure = _LgpConditionBatteryModuleFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 101)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryModuleFailure.setStatus("current")
_LgpConditionOutputToLoadOff_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOff = _LgpConditionOutputToLoadOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 102)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOff.setStatus("current")
_LgpConditionSystemOff_ObjectIdentity = ObjectIdentity
lgpConditionSystemOff = _LgpConditionSystemOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 103)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOff.setStatus("current")
_LgpConditionRectifierStartupFailure_ObjectIdentity = ObjectIdentity
lgpConditionRectifierStartupFailure = _LgpConditionRectifierStartupFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 104)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierStartupFailure.setStatus("current")
_LgpConditionRectifierFault_ObjectIdentity = ObjectIdentity
lgpConditionRectifierFault = _LgpConditionRectifierFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 105)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierFault.setStatus("current")
_LgpConditionInverterShutdownLowDc_ObjectIdentity = ObjectIdentity
lgpConditionInverterShutdownLowDc = _LgpConditionInverterShutdownLowDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 106)
)
if mibBuilder.loadTexts:
    lgpConditionInverterShutdownLowDc.setStatus("current")
_LgpConditionInverterFault_ObjectIdentity = ObjectIdentity
lgpConditionInverterFault = _LgpConditionInverterFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 107)
)
if mibBuilder.loadTexts:
    lgpConditionInverterFault.setStatus("current")
_LgpConditionInverterDcOffsetOverrun_ObjectIdentity = ObjectIdentity
lgpConditionInverterDcOffsetOverrun = _LgpConditionInverterDcOffsetOverrun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 108)
)
if mibBuilder.loadTexts:
    lgpConditionInverterDcOffsetOverrun.setStatus("current")
_LgpConditionParallelSysLowBatteryWarning_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysLowBatteryWarning = _LgpConditionParallelSysLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 109)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysLowBatteryWarning.setStatus("current")
_LgpConditionParallelSysLoadShareFault_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysLoadShareFault = _LgpConditionParallelSysLoadShareFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 110)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysLoadShareFault.setStatus("current")
_LgpConditionBatteryFault_ObjectIdentity = ObjectIdentity
lgpConditionBatteryFault = _LgpConditionBatteryFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 111)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryFault.setStatus("current")
_LgpConditionBatteryConverterFailure_ObjectIdentity = ObjectIdentity
lgpConditionBatteryConverterFailure = _LgpConditionBatteryConverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 112)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryConverterFailure.setStatus("current")
_LgpConditionBatteryBalancerFault_ObjectIdentity = ObjectIdentity
lgpConditionBatteryBalancerFault = _LgpConditionBatteryBalancerFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 113)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryBalancerFault.setStatus("current")
_LgpConditionpsUpsOperationFault_ObjectIdentity = ObjectIdentity
lgpConditionpsUpsOperationFault = _LgpConditionpsUpsOperationFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 114)
)
if mibBuilder.loadTexts:
    lgpConditionpsUpsOperationFault.setStatus("deprecated")
_LgpConditionOutputToLoadOnJointMode_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadOnJointMode = _LgpConditionOutputToLoadOnJointMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 115)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadOnJointMode.setStatus("current")
_LgpConditionInputNeutralLost_ObjectIdentity = ObjectIdentity
lgpConditionInputNeutralLost = _LgpConditionInputNeutralLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 116)
)
if mibBuilder.loadTexts:
    lgpConditionInputNeutralLost.setStatus("current")
_LgpConditionLowBatteryWarning_ObjectIdentity = ObjectIdentity
lgpConditionLowBatteryWarning = _LgpConditionLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 117)
)
if mibBuilder.loadTexts:
    lgpConditionLowBatteryWarning.setStatus("current")
_LgpConditionInternalFault_ObjectIdentity = ObjectIdentity
lgpConditionInternalFault = _LgpConditionInternalFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 118)
)
if mibBuilder.loadTexts:
    lgpConditionInternalFault.setStatus("current")
_LgpConditionBatteryTestFailed_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTestFailed = _LgpConditionBatteryTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 119)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTestFailed.setStatus("current")
_LgpConditionPowerModuleWarning_ObjectIdentity = ObjectIdentity
lgpConditionPowerModuleWarning = _LgpConditionPowerModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 120)
)
if mibBuilder.loadTexts:
    lgpConditionPowerModuleWarning.setStatus("current")
_LgpConditionBatteryModuleWarning_ObjectIdentity = ObjectIdentity
lgpConditionBatteryModuleWarning = _LgpConditionBatteryModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 121)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryModuleWarning.setStatus("current")
_LgpConditionControlModuleWarning_ObjectIdentity = ObjectIdentity
lgpConditionControlModuleWarning = _LgpConditionControlModuleWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 122)
)
if mibBuilder.loadTexts:
    lgpConditionControlModuleWarning.setStatus("current")
_LgpConditionUpsOperationFault_ObjectIdentity = ObjectIdentity
lgpConditionUpsOperationFault = _LgpConditionUpsOperationFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 123)
)
if mibBuilder.loadTexts:
    lgpConditionUpsOperationFault.setStatus("current")
_LgpConditionActiveAlarm_ObjectIdentity = ObjectIdentity
lgpConditionActiveAlarm = _LgpConditionActiveAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 124)
)
if mibBuilder.loadTexts:
    lgpConditionActiveAlarm.setStatus("current")
_LgpConditionRectifierCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionRectifierCommunicationFailure = _LgpConditionRectifierCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 125)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierCommunicationFailure.setStatus("current")
_LgpConditionInverterCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionInverterCommunicationFailure = _LgpConditionInverterCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 126)
)
if mibBuilder.loadTexts:
    lgpConditionInverterCommunicationFailure.setStatus("current")
_LgpConditionParallelSysConnectionFault_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysConnectionFault = _LgpConditionParallelSysConnectionFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 127)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysConnectionFault.setStatus("current")
_LgpConditionParallelSysCommunicationFailure_ObjectIdentity = ObjectIdentity
lgpConditionParallelSysCommunicationFailure = _LgpConditionParallelSysCommunicationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 128)
)
if mibBuilder.loadTexts:
    lgpConditionParallelSysCommunicationFailure.setStatus("current")
_LgpConditionLostBatteryRedundancy_ObjectIdentity = ObjectIdentity
lgpConditionLostBatteryRedundancy = _LgpConditionLostBatteryRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 129)
)
if mibBuilder.loadTexts:
    lgpConditionLostBatteryRedundancy.setStatus("current")
_LgpConditionCompPumpDownFailure_ObjectIdentity = ObjectIdentity
lgpConditionCompPumpDownFailure = _LgpConditionCompPumpDownFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 130)
)
if mibBuilder.loadTexts:
    lgpConditionCompPumpDownFailure.setStatus("current")
_LgpConditionComp1PumpDownFailure_ObjectIdentity = ObjectIdentity
lgpConditionComp1PumpDownFailure = _LgpConditionComp1PumpDownFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 130, 1)
)
if mibBuilder.loadTexts:
    lgpConditionComp1PumpDownFailure.setStatus("current")
_LgpConditionComp2PumpDownFailure_ObjectIdentity = ObjectIdentity
lgpConditionComp2PumpDownFailure = _LgpConditionComp2PumpDownFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 130, 2)
)
if mibBuilder.loadTexts:
    lgpConditionComp2PumpDownFailure.setStatus("current")
_LgpConditionChilledWaterLowWaterFlow_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterLowWaterFlow = _LgpConditionChilledWaterLowWaterFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 131)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterLowWaterFlow.setStatus("current")
_LgpConditionAirFilterClogged_ObjectIdentity = ObjectIdentity
lgpConditionAirFilterClogged = _LgpConditionAirFilterClogged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 132)
)
if mibBuilder.loadTexts:
    lgpConditionAirFilterClogged.setStatus("deprecated")
_LgpConditionHumidifierFailure_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierFailure = _LgpConditionHumidifierFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 133)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierFailure.setStatus("current")
_LgpConditionRunHoursExceeded_ObjectIdentity = ObjectIdentity
lgpConditionRunHoursExceeded = _LgpConditionRunHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134)
)
if mibBuilder.loadTexts:
    lgpConditionRunHoursExceeded.setStatus("current")
_LgpConditionUnitRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionUnitRunHrsExceeded = _LgpConditionUnitRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 1)
)
if mibBuilder.loadTexts:
    lgpConditionUnitRunHrsExceeded.setStatus("current")
_LgpConditionComp1RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionComp1RunHrsExceeded = _LgpConditionComp1RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 2)
)
if mibBuilder.loadTexts:
    lgpConditionComp1RunHrsExceeded.setStatus("current")
_LgpConditionComp2RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionComp2RunHrsExceeded = _LgpConditionComp2RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 3)
)
if mibBuilder.loadTexts:
    lgpConditionComp2RunHrsExceeded.setStatus("current")
_LgpConditionFreeCoolRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionFreeCoolRunHrsExceeded = _LgpConditionFreeCoolRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 4)
)
if mibBuilder.loadTexts:
    lgpConditionFreeCoolRunHrsExceeded.setStatus("current")
_LgpConditionElectricalHeater1RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionElectricalHeater1RunHrsExceeded = _LgpConditionElectricalHeater1RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 5)
)
if mibBuilder.loadTexts:
    lgpConditionElectricalHeater1RunHrsExceeded.setStatus("current")
_LgpConditionElectricalHeater2RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionElectricalHeater2RunHrsExceeded = _LgpConditionElectricalHeater2RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 6)
)
if mibBuilder.loadTexts:
    lgpConditionElectricalHeater2RunHrsExceeded.setStatus("current")
_LgpConditionElectricalHeater3RunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionElectricalHeater3RunHrsExceeded = _LgpConditionElectricalHeater3RunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 7)
)
if mibBuilder.loadTexts:
    lgpConditionElectricalHeater3RunHrsExceeded.setStatus("current")
_LgpConditionHotWaterRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionHotWaterRunHrsExceeded = _LgpConditionHotWaterRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 8)
)
if mibBuilder.loadTexts:
    lgpConditionHotWaterRunHrsExceeded.setStatus("current")
_LgpConditionHotGasRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionHotGasRunHrsExceeded = _LgpConditionHotGasRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 9)
)
if mibBuilder.loadTexts:
    lgpConditionHotGasRunHrsExceeded.setStatus("current")
_LgpConditionHumidifierRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierRunHrsExceeded = _LgpConditionHumidifierRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 10)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierRunHrsExceeded.setStatus("current")
_LgpConditionDehumidiferRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionDehumidiferRunHrsExceeded = _LgpConditionDehumidiferRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 11)
)
if mibBuilder.loadTexts:
    lgpConditionDehumidiferRunHrsExceeded.setStatus("current")
_LgpConditionFanRunHrsExceeded_ObjectIdentity = ObjectIdentity
lgpConditionFanRunHrsExceeded = _LgpConditionFanRunHrsExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 134, 12)
)
if mibBuilder.loadTexts:
    lgpConditionFanRunHrsExceeded.setStatus("current")
_LgpConditionCommWarning_ObjectIdentity = ObjectIdentity
lgpConditionCommWarning = _LgpConditionCommWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarning.setStatus("current")
_LgpConditionCommWarningUnit1_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit1 = _LgpConditionCommWarningUnit1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit1.setStatus("current")
_LgpConditionCommWarningUnit2_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit2 = _LgpConditionCommWarningUnit2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit2.setStatus("current")
_LgpConditionCommWarningUnit3_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit3 = _LgpConditionCommWarningUnit3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit3.setStatus("current")
_LgpConditionCommWarningUnit4_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit4 = _LgpConditionCommWarningUnit4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 4)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit4.setStatus("current")
_LgpConditionCommWarningUnit5_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit5 = _LgpConditionCommWarningUnit5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 5)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit5.setStatus("current")
_LgpConditionCommWarningUnit6_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit6 = _LgpConditionCommWarningUnit6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 6)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit6.setStatus("current")
_LgpConditionCommWarningUnit7_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit7 = _LgpConditionCommWarningUnit7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 7)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit7.setStatus("current")
_LgpConditionCommWarningUnit8_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit8 = _LgpConditionCommWarningUnit8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 8)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit8.setStatus("current")
_LgpConditionCommWarningUnit9_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit9 = _LgpConditionCommWarningUnit9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 9)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit9.setStatus("current")
_LgpConditionCommWarningUnit10_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit10 = _LgpConditionCommWarningUnit10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 10)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit10.setStatus("current")
_LgpConditionCommWarningUnit11_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit11 = _LgpConditionCommWarningUnit11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 11)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit11.setStatus("current")
_LgpConditionCommWarningUnit12_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit12 = _LgpConditionCommWarningUnit12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 12)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit12.setStatus("current")
_LgpConditionCommWarningUnit13_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit13 = _LgpConditionCommWarningUnit13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 13)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit13.setStatus("current")
_LgpConditionCommWarningUnit14_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit14 = _LgpConditionCommWarningUnit14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 14)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit14.setStatus("current")
_LgpConditionCommWarningUnit15_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit15 = _LgpConditionCommWarningUnit15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 15)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit15.setStatus("current")
_LgpConditionCommWarningUnit16_ObjectIdentity = ObjectIdentity
lgpConditionCommWarningUnit16 = _LgpConditionCommWarningUnit16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 135, 16)
)
if mibBuilder.loadTexts:
    lgpConditionCommWarningUnit16.setStatus("current")
_LgpConditionUnitOn_ObjectIdentity = ObjectIdentity
lgpConditionUnitOn = _LgpConditionUnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 136)
)
if mibBuilder.loadTexts:
    lgpConditionUnitOn.setStatus("current")
_LgpConditionUnitOff_ObjectIdentity = ObjectIdentity
lgpConditionUnitOff = _LgpConditionUnitOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 137)
)
if mibBuilder.loadTexts:
    lgpConditionUnitOff.setStatus("current")
_LgpConditionSleepModeOff_ObjectIdentity = ObjectIdentity
lgpConditionSleepModeOff = _LgpConditionSleepModeOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 138)
)
if mibBuilder.loadTexts:
    lgpConditionSleepModeOff.setStatus("current")
_LgpConditionPowerOn_ObjectIdentity = ObjectIdentity
lgpConditionPowerOn = _LgpConditionPowerOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 139)
)
if mibBuilder.loadTexts:
    lgpConditionPowerOn.setStatus("current")
_LgpConditionSystemOnStanby_ObjectIdentity = ObjectIdentity
lgpConditionSystemOnStanby = _LgpConditionSystemOnStanby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 140)
)
if mibBuilder.loadTexts:
    lgpConditionSystemOnStanby.setStatus("current")
_LgpConditionPowerOff_ObjectIdentity = ObjectIdentity
lgpConditionPowerOff = _LgpConditionPowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 141)
)
if mibBuilder.loadTexts:
    lgpConditionPowerOff.setStatus("current")
_LgpConditionHighTemperatureGroup_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureGroup = _LgpConditionHighTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureGroup.setStatus("current")
_LgpConditionHighTemperatureSensor1_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureSensor1 = _LgpConditionHighTemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureSensor1.setStatus("current")
_LgpConditionHighTemperatureDigitalScroll1_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureDigitalScroll1 = _LgpConditionHighTemperatureDigitalScroll1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 2)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureDigitalScroll1.setStatus("current")
_LgpConditionHighTemperatureDigitalScroll2_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureDigitalScroll2 = _LgpConditionHighTemperatureDigitalScroll2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 3)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureDigitalScroll2.setStatus("current")
_LgpConditionHighTemperatureUser1_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureUser1 = _LgpConditionHighTemperatureUser1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 4)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureUser1.setStatus("current")
_LgpConditionHighTemperatureInternal_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureInternal = _LgpConditionHighTemperatureInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 5)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureInternal.setStatus("current")
_LgpConditionHighTemperatureExternalAirSensorA_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureExternalAirSensorA = _LgpConditionHighTemperatureExternalAirSensorA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 6)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureExternalAirSensorA.setStatus("current")
_LgpConditionHighTemperatureExternalAirSensorB_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureExternalAirSensorB = _LgpConditionHighTemperatureExternalAirSensorB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 7)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureExternalAirSensorB.setStatus("current")
_LgpConditionHighTemperatureRefrigerantSupply_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureRefrigerantSupply = _LgpConditionHighTemperatureRefrigerantSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 8)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureRefrigerantSupply.setStatus("current")
_LgpConditionHighTemperatureFluidSupply_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureFluidSupply = _LgpConditionHighTemperatureFluidSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 9)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureFluidSupply.setStatus("current")
_LgpConditionHighTemperatureSupplyAir_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureSupplyAir = _LgpConditionHighTemperatureSupplyAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 10)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureSupplyAir.setStatus("current")
_LgpConditionHighTemperatureReturnAir_ObjectIdentity = ObjectIdentity
lgpConditionHighTemperatureReturnAir = _LgpConditionHighTemperatureReturnAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 142, 11)
)
if mibBuilder.loadTexts:
    lgpConditionHighTemperatureReturnAir.setStatus("current")
_LgpConditionLowTemperatureGroup_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureGroup = _LgpConditionLowTemperatureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureGroup.setStatus("current")
_LgpConditionLowTemperatureSensor1_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureSensor1 = _LgpConditionLowTemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureSensor1.setStatus("current")
_LgpConditionLowTemperatureInternal_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureInternal = _LgpConditionLowTemperatureInternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureInternal.setStatus("current")
_LgpConditionLowTemperatureExternalAirSensorA_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureExternalAirSensorA = _LgpConditionLowTemperatureExternalAirSensorA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 3)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureExternalAirSensorA.setStatus("current")
_LgpConditionLowTemperatureExternalAirSensorB_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureExternalAirSensorB = _LgpConditionLowTemperatureExternalAirSensorB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 4)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureExternalAirSensorB.setStatus("current")
_LgpConditionLowTemperatureRefrigerantSupply_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureRefrigerantSupply = _LgpConditionLowTemperatureRefrigerantSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 5)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureRefrigerantSupply.setStatus("current")
_LgpConditionLowTemperatureFluidSupply_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureFluidSupply = _LgpConditionLowTemperatureFluidSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 6)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureFluidSupply.setStatus("current")
_LgpConditionLowTemperatureSupplyAir_ObjectIdentity = ObjectIdentity
lgpConditionLowTemperatureSupplyAir = _LgpConditionLowTemperatureSupplyAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 143, 7)
)
if mibBuilder.loadTexts:
    lgpConditionLowTemperatureSupplyAir.setStatus("current")
_LgpConditionHighHumidityGroup_ObjectIdentity = ObjectIdentity
lgpConditionHighHumidityGroup = _LgpConditionHighHumidityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 144)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumidityGroup.setStatus("current")
_LgpConditionHighHumiditySensor1_ObjectIdentity = ObjectIdentity
lgpConditionHighHumiditySensor1 = _LgpConditionHighHumiditySensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 144, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumiditySensor1.setStatus("current")
_LgpConditionHighHumidityReturnAir_ObjectIdentity = ObjectIdentity
lgpConditionHighHumidityReturnAir = _LgpConditionHighHumidityReturnAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 144, 2)
)
if mibBuilder.loadTexts:
    lgpConditionHighHumidityReturnAir.setStatus("current")
_LgpConditionLowHumidityGroup_ObjectIdentity = ObjectIdentity
lgpConditionLowHumidityGroup = _LgpConditionLowHumidityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 145)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumidityGroup.setStatus("current")
_LgpConditionLowHumiditySensor1_ObjectIdentity = ObjectIdentity
lgpConditionLowHumiditySensor1 = _LgpConditionLowHumiditySensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 145, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumiditySensor1.setStatus("current")
_LgpConditionLowHumidityReturnAir_ObjectIdentity = ObjectIdentity
lgpConditionLowHumidityReturnAir = _LgpConditionLowHumidityReturnAir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 145, 2)
)
if mibBuilder.loadTexts:
    lgpConditionLowHumidityReturnAir.setStatus("current")
_LgpConditionPeerNetworkNoMaster_ObjectIdentity = ObjectIdentity
lgpConditionPeerNetworkNoMaster = _LgpConditionPeerNetworkNoMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 146)
)
if mibBuilder.loadTexts:
    lgpConditionPeerNetworkNoMaster.setStatus("current")
_LgpConditionNoOnOffPermissions_ObjectIdentity = ObjectIdentity
lgpConditionNoOnOffPermissions = _LgpConditionNoOnOffPermissions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 147)
)
if mibBuilder.loadTexts:
    lgpConditionNoOnOffPermissions.setStatus("current")
_LgpConditionPeerNetworkFailure_ObjectIdentity = ObjectIdentity
lgpConditionPeerNetworkFailure = _LgpConditionPeerNetworkFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 148)
)
if mibBuilder.loadTexts:
    lgpConditionPeerNetworkFailure.setStatus("current")
_LgpConditionUnitDisabled_ObjectIdentity = ObjectIdentity
lgpConditionUnitDisabled = _LgpConditionUnitDisabled_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 149)
)
if mibBuilder.loadTexts:
    lgpConditionUnitDisabled.setStatus("current")
_LgpConditionUnitShutdown_ObjectIdentity = ObjectIdentity
lgpConditionUnitShutdown = _LgpConditionUnitShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 150)
)
if mibBuilder.loadTexts:
    lgpConditionUnitShutdown.setStatus("current")
_LgpConditionPeerNetworkDiscovered_ObjectIdentity = ObjectIdentity
lgpConditionPeerNetworkDiscovered = _LgpConditionPeerNetworkDiscovered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 151)
)
if mibBuilder.loadTexts:
    lgpConditionPeerNetworkDiscovered.setStatus("current")
_LgpConditionLossOfWaterFlow_ObjectIdentity = ObjectIdentity
lgpConditionLossOfWaterFlow = _LgpConditionLossOfWaterFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 152)
)
if mibBuilder.loadTexts:
    lgpConditionLossOfWaterFlow.setStatus("current")
_LgpConditionCondensatePumpHighWater_ObjectIdentity = ObjectIdentity
lgpConditionCondensatePumpHighWater = _LgpConditionCondensatePumpHighWater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 153)
)
if mibBuilder.loadTexts:
    lgpConditionCondensatePumpHighWater.setStatus("current")
_LgpConditionGeneralAlarm_ObjectIdentity = ObjectIdentity
lgpConditionGeneralAlarm = _LgpConditionGeneralAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 154)
)
if mibBuilder.loadTexts:
    lgpConditionGeneralAlarm.setStatus("current")
_LgpConditionProductSpecific_ObjectIdentity = ObjectIdentity
lgpConditionProductSpecific = _LgpConditionProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 155)
)
if mibBuilder.loadTexts:
    lgpConditionProductSpecific.setStatus("current")
_LgpConditionReheatLockout_ObjectIdentity = ObjectIdentity
lgpConditionReheatLockout = _LgpConditionReheatLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 156)
)
if mibBuilder.loadTexts:
    lgpConditionReheatLockout.setStatus("current")
_LgpConditionHumidifierLockout_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierLockout = _LgpConditionHumidifierLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 157)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierLockout.setStatus("current")
_LgpConditionCompressorsLockout_ObjectIdentity = ObjectIdentity
lgpConditionCompressorsLockout = _LgpConditionCompressorsLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 158)
)
if mibBuilder.loadTexts:
    lgpConditionCompressorsLockout.setStatus("current")
_LgpConditionCallService_ObjectIdentity = ObjectIdentity
lgpConditionCallService = _LgpConditionCallService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 159)
)
if mibBuilder.loadTexts:
    lgpConditionCallService.setStatus("current")
_LgpConditionLowMemoryGroup_ObjectIdentity = ObjectIdentity
lgpConditionLowMemoryGroup = _LgpConditionLowMemoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 160)
)
if mibBuilder.loadTexts:
    lgpConditionLowMemoryGroup.setStatus("current")
_LgpConditionLowMemory1_ObjectIdentity = ObjectIdentity
lgpConditionLowMemory1 = _LgpConditionLowMemory1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 160, 1)
)
if mibBuilder.loadTexts:
    lgpConditionLowMemory1.setStatus("current")
_LgpConditionMemoryFailureGroup_ObjectIdentity = ObjectIdentity
lgpConditionMemoryFailureGroup = _LgpConditionMemoryFailureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 161)
)
if mibBuilder.loadTexts:
    lgpConditionMemoryFailureGroup.setStatus("current")
_LgpConditionMemory1Failure_ObjectIdentity = ObjectIdentity
lgpConditionMemory1Failure = _LgpConditionMemory1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 161, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMemory1Failure.setStatus("current")
_LgpConditionMemory2Failure_ObjectIdentity = ObjectIdentity
lgpConditionMemory2Failure = _LgpConditionMemory2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 161, 2)
)
if mibBuilder.loadTexts:
    lgpConditionMemory2Failure.setStatus("current")
_LgpConditionUnitCodeErrorGroup_ObjectIdentity = ObjectIdentity
lgpConditionUnitCodeErrorGroup = _LgpConditionUnitCodeErrorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCodeErrorGroup.setStatus("current")
_LgpConditionUnitCodeNotConfigured_ObjectIdentity = ObjectIdentity
lgpConditionUnitCodeNotConfigured = _LgpConditionUnitCodeNotConfigured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 1)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCodeNotConfigured.setStatus("current")
_LgpConditionUnitCode01OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode01OutOfRange = _LgpConditionUnitCode01OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 2)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode01OutOfRange.setStatus("current")
_LgpConditionUnitCode02OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode02OutOfRange = _LgpConditionUnitCode02OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 3)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode02OutOfRange.setStatus("current")
_LgpConditionUnitCode03OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode03OutOfRange = _LgpConditionUnitCode03OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 4)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode03OutOfRange.setStatus("current")
_LgpConditionUnitCode04OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode04OutOfRange = _LgpConditionUnitCode04OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 5)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode04OutOfRange.setStatus("current")
_LgpConditionUnitCode05OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode05OutOfRange = _LgpConditionUnitCode05OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 6)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode05OutOfRange.setStatus("current")
_LgpConditionUnitCode06OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode06OutOfRange = _LgpConditionUnitCode06OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 7)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode06OutOfRange.setStatus("current")
_LgpConditionUnitCode07OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode07OutOfRange = _LgpConditionUnitCode07OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 8)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode07OutOfRange.setStatus("current")
_LgpConditionUnitCode08OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode08OutOfRange = _LgpConditionUnitCode08OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 9)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode08OutOfRange.setStatus("current")
_LgpConditionUnitCode09OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode09OutOfRange = _LgpConditionUnitCode09OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 10)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode09OutOfRange.setStatus("current")
_LgpConditionUnitCode10OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode10OutOfRange = _LgpConditionUnitCode10OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 11)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode10OutOfRange.setStatus("current")
_LgpConditionUnitCode11OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode11OutOfRange = _LgpConditionUnitCode11OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 12)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode11OutOfRange.setStatus("current")
_LgpConditionUnitCode12OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode12OutOfRange = _LgpConditionUnitCode12OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 13)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode12OutOfRange.setStatus("current")
_LgpConditionUnitCode13OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode13OutOfRange = _LgpConditionUnitCode13OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 14)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode13OutOfRange.setStatus("current")
_LgpConditionUnitCode14OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode14OutOfRange = _LgpConditionUnitCode14OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 15)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode14OutOfRange.setStatus("current")
_LgpConditionUnitCode15OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode15OutOfRange = _LgpConditionUnitCode15OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 16)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode15OutOfRange.setStatus("current")
_LgpConditionUnitCode16OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode16OutOfRange = _LgpConditionUnitCode16OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 17)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode16OutOfRange.setStatus("current")
_LgpConditionUnitCode17OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode17OutOfRange = _LgpConditionUnitCode17OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 18)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode17OutOfRange.setStatus("current")
_LgpConditionUnitCode18OutOfRange_ObjectIdentity = ObjectIdentity
lgpConditionUnitCode18OutOfRange = _LgpConditionUnitCode18OutOfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 162, 19)
)
if mibBuilder.loadTexts:
    lgpConditionUnitCode18OutOfRange.setStatus("current")
_LgpConditionHighExternalDewPoint_ObjectIdentity = ObjectIdentity
lgpConditionHighExternalDewPoint = _LgpConditionHighExternalDewPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 163)
)
if mibBuilder.loadTexts:
    lgpConditionHighExternalDewPoint.setStatus("current")
_LgpConditionHcbDisconnected_ObjectIdentity = ObjectIdentity
lgpConditionHcbDisconnected = _LgpConditionHcbDisconnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 164)
)
if mibBuilder.loadTexts:
    lgpConditionHcbDisconnected.setStatus("current")
_LgpConditionBmsResetTimerExpired_ObjectIdentity = ObjectIdentity
lgpConditionBmsResetTimerExpired = _LgpConditionBmsResetTimerExpired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 165)
)
if mibBuilder.loadTexts:
    lgpConditionBmsResetTimerExpired.setStatus("current")
_LgpConditionAgentFirmwareCorrupt_ObjectIdentity = ObjectIdentity
lgpConditionAgentFirmwareCorrupt = _LgpConditionAgentFirmwareCorrupt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 166)
)
if mibBuilder.loadTexts:
    lgpConditionAgentFirmwareCorrupt.setStatus("current")
_LgpConditionSystemAccessGroup_ObjectIdentity = ObjectIdentity
lgpConditionSystemAccessGroup = _LgpConditionSystemAccessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 175)
)
if mibBuilder.loadTexts:
    lgpConditionSystemAccessGroup.setStatus("current")
_LgpConditionFrontAccessOpen_ObjectIdentity = ObjectIdentity
lgpConditionFrontAccessOpen = _LgpConditionFrontAccessOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 175, 1)
)
if mibBuilder.loadTexts:
    lgpConditionFrontAccessOpen.setStatus("current")
_LgpConditionRearAccessOpen_ObjectIdentity = ObjectIdentity
lgpConditionRearAccessOpen = _LgpConditionRearAccessOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 175, 2)
)
if mibBuilder.loadTexts:
    lgpConditionRearAccessOpen.setStatus("current")
_LgpConditionsDamperFailure_ObjectIdentity = ObjectIdentity
lgpConditionsDamperFailure = _LgpConditionsDamperFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 176)
)
if mibBuilder.loadTexts:
    lgpConditionsDamperFailure.setStatus("current")
_LgpConditionEmergencyDamperFailure_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyDamperFailure = _LgpConditionEmergencyDamperFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 176, 1)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyDamperFailure.setStatus("current")
_LgpConditionRemoteShutdown_ObjectIdentity = ObjectIdentity
lgpConditionRemoteShutdown = _LgpConditionRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 177)
)
if mibBuilder.loadTexts:
    lgpConditionRemoteShutdown.setStatus("current")
_LgpConditionFireAlarm_ObjectIdentity = ObjectIdentity
lgpConditionFireAlarm = _LgpConditionFireAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 178)
)
if mibBuilder.loadTexts:
    lgpConditionFireAlarm.setStatus("current")
_LgpConditionHeatersOverheated_ObjectIdentity = ObjectIdentity
lgpConditionHeatersOverheated = _LgpConditionHeatersOverheated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 179)
)
if mibBuilder.loadTexts:
    lgpConditionHeatersOverheated.setStatus("current")
_LgpConditionCondenserFailureGroup_ObjectIdentity = ObjectIdentity
lgpConditionCondenserFailureGroup = _LgpConditionCondenserFailureGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserFailureGroup.setStatus("current")
_LgpConditionCondenser1Failure_ObjectIdentity = ObjectIdentity
lgpConditionCondenser1Failure = _LgpConditionCondenser1Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCondenser1Failure.setStatus("current")
_LgpConditionCondenser2Failure_ObjectIdentity = ObjectIdentity
lgpConditionCondenser2Failure = _LgpConditionCondenser2Failure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180, 2)
)
if mibBuilder.loadTexts:
    lgpConditionCondenser2Failure.setStatus("current")
_LgpConditionCondenserTVSSFailure_ObjectIdentity = ObjectIdentity
lgpConditionCondenserTVSSFailure = _LgpConditionCondenserTVSSFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 180, 3)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserTVSSFailure.setStatus("current")
_LgpConditionHumidifierCyclinderWorn_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierCyclinderWorn = _LgpConditionHumidifierCyclinderWorn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 181)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierCyclinderWorn.setStatus("current")
_LgpConditionUnderCurrent_ObjectIdentity = ObjectIdentity
lgpConditionUnderCurrent = _LgpConditionUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 182)
)
if mibBuilder.loadTexts:
    lgpConditionUnderCurrent.setStatus("current")
_LgpConditionHumidifierUnderCurrent_ObjectIdentity = ObjectIdentity
lgpConditionHumidifierUnderCurrent = _LgpConditionHumidifierUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 182, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHumidifierUnderCurrent.setStatus("current")
_LgpConditionInputUnderCurrent_ObjectIdentity = ObjectIdentity
lgpConditionInputUnderCurrent = _LgpConditionInputUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 182, 2)
)
if mibBuilder.loadTexts:
    lgpConditionInputUnderCurrent.setStatus("current")
_LgpConditionHeatRejectorGroup_ObjectIdentity = ObjectIdentity
lgpConditionHeatRejectorGroup = _LgpConditionHeatRejectorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 183)
)
if mibBuilder.loadTexts:
    lgpConditionHeatRejectorGroup.setStatus("current")
_LgpConditionHeatRejectorFanFailure_ObjectIdentity = ObjectIdentity
lgpConditionHeatRejectorFanFailure = _LgpConditionHeatRejectorFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 183, 1)
)
if mibBuilder.loadTexts:
    lgpConditionHeatRejectorFanFailure.setStatus("current")
_LgpConditionHeatRejectorVoltageSuppressionFailure_ObjectIdentity = ObjectIdentity
lgpConditionHeatRejectorVoltageSuppressionFailure = _LgpConditionHeatRejectorVoltageSuppressionFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 183, 2)
)
if mibBuilder.loadTexts:
    lgpConditionHeatRejectorVoltageSuppressionFailure.setStatus("current")
_LgpConditionFreeCoolLockout_ObjectIdentity = ObjectIdentity
lgpConditionFreeCoolLockout = _LgpConditionFreeCoolLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 184)
)
if mibBuilder.loadTexts:
    lgpConditionFreeCoolLockout.setStatus("current")
_LgpConditionWaterLeakSensorFailure_ObjectIdentity = ObjectIdentity
lgpConditionWaterLeakSensorFailure = _LgpConditionWaterLeakSensorFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 185)
)
if mibBuilder.loadTexts:
    lgpConditionWaterLeakSensorFailure.setStatus("current")
_LgpConditionNoLoadDetectedWarning_ObjectIdentity = ObjectIdentity
lgpConditionNoLoadDetectedWarning = _LgpConditionNoLoadDetectedWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 186)
)
if mibBuilder.loadTexts:
    lgpConditionNoLoadDetectedWarning.setStatus("current")
_LgpConditionFirmwareGroup_ObjectIdentity = ObjectIdentity
lgpConditionFirmwareGroup = _LgpConditionFirmwareGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 187)
)
if mibBuilder.loadTexts:
    lgpConditionFirmwareGroup.setStatus("current")
_LgpConditionFirmwareUpdateRequired_ObjectIdentity = ObjectIdentity
lgpConditionFirmwareUpdateRequired = _LgpConditionFirmwareUpdateRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 187, 3)
)
if mibBuilder.loadTexts:
    lgpConditionFirmwareUpdateRequired.setStatus("current")
_LgpConditionTestGroup_ObjectIdentity = ObjectIdentity
lgpConditionTestGroup = _LgpConditionTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 188)
)
if mibBuilder.loadTexts:
    lgpConditionTestGroup.setStatus("current")
_LgpConditionTest01_ObjectIdentity = ObjectIdentity
lgpConditionTest01 = _LgpConditionTest01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 188, 5)
)
if mibBuilder.loadTexts:
    lgpConditionTest01.setStatus("current")
_LgpConditionReceptacleBranchGroup_ObjectIdentity = ObjectIdentity
lgpConditionReceptacleBranchGroup = _LgpConditionReceptacleBranchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 190)
)
if mibBuilder.loadTexts:
    lgpConditionReceptacleBranchGroup.setStatus("current")
_LgpConditionRcpBranchFailure_ObjectIdentity = ObjectIdentity
lgpConditionRcpBranchFailure = _LgpConditionRcpBranchFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 190, 5)
)
if mibBuilder.loadTexts:
    lgpConditionRcpBranchFailure.setStatus("current")
_LgpConditionRcpBranchBreakerOpen_ObjectIdentity = ObjectIdentity
lgpConditionRcpBranchBreakerOpen = _LgpConditionRcpBranchBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 190, 10)
)
if mibBuilder.loadTexts:
    lgpConditionRcpBranchBreakerOpen.setStatus("current")
_LgpConditionInputUnqualified_ObjectIdentity = ObjectIdentity
lgpConditionInputUnqualified = _LgpConditionInputUnqualified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 192)
)
if mibBuilder.loadTexts:
    lgpConditionInputUnqualified.setStatus("current")
_LgpConditionBypassUnavailable_ObjectIdentity = ObjectIdentity
lgpConditionBypassUnavailable = _LgpConditionBypassUnavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 193)
)
if mibBuilder.loadTexts:
    lgpConditionBypassUnavailable.setStatus("current")
_LgpConditionAutoTransferFailed_ObjectIdentity = ObjectIdentity
lgpConditionAutoTransferFailed = _LgpConditionAutoTransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 194)
)
if mibBuilder.loadTexts:
    lgpConditionAutoTransferFailed.setStatus("current")
_LgpConditionSBSUnavailable_ObjectIdentity = ObjectIdentity
lgpConditionSBSUnavailable = _LgpConditionSBSUnavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 195)
)
if mibBuilder.loadTexts:
    lgpConditionSBSUnavailable.setStatus("current")
_LgpConditionSBSOverload_ObjectIdentity = ObjectIdentity
lgpConditionSBSOverload = _LgpConditionSBSOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 196)
)
if mibBuilder.loadTexts:
    lgpConditionSBSOverload.setStatus("current")
_LgpConditionExcessPulseParallel_ObjectIdentity = ObjectIdentity
lgpConditionExcessPulseParallel = _LgpConditionExcessPulseParallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 197)
)
if mibBuilder.loadTexts:
    lgpConditionExcessPulseParallel.setStatus("current")
_LgpConditionRemoteBypassSwitchOffExt_ObjectIdentity = ObjectIdentity
lgpConditionRemoteBypassSwitchOffExt = _LgpConditionRemoteBypassSwitchOffExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 198)
)
if mibBuilder.loadTexts:
    lgpConditionRemoteBypassSwitchOffExt.setStatus("current")
_LgpConditionManTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionManTransferInhibited = _LgpConditionManTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 199)
)
if mibBuilder.loadTexts:
    lgpConditionManTransferInhibited.setStatus("current")
_LgpConditionManReTransferInhibited_ObjectIdentity = ObjectIdentity
lgpConditionManReTransferInhibited = _LgpConditionManReTransferInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 200)
)
if mibBuilder.loadTexts:
    lgpConditionManReTransferInhibited.setStatus("current")
_LgpConditionBatteryChargeError_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargeError = _LgpConditionBatteryChargeError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 201)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargeError.setStatus("current")
_LgpConditionBatteryAutoTestInhibited_ObjectIdentity = ObjectIdentity
lgpConditionBatteryAutoTestInhibited = _LgpConditionBatteryAutoTestInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 202)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryAutoTestInhibited.setStatus("current")
_LgpConditionBatteryChargeReducedExt_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargeReducedExt = _LgpConditionBatteryChargeReducedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 203)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargeReducedExt.setStatus("current")
_LgpConditionBatteryCapacityLow_ObjectIdentity = ObjectIdentity
lgpConditionBatteryCapacityLow = _LgpConditionBatteryCapacityLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 204)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryCapacityLow.setStatus("current")
_LgpConditionBatteryTempImbalance_ObjectIdentity = ObjectIdentity
lgpConditionBatteryTempImbalance = _LgpConditionBatteryTempImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 205)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryTempImbalance.setStatus("current")
_LgpConditionBatteryEqualize_ObjectIdentity = ObjectIdentity
lgpConditionBatteryEqualize = _LgpConditionBatteryEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 206)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryEqualize.setStatus("current")
_LgpConditionBatteryChargeInhibitedExt_ObjectIdentity = ObjectIdentity
lgpConditionBatteryChargeInhibitedExt = _LgpConditionBatteryChargeInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 207)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryChargeInhibitedExt.setStatus("current")
_LgpConditionServiceExtBatteryMonitorGroup_ObjectIdentity = ObjectIdentity
lgpConditionServiceExtBatteryMonitorGroup = _LgpConditionServiceExtBatteryMonitorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 208)
)
if mibBuilder.loadTexts:
    lgpConditionServiceExtBatteryMonitorGroup.setStatus("current")
_LgpConditionServiceExtBatteryMonitor1_ObjectIdentity = ObjectIdentity
lgpConditionServiceExtBatteryMonitor1 = _LgpConditionServiceExtBatteryMonitor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 208, 1)
)
if mibBuilder.loadTexts:
    lgpConditionServiceExtBatteryMonitor1.setStatus("current")
_LgpConditionServiceExtBatteryMonitor2_ObjectIdentity = ObjectIdentity
lgpConditionServiceExtBatteryMonitor2 = _LgpConditionServiceExtBatteryMonitor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 208, 2)
)
if mibBuilder.loadTexts:
    lgpConditionServiceExtBatteryMonitor2.setStatus("current")
_LgpConditionBatteryGroundFault_ObjectIdentity = ObjectIdentity
lgpConditionBatteryGroundFault = _LgpConditionBatteryGroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 209)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryGroundFault.setStatus("current")
_LgpConditionBatteryLowShutdown_ObjectIdentity = ObjectIdentity
lgpConditionBatteryLowShutdown = _LgpConditionBatteryLowShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 210)
)
if mibBuilder.loadTexts:
    lgpConditionBatteryLowShutdown.setStatus("current")
_LgpConditionEmergencyPowerOffLocal_ObjectIdentity = ObjectIdentity
lgpConditionEmergencyPowerOffLocal = _LgpConditionEmergencyPowerOffLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 211)
)
if mibBuilder.loadTexts:
    lgpConditionEmergencyPowerOffLocal.setStatus("current")
_LgpConditionOutputLowPFLagging_ObjectIdentity = ObjectIdentity
lgpConditionOutputLowPFLagging = _LgpConditionOutputLowPFLagging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 212)
)
if mibBuilder.loadTexts:
    lgpConditionOutputLowPFLagging.setStatus("current")
_LgpConditionOutputLowPFLeading_ObjectIdentity = ObjectIdentity
lgpConditionOutputLowPFLeading = _LgpConditionOutputLowPFLeading_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 213)
)
if mibBuilder.loadTexts:
    lgpConditionOutputLowPFLeading.setStatus("current")
_LgpConditionOutputToLoadFault_ObjectIdentity = ObjectIdentity
lgpConditionOutputToLoadFault = _LgpConditionOutputToLoadFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 214)
)
if mibBuilder.loadTexts:
    lgpConditionOutputToLoadFault.setStatus("current")
_LgpConditionInvRestartInhibitedExt_ObjectIdentity = ObjectIdentity
lgpConditionInvRestartInhibitedExt = _LgpConditionInvRestartInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 215)
)
if mibBuilder.loadTexts:
    lgpConditionInvRestartInhibitedExt.setStatus("current")
_LgpConditionInverterShutdownOverload_ObjectIdentity = ObjectIdentity
lgpConditionInverterShutdownOverload = _LgpConditionInverterShutdownOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 216)
)
if mibBuilder.loadTexts:
    lgpConditionInverterShutdownOverload.setStatus("current")
_LgpConditionInverterOffExt_ObjectIdentity = ObjectIdentity
lgpConditionInverterOffExt = _LgpConditionInverterOffExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 217)
)
if mibBuilder.loadTexts:
    lgpConditionInverterOffExt.setStatus("current")
_LgpConditionInputContactGroup_ObjectIdentity = ObjectIdentity
lgpConditionInputContactGroup = _LgpConditionInputContactGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218)
)
if mibBuilder.loadTexts:
    lgpConditionInputContactGroup.setStatus("current")
_LgpConditionInputContact01_ObjectIdentity = ObjectIdentity
lgpConditionInputContact01 = _LgpConditionInputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 1)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact01.setStatus("current")
_LgpConditionInputContact02_ObjectIdentity = ObjectIdentity
lgpConditionInputContact02 = _LgpConditionInputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 2)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact02.setStatus("current")
_LgpConditionInputContact03_ObjectIdentity = ObjectIdentity
lgpConditionInputContact03 = _LgpConditionInputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 3)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact03.setStatus("current")
_LgpConditionInputContact04_ObjectIdentity = ObjectIdentity
lgpConditionInputContact04 = _LgpConditionInputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 4)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact04.setStatus("current")
_LgpConditionInputContact05_ObjectIdentity = ObjectIdentity
lgpConditionInputContact05 = _LgpConditionInputContact05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 5)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact05.setStatus("current")
_LgpConditionInputContact06_ObjectIdentity = ObjectIdentity
lgpConditionInputContact06 = _LgpConditionInputContact06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 6)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact06.setStatus("current")
_LgpConditionInputContact07_ObjectIdentity = ObjectIdentity
lgpConditionInputContact07 = _LgpConditionInputContact07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 7)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact07.setStatus("current")
_LgpConditionInputContact08_ObjectIdentity = ObjectIdentity
lgpConditionInputContact08 = _LgpConditionInputContact08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 8)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact08.setStatus("current")
_LgpConditionInputContact09_ObjectIdentity = ObjectIdentity
lgpConditionInputContact09 = _LgpConditionInputContact09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 9)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact09.setStatus("current")
_LgpConditionInputContact10_ObjectIdentity = ObjectIdentity
lgpConditionInputContact10 = _LgpConditionInputContact10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 10)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact10.setStatus("current")
_LgpConditionInputContact11_ObjectIdentity = ObjectIdentity
lgpConditionInputContact11 = _LgpConditionInputContact11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 11)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact11.setStatus("current")
_LgpConditionInputContact12_ObjectIdentity = ObjectIdentity
lgpConditionInputContact12 = _LgpConditionInputContact12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 12)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact12.setStatus("current")
_LgpConditionInputContact13_ObjectIdentity = ObjectIdentity
lgpConditionInputContact13 = _LgpConditionInputContact13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 13)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact13.setStatus("current")
_LgpConditionInputContact14_ObjectIdentity = ObjectIdentity
lgpConditionInputContact14 = _LgpConditionInputContact14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 14)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact14.setStatus("current")
_LgpConditionInputContact15_ObjectIdentity = ObjectIdentity
lgpConditionInputContact15 = _LgpConditionInputContact15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 15)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact15.setStatus("current")
_LgpConditionInputContact16_ObjectIdentity = ObjectIdentity
lgpConditionInputContact16 = _LgpConditionInputContact16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 218, 16)
)
if mibBuilder.loadTexts:
    lgpConditionInputContact16.setStatus("current")
_LgpConditionRectifierOperInhibited_ObjectIdentity = ObjectIdentity
lgpConditionRectifierOperInhibited = _LgpConditionRectifierOperInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 219)
)
if mibBuilder.loadTexts:
    lgpConditionRectifierOperInhibited.setStatus("current")
_LgpConditionBypassBackFeedBrkrOpen_ObjectIdentity = ObjectIdentity
lgpConditionBypassBackFeedBrkrOpen = _LgpConditionBypassBackFeedBrkrOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 220)
)
if mibBuilder.loadTexts:
    lgpConditionBypassBackFeedBrkrOpen.setStatus("current")
_LgpConditionAutoRestartInProgress_ObjectIdentity = ObjectIdentity
lgpConditionAutoRestartInProgress = _LgpConditionAutoRestartInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 221)
)
if mibBuilder.loadTexts:
    lgpConditionAutoRestartInProgress.setStatus("current")
_LgpConditionAutoRestartInhibitedExt_ObjectIdentity = ObjectIdentity
lgpConditionAutoRestartInhibitedExt = _LgpConditionAutoRestartInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 222)
)
if mibBuilder.loadTexts:
    lgpConditionAutoRestartInhibitedExt.setStatus("current")
_LgpConditionAutoRestartFailed_ObjectIdentity = ObjectIdentity
lgpConditionAutoRestartFailed = _LgpConditionAutoRestartFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 223)
)
if mibBuilder.loadTexts:
    lgpConditionAutoRestartFailed.setStatus("current")
_LgpConditionInputOnGenerator_ObjectIdentity = ObjectIdentity
lgpConditionInputOnGenerator = _LgpConditionInputOnGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 224)
)
if mibBuilder.loadTexts:
    lgpConditionInputOnGenerator.setStatus("current")
_LgpConditionInputFilterCycleLock_ObjectIdentity = ObjectIdentity
lgpConditionInputFilterCycleLock = _LgpConditionInputFilterCycleLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 225)
)
if mibBuilder.loadTexts:
    lgpConditionInputFilterCycleLock.setStatus("current")
_LgpConditionServiceCodeActive_ObjectIdentity = ObjectIdentity
lgpConditionServiceCodeActive = _LgpConditionServiceCodeActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 226)
)
if mibBuilder.loadTexts:
    lgpConditionServiceCodeActive.setStatus("current")
_LgpConditionLoadBusSyncActive_ObjectIdentity = ObjectIdentity
lgpConditionLoadBusSyncActive = _LgpConditionLoadBusSyncActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 227)
)
if mibBuilder.loadTexts:
    lgpConditionLoadBusSyncActive.setStatus("current")
_LgpConditionLoadBusSyncInhibited_ObjectIdentity = ObjectIdentity
lgpConditionLoadBusSyncInhibited = _LgpConditionLoadBusSyncInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 228)
)
if mibBuilder.loadTexts:
    lgpConditionLoadBusSyncInhibited.setStatus("current")
_LgpConditionControlsResetRequired_ObjectIdentity = ObjectIdentity
lgpConditionControlsResetRequired = _LgpConditionControlsResetRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 229)
)
if mibBuilder.loadTexts:
    lgpConditionControlsResetRequired.setStatus("current")
_LgpConditionEquipTempSensorFailed_ObjectIdentity = ObjectIdentity
lgpConditionEquipTempSensorFailed = _LgpConditionEquipTempSensorFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 230)
)
if mibBuilder.loadTexts:
    lgpConditionEquipTempSensorFailed.setStatus("current")
_LgpConditionInputCurrentImbalance_ObjectIdentity = ObjectIdentity
lgpConditionInputCurrentImbalance = _LgpConditionInputCurrentImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 231)
)
if mibBuilder.loadTexts:
    lgpConditionInputCurrentImbalance.setStatus("current")
_LgpConditionPumpGroup_ObjectIdentity = ObjectIdentity
lgpConditionPumpGroup = _LgpConditionPumpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232)
)
if mibBuilder.loadTexts:
    lgpConditionPumpGroup.setStatus("current")
_LgpConditionPumpFlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionPumpFlowLoss = _LgpConditionPumpFlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPumpFlowLoss.setStatus("current")
_LgpConditionPump1FlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionPump1FlowLoss = _LgpConditionPump1FlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 1, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPump1FlowLoss.setStatus("current")
_LgpConditionPump2FlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionPump2FlowLoss = _LgpConditionPump2FlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 1, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPump2FlowLoss.setStatus("current")
_LgpConditionPumpShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPumpShortCycle = _LgpConditionPumpShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPumpShortCycle.setStatus("current")
_LgpConditionPumpInverterShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPumpInverterShortCycle = _LgpConditionPumpInverterShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 3)
)
if mibBuilder.loadTexts:
    lgpConditionPumpInverterShortCycle.setStatus("current")
_LgpConditionPump1InverterShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPump1InverterShortCycle = _LgpConditionPump1InverterShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 3, 1)
)
if mibBuilder.loadTexts:
    lgpConditionPump1InverterShortCycle.setStatus("current")
_LgpConditionPump2InverterShortCycle_ObjectIdentity = ObjectIdentity
lgpConditionPump2InverterShortCycle = _LgpConditionPump2InverterShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 232, 3, 2)
)
if mibBuilder.loadTexts:
    lgpConditionPump2InverterShortCycle.setStatus("current")
_LgpConditionValveGroup_ObjectIdentity = ObjectIdentity
lgpConditionValveGroup = _LgpConditionValveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 233)
)
if mibBuilder.loadTexts:
    lgpConditionValveGroup.setStatus("current")
_LgpConditionChilledWaterValvePosition_ObjectIdentity = ObjectIdentity
lgpConditionChilledWaterValvePosition = _LgpConditionChilledWaterValvePosition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 233, 1)
)
if mibBuilder.loadTexts:
    lgpConditionChilledWaterValvePosition.setStatus("current")
_LgpConditionCondensationDetected_ObjectIdentity = ObjectIdentity
lgpConditionCondensationDetected = _LgpConditionCondensationDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 234)
)
if mibBuilder.loadTexts:
    lgpConditionCondensationDetected.setStatus("current")
_LgpConditionMaintenanceGroup_ObjectIdentity = ObjectIdentity
lgpConditionMaintenanceGroup = _LgpConditionMaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 235)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenanceGroup.setStatus("current")
_LgpConditionMaintenanceDue_ObjectIdentity = ObjectIdentity
lgpConditionMaintenanceDue = _LgpConditionMaintenanceDue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 235, 1)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenanceDue.setStatus("current")
_LgpConditionMaintenanceComplete_ObjectIdentity = ObjectIdentity
lgpConditionMaintenanceComplete = _LgpConditionMaintenanceComplete_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 235, 2)
)
if mibBuilder.loadTexts:
    lgpConditionMaintenanceComplete.setStatus("current")
_LgpConditionExternalEventSignalGroup_ObjectIdentity = ObjectIdentity
lgpConditionExternalEventSignalGroup = _LgpConditionExternalEventSignalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236)
)
if mibBuilder.loadTexts:
    lgpConditionExternalEventSignalGroup.setStatus("current")
_LgpConditionExternalFireDetect_ObjectIdentity = ObjectIdentity
lgpConditionExternalFireDetect = _LgpConditionExternalFireDetect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 1)
)
if mibBuilder.loadTexts:
    lgpConditionExternalFireDetect.setStatus("current")
_LgpConditionExternalFlowLoss_ObjectIdentity = ObjectIdentity
lgpConditionExternalFlowLoss = _LgpConditionExternalFlowLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 2)
)
if mibBuilder.loadTexts:
    lgpConditionExternalFlowLoss.setStatus("current")
_LgpConditionExternalReheatLockout_ObjectIdentity = ObjectIdentity
lgpConditionExternalReheatLockout = _LgpConditionExternalReheatLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 3)
)
if mibBuilder.loadTexts:
    lgpConditionExternalReheatLockout.setStatus("current")
_LgpConditionExternalOverTemp_ObjectIdentity = ObjectIdentity
lgpConditionExternalOverTemp = _LgpConditionExternalOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 4)
)
if mibBuilder.loadTexts:
    lgpConditionExternalOverTemp.setStatus("current")
_LgpConditionExternalCompLockout_ObjectIdentity = ObjectIdentity
lgpConditionExternalCompLockout = _LgpConditionExternalCompLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 5)
)
if mibBuilder.loadTexts:
    lgpConditionExternalCompLockout.setStatus("current")
_LgpConditionExternalHumidifierLockout_ObjectIdentity = ObjectIdentity
lgpConditionExternalHumidifierLockout = _LgpConditionExternalHumidifierLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 236, 6)
)
if mibBuilder.loadTexts:
    lgpConditionExternalHumidifierLockout.setStatus("current")
_LgpConditionComponentShutdownGroup_ObjectIdentity = ObjectIdentity
lgpConditionComponentShutdownGroup = _LgpConditionComponentShutdownGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 237)
)
if mibBuilder.loadTexts:
    lgpConditionComponentShutdownGroup.setStatus("current")
_LgpConditionComponentShutdownPartial_ObjectIdentity = ObjectIdentity
lgpConditionComponentShutdownPartial = _LgpConditionComponentShutdownPartial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 237, 1)
)
if mibBuilder.loadTexts:
    lgpConditionComponentShutdownPartial.setStatus("current")
_LgpConditionComponentShutdownHighPower_ObjectIdentity = ObjectIdentity
lgpConditionComponentShutdownHighPower = _LgpConditionComponentShutdownHighPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 237, 2)
)
if mibBuilder.loadTexts:
    lgpConditionComponentShutdownHighPower.setStatus("current")
_LgpConditionCondenserProblemGroup_ObjectIdentity = ObjectIdentity
lgpConditionCondenserProblemGroup = _LgpConditionCondenserProblemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 238)
)
if mibBuilder.loadTexts:
    lgpConditionCondenserProblemGroup.setStatus("current")
_LgpConditionCondenser1Problem_ObjectIdentity = ObjectIdentity
lgpConditionCondenser1Problem = _LgpConditionCondenser1Problem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 238, 1)
)
if mibBuilder.loadTexts:
    lgpConditionCondenser1Problem.setStatus("current")
_LgpConditionHumidityOutOfPropBand_ObjectIdentity = ObjectIdentity
lgpConditionHumidityOutOfPropBand = _LgpConditionHumidityOutOfPropBand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 239)
)
if mibBuilder.loadTexts:
    lgpConditionHumidityOutOfPropBand.setStatus("current")
_LgpConditionEnvRemoteSensorGroup_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensorGroup = _LgpConditionEnvRemoteSensorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensorGroup.setStatus("current")
_LgpConditionEnvRemoteSensor1Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor1Issue = _LgpConditionEnvRemoteSensor1Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 1)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor1Issue.setStatus("current")
_LgpConditionEnvRemoteSensor2Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor2Issue = _LgpConditionEnvRemoteSensor2Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 2)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor2Issue.setStatus("current")
_LgpConditionEnvRemoteSensor3Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor3Issue = _LgpConditionEnvRemoteSensor3Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 3)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor3Issue.setStatus("current")
_LgpConditionEnvRemoteSensor4Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor4Issue = _LgpConditionEnvRemoteSensor4Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 4)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor4Issue.setStatus("current")
_LgpConditionEnvRemoteSensor5Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor5Issue = _LgpConditionEnvRemoteSensor5Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 5)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor5Issue.setStatus("current")
_LgpConditionEnvRemoteSensor6Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor6Issue = _LgpConditionEnvRemoteSensor6Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 6)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor6Issue.setStatus("current")
_LgpConditionEnvRemoteSensor7Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor7Issue = _LgpConditionEnvRemoteSensor7Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 7)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor7Issue.setStatus("current")
_LgpConditionEnvRemoteSensor8Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor8Issue = _LgpConditionEnvRemoteSensor8Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 8)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor8Issue.setStatus("current")
_LgpConditionEnvRemoteSensor9Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor9Issue = _LgpConditionEnvRemoteSensor9Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 9)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor9Issue.setStatus("current")
_LgpConditionEnvRemoteSensor10Issue_ObjectIdentity = ObjectIdentity
lgpConditionEnvRemoteSensor10Issue = _LgpConditionEnvRemoteSensor10Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 240, 10)
)
if mibBuilder.loadTexts:
    lgpConditionEnvRemoteSensor10Issue.setStatus("current")
_LgpConditionNeutralSnubberBoardCommFailure_ObjectIdentity = ObjectIdentity
lgpConditionNeutralSnubberBoardCommFailure = _LgpConditionNeutralSnubberBoardCommFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 241)
)
if mibBuilder.loadTexts:
    lgpConditionNeutralSnubberBoardCommFailure.setStatus("current")
_LgpConditionRedundantChargerFailure_ObjectIdentity = ObjectIdentity
lgpConditionRedundantChargerFailure = _LgpConditionRedundantChargerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 242)
)
if mibBuilder.loadTexts:
    lgpConditionRedundantChargerFailure.setStatus("current")
_LgpConditionBoardInputContactorPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionBoardInputContactorPowerFailure = _LgpConditionBoardInputContactorPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 243)
)
if mibBuilder.loadTexts:
    lgpConditionBoardInputContactorPowerFailure.setStatus("current")
_LgpConditionBoard1InputContactorPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionBoard1InputContactorPowerFailure = _LgpConditionBoard1InputContactorPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 243, 1)
)
if mibBuilder.loadTexts:
    lgpConditionBoard1InputContactorPowerFailure.setStatus("current")
_LgpConditionBoard2InputContactorPowerFailure_ObjectIdentity = ObjectIdentity
lgpConditionBoard2InputContactorPowerFailure = _LgpConditionBoard2InputContactorPowerFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 243, 2)
)
if mibBuilder.loadTexts:
    lgpConditionBoard2InputContactorPowerFailure.setStatus("current")
_LgpConditionTooManySensors_ObjectIdentity = ObjectIdentity
lgpConditionTooManySensors = _LgpConditionTooManySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5423)
)
if mibBuilder.loadTexts:
    lgpConditionTooManySensors.setStatus("current")
_LgpConditionDoorSwitchOpen_ObjectIdentity = ObjectIdentity
lgpConditionDoorSwitchOpen = _LgpConditionDoorSwitchOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5471)
)
if mibBuilder.loadTexts:
    lgpConditionDoorSwitchOpen.setStatus("current")
_LgpConditionContactClosureOpen_ObjectIdentity = ObjectIdentity
lgpConditionContactClosureOpen = _LgpConditionContactClosureOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5479)
)
if mibBuilder.loadTexts:
    lgpConditionContactClosureOpen.setStatus("current")
_LgpConditionContactClosureClosed_ObjectIdentity = ObjectIdentity
lgpConditionContactClosureClosed = _LgpConditionContactClosureClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 1, 5480)
)
if mibBuilder.loadTexts:
    lgpConditionContactClosureClosed.setStatus("current")
_LgpConditionsPresent_Type = Gauge32
_LgpConditionsPresent_Object = MibScalar
lgpConditionsPresent = _LgpConditionsPresent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 2),
    _LgpConditionsPresent_Type()
)
lgpConditionsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionsPresent.setStatus("current")
_LgpConditionsTable_Object = MibTable
lgpConditionsTable = _LgpConditionsTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3)
)
if mibBuilder.loadTexts:
    lgpConditionsTable.setStatus("current")
_LgpConditionEntry_Object = MibTableRow
lgpConditionEntry = _LgpConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1)
)
lgpConditionEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpConditionId"),
)
if mibBuilder.loadTexts:
    lgpConditionEntry.setStatus("current")
_LgpConditionId_Type = Unsigned32
_LgpConditionId_Object = MibTableColumn
lgpConditionId = _LgpConditionId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 1),
    _LgpConditionId_Type()
)
lgpConditionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionId.setStatus("current")
_LgpConditionDescr_Type = ObjectIdentifier
_LgpConditionDescr_Object = MibTableColumn
lgpConditionDescr = _LgpConditionDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 2),
    _LgpConditionDescr_Type()
)
lgpConditionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionDescr.setStatus("current")
_LgpConditionTime_Type = TimeTicks
_LgpConditionTime_Object = MibTableColumn
lgpConditionTime = _LgpConditionTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 3),
    _LgpConditionTime_Type()
)
lgpConditionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionTime.setStatus("current")
_LgpConditionTableRef_Type = ObjectIdentifier
_LgpConditionTableRef_Object = MibTableColumn
lgpConditionTableRef = _LgpConditionTableRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 5),
    _LgpConditionTableRef_Type()
)
lgpConditionTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionTableRef.setStatus("current")
_LgpConditionTableRowRef_Type = ObjectIdentifier
_LgpConditionTableRowRef_Object = MibTableColumn
lgpConditionTableRowRef = _LgpConditionTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 6),
    _LgpConditionTableRowRef_Type()
)
lgpConditionTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionTableRowRef.setStatus("current")


class _LgpConditionType_Type(Integer32):
    """Custom type lgpConditionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("message", 2),
          ("warning", 4),
          ("alarm", 6),
          ("fault", 8))
    )


_LgpConditionType_Type.__name__ = "Integer32"
_LgpConditionType_Object = MibTableColumn
lgpConditionType = _LgpConditionType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 10),
    _LgpConditionType_Type()
)
lgpConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionType.setStatus("current")


class _LgpConditionCurrentState_Type(Integer32):
    """Custom type lgpConditionCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_LgpConditionCurrentState_Type.__name__ = "Integer32"
_LgpConditionCurrentState_Object = MibTableColumn
lgpConditionCurrentState = _LgpConditionCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 12),
    _LgpConditionCurrentState_Type()
)
lgpConditionCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionCurrentState.setStatus("current")


class _LgpConditionSeverity_Type(Integer32):
    """Custom type lgpConditionSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 0),
          ("minor", 3),
          ("major", 6),
          ("critical", 9))
    )


_LgpConditionSeverity_Type.__name__ = "Integer32"
_LgpConditionSeverity_Object = MibTableColumn
lgpConditionSeverity = _LgpConditionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 14),
    _LgpConditionSeverity_Type()
)
lgpConditionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionSeverity.setStatus("current")


class _LgpConditionAcknowledged_Type(Integer32):
    """Custom type lgpConditionAcknowledged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notAcknowledged", 1),
          ("acknowledged", 2))
    )


_LgpConditionAcknowledged_Type.__name__ = "Integer32"
_LgpConditionAcknowledged_Object = MibTableColumn
lgpConditionAcknowledged = _LgpConditionAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 18),
    _LgpConditionAcknowledged_Type()
)
lgpConditionAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionAcknowledged.setStatus("current")


class _LgpConditionAckReq_Type(Integer32):
    """Custom type lgpConditionAckReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("required", 1),
          ("notRequired", 2))
    )


_LgpConditionAckReq_Type.__name__ = "Integer32"
_LgpConditionAckReq_Object = MibTableColumn
lgpConditionAckReq = _LgpConditionAckReq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 3, 1, 19),
    _LgpConditionAckReq_Type()
)
lgpConditionAckReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionAckReq.setStatus("current")
_LgpConditionControl_ObjectIdentity = ObjectIdentity
lgpConditionControl = _LgpConditionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4)
)


class _LgpConditionControlEventReset_Type(Integer32):
    """Custom type lgpConditionControlEventReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("resetAll", 2))
    )


_LgpConditionControlEventReset_Type.__name__ = "Integer32"
_LgpConditionControlEventReset_Object = MibScalar
lgpConditionControlEventReset = _LgpConditionControlEventReset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 1),
    _LgpConditionControlEventReset_Type()
)
lgpConditionControlEventReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlEventReset.setStatus("current")


class _LgpConditionControlEventAck_Type(Integer32):
    """Custom type lgpConditionControlEventAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("ackAll", 2))
    )


_LgpConditionControlEventAck_Type.__name__ = "Integer32"
_LgpConditionControlEventAck_Object = MibScalar
lgpConditionControlEventAck = _LgpConditionControlEventAck_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 2),
    _LgpConditionControlEventAck_Type()
)
lgpConditionControlEventAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlEventAck.setStatus("current")
_LgpConditionControlTable_Object = MibTable
lgpConditionControlTable = _LgpConditionControlTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20)
)
if mibBuilder.loadTexts:
    lgpConditionControlTable.setStatus("current")
_LgpConditionControlEntry_Object = MibTableRow
lgpConditionControlEntry = _LgpConditionControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1)
)
lgpConditionControlEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpConditionControlIndex"),
)
if mibBuilder.loadTexts:
    lgpConditionControlEntry.setStatus("current")
_LgpConditionControlIndex_Type = Unsigned32
_LgpConditionControlIndex_Object = MibTableColumn
lgpConditionControlIndex = _LgpConditionControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 1),
    _LgpConditionControlIndex_Type()
)
lgpConditionControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpConditionControlIndex.setStatus("current")
_LgpConditionControlDescr_Type = ObjectIdentifier
_LgpConditionControlDescr_Object = MibTableColumn
lgpConditionControlDescr = _LgpConditionControlDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 2),
    _LgpConditionControlDescr_Type()
)
lgpConditionControlDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionControlDescr.setStatus("current")


class _LgpConditionControlEnableStatus_Type(Integer32):
    """Custom type lgpConditionControlEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("enabled", 1),
          ("disabled", 2))
    )


_LgpConditionControlEnableStatus_Type.__name__ = "Integer32"
_LgpConditionControlEnableStatus_Object = MibTableColumn
lgpConditionControlEnableStatus = _LgpConditionControlEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 3),
    _LgpConditionControlEnableStatus_Type()
)
lgpConditionControlEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlEnableStatus.setStatus("current")


class _LgpConditionControlType_Type(Integer32):
    """Custom type lgpConditionControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("message", 2),
          ("warning", 4),
          ("alarm", 6),
          ("fault", 8))
    )


_LgpConditionControlType_Type.__name__ = "Integer32"
_LgpConditionControlType_Object = MibTableColumn
lgpConditionControlType = _LgpConditionControlType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 4),
    _LgpConditionControlType_Type()
)
lgpConditionControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpConditionControlType.setStatus("current")


class _LgpConditionControlEnableCapability_Type(Integer32):
    """Custom type lgpConditionControlEnableCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("read-only", 1),
          ("read-write", 2))
    )


_LgpConditionControlEnableCapability_Type.__name__ = "Integer32"
_LgpConditionControlEnableCapability_Object = MibTableColumn
lgpConditionControlEnableCapability = _LgpConditionControlEnableCapability_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 4, 20, 1, 5),
    _LgpConditionControlEnableCapability_Type()
)
lgpConditionControlEnableCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionControlEnableCapability.setStatus("current")


class _LgpConditionDescription_Type(DisplayString):
    """Custom type lgpConditionDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpConditionDescription_Type.__name__ = "DisplayString"
_LgpConditionDescription_Object = MibScalar
lgpConditionDescription = _LgpConditionDescription_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 5),
    _LgpConditionDescription_Type()
)
lgpConditionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpConditionDescription.setStatus("current")


class _LgpNetworkName_Type(DisplayString):
    """Custom type lgpNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpNetworkName_Type.__name__ = "DisplayString"
_LgpNetworkName_Object = MibScalar
lgpNetworkName = _LgpNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 6),
    _LgpNetworkName_Type()
)
lgpNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpNetworkName.setStatus("current")
_LgpFlexConditions_ObjectIdentity = ObjectIdentity
lgpFlexConditions = _LgpFlexConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7)
)
_LgpFlexConditionsWellKnown_ObjectIdentity = ObjectIdentity
lgpFlexConditionsWellKnown = _LgpFlexConditionsWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1)
)
_LgpCondId4122SystemInputPowerProblem_ObjectIdentity = ObjectIdentity
lgpCondId4122SystemInputPowerProblem = _LgpCondId4122SystemInputPowerProblem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4122)
)
if mibBuilder.loadTexts:
    lgpCondId4122SystemInputPowerProblem.setStatus("current")
_LgpCondId4132BypassOverloadPhaseA_ObjectIdentity = ObjectIdentity
lgpCondId4132BypassOverloadPhaseA = _LgpCondId4132BypassOverloadPhaseA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4132)
)
if mibBuilder.loadTexts:
    lgpCondId4132BypassOverloadPhaseA.setStatus("current")
_LgpCondId4133BypassOverloadPhaseB_ObjectIdentity = ObjectIdentity
lgpCondId4133BypassOverloadPhaseB = _LgpCondId4133BypassOverloadPhaseB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4133)
)
if mibBuilder.loadTexts:
    lgpCondId4133BypassOverloadPhaseB.setStatus("current")
_LgpCondId4134BypassOverloadPhaseC_ObjectIdentity = ObjectIdentity
lgpCondId4134BypassOverloadPhaseC = _LgpCondId4134BypassOverloadPhaseC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4134)
)
if mibBuilder.loadTexts:
    lgpCondId4134BypassOverloadPhaseC.setStatus("current")
_LgpCondId4135BypassNotAvailable_ObjectIdentity = ObjectIdentity
lgpCondId4135BypassNotAvailable = _LgpCondId4135BypassNotAvailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4135)
)
if mibBuilder.loadTexts:
    lgpCondId4135BypassNotAvailable.setStatus("current")
_LgpCondId4137BypassAutoRetransferPrimed_ObjectIdentity = ObjectIdentity
lgpCondId4137BypassAutoRetransferPrimed = _LgpCondId4137BypassAutoRetransferPrimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4137)
)
if mibBuilder.loadTexts:
    lgpCondId4137BypassAutoRetransferPrimed.setStatus("current")
_LgpCondId4138BypassAutoRetransferFailed_ObjectIdentity = ObjectIdentity
lgpCondId4138BypassAutoRetransferFailed = _LgpCondId4138BypassAutoRetransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4138)
)
if mibBuilder.loadTexts:
    lgpCondId4138BypassAutoRetransferFailed.setStatus("current")
_LgpCondId4139BypassExcessAutoRetransfers_ObjectIdentity = ObjectIdentity
lgpCondId4139BypassExcessAutoRetransfers = _LgpCondId4139BypassExcessAutoRetransfers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4139)
)
if mibBuilder.loadTexts:
    lgpCondId4139BypassExcessAutoRetransfers.setStatus("current")
_LgpCondId4140BypassRestartInhibitExternal_ObjectIdentity = ObjectIdentity
lgpCondId4140BypassRestartInhibitExternal = _LgpCondId4140BypassRestartInhibitExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4140)
)
if mibBuilder.loadTexts:
    lgpCondId4140BypassRestartInhibitExternal.setStatus("current")
_LgpCondId4141BypassBreakerClosed_ObjectIdentity = ObjectIdentity
lgpCondId4141BypassBreakerClosed = _LgpCondId4141BypassBreakerClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4141)
)
if mibBuilder.loadTexts:
    lgpCondId4141BypassBreakerClosed.setStatus("current")
_LgpCondId4142BypassStaticSwitchOverload_ObjectIdentity = ObjectIdentity
lgpCondId4142BypassStaticSwitchOverload = _LgpCondId4142BypassStaticSwitchOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4142)
)
if mibBuilder.loadTexts:
    lgpCondId4142BypassStaticSwitchOverload.setStatus("current")
_LgpCondId4143BypassStaticSwitchUnavailable_ObjectIdentity = ObjectIdentity
lgpCondId4143BypassStaticSwitchUnavailable = _LgpCondId4143BypassStaticSwitchUnavailable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4143)
)
if mibBuilder.loadTexts:
    lgpCondId4143BypassStaticSwitchUnavailable.setStatus("current")
_LgpCondId4144BypassExcessivePulseParallel_ObjectIdentity = ObjectIdentity
lgpCondId4144BypassExcessivePulseParallel = _LgpCondId4144BypassExcessivePulseParallel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4144)
)
if mibBuilder.loadTexts:
    lgpCondId4144BypassExcessivePulseParallel.setStatus("current")
_LgpCondId4145BypassAutoTransferFailed_ObjectIdentity = ObjectIdentity
lgpCondId4145BypassAutoTransferFailed = _LgpCondId4145BypassAutoTransferFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4145)
)
if mibBuilder.loadTexts:
    lgpCondId4145BypassAutoTransferFailed.setStatus("current")
_LgpCondId4146SystemInputPhsRotationError_ObjectIdentity = ObjectIdentity
lgpCondId4146SystemInputPhsRotationError = _LgpCondId4146SystemInputPhsRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4146)
)
if mibBuilder.loadTexts:
    lgpCondId4146SystemInputPhsRotationError.setStatus("current")
_LgpCondId4147SystemInputCurrentLimit_ObjectIdentity = ObjectIdentity
lgpCondId4147SystemInputCurrentLimit = _LgpCondId4147SystemInputCurrentLimit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4147)
)
if mibBuilder.loadTexts:
    lgpCondId4147SystemInputCurrentLimit.setStatus("current")
_LgpCondId4162BatteryLow_ObjectIdentity = ObjectIdentity
lgpCondId4162BatteryLow = _LgpCondId4162BatteryLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4162)
)
if mibBuilder.loadTexts:
    lgpCondId4162BatteryLow.setStatus("current")
_LgpCondId4163OutputOffEndofDischarge_ObjectIdentity = ObjectIdentity
lgpCondId4163OutputOffEndofDischarge = _LgpCondId4163OutputOffEndofDischarge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4163)
)
if mibBuilder.loadTexts:
    lgpCondId4163OutputOffEndofDischarge.setStatus("current")
_LgpCondId4164BatteryChargingError_ObjectIdentity = ObjectIdentity
lgpCondId4164BatteryChargingError = _LgpCondId4164BatteryChargingError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4164)
)
if mibBuilder.loadTexts:
    lgpCondId4164BatteryChargingError.setStatus("current")
_LgpCondId4165BatteryChargingReducedExtrnl_ObjectIdentity = ObjectIdentity
lgpCondId4165BatteryChargingReducedExtrnl = _LgpCondId4165BatteryChargingReducedExtrnl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4165)
)
if mibBuilder.loadTexts:
    lgpCondId4165BatteryChargingReducedExtrnl.setStatus("current")
_LgpCondId4166BatteryCapacityLow_ObjectIdentity = ObjectIdentity
lgpCondId4166BatteryCapacityLow = _LgpCondId4166BatteryCapacityLow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4166)
)
if mibBuilder.loadTexts:
    lgpCondId4166BatteryCapacityLow.setStatus("current")
_LgpCondId4167OutputOff_ObjectIdentity = ObjectIdentity
lgpCondId4167OutputOff = _LgpCondId4167OutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4167)
)
if mibBuilder.loadTexts:
    lgpCondId4167OutputOff.setStatus("current")
_LgpCondId4168BatteryDischarging_ObjectIdentity = ObjectIdentity
lgpCondId4168BatteryDischarging = _LgpCondId4168BatteryDischarging_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4168)
)
if mibBuilder.loadTexts:
    lgpCondId4168BatteryDischarging.setStatus("current")
_LgpCondId4169BatteryTemperatureImbalance_ObjectIdentity = ObjectIdentity
lgpCondId4169BatteryTemperatureImbalance = _LgpCondId4169BatteryTemperatureImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4169)
)
if mibBuilder.loadTexts:
    lgpCondId4169BatteryTemperatureImbalance.setStatus("current")
_LgpCondId4170BatteryEqualize_ObjectIdentity = ObjectIdentity
lgpCondId4170BatteryEqualize = _LgpCondId4170BatteryEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4170)
)
if mibBuilder.loadTexts:
    lgpCondId4170BatteryEqualize.setStatus("current")
_LgpCondId4171BatteryManualTestInProgress_ObjectIdentity = ObjectIdentity
lgpCondId4171BatteryManualTestInProgress = _LgpCondId4171BatteryManualTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4171)
)
if mibBuilder.loadTexts:
    lgpCondId4171BatteryManualTestInProgress.setStatus("current")
_LgpCondId4172BatteryAutoTestInProgress_ObjectIdentity = ObjectIdentity
lgpCondId4172BatteryAutoTestInProgress = _LgpCondId4172BatteryAutoTestInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4172)
)
if mibBuilder.loadTexts:
    lgpCondId4172BatteryAutoTestInProgress.setStatus("current")
_LgpCondId4173MainBatteryDisconnectOpen_ObjectIdentity = ObjectIdentity
lgpCondId4173MainBatteryDisconnectOpen = _LgpCondId4173MainBatteryDisconnectOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4173)
)
if mibBuilder.loadTexts:
    lgpCondId4173MainBatteryDisconnectOpen.setStatus("current")
_LgpCondId4174BatteryTemperatureSensorFault_ObjectIdentity = ObjectIdentity
lgpCondId4174BatteryTemperatureSensorFault = _LgpCondId4174BatteryTemperatureSensorFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4174)
)
if mibBuilder.loadTexts:
    lgpCondId4174BatteryTemperatureSensorFault.setStatus("current")
_LgpCondId4175BypassFrequencyError_ObjectIdentity = ObjectIdentity
lgpCondId4175BypassFrequencyError = _LgpCondId4175BypassFrequencyError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4175)
)
if mibBuilder.loadTexts:
    lgpCondId4175BypassFrequencyError.setStatus("current")
_LgpCondId4176BatteryCircuitBreaker1Open_ObjectIdentity = ObjectIdentity
lgpCondId4176BatteryCircuitBreaker1Open = _LgpCondId4176BatteryCircuitBreaker1Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4176)
)
if mibBuilder.loadTexts:
    lgpCondId4176BatteryCircuitBreaker1Open.setStatus("current")
_LgpCondId4177BatteryBreaker1OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4177BatteryBreaker1OpenFailure = _LgpCondId4177BatteryBreaker1OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4177)
)
if mibBuilder.loadTexts:
    lgpCondId4177BatteryBreaker1OpenFailure.setStatus("current")
_LgpCondId4178BatteryBreaker1CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4178BatteryBreaker1CloseFailure = _LgpCondId4178BatteryBreaker1CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4178)
)
if mibBuilder.loadTexts:
    lgpCondId4178BatteryBreaker1CloseFailure.setStatus("current")
_LgpCondId4179BatteryCircuitBreaker2Open_ObjectIdentity = ObjectIdentity
lgpCondId4179BatteryCircuitBreaker2Open = _LgpCondId4179BatteryCircuitBreaker2Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4179)
)
if mibBuilder.loadTexts:
    lgpCondId4179BatteryCircuitBreaker2Open.setStatus("current")
_LgpCondId4180BatteryBreaker2OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4180BatteryBreaker2OpenFailure = _LgpCondId4180BatteryBreaker2OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4180)
)
if mibBuilder.loadTexts:
    lgpCondId4180BatteryBreaker2OpenFailure.setStatus("current")
_LgpCondId4181BatteryBreaker2CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4181BatteryBreaker2CloseFailure = _LgpCondId4181BatteryBreaker2CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4181)
)
if mibBuilder.loadTexts:
    lgpCondId4181BatteryBreaker2CloseFailure.setStatus("current")
_LgpCondId4182BatteryCircuitBreaker3Open_ObjectIdentity = ObjectIdentity
lgpCondId4182BatteryCircuitBreaker3Open = _LgpCondId4182BatteryCircuitBreaker3Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4182)
)
if mibBuilder.loadTexts:
    lgpCondId4182BatteryCircuitBreaker3Open.setStatus("current")
_LgpCondId4183BatteryBreaker3OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4183BatteryBreaker3OpenFailure = _LgpCondId4183BatteryBreaker3OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4183)
)
if mibBuilder.loadTexts:
    lgpCondId4183BatteryBreaker3OpenFailure.setStatus("current")
_LgpCondId4184BatteryBreaker3CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4184BatteryBreaker3CloseFailure = _LgpCondId4184BatteryBreaker3CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4184)
)
if mibBuilder.loadTexts:
    lgpCondId4184BatteryBreaker3CloseFailure.setStatus("current")
_LgpCondId4185BatteryCircuitBreaker4Open_ObjectIdentity = ObjectIdentity
lgpCondId4185BatteryCircuitBreaker4Open = _LgpCondId4185BatteryCircuitBreaker4Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4185)
)
if mibBuilder.loadTexts:
    lgpCondId4185BatteryCircuitBreaker4Open.setStatus("current")
_LgpCondId4186BatteryBreaker4OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4186BatteryBreaker4OpenFailure = _LgpCondId4186BatteryBreaker4OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4186)
)
if mibBuilder.loadTexts:
    lgpCondId4186BatteryBreaker4OpenFailure.setStatus("current")
_LgpCondId4187BatteryBreaker4CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4187BatteryBreaker4CloseFailure = _LgpCondId4187BatteryBreaker4CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4187)
)
if mibBuilder.loadTexts:
    lgpCondId4187BatteryBreaker4CloseFailure.setStatus("current")
_LgpCondId4188BatteryCircuitBreaker5Open_ObjectIdentity = ObjectIdentity
lgpCondId4188BatteryCircuitBreaker5Open = _LgpCondId4188BatteryCircuitBreaker5Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4188)
)
if mibBuilder.loadTexts:
    lgpCondId4188BatteryCircuitBreaker5Open.setStatus("current")
_LgpCondId4189BatteryBreaker5OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4189BatteryBreaker5OpenFailure = _LgpCondId4189BatteryBreaker5OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4189)
)
if mibBuilder.loadTexts:
    lgpCondId4189BatteryBreaker5OpenFailure.setStatus("current")
_LgpCondId4190BatteryBreaker5CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4190BatteryBreaker5CloseFailure = _LgpCondId4190BatteryBreaker5CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4190)
)
if mibBuilder.loadTexts:
    lgpCondId4190BatteryBreaker5CloseFailure.setStatus("current")
_LgpCondId4191BatteryCircuitBreaker6Open_ObjectIdentity = ObjectIdentity
lgpCondId4191BatteryCircuitBreaker6Open = _LgpCondId4191BatteryCircuitBreaker6Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4191)
)
if mibBuilder.loadTexts:
    lgpCondId4191BatteryCircuitBreaker6Open.setStatus("current")
_LgpCondId4192BatteryBreaker6OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4192BatteryBreaker6OpenFailure = _LgpCondId4192BatteryBreaker6OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4192)
)
if mibBuilder.loadTexts:
    lgpCondId4192BatteryBreaker6OpenFailure.setStatus("current")
_LgpCondId4193BatteryBreaker6CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4193BatteryBreaker6CloseFailure = _LgpCondId4193BatteryBreaker6CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4193)
)
if mibBuilder.loadTexts:
    lgpCondId4193BatteryBreaker6CloseFailure.setStatus("current")
_LgpCondId4194BatteryCircuitBreaker7Open_ObjectIdentity = ObjectIdentity
lgpCondId4194BatteryCircuitBreaker7Open = _LgpCondId4194BatteryCircuitBreaker7Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4194)
)
if mibBuilder.loadTexts:
    lgpCondId4194BatteryCircuitBreaker7Open.setStatus("current")
_LgpCondId4195BatteryBreaker7OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4195BatteryBreaker7OpenFailure = _LgpCondId4195BatteryBreaker7OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4195)
)
if mibBuilder.loadTexts:
    lgpCondId4195BatteryBreaker7OpenFailure.setStatus("current")
_LgpCondId4196BatteryBreaker7CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4196BatteryBreaker7CloseFailure = _LgpCondId4196BatteryBreaker7CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4196)
)
if mibBuilder.loadTexts:
    lgpCondId4196BatteryBreaker7CloseFailure.setStatus("current")
_LgpCondId4197BatteryCircuitBreaker8Open_ObjectIdentity = ObjectIdentity
lgpCondId4197BatteryCircuitBreaker8Open = _LgpCondId4197BatteryCircuitBreaker8Open_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4197)
)
if mibBuilder.loadTexts:
    lgpCondId4197BatteryCircuitBreaker8Open.setStatus("current")
_LgpCondId4198BatteryBreaker8OpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4198BatteryBreaker8OpenFailure = _LgpCondId4198BatteryBreaker8OpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4198)
)
if mibBuilder.loadTexts:
    lgpCondId4198BatteryBreaker8OpenFailure.setStatus("current")
_LgpCondId4199BatteryBreaker8CloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4199BatteryBreaker8CloseFailure = _LgpCondId4199BatteryBreaker8CloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4199)
)
if mibBuilder.loadTexts:
    lgpCondId4199BatteryBreaker8CloseFailure.setStatus("current")
_LgpCondId4200BatteryChargingInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4200BatteryChargingInhibited = _LgpCondId4200BatteryChargingInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4200)
)
if mibBuilder.loadTexts:
    lgpCondId4200BatteryChargingInhibited.setStatus("current")
_LgpCondId4213SystemShutdownEPO_ObjectIdentity = ObjectIdentity
lgpCondId4213SystemShutdownEPO = _LgpCondId4213SystemShutdownEPO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4213)
)
if mibBuilder.loadTexts:
    lgpCondId4213SystemShutdownEPO.setStatus("current")
_LgpCondId4214SystemShutdownREPO_ObjectIdentity = ObjectIdentity
lgpCondId4214SystemShutdownREPO = _LgpCondId4214SystemShutdownREPO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4214)
)
if mibBuilder.loadTexts:
    lgpCondId4214SystemShutdownREPO.setStatus("current")
_LgpCondId4215SystemOutputOff_ObjectIdentity = ObjectIdentity
lgpCondId4215SystemOutputOff = _LgpCondId4215SystemOutputOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4215)
)
if mibBuilder.loadTexts:
    lgpCondId4215SystemOutputOff.setStatus("current")
_LgpCondId4216BypassBackfeedDetected_ObjectIdentity = ObjectIdentity
lgpCondId4216BypassBackfeedDetected = _LgpCondId4216BypassBackfeedDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4216)
)
if mibBuilder.loadTexts:
    lgpCondId4216BypassBackfeedDetected.setStatus("current")
_LgpCondId4217BypassManualXfrInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4217BypassManualXfrInhibited = _LgpCondId4217BypassManualXfrInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4217)
)
if mibBuilder.loadTexts:
    lgpCondId4217BypassManualXfrInhibited.setStatus("current")
_LgpCondId4218BypassManualRexfrInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4218BypassManualRexfrInhibited = _LgpCondId4218BypassManualRexfrInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4218)
)
if mibBuilder.loadTexts:
    lgpCondId4218BypassManualRexfrInhibited.setStatus("current")
_LgpCondId4219BatteryOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4219BatteryOverTemperature = _LgpCondId4219BatteryOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4219)
)
if mibBuilder.loadTexts:
    lgpCondId4219BatteryOverTemperature.setStatus("current")
_LgpCondId4220BatteryExternalMonitor1_ObjectIdentity = ObjectIdentity
lgpCondId4220BatteryExternalMonitor1 = _LgpCondId4220BatteryExternalMonitor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4220)
)
if mibBuilder.loadTexts:
    lgpCondId4220BatteryExternalMonitor1.setStatus("current")
_LgpCondId4221BatteryExternalMonitor2_ObjectIdentity = ObjectIdentity
lgpCondId4221BatteryExternalMonitor2 = _LgpCondId4221BatteryExternalMonitor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4221)
)
if mibBuilder.loadTexts:
    lgpCondId4221BatteryExternalMonitor2.setStatus("current")
_LgpCondId4222BatteryGroundFault_ObjectIdentity = ObjectIdentity
lgpCondId4222BatteryGroundFault = _LgpCondId4222BatteryGroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4222)
)
if mibBuilder.loadTexts:
    lgpCondId4222BatteryGroundFault.setStatus("current")
_LgpCondId4229EmergencyPowerOffLatched_ObjectIdentity = ObjectIdentity
lgpCondId4229EmergencyPowerOffLatched = _LgpCondId4229EmergencyPowerOffLatched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4229)
)
if mibBuilder.loadTexts:
    lgpCondId4229EmergencyPowerOffLatched.setStatus("current")
_LgpCondId4230SystemOutputLowPowerFactor_ObjectIdentity = ObjectIdentity
lgpCondId4230SystemOutputLowPowerFactor = _LgpCondId4230SystemOutputLowPowerFactor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4230)
)
if mibBuilder.loadTexts:
    lgpCondId4230SystemOutputLowPowerFactor.setStatus("current")
_LgpCondId4231OutputCurrentExceedsThreshold_ObjectIdentity = ObjectIdentity
lgpCondId4231OutputCurrentExceedsThreshold = _LgpCondId4231OutputCurrentExceedsThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4231)
)
if mibBuilder.loadTexts:
    lgpCondId4231OutputCurrentExceedsThreshold.setStatus("current")
_LgpCondId4233InverterFailure_ObjectIdentity = ObjectIdentity
lgpCondId4233InverterFailure = _LgpCondId4233InverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4233)
)
if mibBuilder.loadTexts:
    lgpCondId4233InverterFailure.setStatus("current")
_LgpCondId4234InverterOverloadPhaseA_ObjectIdentity = ObjectIdentity
lgpCondId4234InverterOverloadPhaseA = _LgpCondId4234InverterOverloadPhaseA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4234)
)
if mibBuilder.loadTexts:
    lgpCondId4234InverterOverloadPhaseA.setStatus("current")
_LgpCondId4235InverterOverloadPhaseB_ObjectIdentity = ObjectIdentity
lgpCondId4235InverterOverloadPhaseB = _LgpCondId4235InverterOverloadPhaseB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4235)
)
if mibBuilder.loadTexts:
    lgpCondId4235InverterOverloadPhaseB.setStatus("current")
_LgpCondId4236InverterOverloadPhaseC_ObjectIdentity = ObjectIdentity
lgpCondId4236InverterOverloadPhaseC = _LgpCondId4236InverterOverloadPhaseC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4236)
)
if mibBuilder.loadTexts:
    lgpCondId4236InverterOverloadPhaseC.setStatus("current")
_LgpCondId4237InverterInhibitExternal_ObjectIdentity = ObjectIdentity
lgpCondId4237InverterInhibitExternal = _LgpCondId4237InverterInhibitExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4237)
)
if mibBuilder.loadTexts:
    lgpCondId4237InverterInhibitExternal.setStatus("current")
_LgpCondId4238InverterOutBreakerOpenFail_ObjectIdentity = ObjectIdentity
lgpCondId4238InverterOutBreakerOpenFail = _LgpCondId4238InverterOutBreakerOpenFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4238)
)
if mibBuilder.loadTexts:
    lgpCondId4238InverterOutBreakerOpenFail.setStatus("current")
_LgpCondId4239InverterOutBreakerCloseFail_ObjectIdentity = ObjectIdentity
lgpCondId4239InverterOutBreakerCloseFail = _LgpCondId4239InverterOutBreakerCloseFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4239)
)
if mibBuilder.loadTexts:
    lgpCondId4239InverterOutBreakerCloseFail.setStatus("current")
_LgpCondId4270InputContact01_ObjectIdentity = ObjectIdentity
lgpCondId4270InputContact01 = _LgpCondId4270InputContact01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4270)
)
if mibBuilder.loadTexts:
    lgpCondId4270InputContact01.setStatus("current")
_LgpCondId4271InputContact02_ObjectIdentity = ObjectIdentity
lgpCondId4271InputContact02 = _LgpCondId4271InputContact02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4271)
)
if mibBuilder.loadTexts:
    lgpCondId4271InputContact02.setStatus("current")
_LgpCondId4272InputContact03_ObjectIdentity = ObjectIdentity
lgpCondId4272InputContact03 = _LgpCondId4272InputContact03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4272)
)
if mibBuilder.loadTexts:
    lgpCondId4272InputContact03.setStatus("current")
_LgpCondId4273InputContact04_ObjectIdentity = ObjectIdentity
lgpCondId4273InputContact04 = _LgpCondId4273InputContact04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4273)
)
if mibBuilder.loadTexts:
    lgpCondId4273InputContact04.setStatus("current")
_LgpCondId4274InputContact05_ObjectIdentity = ObjectIdentity
lgpCondId4274InputContact05 = _LgpCondId4274InputContact05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4274)
)
if mibBuilder.loadTexts:
    lgpCondId4274InputContact05.setStatus("current")
_LgpCondId4275InputContact06_ObjectIdentity = ObjectIdentity
lgpCondId4275InputContact06 = _LgpCondId4275InputContact06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4275)
)
if mibBuilder.loadTexts:
    lgpCondId4275InputContact06.setStatus("current")
_LgpCondId4276InputContact07_ObjectIdentity = ObjectIdentity
lgpCondId4276InputContact07 = _LgpCondId4276InputContact07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4276)
)
if mibBuilder.loadTexts:
    lgpCondId4276InputContact07.setStatus("current")
_LgpCondId4277InputContact08_ObjectIdentity = ObjectIdentity
lgpCondId4277InputContact08 = _LgpCondId4277InputContact08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4277)
)
if mibBuilder.loadTexts:
    lgpCondId4277InputContact08.setStatus("current")
_LgpCondId4278InputContact09_ObjectIdentity = ObjectIdentity
lgpCondId4278InputContact09 = _LgpCondId4278InputContact09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4278)
)
if mibBuilder.loadTexts:
    lgpCondId4278InputContact09.setStatus("current")
_LgpCondId4279InputContact10_ObjectIdentity = ObjectIdentity
lgpCondId4279InputContact10 = _LgpCondId4279InputContact10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4279)
)
if mibBuilder.loadTexts:
    lgpCondId4279InputContact10.setStatus("current")
_LgpCondId4280InputContact11_ObjectIdentity = ObjectIdentity
lgpCondId4280InputContact11 = _LgpCondId4280InputContact11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4280)
)
if mibBuilder.loadTexts:
    lgpCondId4280InputContact11.setStatus("current")
_LgpCondId4281InputContact12_ObjectIdentity = ObjectIdentity
lgpCondId4281InputContact12 = _LgpCondId4281InputContact12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4281)
)
if mibBuilder.loadTexts:
    lgpCondId4281InputContact12.setStatus("current")
_LgpCondId4282InputContact13_ObjectIdentity = ObjectIdentity
lgpCondId4282InputContact13 = _LgpCondId4282InputContact13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4282)
)
if mibBuilder.loadTexts:
    lgpCondId4282InputContact13.setStatus("current")
_LgpCondId4283InputContact14_ObjectIdentity = ObjectIdentity
lgpCondId4283InputContact14 = _LgpCondId4283InputContact14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4283)
)
if mibBuilder.loadTexts:
    lgpCondId4283InputContact14.setStatus("current")
_LgpCondId4284InputContact15_ObjectIdentity = ObjectIdentity
lgpCondId4284InputContact15 = _LgpCondId4284InputContact15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4284)
)
if mibBuilder.loadTexts:
    lgpCondId4284InputContact15.setStatus("current")
_LgpCondId4285InputContact16_ObjectIdentity = ObjectIdentity
lgpCondId4285InputContact16 = _LgpCondId4285InputContact16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4285)
)
if mibBuilder.loadTexts:
    lgpCondId4285InputContact16.setStatus("current")
_LgpCondId4286OutputAmpOverUserLimitPhsA_ObjectIdentity = ObjectIdentity
lgpCondId4286OutputAmpOverUserLimitPhsA = _LgpCondId4286OutputAmpOverUserLimitPhsA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4286)
)
if mibBuilder.loadTexts:
    lgpCondId4286OutputAmpOverUserLimitPhsA.setStatus("current")
_LgpCondId4287OutputAmpOverUserLimitPhsB_ObjectIdentity = ObjectIdentity
lgpCondId4287OutputAmpOverUserLimitPhsB = _LgpCondId4287OutputAmpOverUserLimitPhsB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4287)
)
if mibBuilder.loadTexts:
    lgpCondId4287OutputAmpOverUserLimitPhsB.setStatus("current")
_LgpCondId4288OutputAmpOverUserLimitPhsC_ObjectIdentity = ObjectIdentity
lgpCondId4288OutputAmpOverUserLimitPhsC = _LgpCondId4288OutputAmpOverUserLimitPhsC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4288)
)
if mibBuilder.loadTexts:
    lgpCondId4288OutputAmpOverUserLimitPhsC.setStatus("current")
_LgpCondId4289InverterTransferInhibitExt_ObjectIdentity = ObjectIdentity
lgpCondId4289InverterTransferInhibitExt = _LgpCondId4289InverterTransferInhibitExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4289)
)
if mibBuilder.loadTexts:
    lgpCondId4289InverterTransferInhibitExt.setStatus("current")
_LgpCondId4290InverterShutdownOverload_ObjectIdentity = ObjectIdentity
lgpCondId4290InverterShutdownOverload = _LgpCondId4290InverterShutdownOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4290)
)
if mibBuilder.loadTexts:
    lgpCondId4290InverterShutdownOverload.setStatus("current")
_LgpCondId4294InletAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4294InletAirOverTemperature = _LgpCondId4294InletAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4294)
)
if mibBuilder.loadTexts:
    lgpCondId4294InletAirOverTemperature.setStatus("current")
_LgpCondId4295RectifierFailure_ObjectIdentity = ObjectIdentity
lgpCondId4295RectifierFailure = _LgpCondId4295RectifierFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4295)
)
if mibBuilder.loadTexts:
    lgpCondId4295RectifierFailure.setStatus("current")
_LgpCondId4296RectifierOperationInhibitExt_ObjectIdentity = ObjectIdentity
lgpCondId4296RectifierOperationInhibitExt = _LgpCondId4296RectifierOperationInhibitExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4296)
)
if mibBuilder.loadTexts:
    lgpCondId4296RectifierOperationInhibitExt.setStatus("current")
_LgpCondId4297UPSOutputonInverter_ObjectIdentity = ObjectIdentity
lgpCondId4297UPSOutputonInverter = _LgpCondId4297UPSOutputonInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4297)
)
if mibBuilder.loadTexts:
    lgpCondId4297UPSOutputonInverter.setStatus("current")
_LgpCondId4298UPSOutputonBypass_ObjectIdentity = ObjectIdentity
lgpCondId4298UPSOutputonBypass = _LgpCondId4298UPSOutputonBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4298)
)
if mibBuilder.loadTexts:
    lgpCondId4298UPSOutputonBypass.setStatus("current")
_LgpCondId4299OutputLoadonMaintBypass_ObjectIdentity = ObjectIdentity
lgpCondId4299OutputLoadonMaintBypass = _LgpCondId4299OutputLoadonMaintBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4299)
)
if mibBuilder.loadTexts:
    lgpCondId4299OutputLoadonMaintBypass.setStatus("current")
_LgpCondId4300InternalCommunicationsFailure_ObjectIdentity = ObjectIdentity
lgpCondId4300InternalCommunicationsFailure = _LgpCondId4300InternalCommunicationsFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4300)
)
if mibBuilder.loadTexts:
    lgpCondId4300InternalCommunicationsFailure.setStatus("current")
_LgpCondId4308DCBusGroundFaultPositive_ObjectIdentity = ObjectIdentity
lgpCondId4308DCBusGroundFaultPositive = _LgpCondId4308DCBusGroundFaultPositive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4308)
)
if mibBuilder.loadTexts:
    lgpCondId4308DCBusGroundFaultPositive.setStatus("current")
_LgpCondId4309DCBusGroundFaultNegative_ObjectIdentity = ObjectIdentity
lgpCondId4309DCBusGroundFaultNegative = _LgpCondId4309DCBusGroundFaultNegative_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4309)
)
if mibBuilder.loadTexts:
    lgpCondId4309DCBusGroundFaultNegative.setStatus("current")
_LgpCondId4310EquipmentOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4310EquipmentOverTemperature = _LgpCondId4310EquipmentOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4310)
)
if mibBuilder.loadTexts:
    lgpCondId4310EquipmentOverTemperature.setStatus("current")
_LgpCondId4311SystemFanFailure_ObjectIdentity = ObjectIdentity
lgpCondId4311SystemFanFailure = _LgpCondId4311SystemFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4311)
)
if mibBuilder.loadTexts:
    lgpCondId4311SystemFanFailure.setStatus("current")
_LgpCondId4313PasswordChanged_ObjectIdentity = ObjectIdentity
lgpCondId4313PasswordChanged = _LgpCondId4313PasswordChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4313)
)
if mibBuilder.loadTexts:
    lgpCondId4313PasswordChanged.setStatus("current")
_LgpCondId4314PowerSupplyFailure_ObjectIdentity = ObjectIdentity
lgpCondId4314PowerSupplyFailure = _LgpCondId4314PowerSupplyFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4314)
)
if mibBuilder.loadTexts:
    lgpCondId4314PowerSupplyFailure.setStatus("current")
_LgpCondId4315OnGenerator_ObjectIdentity = ObjectIdentity
lgpCondId4315OnGenerator = _LgpCondId4315OnGenerator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4315)
)
if mibBuilder.loadTexts:
    lgpCondId4315OnGenerator.setStatus("current")
_LgpCondId4316AutoRestartInProgress_ObjectIdentity = ObjectIdentity
lgpCondId4316AutoRestartInProgress = _LgpCondId4316AutoRestartInProgress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4316)
)
if mibBuilder.loadTexts:
    lgpCondId4316AutoRestartInProgress.setStatus("current")
_LgpCondId4317AutoRestartInhibitedExt_ObjectIdentity = ObjectIdentity
lgpCondId4317AutoRestartInhibitedExt = _LgpCondId4317AutoRestartInhibitedExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4317)
)
if mibBuilder.loadTexts:
    lgpCondId4317AutoRestartInhibitedExt.setStatus("current")
_LgpCondId4320InitiatedTransfertoBypass_ObjectIdentity = ObjectIdentity
lgpCondId4320InitiatedTransfertoBypass = _LgpCondId4320InitiatedTransfertoBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4320)
)
if mibBuilder.loadTexts:
    lgpCondId4320InitiatedTransfertoBypass.setStatus("current")
_LgpCondId4321InitiatedTransfertoInverter_ObjectIdentity = ObjectIdentity
lgpCondId4321InitiatedTransfertoInverter = _LgpCondId4321InitiatedTransfertoInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4321)
)
if mibBuilder.loadTexts:
    lgpCondId4321InitiatedTransfertoInverter.setStatus("current")
_LgpCondId4322BatteryTestPassed_ObjectIdentity = ObjectIdentity
lgpCondId4322BatteryTestPassed = _LgpCondId4322BatteryTestPassed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4322)
)
if mibBuilder.loadTexts:
    lgpCondId4322BatteryTestPassed.setStatus("current")
_LgpCondId4323BatteryTestFailed_ObjectIdentity = ObjectIdentity
lgpCondId4323BatteryTestFailed = _LgpCondId4323BatteryTestFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4323)
)
if mibBuilder.loadTexts:
    lgpCondId4323BatteryTestFailed.setStatus("current")
_LgpCondId4324BatteryTestManuallyStopped_ObjectIdentity = ObjectIdentity
lgpCondId4324BatteryTestManuallyStopped = _LgpCondId4324BatteryTestManuallyStopped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4324)
)
if mibBuilder.loadTexts:
    lgpCondId4324BatteryTestManuallyStopped.setStatus("current")
_LgpCondId4325BackfeedBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId4325BackfeedBreakerOpen = _LgpCondId4325BackfeedBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4325)
)
if mibBuilder.loadTexts:
    lgpCondId4325BackfeedBreakerOpen.setStatus("current")
_LgpCondId4341VelocityAuthenticationFailure_ObjectIdentity = ObjectIdentity
lgpCondId4341VelocityAuthenticationFailure = _LgpCondId4341VelocityAuthenticationFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4341)
)
if mibBuilder.loadTexts:
    lgpCondId4341VelocityAuthenticationFailure.setStatus("current")
_LgpCondId4360ReceptacleOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4360ReceptacleOverCurrent = _LgpCondId4360ReceptacleOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4360)
)
if mibBuilder.loadTexts:
    lgpCondId4360ReceptacleOverCurrent.setStatus("current")
_LgpCondId4361ReceptacleUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4361ReceptacleUnderCurrent = _LgpCondId4361ReceptacleUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4361)
)
if mibBuilder.loadTexts:
    lgpCondId4361ReceptacleUnderCurrent.setStatus("current")
_LgpCondId4382SystemInputCurrentImbalance_ObjectIdentity = ObjectIdentity
lgpCondId4382SystemInputCurrentImbalance = _LgpCondId4382SystemInputCurrentImbalance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4382)
)
if mibBuilder.loadTexts:
    lgpCondId4382SystemInputCurrentImbalance.setStatus("current")
_LgpCondId4383BypassStaticSwitchOffExtrnl_ObjectIdentity = ObjectIdentity
lgpCondId4383BypassStaticSwitchOffExtrnl = _LgpCondId4383BypassStaticSwitchOffExtrnl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4383)
)
if mibBuilder.loadTexts:
    lgpCondId4383BypassStaticSwitchOffExtrnl.setStatus("current")
_LgpCondId4384BatteryEoDDisconnect_ObjectIdentity = ObjectIdentity
lgpCondId4384BatteryEoDDisconnect = _LgpCondId4384BatteryEoDDisconnect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4384)
)
if mibBuilder.loadTexts:
    lgpCondId4384BatteryEoDDisconnect.setStatus("current")
_LgpCondId4389SystemOutputFault_ObjectIdentity = ObjectIdentity
lgpCondId4389SystemOutputFault = _LgpCondId4389SystemOutputFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4389)
)
if mibBuilder.loadTexts:
    lgpCondId4389SystemOutputFault.setStatus("current")
_LgpCondId4390InverterOffExternal_ObjectIdentity = ObjectIdentity
lgpCondId4390InverterOffExternal = _LgpCondId4390InverterOffExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4390)
)
if mibBuilder.loadTexts:
    lgpCondId4390InverterOffExternal.setStatus("current")
_LgpCondId4391InverterStaticSwitchSCRShort_ObjectIdentity = ObjectIdentity
lgpCondId4391InverterStaticSwitchSCRShort = _LgpCondId4391InverterStaticSwitchSCRShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4391)
)
if mibBuilder.loadTexts:
    lgpCondId4391InverterStaticSwitchSCRShort.setStatus("current")
_LgpCondId4392TemperatureSensorError_ObjectIdentity = ObjectIdentity
lgpCondId4392TemperatureSensorError = _LgpCondId4392TemperatureSensorError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4392)
)
if mibBuilder.loadTexts:
    lgpCondId4392TemperatureSensorError.setStatus("current")
_LgpCondId4406BranchOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4406BranchOverCurrent = _LgpCondId4406BranchOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4406)
)
if mibBuilder.loadTexts:
    lgpCondId4406BranchOverCurrent.setStatus("current")
_LgpCondId4407BranchUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4407BranchUnderCurrent = _LgpCondId4407BranchUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4407)
)
if mibBuilder.loadTexts:
    lgpCondId4407BranchUnderCurrent.setStatus("current")
_LgpCondId4416BranchOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4416BranchOverCurrent = _LgpCondId4416BranchOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4416)
)
if mibBuilder.loadTexts:
    lgpCondId4416BranchOverCurrent.setStatus("current")
_LgpCondId4417BranchUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4417BranchUnderCurrent = _LgpCondId4417BranchUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4417)
)
if mibBuilder.loadTexts:
    lgpCondId4417BranchUnderCurrent.setStatus("current")
_LgpCondId4421BranchFailure_ObjectIdentity = ObjectIdentity
lgpCondId4421BranchFailure = _LgpCondId4421BranchFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4421)
)
if mibBuilder.loadTexts:
    lgpCondId4421BranchFailure.setStatus("current")
_LgpCondId4436PDUOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4436PDUOverCurrent = _LgpCondId4436PDUOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4436)
)
if mibBuilder.loadTexts:
    lgpCondId4436PDUOverCurrent.setStatus("current")
_LgpCondId4437PDUUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4437PDUUnderCurrent = _LgpCondId4437PDUUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4437)
)
if mibBuilder.loadTexts:
    lgpCondId4437PDUUnderCurrent.setStatus("current")
_LgpCondId4438SystemInternalTemperatureRise_ObjectIdentity = ObjectIdentity
lgpCondId4438SystemInternalTemperatureRise = _LgpCondId4438SystemInternalTemperatureRise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4438)
)
if mibBuilder.loadTexts:
    lgpCondId4438SystemInternalTemperatureRise.setStatus("current")
_LgpCondId4439AutomaticRestartFailed_ObjectIdentity = ObjectIdentity
lgpCondId4439AutomaticRestartFailed = _LgpCondId4439AutomaticRestartFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4439)
)
if mibBuilder.loadTexts:
    lgpCondId4439AutomaticRestartFailed.setStatus("current")
_LgpCondId4440FuseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4440FuseFailure = _LgpCondId4440FuseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4440)
)
if mibBuilder.loadTexts:
    lgpCondId4440FuseFailure.setStatus("current")
_LgpCondId4441SystemControllerError_ObjectIdentity = ObjectIdentity
lgpCondId4441SystemControllerError = _LgpCondId4441SystemControllerError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4441)
)
if mibBuilder.loadTexts:
    lgpCondId4441SystemControllerError.setStatus("current")
_LgpCondId4442SystemBreakersOpenFailure_ObjectIdentity = ObjectIdentity
lgpCondId4442SystemBreakersOpenFailure = _LgpCondId4442SystemBreakersOpenFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4442)
)
if mibBuilder.loadTexts:
    lgpCondId4442SystemBreakersOpenFailure.setStatus("current")
_LgpCondId4448PDUOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4448PDUOverCurrent = _LgpCondId4448PDUOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4448)
)
if mibBuilder.loadTexts:
    lgpCondId4448PDUOverCurrent.setStatus("current")
_LgpCondId4449PDUUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4449PDUUnderCurrent = _LgpCondId4449PDUUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4449)
)
if mibBuilder.loadTexts:
    lgpCondId4449PDUUnderCurrent.setStatus("current")
_LgpCondId4468PDUOverCurrentL1_ObjectIdentity = ObjectIdentity
lgpCondId4468PDUOverCurrentL1 = _LgpCondId4468PDUOverCurrentL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4468)
)
if mibBuilder.loadTexts:
    lgpCondId4468PDUOverCurrentL1.setStatus("current")
_LgpCondId4469PDUOverCurrentL2_ObjectIdentity = ObjectIdentity
lgpCondId4469PDUOverCurrentL2 = _LgpCondId4469PDUOverCurrentL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4469)
)
if mibBuilder.loadTexts:
    lgpCondId4469PDUOverCurrentL2.setStatus("current")
_LgpCondId4470PDUOverCurrentL3_ObjectIdentity = ObjectIdentity
lgpCondId4470PDUOverCurrentL3 = _LgpCondId4470PDUOverCurrentL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4470)
)
if mibBuilder.loadTexts:
    lgpCondId4470PDUOverCurrentL3.setStatus("current")
_LgpCondId4471PDUUnderCurrentL1_ObjectIdentity = ObjectIdentity
lgpCondId4471PDUUnderCurrentL1 = _LgpCondId4471PDUUnderCurrentL1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4471)
)
if mibBuilder.loadTexts:
    lgpCondId4471PDUUnderCurrentL1.setStatus("current")
_LgpCondId4472PDUUnderCurrentL2_ObjectIdentity = ObjectIdentity
lgpCondId4472PDUUnderCurrentL2 = _LgpCondId4472PDUUnderCurrentL2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4472)
)
if mibBuilder.loadTexts:
    lgpCondId4472PDUUnderCurrentL2.setStatus("current")
_LgpCondId4473PDUUnderCurrentL3_ObjectIdentity = ObjectIdentity
lgpCondId4473PDUUnderCurrentL3 = _LgpCondId4473PDUUnderCurrentL3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4473)
)
if mibBuilder.loadTexts:
    lgpCondId4473PDUUnderCurrentL3.setStatus("current")
_LgpCondId4492ReceptaclePowerStateOn_ObjectIdentity = ObjectIdentity
lgpCondId4492ReceptaclePowerStateOn = _LgpCondId4492ReceptaclePowerStateOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4492)
)
if mibBuilder.loadTexts:
    lgpCondId4492ReceptaclePowerStateOn.setStatus("current")
_LgpCondId4493ReceptaclePowerStateOff_ObjectIdentity = ObjectIdentity
lgpCondId4493ReceptaclePowerStateOff = _LgpCondId4493ReceptaclePowerStateOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4493)
)
if mibBuilder.loadTexts:
    lgpCondId4493ReceptaclePowerStateOff.setStatus("current")
_LgpCondId4494BranchBreakerOpen_ObjectIdentity = ObjectIdentity
lgpCondId4494BranchBreakerOpen = _LgpCondId4494BranchBreakerOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4494)
)
if mibBuilder.loadTexts:
    lgpCondId4494BranchBreakerOpen.setStatus("current")
_LgpCondId4495DeviceConfigurationChange_ObjectIdentity = ObjectIdentity
lgpCondId4495DeviceConfigurationChange = _LgpCondId4495DeviceConfigurationChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4495)
)
if mibBuilder.loadTexts:
    lgpCondId4495DeviceConfigurationChange.setStatus("current")
_LgpCondId4496BasicDisplayModuleRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4496BasicDisplayModuleRemoved = _LgpCondId4496BasicDisplayModuleRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4496)
)
if mibBuilder.loadTexts:
    lgpCondId4496BasicDisplayModuleRemoved.setStatus("current")
_LgpCondId4497BasicDisplayModuleDiscovered_ObjectIdentity = ObjectIdentity
lgpCondId4497BasicDisplayModuleDiscovered = _LgpCondId4497BasicDisplayModuleDiscovered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4497)
)
if mibBuilder.loadTexts:
    lgpCondId4497BasicDisplayModuleDiscovered.setStatus("current")
_LgpCondId4500PDUOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4500PDUOverCurrent = _LgpCondId4500PDUOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4500)
)
if mibBuilder.loadTexts:
    lgpCondId4500PDUOverCurrent.setStatus("current")
_LgpCondId4501PDUUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4501PDUUnderCurrent = _LgpCondId4501PDUUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4501)
)
if mibBuilder.loadTexts:
    lgpCondId4501PDUUnderCurrent.setStatus("current")
_LgpCondId4502PDUFailure_ObjectIdentity = ObjectIdentity
lgpCondId4502PDUFailure = _LgpCondId4502PDUFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4502)
)
if mibBuilder.loadTexts:
    lgpCondId4502PDUFailure.setStatus("current")
_LgpCondId4503PDUCommunicationFail_ObjectIdentity = ObjectIdentity
lgpCondId4503PDUCommunicationFail = _LgpCondId4503PDUCommunicationFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4503)
)
if mibBuilder.loadTexts:
    lgpCondId4503PDUCommunicationFail.setStatus("current")
_LgpCondId4504BranchRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4504BranchRemoved = _LgpCondId4504BranchRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4504)
)
if mibBuilder.loadTexts:
    lgpCondId4504BranchRemoved.setStatus("current")
_LgpCondId4505BranchDiscovered_ObjectIdentity = ObjectIdentity
lgpCondId4505BranchDiscovered = _LgpCondId4505BranchDiscovered_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4505)
)
if mibBuilder.loadTexts:
    lgpCondId4505BranchDiscovered.setStatus("current")
_LgpCondId4506BranchOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4506BranchOverCurrent = _LgpCondId4506BranchOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4506)
)
if mibBuilder.loadTexts:
    lgpCondId4506BranchOverCurrent.setStatus("current")
_LgpCondId4507BranchCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4507BranchCurrent = _LgpCondId4507BranchCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4507)
)
if mibBuilder.loadTexts:
    lgpCondId4507BranchCurrent.setStatus("current")
_LgpCondId4508ReceptacleLoadRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4508ReceptacleLoadRemoved = _LgpCondId4508ReceptacleLoadRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4508)
)
if mibBuilder.loadTexts:
    lgpCondId4508ReceptacleLoadRemoved.setStatus("current")
_LgpCondId4509ReceptacleLoadAdded_ObjectIdentity = ObjectIdentity
lgpCondId4509ReceptacleLoadAdded = _LgpCondId4509ReceptacleLoadAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4509)
)
if mibBuilder.loadTexts:
    lgpCondId4509ReceptacleLoadAdded.setStatus("current")
_LgpCondId4523ModuleRemoved_ObjectIdentity = ObjectIdentity
lgpCondId4523ModuleRemoved = _LgpCondId4523ModuleRemoved_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4523)
)
if mibBuilder.loadTexts:
    lgpCondId4523ModuleRemoved.setStatus("current")
_LgpCondId4524ModuleAdded_ObjectIdentity = ObjectIdentity
lgpCondId4524ModuleAdded = _LgpCondId4524ModuleAdded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4524)
)
if mibBuilder.loadTexts:
    lgpCondId4524ModuleAdded.setStatus("current")
_LgpCondId4550FirmwareUpdateRequired_ObjectIdentity = ObjectIdentity
lgpCondId4550FirmwareUpdateRequired = _LgpCondId4550FirmwareUpdateRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4550)
)
if mibBuilder.loadTexts:
    lgpCondId4550FirmwareUpdateRequired.setStatus("current")
_LgpCondId4551GenericTestEvent_ObjectIdentity = ObjectIdentity
lgpCondId4551GenericTestEvent = _LgpCondId4551GenericTestEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4551)
)
if mibBuilder.loadTexts:
    lgpCondId4551GenericTestEvent.setStatus("current")
_LgpCondId4580OverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4580OverTemperature = _LgpCondId4580OverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4580)
)
if mibBuilder.loadTexts:
    lgpCondId4580OverTemperature.setStatus("current")
_LgpCondId4581UnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4581UnderTemperature = _LgpCondId4581UnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4581)
)
if mibBuilder.loadTexts:
    lgpCondId4581UnderTemperature.setStatus("current")
_LgpCondId4588OverRelativeHumidity_ObjectIdentity = ObjectIdentity
lgpCondId4588OverRelativeHumidity = _LgpCondId4588OverRelativeHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4588)
)
if mibBuilder.loadTexts:
    lgpCondId4588OverRelativeHumidity.setStatus("current")
_LgpCondId4589UnderRelativeHumidity_ObjectIdentity = ObjectIdentity
lgpCondId4589UnderRelativeHumidity = _LgpCondId4589UnderRelativeHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4589)
)
if mibBuilder.loadTexts:
    lgpCondId4589UnderRelativeHumidity.setStatus("current")
_LgpCondId4601ExternalAirSensorAOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4601ExternalAirSensorAOverTemperature = _LgpCondId4601ExternalAirSensorAOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4601)
)
if mibBuilder.loadTexts:
    lgpCondId4601ExternalAirSensorAOverTemperature.setStatus("current")
_LgpCondId4604ExternalAirSensorBOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4604ExternalAirSensorBOverTemperature = _LgpCondId4604ExternalAirSensorBOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4604)
)
if mibBuilder.loadTexts:
    lgpCondId4604ExternalAirSensorBOverTemperature.setStatus("current")
_LgpCondId4608ExtAirSensorAUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4608ExtAirSensorAUnderTemperature = _LgpCondId4608ExtAirSensorAUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4608)
)
if mibBuilder.loadTexts:
    lgpCondId4608ExtAirSensorAUnderTemperature.setStatus("current")
_LgpCondId4611ExtAirSensorBUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4611ExtAirSensorBUnderTemperature = _LgpCondId4611ExtAirSensorBUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4611)
)
if mibBuilder.loadTexts:
    lgpCondId4611ExtAirSensorBUnderTemperature.setStatus("current")
_LgpCondId4615ExtDewPointOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4615ExtDewPointOverTemperature = _LgpCondId4615ExtDewPointOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4615)
)
if mibBuilder.loadTexts:
    lgpCondId4615ExtDewPointOverTemperature.setStatus("current")
_LgpCondId4618ExternalAirSensorAIssue_ObjectIdentity = ObjectIdentity
lgpCondId4618ExternalAirSensorAIssue = _LgpCondId4618ExternalAirSensorAIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4618)
)
if mibBuilder.loadTexts:
    lgpCondId4618ExternalAirSensorAIssue.setStatus("current")
_LgpCondId4621ExternalAirSensorBIssue_ObjectIdentity = ObjectIdentity
lgpCondId4621ExternalAirSensorBIssue = _LgpCondId4621ExternalAirSensorBIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4621)
)
if mibBuilder.loadTexts:
    lgpCondId4621ExternalAirSensorBIssue.setStatus("current")
_LgpCondId4626SupplyChilledWaterOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId4626SupplyChilledWaterOverTemp = _LgpCondId4626SupplyChilledWaterOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4626)
)
if mibBuilder.loadTexts:
    lgpCondId4626SupplyChilledWaterOverTemp.setStatus("current")
_LgpCondId4629SupplyChilledWaterTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId4629SupplyChilledWaterTempSensorIssue = _LgpCondId4629SupplyChilledWaterTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4629)
)
if mibBuilder.loadTexts:
    lgpCondId4629SupplyChilledWaterTempSensorIssue.setStatus("current")
_LgpCondId4634SupplyRefrigerantOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId4634SupplyRefrigerantOverTemp = _LgpCondId4634SupplyRefrigerantOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4634)
)
if mibBuilder.loadTexts:
    lgpCondId4634SupplyRefrigerantOverTemp.setStatus("current")
_LgpCondId4637SupplyRefrigerantUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId4637SupplyRefrigerantUnderTemp = _LgpCondId4637SupplyRefrigerantUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4637)
)
if mibBuilder.loadTexts:
    lgpCondId4637SupplyRefrigerantUnderTemp.setStatus("current")
_LgpCondId4640SupplyRefrigerantTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId4640SupplyRefrigerantTempSensorIssue = _LgpCondId4640SupplyRefrigerantTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4640)
)
if mibBuilder.loadTexts:
    lgpCondId4640SupplyRefrigerantTempSensorIssue.setStatus("current")
_LgpCondId4645SupplyFluidOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId4645SupplyFluidOverTemp = _LgpCondId4645SupplyFluidOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4645)
)
if mibBuilder.loadTexts:
    lgpCondId4645SupplyFluidOverTemp.setStatus("current")
_LgpCondId4648SupplyFluidUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId4648SupplyFluidUnderTemp = _LgpCondId4648SupplyFluidUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4648)
)
if mibBuilder.loadTexts:
    lgpCondId4648SupplyFluidUnderTemp.setStatus("current")
_LgpCondId4651SupplyFluidTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId4651SupplyFluidTempSensorIssue = _LgpCondId4651SupplyFluidTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4651)
)
if mibBuilder.loadTexts:
    lgpCondId4651SupplyFluidTempSensorIssue.setStatus("current")
_LgpCondId4656Pump1LossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId4656Pump1LossofFlow = _LgpCondId4656Pump1LossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4656)
)
if mibBuilder.loadTexts:
    lgpCondId4656Pump1LossofFlow.setStatus("current")
_LgpCondId4659Pump2LossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId4659Pump2LossofFlow = _LgpCondId4659Pump2LossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4659)
)
if mibBuilder.loadTexts:
    lgpCondId4659Pump2LossofFlow.setStatus("current")
_LgpCondId4662PumpShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4662PumpShortCycle = _LgpCondId4662PumpShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4662)
)
if mibBuilder.loadTexts:
    lgpCondId4662PumpShortCycle.setStatus("current")
_LgpCondId4669Compressor1AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4669Compressor1AHighHeadPressure = _LgpCondId4669Compressor1AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4669)
)
if mibBuilder.loadTexts:
    lgpCondId4669Compressor1AHighHeadPressure.setStatus("current")
_LgpCondId4672Compressor1BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4672Compressor1BHighHeadPressure = _LgpCondId4672Compressor1BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4672)
)
if mibBuilder.loadTexts:
    lgpCondId4672Compressor1BHighHeadPressure.setStatus("current")
_LgpCondId4675Compressor2AHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4675Compressor2AHighHeadPressure = _LgpCondId4675Compressor2AHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4675)
)
if mibBuilder.loadTexts:
    lgpCondId4675Compressor2AHighHeadPressure.setStatus("current")
_LgpCondId4678Compressor2BHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId4678Compressor2BHighHeadPressure = _LgpCondId4678Compressor2BHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4678)
)
if mibBuilder.loadTexts:
    lgpCondId4678Compressor2BHighHeadPressure.setStatus("current")
_LgpCondId4681Compressor1AShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4681Compressor1AShortCycle = _LgpCondId4681Compressor1AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4681)
)
if mibBuilder.loadTexts:
    lgpCondId4681Compressor1AShortCycle.setStatus("current")
_LgpCondId4684Compressor1BShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4684Compressor1BShortCycle = _LgpCondId4684Compressor1BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4684)
)
if mibBuilder.loadTexts:
    lgpCondId4684Compressor1BShortCycle.setStatus("current")
_LgpCondId4687Compressor2AShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4687Compressor2AShortCycle = _LgpCondId4687Compressor2AShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4687)
)
if mibBuilder.loadTexts:
    lgpCondId4687Compressor2AShortCycle.setStatus("current")
_LgpCondId4690Compressor2BShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4690Compressor2BShortCycle = _LgpCondId4690Compressor2BShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4690)
)
if mibBuilder.loadTexts:
    lgpCondId4690Compressor2BShortCycle.setStatus("current")
_LgpCondId4693Tandem1LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId4693Tandem1LowSuctionPressure = _LgpCondId4693Tandem1LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4693)
)
if mibBuilder.loadTexts:
    lgpCondId4693Tandem1LowSuctionPressure.setStatus("current")
_LgpCondId4696Tandem2LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId4696Tandem2LowSuctionPressure = _LgpCondId4696Tandem2LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4696)
)
if mibBuilder.loadTexts:
    lgpCondId4696Tandem2LowSuctionPressure.setStatus("current")
_LgpCondId4703ChilledWaterControlValvePosition_ObjectIdentity = ObjectIdentity
lgpCondId4703ChilledWaterControlValvePosition = _LgpCondId4703ChilledWaterControlValvePosition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4703)
)
if mibBuilder.loadTexts:
    lgpCondId4703ChilledWaterControlValvePosition.setStatus("current")
_LgpCondId4711SystemCondensationDetected_ObjectIdentity = ObjectIdentity
lgpCondId4711SystemCondensationDetected = _LgpCondId4711SystemCondensationDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4711)
)
if mibBuilder.loadTexts:
    lgpCondId4711SystemCondensationDetected.setStatus("current")
_LgpCondId4714ShutdownLossOfPower_ObjectIdentity = ObjectIdentity
lgpCondId4714ShutdownLossOfPower = _LgpCondId4714ShutdownLossOfPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4714)
)
if mibBuilder.loadTexts:
    lgpCondId4714ShutdownLossOfPower.setStatus("current")
_LgpCondId4720SmokeDetected_ObjectIdentity = ObjectIdentity
lgpCondId4720SmokeDetected = _LgpCondId4720SmokeDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4720)
)
if mibBuilder.loadTexts:
    lgpCondId4720SmokeDetected.setStatus("current")
_LgpCondId4723WaterUnderFloor_ObjectIdentity = ObjectIdentity
lgpCondId4723WaterUnderFloor = _LgpCondId4723WaterUnderFloor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4723)
)
if mibBuilder.loadTexts:
    lgpCondId4723WaterUnderFloor.setStatus("current")
_LgpCondId4726ServiceRequired_ObjectIdentity = ObjectIdentity
lgpCondId4726ServiceRequired = _LgpCondId4726ServiceRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4726)
)
if mibBuilder.loadTexts:
    lgpCondId4726ServiceRequired.setStatus("current")
_LgpCondId4729FanIssue_ObjectIdentity = ObjectIdentity
lgpCondId4729FanIssue = _LgpCondId4729FanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4729)
)
if mibBuilder.loadTexts:
    lgpCondId4729FanIssue.setStatus("current")
_LgpCondId4732ReceptacleLoadDropped_ObjectIdentity = ObjectIdentity
lgpCondId4732ReceptacleLoadDropped = _LgpCondId4732ReceptacleLoadDropped_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4732)
)
if mibBuilder.loadTexts:
    lgpCondId4732ReceptacleLoadDropped.setStatus("current")
_LgpCondId4740BatteryAutomaticTestInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4740BatteryAutomaticTestInhibited = _LgpCondId4740BatteryAutomaticTestInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4740)
)
if mibBuilder.loadTexts:
    lgpCondId4740BatteryAutomaticTestInhibited.setStatus("current")
_LgpCondId4741BatterySelfTest_ObjectIdentity = ObjectIdentity
lgpCondId4741BatterySelfTest = _LgpCondId4741BatterySelfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4741)
)
if mibBuilder.loadTexts:
    lgpCondId4741BatterySelfTest.setStatus("current")
_LgpCondId4742BatteryLowShutdown_ObjectIdentity = ObjectIdentity
lgpCondId4742BatteryLowShutdown = _LgpCondId4742BatteryLowShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4742)
)
if mibBuilder.loadTexts:
    lgpCondId4742BatteryLowShutdown.setStatus("current")
_LgpCondId4747EquipmentTemperatureSensorFail_ObjectIdentity = ObjectIdentity
lgpCondId4747EquipmentTemperatureSensorFail = _LgpCondId4747EquipmentTemperatureSensorFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4747)
)
if mibBuilder.loadTexts:
    lgpCondId4747EquipmentTemperatureSensorFail.setStatus("current")
_LgpCondId4749SystemFanFailureRedundant_ObjectIdentity = ObjectIdentity
lgpCondId4749SystemFanFailureRedundant = _LgpCondId4749SystemFanFailureRedundant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4749)
)
if mibBuilder.loadTexts:
    lgpCondId4749SystemFanFailureRedundant.setStatus("current")
_LgpCondId4750MultipleFanFailure_ObjectIdentity = ObjectIdentity
lgpCondId4750MultipleFanFailure = _LgpCondId4750MultipleFanFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4750)
)
if mibBuilder.loadTexts:
    lgpCondId4750MultipleFanFailure.setStatus("current")
_LgpCondId4753MainControllerFault_ObjectIdentity = ObjectIdentity
lgpCondId4753MainControllerFault = _LgpCondId4753MainControllerFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4753)
)
if mibBuilder.loadTexts:
    lgpCondId4753MainControllerFault.setStatus("current")
_LgpCondId4754SystemBreakersCloseFailure_ObjectIdentity = ObjectIdentity
lgpCondId4754SystemBreakersCloseFailure = _LgpCondId4754SystemBreakersCloseFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4754)
)
if mibBuilder.loadTexts:
    lgpCondId4754SystemBreakersCloseFailure.setStatus("current")
_LgpCondId4755InputFilterCycleLock_ObjectIdentity = ObjectIdentity
lgpCondId4755InputFilterCycleLock = _LgpCondId4755InputFilterCycleLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4755)
)
if mibBuilder.loadTexts:
    lgpCondId4755InputFilterCycleLock.setStatus("current")
_LgpCondId4756ServiceCodeActive_ObjectIdentity = ObjectIdentity
lgpCondId4756ServiceCodeActive = _LgpCondId4756ServiceCodeActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4756)
)
if mibBuilder.loadTexts:
    lgpCondId4756ServiceCodeActive.setStatus("current")
_LgpCondId4757LBSActive_ObjectIdentity = ObjectIdentity
lgpCondId4757LBSActive = _LgpCondId4757LBSActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4757)
)
if mibBuilder.loadTexts:
    lgpCondId4757LBSActive.setStatus("current")
_LgpCondId4758LBSInhibited_ObjectIdentity = ObjectIdentity
lgpCondId4758LBSInhibited = _LgpCondId4758LBSInhibited_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4758)
)
if mibBuilder.loadTexts:
    lgpCondId4758LBSInhibited.setStatus("current")
_LgpCondId4759LeadingPowerFactor_ObjectIdentity = ObjectIdentity
lgpCondId4759LeadingPowerFactor = _LgpCondId4759LeadingPowerFactor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4759)
)
if mibBuilder.loadTexts:
    lgpCondId4759LeadingPowerFactor.setStatus("current")
_LgpCondId4760ControlsResetRequired_ObjectIdentity = ObjectIdentity
lgpCondId4760ControlsResetRequired = _LgpCondId4760ControlsResetRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4760)
)
if mibBuilder.loadTexts:
    lgpCondId4760ControlsResetRequired.setStatus("current")
_LgpCondId4823ParallelCommWarning_ObjectIdentity = ObjectIdentity
lgpCondId4823ParallelCommWarning = _LgpCondId4823ParallelCommWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4823)
)
if mibBuilder.loadTexts:
    lgpCondId4823ParallelCommWarning.setStatus("current")
_LgpCondId4824SystemCommFail_ObjectIdentity = ObjectIdentity
lgpCondId4824SystemCommFail = _LgpCondId4824SystemCommFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4824)
)
if mibBuilder.loadTexts:
    lgpCondId4824SystemCommFail.setStatus("current")
_LgpCondId4825LossofRedundancy_ObjectIdentity = ObjectIdentity
lgpCondId4825LossofRedundancy = _LgpCondId4825LossofRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4825)
)
if mibBuilder.loadTexts:
    lgpCondId4825LossofRedundancy.setStatus("current")
_LgpCondId4826BPSSStartupInhibit_ObjectIdentity = ObjectIdentity
lgpCondId4826BPSSStartupInhibit = _LgpCondId4826BPSSStartupInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4826)
)
if mibBuilder.loadTexts:
    lgpCondId4826BPSSStartupInhibit.setStatus("current")
_LgpCondId4827MMSTransferInhibit_ObjectIdentity = ObjectIdentity
lgpCondId4827MMSTransferInhibit = _LgpCondId4827MMSTransferInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4827)
)
if mibBuilder.loadTexts:
    lgpCondId4827MMSTransferInhibit.setStatus("current")
_LgpCondId4828MMSRetransferInhibit_ObjectIdentity = ObjectIdentity
lgpCondId4828MMSRetransferInhibit = _LgpCondId4828MMSRetransferInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4828)
)
if mibBuilder.loadTexts:
    lgpCondId4828MMSRetransferInhibit.setStatus("current")
_LgpCondId4830MMSLossofSyncPulse_ObjectIdentity = ObjectIdentity
lgpCondId4830MMSLossofSyncPulse = _LgpCondId4830MMSLossofSyncPulse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4830)
)
if mibBuilder.loadTexts:
    lgpCondId4830MMSLossofSyncPulse.setStatus("current")
_LgpCondId4831MMSOverload_ObjectIdentity = ObjectIdentity
lgpCondId4831MMSOverload = _LgpCondId4831MMSOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4831)
)
if mibBuilder.loadTexts:
    lgpCondId4831MMSOverload.setStatus("current")
_LgpCondId4834MMSOnBattery_ObjectIdentity = ObjectIdentity
lgpCondId4834MMSOnBattery = _LgpCondId4834MMSOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4834)
)
if mibBuilder.loadTexts:
    lgpCondId4834MMSOnBattery.setStatus("current")
_LgpCondId4835MMSLowBatteryWarning_ObjectIdentity = ObjectIdentity
lgpCondId4835MMSLowBatteryWarning = _LgpCondId4835MMSLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4835)
)
if mibBuilder.loadTexts:
    lgpCondId4835MMSLowBatteryWarning.setStatus("current")
_LgpCondId4906LowAmbientTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4906LowAmbientTemperature = _LgpCondId4906LowAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4906)
)
if mibBuilder.loadTexts:
    lgpCondId4906LowAmbientTemperature.setStatus("current")
_LgpCondId4907HighAmbientTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4907HighAmbientTemperature = _LgpCondId4907HighAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4907)
)
if mibBuilder.loadTexts:
    lgpCondId4907HighAmbientTemperature.setStatus("current")
_LgpCondId4908LowOverallVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4908LowOverallVoltage = _LgpCondId4908LowOverallVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4908)
)
if mibBuilder.loadTexts:
    lgpCondId4908LowOverallVoltage.setStatus("current")
_LgpCondId4909HighOverallVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4909HighOverallVoltage = _LgpCondId4909HighOverallVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4909)
)
if mibBuilder.loadTexts:
    lgpCondId4909HighOverallVoltage.setStatus("current")
_LgpCondId4910HighBatteryStringCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4910HighBatteryStringCurrent = _LgpCondId4910HighBatteryStringCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4910)
)
if mibBuilder.loadTexts:
    lgpCondId4910HighBatteryStringCurrent.setStatus("current")
_LgpCondId4911LowBatteryStringFloatCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4911LowBatteryStringFloatCurrent = _LgpCondId4911LowBatteryStringFloatCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4911)
)
if mibBuilder.loadTexts:
    lgpCondId4911LowBatteryStringFloatCurrent.setStatus("current")
_LgpCondId4912HighBatteryStringFloatCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4912HighBatteryStringFloatCurrent = _LgpCondId4912HighBatteryStringFloatCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4912)
)
if mibBuilder.loadTexts:
    lgpCondId4912HighBatteryStringFloatCurrent.setStatus("current")
_LgpCondId4913HighBatteryStringRippleCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4913HighBatteryStringRippleCurrent = _LgpCondId4913HighBatteryStringRippleCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4913)
)
if mibBuilder.loadTexts:
    lgpCondId4913HighBatteryStringRippleCurrent.setStatus("current")
_LgpCondId4914BatteryStringDischargeDetected_ObjectIdentity = ObjectIdentity
lgpCondId4914BatteryStringDischargeDetected = _LgpCondId4914BatteryStringDischargeDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4914)
)
if mibBuilder.loadTexts:
    lgpCondId4914BatteryStringDischargeDetected.setStatus("current")
_LgpCondId4915MaximumDischargeTimeExceeded_ObjectIdentity = ObjectIdentity
lgpCondId4915MaximumDischargeTimeExceeded = _LgpCondId4915MaximumDischargeTimeExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4915)
)
if mibBuilder.loadTexts:
    lgpCondId4915MaximumDischargeTimeExceeded.setStatus("current")
_LgpCondId4916DischargeLowOverallVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4916DischargeLowOverallVoltage = _LgpCondId4916DischargeLowOverallVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4916)
)
if mibBuilder.loadTexts:
    lgpCondId4916DischargeLowOverallVoltage.setStatus("current")
_LgpCondId4917DischargeLowCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4917DischargeLowCellVoltage = _LgpCondId4917DischargeLowCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4917)
)
if mibBuilder.loadTexts:
    lgpCondId4917DischargeLowCellVoltage.setStatus("current")
_LgpCondId4918DischargeHighBatteryStringCurrent_ObjectIdentity = ObjectIdentity
lgpCondId4918DischargeHighBatteryStringCurrent = _LgpCondId4918DischargeHighBatteryStringCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4918)
)
if mibBuilder.loadTexts:
    lgpCondId4918DischargeHighBatteryStringCurrent.setStatus("current")
_LgpCondId4919ExcessiveCelltoCellTemperatureDeviation_ObjectIdentity = ObjectIdentity
lgpCondId4919ExcessiveCelltoCellTemperatureDeviation = _LgpCondId4919ExcessiveCelltoCellTemperatureDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4919)
)
if mibBuilder.loadTexts:
    lgpCondId4919ExcessiveCelltoCellTemperatureDeviation.setStatus("current")
_LgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation_ObjectIdentity = ObjectIdentity
lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation = _LgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4920)
)
if mibBuilder.loadTexts:
    lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation.setStatus("current")
_LgpCondId4964LowCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4964LowCellVoltage = _LgpCondId4964LowCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4964)
)
if mibBuilder.loadTexts:
    lgpCondId4964LowCellVoltage.setStatus("current")
_LgpCondId4965HighCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId4965HighCellVoltage = _LgpCondId4965HighCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4965)
)
if mibBuilder.loadTexts:
    lgpCondId4965HighCellVoltage.setStatus("current")
_LgpCondId4966LowCellTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4966LowCellTemperature = _LgpCondId4966LowCellTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4966)
)
if mibBuilder.loadTexts:
    lgpCondId4966LowCellTemperature.setStatus("current")
_LgpCondId4967HighCellTemperature_ObjectIdentity = ObjectIdentity
lgpCondId4967HighCellTemperature = _LgpCondId4967HighCellTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4967)
)
if mibBuilder.loadTexts:
    lgpCondId4967HighCellTemperature.setStatus("current")
_LgpCondId4968LowInternalResistance_ObjectIdentity = ObjectIdentity
lgpCondId4968LowInternalResistance = _LgpCondId4968LowInternalResistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4968)
)
if mibBuilder.loadTexts:
    lgpCondId4968LowInternalResistance.setStatus("current")
_LgpCondId4969HighInternalResistance_ObjectIdentity = ObjectIdentity
lgpCondId4969HighInternalResistance = _LgpCondId4969HighInternalResistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4969)
)
if mibBuilder.loadTexts:
    lgpCondId4969HighInternalResistance.setStatus("current")
_LgpCondId4970HighIntercellResistance_ObjectIdentity = ObjectIdentity
lgpCondId4970HighIntercellResistance = _LgpCondId4970HighIntercellResistance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4970)
)
if mibBuilder.loadTexts:
    lgpCondId4970HighIntercellResistance.setStatus("current")
_LgpCondId4978IntertierResistanceHigh_ObjectIdentity = ObjectIdentity
lgpCondId4978IntertierResistanceHigh = _LgpCondId4978IntertierResistanceHigh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4978)
)
if mibBuilder.loadTexts:
    lgpCondId4978IntertierResistanceHigh.setStatus("current")
_LgpCondId4980SupplyChilledWaterLossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId4980SupplyChilledWaterLossofFlow = _LgpCondId4980SupplyChilledWaterLossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4980)
)
if mibBuilder.loadTexts:
    lgpCondId4980SupplyChilledWaterLossofFlow.setStatus("current")
_LgpCondId4983SupplyRefrigOverTempBand1_ObjectIdentity = ObjectIdentity
lgpCondId4983SupplyRefrigOverTempBand1 = _LgpCondId4983SupplyRefrigOverTempBand1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4983)
)
if mibBuilder.loadTexts:
    lgpCondId4983SupplyRefrigOverTempBand1.setStatus("current")
_LgpCondId4986SupplyRefrigUnderTempBand1_ObjectIdentity = ObjectIdentity
lgpCondId4986SupplyRefrigUnderTempBand1 = _LgpCondId4986SupplyRefrigUnderTempBand1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4986)
)
if mibBuilder.loadTexts:
    lgpCondId4986SupplyRefrigUnderTempBand1.setStatus("current")
_LgpCondId4990SupplyRefrigOverTempBand2_ObjectIdentity = ObjectIdentity
lgpCondId4990SupplyRefrigOverTempBand2 = _LgpCondId4990SupplyRefrigOverTempBand2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4990)
)
if mibBuilder.loadTexts:
    lgpCondId4990SupplyRefrigOverTempBand2.setStatus("current")
_LgpCondId4993SupplyRefrigUnderTempBand2_ObjectIdentity = ObjectIdentity
lgpCondId4993SupplyRefrigUnderTempBand2 = _LgpCondId4993SupplyRefrigUnderTempBand2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4993)
)
if mibBuilder.loadTexts:
    lgpCondId4993SupplyRefrigUnderTempBand2.setStatus("current")
_LgpCondId4996Inverter1ShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4996Inverter1ShortCycle = _LgpCondId4996Inverter1ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4996)
)
if mibBuilder.loadTexts:
    lgpCondId4996Inverter1ShortCycle.setStatus("current")
_LgpCondId4999Inverter2ShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId4999Inverter2ShortCycle = _LgpCondId4999Inverter2ShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 4999)
)
if mibBuilder.loadTexts:
    lgpCondId4999Inverter2ShortCycle.setStatus("current")
_LgpCondId5015SupplyAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5015SupplyAirOverTemperature = _LgpCondId5015SupplyAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5015)
)
if mibBuilder.loadTexts:
    lgpCondId5015SupplyAirOverTemperature.setStatus("current")
_LgpCondId5019SupplyAirUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5019SupplyAirUnderTemperature = _LgpCondId5019SupplyAirUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5019)
)
if mibBuilder.loadTexts:
    lgpCondId5019SupplyAirUnderTemperature.setStatus("current")
_LgpCondId5023ReturnAirOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5023ReturnAirOverTemperature = _LgpCondId5023ReturnAirOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5023)
)
if mibBuilder.loadTexts:
    lgpCondId5023ReturnAirOverTemperature.setStatus("current")
_LgpCondId5026SupplyAirSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5026SupplyAirSensorIssue = _LgpCondId5026SupplyAirSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5026)
)
if mibBuilder.loadTexts:
    lgpCondId5026SupplyAirSensorIssue.setStatus("current")
_LgpCondId5034HighReturnHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5034HighReturnHumidity = _LgpCondId5034HighReturnHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5034)
)
if mibBuilder.loadTexts:
    lgpCondId5034HighReturnHumidity.setStatus("current")
_LgpCondId5036LowReturnHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5036LowReturnHumidity = _LgpCondId5036LowReturnHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5036)
)
if mibBuilder.loadTexts:
    lgpCondId5036LowReturnHumidity.setStatus("current")
_LgpCondId5037HumidifierHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5037HumidifierHoursExceeded = _LgpCondId5037HumidifierHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5037)
)
if mibBuilder.loadTexts:
    lgpCondId5037HumidifierHoursExceeded.setStatus("current")
_LgpCondId5038DehumidifierHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5038DehumidifierHoursExceeded = _LgpCondId5038DehumidifierHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5038)
)
if mibBuilder.loadTexts:
    lgpCondId5038DehumidifierHoursExceeded.setStatus("current")
_LgpCondId5039HumidifierUnderCurrent_ObjectIdentity = ObjectIdentity
lgpCondId5039HumidifierUnderCurrent = _LgpCondId5039HumidifierUnderCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5039)
)
if mibBuilder.loadTexts:
    lgpCondId5039HumidifierUnderCurrent.setStatus("current")
_LgpCondId5040HumidifierOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId5040HumidifierOverCurrent = _LgpCondId5040HumidifierOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5040)
)
if mibBuilder.loadTexts:
    lgpCondId5040HumidifierOverCurrent.setStatus("current")
_LgpCondId5041HumidifierLowWater_ObjectIdentity = ObjectIdentity
lgpCondId5041HumidifierLowWater = _LgpCondId5041HumidifierLowWater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5041)
)
if mibBuilder.loadTexts:
    lgpCondId5041HumidifierLowWater.setStatus("current")
_LgpCondId5042HumidifierCylinderWorn_ObjectIdentity = ObjectIdentity
lgpCondId5042HumidifierCylinderWorn = _LgpCondId5042HumidifierCylinderWorn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5042)
)
if mibBuilder.loadTexts:
    lgpCondId5042HumidifierCylinderWorn.setStatus("current")
_LgpCondId5043HumidifierIssue_ObjectIdentity = ObjectIdentity
lgpCondId5043HumidifierIssue = _LgpCondId5043HumidifierIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5043)
)
if mibBuilder.loadTexts:
    lgpCondId5043HumidifierIssue.setStatus("current")
_LgpCondId5044ExtHumidifierLockout_ObjectIdentity = ObjectIdentity
lgpCondId5044ExtHumidifierLockout = _LgpCondId5044ExtHumidifierLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5044)
)
if mibBuilder.loadTexts:
    lgpCondId5044ExtHumidifierLockout.setStatus("current")
_LgpCondId5045HumidifierControlBoardNotDetected_ObjectIdentity = ObjectIdentity
lgpCondId5045HumidifierControlBoardNotDetected = _LgpCondId5045HumidifierControlBoardNotDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5045)
)
if mibBuilder.loadTexts:
    lgpCondId5045HumidifierControlBoardNotDetected.setStatus("current")
_LgpCondId5046ReturnHumidityOutOfProportionalBand_ObjectIdentity = ObjectIdentity
lgpCondId5046ReturnHumidityOutOfProportionalBand = _LgpCondId5046ReturnHumidityOutOfProportionalBand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5046)
)
if mibBuilder.loadTexts:
    lgpCondId5046ReturnHumidityOutOfProportionalBand.setStatus("current")
_LgpCondId5053LossofAirFlow_ObjectIdentity = ObjectIdentity
lgpCondId5053LossofAirFlow = _LgpCondId5053LossofAirFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5053)
)
if mibBuilder.loadTexts:
    lgpCondId5053LossofAirFlow.setStatus("current")
_LgpCondId5054FanHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5054FanHoursExceeded = _LgpCondId5054FanHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5054)
)
if mibBuilder.loadTexts:
    lgpCondId5054FanHoursExceeded.setStatus("current")
_LgpCondId5055TopFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5055TopFanIssue = _LgpCondId5055TopFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5055)
)
if mibBuilder.loadTexts:
    lgpCondId5055TopFanIssue.setStatus("current")
_LgpCondId5056BottomFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5056BottomFanIssue = _LgpCondId5056BottomFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5056)
)
if mibBuilder.loadTexts:
    lgpCondId5056BottomFanIssue.setStatus("current")
_LgpCondId5060RemoteSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5060RemoteSensorIssue = _LgpCondId5060RemoteSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5060)
)
if mibBuilder.loadTexts:
    lgpCondId5060RemoteSensorIssue.setStatus("current")
_LgpCondId5062Compressor1LowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId5062Compressor1LowSuctionPressure = _LgpCondId5062Compressor1LowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5062)
)
if mibBuilder.loadTexts:
    lgpCondId5062Compressor1LowSuctionPressure.setStatus("current")
_LgpCondId5063Compressor1HoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5063Compressor1HoursExceeded = _LgpCondId5063Compressor1HoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5063)
)
if mibBuilder.loadTexts:
    lgpCondId5063Compressor1HoursExceeded.setStatus("current")
_LgpCondId5064DigScrollComp1TempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5064DigScrollComp1TempSensorIssue = _LgpCondId5064DigScrollComp1TempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5064)
)
if mibBuilder.loadTexts:
    lgpCondId5064DigScrollComp1TempSensorIssue.setStatus("current")
_LgpCondId5065DigScrollComp1OverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5065DigScrollComp1OverTemp = _LgpCondId5065DigScrollComp1OverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5065)
)
if mibBuilder.loadTexts:
    lgpCondId5065DigScrollComp1OverTemp.setStatus("current")
_LgpCondId5066Compressor1LowPressureTransducerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5066Compressor1LowPressureTransducerIssue = _LgpCondId5066Compressor1LowPressureTransducerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5066)
)
if mibBuilder.loadTexts:
    lgpCondId5066Compressor1LowPressureTransducerIssue.setStatus("current")
_LgpCondId5067ExtCompressorLockout_ObjectIdentity = ObjectIdentity
lgpCondId5067ExtCompressorLockout = _LgpCondId5067ExtCompressorLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5067)
)
if mibBuilder.loadTexts:
    lgpCondId5067ExtCompressorLockout.setStatus("current")
_LgpCondId5068ReheaterOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5068ReheaterOverTemperature = _LgpCondId5068ReheaterOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5068)
)
if mibBuilder.loadTexts:
    lgpCondId5068ReheaterOverTemperature.setStatus("current")
_LgpCondId5069ElectricReheater1HoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5069ElectricReheater1HoursExceeded = _LgpCondId5069ElectricReheater1HoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5069)
)
if mibBuilder.loadTexts:
    lgpCondId5069ElectricReheater1HoursExceeded.setStatus("current")
_LgpCondId5070ExtReheatLockout_ObjectIdentity = ObjectIdentity
lgpCondId5070ExtReheatLockout = _LgpCondId5070ExtReheatLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5070)
)
if mibBuilder.loadTexts:
    lgpCondId5070ExtReheatLockout.setStatus("current")
_LgpCondId5071Condenser1Issue_ObjectIdentity = ObjectIdentity
lgpCondId5071Condenser1Issue = _LgpCondId5071Condenser1Issue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5071)
)
if mibBuilder.loadTexts:
    lgpCondId5071Condenser1Issue.setStatus("current")
_LgpCondId5072CondenserVFDIssue_ObjectIdentity = ObjectIdentity
lgpCondId5072CondenserVFDIssue = _LgpCondId5072CondenserVFDIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5072)
)
if mibBuilder.loadTexts:
    lgpCondId5072CondenserVFDIssue.setStatus("current")
_LgpCondId5073CondenserTVSSIssue_ObjectIdentity = ObjectIdentity
lgpCondId5073CondenserTVSSIssue = _LgpCondId5073CondenserTVSSIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5073)
)
if mibBuilder.loadTexts:
    lgpCondId5073CondenserTVSSIssue.setStatus("current")
_LgpCondId5104ExtOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5104ExtOverTemperature = _LgpCondId5104ExtOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5104)
)
if mibBuilder.loadTexts:
    lgpCondId5104ExtOverTemperature.setStatus("current")
_LgpCondId5105ExtLossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId5105ExtLossofFlow = _LgpCondId5105ExtLossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5105)
)
if mibBuilder.loadTexts:
    lgpCondId5105ExtLossofFlow.setStatus("current")
_LgpCondId5106ExtCondenserPumpHighWater_ObjectIdentity = ObjectIdentity
lgpCondId5106ExtCondenserPumpHighWater = _LgpCondId5106ExtCondenserPumpHighWater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5106)
)
if mibBuilder.loadTexts:
    lgpCondId5106ExtCondenserPumpHighWater.setStatus("current")
_LgpCondId5107ExtStandbyGlycolPumpOn_ObjectIdentity = ObjectIdentity
lgpCondId5107ExtStandbyGlycolPumpOn = _LgpCondId5107ExtStandbyGlycolPumpOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5107)
)
if mibBuilder.loadTexts:
    lgpCondId5107ExtStandbyGlycolPumpOn.setStatus("current")
_LgpCondId5108ExternalFireDetected_ObjectIdentity = ObjectIdentity
lgpCondId5108ExternalFireDetected = _LgpCondId5108ExternalFireDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5108)
)
if mibBuilder.loadTexts:
    lgpCondId5108ExternalFireDetected.setStatus("current")
_LgpCondId5109UnitOn_ObjectIdentity = ObjectIdentity
lgpCondId5109UnitOn = _LgpCondId5109UnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5109)
)
if mibBuilder.loadTexts:
    lgpCondId5109UnitOn.setStatus("current")
_LgpCondId5110UnitOff_ObjectIdentity = ObjectIdentity
lgpCondId5110UnitOff = _LgpCondId5110UnitOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5110)
)
if mibBuilder.loadTexts:
    lgpCondId5110UnitOff.setStatus("current")
_LgpCondId5111UnitStandby_ObjectIdentity = ObjectIdentity
lgpCondId5111UnitStandby = _LgpCondId5111UnitStandby_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5111)
)
if mibBuilder.loadTexts:
    lgpCondId5111UnitStandby.setStatus("current")
_LgpCondId5112UnitPartialShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5112UnitPartialShutdown = _LgpCondId5112UnitPartialShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5112)
)
if mibBuilder.loadTexts:
    lgpCondId5112UnitPartialShutdown.setStatus("current")
_LgpCondId5113UnitShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5113UnitShutdown = _LgpCondId5113UnitShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5113)
)
if mibBuilder.loadTexts:
    lgpCondId5113UnitShutdown.setStatus("current")
_LgpCondId5114WaterLeakageDetectorSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5114WaterLeakageDetectorSensorIssue = _LgpCondId5114WaterLeakageDetectorSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5114)
)
if mibBuilder.loadTexts:
    lgpCondId5114WaterLeakageDetectorSensorIssue.setStatus("current")
_LgpCondId5115BMSCommunicationsTimeout_ObjectIdentity = ObjectIdentity
lgpCondId5115BMSCommunicationsTimeout = _LgpCondId5115BMSCommunicationsTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5115)
)
if mibBuilder.loadTexts:
    lgpCondId5115BMSCommunicationsTimeout.setStatus("current")
_LgpCondId5116MaintenanceDue_ObjectIdentity = ObjectIdentity
lgpCondId5116MaintenanceDue = _LgpCondId5116MaintenanceDue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5116)
)
if mibBuilder.loadTexts:
    lgpCondId5116MaintenanceDue.setStatus("current")
_LgpCondId5117MaintenanceCompleted_ObjectIdentity = ObjectIdentity
lgpCondId5117MaintenanceCompleted = _LgpCondId5117MaintenanceCompleted_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5117)
)
if mibBuilder.loadTexts:
    lgpCondId5117MaintenanceCompleted.setStatus("current")
_LgpCondId5118CloggedAirFilter_ObjectIdentity = ObjectIdentity
lgpCondId5118CloggedAirFilter = _LgpCondId5118CloggedAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5118)
)
if mibBuilder.loadTexts:
    lgpCondId5118CloggedAirFilter.setStatus("current")
_LgpCondId5119RAMBatteryIssue_ObjectIdentity = ObjectIdentity
lgpCondId5119RAMBatteryIssue = _LgpCondId5119RAMBatteryIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5119)
)
if mibBuilder.loadTexts:
    lgpCondId5119RAMBatteryIssue.setStatus("current")
_LgpCondId5120MasterUnitCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5120MasterUnitCommunicationLost = _LgpCondId5120MasterUnitCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5120)
)
if mibBuilder.loadTexts:
    lgpCondId5120MasterUnitCommunicationLost.setStatus("current")
_LgpCondId5121HighPowerShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5121HighPowerShutdown = _LgpCondId5121HighPowerShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5121)
)
if mibBuilder.loadTexts:
    lgpCondId5121HighPowerShutdown.setStatus("current")
_LgpCondId5126DigScrollComp2OverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5126DigScrollComp2OverTemp = _LgpCondId5126DigScrollComp2OverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5126)
)
if mibBuilder.loadTexts:
    lgpCondId5126DigScrollComp2OverTemp.setStatus("current")
_LgpCondId5144OutputOfUf_ObjectIdentity = ObjectIdentity
lgpCondId5144OutputOfUf = _LgpCondId5144OutputOfUf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5144)
)
if mibBuilder.loadTexts:
    lgpCondId5144OutputOfUf.setStatus("current")
_LgpCondId5145MMSModuleAlarmActive_ObjectIdentity = ObjectIdentity
lgpCondId5145MMSModuleAlarmActive = _LgpCondId5145MMSModuleAlarmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5145)
)
if mibBuilder.loadTexts:
    lgpCondId5145MMSModuleAlarmActive.setStatus("current")
_LgpCondId5146CompressorPumpDownIssue_ObjectIdentity = ObjectIdentity
lgpCondId5146CompressorPumpDownIssue = _LgpCondId5146CompressorPumpDownIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5146)
)
if mibBuilder.loadTexts:
    lgpCondId5146CompressorPumpDownIssue.setStatus("current")
_LgpCondId5147ReturnAirSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5147ReturnAirSensorIssue = _LgpCondId5147ReturnAirSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5147)
)
if mibBuilder.loadTexts:
    lgpCondId5147ReturnAirSensorIssue.setStatus("current")
_LgpCondId5148CompressorHighPressureTransducerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5148CompressorHighPressureTransducerIssue = _LgpCondId5148CompressorHighPressureTransducerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5148)
)
if mibBuilder.loadTexts:
    lgpCondId5148CompressorHighPressureTransducerIssue.setStatus("current")
_LgpCondId5149BatteryNotQualified_ObjectIdentity = ObjectIdentity
lgpCondId5149BatteryNotQualified = _LgpCondId5149BatteryNotQualified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5149)
)
if mibBuilder.loadTexts:
    lgpCondId5149BatteryNotQualified.setStatus("current")
_LgpCondId5150BatteryTerminalsReversed_ObjectIdentity = ObjectIdentity
lgpCondId5150BatteryTerminalsReversed = _LgpCondId5150BatteryTerminalsReversed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5150)
)
if mibBuilder.loadTexts:
    lgpCondId5150BatteryTerminalsReversed.setStatus("current")
_LgpCondId5151BatteryConverterFailure_ObjectIdentity = ObjectIdentity
lgpCondId5151BatteryConverterFailure = _LgpCondId5151BatteryConverterFailure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5151)
)
if mibBuilder.loadTexts:
    lgpCondId5151BatteryConverterFailure.setStatus("current")
_LgpCondId5152InverterSCROpen_ObjectIdentity = ObjectIdentity
lgpCondId5152InverterSCROpen = _LgpCondId5152InverterSCROpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5152)
)
if mibBuilder.loadTexts:
    lgpCondId5152InverterSCROpen.setStatus("current")
_LgpCondId5153LoadSharingFault_ObjectIdentity = ObjectIdentity
lgpCondId5153LoadSharingFault = _LgpCondId5153LoadSharingFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5153)
)
if mibBuilder.loadTexts:
    lgpCondId5153LoadSharingFault.setStatus("current")
_LgpCondId5154DCBusAbnormal_ObjectIdentity = ObjectIdentity
lgpCondId5154DCBusAbnormal = _LgpCondId5154DCBusAbnormal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5154)
)
if mibBuilder.loadTexts:
    lgpCondId5154DCBusAbnormal.setStatus("current")
_LgpCondId5155MainsInputNeutralLost_ObjectIdentity = ObjectIdentity
lgpCondId5155MainsInputNeutralLost = _LgpCondId5155MainsInputNeutralLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5155)
)
if mibBuilder.loadTexts:
    lgpCondId5155MainsInputNeutralLost.setStatus("current")
_LgpCondId5156LoadImpactTransfer_ObjectIdentity = ObjectIdentity
lgpCondId5156LoadImpactTransfer = _LgpCondId5156LoadImpactTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5156)
)
if mibBuilder.loadTexts:
    lgpCondId5156LoadImpactTransfer.setStatus("current")
_LgpCondId5157UserOperationInvalid_ObjectIdentity = ObjectIdentity
lgpCondId5157UserOperationInvalid = _LgpCondId5157UserOperationInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5157)
)
if mibBuilder.loadTexts:
    lgpCondId5157UserOperationInvalid.setStatus("current")
_LgpCondId5158PowerSubModuleFault_ObjectIdentity = ObjectIdentity
lgpCondId5158PowerSubModuleFault = _LgpCondId5158PowerSubModuleFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5158)
)
if mibBuilder.loadTexts:
    lgpCondId5158PowerSubModuleFault.setStatus("current")
_LgpCondId5178OutputOvervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5178OutputOvervoltage = _LgpCondId5178OutputOvervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5178)
)
if mibBuilder.loadTexts:
    lgpCondId5178OutputOvervoltage.setStatus("current")
_LgpCondId5179OutputUndervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5179OutputUndervoltage = _LgpCondId5179OutputUndervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5179)
)
if mibBuilder.loadTexts:
    lgpCondId5179OutputUndervoltage.setStatus("current")
_LgpCondId5180OutputOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5180OutputOvercurrent = _LgpCondId5180OutputOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5180)
)
if mibBuilder.loadTexts:
    lgpCondId5180OutputOvercurrent.setStatus("current")
_LgpCondId5181NeutralOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5181NeutralOvercurrent = _LgpCondId5181NeutralOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5181)
)
if mibBuilder.loadTexts:
    lgpCondId5181NeutralOvercurrent.setStatus("current")
_LgpCondId5182GroundOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5182GroundOvercurrent = _LgpCondId5182GroundOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5182)
)
if mibBuilder.loadTexts:
    lgpCondId5182GroundOvercurrent.setStatus("current")
_LgpCondId5183OutputVoltageTHD_ObjectIdentity = ObjectIdentity
lgpCondId5183OutputVoltageTHD = _LgpCondId5183OutputVoltageTHD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5183)
)
if mibBuilder.loadTexts:
    lgpCondId5183OutputVoltageTHD.setStatus("current")
_LgpCondId5184OutputFrequencyError_ObjectIdentity = ObjectIdentity
lgpCondId5184OutputFrequencyError = _LgpCondId5184OutputFrequencyError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5184)
)
if mibBuilder.loadTexts:
    lgpCondId5184OutputFrequencyError.setStatus("current")
_LgpCondId5185TransformerOvertemperature_ObjectIdentity = ObjectIdentity
lgpCondId5185TransformerOvertemperature = _LgpCondId5185TransformerOvertemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5185)
)
if mibBuilder.loadTexts:
    lgpCondId5185TransformerOvertemperature.setStatus("current")
_LgpCondId5212PanelSummaryStatus_ObjectIdentity = ObjectIdentity
lgpCondId5212PanelSummaryStatus = _LgpCondId5212PanelSummaryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5212)
)
if mibBuilder.loadTexts:
    lgpCondId5212PanelSummaryStatus.setStatus("current")
_LgpCondId5213PanelOvervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5213PanelOvervoltage = _LgpCondId5213PanelOvervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5213)
)
if mibBuilder.loadTexts:
    lgpCondId5213PanelOvervoltage.setStatus("current")
_LgpCondId5214PanelUndervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5214PanelUndervoltage = _LgpCondId5214PanelUndervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5214)
)
if mibBuilder.loadTexts:
    lgpCondId5214PanelUndervoltage.setStatus("current")
_LgpCondId5215PanelOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5215PanelOvercurrent = _LgpCondId5215PanelOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5215)
)
if mibBuilder.loadTexts:
    lgpCondId5215PanelOvercurrent.setStatus("current")
_LgpCondId5216PanelNeutralOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5216PanelNeutralOvercurrent = _LgpCondId5216PanelNeutralOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5216)
)
if mibBuilder.loadTexts:
    lgpCondId5216PanelNeutralOvercurrent.setStatus("current")
_LgpCondId5217PanelGroundOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5217PanelGroundOvercurrent = _LgpCondId5217PanelGroundOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5217)
)
if mibBuilder.loadTexts:
    lgpCondId5217PanelGroundOvercurrent.setStatus("current")
_LgpCondId5226BranchOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5226BranchOvercurrent = _LgpCondId5226BranchOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5226)
)
if mibBuilder.loadTexts:
    lgpCondId5226BranchOvercurrent.setStatus("current")
_LgpCondId5227BranchUndercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5227BranchUndercurrent = _LgpCondId5227BranchUndercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5227)
)
if mibBuilder.loadTexts:
    lgpCondId5227BranchUndercurrent.setStatus("current")
_LgpCondId5245SubfeedPhaseOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5245SubfeedPhaseOvercurrent = _LgpCondId5245SubfeedPhaseOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5245)
)
if mibBuilder.loadTexts:
    lgpCondId5245SubfeedPhaseOvercurrent.setStatus("current")
_LgpCondId5246SubfeedNeutralOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5246SubfeedNeutralOvercurrent = _LgpCondId5246SubfeedNeutralOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5246)
)
if mibBuilder.loadTexts:
    lgpCondId5246SubfeedNeutralOvercurrent.setStatus("current")
_LgpCondId5247SubfeedGroundOvercurrent_ObjectIdentity = ObjectIdentity
lgpCondId5247SubfeedGroundOvercurrent = _LgpCondId5247SubfeedGroundOvercurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5247)
)
if mibBuilder.loadTexts:
    lgpCondId5247SubfeedGroundOvercurrent.setStatus("current")
_LgpCondId5249EventState_ObjectIdentity = ObjectIdentity
lgpCondId5249EventState = _LgpCondId5249EventState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5249)
)
if mibBuilder.loadTexts:
    lgpCondId5249EventState.setStatus("current")
_LgpCondId5263CompressorNotStopping_ObjectIdentity = ObjectIdentity
lgpCondId5263CompressorNotStopping = _LgpCondId5263CompressorNotStopping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5263)
)
if mibBuilder.loadTexts:
    lgpCondId5263CompressorNotStopping.setStatus("current")
_LgpCondId5269CompressorHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5269CompressorHoursExceeded = _LgpCondId5269CompressorHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5269)
)
if mibBuilder.loadTexts:
    lgpCondId5269CompressorHoursExceeded.setStatus("current")
_LgpCondId5270CompressorHighHeadPressure_ObjectIdentity = ObjectIdentity
lgpCondId5270CompressorHighHeadPressure = _LgpCondId5270CompressorHighHeadPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5270)
)
if mibBuilder.loadTexts:
    lgpCondId5270CompressorHighHeadPressure.setStatus("current")
_LgpCondId5271CompressorLowSuctionPressure_ObjectIdentity = ObjectIdentity
lgpCondId5271CompressorLowSuctionPressure = _LgpCondId5271CompressorLowSuctionPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5271)
)
if mibBuilder.loadTexts:
    lgpCondId5271CompressorLowSuctionPressure.setStatus("current")
_LgpCondId5272CompressorThermalOverload_ObjectIdentity = ObjectIdentity
lgpCondId5272CompressorThermalOverload = _LgpCondId5272CompressorThermalOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5272)
)
if mibBuilder.loadTexts:
    lgpCondId5272CompressorThermalOverload.setStatus("current")
_LgpCondId5273CompressorLowOilPressure_ObjectIdentity = ObjectIdentity
lgpCondId5273CompressorLowOilPressure = _LgpCondId5273CompressorLowOilPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5273)
)
if mibBuilder.loadTexts:
    lgpCondId5273CompressorLowOilPressure.setStatus("current")
_LgpCondId5274CompressorHeadPressureOverThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5274CompressorHeadPressureOverThreshold = _LgpCondId5274CompressorHeadPressureOverThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5274)
)
if mibBuilder.loadTexts:
    lgpCondId5274CompressorHeadPressureOverThreshold.setStatus("current")
_LgpCondId5275CompressorLossofDifferentialPressure_ObjectIdentity = ObjectIdentity
lgpCondId5275CompressorLossofDifferentialPressure = _LgpCondId5275CompressorLossofDifferentialPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5275)
)
if mibBuilder.loadTexts:
    lgpCondId5275CompressorLossofDifferentialPressure.setStatus("current")
_LgpCondId5277CondenserFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5277CondenserFanIssue = _LgpCondId5277CondenserFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5277)
)
if mibBuilder.loadTexts:
    lgpCondId5277CondenserFanIssue.setStatus("current")
_LgpCondId5278LowCondenserRefrigerantPressure_ObjectIdentity = ObjectIdentity
lgpCondId5278LowCondenserRefrigerantPressure = _LgpCondId5278LowCondenserRefrigerantPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5278)
)
if mibBuilder.loadTexts:
    lgpCondId5278LowCondenserRefrigerantPressure.setStatus("current")
_LgpCondId5280LowFluidPressure_ObjectIdentity = ObjectIdentity
lgpCondId5280LowFluidPressure = _LgpCondId5280LowFluidPressure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5280)
)
if mibBuilder.loadTexts:
    lgpCondId5280LowFluidPressure.setStatus("current")
_LgpCondId5293ReturnFluidOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5293ReturnFluidOverTemp = _LgpCondId5293ReturnFluidOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5293)
)
if mibBuilder.loadTexts:
    lgpCondId5293ReturnFluidOverTemp.setStatus("current")
_LgpCondId5294ReturnFluidUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId5294ReturnFluidUnderTemp = _LgpCondId5294ReturnFluidUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5294)
)
if mibBuilder.loadTexts:
    lgpCondId5294ReturnFluidUnderTemp.setStatus("current")
_LgpCondId5295ReturnFluidTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5295ReturnFluidTempSensorIssue = _LgpCondId5295ReturnFluidTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5295)
)
if mibBuilder.loadTexts:
    lgpCondId5295ReturnFluidTempSensorIssue.setStatus("current")
_LgpCondId5296TeamworkReturnFluidTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5296TeamworkReturnFluidTempSensorIssue = _LgpCondId5296TeamworkReturnFluidTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5296)
)
if mibBuilder.loadTexts:
    lgpCondId5296TeamworkReturnFluidTempSensorIssue.setStatus("current")
_LgpCondId5297AllPumpsLossofFlow_ObjectIdentity = ObjectIdentity
lgpCondId5297AllPumpsLossofFlow = _LgpCondId5297AllPumpsLossofFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5297)
)
if mibBuilder.loadTexts:
    lgpCondId5297AllPumpsLossofFlow.setStatus("current")
_LgpCondId5300PumpHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5300PumpHoursExceeded = _LgpCondId5300PumpHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5300)
)
if mibBuilder.loadTexts:
    lgpCondId5300PumpHoursExceeded.setStatus("current")
_LgpCondId5306FreeCoolingValveHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5306FreeCoolingValveHoursExceeded = _LgpCondId5306FreeCoolingValveHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5306)
)
if mibBuilder.loadTexts:
    lgpCondId5306FreeCoolingValveHoursExceeded.setStatus("current")
_LgpCondId5308EvaporatorInletTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5308EvaporatorInletTempSensorIssue = _LgpCondId5308EvaporatorInletTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5308)
)
if mibBuilder.loadTexts:
    lgpCondId5308EvaporatorInletTempSensorIssue.setStatus("current")
_LgpCondId5309TeamworkEvaporatorInletTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5309TeamworkEvaporatorInletTempSensorIssue = _LgpCondId5309TeamworkEvaporatorInletTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5309)
)
if mibBuilder.loadTexts:
    lgpCondId5309TeamworkEvaporatorInletTempSensorIssue.setStatus("current")
_LgpCondId5310EvaporatorFluidFreezeAutoReset_ObjectIdentity = ObjectIdentity
lgpCondId5310EvaporatorFluidFreezeAutoReset = _LgpCondId5310EvaporatorFluidFreezeAutoReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5310)
)
if mibBuilder.loadTexts:
    lgpCondId5310EvaporatorFluidFreezeAutoReset.setStatus("current")
_LgpCondId5311EvaporatorFluidFreezeManualResetRequired_ObjectIdentity = ObjectIdentity
lgpCondId5311EvaporatorFluidFreezeManualResetRequired = _LgpCondId5311EvaporatorFluidFreezeManualResetRequired_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5311)
)
if mibBuilder.loadTexts:
    lgpCondId5311EvaporatorFluidFreezeManualResetRequired.setStatus("current")
_LgpCondId5315SubgroupEventOccurredDuringCommunicationLoss_ObjectIdentity = ObjectIdentity
lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss = _LgpCondId5315SubgroupEventOccurredDuringCommunicationLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5315)
)
if mibBuilder.loadTexts:
    lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss.setStatus("current")
_LgpCondId5335ReturnAirUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5335ReturnAirUnderTemperature = _LgpCondId5335ReturnAirUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5335)
)
if mibBuilder.loadTexts:
    lgpCondId5335ReturnAirUnderTemperature.setStatus("current")
_LgpCondId5349ExtAirSensorAHighHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5349ExtAirSensorAHighHumidity = _LgpCondId5349ExtAirSensorAHighHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5349)
)
if mibBuilder.loadTexts:
    lgpCondId5349ExtAirSensorAHighHumidity.setStatus("current")
_LgpCondId5351ExtAirSensorALowHumidity_ObjectIdentity = ObjectIdentity
lgpCondId5351ExtAirSensorALowHumidity = _LgpCondId5351ExtAirSensorALowHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5351)
)
if mibBuilder.loadTexts:
    lgpCondId5351ExtAirSensorALowHumidity.setStatus("current")
_LgpCondId5352CompressorShortCycle_ObjectIdentity = ObjectIdentity
lgpCondId5352CompressorShortCycle = _LgpCondId5352CompressorShortCycle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5352)
)
if mibBuilder.loadTexts:
    lgpCondId5352CompressorShortCycle.setStatus("current")
_LgpCondId5354DigScrollCompDischargeTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5354DigScrollCompDischargeTempSensorIssue = _LgpCondId5354DigScrollCompDischargeTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5354)
)
if mibBuilder.loadTexts:
    lgpCondId5354DigScrollCompDischargeTempSensorIssue.setStatus("current")
_LgpCondId5355DigScrollCompOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5355DigScrollCompOverTemp = _LgpCondId5355DigScrollCompOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5355)
)
if mibBuilder.loadTexts:
    lgpCondId5355DigScrollCompOverTemp.setStatus("current")
_LgpCondId5361ExtFreeCoolingLockout_ObjectIdentity = ObjectIdentity
lgpCondId5361ExtFreeCoolingLockout = _LgpCondId5361ExtFreeCoolingLockout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5361)
)
if mibBuilder.loadTexts:
    lgpCondId5361ExtFreeCoolingLockout.setStatus("current")
_LgpCondId5362FreeCoolingTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5362FreeCoolingTempSensorIssue = _LgpCondId5362FreeCoolingTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5362)
)
if mibBuilder.loadTexts:
    lgpCondId5362FreeCoolingTempSensorIssue.setStatus("current")
_LgpCondId5365HotWaterHotGasValveHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5365HotWaterHotGasValveHoursExceeded = _LgpCondId5365HotWaterHotGasValveHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5365)
)
if mibBuilder.loadTexts:
    lgpCondId5365HotWaterHotGasValveHoursExceeded.setStatus("current")
_LgpCondId5368ElectricReheaterHoursExceeded_ObjectIdentity = ObjectIdentity
lgpCondId5368ElectricReheaterHoursExceeded = _LgpCondId5368ElectricReheaterHoursExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5368)
)
if mibBuilder.loadTexts:
    lgpCondId5368ElectricReheaterHoursExceeded.setStatus("current")
_LgpCondId5376MainFanOverload_ObjectIdentity = ObjectIdentity
lgpCondId5376MainFanOverload = _LgpCondId5376MainFanOverload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5376)
)
if mibBuilder.loadTexts:
    lgpCondId5376MainFanOverload.setStatus("current")
_LgpCondId5377Condenser_ObjectIdentity = ObjectIdentity
lgpCondId5377Condenser = _LgpCondId5377Condenser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5377)
)
if mibBuilder.loadTexts:
    lgpCondId5377Condenser.setStatus("current")
_LgpCondId5415ExtLossofAirBlower_ObjectIdentity = ObjectIdentity
lgpCondId5415ExtLossofAirBlower = _LgpCondId5415ExtLossofAirBlower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5415)
)
if mibBuilder.loadTexts:
    lgpCondId5415ExtLossofAirBlower.setStatus("current")
_LgpCondId5416ExtStandbyUnitOn_ObjectIdentity = ObjectIdentity
lgpCondId5416ExtStandbyUnitOn = _LgpCondId5416ExtStandbyUnitOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5416)
)
if mibBuilder.loadTexts:
    lgpCondId5416ExtStandbyUnitOn.setStatus("current")
_LgpCondId5417DigitalOutputBoardNotDetected_ObjectIdentity = ObjectIdentity
lgpCondId5417DigitalOutputBoardNotDetected = _LgpCondId5417DigitalOutputBoardNotDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5417)
)
if mibBuilder.loadTexts:
    lgpCondId5417DigitalOutputBoardNotDetected.setStatus("current")
_LgpCondId5418UnitCodeMissing_ObjectIdentity = ObjectIdentity
lgpCondId5418UnitCodeMissing = _LgpCondId5418UnitCodeMissing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5418)
)
if mibBuilder.loadTexts:
    lgpCondId5418UnitCodeMissing.setStatus("current")
_LgpCondId5419UnitCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5419UnitCommunicationLost = _LgpCondId5419UnitCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5419)
)
if mibBuilder.loadTexts:
    lgpCondId5419UnitCommunicationLost.setStatus("current")
_LgpCondId5422OvertemperaturePowerOff_ObjectIdentity = ObjectIdentity
lgpCondId5422OvertemperaturePowerOff = _LgpCondId5422OvertemperaturePowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5422)
)
if mibBuilder.loadTexts:
    lgpCondId5422OvertemperaturePowerOff.setStatus("current")
_LgpCondId5423TooManySensors_ObjectIdentity = ObjectIdentity
lgpCondId5423TooManySensors = _LgpCondId5423TooManySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5423)
)
if mibBuilder.loadTexts:
    lgpCondId5423TooManySensors.setStatus("current")
_LgpCondId5432TransformerOvertemperaturePowerOff_ObjectIdentity = ObjectIdentity
lgpCondId5432TransformerOvertemperaturePowerOff = _LgpCondId5432TransformerOvertemperaturePowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5432)
)
if mibBuilder.loadTexts:
    lgpCondId5432TransformerOvertemperaturePowerOff.setStatus("current")
_LgpCondId5433TransformerOvertemperature_ObjectIdentity = ObjectIdentity
lgpCondId5433TransformerOvertemperature = _LgpCondId5433TransformerOvertemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5433)
)
if mibBuilder.loadTexts:
    lgpCondId5433TransformerOvertemperature.setStatus("current")
_LgpCondId5434TransformerTemperatureSensorFail_ObjectIdentity = ObjectIdentity
lgpCondId5434TransformerTemperatureSensorFail = _LgpCondId5434TransformerTemperatureSensorFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5434)
)
if mibBuilder.loadTexts:
    lgpCondId5434TransformerTemperatureSensorFail.setStatus("current")
_LgpCondId5436LowAmbientTemperatureProbeTwo_ObjectIdentity = ObjectIdentity
lgpCondId5436LowAmbientTemperatureProbeTwo = _LgpCondId5436LowAmbientTemperatureProbeTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5436)
)
if mibBuilder.loadTexts:
    lgpCondId5436LowAmbientTemperatureProbeTwo.setStatus("current")
_LgpCondId5437HighAmbientTemperatureProbeTwo_ObjectIdentity = ObjectIdentity
lgpCondId5437HighAmbientTemperatureProbeTwo = _LgpCondId5437HighAmbientTemperatureProbeTwo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5437)
)
if mibBuilder.loadTexts:
    lgpCondId5437HighAmbientTemperatureProbeTwo.setStatus("current")
_LgpCondId5438ThermalRunawayDetected_ObjectIdentity = ObjectIdentity
lgpCondId5438ThermalRunawayDetected = _LgpCondId5438ThermalRunawayDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5438)
)
if mibBuilder.loadTexts:
    lgpCondId5438ThermalRunawayDetected.setStatus("current")
_LgpCondId5439BatteryStringEqualize_ObjectIdentity = ObjectIdentity
lgpCondId5439BatteryStringEqualize = _LgpCondId5439BatteryStringEqualize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5439)
)
if mibBuilder.loadTexts:
    lgpCondId5439BatteryStringEqualize.setStatus("current")
_LgpCondId5440BatteryStringOffline_ObjectIdentity = ObjectIdentity
lgpCondId5440BatteryStringOffline = _LgpCondId5440BatteryStringOffline_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5440)
)
if mibBuilder.loadTexts:
    lgpCondId5440BatteryStringOffline.setStatus("current")
_LgpCondId5442DischargeLowCellVoltage_ObjectIdentity = ObjectIdentity
lgpCondId5442DischargeLowCellVoltage = _LgpCondId5442DischargeLowCellVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5442)
)
if mibBuilder.loadTexts:
    lgpCondId5442DischargeLowCellVoltage.setStatus("current")
_LgpCondId5447MMSPowerSharing_ObjectIdentity = ObjectIdentity
lgpCondId5447MMSPowerSharing = _LgpCondId5447MMSPowerSharing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5447)
)
if mibBuilder.loadTexts:
    lgpCondId5447MMSPowerSharing.setStatus("current")
_LgpCondId5453ModuleInStandbyIntelligentParalleling_ObjectIdentity = ObjectIdentity
lgpCondId5453ModuleInStandbyIntelligentParalleling = _LgpCondId5453ModuleInStandbyIntelligentParalleling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5453)
)
if mibBuilder.loadTexts:
    lgpCondId5453ModuleInStandbyIntelligentParalleling.setStatus("current")
_LgpCondId5456ECOModeActive_ObjectIdentity = ObjectIdentity
lgpCondId5456ECOModeActive = _LgpCondId5456ECOModeActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5456)
)
if mibBuilder.loadTexts:
    lgpCondId5456ECOModeActive.setStatus("current")
_LgpCondId5457ECOModeSuspended_ObjectIdentity = ObjectIdentity
lgpCondId5457ECOModeSuspended = _LgpCondId5457ECOModeSuspended_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5457)
)
if mibBuilder.loadTexts:
    lgpCondId5457ECOModeSuspended.setStatus("current")
_LgpCondId5458ExcessECOSuspends_ObjectIdentity = ObjectIdentity
lgpCondId5458ExcessECOSuspends = _LgpCondId5458ExcessECOSuspends_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5458)
)
if mibBuilder.loadTexts:
    lgpCondId5458ExcessECOSuspends.setStatus("current")
_LgpCondId5471DoorOpen_ObjectIdentity = ObjectIdentity
lgpCondId5471DoorOpen = _LgpCondId5471DoorOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5471)
)
if mibBuilder.loadTexts:
    lgpCondId5471DoorOpen.setStatus("current")
_LgpCondId5472DoorSensorDisconnected_ObjectIdentity = ObjectIdentity
lgpCondId5472DoorSensorDisconnected = _LgpCondId5472DoorSensorDisconnected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5472)
)
if mibBuilder.loadTexts:
    lgpCondId5472DoorSensorDisconnected.setStatus("current")
_LgpCondId5479ContactClosureOpen_ObjectIdentity = ObjectIdentity
lgpCondId5479ContactClosureOpen = _LgpCondId5479ContactClosureOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5479)
)
if mibBuilder.loadTexts:
    lgpCondId5479ContactClosureOpen.setStatus("current")
_LgpCondId5480ContactClosureClosed_ObjectIdentity = ObjectIdentity
lgpCondId5480ContactClosureClosed = _LgpCondId5480ContactClosureClosed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5480)
)
if mibBuilder.loadTexts:
    lgpCondId5480ContactClosureClosed.setStatus("current")
_LgpCondId5492ExtSystemCondensationDetected_ObjectIdentity = ObjectIdentity
lgpCondId5492ExtSystemCondensationDetected = _LgpCondId5492ExtSystemCondensationDetected_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5492)
)
if mibBuilder.loadTexts:
    lgpCondId5492ExtSystemCondensationDetected.setStatus("current")
_LgpCondId5495ExtFanIssue_ObjectIdentity = ObjectIdentity
lgpCondId5495ExtFanIssue = _LgpCondId5495ExtFanIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5495)
)
if mibBuilder.loadTexts:
    lgpCondId5495ExtFanIssue.setStatus("current")
_LgpCondId5500ExtRemoteShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5500ExtRemoteShutdown = _LgpCondId5500ExtRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5500)
)
if mibBuilder.loadTexts:
    lgpCondId5500ExtRemoteShutdown.setStatus("current")
_LgpCondId5505HotAisleTempOutofRange_ObjectIdentity = ObjectIdentity
lgpCondId5505HotAisleTempOutofRange = _LgpCondId5505HotAisleTempOutofRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5505)
)
if mibBuilder.loadTexts:
    lgpCondId5505HotAisleTempOutofRange.setStatus("current")
_LgpCondId5508ColdAisleTempOutofRange_ObjectIdentity = ObjectIdentity
lgpCondId5508ColdAisleTempOutofRange = _LgpCondId5508ColdAisleTempOutofRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5508)
)
if mibBuilder.loadTexts:
    lgpCondId5508ColdAisleTempOutofRange.setStatus("current")
_LgpCondId5512RemoteShutdown_ObjectIdentity = ObjectIdentity
lgpCondId5512RemoteShutdown = _LgpCondId5512RemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5512)
)
if mibBuilder.loadTexts:
    lgpCondId5512RemoteShutdown.setStatus("current")
_LgpCondId5513CompressorCapacityReduced_ObjectIdentity = ObjectIdentity
lgpCondId5513CompressorCapacityReduced = _LgpCondId5513CompressorCapacityReduced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5513)
)
if mibBuilder.loadTexts:
    lgpCondId5513CompressorCapacityReduced.setStatus("current")
_LgpCondId5514CompressorLowPressureTransducerIssue_ObjectIdentity = ObjectIdentity
lgpCondId5514CompressorLowPressureTransducerIssue = _LgpCondId5514CompressorLowPressureTransducerIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5514)
)
if mibBuilder.loadTexts:
    lgpCondId5514CompressorLowPressureTransducerIssue.setStatus("current")
_LgpCondId5524PDUNeutralOverCurrent_ObjectIdentity = ObjectIdentity
lgpCondId5524PDUNeutralOverCurrent = _LgpCondId5524PDUNeutralOverCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5524)
)
if mibBuilder.loadTexts:
    lgpCondId5524PDUNeutralOverCurrent.setStatus("current")
_LgpCondId5531CondenserCommunicationLost_ObjectIdentity = ObjectIdentity
lgpCondId5531CondenserCommunicationLost = _LgpCondId5531CondenserCommunicationLost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5531)
)
if mibBuilder.loadTexts:
    lgpCondId5531CondenserCommunicationLost.setStatus("current")
_LgpCondId5535CondenserOutsideAirTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5535CondenserOutsideAirTempSensorIssue = _LgpCondId5535CondenserOutsideAirTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5535)
)
if mibBuilder.loadTexts:
    lgpCondId5535CondenserOutsideAirTempSensorIssue.setStatus("current")
_LgpCondId5536CondenserOutsideAirTempOutofOperatingRange_ObjectIdentity = ObjectIdentity
lgpCondId5536CondenserOutsideAirTempOutofOperatingRange = _LgpCondId5536CondenserOutsideAirTempOutofOperatingRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5536)
)
if mibBuilder.loadTexts:
    lgpCondId5536CondenserOutsideAirTempOutofOperatingRange.setStatus("current")
_LgpCondId5537CondenserControlBoardIssue_ObjectIdentity = ObjectIdentity
lgpCondId5537CondenserControlBoardIssue = _LgpCondId5537CondenserControlBoardIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5537)
)
if mibBuilder.loadTexts:
    lgpCondId5537CondenserControlBoardIssue.setStatus("current")
_LgpCondId5539CondenserRefrigerantPressureOverThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5539CondenserRefrigerantPressureOverThreshold = _LgpCondId5539CondenserRefrigerantPressureOverThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5539)
)
if mibBuilder.loadTexts:
    lgpCondId5539CondenserRefrigerantPressureOverThreshold.setStatus("current")
_LgpCondId5540CondenserRefrigerantPressureUnderThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5540CondenserRefrigerantPressureUnderThreshold = _LgpCondId5540CondenserRefrigerantPressureUnderThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5540)
)
if mibBuilder.loadTexts:
    lgpCondId5540CondenserRefrigerantPressureUnderThreshold.setStatus("current")
_LgpCondId5541CondenserRefrigerantPressureSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5541CondenserRefrigerantPressureSensorIssue = _LgpCondId5541CondenserRefrigerantPressureSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5541)
)
if mibBuilder.loadTexts:
    lgpCondId5541CondenserRefrigerantPressureSensorIssue.setStatus("current")
_LgpCondId5542CondenserSupplyRefrigerantOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5542CondenserSupplyRefrigerantOverTemp = _LgpCondId5542CondenserSupplyRefrigerantOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5542)
)
if mibBuilder.loadTexts:
    lgpCondId5542CondenserSupplyRefrigerantOverTemp.setStatus("current")
_LgpCondId5543CondenserSupplyRefrigerantUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId5543CondenserSupplyRefrigerantUnderTemp = _LgpCondId5543CondenserSupplyRefrigerantUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5543)
)
if mibBuilder.loadTexts:
    lgpCondId5543CondenserSupplyRefrigerantUnderTemp.setStatus("current")
_LgpCondId5544CondenserSupplyRefrigerantTempSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue = _LgpCondId5544CondenserSupplyRefrigerantTempSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5544)
)
if mibBuilder.loadTexts:
    lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue.setStatus("current")
_LgpCondId5545CondenserMaxFanSpeedOverride_ObjectIdentity = ObjectIdentity
lgpCondId5545CondenserMaxFanSpeedOverride = _LgpCondId5545CondenserMaxFanSpeedOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5545)
)
if mibBuilder.loadTexts:
    lgpCondId5545CondenserMaxFanSpeedOverride.setStatus("current")
_LgpCondId5559EvaporatorReturnFluidOverTemp_ObjectIdentity = ObjectIdentity
lgpCondId5559EvaporatorReturnFluidOverTemp = _LgpCondId5559EvaporatorReturnFluidOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5559)
)
if mibBuilder.loadTexts:
    lgpCondId5559EvaporatorReturnFluidOverTemp.setStatus("current")
_LgpCondId5560EvaporatorReturnFluidUnderTemp_ObjectIdentity = ObjectIdentity
lgpCondId5560EvaporatorReturnFluidUnderTemp = _LgpCondId5560EvaporatorReturnFluidUnderTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5560)
)
if mibBuilder.loadTexts:
    lgpCondId5560EvaporatorReturnFluidUnderTemp.setStatus("current")
_LgpCondId5561LBSActiveMaster_ObjectIdentity = ObjectIdentity
lgpCondId5561LBSActiveMaster = _LgpCondId5561LBSActiveMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5561)
)
if mibBuilder.loadTexts:
    lgpCondId5561LBSActiveMaster.setStatus("current")
_LgpCondId5562LBSActiveSlave_ObjectIdentity = ObjectIdentity
lgpCondId5562LBSActiveSlave = _LgpCondId5562LBSActiveSlave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5562)
)
if mibBuilder.loadTexts:
    lgpCondId5562LBSActiveSlave.setStatus("current")
_LgpCondId5563DCBusLowFault_ObjectIdentity = ObjectIdentity
lgpCondId5563DCBusLowFault = _LgpCondId5563DCBusLowFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5563)
)
if mibBuilder.loadTexts:
    lgpCondId5563DCBusLowFault.setStatus("current")
_LgpCondId5564FanContactorOpen_ObjectIdentity = ObjectIdentity
lgpCondId5564FanContactorOpen = _LgpCondId5564FanContactorOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5564)
)
if mibBuilder.loadTexts:
    lgpCondId5564FanContactorOpen.setStatus("current")
_LgpCondId5565FanContactorOpenFail_ObjectIdentity = ObjectIdentity
lgpCondId5565FanContactorOpenFail = _LgpCondId5565FanContactorOpenFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5565)
)
if mibBuilder.loadTexts:
    lgpCondId5565FanContactorOpenFail.setStatus("current")
_LgpCondId5566FanContactorCloseFail_ObjectIdentity = ObjectIdentity
lgpCondId5566FanContactorCloseFail = _LgpCondId5566FanContactorCloseFail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5566)
)
if mibBuilder.loadTexts:
    lgpCondId5566FanContactorCloseFail.setStatus("current")
_LgpCondId5567IPInhibit_ObjectIdentity = ObjectIdentity
lgpCondId5567IPInhibit = _LgpCondId5567IPInhibit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5567)
)
if mibBuilder.loadTexts:
    lgpCondId5567IPInhibit.setStatus("current")
_LgpCondId5568InputUndervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5568InputUndervoltage = _LgpCondId5568InputUndervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5568)
)
if mibBuilder.loadTexts:
    lgpCondId5568InputUndervoltage.setStatus("current")
_LgpCondId5569InputOvervoltage_ObjectIdentity = ObjectIdentity
lgpCondId5569InputOvervoltage = _LgpCondId5569InputOvervoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5569)
)
if mibBuilder.loadTexts:
    lgpCondId5569InputOvervoltage.setStatus("current")
_LgpCondId5573AmbientAirSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5573AmbientAirSensorIssue = _LgpCondId5573AmbientAirSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5573)
)
if mibBuilder.loadTexts:
    lgpCondId5573AmbientAirSensorIssue.setStatus("current")
_LgpCondId5577ExtDewPointUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5577ExtDewPointUnderTemperature = _LgpCondId5577ExtDewPointUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5577)
)
if mibBuilder.loadTexts:
    lgpCondId5577ExtDewPointUnderTemperature.setStatus("current")
_LgpCondId5578DewPointOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5578DewPointOverTemperature = _LgpCondId5578DewPointOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5578)
)
if mibBuilder.loadTexts:
    lgpCondId5578DewPointOverTemperature.setStatus("current")
_LgpCondId5579DewPointUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5579DewPointUnderTemperature = _LgpCondId5579DewPointUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5579)
)
if mibBuilder.loadTexts:
    lgpCondId5579DewPointUnderTemperature.setStatus("current")
_LgpCondId5588UnspecifiedGeneralEvent_ObjectIdentity = ObjectIdentity
lgpCondId5588UnspecifiedGeneralEvent = _LgpCondId5588UnspecifiedGeneralEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5588)
)
if mibBuilder.loadTexts:
    lgpCondId5588UnspecifiedGeneralEvent.setStatus("current")
_LgpCondId5593RemoteSensorAverageOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5593RemoteSensorAverageOverTemperature = _LgpCondId5593RemoteSensorAverageOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5593)
)
if mibBuilder.loadTexts:
    lgpCondId5593RemoteSensorAverageOverTemperature.setStatus("current")
_LgpCondId5594RemoteSensorAverageUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5594RemoteSensorAverageUnderTemperature = _LgpCondId5594RemoteSensorAverageUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5594)
)
if mibBuilder.loadTexts:
    lgpCondId5594RemoteSensorAverageUnderTemperature.setStatus("current")
_LgpCondId5595RemoteSensorSystemAverageOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5595RemoteSensorSystemAverageOverTemperature = _LgpCondId5595RemoteSensorSystemAverageOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5595)
)
if mibBuilder.loadTexts:
    lgpCondId5595RemoteSensorSystemAverageOverTemperature.setStatus("current")
_LgpCondId5596RemoteSensorSystemAverageUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5596RemoteSensorSystemAverageUnderTemperature = _LgpCondId5596RemoteSensorSystemAverageUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5596)
)
if mibBuilder.loadTexts:
    lgpCondId5596RemoteSensorSystemAverageUnderTemperature.setStatus("current")
_LgpCondId5597RemoteSensorOverTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5597RemoteSensorOverTemperature = _LgpCondId5597RemoteSensorOverTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5597)
)
if mibBuilder.loadTexts:
    lgpCondId5597RemoteSensorOverTemperature.setStatus("current")
_LgpCondId5598RemoteSensorUnderTemperature_ObjectIdentity = ObjectIdentity
lgpCondId5598RemoteSensorUnderTemperature = _LgpCondId5598RemoteSensorUnderTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5598)
)
if mibBuilder.loadTexts:
    lgpCondId5598RemoteSensorUnderTemperature.setStatus("current")
_LgpCondId5600AirEconomizerEmergencyOverride_ObjectIdentity = ObjectIdentity
lgpCondId5600AirEconomizerEmergencyOverride = _LgpCondId5600AirEconomizerEmergencyOverride_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5600)
)
if mibBuilder.loadTexts:
    lgpCondId5600AirEconomizerEmergencyOverride.setStatus("current")
_LgpCondId5601AirEconomizerReducedAirflow_ObjectIdentity = ObjectIdentity
lgpCondId5601AirEconomizerReducedAirflow = _LgpCondId5601AirEconomizerReducedAirflow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5601)
)
if mibBuilder.loadTexts:
    lgpCondId5601AirEconomizerReducedAirflow.setStatus("current")
_LgpCondId5604CompressorSuperheatOverThreshold_ObjectIdentity = ObjectIdentity
lgpCondId5604CompressorSuperheatOverThreshold = _LgpCondId5604CompressorSuperheatOverThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5604)
)
if mibBuilder.loadTexts:
    lgpCondId5604CompressorSuperheatOverThreshold.setStatus("current")
_LgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent_ObjectIdentity = ObjectIdentity
lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent = _LgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5609)
)
if mibBuilder.loadTexts:
    lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent.setStatus("current")
_LgpCondId5610ThermalRunawayCelltoCellTemperatureEvent_ObjectIdentity = ObjectIdentity
lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent = _LgpCondId5610ThermalRunawayCelltoCellTemperatureEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5610)
)
if mibBuilder.loadTexts:
    lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent.setStatus("current")
_LgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent_ObjectIdentity = ObjectIdentity
lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent = _LgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5611)
)
if mibBuilder.loadTexts:
    lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent.setStatus("current")
_LgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent_ObjectIdentity = ObjectIdentity
lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent = _LgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5612)
)
if mibBuilder.loadTexts:
    lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent.setStatus("current")
_LgpCondId5617TemperatureControlSensorIssue_ObjectIdentity = ObjectIdentity
lgpCondId5617TemperatureControlSensorIssue = _LgpCondId5617TemperatureControlSensorIssue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 2, 7, 1, 5617)
)
if mibBuilder.loadTexts:
    lgpCondId5617TemperatureControlSensorIssue.setStatus("current")
_LgpNotifications_ObjectIdentity = ObjectIdentity
lgpNotifications = _LgpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3)
)
if mibBuilder.loadTexts:
    lgpNotifications.setStatus("current")
_LgpEventNotifications_ObjectIdentity = ObjectIdentity
lgpEventNotifications = _LgpEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0)
)
if mibBuilder.loadTexts:
    lgpEventNotifications.setStatus("current")
_LgpEventParameters_ObjectIdentity = ObjectIdentity
lgpEventParameters = _LgpEventParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10)
)
if mibBuilder.loadTexts:
    lgpEventParameters.setStatus("current")
_LgpEventParmTableRef_Type = ObjectIdentifier
_LgpEventParmTableRef_Object = MibScalar
lgpEventParmTableRef = _LgpEventParmTableRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 5),
    _LgpEventParmTableRef_Type()
)
lgpEventParmTableRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEventParmTableRef.setStatus("current")
_LgpEventParmTableRowRef_Type = ObjectIdentifier
_LgpEventParmTableRowRef_Object = MibScalar
lgpEventParmTableRowRef = _LgpEventParmTableRowRef_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 6),
    _LgpEventParmTableRowRef_Type()
)
lgpEventParmTableRowRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEventParmTableRowRef.setStatus("current")
_LgpEnvironmental_ObjectIdentity = ObjectIdentity
lgpEnvironmental = _LgpEnvironmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4)
)
if mibBuilder.loadTexts:
    lgpEnvironmental.setStatus("current")
_LgpEnvTemperature_ObjectIdentity = ObjectIdentity
lgpEnvTemperature = _LgpEnvTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1)
)
if mibBuilder.loadTexts:
    lgpEnvTemperature.setStatus("current")
_LgpEnvTemperatureWellKnown_ObjectIdentity = ObjectIdentity
lgpEnvTemperatureWellKnown = _LgpEnvTemperatureWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureWellKnown.setStatus("current")
_LgpEnvControlTemperature_ObjectIdentity = ObjectIdentity
lgpEnvControlTemperature = _LgpEnvControlTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvControlTemperature.setStatus("current")
_LgpEnvReturnAirTemperature_ObjectIdentity = ObjectIdentity
lgpEnvReturnAirTemperature = _LgpEnvReturnAirTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvReturnAirTemperature.setStatus("current")
_LgpEnvSupplyAirTemperature_ObjectIdentity = ObjectIdentity
lgpEnvSupplyAirTemperature = _LgpEnvSupplyAirTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyAirTemperature.setStatus("current")
_LgpAmbientTemperature_ObjectIdentity = ObjectIdentity
lgpAmbientTemperature = _LgpAmbientTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    lgpAmbientTemperature.setStatus("current")
_LgpInverterTemperature_ObjectIdentity = ObjectIdentity
lgpInverterTemperature = _LgpInverterTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    lgpInverterTemperature.setStatus("current")
_LgpBatteryTempterature_ObjectIdentity = ObjectIdentity
lgpBatteryTempterature = _LgpBatteryTempterature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lgpBatteryTempterature.setStatus("current")
_LgpAcDcConverterTemperature_ObjectIdentity = ObjectIdentity
lgpAcDcConverterTemperature = _LgpAcDcConverterTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    lgpAcDcConverterTemperature.setStatus("current")
_LgpPfcTemperature_ObjectIdentity = ObjectIdentity
lgpPfcTemperature = _LgpPfcTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    lgpPfcTemperature.setStatus("current")
_LgpTransformerTemperature_ObjectIdentity = ObjectIdentity
lgpTransformerTemperature = _LgpTransformerTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    lgpTransformerTemperature.setStatus("current")
_LgpLocalTemperature_ObjectIdentity = ObjectIdentity
lgpLocalTemperature = _LgpLocalTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    lgpLocalTemperature.setStatus("current")
_LgpLocal1Temperature_ObjectIdentity = ObjectIdentity
lgpLocal1Temperature = _LgpLocal1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    lgpLocal1Temperature.setStatus("current")
_LgpLocal2Temperature_ObjectIdentity = ObjectIdentity
lgpLocal2Temperature = _LgpLocal2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    lgpLocal2Temperature.setStatus("current")
_LgpLocal3Temperature_ObjectIdentity = ObjectIdentity
lgpLocal3Temperature = _LgpLocal3Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    lgpLocal3Temperature.setStatus("current")
_LgpDigitalScrollCompressorTemperature_ObjectIdentity = ObjectIdentity
lgpDigitalScrollCompressorTemperature = _LgpDigitalScrollCompressorTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    lgpDigitalScrollCompressorTemperature.setStatus("current")
_LgpDigitalScrollCompressor1Temperature_ObjectIdentity = ObjectIdentity
lgpDigitalScrollCompressor1Temperature = _LgpDigitalScrollCompressor1Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    lgpDigitalScrollCompressor1Temperature.setStatus("current")
_LgpDigitalScrollCompressor2Temperature_ObjectIdentity = ObjectIdentity
lgpDigitalScrollCompressor2Temperature = _LgpDigitalScrollCompressor2Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    lgpDigitalScrollCompressor2Temperature.setStatus("current")
_LgpChillWaterTemperature_ObjectIdentity = ObjectIdentity
lgpChillWaterTemperature = _LgpChillWaterTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    lgpChillWaterTemperature.setStatus("current")
_LgpCoolantTemperature_ObjectIdentity = ObjectIdentity
lgpCoolantTemperature = _LgpCoolantTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    lgpCoolantTemperature.setStatus("current")
_LgpEnvEnclosureTemperatureSensors_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensors = _LgpEnvEnclosureTemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensors.setStatus("current")
_LgpEnvEnclosureTemperatureSensor1_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor1 = _LgpEnvEnclosureTemperatureSensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor1.setStatus("current")
_LgpEnvEnclosureTemperatureSensor2_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor2 = _LgpEnvEnclosureTemperatureSensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 2)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor2.setStatus("current")
_LgpEnvEnclosureTemperatureSensor3_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor3 = _LgpEnvEnclosureTemperatureSensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 3)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor3.setStatus("current")
_LgpEnvEnclosureTemperatureSensor4_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperatureSensor4 = _LgpEnvEnclosureTemperatureSensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 14, 4)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperatureSensor4.setStatus("current")
_LgpEnvValueAmbientRoomTemperature_ObjectIdentity = ObjectIdentity
lgpEnvValueAmbientRoomTemperature = _LgpEnvValueAmbientRoomTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    lgpEnvValueAmbientRoomTemperature.setStatus("current")
_LgpEnvDewPointTemperature_ObjectIdentity = ObjectIdentity
lgpEnvDewPointTemperature = _LgpEnvDewPointTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    lgpEnvDewPointTemperature.setStatus("current")
_LgpEnvEnclosureTemperature_ObjectIdentity = ObjectIdentity
lgpEnvEnclosureTemperature = _LgpEnvEnclosureTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    lgpEnvEnclosureTemperature.setStatus("current")
_LgpEnvAdjustedTemperature_ObjectIdentity = ObjectIdentity
lgpEnvAdjustedTemperature = _LgpEnvAdjustedTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    lgpEnvAdjustedTemperature.setStatus("current")
_LgpEnvExternalSensors_ObjectIdentity = ObjectIdentity
lgpEnvExternalSensors = _LgpEnvExternalSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19)
)
if mibBuilder.loadTexts:
    lgpEnvExternalSensors.setStatus("current")
_LgpEnvExternalAirSensorA_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorA = _LgpEnvExternalAirSensorA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorA.setStatus("current")
_LgpEnvExternalAirSensorADewPoint_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorADewPoint = _LgpEnvExternalAirSensorADewPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 2)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorADewPoint.setStatus("current")
_LgpEnvExternalAirSensorB_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorB = _LgpEnvExternalAirSensorB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 3)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorB.setStatus("current")
_LgpEnvExternalAirSensorBDewPoint_ObjectIdentity = ObjectIdentity
lgpEnvExternalAirSensorBDewPoint = _LgpEnvExternalAirSensorBDewPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 19, 4)
)
if mibBuilder.loadTexts:
    lgpEnvExternalAirSensorBDewPoint.setStatus("current")
_LgpEnvSupplyFluidTemperature_ObjectIdentity = ObjectIdentity
lgpEnvSupplyFluidTemperature = _LgpEnvSupplyFluidTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 20)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyFluidTemperature.setStatus("current")
_LgpEnvSupplyRefrigerantTemperature_ObjectIdentity = ObjectIdentity
lgpEnvSupplyRefrigerantTemperature = _LgpEnvSupplyRefrigerantTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 21)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyRefrigerantTemperature.setStatus("current")
_LgpEnvMinDesiredRoomAirTemperature_ObjectIdentity = ObjectIdentity
lgpEnvMinDesiredRoomAirTemperature = _LgpEnvMinDesiredRoomAirTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 22)
)
if mibBuilder.loadTexts:
    lgpEnvMinDesiredRoomAirTemperature.setStatus("current")
_LgpEnvDewPointTemperatures_ObjectIdentity = ObjectIdentity
lgpEnvDewPointTemperatures = _LgpEnvDewPointTemperatures_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 23)
)
if mibBuilder.loadTexts:
    lgpEnvDewPointTemperatures.setStatus("current")
_LgpEnvInletDewPointTemperature_ObjectIdentity = ObjectIdentity
lgpEnvInletDewPointTemperature = _LgpEnvInletDewPointTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 1, 23, 1)
)
if mibBuilder.loadTexts:
    lgpEnvInletDewPointTemperature.setStatus("current")
_LgpEnvTemperatureFahrenheit_ObjectIdentity = ObjectIdentity
lgpEnvTemperatureFahrenheit = _LgpEnvTemperatureFahrenheit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureFahrenheit.setStatus("current")
_LgpEnvTemperatureSettingDegF_Type = Integer32
_LgpEnvTemperatureSettingDegF_Object = MibScalar
lgpEnvTemperatureSettingDegF = _LgpEnvTemperatureSettingDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 1),
    _LgpEnvTemperatureSettingDegF_Type()
)
lgpEnvTemperatureSettingDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureToleranceDegF_Type = Integer32
_LgpEnvTemperatureToleranceDegF_Object = MibScalar
lgpEnvTemperatureToleranceDegF = _LgpEnvTemperatureToleranceDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 2),
    _LgpEnvTemperatureToleranceDegF_Type()
)
lgpEnvTemperatureToleranceDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegF.setUnits("0.1 degrees Fahrenheit")
_LgpEnvTemperatureTableDegF_Object = MibTable
lgpEnvTemperatureTableDegF = _LgpEnvTemperatureTableDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureTableDegF.setStatus("current")
_LgpEnvTemperatureEntryDegF_Object = MibTableRow
lgpEnvTemperatureEntryDegF = _LgpEnvTemperatureEntryDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1)
)
lgpEnvTemperatureEntryDegF.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvTemperatureIdDegF"),
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureEntryDegF.setStatus("current")
_LgpEnvTemperatureIdDegF_Type = Unsigned32
_LgpEnvTemperatureIdDegF_Object = MibTableColumn
lgpEnvTemperatureIdDegF = _LgpEnvTemperatureIdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 1),
    _LgpEnvTemperatureIdDegF_Type()
)
lgpEnvTemperatureIdDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureIdDegF.setStatus("current")
_LgpEnvTemperatureDescrDegF_Type = ObjectIdentifier
_LgpEnvTemperatureDescrDegF_Object = MibTableColumn
lgpEnvTemperatureDescrDegF = _LgpEnvTemperatureDescrDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 2),
    _LgpEnvTemperatureDescrDegF_Type()
)
lgpEnvTemperatureDescrDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDescrDegF.setStatus("current")
_LgpEnvTemperatureMeasurementDegF_Type = Integer32
_LgpEnvTemperatureMeasurementDegF_Object = MibTableColumn
lgpEnvTemperatureMeasurementDegF = _LgpEnvTemperatureMeasurementDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 3),
    _LgpEnvTemperatureMeasurementDegF_Type()
)
lgpEnvTemperatureMeasurementDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureHighThresholdDegF_Type = Integer32
_LgpEnvTemperatureHighThresholdDegF_Object = MibTableColumn
lgpEnvTemperatureHighThresholdDegF = _LgpEnvTemperatureHighThresholdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 4),
    _LgpEnvTemperatureHighThresholdDegF_Type()
)
lgpEnvTemperatureHighThresholdDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureLowThresholdDegF_Type = Integer32
_LgpEnvTemperatureLowThresholdDegF_Object = MibTableColumn
lgpEnvTemperatureLowThresholdDegF = _LgpEnvTemperatureLowThresholdDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 5),
    _LgpEnvTemperatureLowThresholdDegF_Type()
)
lgpEnvTemperatureLowThresholdDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureSetPointDegF_Type = Integer32
_LgpEnvTemperatureSetPointDegF_Object = MibTableColumn
lgpEnvTemperatureSetPointDegF = _LgpEnvTemperatureSetPointDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 6),
    _LgpEnvTemperatureSetPointDegF_Type()
)
lgpEnvTemperatureSetPointDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureDailyHighDegF_Type = Integer32
_LgpEnvTemperatureDailyHighDegF_Object = MibTableColumn
lgpEnvTemperatureDailyHighDegF = _LgpEnvTemperatureDailyHighDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 7),
    _LgpEnvTemperatureDailyHighDegF_Type()
)
lgpEnvTemperatureDailyHighDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegF.setUnits("degrees Fahrenheit")
_LgpEnvTemperatureDailyLowDegF_Type = Integer32
_LgpEnvTemperatureDailyLowDegF_Object = MibTableColumn
lgpEnvTemperatureDailyLowDegF = _LgpEnvTemperatureDailyLowDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 8),
    _LgpEnvTemperatureDailyLowDegF_Type()
)
lgpEnvTemperatureDailyLowDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegF.setUnits("degrees Fahrenheit")


class _LgpEnvTempDailyHighTimeHourDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeHourDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyHighTimeHourDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeHourDegF_Object = MibTableColumn
lgpEnvTempDailyHighTimeHourDegF = _LgpEnvTempDailyHighTimeHourDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 9),
    _LgpEnvTempDailyHighTimeHourDegF_Type()
)
lgpEnvTempDailyHighTimeHourDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegF.setUnits("hours")


class _LgpEnvTempDailyHighTimeMinuteDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeMinuteDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeMinuteDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeMinuteDegF_Object = MibTableColumn
lgpEnvTempDailyHighTimeMinuteDegF = _LgpEnvTempDailyHighTimeMinuteDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 10),
    _LgpEnvTempDailyHighTimeMinuteDegF_Type()
)
lgpEnvTempDailyHighTimeMinuteDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegF.setUnits("minutes")


class _LgpEnvTempDailyHighTimeSecondDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeSecondDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeSecondDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeSecondDegF_Object = MibTableColumn
lgpEnvTempDailyHighTimeSecondDegF = _LgpEnvTempDailyHighTimeSecondDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 11),
    _LgpEnvTempDailyHighTimeSecondDegF_Type()
)
lgpEnvTempDailyHighTimeSecondDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegF.setUnits("seconds")


class _LgpEnvTempDailyLowTimeHourDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeHourDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyLowTimeHourDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeHourDegF_Object = MibTableColumn
lgpEnvTempDailyLowTimeHourDegF = _LgpEnvTempDailyLowTimeHourDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 12),
    _LgpEnvTempDailyLowTimeHourDegF_Type()
)
lgpEnvTempDailyLowTimeHourDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegF.setUnits("hours")


class _LgpEnvTempDailyLowTimeMinuteDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeMinuteDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeMinuteDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeMinuteDegF_Object = MibTableColumn
lgpEnvTempDailyLowTimeMinuteDegF = _LgpEnvTempDailyLowTimeMinuteDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 13),
    _LgpEnvTempDailyLowTimeMinuteDegF_Type()
)
lgpEnvTempDailyLowTimeMinuteDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegF.setUnits("minutes")


class _LgpEnvTempDailyLowTimeSecondDegF_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeSecondDegF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeSecondDegF_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeSecondDegF_Object = MibTableColumn
lgpEnvTempDailyLowTimeSecondDegF = _LgpEnvTempDailyLowTimeSecondDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 14),
    _LgpEnvTempDailyLowTimeSecondDegF_Type()
)
lgpEnvTempDailyLowTimeSecondDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegF.setUnits("seconds")
_LgpEnvTemperatureMeasurementTenthsDegF_Type = Integer32
_LgpEnvTemperatureMeasurementTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureMeasurementTenthsDegF = _LgpEnvTemperatureMeasurementTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 50),
    _LgpEnvTemperatureMeasurementTenthsDegF_Type()
)
lgpEnvTemperatureMeasurementTenthsDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureHighThresholdTenthsDegF_Type = Integer32
_LgpEnvTemperatureHighThresholdTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureHighThresholdTenthsDegF = _LgpEnvTemperatureHighThresholdTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 51),
    _LgpEnvTemperatureHighThresholdTenthsDegF_Type()
)
lgpEnvTemperatureHighThresholdTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureLowThresholdTenthsDegF_Type = Integer32
_LgpEnvTemperatureLowThresholdTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureLowThresholdTenthsDegF = _LgpEnvTemperatureLowThresholdTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 52),
    _LgpEnvTemperatureLowThresholdTenthsDegF_Type()
)
lgpEnvTemperatureLowThresholdTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureSetPointTenthsDegF_Type = Integer32
_LgpEnvTemperatureSetPointTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureSetPointTenthsDegF = _LgpEnvTemperatureSetPointTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 53),
    _LgpEnvTemperatureSetPointTenthsDegF_Type()
)
lgpEnvTemperatureSetPointTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureDeadBandTenthsDegF_Type = Integer32
_LgpEnvTemperatureDeadBandTenthsDegF_Object = MibTableColumn
lgpEnvTemperatureDeadBandTenthsDegF = _LgpEnvTemperatureDeadBandTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 60),
    _LgpEnvTemperatureDeadBandTenthsDegF_Type()
)
lgpEnvTemperatureDeadBandTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTempHeatingPropBandTenthsDegF_Type = Integer32
_LgpEnvTempHeatingPropBandTenthsDegF_Object = MibTableColumn
lgpEnvTempHeatingPropBandTenthsDegF = _LgpEnvTempHeatingPropBandTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 61),
    _LgpEnvTempHeatingPropBandTenthsDegF_Type()
)
lgpEnvTempHeatingPropBandTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTempCoolingPropBandTenthsDegF_Type = Integer32
_LgpEnvTempCoolingPropBandTenthsDegF_Object = MibTableColumn
lgpEnvTempCoolingPropBandTenthsDegF = _LgpEnvTempCoolingPropBandTenthsDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 3, 1, 62),
    _LgpEnvTempCoolingPropBandTenthsDegF_Type()
)
lgpEnvTempCoolingPropBandTenthsDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureDeadbandRangeDegF_Type = Integer32
_LgpEnvTemperatureDeadbandRangeDegF_Object = MibScalar
lgpEnvTemperatureDeadbandRangeDegF = _LgpEnvTemperatureDeadbandRangeDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 2, 4),
    _LgpEnvTemperatureDeadbandRangeDegF_Type()
)
lgpEnvTemperatureDeadbandRangeDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvTemperatureCelsius_ObjectIdentity = ObjectIdentity
lgpEnvTemperatureCelsius = _LgpEnvTemperatureCelsius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureCelsius.setStatus("current")
_LgpEnvTemperatureSettingDegC_Type = Integer32
_LgpEnvTemperatureSettingDegC_Object = MibScalar
lgpEnvTemperatureSettingDegC = _LgpEnvTemperatureSettingDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 1),
    _LgpEnvTemperatureSettingDegC_Type()
)
lgpEnvTemperatureSettingDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSettingDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureToleranceDegC_Type = Integer32
_LgpEnvTemperatureToleranceDegC_Object = MibScalar
lgpEnvTemperatureToleranceDegC = _LgpEnvTemperatureToleranceDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 2),
    _LgpEnvTemperatureToleranceDegC_Type()
)
lgpEnvTemperatureToleranceDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureToleranceDegC.setUnits("0.1 degrees Celsius")
_LgpEnvTemperatureTableDegC_Object = MibTable
lgpEnvTemperatureTableDegC = _LgpEnvTemperatureTableDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureTableDegC.setStatus("current")
_LgpEnvTemperatureEntryDegC_Object = MibTableRow
lgpEnvTemperatureEntryDegC = _LgpEnvTemperatureEntryDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1)
)
lgpEnvTemperatureEntryDegC.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvTemperatureIdDegC"),
)
if mibBuilder.loadTexts:
    lgpEnvTemperatureEntryDegC.setStatus("current")
_LgpEnvTemperatureIdDegC_Type = Unsigned32
_LgpEnvTemperatureIdDegC_Object = MibTableColumn
lgpEnvTemperatureIdDegC = _LgpEnvTemperatureIdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 1),
    _LgpEnvTemperatureIdDegC_Type()
)
lgpEnvTemperatureIdDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureIdDegC.setStatus("current")
_LgpEnvTemperatureDescrDegC_Type = ObjectIdentifier
_LgpEnvTemperatureDescrDegC_Object = MibTableColumn
lgpEnvTemperatureDescrDegC = _LgpEnvTemperatureDescrDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 2),
    _LgpEnvTemperatureDescrDegC_Type()
)
lgpEnvTemperatureDescrDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDescrDegC.setStatus("current")
_LgpEnvTemperatureMeasurementDegC_Type = Integer32
_LgpEnvTemperatureMeasurementDegC_Object = MibTableColumn
lgpEnvTemperatureMeasurementDegC = _LgpEnvTemperatureMeasurementDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 3),
    _LgpEnvTemperatureMeasurementDegC_Type()
)
lgpEnvTemperatureMeasurementDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureHighThresholdDegC_Type = Integer32
_LgpEnvTemperatureHighThresholdDegC_Object = MibTableColumn
lgpEnvTemperatureHighThresholdDegC = _LgpEnvTemperatureHighThresholdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 4),
    _LgpEnvTemperatureHighThresholdDegC_Type()
)
lgpEnvTemperatureHighThresholdDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureLowThresholdDegC_Type = Integer32
_LgpEnvTemperatureLowThresholdDegC_Object = MibTableColumn
lgpEnvTemperatureLowThresholdDegC = _LgpEnvTemperatureLowThresholdDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 5),
    _LgpEnvTemperatureLowThresholdDegC_Type()
)
lgpEnvTemperatureLowThresholdDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureSetPointDegC_Type = Integer32
_LgpEnvTemperatureSetPointDegC_Object = MibTableColumn
lgpEnvTemperatureSetPointDegC = _LgpEnvTemperatureSetPointDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 6),
    _LgpEnvTemperatureSetPointDegC_Type()
)
lgpEnvTemperatureSetPointDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureDailyHighDegC_Type = Integer32
_LgpEnvTemperatureDailyHighDegC_Object = MibTableColumn
lgpEnvTemperatureDailyHighDegC = _LgpEnvTemperatureDailyHighDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 7),
    _LgpEnvTemperatureDailyHighDegC_Type()
)
lgpEnvTemperatureDailyHighDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyHighDegC.setUnits("degrees Celsius")
_LgpEnvTemperatureDailyLowDegC_Type = Integer32
_LgpEnvTemperatureDailyLowDegC_Object = MibTableColumn
lgpEnvTemperatureDailyLowDegC = _LgpEnvTemperatureDailyLowDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 8),
    _LgpEnvTemperatureDailyLowDegC_Type()
)
lgpEnvTemperatureDailyLowDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDailyLowDegC.setUnits("degrees Celsius")


class _LgpEnvTempDailyHighTimeHourDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeHourDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyHighTimeHourDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeHourDegC_Object = MibTableColumn
lgpEnvTempDailyHighTimeHourDegC = _LgpEnvTempDailyHighTimeHourDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 9),
    _LgpEnvTempDailyHighTimeHourDegC_Type()
)
lgpEnvTempDailyHighTimeHourDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeHourDegC.setUnits("hours")


class _LgpEnvTempDailyHighTimeMinuteDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeMinuteDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeMinuteDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeMinuteDegC_Object = MibTableColumn
lgpEnvTempDailyHighTimeMinuteDegC = _LgpEnvTempDailyHighTimeMinuteDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 10),
    _LgpEnvTempDailyHighTimeMinuteDegC_Type()
)
lgpEnvTempDailyHighTimeMinuteDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeMinuteDegC.setUnits("minutes")


class _LgpEnvTempDailyHighTimeSecondDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyHighTimeSecondDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyHighTimeSecondDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyHighTimeSecondDegC_Object = MibTableColumn
lgpEnvTempDailyHighTimeSecondDegC = _LgpEnvTempDailyHighTimeSecondDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 11),
    _LgpEnvTempDailyHighTimeSecondDegC_Type()
)
lgpEnvTempDailyHighTimeSecondDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyHighTimeSecondDegC.setUnits("seconds")


class _LgpEnvTempDailyLowTimeHourDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeHourDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvTempDailyLowTimeHourDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeHourDegC_Object = MibTableColumn
lgpEnvTempDailyLowTimeHourDegC = _LgpEnvTempDailyLowTimeHourDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 12),
    _LgpEnvTempDailyLowTimeHourDegC_Type()
)
lgpEnvTempDailyLowTimeHourDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeHourDegC.setUnits("hours")


class _LgpEnvTempDailyLowTimeMinuteDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeMinuteDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeMinuteDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeMinuteDegC_Object = MibTableColumn
lgpEnvTempDailyLowTimeMinuteDegC = _LgpEnvTempDailyLowTimeMinuteDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 13),
    _LgpEnvTempDailyLowTimeMinuteDegC_Type()
)
lgpEnvTempDailyLowTimeMinuteDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeMinuteDegC.setUnits("minutes")


class _LgpEnvTempDailyLowTimeSecondDegC_Type(Integer32):
    """Custom type lgpEnvTempDailyLowTimeSecondDegC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvTempDailyLowTimeSecondDegC_Type.__name__ = "Integer32"
_LgpEnvTempDailyLowTimeSecondDegC_Object = MibTableColumn
lgpEnvTempDailyLowTimeSecondDegC = _LgpEnvTempDailyLowTimeSecondDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 14),
    _LgpEnvTempDailyLowTimeSecondDegC_Type()
)
lgpEnvTempDailyLowTimeSecondDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempDailyLowTimeSecondDegC.setUnits("seconds")
_LgpEnvTemperatureMeasurementTenthsDegC_Type = Integer32
_LgpEnvTemperatureMeasurementTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureMeasurementTenthsDegC = _LgpEnvTemperatureMeasurementTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 50),
    _LgpEnvTemperatureMeasurementTenthsDegC_Type()
)
lgpEnvTemperatureMeasurementTenthsDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureMeasurementTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureHighThresholdTenthsDegC_Type = Integer32
_LgpEnvTemperatureHighThresholdTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureHighThresholdTenthsDegC = _LgpEnvTemperatureHighThresholdTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 51),
    _LgpEnvTemperatureHighThresholdTenthsDegC_Type()
)
lgpEnvTemperatureHighThresholdTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureHighThresholdTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureLowThresholdTenthsDegC_Type = Integer32
_LgpEnvTemperatureLowThresholdTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureLowThresholdTenthsDegC = _LgpEnvTemperatureLowThresholdTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 52),
    _LgpEnvTemperatureLowThresholdTenthsDegC_Type()
)
lgpEnvTemperatureLowThresholdTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureLowThresholdTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureSetPointTenthsDegC_Type = Integer32
_LgpEnvTemperatureSetPointTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureSetPointTenthsDegC = _LgpEnvTemperatureSetPointTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 53),
    _LgpEnvTemperatureSetPointTenthsDegC_Type()
)
lgpEnvTemperatureSetPointTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureSetPointTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureDeadBandTenthsDegC_Type = Integer32
_LgpEnvTemperatureDeadBandTenthsDegC_Object = MibTableColumn
lgpEnvTemperatureDeadBandTenthsDegC = _LgpEnvTemperatureDeadBandTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 60),
    _LgpEnvTemperatureDeadBandTenthsDegC_Type()
)
lgpEnvTemperatureDeadBandTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadBandTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTempHeatingPropBandTenthsDegC_Type = Integer32
_LgpEnvTempHeatingPropBandTenthsDegC_Object = MibTableColumn
lgpEnvTempHeatingPropBandTenthsDegC = _LgpEnvTempHeatingPropBandTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 61),
    _LgpEnvTempHeatingPropBandTenthsDegC_Type()
)
lgpEnvTempHeatingPropBandTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempHeatingPropBandTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTempCoolingPropBandTenthsDegC_Type = Integer32
_LgpEnvTempCoolingPropBandTenthsDegC_Object = MibTableColumn
lgpEnvTempCoolingPropBandTenthsDegC = _LgpEnvTempCoolingPropBandTenthsDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 3, 1, 62),
    _LgpEnvTempCoolingPropBandTenthsDegC_Type()
)
lgpEnvTempCoolingPropBandTenthsDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTempCoolingPropBandTenthsDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureDeadbandRangeDegC_Type = Integer32
_LgpEnvTemperatureDeadbandRangeDegC_Object = MibScalar
lgpEnvTemperatureDeadbandRangeDegC = _LgpEnvTemperatureDeadbandRangeDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 3, 4),
    _LgpEnvTemperatureDeadbandRangeDegC_Type()
)
lgpEnvTemperatureDeadbandRangeDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvTemperatureDeadbandRangeDegC.setUnits(".1 degrees Celsius")
_LgpEnvTemperatureControlMode_Type = ObjectIdentifier
_LgpEnvTemperatureControlMode_Object = MibScalar
lgpEnvTemperatureControlMode = _LgpEnvTemperatureControlMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 1, 4),
    _LgpEnvTemperatureControlMode_Type()
)
lgpEnvTemperatureControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvTemperatureControlMode.setStatus("current")
_LgpEnvHumidity_ObjectIdentity = ObjectIdentity
lgpEnvHumidity = _LgpEnvHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2)
)
if mibBuilder.loadTexts:
    lgpEnvHumidity.setStatus("current")
_LgpEnvHumidityWellKnown_ObjectIdentity = ObjectIdentity
lgpEnvHumidityWellKnown = _LgpEnvHumidityWellKnown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lgpEnvHumidityWellKnown.setStatus("current")
_LgpEnvControlHumidity_ObjectIdentity = ObjectIdentity
lgpEnvControlHumidity = _LgpEnvControlHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvControlHumidity.setStatus("current")
_LgpEnvReturnAirHumidity_ObjectIdentity = ObjectIdentity
lgpEnvReturnAirHumidity = _LgpEnvReturnAirHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvReturnAirHumidity.setStatus("current")
_LgpEnvSupplyAirHumidity_ObjectIdentity = ObjectIdentity
lgpEnvSupplyAirHumidity = _LgpEnvSupplyAirHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvSupplyAirHumidity.setStatus("current")
_LgpEnvValueAmbientHumidity_ObjectIdentity = ObjectIdentity
lgpEnvValueAmbientHumidity = _LgpEnvValueAmbientHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgpEnvValueAmbientHumidity.setStatus("current")
_LgpEnvHumidityRelative_ObjectIdentity = ObjectIdentity
lgpEnvHumidityRelative = _LgpEnvHumidityRelative_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lgpEnvHumidityRelative.setStatus("current")
_LgpEnvHumiditySettingRel_Type = Integer32
_LgpEnvHumiditySettingRel_Object = MibScalar
lgpEnvHumiditySettingRel = _LgpEnvHumiditySettingRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 1),
    _LgpEnvHumiditySettingRel_Type()
)
lgpEnvHumiditySettingRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumiditySettingRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumiditySettingRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityToleranceRel_Type = Integer32
_LgpEnvHumidityToleranceRel_Object = MibScalar
lgpEnvHumidityToleranceRel = _LgpEnvHumidityToleranceRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 2),
    _LgpEnvHumidityToleranceRel_Type()
)
lgpEnvHumidityToleranceRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityToleranceRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityToleranceRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityTableRel_Object = MibTable
lgpEnvHumidityTableRel = _LgpEnvHumidityTableRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3)
)
if mibBuilder.loadTexts:
    lgpEnvHumidityTableRel.setStatus("current")
_LgpEnvHumidityEntryRel_Object = MibTableRow
lgpEnvHumidityEntryRel = _LgpEnvHumidityEntryRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1)
)
lgpEnvHumidityEntryRel.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvHumidityIdRel"),
)
if mibBuilder.loadTexts:
    lgpEnvHumidityEntryRel.setStatus("current")
_LgpEnvHumidityIdRel_Type = Unsigned32
_LgpEnvHumidityIdRel_Object = MibTableColumn
lgpEnvHumidityIdRel = _LgpEnvHumidityIdRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 1),
    _LgpEnvHumidityIdRel_Type()
)
lgpEnvHumidityIdRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityIdRel.setStatus("current")
_LgpEnvHumidityDescrRel_Type = ObjectIdentifier
_LgpEnvHumidityDescrRel_Object = MibTableColumn
lgpEnvHumidityDescrRel = _LgpEnvHumidityDescrRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 2),
    _LgpEnvHumidityDescrRel_Type()
)
lgpEnvHumidityDescrRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDescrRel.setStatus("current")
_LgpEnvHumidityMeasurementRel_Type = Integer32
_LgpEnvHumidityMeasurementRel_Object = MibTableColumn
lgpEnvHumidityMeasurementRel = _LgpEnvHumidityMeasurementRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 3),
    _LgpEnvHumidityMeasurementRel_Type()
)
lgpEnvHumidityMeasurementRel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityHighThresholdRel_Type = Integer32
_LgpEnvHumidityHighThresholdRel_Object = MibTableColumn
lgpEnvHumidityHighThresholdRel = _LgpEnvHumidityHighThresholdRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 4),
    _LgpEnvHumidityHighThresholdRel_Type()
)
lgpEnvHumidityHighThresholdRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRel.setUnits("percent Relative Humidity")
_LgpEnvHumidityLowThresholdRel_Type = Integer32
_LgpEnvHumidityLowThresholdRel_Object = MibTableColumn
lgpEnvHumidityLowThresholdRel = _LgpEnvHumidityLowThresholdRel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 5),
    _LgpEnvHumidityLowThresholdRel_Type()
)
lgpEnvHumidityLowThresholdRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRel.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRel.setUnits("percent Relative Humidity")
_LgpEnvHumiditySetPoint_Type = Integer32
_LgpEnvHumiditySetPoint_Object = MibTableColumn
lgpEnvHumiditySetPoint = _LgpEnvHumiditySetPoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 6),
    _LgpEnvHumiditySetPoint_Type()
)
lgpEnvHumiditySetPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumiditySetPoint.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumiditySetPoint.setUnits("percent Relative Humidity")
_LgpEnvHumidityDailyHigh_Type = Integer32
_LgpEnvHumidityDailyHigh_Object = MibTableColumn
lgpEnvHumidityDailyHigh = _LgpEnvHumidityDailyHigh_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 7),
    _LgpEnvHumidityDailyHigh_Type()
)
lgpEnvHumidityDailyHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHigh.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHigh.setUnits("percent Relative Humidity")
_LgpEnvHumidityDailyLow_Type = Integer32
_LgpEnvHumidityDailyLow_Object = MibTableColumn
lgpEnvHumidityDailyLow = _LgpEnvHumidityDailyLow_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 8),
    _LgpEnvHumidityDailyLow_Type()
)
lgpEnvHumidityDailyLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLow.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLow.setUnits("percent Relative Humidity")


class _LgpEnvHumidityDailyHighTimeHour_Type(Integer32):
    """Custom type lgpEnvHumidityDailyHighTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvHumidityDailyHighTimeHour_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyHighTimeHour_Object = MibTableColumn
lgpEnvHumidityDailyHighTimeHour = _LgpEnvHumidityDailyHighTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 9),
    _LgpEnvHumidityDailyHighTimeHour_Type()
)
lgpEnvHumidityDailyHighTimeHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeHour.setUnits("hours")


class _LgpEnvHumidityDailyHighTimeMinute_Type(Integer32):
    """Custom type lgpEnvHumidityDailyHighTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyHighTimeMinute_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyHighTimeMinute_Object = MibTableColumn
lgpEnvHumidityDailyHighTimeMinute = _LgpEnvHumidityDailyHighTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 10),
    _LgpEnvHumidityDailyHighTimeMinute_Type()
)
lgpEnvHumidityDailyHighTimeMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeMinute.setUnits("minutes")


class _LgpEnvHumidityDailyHighTimeSecond_Type(Integer32):
    """Custom type lgpEnvHumidityDailyHighTimeSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyHighTimeSecond_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyHighTimeSecond_Object = MibTableColumn
lgpEnvHumidityDailyHighTimeSecond = _LgpEnvHumidityDailyHighTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 11),
    _LgpEnvHumidityDailyHighTimeSecond_Type()
)
lgpEnvHumidityDailyHighTimeSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeSecond.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyHighTimeSecond.setUnits("seconds")


class _LgpEnvHumidityDailyLowTimeHour_Type(Integer32):
    """Custom type lgpEnvHumidityDailyLowTimeHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvHumidityDailyLowTimeHour_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyLowTimeHour_Object = MibTableColumn
lgpEnvHumidityDailyLowTimeHour = _LgpEnvHumidityDailyLowTimeHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 12),
    _LgpEnvHumidityDailyLowTimeHour_Type()
)
lgpEnvHumidityDailyLowTimeHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeHour.setUnits("hours")


class _LgpEnvHumidityDailyLowTimeMinute_Type(Integer32):
    """Custom type lgpEnvHumidityDailyLowTimeMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyLowTimeMinute_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyLowTimeMinute_Object = MibTableColumn
lgpEnvHumidityDailyLowTimeMinute = _LgpEnvHumidityDailyLowTimeMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 13),
    _LgpEnvHumidityDailyLowTimeMinute_Type()
)
lgpEnvHumidityDailyLowTimeMinute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeMinute.setUnits("minutes")


class _LgpEnvHumidityDailyLowTimeSecond_Type(Integer32):
    """Custom type lgpEnvHumidityDailyLowTimeSecond based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvHumidityDailyLowTimeSecond_Type.__name__ = "Integer32"
_LgpEnvHumidityDailyLowTimeSecond_Object = MibTableColumn
lgpEnvHumidityDailyLowTimeSecond = _LgpEnvHumidityDailyLowTimeSecond_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 14),
    _LgpEnvHumidityDailyLowTimeSecond_Type()
)
lgpEnvHumidityDailyLowTimeSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeSecond.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDailyLowTimeSecond.setUnits("seconds")
_LgpEnvHumidityDeadBand_Type = Integer32
_LgpEnvHumidityDeadBand_Object = MibTableColumn
lgpEnvHumidityDeadBand = _LgpEnvHumidityDeadBand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 15),
    _LgpEnvHumidityDeadBand_Type()
)
lgpEnvHumidityDeadBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadBand.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadBand.setUnits("percent Relative Humidity")
_LgpEnvHumidifyPropBand_Type = Integer32
_LgpEnvHumidifyPropBand_Object = MibTableColumn
lgpEnvHumidifyPropBand = _LgpEnvHumidifyPropBand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 16),
    _LgpEnvHumidifyPropBand_Type()
)
lgpEnvHumidifyPropBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidifyPropBand.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidifyPropBand.setUnits("percent Relative Humidity")
_LgpEnvDehumidifyPropBand_Type = Integer32
_LgpEnvDehumidifyPropBand_Object = MibTableColumn
lgpEnvDehumidifyPropBand = _LgpEnvDehumidifyPropBand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 17),
    _LgpEnvDehumidifyPropBand_Type()
)
lgpEnvDehumidifyPropBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvDehumidifyPropBand.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvDehumidifyPropBand.setUnits("percent Relative Humidity")
_LgpEnvHumidityMeasurementRelTenths_Type = Integer32
_LgpEnvHumidityMeasurementRelTenths_Object = MibTableColumn
lgpEnvHumidityMeasurementRelTenths = _LgpEnvHumidityMeasurementRelTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 50),
    _LgpEnvHumidityMeasurementRelTenths_Type()
)
lgpEnvHumidityMeasurementRelTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRelTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityMeasurementRelTenths.setUnits(".1 percent Relative Humidity")
_LgpEnvHumidityHighThresholdRelTenths_Type = Integer32
_LgpEnvHumidityHighThresholdRelTenths_Object = MibTableColumn
lgpEnvHumidityHighThresholdRelTenths = _LgpEnvHumidityHighThresholdRelTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 51),
    _LgpEnvHumidityHighThresholdRelTenths_Type()
)
lgpEnvHumidityHighThresholdRelTenths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRelTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityHighThresholdRelTenths.setUnits(".1 percent Relative Humidity")
_LgpEnvHumidityLowThresholdRelTenths_Type = Integer32
_LgpEnvHumidityLowThresholdRelTenths_Object = MibTableColumn
lgpEnvHumidityLowThresholdRelTenths = _LgpEnvHumidityLowThresholdRelTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 3, 1, 52),
    _LgpEnvHumidityLowThresholdRelTenths_Type()
)
lgpEnvHumidityLowThresholdRelTenths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRelTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityLowThresholdRelTenths.setUnits(".1 percent Relative Humidity")
_LgpEnvHumidityDeadbandRange_Type = Integer32
_LgpEnvHumidityDeadbandRange_Object = MibScalar
lgpEnvHumidityDeadbandRange = _LgpEnvHumidityDeadbandRange_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 2, 2, 4),
    _LgpEnvHumidityDeadbandRange_Type()
)
lgpEnvHumidityDeadbandRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadbandRange.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvHumidityDeadbandRange.setUnits(".1 percent RH")
_LgpEnvState_ObjectIdentity = ObjectIdentity
lgpEnvState = _LgpEnvState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3)
)
if mibBuilder.loadTexts:
    lgpEnvState.setStatus("current")


class _LgpEnvStateSystem_Type(Integer32):
    """Custom type lgpEnvStateSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("standby", 3))
    )


_LgpEnvStateSystem_Type.__name__ = "Integer32"
_LgpEnvStateSystem_Object = MibScalar
lgpEnvStateSystem = _LgpEnvStateSystem_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 1),
    _LgpEnvStateSystem_Type()
)
lgpEnvStateSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateSystem.setStatus("current")


class _LgpEnvStateCooling_Type(Integer32):
    """Custom type lgpEnvStateCooling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateCooling_Type.__name__ = "Integer32"
_LgpEnvStateCooling_Object = MibScalar
lgpEnvStateCooling = _LgpEnvStateCooling_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 2),
    _LgpEnvStateCooling_Type()
)
lgpEnvStateCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCooling.setStatus("current")


class _LgpEnvStateHeating_Type(Integer32):
    """Custom type lgpEnvStateHeating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHeating_Type.__name__ = "Integer32"
_LgpEnvStateHeating_Object = MibScalar
lgpEnvStateHeating = _LgpEnvStateHeating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 3),
    _LgpEnvStateHeating_Type()
)
lgpEnvStateHeating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeating.setStatus("current")


class _LgpEnvStateHumidifying_Type(Integer32):
    """Custom type lgpEnvStateHumidifying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHumidifying_Type.__name__ = "Integer32"
_LgpEnvStateHumidifying_Object = MibScalar
lgpEnvStateHumidifying = _LgpEnvStateHumidifying_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 4),
    _LgpEnvStateHumidifying_Type()
)
lgpEnvStateHumidifying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHumidifying.setStatus("current")


class _LgpEnvStateDehumidifying_Type(Integer32):
    """Custom type lgpEnvStateDehumidifying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateDehumidifying_Type.__name__ = "Integer32"
_LgpEnvStateDehumidifying_Object = MibScalar
lgpEnvStateDehumidifying = _LgpEnvStateDehumidifying_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 5),
    _LgpEnvStateDehumidifying_Type()
)
lgpEnvStateDehumidifying.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateDehumidifying.setStatus("current")


class _LgpEnvStateEconoCycle_Type(Integer32):
    """Custom type lgpEnvStateEconoCycle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateEconoCycle_Type.__name__ = "Integer32"
_LgpEnvStateEconoCycle_Object = MibScalar
lgpEnvStateEconoCycle = _LgpEnvStateEconoCycle_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 6),
    _LgpEnvStateEconoCycle_Type()
)
lgpEnvStateEconoCycle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateEconoCycle.setStatus("current")


class _LgpEnvStateFan_Type(Integer32):
    """Custom type lgpEnvStateFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateFan_Type.__name__ = "Integer32"
_LgpEnvStateFan_Object = MibScalar
lgpEnvStateFan = _LgpEnvStateFan_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 7),
    _LgpEnvStateFan_Type()
)
lgpEnvStateFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFan.setStatus("current")


class _LgpEnvStateGeneralAlarmOutput_Type(Integer32):
    """Custom type lgpEnvStateGeneralAlarmOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateGeneralAlarmOutput_Type.__name__ = "Integer32"
_LgpEnvStateGeneralAlarmOutput_Object = MibScalar
lgpEnvStateGeneralAlarmOutput = _LgpEnvStateGeneralAlarmOutput_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 8),
    _LgpEnvStateGeneralAlarmOutput_Type()
)
lgpEnvStateGeneralAlarmOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateGeneralAlarmOutput.setStatus("current")
_LgpEnvStateCoolingCapacity_Type = Unsigned32
_LgpEnvStateCoolingCapacity_Object = MibScalar
lgpEnvStateCoolingCapacity = _LgpEnvStateCoolingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 9),
    _LgpEnvStateCoolingCapacity_Type()
)
lgpEnvStateCoolingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingCapacity.setUnits("percent")
_LgpEnvStateHeatingCapacity_Type = Unsigned32
_LgpEnvStateHeatingCapacity_Object = MibScalar
lgpEnvStateHeatingCapacity = _LgpEnvStateHeatingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 10),
    _LgpEnvStateHeatingCapacity_Type()
)
lgpEnvStateHeatingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingCapacity.setUnits("percent")


class _LgpEnvStateAudibleAlarm_Type(Integer32):
    """Custom type lgpEnvStateAudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateAudibleAlarm_Type.__name__ = "Integer32"
_LgpEnvStateAudibleAlarm_Object = MibScalar
lgpEnvStateAudibleAlarm = _LgpEnvStateAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 11),
    _LgpEnvStateAudibleAlarm_Type()
)
lgpEnvStateAudibleAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateAudibleAlarm.setStatus("current")
_LgpEnvStateCoolingUnits_ObjectIdentity = ObjectIdentity
lgpEnvStateCoolingUnits = _LgpEnvStateCoolingUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12)
)
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnits.setStatus("current")


class _LgpEnvStateCoolingUnit1_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateCoolingUnit1_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit1_Object = MibScalar
lgpEnvStateCoolingUnit1 = _LgpEnvStateCoolingUnit1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 2),
    _LgpEnvStateCoolingUnit1_Type()
)
lgpEnvStateCoolingUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit1.setStatus("current")


class _LgpEnvStateCoolingUnit2_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateCoolingUnit2_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit2_Object = MibScalar
lgpEnvStateCoolingUnit2 = _LgpEnvStateCoolingUnit2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 3),
    _LgpEnvStateCoolingUnit2_Type()
)
lgpEnvStateCoolingUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit2.setStatus("current")


class _LgpEnvStateCoolingUnit3_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateCoolingUnit3_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit3_Object = MibScalar
lgpEnvStateCoolingUnit3 = _LgpEnvStateCoolingUnit3_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 4),
    _LgpEnvStateCoolingUnit3_Type()
)
lgpEnvStateCoolingUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit3.setStatus("current")


class _LgpEnvStateCoolingUnit4_Type(Integer32):
    """Custom type lgpEnvStateCoolingUnit4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateCoolingUnit4_Type.__name__ = "Integer32"
_LgpEnvStateCoolingUnit4_Object = MibScalar
lgpEnvStateCoolingUnit4 = _LgpEnvStateCoolingUnit4_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 12, 5),
    _LgpEnvStateCoolingUnit4_Type()
)
lgpEnvStateCoolingUnit4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateCoolingUnit4.setStatus("current")
_LgpEnvStateHeatingUnits_ObjectIdentity = ObjectIdentity
lgpEnvStateHeatingUnits = _LgpEnvStateHeatingUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13)
)
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnits.setStatus("current")


class _LgpEnvStateHeatingUnit1_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHeatingUnit1_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit1_Object = MibScalar
lgpEnvStateHeatingUnit1 = _LgpEnvStateHeatingUnit1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 2),
    _LgpEnvStateHeatingUnit1_Type()
)
lgpEnvStateHeatingUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit1.setStatus("current")


class _LgpEnvStateHeatingUnit2_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHeatingUnit2_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit2_Object = MibScalar
lgpEnvStateHeatingUnit2 = _LgpEnvStateHeatingUnit2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 3),
    _LgpEnvStateHeatingUnit2_Type()
)
lgpEnvStateHeatingUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit2.setStatus("current")


class _LgpEnvStateHeatingUnit3_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHeatingUnit3_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit3_Object = MibScalar
lgpEnvStateHeatingUnit3 = _LgpEnvStateHeatingUnit3_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 4),
    _LgpEnvStateHeatingUnit3_Type()
)
lgpEnvStateHeatingUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit3.setStatus("current")


class _LgpEnvStateHeatingUnit4_Type(Integer32):
    """Custom type lgpEnvStateHeatingUnit4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHeatingUnit4_Type.__name__ = "Integer32"
_LgpEnvStateHeatingUnit4_Object = MibScalar
lgpEnvStateHeatingUnit4 = _LgpEnvStateHeatingUnit4_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 13, 5),
    _LgpEnvStateHeatingUnit4_Type()
)
lgpEnvStateHeatingUnit4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHeatingUnit4.setStatus("current")


class _LgpEnvStateOperatingReason_Type(Integer32):
    """Custom type lgpEnvStateOperatingReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("localUser", 2),
          ("alarm", 3),
          ("schedule", 4),
          ("remoteUser", 5),
          ("externalDevice", 6),
          ("localDisplay", 7))
    )


_LgpEnvStateOperatingReason_Type.__name__ = "Integer32"
_LgpEnvStateOperatingReason_Object = MibScalar
lgpEnvStateOperatingReason = _LgpEnvStateOperatingReason_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 14),
    _LgpEnvStateOperatingReason_Type()
)
lgpEnvStateOperatingReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingReason.setStatus("current")


class _LgpEnvStateOperatingMode_Type(Integer32):
    """Custom type lgpEnvStateOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_LgpEnvStateOperatingMode_Type.__name__ = "Integer32"
_LgpEnvStateOperatingMode_Object = MibScalar
lgpEnvStateOperatingMode = _LgpEnvStateOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 15),
    _LgpEnvStateOperatingMode_Type()
)
lgpEnvStateOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingMode.setStatus("current")
_LgpEnvStateFanCapacity_Type = Unsigned32
_LgpEnvStateFanCapacity_Object = MibScalar
lgpEnvStateFanCapacity = _LgpEnvStateFanCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 16),
    _LgpEnvStateFanCapacity_Type()
)
lgpEnvStateFanCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFanCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateFanCapacity.setUnits("percent")
_LgpEnvStateFreeCoolingCapacity_Type = Unsigned32
_LgpEnvStateFreeCoolingCapacity_Object = MibScalar
lgpEnvStateFreeCoolingCapacity = _LgpEnvStateFreeCoolingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 17),
    _LgpEnvStateFreeCoolingCapacity_Type()
)
lgpEnvStateFreeCoolingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFreeCoolingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateFreeCoolingCapacity.setUnits("percent")
_LgpEnvStateDehumidifyingCapacity_Type = Unsigned32
_LgpEnvStateDehumidifyingCapacity_Object = MibScalar
lgpEnvStateDehumidifyingCapacity = _LgpEnvStateDehumidifyingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 18),
    _LgpEnvStateDehumidifyingCapacity_Type()
)
lgpEnvStateDehumidifyingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateDehumidifyingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateDehumidifyingCapacity.setUnits("percent")
_LgpEnvStateHumidifyingCapacity_Type = Unsigned32
_LgpEnvStateHumidifyingCapacity_Object = MibScalar
lgpEnvStateHumidifyingCapacity = _LgpEnvStateHumidifyingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 19),
    _LgpEnvStateHumidifyingCapacity_Type()
)
lgpEnvStateHumidifyingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHumidifyingCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateHumidifyingCapacity.setUnits("percent")


class _LgpEnvStateFreeCooling_Type(Integer32):
    """Custom type lgpEnvStateFreeCooling based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("start", 3),
          ("unavailable", 4))
    )


_LgpEnvStateFreeCooling_Type.__name__ = "Integer32"
_LgpEnvStateFreeCooling_Object = MibScalar
lgpEnvStateFreeCooling = _LgpEnvStateFreeCooling_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 20),
    _LgpEnvStateFreeCooling_Type()
)
lgpEnvStateFreeCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateFreeCooling.setStatus("current")


class _LgpEnvStateElectricHeater_Type(Integer32):
    """Custom type lgpEnvStateElectricHeater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateElectricHeater_Type.__name__ = "Integer32"
_LgpEnvStateElectricHeater_Object = MibScalar
lgpEnvStateElectricHeater = _LgpEnvStateElectricHeater_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 21),
    _LgpEnvStateElectricHeater_Type()
)
lgpEnvStateElectricHeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateElectricHeater.setStatus("current")


class _LgpEnvStateHotWater_Type(Integer32):
    """Custom type lgpEnvStateHotWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpEnvStateHotWater_Type.__name__ = "Integer32"
_LgpEnvStateHotWater_Object = MibScalar
lgpEnvStateHotWater = _LgpEnvStateHotWater_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 22),
    _LgpEnvStateHotWater_Type()
)
lgpEnvStateHotWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateHotWater.setStatus("current")
_LgpEnvStateOperatingEfficiency_Type = Unsigned32
_LgpEnvStateOperatingEfficiency_Object = MibScalar
lgpEnvStateOperatingEfficiency = _LgpEnvStateOperatingEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 23),
    _LgpEnvStateOperatingEfficiency_Type()
)
lgpEnvStateOperatingEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingEfficiency.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStateOperatingEfficiency.setUnits("percent")
_LgpEnvComponentStateTable_Object = MibTable
lgpEnvComponentStateTable = _LgpEnvComponentStateTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50)
)
if mibBuilder.loadTexts:
    lgpEnvComponentStateTable.setStatus("current")
_LgpEnvComponentStateEntry_Object = MibTableRow
lgpEnvComponentStateEntry = _LgpEnvComponentStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1)
)
lgpEnvComponentStateEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvComponentStateIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvComponentStateEntry.setStatus("current")
_LgpEnvComponentStateIndex_Type = Unsigned32
_LgpEnvComponentStateIndex_Object = MibTableColumn
lgpEnvComponentStateIndex = _LgpEnvComponentStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1, 1),
    _LgpEnvComponentStateIndex_Type()
)
lgpEnvComponentStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvComponentStateIndex.setStatus("current")
_LgpEnvComponentStateDescr_Type = ObjectIdentifier
_LgpEnvComponentStateDescr_Object = MibTableColumn
lgpEnvComponentStateDescr = _LgpEnvComponentStateDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1, 2),
    _LgpEnvComponentStateDescr_Type()
)
lgpEnvComponentStateDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvComponentStateDescr.setStatus("current")


class _LgpEnvComponentState_Type(Integer32):
    """Custom type lgpEnvComponentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("on", 1),
          ("off", 2))
    )


_LgpEnvComponentState_Type.__name__ = "Integer32"
_LgpEnvComponentState_Object = MibTableColumn
lgpEnvComponentState = _LgpEnvComponentState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 50, 1, 3),
    _LgpEnvComponentState_Type()
)
lgpEnvComponentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvComponentState.setStatus("current")
_LgpEnvValveTable_Object = MibTable
lgpEnvValveTable = _LgpEnvValveTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70)
)
if mibBuilder.loadTexts:
    lgpEnvValveTable.setStatus("current")
_LgpEnvValveEntry_Object = MibTableRow
lgpEnvValveEntry = _LgpEnvValveEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1)
)
lgpEnvValveEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvValveIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvValveEntry.setStatus("current")
_LgpEnvValveIndex_Type = Unsigned32
_LgpEnvValveIndex_Object = MibTableColumn
lgpEnvValveIndex = _LgpEnvValveIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 1),
    _LgpEnvValveIndex_Type()
)
lgpEnvValveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvValveIndex.setStatus("current")
_LgpEnvValveDescr_Type = ObjectIdentifier
_LgpEnvValveDescr_Object = MibTableColumn
lgpEnvValveDescr = _LgpEnvValveDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 2),
    _LgpEnvValveDescr_Type()
)
lgpEnvValveDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvValveDescr.setStatus("current")


class _LgpEnvValveState_Type(Integer32):
    """Custom type lgpEnvValveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("open", 1),
          ("closed", 2))
    )


_LgpEnvValveState_Type.__name__ = "Integer32"
_LgpEnvValveState_Object = MibTableColumn
lgpEnvValveState = _LgpEnvValveState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 3),
    _LgpEnvValveState_Type()
)
lgpEnvValveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvValveState.setStatus("current")
_LgpEnvValvePositionTenths_Type = Unsigned32
_LgpEnvValvePositionTenths_Object = MibTableColumn
lgpEnvValvePositionTenths = _LgpEnvValvePositionTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 3, 70, 1, 20),
    _LgpEnvValvePositionTenths_Type()
)
lgpEnvValvePositionTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvValvePositionTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvValvePositionTenths.setUnits(".1 percent")
_LgpEnvConfig_ObjectIdentity = ObjectIdentity
lgpEnvConfig = _LgpEnvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4)
)
if mibBuilder.loadTexts:
    lgpEnvConfig.setStatus("current")


class _LgpEnvConfigReheatLockout_Type(Integer32):
    """Custom type lgpEnvConfigReheatLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigReheatLockout_Type.__name__ = "Integer32"
_LgpEnvConfigReheatLockout_Object = MibScalar
lgpEnvConfigReheatLockout = _LgpEnvConfigReheatLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 1),
    _LgpEnvConfigReheatLockout_Type()
)
lgpEnvConfigReheatLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigReheatLockout.setStatus("current")


class _LgpEnvConfigHumLockout_Type(Integer32):
    """Custom type lgpEnvConfigHumLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigHumLockout_Type.__name__ = "Integer32"
_LgpEnvConfigHumLockout_Object = MibScalar
lgpEnvConfigHumLockout = _LgpEnvConfigHumLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 2),
    _LgpEnvConfigHumLockout_Type()
)
lgpEnvConfigHumLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumLockout.setStatus("current")
_LgpEnvConfigRestartDelay_Type = Unsigned32
_LgpEnvConfigRestartDelay_Object = MibScalar
lgpEnvConfigRestartDelay = _LgpEnvConfigRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 4),
    _LgpEnvConfigRestartDelay_Type()
)
lgpEnvConfigRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigRestartDelay.setUnits("seconds")


class _LgpEnvConfigRemoteShutdown_Type(Integer32):
    """Custom type lgpEnvConfigRemoteShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigRemoteShutdown_Type.__name__ = "Integer32"
_LgpEnvConfigRemoteShutdown_Object = MibScalar
lgpEnvConfigRemoteShutdown = _LgpEnvConfigRemoteShutdown_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 7),
    _LgpEnvConfigRemoteShutdown_Type()
)
lgpEnvConfigRemoteShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigRemoteShutdown.setStatus("current")
_LgpEnvConfigCoolingServiceInterval_Type = Unsigned32
_LgpEnvConfigCoolingServiceInterval_Object = MibScalar
lgpEnvConfigCoolingServiceInterval = _LgpEnvConfigCoolingServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 8),
    _LgpEnvConfigCoolingServiceInterval_Type()
)
lgpEnvConfigCoolingServiceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigCoolingServiceInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigCoolingServiceInterval.setUnits("hours")
_LgpEnvConfigHumidifierServiceInterval_Type = Unsigned32
_LgpEnvConfigHumidifierServiceInterval_Object = MibScalar
lgpEnvConfigHumidifierServiceInterval = _LgpEnvConfigHumidifierServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 9),
    _LgpEnvConfigHumidifierServiceInterval_Type()
)
lgpEnvConfigHumidifierServiceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidifierServiceInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidifierServiceInterval.setUnits("hours")
_LgpEnvConfigFilterServiceInterval_Type = Unsigned32
_LgpEnvConfigFilterServiceInterval_Object = MibScalar
lgpEnvConfigFilterServiceInterval = _LgpEnvConfigFilterServiceInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 10),
    _LgpEnvConfigFilterServiceInterval_Type()
)
lgpEnvConfigFilterServiceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFilterServiceInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFilterServiceInterval.setUnits("hours")
_LgpEnvConfigSleepModeDeadbandRangeDegC_Type = Integer32
_LgpEnvConfigSleepModeDeadbandRangeDegC_Object = MibScalar
lgpEnvConfigSleepModeDeadbandRangeDegC = _LgpEnvConfigSleepModeDeadbandRangeDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 11),
    _LgpEnvConfigSleepModeDeadbandRangeDegC_Type()
)
lgpEnvConfigSleepModeDeadbandRangeDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegC.setUnits(".1 degrees Celsius")
_LgpEnvConfigSleepModeDeadbandRangeDegF_Type = Integer32
_LgpEnvConfigSleepModeDeadbandRangeDegF_Object = MibScalar
lgpEnvConfigSleepModeDeadbandRangeDegF = _LgpEnvConfigSleepModeDeadbandRangeDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 12),
    _LgpEnvConfigSleepModeDeadbandRangeDegF_Type()
)
lgpEnvConfigSleepModeDeadbandRangeDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRangeDegF.setUnits(".1 degrees Fahrenheit")
_LgpEnvConfigSupplyTempLowLimitDegF_Type = Integer32
_LgpEnvConfigSupplyTempLowLimitDegF_Object = MibScalar
lgpEnvConfigSupplyTempLowLimitDegF = _LgpEnvConfigSupplyTempLowLimitDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 13),
    _LgpEnvConfigSupplyTempLowLimitDegF_Type()
)
lgpEnvConfigSupplyTempLowLimitDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegF.setUnits("degrees Fahrenheit")
_LgpEnvConfigSupplyTempLowLimitDegC_Type = Integer32
_LgpEnvConfigSupplyTempLowLimitDegC_Object = MibScalar
lgpEnvConfigSupplyTempLowLimitDegC = _LgpEnvConfigSupplyTempLowLimitDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 14),
    _LgpEnvConfigSupplyTempLowLimitDegC_Type()
)
lgpEnvConfigSupplyTempLowLimitDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimitDegC.setUnits("degrees Celsius")
_LgpEnvConfigTemperatureIntegTime_Type = Integer32
_LgpEnvConfigTemperatureIntegTime_Object = MibScalar
lgpEnvConfigTemperatureIntegTime = _LgpEnvConfigTemperatureIntegTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 15),
    _LgpEnvConfigTemperatureIntegTime_Type()
)
lgpEnvConfigTemperatureIntegTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigTemperatureIntegTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigTemperatureIntegTime.setUnits("minutes")


class _LgpEnvConfigLocalTemperatureUnit_Type(Integer32):
    """Custom type lgpEnvConfigLocalTemperatureUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("degC", 1),
          ("degF", 2))
    )


_LgpEnvConfigLocalTemperatureUnit_Type.__name__ = "Integer32"
_LgpEnvConfigLocalTemperatureUnit_Object = MibScalar
lgpEnvConfigLocalTemperatureUnit = _LgpEnvConfigLocalTemperatureUnit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 16),
    _LgpEnvConfigLocalTemperatureUnit_Type()
)
lgpEnvConfigLocalTemperatureUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigLocalTemperatureUnit.setStatus("current")


class _LgpEnvConfigSleepMode_Type(Integer32):
    """Custom type lgpEnvConfigSleepMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("auto", 3))
    )


_LgpEnvConfigSleepMode_Type.__name__ = "Integer32"
_LgpEnvConfigSleepMode_Object = MibScalar
lgpEnvConfigSleepMode = _LgpEnvConfigSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 17),
    _LgpEnvConfigSleepMode_Type()
)
lgpEnvConfigSleepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepMode.setStatus("current")
_LgpEnvConfigHumidityIntegTime_Type = Integer32
_LgpEnvConfigHumidityIntegTime_Object = MibScalar
lgpEnvConfigHumidityIntegTime = _LgpEnvConfigHumidityIntegTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 18),
    _LgpEnvConfigHumidityIntegTime_Type()
)
lgpEnvConfigHumidityIntegTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidityIntegTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidityIntegTime.setUnits("minutes")
_LgpEnvConfigFreecoolingDeltaDegF_Type = Integer32
_LgpEnvConfigFreecoolingDeltaDegF_Object = MibScalar
lgpEnvConfigFreecoolingDeltaDegF = _LgpEnvConfigFreecoolingDeltaDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 19),
    _LgpEnvConfigFreecoolingDeltaDegF_Type()
)
lgpEnvConfigFreecoolingDeltaDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegF.setUnits("degrees Fahrenheit")
_LgpEnvConfigFreecoolingDeltaDegC_Type = Integer32
_LgpEnvConfigFreecoolingDeltaDegC_Object = MibScalar
lgpEnvConfigFreecoolingDeltaDegC = _LgpEnvConfigFreecoolingDeltaDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 20),
    _LgpEnvConfigFreecoolingDeltaDegC_Type()
)
lgpEnvConfigFreecoolingDeltaDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFreecoolingDeltaDegC.setUnits("degrees Celsius")


class _LgpEnvConfigSupplyTempLowLimit_Type(Integer32):
    """Custom type lgpEnvConfigSupplyTempLowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSupplyTempLowLimit_Type.__name__ = "Integer32"
_LgpEnvConfigSupplyTempLowLimit_Object = MibScalar
lgpEnvConfigSupplyTempLowLimit = _LgpEnvConfigSupplyTempLowLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 21),
    _LgpEnvConfigSupplyTempLowLimit_Type()
)
lgpEnvConfigSupplyTempLowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSupplyTempLowLimit.setStatus("current")


class _LgpEnvConfigSensorEventsStandard_Type(Integer32):
    """Custom type lgpEnvConfigSensorEventsStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSensorEventsStandard_Type.__name__ = "Integer32"
_LgpEnvConfigSensorEventsStandard_Object = MibScalar
lgpEnvConfigSensorEventsStandard = _LgpEnvConfigSensorEventsStandard_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 22),
    _LgpEnvConfigSensorEventsStandard_Type()
)
lgpEnvConfigSensorEventsStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSensorEventsStandard.setStatus("current")


class _LgpEnvConfigSensorEvents1_Type(Integer32):
    """Custom type lgpEnvConfigSensorEvents1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSensorEvents1_Type.__name__ = "Integer32"
_LgpEnvConfigSensorEvents1_Object = MibScalar
lgpEnvConfigSensorEvents1 = _LgpEnvConfigSensorEvents1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 23),
    _LgpEnvConfigSensorEvents1_Type()
)
lgpEnvConfigSensorEvents1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSensorEvents1.setStatus("current")


class _LgpEnvConfigSleepModeDeadbandRange_Type(Integer32):
    """Custom type lgpEnvConfigSleepModeDeadbandRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigSleepModeDeadbandRange_Type.__name__ = "Integer32"
_LgpEnvConfigSleepModeDeadbandRange_Object = MibScalar
lgpEnvConfigSleepModeDeadbandRange = _LgpEnvConfigSleepModeDeadbandRange_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 24),
    _LgpEnvConfigSleepModeDeadbandRange_Type()
)
lgpEnvConfigSleepModeDeadbandRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigSleepModeDeadbandRange.setStatus("current")


class _LgpEnvConfigAutoConfiguration_Type(Integer32):
    """Custom type lgpEnvConfigAutoConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigAutoConfiguration_Type.__name__ = "Integer32"
_LgpEnvConfigAutoConfiguration_Object = MibScalar
lgpEnvConfigAutoConfiguration = _LgpEnvConfigAutoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 25),
    _LgpEnvConfigAutoConfiguration_Type()
)
lgpEnvConfigAutoConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigAutoConfiguration.setStatus("current")


class _LgpEnvConfigDeltaGlycolType_Type(Integer32):
    """Custom type lgpEnvConfigDeltaGlycolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("contact", 2),
          ("value", 3))
    )


_LgpEnvConfigDeltaGlycolType_Type.__name__ = "Integer32"
_LgpEnvConfigDeltaGlycolType_Object = MibScalar
lgpEnvConfigDeltaGlycolType = _LgpEnvConfigDeltaGlycolType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 26),
    _LgpEnvConfigDeltaGlycolType_Type()
)
lgpEnvConfigDeltaGlycolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigDeltaGlycolType.setStatus("current")


class _LgpEnvConfigChillWaterControl_Type(Integer32):
    """Custom type lgpEnvConfigChillWaterControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LgpEnvConfigChillWaterControl_Type.__name__ = "Integer32"
_LgpEnvConfigChillWaterControl_Object = MibScalar
lgpEnvConfigChillWaterControl = _LgpEnvConfigChillWaterControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 27),
    _LgpEnvConfigChillWaterControl_Type()
)
lgpEnvConfigChillWaterControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigChillWaterControl.setStatus("current")
_LgpEnvConfigInfaredFlushRate_Type = Unsigned32
_LgpEnvConfigInfaredFlushRate_Object = MibScalar
lgpEnvConfigInfaredFlushRate = _LgpEnvConfigInfaredFlushRate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 28),
    _LgpEnvConfigInfaredFlushRate_Type()
)
lgpEnvConfigInfaredFlushRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigInfaredFlushRate.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigInfaredFlushRate.setUnits("percent")


class _LgpEnvConfigHumidityControl_Type(Integer32):
    """Custom type lgpEnvConfigHumidityControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("relative", 1),
          ("compensated", 2),
          ("predictive", 3))
    )


_LgpEnvConfigHumidityControl_Type.__name__ = "Integer32"
_LgpEnvConfigHumidityControl_Object = MibScalar
lgpEnvConfigHumidityControl = _LgpEnvConfigHumidityControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 29),
    _LgpEnvConfigHumidityControl_Type()
)
lgpEnvConfigHumidityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigHumidityControl.setStatus("current")


class _LgpEnvConfigCompressorLockout_Type(Integer32):
    """Custom type lgpEnvConfigCompressorLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigCompressorLockout_Type.__name__ = "Integer32"
_LgpEnvConfigCompressorLockout_Object = MibScalar
lgpEnvConfigCompressorLockout = _LgpEnvConfigCompressorLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 30),
    _LgpEnvConfigCompressorLockout_Type()
)
lgpEnvConfigCompressorLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigCompressorLockout.setStatus("current")


class _LgpEnvConfigReheatAndHumidifierLockout_Type(Integer32):
    """Custom type lgpEnvConfigReheatAndHumidifierLockout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lockedOut", 1),
          ("notLockedOut", 2))
    )


_LgpEnvConfigReheatAndHumidifierLockout_Type.__name__ = "Integer32"
_LgpEnvConfigReheatAndHumidifierLockout_Object = MibScalar
lgpEnvConfigReheatAndHumidifierLockout = _LgpEnvConfigReheatAndHumidifierLockout_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 31),
    _LgpEnvConfigReheatAndHumidifierLockout_Type()
)
lgpEnvConfigReheatAndHumidifierLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigReheatAndHumidifierLockout.setStatus("current")
_LgpEnvOperationalTimeTable_Object = MibTable
lgpEnvOperationalTimeTable = _LgpEnvOperationalTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32)
)
if mibBuilder.loadTexts:
    lgpEnvOperationalTimeTable.setStatus("current")
_LgpEnvOperationalTimeEntry_Object = MibTableRow
lgpEnvOperationalTimeEntry = _LgpEnvOperationalTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1)
)
lgpEnvOperationalTimeEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvOperationTimeIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvOperationalTimeEntry.setStatus("current")
_LgpEnvOperationTimeIndex_Type = Unsigned32
_LgpEnvOperationTimeIndex_Object = MibTableColumn
lgpEnvOperationTimeIndex = _LgpEnvOperationTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 1),
    _LgpEnvOperationTimeIndex_Type()
)
lgpEnvOperationTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeIndex.setStatus("current")
_LgpEnvOperationTimePoint_Type = ObjectIdentifier
_LgpEnvOperationTimePoint_Object = MibTableColumn
lgpEnvOperationTimePoint = _LgpEnvOperationTimePoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 2),
    _LgpEnvOperationTimePoint_Type()
)
lgpEnvOperationTimePoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvOperationTimePoint.setStatus("current")
_LgpEnvOperationTimeSubID_Type = Integer32
_LgpEnvOperationTimeSubID_Object = MibTableColumn
lgpEnvOperationTimeSubID = _LgpEnvOperationTimeSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 3),
    _LgpEnvOperationTimeSubID_Type()
)
lgpEnvOperationTimeSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeSubID.setStatus("current")
_LgpEnvOperationTimeUnit_Type = ObjectIdentifier
_LgpEnvOperationTimeUnit_Object = MibTableColumn
lgpEnvOperationTimeUnit = _LgpEnvOperationTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 4),
    _LgpEnvOperationTimeUnit_Type()
)
lgpEnvOperationTimeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeUnit.setStatus("current")
_LgpEnvOperationTimeValue_Type = Integer32
_LgpEnvOperationTimeValue_Object = MibTableColumn
lgpEnvOperationTimeValue = _LgpEnvOperationTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 5),
    _LgpEnvOperationTimeValue_Type()
)
lgpEnvOperationTimeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeValue.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeValue.setUnits("hours")
_LgpEnvOperationTimeHighWarning_Type = Integer32
_LgpEnvOperationTimeHighWarning_Object = MibTableColumn
lgpEnvOperationTimeHighWarning = _LgpEnvOperationTimeHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 32, 1, 6),
    _LgpEnvOperationTimeHighWarning_Type()
)
lgpEnvOperationTimeHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeHighWarning.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvOperationTimeHighWarning.setUnits("hours")


class _LgpEnvConfigTempControlAlgorithm_Type(Integer32):
    """Custom type lgpEnvConfigTempControlAlgorithm based on Integer32"""
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
        *(("pi", 1),
          ("pid", 2),
          ("intelligent", 3),
          ("proportional", 4))
    )


_LgpEnvConfigTempControlAlgorithm_Type.__name__ = "Integer32"
_LgpEnvConfigTempControlAlgorithm_Object = MibScalar
lgpEnvConfigTempControlAlgorithm = _LgpEnvConfigTempControlAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 33),
    _LgpEnvConfigTempControlAlgorithm_Type()
)
lgpEnvConfigTempControlAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigTempControlAlgorithm.setStatus("current")


class _LgpEnvConfigFanSpeedMode_Type(Integer32):
    """Custom type lgpEnvConfigFanSpeedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_LgpEnvConfigFanSpeedMode_Type.__name__ = "Integer32"
_LgpEnvConfigFanSpeedMode_Object = MibScalar
lgpEnvConfigFanSpeedMode = _LgpEnvConfigFanSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 34),
    _LgpEnvConfigFanSpeedMode_Type()
)
lgpEnvConfigFanSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedMode.setStatus("current")
_LgpEnvConfigFanSpeedCapacity_Type = Unsigned32
_LgpEnvConfigFanSpeedCapacity_Object = MibScalar
lgpEnvConfigFanSpeedCapacity = _LgpEnvConfigFanSpeedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 35),
    _LgpEnvConfigFanSpeedCapacity_Type()
)
lgpEnvConfigFanSpeedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedCapacity.setUnits("percent")
_LgpEnvConfigBmsResetTimer_Type = Unsigned32
_LgpEnvConfigBmsResetTimer_Object = MibScalar
lgpEnvConfigBmsResetTimer = _LgpEnvConfigBmsResetTimer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 36),
    _LgpEnvConfigBmsResetTimer_Type()
)
lgpEnvConfigBmsResetTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigBmsResetTimer.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigBmsResetTimer.setUnits("minutes")
_LgpEnvConfigDisableSensorOffsetDegC_Type = Integer32
_LgpEnvConfigDisableSensorOffsetDegC_Object = MibScalar
lgpEnvConfigDisableSensorOffsetDegC = _LgpEnvConfigDisableSensorOffsetDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 37),
    _LgpEnvConfigDisableSensorOffsetDegC_Type()
)
lgpEnvConfigDisableSensorOffsetDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegC.setUnits("degrees Celsius")
_LgpEnvConfigDisableSensorOffsetDegF_Type = Integer32
_LgpEnvConfigDisableSensorOffsetDegF_Object = MibScalar
lgpEnvConfigDisableSensorOffsetDegF = _LgpEnvConfigDisableSensorOffsetDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 38),
    _LgpEnvConfigDisableSensorOffsetDegF_Type()
)
lgpEnvConfigDisableSensorOffsetDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigDisableSensorOffsetDegF.setUnits("degrees Fahrenheit")


class _LgpEnvConfigCabinetSensorAlarms_Type(Integer32):
    """Custom type lgpEnvConfigCabinetSensorAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_LgpEnvConfigCabinetSensorAlarms_Type.__name__ = "Integer32"
_LgpEnvConfigCabinetSensorAlarms_Object = MibScalar
lgpEnvConfigCabinetSensorAlarms = _LgpEnvConfigCabinetSensorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 39),
    _LgpEnvConfigCabinetSensorAlarms_Type()
)
lgpEnvConfigCabinetSensorAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigCabinetSensorAlarms.setStatus("current")


class _LgpEnvConfigAirTemperatureControlSensor_Type(Integer32):
    """Custom type lgpEnvConfigAirTemperatureControlSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("supply", 1),
          ("remote", 2),
          ("return", 3))
    )


_LgpEnvConfigAirTemperatureControlSensor_Type.__name__ = "Integer32"
_LgpEnvConfigAirTemperatureControlSensor_Object = MibScalar
lgpEnvConfigAirTemperatureControlSensor = _LgpEnvConfigAirTemperatureControlSensor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 42),
    _LgpEnvConfigAirTemperatureControlSensor_Type()
)
lgpEnvConfigAirTemperatureControlSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigAirTemperatureControlSensor.setStatus("current")


class _LgpEnvConfigFanSpeedControlSensor_Type(Integer32):
    """Custom type lgpEnvConfigFanSpeedControlSensor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("supply", 1),
          ("remote", 2),
          ("return", 3))
    )


_LgpEnvConfigFanSpeedControlSensor_Type.__name__ = "Integer32"
_LgpEnvConfigFanSpeedControlSensor_Object = MibScalar
lgpEnvConfigFanSpeedControlSensor = _LgpEnvConfigFanSpeedControlSensor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 43),
    _LgpEnvConfigFanSpeedControlSensor_Type()
)
lgpEnvConfigFanSpeedControlSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedControlSensor.setStatus("current")
_LgpEnvConfigMinFanSpeed_Type = Unsigned32
_LgpEnvConfigMinFanSpeed_Object = MibScalar
lgpEnvConfigMinFanSpeed = _LgpEnvConfigMinFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 44),
    _LgpEnvConfigMinFanSpeed_Type()
)
lgpEnvConfigMinFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigMinFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigMinFanSpeed.setUnits("percent")
_LgpEnvConfigMaxFanSpeed_Type = Unsigned32
_LgpEnvConfigMaxFanSpeed_Object = MibScalar
lgpEnvConfigMaxFanSpeed = _LgpEnvConfigMaxFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 45),
    _LgpEnvConfigMaxFanSpeed_Type()
)
lgpEnvConfigMaxFanSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigMaxFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigMaxFanSpeed.setUnits("percent")
_LgpEnvConfigFanSpeedPropBandDegC_Type = Integer32
_LgpEnvConfigFanSpeedPropBandDegC_Object = MibScalar
lgpEnvConfigFanSpeedPropBandDegC = _LgpEnvConfigFanSpeedPropBandDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 46),
    _LgpEnvConfigFanSpeedPropBandDegC_Type()
)
lgpEnvConfigFanSpeedPropBandDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegC.setUnits("degrees Celsius")
_LgpEnvConfigFanSpeedPropBandDegF_Type = Integer32
_LgpEnvConfigFanSpeedPropBandDegF_Object = MibScalar
lgpEnvConfigFanSpeedPropBandDegF = _LgpEnvConfigFanSpeedPropBandDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 4, 47),
    _LgpEnvConfigFanSpeedPropBandDegF_Type()
)
lgpEnvConfigFanSpeedPropBandDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvConfigFanSpeedPropBandDegF.setUnits("degrees Fahrenheit")
_LgpEnvControl_ObjectIdentity = ObjectIdentity
lgpEnvControl = _LgpEnvControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5)
)
if mibBuilder.loadTexts:
    lgpEnvControl.setStatus("current")


class _LgpEnvControlShutdownAfterDelay_Type(Integer32):
    """Custom type lgpEnvControlShutdownAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LgpEnvControlShutdownAfterDelay_Type.__name__ = "Integer32"
_LgpEnvControlShutdownAfterDelay_Object = MibScalar
lgpEnvControlShutdownAfterDelay = _LgpEnvControlShutdownAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 1),
    _LgpEnvControlShutdownAfterDelay_Type()
)
lgpEnvControlShutdownAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvControlShutdownAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvControlShutdownAfterDelay.setUnits("seconds")


class _LgpEnvControlStartupAfterDelay_Type(Integer32):
    """Custom type lgpEnvControlStartupAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_LgpEnvControlStartupAfterDelay_Type.__name__ = "Integer32"
_LgpEnvControlStartupAfterDelay_Object = MibScalar
lgpEnvControlStartupAfterDelay = _LgpEnvControlStartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 2),
    _LgpEnvControlStartupAfterDelay_Type()
)
lgpEnvControlStartupAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvControlStartupAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvControlStartupAfterDelay.setUnits("seconds")
_LgpEnvSleepIntervalTimeTable_Object = MibTable
lgpEnvSleepIntervalTimeTable = _LgpEnvSleepIntervalTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3)
)
if mibBuilder.loadTexts:
    lgpEnvSleepIntervalTimeTable.setStatus("current")
_LgpEnvSleepIntervalTimeEntry_Object = MibTableRow
lgpEnvSleepIntervalTimeEntry = _LgpEnvSleepIntervalTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1)
)
lgpEnvSleepIntervalTimeEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvSleepTimeIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvSleepIntervalTimeEntry.setStatus("current")
_LgpEnvSleepTimeIndex_Type = Unsigned32
_LgpEnvSleepTimeIndex_Object = MibTableColumn
lgpEnvSleepTimeIndex = _LgpEnvSleepTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 1),
    _LgpEnvSleepTimeIndex_Type()
)
lgpEnvSleepTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeIndex.setStatus("current")
_LgpEnvSleepTimeSubID_Type = Integer32
_LgpEnvSleepTimeSubID_Object = MibTableColumn
lgpEnvSleepTimeSubID = _LgpEnvSleepTimeSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 2),
    _LgpEnvSleepTimeSubID_Type()
)
lgpEnvSleepTimeSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeSubID.setStatus("current")


class _LgpEnvSleepTimeStartHour_Type(Integer32):
    """Custom type lgpEnvSleepTimeStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvSleepTimeStartHour_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStartHour_Object = MibTableColumn
lgpEnvSleepTimeStartHour = _LgpEnvSleepTimeStartHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 3),
    _LgpEnvSleepTimeStartHour_Type()
)
lgpEnvSleepTimeStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartHour.setUnits("hour")


class _LgpEnvSleepTimeStartMinute_Type(Integer32):
    """Custom type lgpEnvSleepTimeStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvSleepTimeStartMinute_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStartMinute_Object = MibTableColumn
lgpEnvSleepTimeStartMinute = _LgpEnvSleepTimeStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 4),
    _LgpEnvSleepTimeStartMinute_Type()
)
lgpEnvSleepTimeStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStartMinute.setUnits("minute")


class _LgpEnvSleepTimeStopHour_Type(Integer32):
    """Custom type lgpEnvSleepTimeStopHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_LgpEnvSleepTimeStopHour_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStopHour_Object = MibTableColumn
lgpEnvSleepTimeStopHour = _LgpEnvSleepTimeStopHour_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 5),
    _LgpEnvSleepTimeStopHour_Type()
)
lgpEnvSleepTimeStopHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopHour.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopHour.setUnits("hour")


class _LgpEnvSleepTimeStopMinute_Type(Integer32):
    """Custom type lgpEnvSleepTimeStopMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_LgpEnvSleepTimeStopMinute_Type.__name__ = "Integer32"
_LgpEnvSleepTimeStopMinute_Object = MibTableColumn
lgpEnvSleepTimeStopMinute = _LgpEnvSleepTimeStopMinute_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 3, 1, 6),
    _LgpEnvSleepTimeStopMinute_Type()
)
lgpEnvSleepTimeStopMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopMinute.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvSleepTimeStopMinute.setUnits("minute")
_LgpEnvSleepDayTable_Object = MibTable
lgpEnvSleepDayTable = _LgpEnvSleepDayTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4)
)
if mibBuilder.loadTexts:
    lgpEnvSleepDayTable.setStatus("current")
_LgpEnvSleepDayEntry_Object = MibTableRow
lgpEnvSleepDayEntry = _LgpEnvSleepDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1)
)
lgpEnvSleepDayEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvSleepDayIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvSleepDayEntry.setStatus("current")
_LgpEnvSleepDayIndex_Type = Unsigned32
_LgpEnvSleepDayIndex_Object = MibTableColumn
lgpEnvSleepDayIndex = _LgpEnvSleepDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1, 1),
    _LgpEnvSleepDayIndex_Type()
)
lgpEnvSleepDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvSleepDayIndex.setStatus("current")


class _LgpEnvSleepDay_Type(Integer32):
    """Custom type lgpEnvSleepDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sunday", 1),
          ("monday", 2),
          ("tuesday", 3),
          ("wednesday", 4),
          ("thursday", 5),
          ("friday", 6),
          ("saturday", 7))
    )


_LgpEnvSleepDay_Type.__name__ = "Integer32"
_LgpEnvSleepDay_Object = MibTableColumn
lgpEnvSleepDay = _LgpEnvSleepDay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1, 2),
    _LgpEnvSleepDay_Type()
)
lgpEnvSleepDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvSleepDay.setStatus("current")


class _LgpEnvSleepAllDayEnabled_Type(Integer32):
    """Custom type lgpEnvSleepAllDayEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpEnvSleepAllDayEnabled_Type.__name__ = "Integer32"
_LgpEnvSleepAllDayEnabled_Object = MibTableColumn
lgpEnvSleepAllDayEnabled = _LgpEnvSleepAllDayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 5, 4, 1, 3),
    _LgpEnvSleepAllDayEnabled_Type()
)
lgpEnvSleepAllDayEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvSleepAllDayEnabled.setStatus("current")
_LgpEnvStatistics_ObjectIdentity = ObjectIdentity
lgpEnvStatistics = _LgpEnvStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6)
)
if mibBuilder.loadTexts:
    lgpEnvStatistics.setStatus("current")
_LgpEnvStatisticsComp1RunHr_Type = Unsigned32
_LgpEnvStatisticsComp1RunHr_Object = MibScalar
lgpEnvStatisticsComp1RunHr = _LgpEnvStatisticsComp1RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 1),
    _LgpEnvStatisticsComp1RunHr_Type()
)
lgpEnvStatisticsComp1RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp1RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp1RunHr.setUnits("hours")
_LgpEnvStatisticsComp2RunHr_Type = Unsigned32
_LgpEnvStatisticsComp2RunHr_Object = MibScalar
lgpEnvStatisticsComp2RunHr = _LgpEnvStatisticsComp2RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 2),
    _LgpEnvStatisticsComp2RunHr_Type()
)
lgpEnvStatisticsComp2RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp2RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp2RunHr.setUnits("hours")
_LgpEnvStatisticsFanRunHr_Type = Unsigned32
_LgpEnvStatisticsFanRunHr_Object = MibScalar
lgpEnvStatisticsFanRunHr = _LgpEnvStatisticsFanRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 3),
    _LgpEnvStatisticsFanRunHr_Type()
)
lgpEnvStatisticsFanRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsFanRunHr.setStatus("current")
_LgpEnvStatisticsHumRunHr_Type = Unsigned32
_LgpEnvStatisticsHumRunHr_Object = MibScalar
lgpEnvStatisticsHumRunHr = _LgpEnvStatisticsHumRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 4),
    _LgpEnvStatisticsHumRunHr_Type()
)
lgpEnvStatisticsHumRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHumRunHr.setStatus("current")
_LgpEnvStatisticsReheat1RunHr_Type = Unsigned32
_LgpEnvStatisticsReheat1RunHr_Object = MibScalar
lgpEnvStatisticsReheat1RunHr = _LgpEnvStatisticsReheat1RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 7),
    _LgpEnvStatisticsReheat1RunHr_Type()
)
lgpEnvStatisticsReheat1RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat1RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat1RunHr.setUnits("hours")
_LgpEnvStatisticsReheat2RunHr_Type = Unsigned32
_LgpEnvStatisticsReheat2RunHr_Object = MibScalar
lgpEnvStatisticsReheat2RunHr = _LgpEnvStatisticsReheat2RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 8),
    _LgpEnvStatisticsReheat2RunHr_Type()
)
lgpEnvStatisticsReheat2RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat2RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat2RunHr.setUnits("hours")
_LgpEnvStatisticsReheat3RunHr_Type = Unsigned32
_LgpEnvStatisticsReheat3RunHr_Object = MibScalar
lgpEnvStatisticsReheat3RunHr = _LgpEnvStatisticsReheat3RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 9),
    _LgpEnvStatisticsReheat3RunHr_Type()
)
lgpEnvStatisticsReheat3RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat3RunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsReheat3RunHr.setUnits("hours")
_LgpEnvStatisticsCoolingModeHrs_Type = Unsigned32
_LgpEnvStatisticsCoolingModeHrs_Object = MibScalar
lgpEnvStatisticsCoolingModeHrs = _LgpEnvStatisticsCoolingModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 10),
    _LgpEnvStatisticsCoolingModeHrs_Type()
)
lgpEnvStatisticsCoolingModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsCoolingModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsCoolingModeHrs.setUnits("hours")
_LgpEnvStatisticsHeatingModeHrs_Type = Unsigned32
_LgpEnvStatisticsHeatingModeHrs_Object = MibScalar
lgpEnvStatisticsHeatingModeHrs = _LgpEnvStatisticsHeatingModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 11),
    _LgpEnvStatisticsHeatingModeHrs_Type()
)
lgpEnvStatisticsHeatingModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHeatingModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHeatingModeHrs.setUnits("hours")
_LgpEnvStatisticsHumidifyModeHrs_Type = Unsigned32
_LgpEnvStatisticsHumidifyModeHrs_Object = MibScalar
lgpEnvStatisticsHumidifyModeHrs = _LgpEnvStatisticsHumidifyModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 12),
    _LgpEnvStatisticsHumidifyModeHrs_Type()
)
lgpEnvStatisticsHumidifyModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHumidifyModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHumidifyModeHrs.setUnits("hours")
_LgpEnvStatisticsDehumidifyModeHrs_Type = Unsigned32
_LgpEnvStatisticsDehumidifyModeHrs_Object = MibScalar
lgpEnvStatisticsDehumidifyModeHrs = _LgpEnvStatisticsDehumidifyModeHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 13),
    _LgpEnvStatisticsDehumidifyModeHrs_Type()
)
lgpEnvStatisticsDehumidifyModeHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsDehumidifyModeHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsDehumidifyModeHrs.setUnits("hours")
_LgpEnvStatisticsHotGasRunHr_Type = Unsigned32
_LgpEnvStatisticsHotGasRunHr_Object = MibScalar
lgpEnvStatisticsHotGasRunHr = _LgpEnvStatisticsHotGasRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 14),
    _LgpEnvStatisticsHotGasRunHr_Type()
)
lgpEnvStatisticsHotGasRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotGasRunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotGasRunHr.setUnits("hours")
_LgpEnvStatisticsHotWaterRunHr_Type = Unsigned32
_LgpEnvStatisticsHotWaterRunHr_Object = MibScalar
lgpEnvStatisticsHotWaterRunHr = _LgpEnvStatisticsHotWaterRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 15),
    _LgpEnvStatisticsHotWaterRunHr_Type()
)
lgpEnvStatisticsHotWaterRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotWaterRunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsHotWaterRunHr.setUnits("hours")
_LgpEnvStatisticsFreeCoolRunHr_Type = Unsigned32
_LgpEnvStatisticsFreeCoolRunHr_Object = MibScalar
lgpEnvStatisticsFreeCoolRunHr = _LgpEnvStatisticsFreeCoolRunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 16),
    _LgpEnvStatisticsFreeCoolRunHr_Type()
)
lgpEnvStatisticsFreeCoolRunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsFreeCoolRunHr.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvStatisticsFreeCoolRunHr.setUnits("hours")
_LgpEnvStatisticsComp3RunHr_Type = Unsigned32
_LgpEnvStatisticsComp3RunHr_Object = MibScalar
lgpEnvStatisticsComp3RunHr = _LgpEnvStatisticsComp3RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 17),
    _LgpEnvStatisticsComp3RunHr_Type()
)
lgpEnvStatisticsComp3RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp3RunHr.setStatus("current")
_LgpEnvStatisticsComp4RunHr_Type = Unsigned32
_LgpEnvStatisticsComp4RunHr_Object = MibScalar
lgpEnvStatisticsComp4RunHr = _LgpEnvStatisticsComp4RunHr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 6, 18),
    _LgpEnvStatisticsComp4RunHr_Type()
)
lgpEnvStatisticsComp4RunHr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvStatisticsComp4RunHr.setStatus("current")
_LgpEnvPoints_ObjectIdentity = ObjectIdentity
lgpEnvPoints = _LgpEnvPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7)
)
if mibBuilder.loadTexts:
    lgpEnvPoints.setStatus("current")
_LgpEnvWellKnownPoints_ObjectIdentity = ObjectIdentity
lgpEnvWellKnownPoints = _LgpEnvWellKnownPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1)
)
if mibBuilder.loadTexts:
    lgpEnvWellKnownPoints.setStatus("current")
_LgpEnvFanPoint_ObjectIdentity = ObjectIdentity
lgpEnvFanPoint = _LgpEnvFanPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvFanPoint.setStatus("current")
_LgpEnvCompressorPoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressorPoint = _LgpEnvCompressorPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressorPoint.setStatus("current")
_LgpEnvElectricHeaterPoint_ObjectIdentity = ObjectIdentity
lgpEnvElectricHeaterPoint = _LgpEnvElectricHeaterPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 3)
)
if mibBuilder.loadTexts:
    lgpEnvElectricHeaterPoint.setStatus("current")
_LgpEnvChilledWaterPoint_ObjectIdentity = ObjectIdentity
lgpEnvChilledWaterPoint = _LgpEnvChilledWaterPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 4)
)
if mibBuilder.loadTexts:
    lgpEnvChilledWaterPoint.setStatus("current")
_LgpEnvHumidifierPoint_ObjectIdentity = ObjectIdentity
lgpEnvHumidifierPoint = _LgpEnvHumidifierPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 5)
)
if mibBuilder.loadTexts:
    lgpEnvHumidifierPoint.setStatus("current")
_LgpEnvDehumidifierPoint_ObjectIdentity = ObjectIdentity
lgpEnvDehumidifierPoint = _LgpEnvDehumidifierPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 6)
)
if mibBuilder.loadTexts:
    lgpEnvDehumidifierPoint.setStatus("current")
_LgpEnvFreeCoolingPoint_ObjectIdentity = ObjectIdentity
lgpEnvFreeCoolingPoint = _LgpEnvFreeCoolingPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 7)
)
if mibBuilder.loadTexts:
    lgpEnvFreeCoolingPoint.setStatus("current")
_LgpEnvHotWaterPoint_ObjectIdentity = ObjectIdentity
lgpEnvHotWaterPoint = _LgpEnvHotWaterPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 8)
)
if mibBuilder.loadTexts:
    lgpEnvHotWaterPoint.setStatus("current")
_LgpEnvHotGasPoint_ObjectIdentity = ObjectIdentity
lgpEnvHotGasPoint = _LgpEnvHotGasPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 9)
)
if mibBuilder.loadTexts:
    lgpEnvHotGasPoint.setStatus("current")
_LgpEnvBatteryCabinetPoint_ObjectIdentity = ObjectIdentity
lgpEnvBatteryCabinetPoint = _LgpEnvBatteryCabinetPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 10)
)
if mibBuilder.loadTexts:
    lgpEnvBatteryCabinetPoint.setStatus("current")
_LgpEnvPumpPoints_ObjectIdentity = ObjectIdentity
lgpEnvPumpPoints = _LgpEnvPumpPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 11)
)
if mibBuilder.loadTexts:
    lgpEnvPumpPoints.setStatus("current")
_LgpEnvPump1Point_ObjectIdentity = ObjectIdentity
lgpEnvPump1Point = _LgpEnvPump1Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 11, 1)
)
if mibBuilder.loadTexts:
    lgpEnvPump1Point.setStatus("current")
_LgpEnvPump2Point_ObjectIdentity = ObjectIdentity
lgpEnvPump2Point = _LgpEnvPump2Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 11, 2)
)
if mibBuilder.loadTexts:
    lgpEnvPump2Point.setStatus("current")
_LgpEnvCompressorPoints_ObjectIdentity = ObjectIdentity
lgpEnvCompressorPoints = _LgpEnvCompressorPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12)
)
if mibBuilder.loadTexts:
    lgpEnvCompressorPoints.setStatus("current")
_LgpEnvCompressor1Point_ObjectIdentity = ObjectIdentity
lgpEnvCompressor1Point = _LgpEnvCompressor1Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor1Point.setStatus("current")
_LgpEnvCompressor1APoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor1APoint = _LgpEnvCompressor1APoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor1APoint.setStatus("current")
_LgpEnvCompressor1BPoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor1BPoint = _LgpEnvCompressor1BPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor1BPoint.setStatus("current")
_LgpEnvCompressor2Point_ObjectIdentity = ObjectIdentity
lgpEnvCompressor2Point = _LgpEnvCompressor2Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor2Point.setStatus("current")
_LgpEnvCompressor2APoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor2APoint = _LgpEnvCompressor2APoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor2APoint.setStatus("current")
_LgpEnvCompressor2BPoint_ObjectIdentity = ObjectIdentity
lgpEnvCompressor2BPoint = _LgpEnvCompressor2BPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 12, 2, 2)
)
if mibBuilder.loadTexts:
    lgpEnvCompressor2BPoint.setStatus("current")
_LgpEnvValvePoints_ObjectIdentity = ObjectIdentity
lgpEnvValvePoints = _LgpEnvValvePoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 13)
)
if mibBuilder.loadTexts:
    lgpEnvValvePoints.setStatus("current")
_LgpEnvHotGasValve1Point_ObjectIdentity = ObjectIdentity
lgpEnvHotGasValve1Point = _LgpEnvHotGasValve1Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 13, 1)
)
if mibBuilder.loadTexts:
    lgpEnvHotGasValve1Point.setStatus("current")
_LgpEnvHotGasValve2Point_ObjectIdentity = ObjectIdentity
lgpEnvHotGasValve2Point = _LgpEnvHotGasValve2Point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 13, 2)
)
if mibBuilder.loadTexts:
    lgpEnvHotGasValve2Point.setStatus("current")
_LgpEnvRemoteSensorStatisticPoints_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorStatisticPoints = _LgpEnvRemoteSensorStatisticPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorStatisticPoints.setStatus("current")
_LgpEnvRemoteSensorMinimumPoint_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorMinimumPoint = _LgpEnvRemoteSensorMinimumPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14, 1)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorMinimumPoint.setStatus("current")
_LgpEnvRemoteSensorMaximumPoint_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorMaximumPoint = _LgpEnvRemoteSensorMaximumPoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14, 2)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorMaximumPoint.setStatus("current")
_LgpEnvRemoteSensorAveragePoint_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensorAveragePoint = _LgpEnvRemoteSensorAveragePoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 7, 1, 14, 3)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorAveragePoint.setStatus("current")
_LgpEnvUnits_ObjectIdentity = ObjectIdentity
lgpEnvUnits = _LgpEnvUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 8)
)
if mibBuilder.loadTexts:
    lgpEnvUnits.setStatus("current")
_LgpEnvWellKnownUnits_ObjectIdentity = ObjectIdentity
lgpEnvWellKnownUnits = _LgpEnvWellKnownUnits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    lgpEnvWellKnownUnits.setStatus("current")
_LgpEnvHours_ObjectIdentity = ObjectIdentity
lgpEnvHours = _LgpEnvHours_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 8, 1, 1)
)
if mibBuilder.loadTexts:
    lgpEnvHours.setStatus("current")
_LgpEnvRemoteSensors_ObjectIdentity = ObjectIdentity
lgpEnvRemoteSensors = _LgpEnvRemoteSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensors.setStatus("current")


class _LgpEnvRemoteSensorCalc_Type(Integer32):
    """Custom type lgpEnvRemoteSensorCalc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("maximum", 2))
    )


_LgpEnvRemoteSensorCalc_Type.__name__ = "Integer32"
_LgpEnvRemoteSensorCalc_Object = MibScalar
lgpEnvRemoteSensorCalc = _LgpEnvRemoteSensorCalc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 1),
    _LgpEnvRemoteSensorCalc_Type()
)
lgpEnvRemoteSensorCalc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorCalc.setStatus("current")
_LgpEnvRemoteSensorTable_Object = MibTable
lgpEnvRemoteSensorTable = _LgpEnvRemoteSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10)
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTable.setStatus("current")
_LgpEnvRemoteSensorEntry_Object = MibTableRow
lgpEnvRemoteSensorEntry = _LgpEnvRemoteSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1)
)
lgpEnvRemoteSensorEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpEnvRemoteSensorIndex"),
)
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorEntry.setStatus("current")
_LgpEnvRemoteSensorIndex_Type = Unsigned32
_LgpEnvRemoteSensorIndex_Object = MibTableColumn
lgpEnvRemoteSensorIndex = _LgpEnvRemoteSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 1),
    _LgpEnvRemoteSensorIndex_Type()
)
lgpEnvRemoteSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorIndex.setStatus("current")
_LgpEnvRemoteSensorId_Type = Unsigned32
_LgpEnvRemoteSensorId_Object = MibTableColumn
lgpEnvRemoteSensorId = _LgpEnvRemoteSensorId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 2),
    _LgpEnvRemoteSensorId_Type()
)
lgpEnvRemoteSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorId.setStatus("current")


class _LgpEnvRemoteSensorMode_Type(Integer32):
    """Custom type lgpEnvRemoteSensorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("reference", 1),
          ("control", 2))
    )


_LgpEnvRemoteSensorMode_Type.__name__ = "Integer32"
_LgpEnvRemoteSensorMode_Object = MibTableColumn
lgpEnvRemoteSensorMode = _LgpEnvRemoteSensorMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 3),
    _LgpEnvRemoteSensorMode_Type()
)
lgpEnvRemoteSensorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorMode.setStatus("current")
_LgpEnvRemoteSensorUsrLabel_Type = DisplayString
_LgpEnvRemoteSensorUsrLabel_Object = MibTableColumn
lgpEnvRemoteSensorUsrLabel = _LgpEnvRemoteSensorUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 4),
    _LgpEnvRemoteSensorUsrLabel_Type()
)
lgpEnvRemoteSensorUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorUsrLabel.setStatus("current")
_LgpEnvRemoteSensorTempMeasurementDegF_Type = Integer32
_LgpEnvRemoteSensorTempMeasurementDegF_Object = MibTableColumn
lgpEnvRemoteSensorTempMeasurementDegF = _LgpEnvRemoteSensorTempMeasurementDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 5),
    _LgpEnvRemoteSensorTempMeasurementDegF_Type()
)
lgpEnvRemoteSensorTempMeasurementDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegF.setUnits("degrees Fahrenheit")
_LgpEnvRemoteSensorTempMeasurementDegC_Type = Integer32
_LgpEnvRemoteSensorTempMeasurementDegC_Object = MibTableColumn
lgpEnvRemoteSensorTempMeasurementDegC = _LgpEnvRemoteSensorTempMeasurementDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 4, 9, 10, 1, 6),
    _LgpEnvRemoteSensorTempMeasurementDegC_Type()
)
lgpEnvRemoteSensorTempMeasurementDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpEnvRemoteSensorTempMeasurementDegC.setUnits("degrees Celsius")
_LgpPower_ObjectIdentity = ObjectIdentity
lgpPower = _LgpPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5)
)
if mibBuilder.loadTexts:
    lgpPower.setStatus("current")
_LgpPwrBattery_ObjectIdentity = ObjectIdentity
lgpPwrBattery = _LgpPwrBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1)
)
if mibBuilder.loadTexts:
    lgpPwrBattery.setStatus("current")
_LgpPwrNumberInstalledBatteryModules_Type = Integer32
_LgpPwrNumberInstalledBatteryModules_Object = MibScalar
lgpPwrNumberInstalledBatteryModules = _LgpPwrNumberInstalledBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 1),
    _LgpPwrNumberInstalledBatteryModules_Type()
)
lgpPwrNumberInstalledBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberInstalledBatteryModules.setStatus("current")
_LgpPwrNumberFailedBatteryModules_Type = Integer32
_LgpPwrNumberFailedBatteryModules_Object = MibScalar
lgpPwrNumberFailedBatteryModules = _LgpPwrNumberFailedBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 2),
    _LgpPwrNumberFailedBatteryModules_Type()
)
lgpPwrNumberFailedBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberFailedBatteryModules.setStatus("current")
_LgpPwrNumberRedundantBatteryModules_Type = Integer32
_LgpPwrNumberRedundantBatteryModules_Object = MibScalar
lgpPwrNumberRedundantBatteryModules = _LgpPwrNumberRedundantBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 3),
    _LgpPwrNumberRedundantBatteryModules_Type()
)
lgpPwrNumberRedundantBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberRedundantBatteryModules.setStatus("current")
_LgpPwrNumberActiveBatteryModules_Type = Integer32
_LgpPwrNumberActiveBatteryModules_Object = MibScalar
lgpPwrNumberActiveBatteryModules = _LgpPwrNumberActiveBatteryModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 4),
    _LgpPwrNumberActiveBatteryModules_Type()
)
lgpPwrNumberActiveBatteryModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberActiveBatteryModules.setStatus("current")
_LgpPwrConfigLowBatteryWarningTime_Type = Integer32
_LgpPwrConfigLowBatteryWarningTime_Object = MibScalar
lgpPwrConfigLowBatteryWarningTime = _LgpPwrConfigLowBatteryWarningTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 5),
    _LgpPwrConfigLowBatteryWarningTime_Type()
)
lgpPwrConfigLowBatteryWarningTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrConfigLowBatteryWarningTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrConfigLowBatteryWarningTime.setUnits("minutes")
_LgpPwrNumberBatteryModuleWarnings_Type = Integer32
_LgpPwrNumberBatteryModuleWarnings_Object = MibScalar
lgpPwrNumberBatteryModuleWarnings = _LgpPwrNumberBatteryModuleWarnings_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 6),
    _LgpPwrNumberBatteryModuleWarnings_Type()
)
lgpPwrNumberBatteryModuleWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberBatteryModuleWarnings.setStatus("current")
_LgpPwrBatteryCount_Type = Integer32
_LgpPwrBatteryCount_Object = MibScalar
lgpPwrBatteryCount = _LgpPwrBatteryCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 7),
    _LgpPwrBatteryCount_Type()
)
lgpPwrBatteryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCount.setUnits("Count")


class _LgpPwrBatteryTestResult_Type(Integer32):
    """Custom type lgpPwrBatteryTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("systemFailure", 5),
          ("inhibited", 6))
    )


_LgpPwrBatteryTestResult_Type.__name__ = "Integer32"
_LgpPwrBatteryTestResult_Object = MibScalar
lgpPwrBatteryTestResult = _LgpPwrBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 8),
    _LgpPwrBatteryTestResult_Type()
)
lgpPwrBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryTestResult.setStatus("current")
_LgpPwrNominalBatteryCapacity_Type = Integer32
_LgpPwrNominalBatteryCapacity_Object = MibScalar
lgpPwrNominalBatteryCapacity = _LgpPwrNominalBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 9),
    _LgpPwrNominalBatteryCapacity_Type()
)
lgpPwrNominalBatteryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrNominalBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNominalBatteryCapacity.setUnits("minutes")
_LgpPwrBatteryFloatVoltage_Type = Integer32
_LgpPwrBatteryFloatVoltage_Object = MibScalar
lgpPwrBatteryFloatVoltage = _LgpPwrBatteryFloatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 10),
    _LgpPwrBatteryFloatVoltage_Type()
)
lgpPwrBatteryFloatVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryFloatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryFloatVoltage.setUnits("Volt")
_LgpPwrBatteryEndOfDischargeVoltage_Type = Integer32
_LgpPwrBatteryEndOfDischargeVoltage_Object = MibScalar
lgpPwrBatteryEndOfDischargeVoltage = _LgpPwrBatteryEndOfDischargeVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 11),
    _LgpPwrBatteryEndOfDischargeVoltage_Type()
)
lgpPwrBatteryEndOfDischargeVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryEndOfDischargeVoltage.setStatus("current")
_LgpPwrAutomaticBatteryTestInterval_Type = Integer32
_LgpPwrAutomaticBatteryTestInterval_Object = MibScalar
lgpPwrAutomaticBatteryTestInterval = _LgpPwrAutomaticBatteryTestInterval_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 12),
    _LgpPwrAutomaticBatteryTestInterval_Type()
)
lgpPwrAutomaticBatteryTestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestInterval.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestInterval.setUnits("hours")
_LgpPwrAutomaticBatteryTestCountdown_Type = Integer32
_LgpPwrAutomaticBatteryTestCountdown_Object = MibScalar
lgpPwrAutomaticBatteryTestCountdown = _LgpPwrAutomaticBatteryTestCountdown_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 13),
    _LgpPwrAutomaticBatteryTestCountdown_Type()
)
lgpPwrAutomaticBatteryTestCountdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestCountdown.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTestCountdown.setUnits("minutes")


class _LgpPwrBatteryChargeStatus_Type(Integer32):
    """Custom type lgpPwrBatteryChargeStatus based on Integer32"""
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
        *(("fullycharged", 1),
          ("notfullycharged", 2),
          ("charging", 3),
          ("discharging", 4))
    )


_LgpPwrBatteryChargeStatus_Type.__name__ = "Integer32"
_LgpPwrBatteryChargeStatus_Object = MibScalar
lgpPwrBatteryChargeStatus = _LgpPwrBatteryChargeStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 14),
    _LgpPwrBatteryChargeStatus_Type()
)
lgpPwrBatteryChargeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryChargeStatus.setStatus("current")


class _LgpPwrBatteryLifeEnhancer_Type(Integer32):
    """Custom type lgpPwrBatteryLifeEnhancer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrBatteryLifeEnhancer_Type.__name__ = "Integer32"
_LgpPwrBatteryLifeEnhancer_Object = MibScalar
lgpPwrBatteryLifeEnhancer = _LgpPwrBatteryLifeEnhancer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 15),
    _LgpPwrBatteryLifeEnhancer_Type()
)
lgpPwrBatteryLifeEnhancer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryLifeEnhancer.setStatus("current")


class _LgpPwrBatteryCharger_Type(Integer32):
    """Custom type lgpPwrBatteryCharger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrBatteryCharger_Type.__name__ = "Integer32"
_LgpPwrBatteryCharger_Object = MibScalar
lgpPwrBatteryCharger = _LgpPwrBatteryCharger_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 16),
    _LgpPwrBatteryCharger_Type()
)
lgpPwrBatteryCharger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCharger.setStatus("current")


class _LgpPwrBatteryChargeMode_Type(Integer32):
    """Custom type lgpPwrBatteryChargeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("float", 1),
          ("equalize", 2))
    )


_LgpPwrBatteryChargeMode_Type.__name__ = "Integer32"
_LgpPwrBatteryChargeMode_Object = MibScalar
lgpPwrBatteryChargeMode = _LgpPwrBatteryChargeMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 17),
    _LgpPwrBatteryChargeMode_Type()
)
lgpPwrBatteryChargeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryChargeMode.setStatus("current")
_LgpPwrBatteryTimeRemaining_Type = Integer32
_LgpPwrBatteryTimeRemaining_Object = MibScalar
lgpPwrBatteryTimeRemaining = _LgpPwrBatteryTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 18),
    _LgpPwrBatteryTimeRemaining_Type()
)
lgpPwrBatteryTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryTimeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryTimeRemaining.setUnits("minutes")
_LgpPwrBatteryCapacity_Type = Integer32
_LgpPwrBatteryCapacity_Object = MibScalar
lgpPwrBatteryCapacity = _LgpPwrBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 19),
    _LgpPwrBatteryCapacity_Type()
)
lgpPwrBatteryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCapacity.setUnits("percent")
_LgpPwrBatteryCabinet_ObjectIdentity = ObjectIdentity
lgpPwrBatteryCabinet = _LgpPwrBatteryCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20)
)
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinet.setStatus("current")
_LgpPwrBatteryCabinetCount_Type = Integer32
_LgpPwrBatteryCabinetCount_Object = MibScalar
lgpPwrBatteryCabinetCount = _LgpPwrBatteryCabinetCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 1),
    _LgpPwrBatteryCabinetCount_Type()
)
lgpPwrBatteryCabinetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetCount.setUnits("Count")


class _LgpPwrBatteryCabinetType_Type(Integer32):
    """Custom type lgpPwrBatteryCabinetType based on Integer32"""
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
        *(("notSpecified", 1),
          ("internal", 2),
          ("external", 3),
          ("lrt", 4))
    )


_LgpPwrBatteryCabinetType_Type.__name__ = "Integer32"
_LgpPwrBatteryCabinetType_Object = MibScalar
lgpPwrBatteryCabinetType = _LgpPwrBatteryCabinetType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 2),
    _LgpPwrBatteryCabinetType_Type()
)
lgpPwrBatteryCabinetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetType.setStatus("current")
_LgpPwrBatteryCabinetRatedCapacity_Type = Integer32
_LgpPwrBatteryCabinetRatedCapacity_Object = MibScalar
lgpPwrBatteryCabinetRatedCapacity = _LgpPwrBatteryCabinetRatedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 3),
    _LgpPwrBatteryCabinetRatedCapacity_Type()
)
lgpPwrBatteryCabinetRatedCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetRatedCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryCabinetRatedCapacity.setUnits("0.1 Amp-hour")
_LgpPwrBatteryLeadAcidCellCount_Type = Integer32
_LgpPwrBatteryLeadAcidCellCount_Object = MibScalar
lgpPwrBatteryLeadAcidCellCount = _LgpPwrBatteryLeadAcidCellCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 4),
    _LgpPwrBatteryLeadAcidCellCount_Type()
)
lgpPwrBatteryLeadAcidCellCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryLeadAcidCellCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryLeadAcidCellCount.setUnits("Count")
_LgpPwrBatteryNiCadCellCount_Type = Integer32
_LgpPwrBatteryNiCadCellCount_Object = MibScalar
lgpPwrBatteryNiCadCellCount = _LgpPwrBatteryNiCadCellCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 20, 5),
    _LgpPwrBatteryNiCadCellCount_Type()
)
lgpPwrBatteryNiCadCellCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryNiCadCellCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryNiCadCellCount.setUnits("Count")
_LgpPwrBatteryAmpHoursConsumed_Type = Integer32
_LgpPwrBatteryAmpHoursConsumed_Object = MibScalar
lgpPwrBatteryAmpHoursConsumed = _LgpPwrBatteryAmpHoursConsumed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 21),
    _LgpPwrBatteryAmpHoursConsumed_Type()
)
lgpPwrBatteryAmpHoursConsumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursConsumed.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursConsumed.setUnits("Amp-hour")
_LgpPwrBatteryAmpHoursDischargeConsumed_Type = Integer32
_LgpPwrBatteryAmpHoursDischargeConsumed_Object = MibScalar
lgpPwrBatteryAmpHoursDischargeConsumed = _LgpPwrBatteryAmpHoursDischargeConsumed_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 22),
    _LgpPwrBatteryAmpHoursDischargeConsumed_Type()
)
lgpPwrBatteryAmpHoursDischargeConsumed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursDischargeConsumed.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHoursDischargeConsumed.setUnits("Amp-hour")
_LgpPwrBatteryLastDischargeTime_Type = Unsigned32
_LgpPwrBatteryLastDischargeTime_Object = MibScalar
lgpPwrBatteryLastDischargeTime = _LgpPwrBatteryLastDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 23),
    _LgpPwrBatteryLastDischargeTime_Type()
)
lgpPwrBatteryLastDischargeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastDischargeTime.setUnits("seconds")
_LgpPwrBatteryLastCommissionTime_Type = Unsigned32
_LgpPwrBatteryLastCommissionTime_Object = MibScalar
lgpPwrBatteryLastCommissionTime = _LgpPwrBatteryLastCommissionTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 24),
    _LgpPwrBatteryLastCommissionTime_Type()
)
lgpPwrBatteryLastCommissionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastCommissionTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryLastCommissionTime.setUnits("seconds")
_LgpPwrBatteryPresentDischargeTime_Type = Integer32
_LgpPwrBatteryPresentDischargeTime_Object = MibScalar
lgpPwrBatteryPresentDischargeTime = _LgpPwrBatteryPresentDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 25),
    _LgpPwrBatteryPresentDischargeTime_Type()
)
lgpPwrBatteryPresentDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryPresentDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryPresentDischargeTime.setUnits("seconds")


class _LgpPwrBatteryCapacityStatus_Type(Integer32):
    """Custom type lgpPwrBatteryCapacityStatus based on Integer32"""
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
        *(("unknown", 1),
          ("batteryNormal", 2),
          ("batteryLow", 3),
          ("batteryDepleted", 4))
    )


_LgpPwrBatteryCapacityStatus_Type.__name__ = "Integer32"
_LgpPwrBatteryCapacityStatus_Object = MibScalar
lgpPwrBatteryCapacityStatus = _LgpPwrBatteryCapacityStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 26),
    _LgpPwrBatteryCapacityStatus_Type()
)
lgpPwrBatteryCapacityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCapacityStatus.setStatus("current")


class _LgpPwrBatteryCircuitBreakerState_Type(Integer32):
    """Custom type lgpPwrBatteryCircuitBreakerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("open", 1),
          ("closed", 2))
    )


_LgpPwrBatteryCircuitBreakerState_Type.__name__ = "Integer32"
_LgpPwrBatteryCircuitBreakerState_Object = MibScalar
lgpPwrBatteryCircuitBreakerState = _LgpPwrBatteryCircuitBreakerState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 1, 27),
    _LgpPwrBatteryCircuitBreakerState_Type()
)
lgpPwrBatteryCircuitBreakerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryCircuitBreakerState.setStatus("current")
_LgpPwrMeasurements_ObjectIdentity = ObjectIdentity
lgpPwrMeasurements = _LgpPwrMeasurements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2)
)
if mibBuilder.loadTexts:
    lgpPwrMeasurements.setStatus("current")
_LgpPwrWellKnownMeasurementPoints_ObjectIdentity = ObjectIdentity
lgpPwrWellKnownMeasurementPoints = _LgpPwrWellKnownMeasurementPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lgpPwrWellKnownMeasurementPoints.setStatus("current")
_LgpPwrSource1Input_ObjectIdentity = ObjectIdentity
lgpPwrSource1Input = _LgpPwrSource1Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lgpPwrSource1Input.setStatus("current")
_LgpPwrSource2Input_ObjectIdentity = ObjectIdentity
lgpPwrSource2Input = _LgpPwrSource2Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lgpPwrSource2Input.setStatus("current")
_LgpPwrSourcePdu1Input_ObjectIdentity = ObjectIdentity
lgpPwrSourcePdu1Input = _LgpPwrSourcePdu1Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 3)
)
if mibBuilder.loadTexts:
    lgpPwrSourcePdu1Input.setStatus("current")
_LgpPwrSourcePdu2Input_ObjectIdentity = ObjectIdentity
lgpPwrSourcePdu2Input = _LgpPwrSourcePdu2Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 4)
)
if mibBuilder.loadTexts:
    lgpPwrSourcePdu2Input.setStatus("current")
_LgpPwrOutputToLoad_ObjectIdentity = ObjectIdentity
lgpPwrOutputToLoad = _LgpPwrOutputToLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 5)
)
if mibBuilder.loadTexts:
    lgpPwrOutputToLoad.setStatus("current")
_LgpPwrMeasBattery_ObjectIdentity = ObjectIdentity
lgpPwrMeasBattery = _LgpPwrMeasBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 6)
)
if mibBuilder.loadTexts:
    lgpPwrMeasBattery.setStatus("current")
_LgpPwrMeasBypass_ObjectIdentity = ObjectIdentity
lgpPwrMeasBypass = _LgpPwrMeasBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 7)
)
if mibBuilder.loadTexts:
    lgpPwrMeasBypass.setStatus("current")
_LgpPwrMeasDcBus_ObjectIdentity = ObjectIdentity
lgpPwrMeasDcBus = _LgpPwrMeasDcBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 8)
)
if mibBuilder.loadTexts:
    lgpPwrMeasDcBus.setStatus("current")
_LgpPwrMeasSystemOutput_ObjectIdentity = ObjectIdentity
lgpPwrMeasSystemOutput = _LgpPwrMeasSystemOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 9)
)
if mibBuilder.loadTexts:
    lgpPwrMeasSystemOutput.setStatus("current")
_LgpPwrMeasBatteryCabinet_ObjectIdentity = ObjectIdentity
lgpPwrMeasBatteryCabinet = _LgpPwrMeasBatteryCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 1, 10)
)
if mibBuilder.loadTexts:
    lgpPwrMeasBatteryCabinet.setStatus("current")
_LgpPwrMeasurementPointTable_Object = MibTable
lgpPwrMeasurementPointTable = _LgpPwrMeasurementPointTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointTable.setStatus("current")
_LgpPwrMeasurementPointEntry_Object = MibTableRow
lgpPwrMeasurementPointEntry = _LgpPwrMeasurementPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1)
)
lgpPwrMeasurementPointEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPwrMeasurementPointIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointEntry.setStatus("current")
_LgpPwrMeasurementPointIndex_Type = Unsigned32
_LgpPwrMeasurementPointIndex_Object = MibTableColumn
lgpPwrMeasurementPointIndex = _LgpPwrMeasurementPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 1),
    _LgpPwrMeasurementPointIndex_Type()
)
lgpPwrMeasurementPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointIndex.setStatus("current")
_LgpPwrMeasurementPointId_Type = ObjectIdentifier
_LgpPwrMeasurementPointId_Object = MibTableColumn
lgpPwrMeasurementPointId = _LgpPwrMeasurementPointId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 2),
    _LgpPwrMeasurementPointId_Type()
)
lgpPwrMeasurementPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointId.setStatus("current")
_LgpPwrMeasurementPointNumLines_Type = Integer32
_LgpPwrMeasurementPointNumLines_Object = MibTableColumn
lgpPwrMeasurementPointNumLines = _LgpPwrMeasurementPointNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 3),
    _LgpPwrMeasurementPointNumLines_Type()
)
lgpPwrMeasurementPointNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNumLines.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNumLines.setUnits("Count")
_LgpPwrMeasurementPointNomVolts_Type = Integer32
_LgpPwrMeasurementPointNomVolts_Object = MibTableColumn
lgpPwrMeasurementPointNomVolts = _LgpPwrMeasurementPointNomVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 4),
    _LgpPwrMeasurementPointNomVolts_Type()
)
lgpPwrMeasurementPointNomVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVolts.setUnits("Volt")
_LgpPwrMeasurementPointNomFrequency_Type = Integer32
_LgpPwrMeasurementPointNomFrequency_Object = MibTableColumn
lgpPwrMeasurementPointNomFrequency = _LgpPwrMeasurementPointNomFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 5),
    _LgpPwrMeasurementPointNomFrequency_Type()
)
lgpPwrMeasurementPointNomFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomFrequency.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomFrequency.setUnits("Hertz")
_LgpPwrMeasurementPointFrequency_Type = Integer32
_LgpPwrMeasurementPointFrequency_Object = MibTableColumn
lgpPwrMeasurementPointFrequency = _LgpPwrMeasurementPointFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 6),
    _LgpPwrMeasurementPointFrequency_Type()
)
lgpPwrMeasurementPointFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointFrequency.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointFrequency.setUnits("Hertz")
_LgpPwrMeasurementPointApparentPower_Type = Integer32
_LgpPwrMeasurementPointApparentPower_Object = MibTableColumn
lgpPwrMeasurementPointApparentPower = _LgpPwrMeasurementPointApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 7),
    _LgpPwrMeasurementPointApparentPower_Type()
)
lgpPwrMeasurementPointApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointApparentPower.setUnits("Volt-Amp")
_LgpPwrMeasurementPointTruePower_Type = Integer32
_LgpPwrMeasurementPointTruePower_Object = MibTableColumn
lgpPwrMeasurementPointTruePower = _LgpPwrMeasurementPointTruePower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 8),
    _LgpPwrMeasurementPointTruePower_Type()
)
lgpPwrMeasurementPointTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointTruePower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointTruePower.setUnits("Watt")
_LgpPwrMeasurementPointPowerFactor_Type = Integer32
_LgpPwrMeasurementPointPowerFactor_Object = MibTableColumn
lgpPwrMeasurementPointPowerFactor = _LgpPwrMeasurementPointPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 9),
    _LgpPwrMeasurementPointPowerFactor_Type()
)
lgpPwrMeasurementPointPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointPowerFactor.setUnits(".01 Power Factor")
_LgpPwrMeasurementPointWattHours_Type = Integer32
_LgpPwrMeasurementPointWattHours_Object = MibTableColumn
lgpPwrMeasurementPointWattHours = _LgpPwrMeasurementPointWattHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 10),
    _LgpPwrMeasurementPointWattHours_Type()
)
lgpPwrMeasurementPointWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointWattHours.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointWattHours.setUnits("Watt-Hour")
_LgpPwrMeasurementPointVAPercent_Type = Integer32
_LgpPwrMeasurementPointVAPercent_Object = MibTableColumn
lgpPwrMeasurementPointVAPercent = _LgpPwrMeasurementPointVAPercent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 11),
    _LgpPwrMeasurementPointVAPercent_Type()
)
lgpPwrMeasurementPointVAPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointVAPercent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointVAPercent.setUnits("0.1 Percent")
_LgpPwrMeasurementPointNeutralCurrent_Type = Integer32
_LgpPwrMeasurementPointNeutralCurrent_Object = MibTableColumn
lgpPwrMeasurementPointNeutralCurrent = _LgpPwrMeasurementPointNeutralCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 12),
    _LgpPwrMeasurementPointNeutralCurrent_Type()
)
lgpPwrMeasurementPointNeutralCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNeutralCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNeutralCurrent.setUnits("Amp")
_LgpPwrMeasurementPointGroundCurrent_Type = Integer32
_LgpPwrMeasurementPointGroundCurrent_Object = MibTableColumn
lgpPwrMeasurementPointGroundCurrent = _LgpPwrMeasurementPointGroundCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 13),
    _LgpPwrMeasurementPointGroundCurrent_Type()
)
lgpPwrMeasurementPointGroundCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointGroundCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointGroundCurrent.setUnits("0.1 Amp")
_LgpPwrMeasurementPointNomCurrent_Type = Integer32
_LgpPwrMeasurementPointNomCurrent_Object = MibTableColumn
lgpPwrMeasurementPointNomCurrent = _LgpPwrMeasurementPointNomCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 14),
    _LgpPwrMeasurementPointNomCurrent_Type()
)
lgpPwrMeasurementPointNomCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomCurrent.setUnits("0.1 Amp")
_LgpPwrMeasurementPointNomPowerFactor_Type = Integer32
_LgpPwrMeasurementPointNomPowerFactor_Object = MibTableColumn
lgpPwrMeasurementPointNomPowerFactor = _LgpPwrMeasurementPointNomPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 15),
    _LgpPwrMeasurementPointNomPowerFactor_Type()
)
lgpPwrMeasurementPointNomPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomPowerFactor.setUnits(".01 Power Factor")
_LgpPwrMeasurementPointNomVA_Type = Integer32
_LgpPwrMeasurementPointNomVA_Object = MibTableColumn
lgpPwrMeasurementPointNomVA = _LgpPwrMeasurementPointNomVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 16),
    _LgpPwrMeasurementPointNomVA_Type()
)
lgpPwrMeasurementPointNomVA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVA.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomVA.setUnits("Volt-Amp")
_LgpPwrMeasurementPointNomW_Type = Integer32
_LgpPwrMeasurementPointNomW_Object = MibTableColumn
lgpPwrMeasurementPointNomW = _LgpPwrMeasurementPointNomW_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 17),
    _LgpPwrMeasurementPointNomW_Type()
)
lgpPwrMeasurementPointNomW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomW.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointNomW.setUnits("Watt")


class _LgpPwrMeasurementPointPowerFactorTag_Type(Integer32):
    """Custom type lgpPwrMeasurementPointPowerFactorTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leading", 1),
          ("lagging", 2))
    )


_LgpPwrMeasurementPointPowerFactorTag_Type.__name__ = "Integer32"
_LgpPwrMeasurementPointPowerFactorTag_Object = MibTableColumn
lgpPwrMeasurementPointPowerFactorTag = _LgpPwrMeasurementPointPowerFactorTag_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 2, 1, 19),
    _LgpPwrMeasurementPointPowerFactorTag_Type()
)
lgpPwrMeasurementPointPowerFactorTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPointPowerFactorTag.setStatus("current")
_LgpPwrLineMeasurementTable_Object = MibTable
lgpPwrLineMeasurementTable = _LgpPwrLineMeasurementTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3)
)
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementTable.setStatus("current")
_LgpPwrLineMeasurementEntry_Object = MibTableRow
lgpPwrLineMeasurementEntry = _LgpPwrLineMeasurementEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1)
)
lgpPwrLineMeasurementEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPwrMeasurementPtIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPwrLineMeasurementIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementEntry.setStatus("current")
_LgpPwrMeasurementPtIndex_Type = Unsigned32
_LgpPwrMeasurementPtIndex_Object = MibTableColumn
lgpPwrMeasurementPtIndex = _LgpPwrMeasurementPtIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 1),
    _LgpPwrMeasurementPtIndex_Type()
)
lgpPwrMeasurementPtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPtIndex.setStatus("current")
_LgpPwrLineMeasurementIndex_Type = Unsigned32
_LgpPwrLineMeasurementIndex_Object = MibTableColumn
lgpPwrLineMeasurementIndex = _LgpPwrLineMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 2),
    _LgpPwrLineMeasurementIndex_Type()
)
lgpPwrLineMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementIndex.setStatus("current")
_LgpPwrMeasurementPoint_Type = ObjectIdentifier
_LgpPwrMeasurementPoint_Object = MibTableColumn
lgpPwrMeasurementPoint = _LgpPwrMeasurementPoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 3),
    _LgpPwrMeasurementPoint_Type()
)
lgpPwrMeasurementPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMeasurementPoint.setStatus("current")
_LgpPwrLineMeasurementVoltsLL_Type = Integer32
_LgpPwrLineMeasurementVoltsLL_Object = MibTableColumn
lgpPwrLineMeasurementVoltsLL = _LgpPwrLineMeasurementVoltsLL_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 4),
    _LgpPwrLineMeasurementVoltsLL_Type()
)
lgpPwrLineMeasurementVoltsLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLL.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLL.setUnits("Volt")
_LgpPwrLineMeasurementVoltsLN_Type = Integer32
_LgpPwrLineMeasurementVoltsLN_Object = MibTableColumn
lgpPwrLineMeasurementVoltsLN = _LgpPwrLineMeasurementVoltsLN_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 5),
    _LgpPwrLineMeasurementVoltsLN_Type()
)
lgpPwrLineMeasurementVoltsLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLN.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltsLN.setUnits("Volt")
_LgpPwrLineMeasurementCurrent_Type = Integer32
_LgpPwrLineMeasurementCurrent_Object = MibTableColumn
lgpPwrLineMeasurementCurrent = _LgpPwrLineMeasurementCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 6),
    _LgpPwrLineMeasurementCurrent_Type()
)
lgpPwrLineMeasurementCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrent.setUnits("Amp")
_LgpPwrLineMeasurementCapacity_Type = Integer32
_LgpPwrLineMeasurementCapacity_Object = MibTableColumn
lgpPwrLineMeasurementCapacity = _LgpPwrLineMeasurementCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 7),
    _LgpPwrLineMeasurementCapacity_Type()
)
lgpPwrLineMeasurementCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCapacity.setUnits("percent")
_LgpPwrLineMeasurementVA_Type = Integer32
_LgpPwrLineMeasurementVA_Object = MibTableColumn
lgpPwrLineMeasurementVA = _LgpPwrLineMeasurementVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 8),
    _LgpPwrLineMeasurementVA_Type()
)
lgpPwrLineMeasurementVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVA.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVA.setUnits("Volt-Amp")
_LgpPwrLineMeasurementTruePower_Type = Integer32
_LgpPwrLineMeasurementTruePower_Object = MibTableColumn
lgpPwrLineMeasurementTruePower = _LgpPwrLineMeasurementTruePower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 9),
    _LgpPwrLineMeasurementTruePower_Type()
)
lgpPwrLineMeasurementTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementTruePower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementTruePower.setUnits("Watt")
_LgpPwrLineMeasurementVoltageTHD_Type = Integer32
_LgpPwrLineMeasurementVoltageTHD_Object = MibTableColumn
lgpPwrLineMeasurementVoltageTHD = _LgpPwrLineMeasurementVoltageTHD_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 10),
    _LgpPwrLineMeasurementVoltageTHD_Type()
)
lgpPwrLineMeasurementVoltageTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltageTHD.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVoltageTHD.setUnits("0.1 Percent")
_LgpPwrLineMeasurementCurrentTHD_Type = Integer32
_LgpPwrLineMeasurementCurrentTHD_Object = MibTableColumn
lgpPwrLineMeasurementCurrentTHD = _LgpPwrLineMeasurementCurrentTHD_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 11),
    _LgpPwrLineMeasurementCurrentTHD_Type()
)
lgpPwrLineMeasurementCurrentTHD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrentTHD.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCurrentTHD.setUnits("0.1 Percent")
_LgpPwrLineMeasurementKFactorCurrent_Type = Integer32
_LgpPwrLineMeasurementKFactorCurrent_Object = MibTableColumn
lgpPwrLineMeasurementKFactorCurrent = _LgpPwrLineMeasurementKFactorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 12),
    _LgpPwrLineMeasurementKFactorCurrent_Type()
)
lgpPwrLineMeasurementKFactorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementKFactorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementKFactorCurrent.setUnits("0.1 K Factor")
_LgpPwrLineMeasurementCrestFactorCurrent_Type = Integer32
_LgpPwrLineMeasurementCrestFactorCurrent_Object = MibTableColumn
lgpPwrLineMeasurementCrestFactorCurrent = _LgpPwrLineMeasurementCrestFactorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 13),
    _LgpPwrLineMeasurementCrestFactorCurrent_Type()
)
lgpPwrLineMeasurementCrestFactorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCrestFactorCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementCrestFactorCurrent.setUnits("0.1 Crest Factor")
_LgpPwrLineMeasurementPowerFactor_Type = Integer32
_LgpPwrLineMeasurementPowerFactor_Object = MibTableColumn
lgpPwrLineMeasurementPowerFactor = _LgpPwrLineMeasurementPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 14),
    _LgpPwrLineMeasurementPowerFactor_Type()
)
lgpPwrLineMeasurementPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPowerFactor.setUnits("0.01 Power Factor")


class _LgpPwrLineMeasurementPowerFactorTag_Type(Integer32):
    """Custom type lgpPwrLineMeasurementPowerFactorTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leading", 1),
          ("lagging", 2))
    )


_LgpPwrLineMeasurementPowerFactorTag_Type.__name__ = "Integer32"
_LgpPwrLineMeasurementPowerFactorTag_Object = MibTableColumn
lgpPwrLineMeasurementPowerFactorTag = _LgpPwrLineMeasurementPowerFactorTag_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 15),
    _LgpPwrLineMeasurementPowerFactorTag_Type()
)
lgpPwrLineMeasurementPowerFactorTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPowerFactorTag.setStatus("current")
_LgpPwrLineMeasurementMaxVolts_Type = Integer32
_LgpPwrLineMeasurementMaxVolts_Object = MibTableColumn
lgpPwrLineMeasurementMaxVolts = _LgpPwrLineMeasurementMaxVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 16),
    _LgpPwrLineMeasurementMaxVolts_Type()
)
lgpPwrLineMeasurementMaxVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMaxVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMaxVolts.setUnits("Volt")
_LgpPwrLineMeasurementMinVolts_Type = Integer32
_LgpPwrLineMeasurementMinVolts_Object = MibTableColumn
lgpPwrLineMeasurementMinVolts = _LgpPwrLineMeasurementMinVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 17),
    _LgpPwrLineMeasurementMinVolts_Type()
)
lgpPwrLineMeasurementMinVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMinVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementMinVolts.setUnits("Volt")
_LgpPwrLineMeasurementVAR_Type = Integer32
_LgpPwrLineMeasurementVAR_Object = MibTableColumn
lgpPwrLineMeasurementVAR = _LgpPwrLineMeasurementVAR_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 18),
    _LgpPwrLineMeasurementVAR_Type()
)
lgpPwrLineMeasurementVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVAR.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVAR.setUnits("Volt-Amp-Reactive")
_LgpPwrLineMeasurementPercentLoad_Type = Integer32
_LgpPwrLineMeasurementPercentLoad_Object = MibTableColumn
lgpPwrLineMeasurementPercentLoad = _LgpPwrLineMeasurementPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 19),
    _LgpPwrLineMeasurementPercentLoad_Type()
)
lgpPwrLineMeasurementPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementPercentLoad.setUnits("percent")
_LgpPwrLineMeasurementVolts_Type = Integer32
_LgpPwrLineMeasurementVolts_Object = MibTableColumn
lgpPwrLineMeasurementVolts = _LgpPwrLineMeasurementVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 20),
    _LgpPwrLineMeasurementVolts_Type()
)
lgpPwrLineMeasurementVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVolts.setUnits("Volt")
_LgpPwrLineMeasurementVACapacity_Type = Integer32
_LgpPwrLineMeasurementVACapacity_Object = MibTableColumn
lgpPwrLineMeasurementVACapacity = _LgpPwrLineMeasurementVACapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 3, 1, 21),
    _LgpPwrLineMeasurementVACapacity_Type()
)
lgpPwrLineMeasurementVACapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVACapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrLineMeasurementVACapacity.setUnits("percent")
_LgpPwrDcMeasurementPointTable_Object = MibTable
lgpPwrDcMeasurementPointTable = _LgpPwrDcMeasurementPointTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointTable.setStatus("current")
_LgpPwrDcMeasurementPointEntry_Object = MibTableRow
lgpPwrDcMeasurementPointEntry = _LgpPwrDcMeasurementPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1)
)
lgpPwrDcMeasurementPointEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPwrDcMeasurementPointIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointEntry.setStatus("current")
_LgpPwrDcMeasurementPointIndex_Type = Unsigned32
_LgpPwrDcMeasurementPointIndex_Object = MibTableColumn
lgpPwrDcMeasurementPointIndex = _LgpPwrDcMeasurementPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 1),
    _LgpPwrDcMeasurementPointIndex_Type()
)
lgpPwrDcMeasurementPointIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointIndex.setStatus("current")
_LgpPwrDcMeasurementPointId_Type = ObjectIdentifier
_LgpPwrDcMeasurementPointId_Object = MibTableColumn
lgpPwrDcMeasurementPointId = _LgpPwrDcMeasurementPointId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 2),
    _LgpPwrDcMeasurementPointId_Type()
)
lgpPwrDcMeasurementPointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointId.setStatus("current")
_LgpPwrDcMeasurementPointSubID_Type = Integer32
_LgpPwrDcMeasurementPointSubID_Object = MibTableColumn
lgpPwrDcMeasurementPointSubID = _LgpPwrDcMeasurementPointSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 3),
    _LgpPwrDcMeasurementPointSubID_Type()
)
lgpPwrDcMeasurementPointSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointSubID.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointSubID.setUnits("Count")
_LgpPwrDcMeasurementPointVolts_Type = Integer32
_LgpPwrDcMeasurementPointVolts_Object = MibTableColumn
lgpPwrDcMeasurementPointVolts = _LgpPwrDcMeasurementPointVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 4),
    _LgpPwrDcMeasurementPointVolts_Type()
)
lgpPwrDcMeasurementPointVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointVolts.setUnits("Volt")
_LgpPwrDcMeasurementPointCurrent_Type = Integer32
_LgpPwrDcMeasurementPointCurrent_Object = MibTableColumn
lgpPwrDcMeasurementPointCurrent = _LgpPwrDcMeasurementPointCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 5),
    _LgpPwrDcMeasurementPointCurrent_Type()
)
lgpPwrDcMeasurementPointCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointCurrent.setUnits("Amp")
_LgpPwrDcMeasurementPointNomVolts_Type = Integer32
_LgpPwrDcMeasurementPointNomVolts_Object = MibTableColumn
lgpPwrDcMeasurementPointNomVolts = _LgpPwrDcMeasurementPointNomVolts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 6),
    _LgpPwrDcMeasurementPointNomVolts_Type()
)
lgpPwrDcMeasurementPointNomVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointNomVolts.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointNomVolts.setUnits("Volt")
_LgpPwrDcMeasurementPointTruePower_Type = Integer32
_LgpPwrDcMeasurementPointTruePower_Object = MibTableColumn
lgpPwrDcMeasurementPointTruePower = _LgpPwrDcMeasurementPointTruePower_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 4, 1, 7),
    _LgpPwrDcMeasurementPointTruePower_Type()
)
lgpPwrDcMeasurementPointTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointTruePower.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrDcMeasurementPointTruePower.setUnits("Watt")
_LgpPwrWellKnownMeasurementTypes_ObjectIdentity = ObjectIdentity
lgpPwrWellKnownMeasurementTypes = _LgpPwrWellKnownMeasurementTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5)
)
if mibBuilder.loadTexts:
    lgpPwrWellKnownMeasurementTypes.setStatus("current")
_LgpPwrVoltsAc_ObjectIdentity = ObjectIdentity
lgpPwrVoltsAc = _LgpPwrVoltsAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5, 1)
)
if mibBuilder.loadTexts:
    lgpPwrVoltsAc.setStatus("current")
_LgpPwrVoltsDc_ObjectIdentity = ObjectIdentity
lgpPwrVoltsDc = _LgpPwrVoltsDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5, 2)
)
if mibBuilder.loadTexts:
    lgpPwrVoltsDc.setStatus("current")
_LgpPwrAmpsNeutral_ObjectIdentity = ObjectIdentity
lgpPwrAmpsNeutral = _LgpPwrAmpsNeutral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 2, 5, 3)
)
if mibBuilder.loadTexts:
    lgpPwrAmpsNeutral.setStatus("current")
_LgpPwrStatus_ObjectIdentity = ObjectIdentity
lgpPwrStatus = _LgpPwrStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3)
)
if mibBuilder.loadTexts:
    lgpPwrStatus.setStatus("current")
_LgpPwrTransferCount_Type = Integer32
_LgpPwrTransferCount_Object = MibScalar
lgpPwrTransferCount = _LgpPwrTransferCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 1),
    _LgpPwrTransferCount_Type()
)
lgpPwrTransferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTransferCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrTransferCount.setUnits("Count")
_LgpPwrAutoTransferTimer_Type = Integer32
_LgpPwrAutoTransferTimer_Object = MibScalar
lgpPwrAutoTransferTimer = _LgpPwrAutoTransferTimer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 2),
    _LgpPwrAutoTransferTimer_Type()
)
lgpPwrAutoTransferTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrAutoTransferTimer.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutoTransferTimer.setUnits("seconds")


class _LgpPwrAutoReTransferEnabled_Type(Integer32):
    """Custom type lgpPwrAutoReTransferEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LgpPwrAutoReTransferEnabled_Type.__name__ = "Integer32"
_LgpPwrAutoReTransferEnabled_Object = MibScalar
lgpPwrAutoReTransferEnabled = _LgpPwrAutoReTransferEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 3),
    _LgpPwrAutoReTransferEnabled_Type()
)
lgpPwrAutoReTransferEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrAutoReTransferEnabled.setStatus("current")


class _LgpPwrSyncPhaseAngle_Type(Integer32):
    """Custom type lgpPwrSyncPhaseAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-3600, 3600),
    )


_LgpPwrSyncPhaseAngle_Type.__name__ = "Integer32"
_LgpPwrSyncPhaseAngle_Object = MibScalar
lgpPwrSyncPhaseAngle = _LgpPwrSyncPhaseAngle_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 4),
    _LgpPwrSyncPhaseAngle_Type()
)
lgpPwrSyncPhaseAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrSyncPhaseAngle.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrSyncPhaseAngle.setUnits("0.1 Degrees")


class _LgpPwrParallelSystemOutputToLoadSource_Type(Integer32):
    """Custom type lgpPwrParallelSystemOutputToLoadSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("utility", 1),
          ("battery", 2),
          ("bypass", 3),
          ("none", 4))
    )


_LgpPwrParallelSystemOutputToLoadSource_Type.__name__ = "Integer32"
_LgpPwrParallelSystemOutputToLoadSource_Object = MibScalar
lgpPwrParallelSystemOutputToLoadSource = _LgpPwrParallelSystemOutputToLoadSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 5),
    _LgpPwrParallelSystemOutputToLoadSource_Type()
)
lgpPwrParallelSystemOutputToLoadSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrParallelSystemOutputToLoadSource.setStatus("current")


class _LgpPwrDcToDcConverter_Type(Integer32):
    """Custom type lgpPwrDcToDcConverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrDcToDcConverter_Type.__name__ = "Integer32"
_LgpPwrDcToDcConverter_Object = MibScalar
lgpPwrDcToDcConverter = _LgpPwrDcToDcConverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 6),
    _LgpPwrDcToDcConverter_Type()
)
lgpPwrDcToDcConverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrDcToDcConverter.setStatus("current")


class _LgpPwrOutputToLoadOnInverter_Type(Integer32):
    """Custom type lgpPwrOutputToLoadOnInverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrOutputToLoadOnInverter_Type.__name__ = "Integer32"
_LgpPwrOutputToLoadOnInverter_Object = MibScalar
lgpPwrOutputToLoadOnInverter = _LgpPwrOutputToLoadOnInverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 7),
    _LgpPwrOutputToLoadOnInverter_Type()
)
lgpPwrOutputToLoadOnInverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadOnInverter.setStatus("current")


class _LgpPwrBatteryChargeCompensating_Type(Integer32):
    """Custom type lgpPwrBatteryChargeCompensating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrBatteryChargeCompensating_Type.__name__ = "Integer32"
_LgpPwrBatteryChargeCompensating_Object = MibScalar
lgpPwrBatteryChargeCompensating = _LgpPwrBatteryChargeCompensating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 8),
    _LgpPwrBatteryChargeCompensating_Type()
)
lgpPwrBatteryChargeCompensating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryChargeCompensating.setStatus("current")


class _LgpPwrInverterReady_Type(Integer32):
    """Custom type lgpPwrInverterReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrInverterReady_Type.__name__ = "Integer32"
_LgpPwrInverterReady_Object = MibScalar
lgpPwrInverterReady = _LgpPwrInverterReady_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 9),
    _LgpPwrInverterReady_Type()
)
lgpPwrInverterReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrInverterReady.setStatus("current")


class _LgpPwrOutputToLoadOnBypass_Type(Integer32):
    """Custom type lgpPwrOutputToLoadOnBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrOutputToLoadOnBypass_Type.__name__ = "Integer32"
_LgpPwrOutputToLoadOnBypass_Object = MibScalar
lgpPwrOutputToLoadOnBypass = _LgpPwrOutputToLoadOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 10),
    _LgpPwrOutputToLoadOnBypass_Type()
)
lgpPwrOutputToLoadOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadOnBypass.setStatus("current")


class _LgpPwrBoost_Type(Integer32):
    """Custom type lgpPwrBoost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrBoost_Type.__name__ = "Integer32"
_LgpPwrBoost_Object = MibScalar
lgpPwrBoost = _LgpPwrBoost_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 11),
    _LgpPwrBoost_Type()
)
lgpPwrBoost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBoost.setStatus("current")


class _LgpPwrBuck_Type(Integer32):
    """Custom type lgpPwrBuck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrBuck_Type.__name__ = "Integer32"
_LgpPwrBuck_Object = MibScalar
lgpPwrBuck = _LgpPwrBuck_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 12),
    _LgpPwrBuck_Type()
)
lgpPwrBuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBuck.setStatus("current")


class _LgpPwrShutdownOverTemperature_Type(Integer32):
    """Custom type lgpPwrShutdownOverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownOverTemperature_Type.__name__ = "Integer32"
_LgpPwrShutdownOverTemperature_Object = MibScalar
lgpPwrShutdownOverTemperature = _LgpPwrShutdownOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 13),
    _LgpPwrShutdownOverTemperature_Type()
)
lgpPwrShutdownOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownOverTemperature.setStatus("current")


class _LgpPwrShutdownOverload_Type(Integer32):
    """Custom type lgpPwrShutdownOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownOverload_Type.__name__ = "Integer32"
_LgpPwrShutdownOverload_Object = MibScalar
lgpPwrShutdownOverload = _LgpPwrShutdownOverload_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 14),
    _LgpPwrShutdownOverload_Type()
)
lgpPwrShutdownOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownOverload.setStatus("current")


class _LgpPwrShutdownDcBusOverload_Type(Integer32):
    """Custom type lgpPwrShutdownDcBusOverload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownDcBusOverload_Type.__name__ = "Integer32"
_LgpPwrShutdownDcBusOverload_Object = MibScalar
lgpPwrShutdownDcBusOverload = _LgpPwrShutdownDcBusOverload_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 15),
    _LgpPwrShutdownDcBusOverload_Type()
)
lgpPwrShutdownDcBusOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownDcBusOverload.setStatus("current")


class _LgpPwrShutdownOutputShort_Type(Integer32):
    """Custom type lgpPwrShutdownOutputShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownOutputShort_Type.__name__ = "Integer32"
_LgpPwrShutdownOutputShort_Object = MibScalar
lgpPwrShutdownOutputShort = _LgpPwrShutdownOutputShort_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 16),
    _LgpPwrShutdownOutputShort_Type()
)
lgpPwrShutdownOutputShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownOutputShort.setStatus("current")


class _LgpPwrShutdownLineSwap_Type(Integer32):
    """Custom type lgpPwrShutdownLineSwap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownLineSwap_Type.__name__ = "Integer32"
_LgpPwrShutdownLineSwap_Object = MibScalar
lgpPwrShutdownLineSwap = _LgpPwrShutdownLineSwap_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 17),
    _LgpPwrShutdownLineSwap_Type()
)
lgpPwrShutdownLineSwap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownLineSwap.setStatus("current")


class _LgpPwrShutdownLowBattery_Type(Integer32):
    """Custom type lgpPwrShutdownLowBattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownLowBattery_Type.__name__ = "Integer32"
_LgpPwrShutdownLowBattery_Object = MibScalar
lgpPwrShutdownLowBattery = _LgpPwrShutdownLowBattery_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 18),
    _LgpPwrShutdownLowBattery_Type()
)
lgpPwrShutdownLowBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownLowBattery.setStatus("current")


class _LgpPwrShutdownRemote_Type(Integer32):
    """Custom type lgpPwrShutdownRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownRemote_Type.__name__ = "Integer32"
_LgpPwrShutdownRemote_Object = MibScalar
lgpPwrShutdownRemote = _LgpPwrShutdownRemote_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 19),
    _LgpPwrShutdownRemote_Type()
)
lgpPwrShutdownRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownRemote.setStatus("current")


class _LgpPwrShutdownInputUnderVoltage_Type(Integer32):
    """Custom type lgpPwrShutdownInputUnderVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownInputUnderVoltage_Type.__name__ = "Integer32"
_LgpPwrShutdownInputUnderVoltage_Object = MibScalar
lgpPwrShutdownInputUnderVoltage = _LgpPwrShutdownInputUnderVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 20),
    _LgpPwrShutdownInputUnderVoltage_Type()
)
lgpPwrShutdownInputUnderVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownInputUnderVoltage.setStatus("current")


class _LgpPwrShutdownPowerFactorCorrectionFailure_Type(Integer32):
    """Custom type lgpPwrShutdownPowerFactorCorrectionFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownPowerFactorCorrectionFailure_Type.__name__ = "Integer32"
_LgpPwrShutdownPowerFactorCorrectionFailure_Object = MibScalar
lgpPwrShutdownPowerFactorCorrectionFailure = _LgpPwrShutdownPowerFactorCorrectionFailure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 21),
    _LgpPwrShutdownPowerFactorCorrectionFailure_Type()
)
lgpPwrShutdownPowerFactorCorrectionFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownPowerFactorCorrectionFailure.setStatus("current")


class _LgpPwrShutdownHardware_Type(Integer32):
    """Custom type lgpPwrShutdownHardware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrShutdownHardware_Type.__name__ = "Integer32"
_LgpPwrShutdownHardware_Object = MibScalar
lgpPwrShutdownHardware = _LgpPwrShutdownHardware_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 22),
    _LgpPwrShutdownHardware_Type()
)
lgpPwrShutdownHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrShutdownHardware.setStatus("current")


class _LgpPwrRedundantSubModule_Type(Integer32):
    """Custom type lgpPwrRedundantSubModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrRedundantSubModule_Type.__name__ = "Integer32"
_LgpPwrRedundantSubModule_Object = MibScalar
lgpPwrRedundantSubModule = _LgpPwrRedundantSubModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 23),
    _LgpPwrRedundantSubModule_Type()
)
lgpPwrRedundantSubModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRedundantSubModule.setStatus("current")


class _LgpPwrBypassReady_Type(Integer32):
    """Custom type lgpPwrBypassReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrBypassReady_Type.__name__ = "Integer32"
_LgpPwrBypassReady_Object = MibScalar
lgpPwrBypassReady = _LgpPwrBypassReady_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 24),
    _LgpPwrBypassReady_Type()
)
lgpPwrBypassReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassReady.setStatus("current")


class _LgpPwrGeneratorStatus_Type(Integer32):
    """Custom type lgpPwrGeneratorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_LgpPwrGeneratorStatus_Type.__name__ = "Integer32"
_LgpPwrGeneratorStatus_Object = MibScalar
lgpPwrGeneratorStatus = _LgpPwrGeneratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 25),
    _LgpPwrGeneratorStatus_Type()
)
lgpPwrGeneratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrGeneratorStatus.setStatus("current")


class _LgpPwrRotaryBreakerStatus_Type(Integer32):
    """Custom type lgpPwrRotaryBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("closed", 2),
          ("test", 3),
          ("normal", 4),
          ("bypass", 5),
          ("maintenance", 6))
    )


_LgpPwrRotaryBreakerStatus_Type.__name__ = "Integer32"
_LgpPwrRotaryBreakerStatus_Object = MibScalar
lgpPwrRotaryBreakerStatus = _LgpPwrRotaryBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 26),
    _LgpPwrRotaryBreakerStatus_Type()
)
lgpPwrRotaryBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRotaryBreakerStatus.setStatus("current")


class _LgpPwrPowerFactorCorrection_Type(Integer32):
    """Custom type lgpPwrPowerFactorCorrection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrPowerFactorCorrection_Type.__name__ = "Integer32"
_LgpPwrPowerFactorCorrection_Object = MibScalar
lgpPwrPowerFactorCorrection = _LgpPwrPowerFactorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 27),
    _LgpPwrPowerFactorCorrection_Type()
)
lgpPwrPowerFactorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrPowerFactorCorrection.setStatus("current")
_LgpPwrBypassSyncDiff_Type = Integer32
_LgpPwrBypassSyncDiff_Object = MibScalar
lgpPwrBypassSyncDiff = _LgpPwrBypassSyncDiff_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 28),
    _LgpPwrBypassSyncDiff_Type()
)
lgpPwrBypassSyncDiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassSyncDiff.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBypassSyncDiff.setUnits("0.1 Degrees")
_LgpPwrBypassOverloadShutdownTime_Type = Integer32
_LgpPwrBypassOverloadShutdownTime_Object = MibScalar
lgpPwrBypassOverloadShutdownTime = _LgpPwrBypassOverloadShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 29),
    _LgpPwrBypassOverloadShutdownTime_Type()
)
lgpPwrBypassOverloadShutdownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassOverloadShutdownTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBypassOverloadShutdownTime.setUnits("seconds")
_LgpPwrInverterOverloadShutdownTime_Type = Integer32
_LgpPwrInverterOverloadShutdownTime_Object = MibScalar
lgpPwrInverterOverloadShutdownTime = _LgpPwrInverterOverloadShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 30),
    _LgpPwrInverterOverloadShutdownTime_Type()
)
lgpPwrInverterOverloadShutdownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrInverterOverloadShutdownTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrInverterOverloadShutdownTime.setUnits("seconds")


class _LgpPwrStateOutputSource_Type(Integer32):
    """Custom type lgpPwrStateOutputSource based on Integer32"""
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
        *(("none", 1),
          ("inverter", 2),
          ("bypass", 3),
          ("maintenanceBypass", 4))
    )


_LgpPwrStateOutputSource_Type.__name__ = "Integer32"
_LgpPwrStateOutputSource_Object = MibScalar
lgpPwrStateOutputSource = _LgpPwrStateOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 31),
    _LgpPwrStateOutputSource_Type()
)
lgpPwrStateOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutputSource.setStatus("current")


class _LgpPwrStateInputSource_Type(Integer32):
    """Custom type lgpPwrStateInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("utility", 2),
          ("generator", 3))
    )


_LgpPwrStateInputSource_Type.__name__ = "Integer32"
_LgpPwrStateInputSource_Object = MibScalar
lgpPwrStateInputSource = _LgpPwrStateInputSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 32),
    _LgpPwrStateInputSource_Type()
)
lgpPwrStateInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInputSource.setStatus("current")


class _LgpPwrStateInputQualification_Type(Integer32):
    """Custom type lgpPwrStateInputQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalLow", 2),
          ("normal", 3),
          ("marginalHigh", 4))
    )


_LgpPwrStateInputQualification_Type.__name__ = "Integer32"
_LgpPwrStateInputQualification_Object = MibScalar
lgpPwrStateInputQualification = _LgpPwrStateInputQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 33),
    _LgpPwrStateInputQualification_Type()
)
lgpPwrStateInputQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInputQualification.setStatus("current")


class _LgpPwrStateBypassStaticSwitchState_Type(Integer32):
    """Custom type lgpPwrStateBypassStaticSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrStateBypassStaticSwitchState_Type.__name__ = "Integer32"
_LgpPwrStateBypassStaticSwitchState_Object = MibScalar
lgpPwrStateBypassStaticSwitchState = _LgpPwrStateBypassStaticSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 34),
    _LgpPwrStateBypassStaticSwitchState_Type()
)
lgpPwrStateBypassStaticSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassStaticSwitchState.setStatus("current")


class _LgpPwrStateBypassQualification_Type(Integer32):
    """Custom type lgpPwrStateBypassQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalLow", 2),
          ("normal", 3),
          ("marginalHigh", 4))
    )


_LgpPwrStateBypassQualification_Type.__name__ = "Integer32"
_LgpPwrStateBypassQualification_Object = MibScalar
lgpPwrStateBypassQualification = _LgpPwrStateBypassQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 35),
    _LgpPwrStateBypassQualification_Type()
)
lgpPwrStateBypassQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassQualification.setStatus("current")


class _LgpPwrStateDCBusQualification_Type(Integer32):
    """Custom type lgpPwrStateDCBusQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalLow", 2),
          ("normal", 3),
          ("marginalHigh", 4))
    )


_LgpPwrStateDCBusQualification_Type.__name__ = "Integer32"
_LgpPwrStateDCBusQualification_Object = MibScalar
lgpPwrStateDCBusQualification = _LgpPwrStateDCBusQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 36),
    _LgpPwrStateDCBusQualification_Type()
)
lgpPwrStateDCBusQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateDCBusQualification.setStatus("current")


class _LgpPwrStateOutQualification_Type(Integer32):
    """Custom type lgpPwrStateOutQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalLow", 2),
          ("normal", 3),
          ("marginalHigh", 4))
    )


_LgpPwrStateOutQualification_Type.__name__ = "Integer32"
_LgpPwrStateOutQualification_Object = MibScalar
lgpPwrStateOutQualification = _LgpPwrStateOutQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 37),
    _LgpPwrStateOutQualification_Type()
)
lgpPwrStateOutQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutQualification.setStatus("current")


class _LgpPwrStateInverterQualification_Type(Integer32):
    """Custom type lgpPwrStateInverterQualification based on Integer32"""
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
        *(("fail", 1),
          ("marginalLow", 2),
          ("normal", 3),
          ("marginalHigh", 4))
    )


_LgpPwrStateInverterQualification_Type.__name__ = "Integer32"
_LgpPwrStateInverterQualification_Object = MibScalar
lgpPwrStateInverterQualification = _LgpPwrStateInverterQualification_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 38),
    _LgpPwrStateInverterQualification_Type()
)
lgpPwrStateInverterQualification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInverterQualification.setStatus("current")


class _LgpPwrStateInverterState_Type(Integer32):
    """Custom type lgpPwrStateInverterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrStateInverterState_Type.__name__ = "Integer32"
_LgpPwrStateInverterState_Object = MibScalar
lgpPwrStateInverterState = _LgpPwrStateInverterState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 39),
    _LgpPwrStateInverterState_Type()
)
lgpPwrStateInverterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInverterState.setStatus("current")


class _LgpPwrStateRectifierState_Type(Integer32):
    """Custom type lgpPwrStateRectifierState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrStateRectifierState_Type.__name__ = "Integer32"
_LgpPwrStateRectifierState_Object = MibScalar
lgpPwrStateRectifierState = _LgpPwrStateRectifierState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 40),
    _LgpPwrStateRectifierState_Type()
)
lgpPwrStateRectifierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateRectifierState.setStatus("current")
_LgpPwrStateModuleGroup_ObjectIdentity = ObjectIdentity
lgpPwrStateModuleGroup = _LgpPwrStateModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 41)
)
if mibBuilder.loadTexts:
    lgpPwrStateModuleGroup.setStatus("current")
_LgpPwrStateUpsModuleCount_Type = Integer32
_LgpPwrStateUpsModuleCount_Object = MibScalar
lgpPwrStateUpsModuleCount = _LgpPwrStateUpsModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 41, 1),
    _LgpPwrStateUpsModuleCount_Type()
)
lgpPwrStateUpsModuleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleCount.setUnits("Count")
_LgpPwrStateUpsModuleRedundantCount_Type = Integer32
_LgpPwrStateUpsModuleRedundantCount_Object = MibScalar
lgpPwrStateUpsModuleRedundantCount = _LgpPwrStateUpsModuleRedundantCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 41, 2),
    _LgpPwrStateUpsModuleRedundantCount_Type()
)
lgpPwrStateUpsModuleRedundantCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleRedundantCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrStateUpsModuleRedundantCount.setUnits("Count")


class _LgpPwrStateBackfeedBrkrState_Type(Integer32):
    """Custom type lgpPwrStateBackfeedBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateBackfeedBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateBackfeedBrkrState_Object = MibScalar
lgpPwrStateBackfeedBrkrState = _LgpPwrStateBackfeedBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 42),
    _LgpPwrStateBackfeedBrkrState_Type()
)
lgpPwrStateBackfeedBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBackfeedBrkrState.setStatus("current")


class _LgpPwrStateLoadDisconnectState_Type(Integer32):
    """Custom type lgpPwrStateLoadDisconnectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateLoadDisconnectState_Type.__name__ = "Integer32"
_LgpPwrStateLoadDisconnectState_Object = MibScalar
lgpPwrStateLoadDisconnectState = _LgpPwrStateLoadDisconnectState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 43),
    _LgpPwrStateLoadDisconnectState_Type()
)
lgpPwrStateLoadDisconnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateLoadDisconnectState.setStatus("current")


class _LgpPwrStateInputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateInputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateInputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateInputBrkrState_Object = MibScalar
lgpPwrStateInputBrkrState = _LgpPwrStateInputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 44),
    _LgpPwrStateInputBrkrState_Type()
)
lgpPwrStateInputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInputBrkrState.setStatus("current")


class _LgpPwrStateTrapFilterBrkrState_Type(Integer32):
    """Custom type lgpPwrStateTrapFilterBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateTrapFilterBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateTrapFilterBrkrState_Object = MibScalar
lgpPwrStateTrapFilterBrkrState = _LgpPwrStateTrapFilterBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 45),
    _LgpPwrStateTrapFilterBrkrState_Type()
)
lgpPwrStateTrapFilterBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateTrapFilterBrkrState.setStatus("current")


class _LgpPwrStateInvOutputBrkrState_Type(Integer32):
    """Custom type lgpPwrStateInvOutputBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateInvOutputBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateInvOutputBrkrState_Object = MibScalar
lgpPwrStateInvOutputBrkrState = _LgpPwrStateInvOutputBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 46),
    _LgpPwrStateInvOutputBrkrState_Type()
)
lgpPwrStateInvOutputBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateInvOutputBrkrState.setStatus("current")


class _LgpPwrStateIntBypassBrkrState_Type(Integer32):
    """Custom type lgpPwrStateIntBypassBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateIntBypassBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateIntBypassBrkrState_Object = MibScalar
lgpPwrStateIntBypassBrkrState = _LgpPwrStateIntBypassBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 47),
    _LgpPwrStateIntBypassBrkrState_Type()
)
lgpPwrStateIntBypassBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateIntBypassBrkrState.setStatus("current")


class _LgpPwrStateBypassIsolBrkrState_Type(Integer32):
    """Custom type lgpPwrStateBypassIsolBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateBypassIsolBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateBypassIsolBrkrState_Object = MibScalar
lgpPwrStateBypassIsolBrkrState = _LgpPwrStateBypassIsolBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 48),
    _LgpPwrStateBypassIsolBrkrState_Type()
)
lgpPwrStateBypassIsolBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassIsolBrkrState.setStatus("current")


class _LgpPwrStateRectifierIsolBrkrState_Type(Integer32):
    """Custom type lgpPwrStateRectifierIsolBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateRectifierIsolBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateRectifierIsolBrkrState_Object = MibScalar
lgpPwrStateRectifierIsolBrkrState = _LgpPwrStateRectifierIsolBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 49),
    _LgpPwrStateRectifierIsolBrkrState_Type()
)
lgpPwrStateRectifierIsolBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateRectifierIsolBrkrState.setStatus("current")


class _LgpPwrStateMaintBypassBrkrState_Type(Integer32):
    """Custom type lgpPwrStateMaintBypassBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateMaintBypassBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateMaintBypassBrkrState_Object = MibScalar
lgpPwrStateMaintBypassBrkrState = _LgpPwrStateMaintBypassBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 50),
    _LgpPwrStateMaintBypassBrkrState_Type()
)
lgpPwrStateMaintBypassBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateMaintBypassBrkrState.setStatus("current")


class _LgpPwrStateMaintIsolBrkrState_Type(Integer32):
    """Custom type lgpPwrStateMaintIsolBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateMaintIsolBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateMaintIsolBrkrState_Object = MibScalar
lgpPwrStateMaintIsolBrkrState = _LgpPwrStateMaintIsolBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 51),
    _LgpPwrStateMaintIsolBrkrState_Type()
)
lgpPwrStateMaintIsolBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateMaintIsolBrkrState.setStatus("current")


class _LgpPwrStateOutStaticSwState_Type(Integer32):
    """Custom type lgpPwrStateOutStaticSwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateOutStaticSwState_Type.__name__ = "Integer32"
_LgpPwrStateOutStaticSwState_Object = MibScalar
lgpPwrStateOutStaticSwState = _LgpPwrStateOutStaticSwState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 52),
    _LgpPwrStateOutStaticSwState_Type()
)
lgpPwrStateOutStaticSwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutStaticSwState.setStatus("current")


class _LgpPwrStateModuleOutBrkrState_Type(Integer32):
    """Custom type lgpPwrStateModuleOutBrkrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("notInstalled", 3))
    )


_LgpPwrStateModuleOutBrkrState_Type.__name__ = "Integer32"
_LgpPwrStateModuleOutBrkrState_Object = MibScalar
lgpPwrStateModuleOutBrkrState = _LgpPwrStateModuleOutBrkrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 53),
    _LgpPwrStateModuleOutBrkrState_Type()
)
lgpPwrStateModuleOutBrkrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateModuleOutBrkrState.setStatus("current")
_LgpPwrBypassReXfrRemainTime_Type = Integer32
_LgpPwrBypassReXfrRemainTime_Object = MibScalar
lgpPwrBypassReXfrRemainTime = _LgpPwrBypassReXfrRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 54),
    _LgpPwrBypassReXfrRemainTime_Type()
)
lgpPwrBypassReXfrRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBypassReXfrRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBypassReXfrRemainTime.setUnits("seconds")


class _LgpPwrStateUpsOutputSource_Type(Integer32):
    """Custom type lgpPwrStateUpsOutputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5),
          ("booster", 6),
          ("reducer", 7))
    )


_LgpPwrStateUpsOutputSource_Type.__name__ = "Integer32"
_LgpPwrStateUpsOutputSource_Object = MibScalar
lgpPwrStateUpsOutputSource = _LgpPwrStateUpsOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 55),
    _LgpPwrStateUpsOutputSource_Type()
)
lgpPwrStateUpsOutputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateUpsOutputSource.setStatus("current")


class _LgpPwrStateLoadBusSynchronization_Type(Integer32):
    """Custom type lgpPwrStateLoadBusSynchronization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("active", 1),
          ("abnormal", 2))
    )


_LgpPwrStateLoadBusSynchronization_Type.__name__ = "Integer32"
_LgpPwrStateLoadBusSynchronization_Object = MibScalar
lgpPwrStateLoadBusSynchronization = _LgpPwrStateLoadBusSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 3, 56),
    _LgpPwrStateLoadBusSynchronization_Type()
)
lgpPwrStateLoadBusSynchronization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateLoadBusSynchronization.setStatus("current")
_LgpPwrSettings_ObjectIdentity = ObjectIdentity
lgpPwrSettings = _LgpPwrSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4)
)
if mibBuilder.loadTexts:
    lgpPwrSettings.setStatus("current")
_LgpPwrPreferredSource_Type = ObjectIdentifier
_LgpPwrPreferredSource_Object = MibScalar
lgpPwrPreferredSource = _LgpPwrPreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 1),
    _LgpPwrPreferredSource_Type()
)
lgpPwrPreferredSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrPreferredSource.setStatus("current")
_LgpPwrLoadOnSource_Type = ObjectIdentifier
_LgpPwrLoadOnSource_Object = MibScalar
lgpPwrLoadOnSource = _LgpPwrLoadOnSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 2),
    _LgpPwrLoadOnSource_Type()
)
lgpPwrLoadOnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLoadOnSource.setStatus("current")
_LgpPwrNominalVoltageDeviation_Type = Integer32
_LgpPwrNominalVoltageDeviation_Object = MibScalar
lgpPwrNominalVoltageDeviation = _LgpPwrNominalVoltageDeviation_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 3),
    _LgpPwrNominalVoltageDeviation_Type()
)
lgpPwrNominalVoltageDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviation.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviation.setUnits("Volt")
_LgpPwrNominalVoltageDeviationPercent_Type = Integer32
_LgpPwrNominalVoltageDeviationPercent_Object = MibScalar
lgpPwrNominalVoltageDeviationPercent = _LgpPwrNominalVoltageDeviationPercent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 4),
    _LgpPwrNominalVoltageDeviationPercent_Type()
)
lgpPwrNominalVoltageDeviationPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviationPercent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNominalVoltageDeviationPercent.setUnits("percent")
_LgpPwrPhaseDifferenceLimit_Type = Integer32
_LgpPwrPhaseDifferenceLimit_Object = MibScalar
lgpPwrPhaseDifferenceLimit = _LgpPwrPhaseDifferenceLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 5),
    _LgpPwrPhaseDifferenceLimit_Type()
)
lgpPwrPhaseDifferenceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrPhaseDifferenceLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrPhaseDifferenceLimit.setUnits("0.1 Degrees")
_LgpPwrFrequencyDeviationLimit_Type = Integer32
_LgpPwrFrequencyDeviationLimit_Object = MibScalar
lgpPwrFrequencyDeviationLimit = _LgpPwrFrequencyDeviationLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 6),
    _LgpPwrFrequencyDeviationLimit_Type()
)
lgpPwrFrequencyDeviationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrFrequencyDeviationLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrFrequencyDeviationLimit.setUnits("0.1 Hertz")
_LgpPwrThresholdTable_Object = MibTable
lgpPwrThresholdTable = _LgpPwrThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7)
)
if mibBuilder.loadTexts:
    lgpPwrThresholdTable.setStatus("current")
_LgpPwrThresholdEntry_Object = MibTableRow
lgpPwrThresholdEntry = _LgpPwrThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1)
)
lgpPwrThresholdEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPwrThresholdIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrThresholdEntry.setStatus("current")
_LgpPwrThresholdIndex_Type = Unsigned32
_LgpPwrThresholdIndex_Object = MibTableColumn
lgpPwrThresholdIndex = _LgpPwrThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 1),
    _LgpPwrThresholdIndex_Type()
)
lgpPwrThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrThresholdIndex.setStatus("current")
_LgpPwrThresholdPoint_Type = ObjectIdentifier
_LgpPwrThresholdPoint_Object = MibTableColumn
lgpPwrThresholdPoint = _LgpPwrThresholdPoint_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 2),
    _LgpPwrThresholdPoint_Type()
)
lgpPwrThresholdPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrThresholdPoint.setStatus("current")
_LgpPwrThresholdSubID_Type = Unsigned32
_LgpPwrThresholdSubID_Object = MibTableColumn
lgpPwrThresholdSubID = _LgpPwrThresholdSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 3),
    _LgpPwrThresholdSubID_Type()
)
lgpPwrThresholdSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrThresholdSubID.setStatus("current")
_LgpPwrThresholdType_Type = ObjectIdentifier
_LgpPwrThresholdType_Object = MibTableColumn
lgpPwrThresholdType = _LgpPwrThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 4),
    _LgpPwrThresholdType_Type()
)
lgpPwrThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrThresholdType.setStatus("current")
_LgpPwrThresholdHighWarning_Type = Integer32
_LgpPwrThresholdHighWarning_Object = MibTableColumn
lgpPwrThresholdHighWarning = _LgpPwrThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 5),
    _LgpPwrThresholdHighWarning_Type()
)
lgpPwrThresholdHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdHighWarning.setStatus("current")
_LgpPwrThresholdHighFailure_Type = Integer32
_LgpPwrThresholdHighFailure_Object = MibTableColumn
lgpPwrThresholdHighFailure = _LgpPwrThresholdHighFailure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 6),
    _LgpPwrThresholdHighFailure_Type()
)
lgpPwrThresholdHighFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdHighFailure.setStatus("current")
_LgpPwrThresholdLowWarning_Type = Integer32
_LgpPwrThresholdLowWarning_Object = MibTableColumn
lgpPwrThresholdLowWarning = _LgpPwrThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 7),
    _LgpPwrThresholdLowWarning_Type()
)
lgpPwrThresholdLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdLowWarning.setStatus("current")
_LgpPwrThresholdLowFailure_Type = Integer32
_LgpPwrThresholdLowFailure_Object = MibTableColumn
lgpPwrThresholdLowFailure = _LgpPwrThresholdLowFailure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 7, 1, 8),
    _LgpPwrThresholdLowFailure_Type()
)
lgpPwrThresholdLowFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrThresholdLowFailure.setStatus("current")


class _LgpPwrUpsAutoRestart_Type(Integer32):
    """Custom type lgpPwrUpsAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrUpsAutoRestart_Type.__name__ = "Integer32"
_LgpPwrUpsAutoRestart_Object = MibScalar
lgpPwrUpsAutoRestart = _LgpPwrUpsAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 8),
    _LgpPwrUpsAutoRestart_Type()
)
lgpPwrUpsAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsAutoRestart.setStatus("current")
_LgpPwrUpsAutoRestartDelay_Type = Integer32
_LgpPwrUpsAutoRestartDelay_Object = MibScalar
lgpPwrUpsAutoRestartDelay = _LgpPwrUpsAutoRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 9),
    _LgpPwrUpsAutoRestartDelay_Type()
)
lgpPwrUpsAutoRestartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsAutoRestartDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrUpsAutoRestartDelay.setUnits("seconds")
_LgpPwrAutoRestartBatteryChargeThreshold_Type = Integer32
_LgpPwrAutoRestartBatteryChargeThreshold_Object = MibScalar
lgpPwrAutoRestartBatteryChargeThreshold = _LgpPwrAutoRestartBatteryChargeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 10),
    _LgpPwrAutoRestartBatteryChargeThreshold_Type()
)
lgpPwrAutoRestartBatteryChargeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutoRestartBatteryChargeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrAutoRestartBatteryChargeThreshold.setUnits("percent")
_LgpPwrParallelModuleCount_Type = Integer32
_LgpPwrParallelModuleCount_Object = MibScalar
lgpPwrParallelModuleCount = _LgpPwrParallelModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 11),
    _LgpPwrParallelModuleCount_Type()
)
lgpPwrParallelModuleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrParallelModuleCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrParallelModuleCount.setUnits("Count")
_LgpPwrParallelRedundancyCount_Type = Integer32
_LgpPwrParallelRedundancyCount_Object = MibScalar
lgpPwrParallelRedundancyCount = _LgpPwrParallelRedundancyCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 12),
    _LgpPwrParallelRedundancyCount_Type()
)
lgpPwrParallelRedundancyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrParallelRedundancyCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrParallelRedundancyCount.setUnits("Count")


class _LgpPwrLoadBusSyncMode_Type(Integer32):
    """Custom type lgpPwrLoadBusSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("none", 3))
    )


_LgpPwrLoadBusSyncMode_Type.__name__ = "Integer32"
_LgpPwrLoadBusSyncMode_Object = MibScalar
lgpPwrLoadBusSyncMode = _LgpPwrLoadBusSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 13),
    _LgpPwrLoadBusSyncMode_Type()
)
lgpPwrLoadBusSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrLoadBusSyncMode.setStatus("current")


class _LgpPwrEconomicOperationMode_Type(Integer32):
    """Custom type lgpPwrEconomicOperationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrEconomicOperationMode_Type.__name__ = "Integer32"
_LgpPwrEconomicOperationMode_Object = MibScalar
lgpPwrEconomicOperationMode = _LgpPwrEconomicOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 14),
    _LgpPwrEconomicOperationMode_Type()
)
lgpPwrEconomicOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrEconomicOperationMode.setStatus("current")


class _LgpPwrAutomaticBatteryTest_Type(Integer32):
    """Custom type lgpPwrAutomaticBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrAutomaticBatteryTest_Type.__name__ = "Integer32"
_LgpPwrAutomaticBatteryTest_Object = MibScalar
lgpPwrAutomaticBatteryTest = _LgpPwrAutomaticBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 15),
    _LgpPwrAutomaticBatteryTest_Type()
)
lgpPwrAutomaticBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAutomaticBatteryTest.setStatus("current")
_LgpPwrMinimumRedundantPowerModule_Type = Integer32
_LgpPwrMinimumRedundantPowerModule_Object = MibScalar
lgpPwrMinimumRedundantPowerModule = _LgpPwrMinimumRedundantPowerModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 16),
    _LgpPwrMinimumRedundantPowerModule_Type()
)
lgpPwrMinimumRedundantPowerModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantPowerModule.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantPowerModule.setUnits("Count")
_LgpPwrMinimumRedundantBatteryModule_Type = Integer32
_LgpPwrMinimumRedundantBatteryModule_Object = MibScalar
lgpPwrMinimumRedundantBatteryModule = _LgpPwrMinimumRedundantBatteryModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 17),
    _LgpPwrMinimumRedundantBatteryModule_Type()
)
lgpPwrMinimumRedundantBatteryModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantBatteryModule.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMinimumRedundantBatteryModule.setUnits("Count")
_LgpPwrOutputToLoadUserOverloadLimit_Type = Integer32
_LgpPwrOutputToLoadUserOverloadLimit_Object = MibScalar
lgpPwrOutputToLoadUserOverloadLimit = _LgpPwrOutputToLoadUserOverloadLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 18),
    _LgpPwrOutputToLoadUserOverloadLimit_Type()
)
lgpPwrOutputToLoadUserOverloadLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadUserOverloadLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputToLoadUserOverloadLimit.setUnits("Volt-Amp")
_LgpPwrNoLoadWarningLimit_Type = Integer32
_LgpPwrNoLoadWarningLimit_Object = MibScalar
lgpPwrNoLoadWarningLimit = _LgpPwrNoLoadWarningLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 19),
    _LgpPwrNoLoadWarningLimit_Type()
)
lgpPwrNoLoadWarningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningLimit.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningLimit.setUnits("Amp")


class _LgpPwrNoLoadWarningDelay_Type(Integer32):
    """Custom type lgpPwrNoLoadWarningDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_LgpPwrNoLoadWarningDelay_Type.__name__ = "Integer32"
_LgpPwrNoLoadWarningDelay_Object = MibScalar
lgpPwrNoLoadWarningDelay = _LgpPwrNoLoadWarningDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 4, 20),
    _LgpPwrNoLoadWarningDelay_Type()
)
lgpPwrNoLoadWarningDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNoLoadWarningDelay.setUnits("minutes")
_LgpPwrConversion_ObjectIdentity = ObjectIdentity
lgpPwrConversion = _LgpPwrConversion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5)
)
if mibBuilder.loadTexts:
    lgpPwrConversion.setStatus("current")
_LgpPwrNumberInstalledPowerModules_Type = Integer32
_LgpPwrNumberInstalledPowerModules_Object = MibScalar
lgpPwrNumberInstalledPowerModules = _LgpPwrNumberInstalledPowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 1),
    _LgpPwrNumberInstalledPowerModules_Type()
)
lgpPwrNumberInstalledPowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberInstalledPowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberInstalledPowerModules.setUnits("Count")
_LgpPwrNumberFailedPowerModules_Type = Integer32
_LgpPwrNumberFailedPowerModules_Object = MibScalar
lgpPwrNumberFailedPowerModules = _LgpPwrNumberFailedPowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 2),
    _LgpPwrNumberFailedPowerModules_Type()
)
lgpPwrNumberFailedPowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberFailedPowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberFailedPowerModules.setUnits("Count")
_LgpPwrNumberRedundantPowerModules_Type = Integer32
_LgpPwrNumberRedundantPowerModules_Object = MibScalar
lgpPwrNumberRedundantPowerModules = _LgpPwrNumberRedundantPowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 3),
    _LgpPwrNumberRedundantPowerModules_Type()
)
lgpPwrNumberRedundantPowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberRedundantPowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberRedundantPowerModules.setUnits("Count")
_LgpPwrNumberActivePowerModules_Type = Integer32
_LgpPwrNumberActivePowerModules_Object = MibScalar
lgpPwrNumberActivePowerModules = _LgpPwrNumberActivePowerModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 4),
    _LgpPwrNumberActivePowerModules_Type()
)
lgpPwrNumberActivePowerModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberActivePowerModules.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberActivePowerModules.setUnits("Count")
_LgpPwrNumberPowerModuleWarnings_Type = Integer32
_LgpPwrNumberPowerModuleWarnings_Object = MibScalar
lgpPwrNumberPowerModuleWarnings = _LgpPwrNumberPowerModuleWarnings_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 6),
    _LgpPwrNumberPowerModuleWarnings_Type()
)
lgpPwrNumberPowerModuleWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrNumberPowerModuleWarnings.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrNumberPowerModuleWarnings.setUnits("Count")


class _LgpPwrUpsInverterStandby_Type(Integer32):
    """Custom type lgpPwrUpsInverterStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpPwrUpsInverterStandby_Type.__name__ = "Integer32"
_LgpPwrUpsInverterStandby_Object = MibScalar
lgpPwrUpsInverterStandby = _LgpPwrUpsInverterStandby_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 5, 7),
    _LgpPwrUpsInverterStandby_Type()
)
lgpPwrUpsInverterStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsInverterStandby.setStatus("current")
_LgpPwrControl_ObjectIdentity = ObjectIdentity
lgpPwrControl = _LgpPwrControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6)
)
if mibBuilder.loadTexts:
    lgpPwrControl.setStatus("current")
_LgpPwrWellKnownControlPoints_ObjectIdentity = ObjectIdentity
lgpPwrWellKnownControlPoints = _LgpPwrWellKnownControlPoints_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lgpPwrWellKnownControlPoints.setStatus("current")
_LgpPwrLoadCircuit_ObjectIdentity = ObjectIdentity
lgpPwrLoadCircuit = _LgpPwrLoadCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 1, 1)
)
if mibBuilder.loadTexts:
    lgpPwrLoadCircuit.setStatus("current")
_LgpPwrLoadCircuitTable_Object = MibTable
lgpPwrLoadCircuitTable = _LgpPwrLoadCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2)
)
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitTable.setStatus("current")
_LgpPwrLoadCircuitEntry_Object = MibTableRow
lgpPwrLoadCircuitEntry = _LgpPwrLoadCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1)
)
lgpPwrLoadCircuitEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPwrLoadCircuitIndex"),
)
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitEntry.setStatus("current")
_LgpPwrLoadCircuitIndex_Type = Unsigned32
_LgpPwrLoadCircuitIndex_Object = MibTableColumn
lgpPwrLoadCircuitIndex = _LgpPwrLoadCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 1),
    _LgpPwrLoadCircuitIndex_Type()
)
lgpPwrLoadCircuitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitIndex.setStatus("current")
_LgpPwrLoadCircuitId_Type = ObjectIdentifier
_LgpPwrLoadCircuitId_Object = MibTableColumn
lgpPwrLoadCircuitId = _LgpPwrLoadCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 2),
    _LgpPwrLoadCircuitId_Type()
)
lgpPwrLoadCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitId.setStatus("current")
_LgpPwrLoadCircuitSubID_Type = Unsigned32
_LgpPwrLoadCircuitSubID_Object = MibTableColumn
lgpPwrLoadCircuitSubID = _LgpPwrLoadCircuitSubID_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 3),
    _LgpPwrLoadCircuitSubID_Type()
)
lgpPwrLoadCircuitSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitSubID.setStatus("current")


class _LgpPwrLoadCircuitState_Type(Integer32):
    """Custom type lgpPwrLoadCircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("default", 3))
    )


_LgpPwrLoadCircuitState_Type.__name__ = "Integer32"
_LgpPwrLoadCircuitState_Object = MibTableColumn
lgpPwrLoadCircuitState = _LgpPwrLoadCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 2, 1, 4),
    _LgpPwrLoadCircuitState_Type()
)
lgpPwrLoadCircuitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrLoadCircuitState.setStatus("current")
_LgpPwrAlarmSilence_Type = Integer32
_LgpPwrAlarmSilence_Object = MibScalar
lgpPwrAlarmSilence = _LgpPwrAlarmSilence_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 3),
    _LgpPwrAlarmSilence_Type()
)
lgpPwrAlarmSilence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrAlarmSilence.setStatus("current")


class _LgpPwrBatteryTest_Type(Integer32):
    """Custom type lgpPwrBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("abort", 2))
    )


_LgpPwrBatteryTest_Type.__name__ = "Integer32"
_LgpPwrBatteryTest_Object = MibScalar
lgpPwrBatteryTest = _LgpPwrBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 4),
    _LgpPwrBatteryTest_Type()
)
lgpPwrBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryTest.setStatus("current")
_LgpPwrUpsAbortCommand_Type = Integer32
_LgpPwrUpsAbortCommand_Object = MibScalar
lgpPwrUpsAbortCommand = _LgpPwrUpsAbortCommand_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 5),
    _LgpPwrUpsAbortCommand_Type()
)
lgpPwrUpsAbortCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUpsAbortCommand.setStatus("current")
_LgpPwrTransferToBypass_Type = Integer32
_LgpPwrTransferToBypass_Object = MibScalar
lgpPwrTransferToBypass = _LgpPwrTransferToBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 6),
    _LgpPwrTransferToBypass_Type()
)
lgpPwrTransferToBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrTransferToBypass.setStatus("current")
_LgpPwrTransferToInverter_Type = Integer32
_LgpPwrTransferToInverter_Object = MibScalar
lgpPwrTransferToInverter = _LgpPwrTransferToInverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 7),
    _LgpPwrTransferToInverter_Type()
)
lgpPwrTransferToInverter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrTransferToInverter.setStatus("current")
_LgpPwrOutputOnDelay_Type = Integer32
_LgpPwrOutputOnDelay_Object = MibScalar
lgpPwrOutputOnDelay = _LgpPwrOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 8),
    _LgpPwrOutputOnDelay_Type()
)
lgpPwrOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputOnDelay.setUnits("seconds")
_LgpPwrOutputOffDelayWithRestart_Type = Integer32
_LgpPwrOutputOffDelayWithRestart_Object = MibScalar
lgpPwrOutputOffDelayWithRestart = _LgpPwrOutputOffDelayWithRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 9),
    _LgpPwrOutputOffDelayWithRestart_Type()
)
lgpPwrOutputOffDelayWithRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithRestart.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithRestart.setUnits("seconds")
_LgpPwrOutputOffDelayWithoutRestart_Type = Integer32
_LgpPwrOutputOffDelayWithoutRestart_Object = MibScalar
lgpPwrOutputOffDelayWithoutRestart = _LgpPwrOutputOffDelayWithoutRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 6, 10),
    _LgpPwrOutputOffDelayWithoutRestart_Type()
)
lgpPwrOutputOffDelayWithoutRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithoutRestart.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrOutputOffDelayWithoutRestart.setUnits("seconds")
_LgpPwrTopology_ObjectIdentity = ObjectIdentity
lgpPwrTopology = _LgpPwrTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7)
)
if mibBuilder.loadTexts:
    lgpPwrTopology.setStatus("current")


class _LgpPwrUpsTopOffline_Type(Integer32):
    """Custom type lgpPwrUpsTopOffline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrUpsTopOffline_Type.__name__ = "Integer32"
_LgpPwrUpsTopOffline_Object = MibScalar
lgpPwrUpsTopOffline = _LgpPwrUpsTopOffline_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 1),
    _LgpPwrUpsTopOffline_Type()
)
lgpPwrUpsTopOffline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrUpsTopOffline.setStatus("current")


class _LgpPwrUpsTopLineInteractive_Type(Integer32):
    """Custom type lgpPwrUpsTopLineInteractive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrUpsTopLineInteractive_Type.__name__ = "Integer32"
_LgpPwrUpsTopLineInteractive_Object = MibScalar
lgpPwrUpsTopLineInteractive = _LgpPwrUpsTopLineInteractive_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 2),
    _LgpPwrUpsTopLineInteractive_Type()
)
lgpPwrUpsTopLineInteractive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrUpsTopLineInteractive.setStatus("current")


class _LgpPwrUPSTopDualInput_Type(Integer32):
    """Custom type lgpPwrUPSTopDualInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrUPSTopDualInput_Type.__name__ = "Integer32"
_LgpPwrUPSTopDualInput_Object = MibScalar
lgpPwrUPSTopDualInput = _LgpPwrUPSTopDualInput_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 3),
    _LgpPwrUPSTopDualInput_Type()
)
lgpPwrUPSTopDualInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrUPSTopDualInput.setStatus("current")


class _LgpPwrTopFrequencyConverter_Type(Integer32):
    """Custom type lgpPwrTopFrequencyConverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrTopFrequencyConverter_Type.__name__ = "Integer32"
_LgpPwrTopFrequencyConverter_Object = MibScalar
lgpPwrTopFrequencyConverter = _LgpPwrTopFrequencyConverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 4),
    _LgpPwrTopFrequencyConverter_Type()
)
lgpPwrTopFrequencyConverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTopFrequencyConverter.setStatus("current")


class _LgpPwrTopVoltageConverter_Type(Integer32):
    """Custom type lgpPwrTopVoltageConverter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrTopVoltageConverter_Type.__name__ = "Integer32"
_LgpPwrTopVoltageConverter_Object = MibScalar
lgpPwrTopVoltageConverter = _LgpPwrTopVoltageConverter_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 5),
    _LgpPwrTopVoltageConverter_Type()
)
lgpPwrTopVoltageConverter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTopVoltageConverter.setStatus("current")
_LgpPwrTopMaximumFrameCapacity_Type = Integer32
_LgpPwrTopMaximumFrameCapacity_Object = MibScalar
lgpPwrTopMaximumFrameCapacity = _LgpPwrTopMaximumFrameCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 6),
    _LgpPwrTopMaximumFrameCapacity_Type()
)
lgpPwrTopMaximumFrameCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrTopMaximumFrameCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrTopMaximumFrameCapacity.setUnits("Volt-Amp")


class _LgpPwrTopRedundantControlModules_Type(Integer32):
    """Custom type lgpPwrTopRedundantControlModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_LgpPwrTopRedundantControlModules_Type.__name__ = "Integer32"
_LgpPwrTopRedundantControlModules_Object = MibScalar
lgpPwrTopRedundantControlModules = _LgpPwrTopRedundantControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 7),
    _LgpPwrTopRedundantControlModules_Type()
)
lgpPwrTopRedundantControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTopRedundantControlModules.setStatus("current")


class _LgpPwrInputIsolationTransformerInstalled_Type(Integer32):
    """Custom type lgpPwrInputIsolationTransformerInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_LgpPwrInputIsolationTransformerInstalled_Type.__name__ = "Integer32"
_LgpPwrInputIsolationTransformerInstalled_Object = MibScalar
lgpPwrInputIsolationTransformerInstalled = _LgpPwrInputIsolationTransformerInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 8),
    _LgpPwrInputIsolationTransformerInstalled_Type()
)
lgpPwrInputIsolationTransformerInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrInputIsolationTransformerInstalled.setStatus("current")


class _LgpPwrStateStaticSwitchType_Type(Integer32):
    """Custom type lgpPwrStateStaticSwitchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("continuousDuty", 2),
          ("momentaryDuty", 3))
    )


_LgpPwrStateStaticSwitchType_Type.__name__ = "Integer32"
_LgpPwrStateStaticSwitchType_Object = MibScalar
lgpPwrStateStaticSwitchType = _LgpPwrStateStaticSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 9),
    _LgpPwrStateStaticSwitchType_Type()
)
lgpPwrStateStaticSwitchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateStaticSwitchType.setStatus("current")


class _LgpPwrStateModuleType_Type(Integer32):
    """Custom type lgpPwrStateModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("singleModuleSystem", 1),
          ("module1plus1", 2),
          ("module1plusN", 3),
          ("moduleNplus1", 4),
          ("systemControlCabinet", 5),
          ("mainStaticSwitch", 6))
    )


_LgpPwrStateModuleType_Type.__name__ = "Integer32"
_LgpPwrStateModuleType_Object = MibScalar
lgpPwrStateModuleType = _LgpPwrStateModuleType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 10),
    _LgpPwrStateModuleType_Type()
)
lgpPwrStateModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateModuleType.setStatus("current")


class _LgpPwrStateBypassInputConfig_Type(Integer32):
    """Custom type lgpPwrStateBypassInputConfig based on Integer32"""
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
        *(("singlePhase2WireL1WithReturn", 1),
          ("twoPhase2WireL1L2", 2),
          ("twoPhase3WireL1L2WithNeutral", 3),
          ("threePhase3WireL1L2L3", 4),
          ("threePhase4WireL1L2L3WithNeutral", 5))
    )


_LgpPwrStateBypassInputConfig_Type.__name__ = "Integer32"
_LgpPwrStateBypassInputConfig_Object = MibScalar
lgpPwrStateBypassInputConfig = _LgpPwrStateBypassInputConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 11),
    _LgpPwrStateBypassInputConfig_Type()
)
lgpPwrStateBypassInputConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateBypassInputConfig.setStatus("current")


class _LgpPwrStateOutputConfig_Type(Integer32):
    """Custom type lgpPwrStateOutputConfig based on Integer32"""
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
        *(("singlePhase2WireL1WithReturn", 1),
          ("twoPhase2WireL1L2", 2),
          ("twoPhase3WireL1L2WithNeutral", 3),
          ("threePhase3WireL1L2L3", 4),
          ("threePhase4WireL1L2L3WithNeutral", 5))
    )


_LgpPwrStateOutputConfig_Type.__name__ = "Integer32"
_LgpPwrStateOutputConfig_Object = MibScalar
lgpPwrStateOutputConfig = _LgpPwrStateOutputConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 12),
    _LgpPwrStateOutputConfig_Type()
)
lgpPwrStateOutputConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrStateOutputConfig.setStatus("current")


class _LgpPwrRectifierPassiveFilterInstalled_Type(Integer32):
    """Custom type lgpPwrRectifierPassiveFilterInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_LgpPwrRectifierPassiveFilterInstalled_Type.__name__ = "Integer32"
_LgpPwrRectifierPassiveFilterInstalled_Object = MibScalar
lgpPwrRectifierPassiveFilterInstalled = _LgpPwrRectifierPassiveFilterInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 13),
    _LgpPwrRectifierPassiveFilterInstalled_Type()
)
lgpPwrRectifierPassiveFilterInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierPassiveFilterInstalled.setStatus("current")


class _LgpPwrRectifierTrapInstalled_Type(Integer32):
    """Custom type lgpPwrRectifierTrapInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_LgpPwrRectifierTrapInstalled_Type.__name__ = "Integer32"
_LgpPwrRectifierTrapInstalled_Object = MibScalar
lgpPwrRectifierTrapInstalled = _LgpPwrRectifierTrapInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 14),
    _LgpPwrRectifierTrapInstalled_Type()
)
lgpPwrRectifierTrapInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierTrapInstalled.setStatus("current")


class _LgpPwrRectifierActiveFilterInstalled_Type(Integer32):
    """Custom type lgpPwrRectifierActiveFilterInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_LgpPwrRectifierActiveFilterInstalled_Type.__name__ = "Integer32"
_LgpPwrRectifierActiveFilterInstalled_Object = MibScalar
lgpPwrRectifierActiveFilterInstalled = _LgpPwrRectifierActiveFilterInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 7, 15),
    _LgpPwrRectifierActiveFilterInstalled_Type()
)
lgpPwrRectifierActiveFilterInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierActiveFilterInstalled.setStatus("current")
_LgpPwrStatistic_ObjectIdentity = ObjectIdentity
lgpPwrStatistic = _LgpPwrStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8)
)
if mibBuilder.loadTexts:
    lgpPwrStatistic.setStatus("current")
_LgpPwrBrownOutCount_Type = Integer32
_LgpPwrBrownOutCount_Object = MibScalar
lgpPwrBrownOutCount = _LgpPwrBrownOutCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 1),
    _LgpPwrBrownOutCount_Type()
)
lgpPwrBrownOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBrownOutCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBrownOutCount.setUnits("Count")
_LgpPwrBlackOutCount_Type = Integer32
_LgpPwrBlackOutCount_Object = MibScalar
lgpPwrBlackOutCount = _LgpPwrBlackOutCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 2),
    _LgpPwrBlackOutCount_Type()
)
lgpPwrBlackOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBlackOutCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBlackOutCount.setUnits("Count")
_LgpPwrTransientCount_Type = Integer32
_LgpPwrTransientCount_Object = MibScalar
lgpPwrTransientCount = _LgpPwrTransientCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 3),
    _LgpPwrTransientCount_Type()
)
lgpPwrTransientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrTransientCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrTransientCount.setUnits("Count")
_LgpPwrBatteryDischargeCount_Type = Integer32
_LgpPwrBatteryDischargeCount_Object = MibScalar
lgpPwrBatteryDischargeCount = _LgpPwrBatteryDischargeCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 4),
    _LgpPwrBatteryDischargeCount_Type()
)
lgpPwrBatteryDischargeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeCount.setUnits("Count")
_LgpPwrBatteryDischargeTime_Type = Integer32
_LgpPwrBatteryDischargeTime_Object = MibScalar
lgpPwrBatteryDischargeTime = _LgpPwrBatteryDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 5),
    _LgpPwrBatteryDischargeTime_Type()
)
lgpPwrBatteryDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeTime.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryDischargeTime.setUnits("minutes")
_LgpPwrBatteryAmpHours_Type = Integer32
_LgpPwrBatteryAmpHours_Object = MibScalar
lgpPwrBatteryAmpHours = _LgpPwrBatteryAmpHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 6),
    _LgpPwrBatteryAmpHours_Type()
)
lgpPwrBatteryAmpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHours.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryAmpHours.setUnits("Amp-hour")
_LgpPwrBatteryWattHours_Type = Integer32
_LgpPwrBatteryWattHours_Object = MibScalar
lgpPwrBatteryWattHours = _LgpPwrBatteryWattHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 7),
    _LgpPwrBatteryWattHours_Type()
)
lgpPwrBatteryWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrBatteryWattHours.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrBatteryWattHours.setUnits("Watt-Hour")
_LgpPwrBatteryStatisticsReset_Type = Integer32
_LgpPwrBatteryStatisticsReset_Object = MibScalar
lgpPwrBatteryStatisticsReset = _LgpPwrBatteryStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 8),
    _LgpPwrBatteryStatisticsReset_Type()
)
lgpPwrBatteryStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrBatteryStatisticsReset.setStatus("current")
_LgpPwrStatisticsReset_Type = Integer32
_LgpPwrStatisticsReset_Object = MibScalar
lgpPwrStatisticsReset = _LgpPwrStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 8, 9),
    _LgpPwrStatisticsReset_Type()
)
lgpPwrStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrStatisticsReset.setStatus("current")
_LgpPwrConfig_ObjectIdentity = ObjectIdentity
lgpPwrConfig = _LgpPwrConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9)
)
if mibBuilder.loadTexts:
    lgpPwrConfig.setStatus("current")
_LgpPwrSysCapacity_Type = Integer32
_LgpPwrSysCapacity_Object = MibScalar
lgpPwrSysCapacity = _LgpPwrSysCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 1),
    _LgpPwrSysCapacity_Type()
)
lgpPwrSysCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrSysCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrSysCapacity.setUnits("Volt-Amp")


class _LgpPwrUPSModuleMode_Type(Integer32):
    """Custom type lgpPwrUPSModuleMode based on Integer32"""
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
        *(("single", 1),
          ("parallel", 2),
          ("hotmaster", 3),
          ("hotslave", 4))
    )


_LgpPwrUPSModuleMode_Type.__name__ = "Integer32"
_LgpPwrUPSModuleMode_Object = MibScalar
lgpPwrUPSModuleMode = _LgpPwrUPSModuleMode_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 2),
    _LgpPwrUPSModuleMode_Type()
)
lgpPwrUPSModuleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPwrUPSModuleMode.setStatus("current")
_LgpPwrMaxRatedCurrent_Type = Integer32
_LgpPwrMaxRatedCurrent_Object = MibScalar
lgpPwrMaxRatedCurrent = _LgpPwrMaxRatedCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 3),
    _LgpPwrMaxRatedCurrent_Type()
)
lgpPwrMaxRatedCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrMaxRatedCurrent.setStatus("current")
if mibBuilder.loadTexts:
    lgpPwrMaxRatedCurrent.setUnits("Amp")


class _LgpPwrRectifierPulseCount_Type(Integer32):
    """Custom type lgpPwrRectifierPulseCount based on Integer32"""
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
        *(("sixPulse", 1),
          ("twelvePulse", 2),
          ("eighteenPulse", 3),
          ("twentyFourPulse", 4))
    )


_LgpPwrRectifierPulseCount_Type.__name__ = "Integer32"
_LgpPwrRectifierPulseCount_Object = MibScalar
lgpPwrRectifierPulseCount = _LgpPwrRectifierPulseCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 5, 9, 4),
    _LgpPwrRectifierPulseCount_Type()
)
lgpPwrRectifierPulseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPwrRectifierPulseCount.setStatus("current")
_LgpController_ObjectIdentity = ObjectIdentity
lgpController = _LgpController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6)
)
if mibBuilder.loadTexts:
    lgpController.setStatus("current")
_LgpCtrlNumberInstalledControlModules_Type = Integer32
_LgpCtrlNumberInstalledControlModules_Object = MibScalar
lgpCtrlNumberInstalledControlModules = _LgpCtrlNumberInstalledControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 1),
    _LgpCtrlNumberInstalledControlModules_Type()
)
lgpCtrlNumberInstalledControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberInstalledControlModules.setStatus("current")
_LgpCtrlNumberFailedControlModules_Type = Integer32
_LgpCtrlNumberFailedControlModules_Object = MibScalar
lgpCtrlNumberFailedControlModules = _LgpCtrlNumberFailedControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 2),
    _LgpCtrlNumberFailedControlModules_Type()
)
lgpCtrlNumberFailedControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberFailedControlModules.setStatus("current")
_LgpCtrlNumberRedundantControlModules_Type = Integer32
_LgpCtrlNumberRedundantControlModules_Object = MibScalar
lgpCtrlNumberRedundantControlModules = _LgpCtrlNumberRedundantControlModules_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 3),
    _LgpCtrlNumberRedundantControlModules_Type()
)
lgpCtrlNumberRedundantControlModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberRedundantControlModules.setStatus("current")
_LgpCtrlNumberControlModuleWarnings_Type = Integer32
_LgpCtrlNumberControlModuleWarnings_Object = MibScalar
lgpCtrlNumberControlModuleWarnings = _LgpCtrlNumberControlModuleWarnings_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 5),
    _LgpCtrlNumberControlModuleWarnings_Type()
)
lgpCtrlNumberControlModuleWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlNumberControlModuleWarnings.setStatus("current")
_LgpCtrlBoardBatteryVoltage_Type = Unsigned32
_LgpCtrlBoardBatteryVoltage_Object = MibScalar
lgpCtrlBoardBatteryVoltage = _LgpCtrlBoardBatteryVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 6, 6),
    _LgpCtrlBoardBatteryVoltage_Type()
)
lgpCtrlBoardBatteryVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpCtrlBoardBatteryVoltage.setStatus("current")
if mibBuilder.loadTexts:
    lgpCtrlBoardBatteryVoltage.setUnits(".01 Volts")
_LgpSystem_ObjectIdentity = ObjectIdentity
lgpSystem = _LgpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7)
)
if mibBuilder.loadTexts:
    lgpSystem.setStatus("current")
_LgpSysStatistics_ObjectIdentity = ObjectIdentity
lgpSysStatistics = _LgpSysStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1)
)
if mibBuilder.loadTexts:
    lgpSysStatistics.setStatus("current")
_LgpSysStatisticsRunHrs_Type = Unsigned32
_LgpSysStatisticsRunHrs_Object = MibScalar
lgpSysStatisticsRunHrs = _LgpSysStatisticsRunHrs_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1, 1),
    _LgpSysStatisticsRunHrs_Type()
)
lgpSysStatisticsRunHrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysStatisticsRunHrs.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysStatisticsRunHrs.setUnits("hours")
_LgpSysStatus_ObjectIdentity = ObjectIdentity
lgpSysStatus = _LgpSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2)
)
if mibBuilder.loadTexts:
    lgpSysStatus.setStatus("current")


class _LgpSysSelfTestResult_Type(Integer32):
    """Custom type lgpSysSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("sysFailure", 5),
          ("inhibited", 6))
    )


_LgpSysSelfTestResult_Type.__name__ = "Integer32"
_LgpSysSelfTestResult_Object = MibScalar
lgpSysSelfTestResult = _LgpSysSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 1),
    _LgpSysSelfTestResult_Type()
)
lgpSysSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysSelfTestResult.setStatus("current")


class _LgpSysState_Type(Integer32):
    """Custom type lgpSysState based on Integer32"""
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
        *(("normalOperation", 1),
          ("startUp", 2),
          ("normalWithWarning", 3),
          ("normalWithAlarm", 4),
          ("abnormalOperation", 5))
    )


_LgpSysState_Type.__name__ = "Integer32"
_LgpSysState_Object = MibScalar
lgpSysState = _LgpSysState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 2),
    _LgpSysState_Type()
)
lgpSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysState.setStatus("current")
_LgpSysSettings_ObjectIdentity = ObjectIdentity
lgpSysSettings = _LgpSysSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3)
)
if mibBuilder.loadTexts:
    lgpSysSettings.setStatus("current")


class _LgpSysAudibleAlarm_Type(Integer32):
    """Custom type lgpSysAudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpSysAudibleAlarm_Type.__name__ = "Integer32"
_LgpSysAudibleAlarm_Object = MibScalar
lgpSysAudibleAlarm = _LgpSysAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3, 1),
    _LgpSysAudibleAlarm_Type()
)
lgpSysAudibleAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysAudibleAlarm.setStatus("current")
_LgpSysControl_ObjectIdentity = ObjectIdentity
lgpSysControl = _LgpSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4)
)
if mibBuilder.loadTexts:
    lgpSysControl.setStatus("current")
_LgpSysSelfTest_Type = Integer32
_LgpSysSelfTest_Object = MibScalar
lgpSysSelfTest = _LgpSysSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 1),
    _LgpSysSelfTest_Type()
)
lgpSysSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysSelfTest.setStatus("current")


class _LgpSysControlOperationOnOff_Type(Integer32):
    """Custom type lgpSysControlOperationOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_LgpSysControlOperationOnOff_Type.__name__ = "Integer32"
_LgpSysControlOperationOnOff_Object = MibScalar
lgpSysControlOperationOnOff = _LgpSysControlOperationOnOff_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 2),
    _LgpSysControlOperationOnOff_Type()
)
lgpSysControlOperationOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysControlOperationOnOff.setStatus("current")
_LgpSysTime_ObjectIdentity = ObjectIdentity
lgpSysTime = _LgpSysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5)
)
if mibBuilder.loadTexts:
    lgpSysTime.setStatus("current")
_LgpSysTimeEpoch_Type = Unsigned32
_LgpSysTimeEpoch_Object = MibScalar
lgpSysTimeEpoch = _LgpSysTimeEpoch_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5, 1),
    _LgpSysTimeEpoch_Type()
)
lgpSysTimeEpoch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpSysTimeEpoch.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysTimeEpoch.setUnits("seconds")
_LgpSysMaintenance_ObjectIdentity = ObjectIdentity
lgpSysMaintenance = _LgpSysMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6)
)
if mibBuilder.loadTexts:
    lgpSysMaintenance.setStatus("current")
_LgpSysMaintenanceCapacity_Type = Unsigned32
_LgpSysMaintenanceCapacity_Object = MibScalar
lgpSysMaintenanceCapacity = _LgpSysMaintenanceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 1),
    _LgpSysMaintenanceCapacity_Type()
)
lgpSysMaintenanceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysMaintenanceCapacity.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysMaintenanceCapacity.setUnits("percent")
_LgpSysMaintenanceYear_Type = Unsigned32
_LgpSysMaintenanceYear_Object = MibScalar
lgpSysMaintenanceYear = _LgpSysMaintenanceYear_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 2),
    _LgpSysMaintenanceYear_Type()
)
lgpSysMaintenanceYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysMaintenanceYear.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysMaintenanceYear.setUnits("year")
_LgpSysMaintenanceMonth_Type = Unsigned32
_LgpSysMaintenanceMonth_Object = MibScalar
lgpSysMaintenanceMonth = _LgpSysMaintenanceMonth_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 3),
    _LgpSysMaintenanceMonth_Type()
)
lgpSysMaintenanceMonth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysMaintenanceMonth.setStatus("current")
if mibBuilder.loadTexts:
    lgpSysMaintenanceMonth.setUnits("month")


class _LgpSysEventDescription_Type(DisplayString):
    """Custom type lgpSysEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpSysEventDescription_Type.__name__ = "DisplayString"
_LgpSysEventDescription_Object = MibScalar
lgpSysEventDescription = _LgpSysEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 7),
    _LgpSysEventDescription_Type()
)
lgpSysEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysEventDescription.setStatus("current")
_LgpSysEventNotifications_ObjectIdentity = ObjectIdentity
lgpSysEventNotifications = _LgpSysEventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8)
)
if mibBuilder.loadTexts:
    lgpSysEventNotifications.setStatus("current")
_LgpSysDeviceComponentGroup_ObjectIdentity = ObjectIdentity
lgpSysDeviceComponentGroup = _LgpSysDeviceComponentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9)
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentGroup.setStatus("current")
_LgpSysDeviceComponentTable_Object = MibTable
lgpSysDeviceComponentTable = _LgpSysDeviceComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1)
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentTable.setStatus("current")
_LgpSysDeviceComponentEntry_Object = MibTableRow
lgpSysDeviceComponentEntry = _LgpSysDeviceComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1)
)
lgpSysDeviceComponentEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpAgentDeviceIndex"),
    (0, "LIEBERT-GP-MIB", "lgpSysDeviceComponentIndex"),
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentEntry.setStatus("current")
_LgpSysDeviceComponentIndex_Type = Unsigned32
_LgpSysDeviceComponentIndex_Object = MibTableColumn
lgpSysDeviceComponentIndex = _LgpSysDeviceComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 1),
    _LgpSysDeviceComponentIndex_Type()
)
lgpSysDeviceComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentIndex.setStatus("current")
_LgpSysDeviceComponentDescr_Type = ObjectIdentifier
_LgpSysDeviceComponentDescr_Object = MibTableColumn
lgpSysDeviceComponentDescr = _LgpSysDeviceComponentDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 2),
    _LgpSysDeviceComponentDescr_Type()
)
lgpSysDeviceComponentDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentDescr.setStatus("current")


class _LgpSysDeviceComponentSerialNum_Type(DisplayString):
    """Custom type lgpSysDeviceComponentSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpSysDeviceComponentSerialNum_Type.__name__ = "DisplayString"
_LgpSysDeviceComponentSerialNum_Object = MibTableColumn
lgpSysDeviceComponentSerialNum = _LgpSysDeviceComponentSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 3),
    _LgpSysDeviceComponentSerialNum_Type()
)
lgpSysDeviceComponentSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentSerialNum.setStatus("current")


class _LgpSysDeviceComponentModelNum_Type(DisplayString):
    """Custom type lgpSysDeviceComponentModelNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LgpSysDeviceComponentModelNum_Type.__name__ = "DisplayString"
_LgpSysDeviceComponentModelNum_Object = MibTableColumn
lgpSysDeviceComponentModelNum = _LgpSysDeviceComponentModelNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 4),
    _LgpSysDeviceComponentModelNum_Type()
)
lgpSysDeviceComponentModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpSysDeviceComponentModelNum.setStatus("current")
_LgpSysDeviceComponentWellknown_ObjectIdentity = ObjectIdentity
lgpSysDeviceComponentWellknown = _LgpSysDeviceComponentWellknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5)
)
if mibBuilder.loadTexts:
    lgpSysDeviceComponentWellknown.setStatus("current")
_LgpSysDeviceBatCabinet_ObjectIdentity = ObjectIdentity
lgpSysDeviceBatCabinet = _LgpSysDeviceBatCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 5)
)
if mibBuilder.loadTexts:
    lgpSysDeviceBatCabinet.setStatus("current")
_LgpSysDeviceParallelCabinet_ObjectIdentity = ObjectIdentity
lgpSysDeviceParallelCabinet = _LgpSysDeviceParallelCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 6)
)
if mibBuilder.loadTexts:
    lgpSysDeviceParallelCabinet.setStatus("current")
_LgpSysDeviceMaintBypass_ObjectIdentity = ObjectIdentity
lgpSysDeviceMaintBypass = _LgpSysDeviceMaintBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 7)
)
if mibBuilder.loadTexts:
    lgpSysDeviceMaintBypass.setStatus("current")
_LgpPdu_ObjectIdentity = ObjectIdentity
lgpPdu = _LgpPdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8)
)
if mibBuilder.loadTexts:
    lgpPdu.setStatus("current")
_LgpPduCluster_ObjectIdentity = ObjectIdentity
lgpPduCluster = _LgpPduCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 10)
)
if mibBuilder.loadTexts:
    lgpPduCluster.setStatus("current")
_LgpPduGrpSysStatus_Type = Unsigned32
_LgpPduGrpSysStatus_Object = MibScalar
lgpPduGrpSysStatus = _LgpPduGrpSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 10, 5),
    _LgpPduGrpSysStatus_Type()
)
lgpPduGrpSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduGrpSysStatus.setStatus("current")
_LgpPduTableCount_Type = Unsigned32
_LgpPduTableCount_Object = MibScalar
lgpPduTableCount = _LgpPduTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 19),
    _LgpPduTableCount_Type()
)
lgpPduTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduTableCount.setUnits("Count")
_LgpPduTable_Object = MibTable
lgpPduTable = _LgpPduTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20)
)
if mibBuilder.loadTexts:
    lgpPduTable.setStatus("current")
_LgpPduEntry_Object = MibTableRow
lgpPduEntry = _LgpPduEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1)
)
lgpPduEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduEntry.setStatus("current")
_LgpPduEntryIndex_Type = Unsigned32
_LgpPduEntryIndex_Object = MibTableColumn
lgpPduEntryIndex = _LgpPduEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 1),
    _LgpPduEntryIndex_Type()
)
lgpPduEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduEntryIndex.setStatus("current")
_LgpPduEntryId_Type = Unsigned32
_LgpPduEntryId_Object = MibTableColumn
lgpPduEntryId = _LgpPduEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 5),
    _LgpPduEntryId_Type()
)
lgpPduEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntryId.setStatus("current")
_LgpPduEntryUsrLabel_Type = DisplayString
_LgpPduEntryUsrLabel_Object = MibTableColumn
lgpPduEntryUsrLabel = _LgpPduEntryUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 10),
    _LgpPduEntryUsrLabel_Type()
)
lgpPduEntryUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduEntryUsrLabel.setStatus("current")
_LgpPduEntrySysAssignLabel_Type = DisplayString
_LgpPduEntrySysAssignLabel_Object = MibTableColumn
lgpPduEntrySysAssignLabel = _LgpPduEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 15),
    _LgpPduEntrySysAssignLabel_Type()
)
lgpPduEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntrySysAssignLabel.setStatus("current")
_LgpPduEntryPositionRelative_Type = Unsigned32
_LgpPduEntryPositionRelative_Object = MibTableColumn
lgpPduEntryPositionRelative = _LgpPduEntryPositionRelative_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 20),
    _LgpPduEntryPositionRelative_Type()
)
lgpPduEntryPositionRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntryPositionRelative.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduEntryPositionRelative.setUnits("Count")
_LgpPduEntrySysStatus_Type = Unsigned32
_LgpPduEntrySysStatus_Object = MibTableColumn
lgpPduEntrySysStatus = _LgpPduEntrySysStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 25),
    _LgpPduEntrySysStatus_Type()
)
lgpPduEntrySysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntrySysStatus.setStatus("current")
_LgpPduEntryUsrTag1_Type = DisplayString
_LgpPduEntryUsrTag1_Object = MibTableColumn
lgpPduEntryUsrTag1 = _LgpPduEntryUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 35),
    _LgpPduEntryUsrTag1_Type()
)
lgpPduEntryUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduEntryUsrTag1.setStatus("current")
_LgpPduEntryUsrTag2_Type = DisplayString
_LgpPduEntryUsrTag2_Object = MibTableColumn
lgpPduEntryUsrTag2 = _LgpPduEntryUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 40),
    _LgpPduEntryUsrTag2_Type()
)
lgpPduEntryUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduEntryUsrTag2.setStatus("current")
_LgpPduEntrySerialNumber_Type = DisplayString
_LgpPduEntrySerialNumber_Object = MibTableColumn
lgpPduEntrySerialNumber = _LgpPduEntrySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 45),
    _LgpPduEntrySerialNumber_Type()
)
lgpPduEntrySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntrySerialNumber.setStatus("current")
_LgpPduEntryRbCount_Type = Unsigned32
_LgpPduEntryRbCount_Object = MibTableColumn
lgpPduEntryRbCount = _LgpPduEntryRbCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 20, 1, 50),
    _LgpPduEntryRbCount_Type()
)
lgpPduEntryRbCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduEntryRbCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduEntryRbCount.setUnits("Count")
_LgpPduPowerSource_ObjectIdentity = ObjectIdentity
lgpPduPowerSource = _LgpPduPowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30)
)
if mibBuilder.loadTexts:
    lgpPduPowerSource.setStatus("current")
_LgpPduPsTableCount_Type = Unsigned32
_LgpPduPsTableCount_Object = MibScalar
lgpPduPsTableCount = _LgpPduPsTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 19),
    _LgpPduPsTableCount_Type()
)
lgpPduPsTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsTableCount.setUnits("Count")
_LgpPduPsTable_Object = MibTable
lgpPduPsTable = _LgpPduPsTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20)
)
if mibBuilder.loadTexts:
    lgpPduPsTable.setStatus("current")
_LgpPduPsEntry_Object = MibTableRow
lgpPduPsEntry = _LgpPduPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1)
)
lgpPduPsEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduPsEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduPsEntry.setStatus("current")
_LgpPduPsEntryIndex_Type = Unsigned32
_LgpPduPsEntryIndex_Object = MibTableColumn
lgpPduPsEntryIndex = _LgpPduPsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 5),
    _LgpPduPsEntryIndex_Type()
)
lgpPduPsEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduPsEntryIndex.setStatus("current")
_LgpPduPsEntryId_Type = Unsigned32
_LgpPduPsEntryId_Object = MibTableColumn
lgpPduPsEntryId = _LgpPduPsEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 10),
    _LgpPduPsEntryId_Type()
)
lgpPduPsEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryId.setStatus("current")
_LgpPduPsEntrySysAssignLabel_Type = DisplayString
_LgpPduPsEntrySysAssignLabel_Object = MibTableColumn
lgpPduPsEntrySysAssignLabel = _LgpPduPsEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 15),
    _LgpPduPsEntrySysAssignLabel_Type()
)
lgpPduPsEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntrySysAssignLabel.setStatus("current")
_LgpPduPsEntryModel_Type = DisplayString
_LgpPduPsEntryModel_Object = MibTableColumn
lgpPduPsEntryModel = _LgpPduPsEntryModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 20),
    _LgpPduPsEntryModel_Type()
)
lgpPduPsEntryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryModel.setStatus("current")


class _LgpPduPsEntryWiringType_Type(Integer32):
    """Custom type lgpPduPsEntryWiringType based on Integer32"""
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
        *(("not-specified", 0),
          ("single-phase-3-wire-L1-N-PE", 1),
          ("two-phase-3-wire-L1-L2-PE", 2),
          ("three-phase-4-wire-L1-L2-L3-PE", 3),
          ("three-phase-5-wire-L1-L2-L3-N-PE", 4),
          ("two-phase-4-wire-L1-L2-N-PE", 5))
    )


_LgpPduPsEntryWiringType_Type.__name__ = "Integer32"
_LgpPduPsEntryWiringType_Object = MibTableColumn
lgpPduPsEntryWiringType = _LgpPduPsEntryWiringType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 25),
    _LgpPduPsEntryWiringType_Type()
)
lgpPduPsEntryWiringType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryWiringType.setStatus("current")
_LgpPduPsEntryEpInputRated_Type = Unsigned32
_LgpPduPsEntryEpInputRated_Object = MibTableColumn
lgpPduPsEntryEpInputRated = _LgpPduPsEntryEpInputRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 30),
    _LgpPduPsEntryEpInputRated_Type()
)
lgpPduPsEntryEpInputRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryEpInputRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEpInputRated.setUnits("VoltRMS")
_LgpPduPsEntryEcInputRated_Type = Unsigned32
_LgpPduPsEntryEcInputRated_Object = MibTableColumn
lgpPduPsEntryEcInputRated = _LgpPduPsEntryEcInputRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 35),
    _LgpPduPsEntryEcInputRated_Type()
)
lgpPduPsEntryEcInputRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcInputRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcInputRated.setUnits("0.1 Amp-AC-RMS")
_LgpPduPsEntryFreqRated_Type = Unsigned32
_LgpPduPsEntryFreqRated_Object = MibTableColumn
lgpPduPsEntryFreqRated = _LgpPduPsEntryFreqRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 40),
    _LgpPduPsEntryFreqRated_Type()
)
lgpPduPsEntryFreqRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryFreqRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryFreqRated.setUnits("Hertz")
_LgpPduPsEntryEnergyAccum_Type = Unsigned32
_LgpPduPsEntryEnergyAccum_Object = MibTableColumn
lgpPduPsEntryEnergyAccum = _LgpPduPsEntryEnergyAccum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 50),
    _LgpPduPsEntryEnergyAccum_Type()
)
lgpPduPsEntryEnergyAccum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryEnergyAccum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEnergyAccum.setUnits("0.1 Kilowatt-Hour")
_LgpPduPsEntrySerialNum_Type = DisplayString
_LgpPduPsEntrySerialNum_Object = MibTableColumn
lgpPduPsEntrySerialNum = _LgpPduPsEntrySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 55),
    _LgpPduPsEntrySerialNum_Type()
)
lgpPduPsEntrySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntrySerialNum.setStatus("current")
_LgpPduPsEntryFirmwareVersion_Type = DisplayString
_LgpPduPsEntryFirmwareVersion_Object = MibTableColumn
lgpPduPsEntryFirmwareVersion = _LgpPduPsEntryFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 60),
    _LgpPduPsEntryFirmwareVersion_Type()
)
lgpPduPsEntryFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryFirmwareVersion.setStatus("current")
_LgpPduPsEntryPwrTotal_Type = Unsigned32
_LgpPduPsEntryPwrTotal_Object = MibTableColumn
lgpPduPsEntryPwrTotal = _LgpPduPsEntryPwrTotal_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 65),
    _LgpPduPsEntryPwrTotal_Type()
)
lgpPduPsEntryPwrTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryPwrTotal.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryPwrTotal.setUnits("Watt")
_LgpPduPsEntryEcNeutral_Type = Unsigned32
_LgpPduPsEntryEcNeutral_Object = MibTableColumn
lgpPduPsEntryEcNeutral = _LgpPduPsEntryEcNeutral_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 70),
    _LgpPduPsEntryEcNeutral_Type()
)
lgpPduPsEntryEcNeutral.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutral.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutral.setUnits("0.1 Amp-AC-RMS")
_LgpPduPsEntryEcNeutralThrshldOvrWarn_Type = Unsigned32
_LgpPduPsEntryEcNeutralThrshldOvrWarn_Object = MibTableColumn
lgpPduPsEntryEcNeutralThrshldOvrWarn = _LgpPduPsEntryEcNeutralThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 75),
    _LgpPduPsEntryEcNeutralThrshldOvrWarn_Type()
)
lgpPduPsEntryEcNeutralThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrWarn.setUnits("Percent")
_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Type = Unsigned32
_LgpPduPsEntryEcNeutralThrshldOvrAlarm_Object = MibTableColumn
lgpPduPsEntryEcNeutralThrshldOvrAlarm = _LgpPduPsEntryEcNeutralThrshldOvrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 20, 1, 80),
    _LgpPduPsEntryEcNeutralThrshldOvrAlarm_Type()
)
lgpPduPsEntryEcNeutralThrshldOvrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsEntryEcNeutralThrshldOvrAlarm.setUnits("Percent")
_LgpPduPsLineTable_Object = MibTable
lgpPduPsLineTable = _LgpPduPsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40)
)
if mibBuilder.loadTexts:
    lgpPduPsLineTable.setStatus("current")
_LgpPduPsLineEntry_Object = MibTableRow
lgpPduPsLineEntry = _LgpPduPsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1)
)
lgpPduPsLineEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduPsEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduPsLineEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduPsLineEntry.setStatus("current")
_LgpPduPsLineEntryIndex_Type = Unsigned32
_LgpPduPsLineEntryIndex_Object = MibTableColumn
lgpPduPsLineEntryIndex = _LgpPduPsLineEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 5),
    _LgpPduPsLineEntryIndex_Type()
)
lgpPduPsLineEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryIndex.setStatus("current")
_LgpPduPsLineEntryId_Type = Unsigned32
_LgpPduPsLineEntryId_Object = MibTableColumn
lgpPduPsLineEntryId = _LgpPduPsLineEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 10),
    _LgpPduPsLineEntryId_Type()
)
lgpPduPsLineEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryId.setStatus("current")


class _LgpPduPsLineEntryLine_Type(Integer32):
    """Custom type lgpPduPsLineEntryLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_LgpPduPsLineEntryLine_Type.__name__ = "Integer32"
_LgpPduPsLineEntryLine_Object = MibTableColumn
lgpPduPsLineEntryLine = _LgpPduPsLineEntryLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 15),
    _LgpPduPsLineEntryLine_Type()
)
lgpPduPsLineEntryLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryLine.setStatus("current")
_LgpPduPsLineEntryEpLNTenths_Type = Unsigned32
_LgpPduPsLineEntryEpLNTenths_Object = MibTableColumn
lgpPduPsLineEntryEpLNTenths = _LgpPduPsLineEntryEpLNTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 19),
    _LgpPduPsLineEntryEpLNTenths_Type()
)
lgpPduPsLineEntryEpLNTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLNTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLNTenths.setUnits("0.1 Volts-AC-RMS")
_LgpPduPsLineEntryEpLN_Type = Unsigned32
_LgpPduPsLineEntryEpLN_Object = MibTableColumn
lgpPduPsLineEntryEpLN = _LgpPduPsLineEntryEpLN_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 20),
    _LgpPduPsLineEntryEpLN_Type()
)
lgpPduPsLineEntryEpLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLN.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLN.setUnits("Volts-AC-RMS")
_LgpPduPsLineEntryEc_Type = Unsigned32
_LgpPduPsLineEntryEc_Object = MibTableColumn
lgpPduPsLineEntryEc = _LgpPduPsLineEntryEc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 21),
    _LgpPduPsLineEntryEc_Type()
)
lgpPduPsLineEntryEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEc.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEc.setUnits("0.1 Amps-AC-RMS")
_LgpPduPsLineEntryEcHundredths_Type = Unsigned32
_LgpPduPsLineEntryEcHundredths_Object = MibTableColumn
lgpPduPsLineEntryEcHundredths = _LgpPduPsLineEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 22),
    _LgpPduPsLineEntryEcHundredths_Type()
)
lgpPduPsLineEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduPsLineEntryEcThrshldUndrAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcThrshldUndrAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcThrshldUndrAlarm = _LgpPduPsLineEntryEcThrshldUndrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 35),
    _LgpPduPsLineEntryEcThrshldUndrAlarm_Type()
)
lgpPduPsLineEntryEcThrshldUndrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldUndrAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldUndrAlarm.setUnits("Percent")
_LgpPduPsLineEntryEcThrshldOvrWarn_Type = Unsigned32
_LgpPduPsLineEntryEcThrshldOvrWarn_Object = MibTableColumn
lgpPduPsLineEntryEcThrshldOvrWarn = _LgpPduPsLineEntryEcThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 36),
    _LgpPduPsLineEntryEcThrshldOvrWarn_Type()
)
lgpPduPsLineEntryEcThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrWarn.setUnits("Percent")
_LgpPduPsLineEntryEcThrshldOvrAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcThrshldOvrAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcThrshldOvrAlarm = _LgpPduPsLineEntryEcThrshldOvrAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 37),
    _LgpPduPsLineEntryEcThrshldOvrAlarm_Type()
)
lgpPduPsLineEntryEcThrshldOvrAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcThrshldOvrAlarm.setUnits("Percent")
_LgpPduPsLineEntryEcAvailBeforeAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcAvailBeforeAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcAvailBeforeAlarm = _LgpPduPsLineEntryEcAvailBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 38),
    _LgpPduPsLineEntryEcAvailBeforeAlarm_Type()
)
lgpPduPsLineEntryEcAvailBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarm.setUnits("0.1 Amps-AC-RMS")
_LgpPduPsLineEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduPsLineEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduPsLineEntryEcUsedBeforeAlarm = _LgpPduPsLineEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 39),
    _LgpPduPsLineEntryEcUsedBeforeAlarm_Type()
)
lgpPduPsLineEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcUsedBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduPsLineEntryEpLL_Type = Unsigned32
_LgpPduPsLineEntryEpLL_Object = MibTableColumn
lgpPduPsLineEntryEpLL = _LgpPduPsLineEntryEpLL_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 60),
    _LgpPduPsLineEntryEpLL_Type()
)
lgpPduPsLineEntryEpLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLL.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLL.setUnits("Volts-AC-RMS")
_LgpPduPsLineEntryEpLLTenths_Type = Unsigned32
_LgpPduPsLineEntryEpLLTenths_Object = MibTableColumn
lgpPduPsLineEntryEpLLTenths = _LgpPduPsLineEntryEpLLTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 61),
    _LgpPduPsLineEntryEpLLTenths_Type()
)
lgpPduPsLineEntryEpLLTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLLTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEpLLTenths.setUnits("0.1 Volts-AC-RMS")
_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduPsLineEntryEcAvailBeforeAlarmHundredths = _LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 30, 40, 1, 62),
    _LgpPduPsLineEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduPsLineEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduReceptacleBranch_ObjectIdentity = ObjectIdentity
lgpPduReceptacleBranch = _LgpPduReceptacleBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40)
)
if mibBuilder.loadTexts:
    lgpPduReceptacleBranch.setStatus("current")
_LgpPduRbTableCount_Type = Unsigned32
_LgpPduRbTableCount_Object = MibScalar
lgpPduRbTableCount = _LgpPduRbTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 19),
    _LgpPduRbTableCount_Type()
)
lgpPduRbTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbTableCount.setUnits("Count")
_LgpPduRbTable_Object = MibTable
lgpPduRbTable = _LgpPduRbTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20)
)
if mibBuilder.loadTexts:
    lgpPduRbTable.setStatus("current")
_LgpPduRbEntry_Object = MibTableRow
lgpPduRbEntry = _LgpPduRbEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1)
)
lgpPduRbEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduRbEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduRbEntry.setStatus("current")
_LgpPduRbEntryIndex_Type = Unsigned32
_LgpPduRbEntryIndex_Object = MibTableColumn
lgpPduRbEntryIndex = _LgpPduRbEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 1),
    _LgpPduRbEntryIndex_Type()
)
lgpPduRbEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduRbEntryIndex.setStatus("current")
_LgpPduRbEntryId_Type = Unsigned32
_LgpPduRbEntryId_Object = MibTableColumn
lgpPduRbEntryId = _LgpPduRbEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 5),
    _LgpPduRbEntryId_Type()
)
lgpPduRbEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryId.setStatus("current")
_LgpPduRbEntryUsrLabel_Type = DisplayString
_LgpPduRbEntryUsrLabel_Object = MibTableColumn
lgpPduRbEntryUsrLabel = _LgpPduRbEntryUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 8),
    _LgpPduRbEntryUsrLabel_Type()
)
lgpPduRbEntryUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryUsrLabel.setStatus("current")
_LgpPduRbEntrySysAssignLabel_Type = DisplayString
_LgpPduRbEntrySysAssignLabel_Object = MibTableColumn
lgpPduRbEntrySysAssignLabel = _LgpPduRbEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 20),
    _LgpPduRbEntrySysAssignLabel_Type()
)
lgpPduRbEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntrySysAssignLabel.setStatus("current")
_LgpPduRbEntryPositionRelative_Type = Unsigned32
_LgpPduRbEntryPositionRelative_Object = MibTableColumn
lgpPduRbEntryPositionRelative = _LgpPduRbEntryPositionRelative_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 25),
    _LgpPduRbEntryPositionRelative_Type()
)
lgpPduRbEntryPositionRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryPositionRelative.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryPositionRelative.setUnits("Count")
_LgpPduRbEntrySerialNum_Type = DisplayString
_LgpPduRbEntrySerialNum_Object = MibTableColumn
lgpPduRbEntrySerialNum = _LgpPduRbEntrySerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 30),
    _LgpPduRbEntrySerialNum_Type()
)
lgpPduRbEntrySerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntrySerialNum.setStatus("current")
_LgpPduRbEntryModel_Type = DisplayString
_LgpPduRbEntryModel_Object = MibTableColumn
lgpPduRbEntryModel = _LgpPduRbEntryModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 35),
    _LgpPduRbEntryModel_Type()
)
lgpPduRbEntryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryModel.setStatus("current")
_LgpPduRbEntryFirmwareVersion_Type = DisplayString
_LgpPduRbEntryFirmwareVersion_Object = MibTableColumn
lgpPduRbEntryFirmwareVersion = _LgpPduRbEntryFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 40),
    _LgpPduRbEntryFirmwareVersion_Type()
)
lgpPduRbEntryFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryFirmwareVersion.setStatus("current")
_LgpPduRbEntryUsrTag1_Type = DisplayString
_LgpPduRbEntryUsrTag1_Object = MibTableColumn
lgpPduRbEntryUsrTag1 = _LgpPduRbEntryUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 41),
    _LgpPduRbEntryUsrTag1_Type()
)
lgpPduRbEntryUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryUsrTag1.setStatus("current")
_LgpPduRbEntryUsrTag2_Type = DisplayString
_LgpPduRbEntryUsrTag2_Object = MibTableColumn
lgpPduRbEntryUsrTag2 = _LgpPduRbEntryUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 42),
    _LgpPduRbEntryUsrTag2_Type()
)
lgpPduRbEntryUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryUsrTag2.setStatus("current")


class _LgpPduRbEntryReceptacleType_Type(Integer32):
    """Custom type lgpPduRbEntryReceptacleType based on Integer32"""
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
        *(("not-specified", 0),
          ("nema-5-20R-20-Amp", 1),
          ("iec-C13-sheet-F-10-Amp", 2),
          ("iec-C19-sheet-J-16-Amp", 3),
          ("iec-C13-sheet-F-10-Amp-and-iec-C19-sheet-J-16-Amp", 4),
          ("nema-5-20R-20-Amp-and-iec-C13-sheet-F-10-Amp", 5),
          ("nema-5-20R-20-Amp-and-iec-C19-sheet-J-16-Amp", 6),
          ("cee-7-type-E-schuko", 7))
    )


_LgpPduRbEntryReceptacleType_Type.__name__ = "Integer32"
_LgpPduRbEntryReceptacleType_Object = MibTableColumn
lgpPduRbEntryReceptacleType = _LgpPduRbEntryReceptacleType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 45),
    _LgpPduRbEntryReceptacleType_Type()
)
lgpPduRbEntryReceptacleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryReceptacleType.setStatus("current")


class _LgpPduRbEntryCapabilities_Type(Integer32):
    """Custom type lgpPduRbEntryCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("no-optional-capabilities", 1),
          ("measurement-only", 2),
          ("measurement-and-control", 3),
          ("control-only", 4),
          ("current-measurement-only", 5),
          ("current-measurement-and-control", 6))
    )


_LgpPduRbEntryCapabilities_Type.__name__ = "Integer32"
_LgpPduRbEntryCapabilities_Object = MibTableColumn
lgpPduRbEntryCapabilities = _LgpPduRbEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 50),
    _LgpPduRbEntryCapabilities_Type()
)
lgpPduRbEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryCapabilities.setStatus("current")


class _LgpPduRbEntryLineSource_Type(Integer32):
    """Custom type lgpPduRbEntryLineSource based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("line-1-neutral", 1),
          ("line-2-neutral", 2),
          ("line-3-neutral", 3),
          ("line-1-line-2", 4),
          ("line-2-line-3", 5),
          ("line-3-line-1", 6),
          ("line-1-line-2-and-line-1-neutral", 7),
          ("line-2-line-3-and-line-2-neutral", 8),
          ("line-3-line-1-and-line-3-neutral", 9),
          ("unknown-line-neutral", 10),
          ("unknown-line-line", 11))
    )


_LgpPduRbEntryLineSource_Type.__name__ = "Integer32"
_LgpPduRbEntryLineSource_Object = MibTableColumn
lgpPduRbEntryLineSource = _LgpPduRbEntryLineSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 55),
    _LgpPduRbEntryLineSource_Type()
)
lgpPduRbEntryLineSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryLineSource.setStatus("current")
_LgpPduRbEntryRcpCount_Type = Unsigned32
_LgpPduRbEntryRcpCount_Object = MibTableColumn
lgpPduRbEntryRcpCount = _LgpPduRbEntryRcpCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 60),
    _LgpPduRbEntryRcpCount_Type()
)
lgpPduRbEntryRcpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryRcpCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryRcpCount.setUnits("Count")
_LgpPduRbEntryEpRated_Type = Unsigned32
_LgpPduRbEntryEpRated_Object = MibTableColumn
lgpPduRbEntryEpRated = _LgpPduRbEntryEpRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 70),
    _LgpPduRbEntryEpRated_Type()
)
lgpPduRbEntryEpRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpRated.setUnits("VoltRMS")
_LgpPduRbEntryEcRated_Type = Unsigned32
_LgpPduRbEntryEcRated_Object = MibTableColumn
lgpPduRbEntryEcRated = _LgpPduRbEntryEcRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 75),
    _LgpPduRbEntryEcRated_Type()
)
lgpPduRbEntryEcRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcRated.setUnits("0.1 Amp-AC-RMS")
_LgpPduRbEntryFreqRated_Type = Unsigned32
_LgpPduRbEntryFreqRated_Object = MibTableColumn
lgpPduRbEntryFreqRated = _LgpPduRbEntryFreqRated_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 80),
    _LgpPduRbEntryFreqRated_Type()
)
lgpPduRbEntryFreqRated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryFreqRated.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryFreqRated.setUnits("Hertz")
_LgpPduRbEntryEnergyAccum_Type = Unsigned32
_LgpPduRbEntryEnergyAccum_Object = MibTableColumn
lgpPduRbEntryEnergyAccum = _LgpPduRbEntryEnergyAccum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 85),
    _LgpPduRbEntryEnergyAccum_Type()
)
lgpPduRbEntryEnergyAccum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEnergyAccum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEnergyAccum.setUnits("0.1 Kilowatt-Hour")
_LgpPduRbEntryEpLNTenths_Type = Unsigned32
_LgpPduRbEntryEpLNTenths_Object = MibTableColumn
lgpPduRbEntryEpLNTenths = _LgpPduRbEntryEpLNTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 100),
    _LgpPduRbEntryEpLNTenths_Type()
)
lgpPduRbEntryEpLNTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLNTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLNTenths.setUnits("0.1 VoltRMS")
_LgpPduRbEntryPwr_Type = Unsigned32
_LgpPduRbEntryPwr_Object = MibTableColumn
lgpPduRbEntryPwr = _LgpPduRbEntryPwr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 115),
    _LgpPduRbEntryPwr_Type()
)
lgpPduRbEntryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryPwr.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryPwr.setUnits("Watt")
_LgpPduRbEntryAp_Type = Unsigned32
_LgpPduRbEntryAp_Object = MibTableColumn
lgpPduRbEntryAp = _LgpPduRbEntryAp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 120),
    _LgpPduRbEntryAp_Type()
)
lgpPduRbEntryAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryAp.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryAp.setUnits("VoltAmp")
_LgpPduRbEntryPf_Type = Integer32
_LgpPduRbEntryPf_Object = MibTableColumn
lgpPduRbEntryPf = _LgpPduRbEntryPf_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 125),
    _LgpPduRbEntryPf_Type()
)
lgpPduRbEntryPf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryPf.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryPf.setUnits("0.01 Power Factor")
_LgpPduRbEntryEcHundredths_Type = Unsigned32
_LgpPduRbEntryEcHundredths_Object = MibTableColumn
lgpPduRbEntryEcHundredths = _LgpPduRbEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 130),
    _LgpPduRbEntryEcHundredths_Type()
)
lgpPduRbEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcHundredths.setUnits("0.01 Amp-AC-RMS")
_LgpPduRbEntryEcThrshldUndrAlm_Type = Unsigned32
_LgpPduRbEntryEcThrshldUndrAlm_Object = MibTableColumn
lgpPduRbEntryEcThrshldUndrAlm = _LgpPduRbEntryEcThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 135),
    _LgpPduRbEntryEcThrshldUndrAlm_Type()
)
lgpPduRbEntryEcThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldUndrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldUndrAlm.setUnits("Percent")
_LgpPduRbEntryEcThrshldOvrWarn_Type = Unsigned32
_LgpPduRbEntryEcThrshldOvrWarn_Object = MibTableColumn
lgpPduRbEntryEcThrshldOvrWarn = _LgpPduRbEntryEcThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 140),
    _LgpPduRbEntryEcThrshldOvrWarn_Type()
)
lgpPduRbEntryEcThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrWarn.setUnits("Percent")
_LgpPduRbEntryEcThrshldOvrAlm_Type = Unsigned32
_LgpPduRbEntryEcThrshldOvrAlm_Object = MibTableColumn
lgpPduRbEntryEcThrshldOvrAlm = _LgpPduRbEntryEcThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 145),
    _LgpPduRbEntryEcThrshldOvrAlm_Type()
)
lgpPduRbEntryEcThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcThrshldOvrAlm.setUnits("Percent")
_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduRbEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduRbEntryEcAvailBeforeAlarmHundredths = _LgpPduRbEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 150),
    _LgpPduRbEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduRbEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcAvailBeforeAlarmHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduRbEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduRbEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduRbEntryEcUsedBeforeAlarm = _LgpPduRbEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 160),
    _LgpPduRbEntryEcUsedBeforeAlarm_Type()
)
lgpPduRbEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcUsedBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduRbEntryEpLLTenths_Type = Unsigned32
_LgpPduRbEntryEpLLTenths_Object = MibTableColumn
lgpPduRbEntryEpLLTenths = _LgpPduRbEntryEpLLTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 20, 1, 170),
    _LgpPduRbEntryEpLLTenths_Type()
)
lgpPduRbEntryEpLLTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLLTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRbEntryEpLLTenths.setUnits("0.1 VoltRMS")
_LgpPduRbLineTable_Object = MibTable
lgpPduRbLineTable = _LgpPduRbLineTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40)
)
if mibBuilder.loadTexts:
    lgpPduRbLineTable.setStatus("deprecated")
_LgpPduRbLineEntry_Object = MibTableRow
lgpPduRbLineEntry = _LgpPduRbLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1)
)
lgpPduRbLineEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduRbEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduRbLineEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduRbLineEntry.setStatus("deprecated")
_LgpPduRbLineEntryIndex_Type = Unsigned32
_LgpPduRbLineEntryIndex_Object = MibTableColumn
lgpPduRbLineEntryIndex = _LgpPduRbLineEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 1),
    _LgpPduRbLineEntryIndex_Type()
)
lgpPduRbLineEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryIndex.setStatus("deprecated")
_LgpPduRbLineEntryId_Type = Unsigned32
_LgpPduRbLineEntryId_Object = MibTableColumn
lgpPduRbLineEntryId = _LgpPduRbLineEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 5),
    _LgpPduRbLineEntryId_Type()
)
lgpPduRbLineEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryId.setStatus("deprecated")


class _LgpPduRbLineEntryLine_Type(Integer32):
    """Custom type lgpPduRbLineEntryLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("phase1", 1),
          ("phase2", 2),
          ("phase3", 3))
    )


_LgpPduRbLineEntryLine_Type.__name__ = "Integer32"
_LgpPduRbLineEntryLine_Object = MibTableColumn
lgpPduRbLineEntryLine = _LgpPduRbLineEntryLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 10),
    _LgpPduRbLineEntryLine_Type()
)
lgpPduRbLineEntryLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryLine.setStatus("deprecated")
_LgpPduRbLineEntryEpLNTenths_Type = Unsigned32
_LgpPduRbLineEntryEpLNTenths_Object = MibTableColumn
lgpPduRbLineEntryEpLNTenths = _LgpPduRbLineEntryEpLNTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 19),
    _LgpPduRbLineEntryEpLNTenths_Type()
)
lgpPduRbLineEntryEpLNTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLNTenths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLNTenths.setUnits("0.1 VoltRMS")
_LgpPduRbLineEntryEpLN_Type = Unsigned32
_LgpPduRbLineEntryEpLN_Object = MibTableColumn
lgpPduRbLineEntryEpLN = _LgpPduRbLineEntryEpLN_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 20),
    _LgpPduRbLineEntryEpLN_Type()
)
lgpPduRbLineEntryEpLN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLN.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLN.setUnits("VoltRMS")
_LgpPduRbLineEntryEc_Type = Unsigned32
_LgpPduRbLineEntryEc_Object = MibTableColumn
lgpPduRbLineEntryEc = _LgpPduRbLineEntryEc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 21),
    _LgpPduRbLineEntryEc_Type()
)
lgpPduRbLineEntryEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEc.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEc.setUnits("0.1 Amp-AC-RMS")
_LgpPduRbLineEntryPwr_Type = Unsigned32
_LgpPduRbLineEntryPwr_Object = MibTableColumn
lgpPduRbLineEntryPwr = _LgpPduRbLineEntryPwr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 22),
    _LgpPduRbLineEntryPwr_Type()
)
lgpPduRbLineEntryPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPwr.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPwr.setUnits("Watt")
_LgpPduRbLineEntryAp_Type = Unsigned32
_LgpPduRbLineEntryAp_Object = MibTableColumn
lgpPduRbLineEntryAp = _LgpPduRbLineEntryAp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 23),
    _LgpPduRbLineEntryAp_Type()
)
lgpPduRbLineEntryAp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryAp.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryAp.setUnits("VoltAmp")
_LgpPduRbLineEntryPf_Type = Integer32
_LgpPduRbLineEntryPf_Object = MibTableColumn
lgpPduRbLineEntryPf = _LgpPduRbLineEntryPf_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 24),
    _LgpPduRbLineEntryPf_Type()
)
lgpPduRbLineEntryPf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPf.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryPf.setUnits("0.01 Power Factor")
_LgpPduRbLineEntryEcHundredths_Type = Unsigned32
_LgpPduRbLineEntryEcHundredths_Object = MibTableColumn
lgpPduRbLineEntryEcHundredths = _LgpPduRbLineEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 25),
    _LgpPduRbLineEntryEcHundredths_Type()
)
lgpPduRbLineEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcHundredths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcHundredths.setUnits("0.01 Amp-AC-RMS")
_LgpPduRbLineEntryEcThrshldUndrAlm_Type = Unsigned32
_LgpPduRbLineEntryEcThrshldUndrAlm_Object = MibTableColumn
lgpPduRbLineEntryEcThrshldUndrAlm = _LgpPduRbLineEntryEcThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 35),
    _LgpPduRbLineEntryEcThrshldUndrAlm_Type()
)
lgpPduRbLineEntryEcThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldUndrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldUndrAlm.setUnits("Percent")
_LgpPduRbLineEntryEcThrshldOvrWarn_Type = Unsigned32
_LgpPduRbLineEntryEcThrshldOvrWarn_Object = MibTableColumn
lgpPduRbLineEntryEcThrshldOvrWarn = _LgpPduRbLineEntryEcThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 36),
    _LgpPduRbLineEntryEcThrshldOvrWarn_Type()
)
lgpPduRbLineEntryEcThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrWarn.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrWarn.setUnits("Percent")
_LgpPduRbLineEntryEcThrshldOvrAlm_Type = Unsigned32
_LgpPduRbLineEntryEcThrshldOvrAlm_Object = MibTableColumn
lgpPduRbLineEntryEcThrshldOvrAlm = _LgpPduRbLineEntryEcThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 37),
    _LgpPduRbLineEntryEcThrshldOvrAlm_Type()
)
lgpPduRbLineEntryEcThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcThrshldOvrAlm.setUnits("Percent")
_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduRbLineEntryEcAvailBeforeAlarmHundredths = _LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 39),
    _LgpPduRbLineEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduRbLineEntryEcAvailBeforeAlarm_Type = Unsigned32
_LgpPduRbLineEntryEcAvailBeforeAlarm_Object = MibTableColumn
lgpPduRbLineEntryEcAvailBeforeAlarm = _LgpPduRbLineEntryEcAvailBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 40),
    _LgpPduRbLineEntryEcAvailBeforeAlarm_Type()
)
lgpPduRbLineEntryEcAvailBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcAvailBeforeAlarm.setUnits("0.1 Amps-AC-RMS")
_LgpPduRbLineEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduRbLineEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduRbLineEntryEcUsedBeforeAlarm = _LgpPduRbLineEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 41),
    _LgpPduRbLineEntryEcUsedBeforeAlarm_Type()
)
lgpPduRbLineEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcUsedBeforeAlarm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduRbLineEntryEpLL_Type = Unsigned32
_LgpPduRbLineEntryEpLL_Object = MibTableColumn
lgpPduRbLineEntryEpLL = _LgpPduRbLineEntryEpLL_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 60),
    _LgpPduRbLineEntryEpLL_Type()
)
lgpPduRbLineEntryEpLL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLL.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLL.setUnits("VoltRMS")
_LgpPduRbLineEntryEpLLTenths_Type = Unsigned32
_LgpPduRbLineEntryEpLLTenths_Object = MibTableColumn
lgpPduRbLineEntryEpLLTenths = _LgpPduRbLineEntryEpLLTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 40, 40, 1, 61),
    _LgpPduRbLineEntryEpLLTenths_Type()
)
lgpPduRbLineEntryEpLLTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLLTenths.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduRbLineEntryEpLLTenths.setUnits("0.1 VoltRMS")
_LgpPduReceptacle_ObjectIdentity = ObjectIdentity
lgpPduReceptacle = _LgpPduReceptacle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50)
)
if mibBuilder.loadTexts:
    lgpPduReceptacle.setStatus("current")
_LgpPduRcpTableCount_Type = Unsigned32
_LgpPduRcpTableCount_Object = MibScalar
lgpPduRcpTableCount = _LgpPduRcpTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 19),
    _LgpPduRcpTableCount_Type()
)
lgpPduRcpTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpTableCount.setUnits("Count")
_LgpPduRcpTable_Object = MibTable
lgpPduRcpTable = _LgpPduRcpTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20)
)
if mibBuilder.loadTexts:
    lgpPduRcpTable.setStatus("current")
_LgpPduRcpEntry_Object = MibTableRow
lgpPduRcpEntry = _LgpPduRcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1)
)
lgpPduRcpEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduRbEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduRcpEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpPduRcpEntry.setStatus("current")
_LgpPduRcpEntryIndex_Type = Unsigned32
_LgpPduRcpEntryIndex_Object = MibTableColumn
lgpPduRcpEntryIndex = _LgpPduRcpEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 1),
    _LgpPduRcpEntryIndex_Type()
)
lgpPduRcpEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduRcpEntryIndex.setStatus("current")
_LgpPduRcpEntryId_Type = Unsigned32
_LgpPduRcpEntryId_Object = MibTableColumn
lgpPduRcpEntryId = _LgpPduRcpEntryId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 5),
    _LgpPduRcpEntryId_Type()
)
lgpPduRcpEntryId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryId.setStatus("current")
_LgpPduRcpEntryUsrLabel_Type = DisplayString
_LgpPduRcpEntryUsrLabel_Object = MibTableColumn
lgpPduRcpEntryUsrLabel = _LgpPduRcpEntryUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 10),
    _LgpPduRcpEntryUsrLabel_Type()
)
lgpPduRcpEntryUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryUsrLabel.setStatus("current")
_LgpPduRcpEntryUsrTag1_Type = DisplayString
_LgpPduRcpEntryUsrTag1_Object = MibTableColumn
lgpPduRcpEntryUsrTag1 = _LgpPduRcpEntryUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 15),
    _LgpPduRcpEntryUsrTag1_Type()
)
lgpPduRcpEntryUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryUsrTag1.setStatus("current")
_LgpPduRcpEntryUsrTag2_Type = DisplayString
_LgpPduRcpEntryUsrTag2_Object = MibTableColumn
lgpPduRcpEntryUsrTag2 = _LgpPduRcpEntryUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 20),
    _LgpPduRcpEntryUsrTag2_Type()
)
lgpPduRcpEntryUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryUsrTag2.setStatus("current")
_LgpPduRcpEntrySysAssignLabel_Type = DisplayString
_LgpPduRcpEntrySysAssignLabel_Object = MibTableColumn
lgpPduRcpEntrySysAssignLabel = _LgpPduRcpEntrySysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 25),
    _LgpPduRcpEntrySysAssignLabel_Type()
)
lgpPduRcpEntrySysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntrySysAssignLabel.setStatus("current")
_LgpPduRcpEntryPosition_Type = Unsigned32
_LgpPduRcpEntryPosition_Object = MibTableColumn
lgpPduRcpEntryPosition = _LgpPduRcpEntryPosition_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 30),
    _LgpPduRcpEntryPosition_Type()
)
lgpPduRcpEntryPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPosition.setStatus("current")


class _LgpPduRcpEntryType_Type(Integer32):
    """Custom type lgpPduRcpEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              7)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("nema-5-20R-20-Amp", 1),
          ("iec-C13-sheet-F-10-Amp", 2),
          ("iec-C19-sheet-J-16-Amp", 3),
          ("cee-7-type-E-schuko", 7))
    )


_LgpPduRcpEntryType_Type.__name__ = "Integer32"
_LgpPduRcpEntryType_Object = MibTableColumn
lgpPduRcpEntryType = _LgpPduRcpEntryType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 40),
    _LgpPduRcpEntryType_Type()
)
lgpPduRcpEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryType.setStatus("current")


class _LgpPduRcpEntryLineSource_Type(Integer32):
    """Custom type lgpPduRcpEntryLineSource based on Integer32"""
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
        *(("not-specified", 0),
          ("line-1-N", 1),
          ("line-2-N", 2),
          ("line-3-N", 3),
          ("line-1-line-2", 4),
          ("line-2-line-3", 5),
          ("line-3-line-1", 6),
          ("unknown-line-neutral", 7),
          ("unknown-line-line", 8))
    )


_LgpPduRcpEntryLineSource_Type.__name__ = "Integer32"
_LgpPduRcpEntryLineSource_Object = MibTableColumn
lgpPduRcpEntryLineSource = _LgpPduRcpEntryLineSource_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 45),
    _LgpPduRcpEntryLineSource_Type()
)
lgpPduRcpEntryLineSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryLineSource.setStatus("current")


class _LgpPduRcpEntryCapabilities_Type(Integer32):
    """Custom type lgpPduRcpEntryCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("no-optional-capabilities", 1),
          ("measurement-only", 2),
          ("measurement-and-control", 3),
          ("control-only", 4),
          ("current-measurement-only", 5),
          ("current-measurement-and-control", 6))
    )


_LgpPduRcpEntryCapabilities_Type.__name__ = "Integer32"
_LgpPduRcpEntryCapabilities_Object = MibTableColumn
lgpPduRcpEntryCapabilities = _LgpPduRcpEntryCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 50),
    _LgpPduRcpEntryCapabilities_Type()
)
lgpPduRcpEntryCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryCapabilities.setStatus("current")
_LgpPduRcpEntryEp_Type = Unsigned32
_LgpPduRcpEntryEp_Object = MibTableColumn
lgpPduRcpEntryEp = _LgpPduRcpEntryEp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 55),
    _LgpPduRcpEntryEp_Type()
)
lgpPduRcpEntryEp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEp.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEp.setUnits("Volts-AC-RMS")
_LgpPduRcpEntryEpTenths_Type = Unsigned32
_LgpPduRcpEntryEpTenths_Object = MibTableColumn
lgpPduRcpEntryEpTenths = _LgpPduRcpEntryEpTenths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 56),
    _LgpPduRcpEntryEpTenths_Type()
)
lgpPduRcpEntryEpTenths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEpTenths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEpTenths.setUnits("0.1 Volts-AC-RMS")
_LgpPduRcpEntryEc_Type = Unsigned32
_LgpPduRcpEntryEc_Object = MibTableColumn
lgpPduRcpEntryEc = _LgpPduRcpEntryEc_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 60),
    _LgpPduRcpEntryEc_Type()
)
lgpPduRcpEntryEc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEc.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEc.setUnits("0.1 Amp-AC-RMS")
_LgpPduRcpEntryEcHundredths_Type = Unsigned32
_LgpPduRcpEntryEcHundredths_Object = MibTableColumn
lgpPduRcpEntryEcHundredths = _LgpPduRcpEntryEcHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 61),
    _LgpPduRcpEntryEcHundredths_Type()
)
lgpPduRcpEntryEcHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcHundredths.setUnits("0.01 Amp-AC-RMS")
_LgpPduRcpEntryPwrOut_Type = Unsigned32
_LgpPduRcpEntryPwrOut_Object = MibTableColumn
lgpPduRcpEntryPwrOut = _LgpPduRcpEntryPwrOut_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 65),
    _LgpPduRcpEntryPwrOut_Type()
)
lgpPduRcpEntryPwrOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOut.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOut.setUnits("Watt")
_LgpPduRcpEntryApOut_Type = Unsigned32
_LgpPduRcpEntryApOut_Object = MibTableColumn
lgpPduRcpEntryApOut = _LgpPduRcpEntryApOut_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 70),
    _LgpPduRcpEntryApOut_Type()
)
lgpPduRcpEntryApOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryApOut.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryApOut.setUnits("Volt-Amp-RMS")
_LgpPduRcpEntryPf_Type = Unsigned32
_LgpPduRcpEntryPf_Object = MibTableColumn
lgpPduRcpEntryPf = _LgpPduRcpEntryPf_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 75),
    _LgpPduRcpEntryPf_Type()
)
lgpPduRcpEntryPf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPf.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPf.setUnits(".01 Power Factor")
_LgpPduRcpEntryFreq_Type = Unsigned32
_LgpPduRcpEntryFreq_Object = MibTableColumn
lgpPduRcpEntryFreq = _LgpPduRcpEntryFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 80),
    _LgpPduRcpEntryFreq_Type()
)
lgpPduRcpEntryFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryFreq.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryFreq.setUnits("0.1 Hertz")
_LgpPduRcpEntryEnergyAccum_Type = Unsigned32
_LgpPduRcpEntryEnergyAccum_Object = MibTableColumn
lgpPduRcpEntryEnergyAccum = _LgpPduRcpEntryEnergyAccum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 85),
    _LgpPduRcpEntryEnergyAccum_Type()
)
lgpPduRcpEntryEnergyAccum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEnergyAccum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEnergyAccum.setUnits("0.1 Kilowatt-Hour")
_LgpPduRcpEntryPwrOnDelay_Type = Unsigned32
_LgpPduRcpEntryPwrOnDelay_Object = MibTableColumn
lgpPduRcpEntryPwrOnDelay = _LgpPduRcpEntryPwrOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 90),
    _LgpPduRcpEntryPwrOnDelay_Type()
)
lgpPduRcpEntryPwrOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrOnDelay.setUnits("Seconds")


class _LgpPduRcpEntryPwrState_Type(Integer32):
    """Custom type lgpPduRcpEntryPwrState based on Integer32"""
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
        *(("unknown", 0),
          ("off", 1),
          ("on", 2),
          ("off-pending-on-delay", 3))
    )


_LgpPduRcpEntryPwrState_Type.__name__ = "Integer32"
_LgpPduRcpEntryPwrState_Object = MibTableColumn
lgpPduRcpEntryPwrState = _LgpPduRcpEntryPwrState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 95),
    _LgpPduRcpEntryPwrState_Type()
)
lgpPduRcpEntryPwrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryPwrState.setStatus("current")


class _LgpPduRcpEntryControl_Type(Integer32):
    """Custom type lgpPduRcpEntryControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("cycle-power", 2))
    )


_LgpPduRcpEntryControl_Type.__name__ = "Integer32"
_LgpPduRcpEntryControl_Object = MibTableColumn
lgpPduRcpEntryControl = _LgpPduRcpEntryControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 100),
    _LgpPduRcpEntryControl_Type()
)
lgpPduRcpEntryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryControl.setStatus("current")


class _LgpPduRcpEntryControlLock_Type(Integer32):
    """Custom type lgpPduRcpEntryControlLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("unlocked", 1),
          ("locked", 2))
    )


_LgpPduRcpEntryControlLock_Type.__name__ = "Integer32"
_LgpPduRcpEntryControlLock_Object = MibTableColumn
lgpPduRcpEntryControlLock = _LgpPduRcpEntryControlLock_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 105),
    _LgpPduRcpEntryControlLock_Type()
)
lgpPduRcpEntryControlLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryControlLock.setStatus("current")
_LgpPduRcpEntryEcThrshldUnderAlarm_Type = Unsigned32
_LgpPduRcpEntryEcThrshldUnderAlarm_Object = MibTableColumn
lgpPduRcpEntryEcThrshldUnderAlarm = _LgpPduRcpEntryEcThrshldUnderAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 150),
    _LgpPduRcpEntryEcThrshldUnderAlarm_Type()
)
lgpPduRcpEntryEcThrshldUnderAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldUnderAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldUnderAlarm.setUnits("Percent")
_LgpPduRcpEntryEcThrshldOverWarn_Type = Unsigned32
_LgpPduRcpEntryEcThrshldOverWarn_Object = MibTableColumn
lgpPduRcpEntryEcThrshldOverWarn = _LgpPduRcpEntryEcThrshldOverWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 151),
    _LgpPduRcpEntryEcThrshldOverWarn_Type()
)
lgpPduRcpEntryEcThrshldOverWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverWarn.setUnits("Percent")
_LgpPduRcpEntryEcThrshldOverAlarm_Type = Unsigned32
_LgpPduRcpEntryEcThrshldOverAlarm_Object = MibTableColumn
lgpPduRcpEntryEcThrshldOverAlarm = _LgpPduRcpEntryEcThrshldOverAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 152),
    _LgpPduRcpEntryEcThrshldOverAlarm_Type()
)
lgpPduRcpEntryEcThrshldOverAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcThrshldOverAlarm.setUnits("Percent")
_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Type = Unsigned32
_LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Object = MibTableColumn
lgpPduRcpEntryEcAvailBeforeAlarmHundredths = _LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 159),
    _LgpPduRcpEntryEcAvailBeforeAlarmHundredths_Type()
)
lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarmHundredths.setUnits("0.01 Amps-AC-RMS")
_LgpPduRcpEntryEcAvailBeforeAlarm_Type = Unsigned32
_LgpPduRcpEntryEcAvailBeforeAlarm_Object = MibTableColumn
lgpPduRcpEntryEcAvailBeforeAlarm = _LgpPduRcpEntryEcAvailBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 160),
    _LgpPduRcpEntryEcAvailBeforeAlarm_Type()
)
lgpPduRcpEntryEcAvailBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcAvailBeforeAlarm.setUnits("0.1 Amps-AC-RMS")
_LgpPduRcpEntryEcUsedBeforeAlarm_Type = Unsigned32
_LgpPduRcpEntryEcUsedBeforeAlarm_Object = MibTableColumn
lgpPduRcpEntryEcUsedBeforeAlarm = _LgpPduRcpEntryEcUsedBeforeAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 161),
    _LgpPduRcpEntryEcUsedBeforeAlarm_Type()
)
lgpPduRcpEntryEcUsedBeforeAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcUsedBeforeAlarm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcUsedBeforeAlarm.setUnits("0.1 Percent")
_LgpPduRcpEntryEcCrestFactor_Type = Unsigned32
_LgpPduRcpEntryEcCrestFactor_Object = MibTableColumn
lgpPduRcpEntryEcCrestFactor = _LgpPduRcpEntryEcCrestFactor_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 162),
    _LgpPduRcpEntryEcCrestFactor_Type()
)
lgpPduRcpEntryEcCrestFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcCrestFactor.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduRcpEntryEcCrestFactor.setUnits("0.01")


class _LgpPduRcpEntryBlinkLED_Type(Integer32):
    """Custom type lgpPduRcpEntryBlinkLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("blinkLED", 2))
    )


_LgpPduRcpEntryBlinkLED_Type.__name__ = "Integer32"
_LgpPduRcpEntryBlinkLED_Object = MibTableColumn
lgpPduRcpEntryBlinkLED = _LgpPduRcpEntryBlinkLED_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 50, 20, 1, 200),
    _LgpPduRcpEntryBlinkLED_Type()
)
lgpPduRcpEntryBlinkLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduRcpEntryBlinkLED.setStatus("current")
_LgpPduAuxiliarySensors_ObjectIdentity = ObjectIdentity
lgpPduAuxiliarySensors = _LgpPduAuxiliarySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60)
)
if mibBuilder.loadTexts:
    lgpPduAuxiliarySensors.setStatus("current")
_LgpPduAuxSensorCount_Type = Unsigned32
_LgpPduAuxSensorCount_Object = MibScalar
lgpPduAuxSensorCount = _LgpPduAuxSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 5),
    _LgpPduAuxSensorCount_Type()
)
lgpPduAuxSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxSensorCount.setUnits("Count")
_LgpPduAuxSensorTable_Object = MibTable
lgpPduAuxSensorTable = _LgpPduAuxSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10)
)
if mibBuilder.loadTexts:
    lgpPduAuxSensorTable.setStatus("deprecated")
_LgpPduAuxSensorEntry_Object = MibTableRow
lgpPduAuxSensorEntry = _LgpPduAuxSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1)
)
lgpPduAuxSensorEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduAuxSensorIndex"),
)
if mibBuilder.loadTexts:
    lgpPduAuxSensorEntry.setStatus("deprecated")
_LgpPduAuxSensorIndex_Type = Unsigned32
_LgpPduAuxSensorIndex_Object = MibTableColumn
lgpPduAuxSensorIndex = _LgpPduAuxSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 1),
    _LgpPduAuxSensorIndex_Type()
)
lgpPduAuxSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduAuxSensorIndex.setStatus("deprecated")


class _LgpPduAuxSensorMeasType_Type(Integer32):
    """Custom type lgpPduAuxSensorMeasType based on Integer32"""
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
        *(("not-specified", 0),
          ("temperature", 1),
          ("humidity", 2),
          ("temperature-and-humidity", 3))
    )


_LgpPduAuxSensorMeasType_Type.__name__ = "Integer32"
_LgpPduAuxSensorMeasType_Object = MibTableColumn
lgpPduAuxSensorMeasType = _LgpPduAuxSensorMeasType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 5),
    _LgpPduAuxSensorMeasType_Type()
)
lgpPduAuxSensorMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorMeasType.setStatus("deprecated")
_LgpPduAuxSensorId_Type = Unsigned32
_LgpPduAuxSensorId_Object = MibTableColumn
lgpPduAuxSensorId = _LgpPduAuxSensorId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 10),
    _LgpPduAuxSensorId_Type()
)
lgpPduAuxSensorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorId.setStatus("deprecated")
_LgpPduAuxSensorSysAssignLabel_Type = DisplayString
_LgpPduAuxSensorSysAssignLabel_Object = MibTableColumn
lgpPduAuxSensorSysAssignLabel = _LgpPduAuxSensorSysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 15),
    _LgpPduAuxSensorSysAssignLabel_Type()
)
lgpPduAuxSensorSysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorSysAssignLabel.setStatus("deprecated")
_LgpPduAuxSensorPositionRelative_Type = Unsigned32
_LgpPduAuxSensorPositionRelative_Object = MibTableColumn
lgpPduAuxSensorPositionRelative = _LgpPduAuxSensorPositionRelative_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 20),
    _LgpPduAuxSensorPositionRelative_Type()
)
lgpPduAuxSensorPositionRelative.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorPositionRelative.setStatus("deprecated")
_LgpPduAuxSensorUsrLabel_Type = DisplayString
_LgpPduAuxSensorUsrLabel_Object = MibTableColumn
lgpPduAuxSensorUsrLabel = _LgpPduAuxSensorUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 25),
    _LgpPduAuxSensorUsrLabel_Type()
)
lgpPduAuxSensorUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorUsrLabel.setStatus("deprecated")
_LgpPduAuxSensorUsrTag1_Type = DisplayString
_LgpPduAuxSensorUsrTag1_Object = MibTableColumn
lgpPduAuxSensorUsrTag1 = _LgpPduAuxSensorUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 30),
    _LgpPduAuxSensorUsrTag1_Type()
)
lgpPduAuxSensorUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorUsrTag1.setStatus("deprecated")
_LgpPduAuxSensorUsrTag2_Type = DisplayString
_LgpPduAuxSensorUsrTag2_Object = MibTableColumn
lgpPduAuxSensorUsrTag2 = _LgpPduAuxSensorUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 35),
    _LgpPduAuxSensorUsrTag2_Type()
)
lgpPduAuxSensorUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorUsrTag2.setStatus("deprecated")
_LgpPduAuxSensorTempSerialNum_Type = DisplayString
_LgpPduAuxSensorTempSerialNum_Object = MibTableColumn
lgpPduAuxSensorTempSerialNum = _LgpPduAuxSensorTempSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 40),
    _LgpPduAuxSensorTempSerialNum_Type()
)
lgpPduAuxSensorTempSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempSerialNum.setStatus("deprecated")
_LgpPduAuxSensorHumSerialNum_Type = DisplayString
_LgpPduAuxSensorHumSerialNum_Object = MibTableColumn
lgpPduAuxSensorHumSerialNum = _LgpPduAuxSensorHumSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 45),
    _LgpPduAuxSensorHumSerialNum_Type()
)
lgpPduAuxSensorHumSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumSerialNum.setStatus("deprecated")
_LgpPduAuxSensorTempMeasurementDegF_Type = Integer32
_LgpPduAuxSensorTempMeasurementDegF_Object = MibTableColumn
lgpPduAuxSensorTempMeasurementDegF = _LgpPduAuxSensorTempMeasurementDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 50),
    _LgpPduAuxSensorTempMeasurementDegF_Type()
)
lgpPduAuxSensorTempMeasurementDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldUndrAlmDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrAlmDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrAlmDegF = _LgpPduAuxSensorTempThrshldUndrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 55),
    _LgpPduAuxSensorTempThrshldUndrAlmDegF_Type()
)
lgpPduAuxSensorTempThrshldUndrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldOvrAlmDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrAlmDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrAlmDegF = _LgpPduAuxSensorTempThrshldOvrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 60),
    _LgpPduAuxSensorTempThrshldOvrAlmDegF_Type()
)
lgpPduAuxSensorTempThrshldOvrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldUndrWarnDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrWarnDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrWarnDegF = _LgpPduAuxSensorTempThrshldUndrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 65),
    _LgpPduAuxSensorTempThrshldUndrWarnDegF_Type()
)
lgpPduAuxSensorTempThrshldUndrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempThrshldOvrWarnDegF_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrWarnDegF_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrWarnDegF = _LgpPduAuxSensorTempThrshldOvrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 70),
    _LgpPduAuxSensorTempThrshldOvrWarnDegF_Type()
)
lgpPduAuxSensorTempThrshldOvrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegF.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxSensorTempMeasurementDegC_Type = Integer32
_LgpPduAuxSensorTempMeasurementDegC_Object = MibTableColumn
lgpPduAuxSensorTempMeasurementDegC = _LgpPduAuxSensorTempMeasurementDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 75),
    _LgpPduAuxSensorTempMeasurementDegC_Type()
)
lgpPduAuxSensorTempMeasurementDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempMeasurementDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldUndrAlmDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrAlmDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrAlmDegC = _LgpPduAuxSensorTempThrshldUndrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 80),
    _LgpPduAuxSensorTempThrshldUndrAlmDegC_Type()
)
lgpPduAuxSensorTempThrshldUndrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldOvrAlmDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrAlmDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrAlmDegC = _LgpPduAuxSensorTempThrshldOvrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 85),
    _LgpPduAuxSensorTempThrshldOvrAlmDegC_Type()
)
lgpPduAuxSensorTempThrshldOvrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldUndrWarnDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldUndrWarnDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldUndrWarnDegC = _LgpPduAuxSensorTempThrshldUndrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 90),
    _LgpPduAuxSensorTempThrshldUndrWarnDegC_Type()
)
lgpPduAuxSensorTempThrshldUndrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldUndrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorTempThrshldOvrWarnDegC_Type = Integer32
_LgpPduAuxSensorTempThrshldOvrWarnDegC_Object = MibTableColumn
lgpPduAuxSensorTempThrshldOvrWarnDegC = _LgpPduAuxSensorTempThrshldOvrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 95),
    _LgpPduAuxSensorTempThrshldOvrWarnDegC_Type()
)
lgpPduAuxSensorTempThrshldOvrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegC.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorTempThrshldOvrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxSensorHumMeasurement_Type = Unsigned32
_LgpPduAuxSensorHumMeasurement_Object = MibTableColumn
lgpPduAuxSensorHumMeasurement = _LgpPduAuxSensorHumMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 100),
    _LgpPduAuxSensorHumMeasurement_Type()
)
lgpPduAuxSensorHumMeasurement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumMeasurement.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumMeasurement.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldUndrAlm_Type = Unsigned32
_LgpPduAuxSensorHumThrshldUndrAlm_Object = MibTableColumn
lgpPduAuxSensorHumThrshldUndrAlm = _LgpPduAuxSensorHumThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 105),
    _LgpPduAuxSensorHumThrshldUndrAlm_Type()
)
lgpPduAuxSensorHumThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldOvrAlm_Type = Unsigned32
_LgpPduAuxSensorHumThrshldOvrAlm_Object = MibTableColumn
lgpPduAuxSensorHumThrshldOvrAlm = _LgpPduAuxSensorHumThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 110),
    _LgpPduAuxSensorHumThrshldOvrAlm_Type()
)
lgpPduAuxSensorHumThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrAlm.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldUndrWarn_Type = Unsigned32
_LgpPduAuxSensorHumThrshldUndrWarn_Object = MibTableColumn
lgpPduAuxSensorHumThrshldUndrWarn = _LgpPduAuxSensorHumThrshldUndrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 115),
    _LgpPduAuxSensorHumThrshldUndrWarn_Type()
)
lgpPduAuxSensorHumThrshldUndrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrWarn.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldUndrWarn.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxSensorHumThrshldOvrWarn_Type = Unsigned32
_LgpPduAuxSensorHumThrshldOvrWarn_Object = MibTableColumn
lgpPduAuxSensorHumThrshldOvrWarn = _LgpPduAuxSensorHumThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 10, 1, 120),
    _LgpPduAuxSensorHumThrshldOvrWarn_Type()
)
lgpPduAuxSensorHumThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrWarn.setStatus("deprecated")
if mibBuilder.loadTexts:
    lgpPduAuxSensorHumThrshldOvrWarn.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasTable_Object = MibTable
lgpPduAuxMeasTable = _LgpPduAuxMeasTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15)
)
if mibBuilder.loadTexts:
    lgpPduAuxMeasTable.setStatus("current")
_LgpPduAuxMeasEntry_Object = MibTableRow
lgpPduAuxMeasEntry = _LgpPduAuxMeasEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1)
)
lgpPduAuxMeasEntry.setIndexNames(
    (0, "LIEBERT-GP-MIB", "lgpPduEntryIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduAuxMeasSensorIndex"),
    (0, "LIEBERT-GP-MIB", "lgpPduAuxMeasSensorMeasurementIndex"),
)
if mibBuilder.loadTexts:
    lgpPduAuxMeasEntry.setStatus("current")
_LgpPduAuxMeasSensorIndex_Type = Unsigned32
_LgpPduAuxMeasSensorIndex_Object = MibTableColumn
lgpPduAuxMeasSensorIndex = _LgpPduAuxMeasSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 1),
    _LgpPduAuxMeasSensorIndex_Type()
)
lgpPduAuxMeasSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorIndex.setStatus("current")
_LgpPduAuxMeasSensorMeasurementIndex_Type = Unsigned32
_LgpPduAuxMeasSensorMeasurementIndex_Object = MibTableColumn
lgpPduAuxMeasSensorMeasurementIndex = _LgpPduAuxMeasSensorMeasurementIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 5),
    _LgpPduAuxMeasSensorMeasurementIndex_Type()
)
lgpPduAuxMeasSensorMeasurementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorMeasurementIndex.setStatus("current")


class _LgpPduAuxMeasType_Type(Integer32):
    """Custom type lgpPduAuxMeasType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("temperature", 1),
          ("humidity", 2),
          ("door-closure", 3),
          ("contact-closure", 4))
    )


_LgpPduAuxMeasType_Type.__name__ = "Integer32"
_LgpPduAuxMeasType_Object = MibTableColumn
lgpPduAuxMeasType = _LgpPduAuxMeasType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 10),
    _LgpPduAuxMeasType_Type()
)
lgpPduAuxMeasType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasType.setStatus("current")
_LgpPduAuxMeasSensorSysAssignLabel_Type = DisplayString
_LgpPduAuxMeasSensorSysAssignLabel_Object = MibTableColumn
lgpPduAuxMeasSensorSysAssignLabel = _LgpPduAuxMeasSensorSysAssignLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 15),
    _LgpPduAuxMeasSensorSysAssignLabel_Type()
)
lgpPduAuxMeasSensorSysAssignLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorSysAssignLabel.setStatus("current")
_LgpPduAuxMeasUsrLabel_Type = DisplayString
_LgpPduAuxMeasUsrLabel_Object = MibTableColumn
lgpPduAuxMeasUsrLabel = _LgpPduAuxMeasUsrLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 20),
    _LgpPduAuxMeasUsrLabel_Type()
)
lgpPduAuxMeasUsrLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasUsrLabel.setStatus("current")
_LgpPduAuxMeasUsrTag1_Type = DisplayString
_LgpPduAuxMeasUsrTag1_Object = MibTableColumn
lgpPduAuxMeasUsrTag1 = _LgpPduAuxMeasUsrTag1_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 25),
    _LgpPduAuxMeasUsrTag1_Type()
)
lgpPduAuxMeasUsrTag1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasUsrTag1.setStatus("current")
_LgpPduAuxMeasUsrTag2_Type = DisplayString
_LgpPduAuxMeasUsrTag2_Object = MibTableColumn
lgpPduAuxMeasUsrTag2 = _LgpPduAuxMeasUsrTag2_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 30),
    _LgpPduAuxMeasUsrTag2_Type()
)
lgpPduAuxMeasUsrTag2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasUsrTag2.setStatus("current")
_LgpPduAuxMeasSensorSerialNum_Type = DisplayString
_LgpPduAuxMeasSensorSerialNum_Object = MibTableColumn
lgpPduAuxMeasSensorSerialNum = _LgpPduAuxMeasSensorSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 35),
    _LgpPduAuxMeasSensorSerialNum_Type()
)
lgpPduAuxMeasSensorSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasSensorSerialNum.setStatus("current")
_LgpPduAuxMeasTempDegF_Type = Integer32
_LgpPduAuxMeasTempDegF_Object = MibTableColumn
lgpPduAuxMeasTempDegF = _LgpPduAuxMeasTempDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 40),
    _LgpPduAuxMeasTempDegF_Type()
)
lgpPduAuxMeasTempDegF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldUndrAlmDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrAlmDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrAlmDegF = _LgpPduAuxMeasTempThrshldUndrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 50),
    _LgpPduAuxMeasTempThrshldUndrAlmDegF_Type()
)
lgpPduAuxMeasTempThrshldUndrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldOvrAlmDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrAlmDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrAlmDegF = _LgpPduAuxMeasTempThrshldOvrAlmDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 55),
    _LgpPduAuxMeasTempThrshldOvrAlmDegF_Type()
)
lgpPduAuxMeasTempThrshldOvrAlmDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldUndrWarnDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrWarnDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrWarnDegF = _LgpPduAuxMeasTempThrshldUndrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 60),
    _LgpPduAuxMeasTempThrshldUndrWarnDegF_Type()
)
lgpPduAuxMeasTempThrshldUndrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempThrshldOvrWarnDegF_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrWarnDegF_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrWarnDegF = _LgpPduAuxMeasTempThrshldOvrWarnDegF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 65),
    _LgpPduAuxMeasTempThrshldOvrWarnDegF_Type()
)
lgpPduAuxMeasTempThrshldOvrWarnDegF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegF.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegF.setUnits("0.1 degrees Fahrenheit")
_LgpPduAuxMeasTempDegC_Type = Integer32
_LgpPduAuxMeasTempDegC_Object = MibTableColumn
lgpPduAuxMeasTempDegC = _LgpPduAuxMeasTempDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 70),
    _LgpPduAuxMeasTempDegC_Type()
)
lgpPduAuxMeasTempDegC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldUndrAlmDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrAlmDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrAlmDegC = _LgpPduAuxMeasTempThrshldUndrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 75),
    _LgpPduAuxMeasTempThrshldUndrAlmDegC_Type()
)
lgpPduAuxMeasTempThrshldUndrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldOvrAlmDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrAlmDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrAlmDegC = _LgpPduAuxMeasTempThrshldOvrAlmDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 80),
    _LgpPduAuxMeasTempThrshldOvrAlmDegC_Type()
)
lgpPduAuxMeasTempThrshldOvrAlmDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrAlmDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldUndrWarnDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldUndrWarnDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldUndrWarnDegC = _LgpPduAuxMeasTempThrshldUndrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 85),
    _LgpPduAuxMeasTempThrshldUndrWarnDegC_Type()
)
lgpPduAuxMeasTempThrshldUndrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldUndrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasTempThrshldOvrWarnDegC_Type = Integer32
_LgpPduAuxMeasTempThrshldOvrWarnDegC_Object = MibTableColumn
lgpPduAuxMeasTempThrshldOvrWarnDegC = _LgpPduAuxMeasTempThrshldOvrWarnDegC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 90),
    _LgpPduAuxMeasTempThrshldOvrWarnDegC_Type()
)
lgpPduAuxMeasTempThrshldOvrWarnDegC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegC.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasTempThrshldOvrWarnDegC.setUnits("0.1 degrees Celsius")
_LgpPduAuxMeasHum_Type = Unsigned32
_LgpPduAuxMeasHum_Object = MibTableColumn
lgpPduAuxMeasHum = _LgpPduAuxMeasHum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 95),
    _LgpPduAuxMeasHum_Type()
)
lgpPduAuxMeasHum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHum.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHum.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldUndrAlm_Type = Unsigned32
_LgpPduAuxMeasHumThrshldUndrAlm_Object = MibTableColumn
lgpPduAuxMeasHumThrshldUndrAlm = _LgpPduAuxMeasHumThrshldUndrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 100),
    _LgpPduAuxMeasHumThrshldUndrAlm_Type()
)
lgpPduAuxMeasHumThrshldUndrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldOvrAlm_Type = Unsigned32
_LgpPduAuxMeasHumThrshldOvrAlm_Object = MibTableColumn
lgpPduAuxMeasHumThrshldOvrAlm = _LgpPduAuxMeasHumThrshldOvrAlm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 105),
    _LgpPduAuxMeasHumThrshldOvrAlm_Type()
)
lgpPduAuxMeasHumThrshldOvrAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrAlm.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrAlm.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldUndrWarn_Type = Unsigned32
_LgpPduAuxMeasHumThrshldUndrWarn_Object = MibTableColumn
lgpPduAuxMeasHumThrshldUndrWarn = _LgpPduAuxMeasHumThrshldUndrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 110),
    _LgpPduAuxMeasHumThrshldUndrWarn_Type()
)
lgpPduAuxMeasHumThrshldUndrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldUndrWarn.setUnits("0.1 percent Relative Humidity")
_LgpPduAuxMeasHumThrshldOvrWarn_Type = Unsigned32
_LgpPduAuxMeasHumThrshldOvrWarn_Object = MibTableColumn
lgpPduAuxMeasHumThrshldOvrWarn = _LgpPduAuxMeasHumThrshldOvrWarn_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 115),
    _LgpPduAuxMeasHumThrshldOvrWarn_Type()
)
lgpPduAuxMeasHumThrshldOvrWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrWarn.setStatus("current")
if mibBuilder.loadTexts:
    lgpPduAuxMeasHumThrshldOvrWarn.setUnits("0.1 percent Relative Humidity")


class _LgpPduAuxMeasDrClosureState_Type(Integer32):
    """Custom type lgpPduAuxMeasDrClosureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("open", 1),
          ("closed", 2))
    )


_LgpPduAuxMeasDrClosureState_Type.__name__ = "Integer32"
_LgpPduAuxMeasDrClosureState_Object = MibTableColumn
lgpPduAuxMeasDrClosureState = _LgpPduAuxMeasDrClosureState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 120),
    _LgpPduAuxMeasDrClosureState_Type()
)
lgpPduAuxMeasDrClosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasDrClosureState.setStatus("current")


class _LgpPduAuxMeasDrClosureConfig_Type(Integer32):
    """Custom type lgpPduAuxMeasDrClosureConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("alarm-when-open", 1))
    )


_LgpPduAuxMeasDrClosureConfig_Type.__name__ = "Integer32"
_LgpPduAuxMeasDrClosureConfig_Object = MibTableColumn
lgpPduAuxMeasDrClosureConfig = _LgpPduAuxMeasDrClosureConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 125),
    _LgpPduAuxMeasDrClosureConfig_Type()
)
lgpPduAuxMeasDrClosureConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasDrClosureConfig.setStatus("current")


class _LgpPduAuxMeasCntctClosureState_Type(Integer32):
    """Custom type lgpPduAuxMeasCntctClosureState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("open", 1),
          ("closed", 2))
    )


_LgpPduAuxMeasCntctClosureState_Type.__name__ = "Integer32"
_LgpPduAuxMeasCntctClosureState_Object = MibTableColumn
lgpPduAuxMeasCntctClosureState = _LgpPduAuxMeasCntctClosureState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 130),
    _LgpPduAuxMeasCntctClosureState_Type()
)
lgpPduAuxMeasCntctClosureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpPduAuxMeasCntctClosureState.setStatus("current")


class _LgpPduAuxMeasCntctClosureConfig_Type(Integer32):
    """Custom type lgpPduAuxMeasCntctClosureConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("alarm-when-open", 1),
          ("alarm-when-closed", 2))
    )


_LgpPduAuxMeasCntctClosureConfig_Type.__name__ = "Integer32"
_LgpPduAuxMeasCntctClosureConfig_Object = MibTableColumn
lgpPduAuxMeasCntctClosureConfig = _LgpPduAuxMeasCntctClosureConfig_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 8, 60, 15, 1, 135),
    _LgpPduAuxMeasCntctClosureConfig_Type()
)
lgpPduAuxMeasCntctClosureConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpPduAuxMeasCntctClosureConfig.setStatus("current")
_LgpFlexible_ObjectIdentity = ObjectIdentity
lgpFlexible = _LgpFlexible_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9)
)
if mibBuilder.loadTexts:
    lgpFlexible.setStatus("current")
_LgpFlexibleTableCount_Type = Unsigned32
_LgpFlexibleTableCount_Object = MibScalar
lgpFlexibleTableCount = _LgpFlexibleTableCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 10),
    _LgpFlexibleTableCount_Type()
)
lgpFlexibleTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleTableCount.setStatus("current")
if mibBuilder.loadTexts:
    lgpFlexibleTableCount.setUnits("Count")
_LgpFlexibleBasicTable_Object = MibTable
lgpFlexibleBasicTable = _LgpFlexibleBasicTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20)
)
if mibBuilder.loadTexts:
    lgpFlexibleBasicTable.setStatus("current")
_LgpFlexibleBasicEntry_Object = MibTableRow
lgpFlexibleBasicEntry = _LgpFlexibleBasicEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1)
)
lgpFlexibleBasicEntry.setIndexNames(
    (1, "LIEBERT-GP-MIB", "lgpFlexibleEntryIndex"),
)
if mibBuilder.loadTexts:
    lgpFlexibleBasicEntry.setStatus("current")
_LgpFlexibleEntryIndex_Type = ObjectIdentifier
_LgpFlexibleEntryIndex_Object = MibTableColumn
lgpFlexibleEntryIndex = _LgpFlexibleEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 1),
    _LgpFlexibleEntryIndex_Type()
)
lgpFlexibleEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lgpFlexibleEntryIndex.setStatus("current")
_LgpFlexibleEntryDataLabel_Type = DisplayString
_LgpFlexibleEntryDataLabel_Object = MibTableColumn
lgpFlexibleEntryDataLabel = _LgpFlexibleEntryDataLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 10),
    _LgpFlexibleEntryDataLabel_Type()
)
lgpFlexibleEntryDataLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDataLabel.setStatus("current")
_LgpFlexibleEntryValue_Type = DisplayString
_LgpFlexibleEntryValue_Object = MibTableColumn
lgpFlexibleEntryValue = _LgpFlexibleEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 20),
    _LgpFlexibleEntryValue_Type()
)
lgpFlexibleEntryValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpFlexibleEntryValue.setStatus("current")
_LgpFlexibleEntryUnitsOfMeasure_Type = DisplayString
_LgpFlexibleEntryUnitsOfMeasure_Object = MibTableColumn
lgpFlexibleEntryUnitsOfMeasure = _LgpFlexibleEntryUnitsOfMeasure_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 30),
    _LgpFlexibleEntryUnitsOfMeasure_Type()
)
lgpFlexibleEntryUnitsOfMeasure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryUnitsOfMeasure.setStatus("current")
_LgpFlexibleExtendedTable_Object = MibTable
lgpFlexibleExtendedTable = _LgpFlexibleExtendedTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30)
)
if mibBuilder.loadTexts:
    lgpFlexibleExtendedTable.setStatus("current")
_LgpFlexibleExtendedEntry_Object = MibTableRow
lgpFlexibleExtendedEntry = _LgpFlexibleExtendedEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1)
)
if mibBuilder.loadTexts:
    lgpFlexibleExtendedEntry.setStatus("current")
_LgpFlexibleEntryIntegerValue_Type = Integer32
_LgpFlexibleEntryIntegerValue_Object = MibTableColumn
lgpFlexibleEntryIntegerValue = _LgpFlexibleEntryIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 10),
    _LgpFlexibleEntryIntegerValue_Type()
)
lgpFlexibleEntryIntegerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpFlexibleEntryIntegerValue.setStatus("current")
_LgpFlexibleEntryUnsignedIntegerValue_Type = Unsigned32
_LgpFlexibleEntryUnsignedIntegerValue_Object = MibTableColumn
lgpFlexibleEntryUnsignedIntegerValue = _LgpFlexibleEntryUnsignedIntegerValue_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 20),
    _LgpFlexibleEntryUnsignedIntegerValue_Type()
)
lgpFlexibleEntryUnsignedIntegerValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lgpFlexibleEntryUnsignedIntegerValue.setStatus("current")
_LgpFlexibleEntryDecimalPosition_Type = Unsigned32
_LgpFlexibleEntryDecimalPosition_Object = MibTableColumn
lgpFlexibleEntryDecimalPosition = _LgpFlexibleEntryDecimalPosition_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 30),
    _LgpFlexibleEntryDecimalPosition_Type()
)
lgpFlexibleEntryDecimalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDecimalPosition.setStatus("current")


class _LgpFlexibleEntryDataType_Type(Integer32):
    """Custom type lgpFlexibleEntryDataType based on Integer32"""
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
        *(("not-specified", 0),
          ("int16", 1),
          ("uint16", 2),
          ("int32", 3),
          ("uint32", 4),
          ("text", 5),
          ("enum", 6),
          ("event16", 7),
          ("event32", 8),
          ("ipv4", 9),
          ("time32", 10))
    )


_LgpFlexibleEntryDataType_Type.__name__ = "Integer32"
_LgpFlexibleEntryDataType_Object = MibTableColumn
lgpFlexibleEntryDataType = _LgpFlexibleEntryDataType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 40),
    _LgpFlexibleEntryDataType_Type()
)
lgpFlexibleEntryDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDataType.setStatus("current")


class _LgpFlexibleEntryAccessibility_Type(Integer32):
    """Custom type lgpFlexibleEntryAccessibility based on Integer32"""
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
        *(("not-specified", 0),
          ("readonly", 1),
          ("writeonly", 2),
          ("readwrite", 3))
    )


_LgpFlexibleEntryAccessibility_Type.__name__ = "Integer32"
_LgpFlexibleEntryAccessibility_Object = MibTableColumn
lgpFlexibleEntryAccessibility = _LgpFlexibleEntryAccessibility_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 50),
    _LgpFlexibleEntryAccessibility_Type()
)
lgpFlexibleEntryAccessibility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryAccessibility.setStatus("current")


class _LgpFlexibleEntryUnitsOfMeasureEnum_Type(Integer32):
    """Custom type lgpFlexibleEntryUnitsOfMeasureEnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              4097,
              4098,
              4099,
              4100,
              4101,
              4102,
              4103,
              4104,
              4105,
              4106,
              4107,
              4108,
              4109,
              4110,
              4111,
              4112,
              4113,
              4114,
              4115,
              4116,
              4117,
              4118,
              4119,
              4120,
              4121,
              4122,
              4123,
              4124,
              4125,
              4126,
              4127,
              4128,
              4129,
              4130,
              4131,
              4132,
              4133,
              4134,
              4135,
              4136,
              4137,
              4138,
              4139,
              4140,
              4141)
        )
    )
    namedValues = NamedValues(
        *(("not-specified", 0),
          ("milliSeconds", 4096),
          ("seconds", 4097),
          ("minutes", 4098),
          ("hours", 4099),
          ("voltsAcRms", 4100),
          ("milliVoltsAcRms", 4101),
          ("voltsDc", 4102),
          ("milliVoltsDc", 4103),
          ("voltsPeak", 4104),
          ("voltsPeakToPeak", 4105),
          ("ampsAcRms", 4106),
          ("milliAmpsAcRms", 4107),
          ("ampsDc", 4108),
          ("milliAmpsDc", 4109),
          ("voltAmps", 4110),
          ("kiloVoltAmps", 4111),
          ("voltAmpsReactive", 4112),
          ("kVAReactive", 4113),
          ("watts", 4114),
          ("kiloWatts", 4115),
          ("wattHours", 4116),
          ("kiloWattHour", 4117),
          ("ampDcHours", 4118),
          ("hertz", 4119),
          ("milliHertz", 4120),
          ("kiloHertz", 4121),
          ("megaHertz", 4122),
          ("gigaHertz", 4123),
          ("percent", 4124),
          ("degC", 4125),
          ("degCDelta", 4126),
          ("degF", 4127),
          ("degFDelta", 4128),
          ("psi", 4129),
          ("pascal", 4130),
          ("psia", 4131),
          ("relativeHumidity", 4132),
          ("thd", 4133),
          ("days", 4134),
          ("phase", 4135),
          ("microOhms", 4136),
          ("milliOhms", 4137),
          ("ohms", 4138),
          ("kiloOhms", 4139),
          ("megaOhms", 4140),
          ("bars", 4141))
    )


_LgpFlexibleEntryUnitsOfMeasureEnum_Type.__name__ = "Integer32"
_LgpFlexibleEntryUnitsOfMeasureEnum_Object = MibTableColumn
lgpFlexibleEntryUnitsOfMeasureEnum = _LgpFlexibleEntryUnitsOfMeasureEnum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 60),
    _LgpFlexibleEntryUnitsOfMeasureEnum_Type()
)
lgpFlexibleEntryUnitsOfMeasureEnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryUnitsOfMeasureEnum.setStatus("current")
_LgpFlexibleEntryDataDescription_Type = DisplayString
_LgpFlexibleEntryDataDescription_Object = MibTableColumn
lgpFlexibleEntryDataDescription = _LgpFlexibleEntryDataDescription_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 70),
    _LgpFlexibleEntryDataDescription_Type()
)
lgpFlexibleEntryDataDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lgpFlexibleEntryDataDescription.setStatus("current")
_LgpProductSpecific_ObjectIdentity = ObjectIdentity
lgpProductSpecific = _LgpProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4)
)
if mibBuilder.loadTexts:
    lgpProductSpecific.setStatus("current")
_LgpUpsProducts_ObjectIdentity = ObjectIdentity
lgpUpsProducts = _LgpUpsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2)
)
if mibBuilder.loadTexts:
    lgpUpsProducts.setStatus("current")
_LgpSeries7200_ObjectIdentity = ObjectIdentity
lgpSeries7200 = _LgpSeries7200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 1)
)
if mibBuilder.loadTexts:
    lgpSeries7200.setStatus("current")
_LgpUPStationGXT_ObjectIdentity = ObjectIdentity
lgpUPStationGXT = _LgpUPStationGXT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 2)
)
if mibBuilder.loadTexts:
    lgpUPStationGXT.setStatus("current")
_LgpPowerSureInteractive_ObjectIdentity = ObjectIdentity
lgpPowerSureInteractive = _LgpPowerSureInteractive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 3)
)
if mibBuilder.loadTexts:
    lgpPowerSureInteractive.setStatus("current")
_LgpNfinity_ObjectIdentity = ObjectIdentity
lgpNfinity = _LgpNfinity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 4)
)
if mibBuilder.loadTexts:
    lgpNfinity.setStatus("current")
_LgpNpower_ObjectIdentity = ObjectIdentity
lgpNpower = _LgpNpower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 5)
)
if mibBuilder.loadTexts:
    lgpNpower.setStatus("current")
_LgpGXT2Dual_ObjectIdentity = ObjectIdentity
lgpGXT2Dual = _LgpGXT2Dual_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 6)
)
if mibBuilder.loadTexts:
    lgpGXT2Dual.setStatus("current")
_LgpPowerSureInteractive2_ObjectIdentity = ObjectIdentity
lgpPowerSureInteractive2 = _LgpPowerSureInteractive2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 7)
)
if mibBuilder.loadTexts:
    lgpPowerSureInteractive2.setStatus("current")
_LgpNX_ObjectIdentity = ObjectIdentity
lgpNX = _LgpNX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 8)
)
if mibBuilder.loadTexts:
    lgpNX.setStatus("current")
_LgpHiNet_ObjectIdentity = ObjectIdentity
lgpHiNet = _LgpHiNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 9)
)
if mibBuilder.loadTexts:
    lgpHiNet.setStatus("current")
_LgpNXL_ObjectIdentity = ObjectIdentity
lgpNXL = _LgpNXL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 10)
)
if mibBuilder.loadTexts:
    lgpNXL.setStatus("current")
_LgpSuper400_ObjectIdentity = ObjectIdentity
lgpSuper400 = _LgpSuper400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 11)
)
if mibBuilder.loadTexts:
    lgpSuper400.setStatus("current")
_LgpSeries600or610_ObjectIdentity = ObjectIdentity
lgpSeries600or610 = _LgpSeries600or610_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 12)
)
if mibBuilder.loadTexts:
    lgpSeries600or610.setStatus("current")
_LgpSeries300_ObjectIdentity = ObjectIdentity
lgpSeries300 = _LgpSeries300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 13)
)
if mibBuilder.loadTexts:
    lgpSeries300.setStatus("current")
_LgpSeries610SMS_ObjectIdentity = ObjectIdentity
lgpSeries610SMS = _LgpSeries610SMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 14)
)
if mibBuilder.loadTexts:
    lgpSeries610SMS.setStatus("current")
_LgpSeries610MMU_ObjectIdentity = ObjectIdentity
lgpSeries610MMU = _LgpSeries610MMU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 15)
)
if mibBuilder.loadTexts:
    lgpSeries610MMU.setStatus("current")
_LgpSeries610SCC_ObjectIdentity = ObjectIdentity
lgpSeries610SCC = _LgpSeries610SCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 16)
)
if mibBuilder.loadTexts:
    lgpSeries610SCC.setStatus("current")
_LgpNXr_ObjectIdentity = ObjectIdentity
lgpNXr = _LgpNXr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 2, 19)
)
if mibBuilder.loadTexts:
    lgpNXr.setStatus("current")
_LgpAcProducts_ObjectIdentity = ObjectIdentity
lgpAcProducts = _LgpAcProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3)
)
if mibBuilder.loadTexts:
    lgpAcProducts.setStatus("current")
_LgpAdvancedMicroprocessor_ObjectIdentity = ObjectIdentity
lgpAdvancedMicroprocessor = _LgpAdvancedMicroprocessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 1)
)
if mibBuilder.loadTexts:
    lgpAdvancedMicroprocessor.setStatus("current")
_LgpStandardMicroprocessor_ObjectIdentity = ObjectIdentity
lgpStandardMicroprocessor = _LgpStandardMicroprocessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 2)
)
if mibBuilder.loadTexts:
    lgpStandardMicroprocessor.setStatus("current")
_LgpMiniMate2_ObjectIdentity = ObjectIdentity
lgpMiniMate2 = _LgpMiniMate2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 3)
)
if mibBuilder.loadTexts:
    lgpMiniMate2.setStatus("current")
_LgpHimod_ObjectIdentity = ObjectIdentity
lgpHimod = _LgpHimod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 4)
)
if mibBuilder.loadTexts:
    lgpHimod.setStatus("current")
_LgpCEMS100orLECS15_ObjectIdentity = ObjectIdentity
lgpCEMS100orLECS15 = _LgpCEMS100orLECS15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 5)
)
if mibBuilder.loadTexts:
    lgpCEMS100orLECS15.setStatus("current")
_LgpIcom_ObjectIdentity = ObjectIdentity
lgpIcom = _LgpIcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 6)
)
if mibBuilder.loadTexts:
    lgpIcom.setStatus("current")
_LgpIcomPA_ObjectIdentity = ObjectIdentity
lgpIcomPA = _LgpIcomPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7)
)
if mibBuilder.loadTexts:
    lgpIcomPA.setStatus("current")
_LgpIcomPAtypeDS_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeDS = _LgpIcomPAtypeDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 1)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeDS.setStatus("current")
_LgpIcomPAtypeHPM_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeHPM = _LgpIcomPAtypeHPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 2)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeHPM.setStatus("current")
_LgpIcomPAtypeChallenger_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeChallenger = _LgpIcomPAtypeChallenger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 3)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeChallenger.setStatus("current")
_LgpIcomPAtypePeX_ObjectIdentity = ObjectIdentity
lgpIcomPAtypePeX = _LgpIcomPAtypePeX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 4)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypePeX.setStatus("current")
_LgpIcomPAtypeDeluxeSys3_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeDeluxeSys3 = _LgpIcomPAtypeDeluxeSys3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 5)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeDeluxeSys3.setStatus("current")
_LgpIcomPAtypeJumboCW_ObjectIdentity = ObjectIdentity
lgpIcomPAtypeJumboCW = _LgpIcomPAtypeJumboCW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 7, 6)
)
if mibBuilder.loadTexts:
    lgpIcomPAtypeJumboCW.setStatus("current")
_LgpIcomXD_ObjectIdentity = ObjectIdentity
lgpIcomXD = _LgpIcomXD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 8)
)
if mibBuilder.loadTexts:
    lgpIcomXD.setStatus("current")
_LgpIcomXDtypeXDF_ObjectIdentity = ObjectIdentity
lgpIcomXDtypeXDF = _LgpIcomXDtypeXDF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 8, 1)
)
if mibBuilder.loadTexts:
    lgpIcomXDtypeXDF.setStatus("current")
_LgpIcomXDtypeXDFN_ObjectIdentity = ObjectIdentity
lgpIcomXDtypeXDFN = _LgpIcomXDtypeXDFN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 8, 2)
)
if mibBuilder.loadTexts:
    lgpIcomXDtypeXDFN.setStatus("current")
_LgpIcomXP_ObjectIdentity = ObjectIdentity
lgpIcomXP = _LgpIcomXP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9)
)
if mibBuilder.loadTexts:
    lgpIcomXP.setStatus("current")
_LgpIcomXPtypeXDP_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDP = _LgpIcomXPtypeXDP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 1)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDP.setStatus("current")
_LgpIcomXPtypeXDPCray_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDPCray = _LgpIcomXPtypeXDPCray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 1, 1)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDPCray.setStatus("current")
_LgpIcomXPtypeXDC_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDC = _LgpIcomXPtypeXDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 2)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDC.setStatus("current")
_LgpIcomXPtypeXDPW_ObjectIdentity = ObjectIdentity
lgpIcomXPtypeXDPW = _LgpIcomXPtypeXDPW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 9, 3)
)
if mibBuilder.loadTexts:
    lgpIcomXPtypeXDPW.setStatus("current")
_LgpIcomSC_ObjectIdentity = ObjectIdentity
lgpIcomSC = _LgpIcomSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10)
)
if mibBuilder.loadTexts:
    lgpIcomSC.setStatus("current")
_LgpIcomSCtypeHPC_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPC = _LgpIcomSCtypeHPC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPC.setStatus("current")
_LgpIcomSCtypeHPCSSmall_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCSSmall = _LgpIcomSCtypeHPCSSmall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCSSmall.setStatus("current")
_LgpIcomSCtypeHPCSLarge_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCSLarge = _LgpIcomSCtypeHPCSLarge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 2)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCSLarge.setStatus("current")
_LgpIcomSCtypeHPCR_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCR = _LgpIcomSCtypeHPCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 3)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCR.setStatus("current")
_LgpIcomSCtypeHPCM_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCM = _LgpIcomSCtypeHPCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 4)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCM.setStatus("current")
_LgpIcomSCtypeHPCL_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCL = _LgpIcomSCtypeHPCL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 5)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCL.setStatus("current")
_LgpIcomSCtypeHPCW_ObjectIdentity = ObjectIdentity
lgpIcomSCtypeHPCW = _LgpIcomSCtypeHPCW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 10, 1, 6)
)
if mibBuilder.loadTexts:
    lgpIcomSCtypeHPCW.setStatus("current")
_LgpIcomCR_ObjectIdentity = ObjectIdentity
lgpIcomCR = _LgpIcomCR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 11)
)
if mibBuilder.loadTexts:
    lgpIcomCR.setStatus("current")
_LgpIcomCRtypeCRV_ObjectIdentity = ObjectIdentity
lgpIcomCRtypeCRV = _LgpIcomCRtypeCRV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 3, 11, 1)
)
if mibBuilder.loadTexts:
    lgpIcomCRtypeCRV.setStatus("current")
_LgpPowerConditioningProducts_ObjectIdentity = ObjectIdentity
lgpPowerConditioningProducts = _LgpPowerConditioningProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 4)
)
if mibBuilder.loadTexts:
    lgpPowerConditioningProducts.setStatus("current")
_LgpPMP_ObjectIdentity = ObjectIdentity
lgpPMP = _LgpPMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 4, 1)
)
if mibBuilder.loadTexts:
    lgpPMP.setStatus("current")
_LgpEPMP_ObjectIdentity = ObjectIdentity
lgpEPMP = _LgpEPMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 4, 2)
)
if mibBuilder.loadTexts:
    lgpEPMP.setStatus("current")
_LgpTransferSwitchProducts_ObjectIdentity = ObjectIdentity
lgpTransferSwitchProducts = _LgpTransferSwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5)
)
if mibBuilder.loadTexts:
    lgpTransferSwitchProducts.setStatus("current")
_LgpStaticTransferSwitchEDS_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitchEDS = _LgpStaticTransferSwitchEDS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 1)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitchEDS.setStatus("current")
_LgpStaticTransferSwitch1_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitch1 = _LgpStaticTransferSwitch1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 2)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitch1.setStatus("current")
_LgpStaticTransferSwitch2_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitch2 = _LgpStaticTransferSwitch2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 3)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitch2.setStatus("current")
_LgpStaticTransferSwitch2FourPole_ObjectIdentity = ObjectIdentity
lgpStaticTransferSwitch2FourPole = _LgpStaticTransferSwitch2FourPole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 5, 4)
)
if mibBuilder.loadTexts:
    lgpStaticTransferSwitch2FourPole.setStatus("current")
_LgpMultiLinkProducts_ObjectIdentity = ObjectIdentity
lgpMultiLinkProducts = _LgpMultiLinkProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 7)
)
if mibBuilder.loadTexts:
    lgpMultiLinkProducts.setStatus("current")
_LgpMultiLinkBasicNotification_ObjectIdentity = ObjectIdentity
lgpMultiLinkBasicNotification = _LgpMultiLinkBasicNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 7, 1)
)
if mibBuilder.loadTexts:
    lgpMultiLinkBasicNotification.setStatus("current")
_LgpPowerDistributionProducts_ObjectIdentity = ObjectIdentity
lgpPowerDistributionProducts = _LgpPowerDistributionProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8)
)
if mibBuilder.loadTexts:
    lgpPowerDistributionProducts.setStatus("current")
_LgpRackPDU_ObjectIdentity = ObjectIdentity
lgpRackPDU = _LgpRackPDU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 2)
)
if mibBuilder.loadTexts:
    lgpRackPDU.setStatus("current")
_LgpMPX_ObjectIdentity = ObjectIdentity
lgpMPX = _LgpMPX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    lgpMPX.setStatus("current")
_LgpMPH_ObjectIdentity = ObjectIdentity
lgpMPH = _LgpMPH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 4, 8, 2, 2)
)
if mibBuilder.loadTexts:
    lgpMPH.setStatus("current")
lgpFlexibleBasicEntry.registerAugmentions(
    ("LIEBERT-GP-MIB",
     "lgpFlexibleExtendedEntry")
)
lgpFlexibleExtendedEntry.setIndexNames(*lgpFlexibleBasicEntry.getIndexNames())

# Managed Objects groups


# Notification objects

lgpAgentDeviceCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 1)
)
lgpAgentDeviceCommunicationLost.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpAgentDeviceCommunicationLost.setStatus(
        "current"
    )

lgpAgentFirmwareUpdateSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 5)
)
lgpAgentFirmwareUpdateSuccessful.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpAgentFirmwareUpdateSuccessful.setStatus(
        "current"
    )

lgpAgentFirmwareCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 6)
)
lgpAgentFirmwareCorrupt.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpAgentFirmwareCorrupt.setStatus(
        "current"
    )

lgpAgentHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 7)
)
lgpAgentHeartbeat.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpConditionsPresent"),
        ("LIEBERT-GP-MIB", "lgpAgentConnectedDeviceCount"))
)
if mibBuilder.loadTexts:
    lgpAgentHeartbeat.setStatus(
        "current"
    )

lgpAgentDnsLookupFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 2, 3, 0, 8)
)
lgpAgentDnsLookupFailure.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpNetworkName"))
)
if mibBuilder.loadTexts:
    lgpAgentDnsLookupFailure.setStatus(
        "current"
    )

lgpEventConditionEntryAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 1)
)
lgpEventConditionEntryAdded.setObjects(
      *(("LIEBERT-GP-MIB", "lgpConditionId"),
        ("LIEBERT-GP-MIB", "lgpConditionDescr"),
        ("LIEBERT-GP-MIB", "lgpConditionTime"),
        ("LIEBERT-GP-MIB", "lgpConditionTableRef"),
        ("LIEBERT-GP-MIB", "lgpConditionTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventConditionEntryAdded.setStatus(
        "current"
    )

lgpEventConditionEntryRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 2)
)
lgpEventConditionEntryRemoved.setObjects(
      *(("LIEBERT-GP-MIB", "lgpConditionId"),
        ("LIEBERT-GP-MIB", "lgpConditionDescr"),
        ("LIEBERT-GP-MIB", "lgpConditionTime"),
        ("LIEBERT-GP-MIB", "lgpConditionTableRef"),
        ("LIEBERT-GP-MIB", "lgpConditionTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventConditionEntryRemoved.setStatus(
        "current"
    )

lgpEventLowBatteryWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 3)
)
lgpEventLowBatteryWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventLowBatteryWarning.setStatus(
        "current"
    )

lgpEventLoadTransferedToBypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 4)
)
lgpEventLoadTransferedToBypass.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventLoadTransferedToBypass.setStatus(
        "current"
    )

lgpEventInternalFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 5)
)
lgpEventInternalFault.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventInternalFault.setStatus(
        "current"
    )

lgpEventBatteryTestFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 6)
)
lgpEventBatteryTestFailed.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventBatteryTestFailed.setStatus(
        "current"
    )

lgpEventOutputOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 7)
)
lgpEventOutputOverload.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventOutputOverload.setStatus(
        "current"
    )

lgpEventEstablishedPowerRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 8)
)
lgpEventEstablishedPowerRedundancy.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventEstablishedPowerRedundancy.setStatus(
        "current"
    )

lgpEventLostPowerRedundancy = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 9)
)
lgpEventLostPowerRedundancy.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventLostPowerRedundancy.setStatus(
        "current"
    )

lgpEventPowerModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 10)
)
lgpEventPowerModuleFailure.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventPowerModuleFailure.setStatus(
        "current"
    )

lgpEventBatteryModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 11)
)
lgpEventBatteryModuleFailure.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventBatteryModuleFailure.setStatus(
        "current"
    )

lgpEventControlModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 12)
)
lgpEventControlModuleFailure.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventControlModuleFailure.setStatus(
        "current"
    )

lgpEventPowerModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 13)
)
lgpEventPowerModuleWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventPowerModuleWarning.setStatus(
        "current"
    )

lgpEventBatteryModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 14)
)
lgpEventBatteryModuleWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventBatteryModuleWarning.setStatus(
        "current"
    )

lgpEventControlModuleWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 15)
)
lgpEventControlModuleWarning.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventControlModuleWarning.setStatus(
        "current"
    )

lgpEventAgentFirmwareUpdateSuccessful = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 16)
)
lgpEventAgentFirmwareUpdateSuccessful.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventAgentFirmwareUpdateSuccessful.setStatus(
        "deprecated"
    )

lgpEventAgentFirmwareCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 17)
)
lgpEventAgentFirmwareCorrupt.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgpEventAgentFirmwareCorrupt.setStatus(
        "deprecated"
    )

lgpEventConfigModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 18)
)
lgpEventConfigModified.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventConfigModified.setStatus(
        "current"
    )

lgpEventModuleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 19)
)
lgpEventModuleAdded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventModuleAdded.setStatus(
        "current"
    )

lgpEventModuleRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 20)
)
lgpEventModuleRemoved.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventModuleRemoved.setStatus(
        "current"
    )

lgpEventRcpPowerStateChangeOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 21)
)
lgpEventRcpPowerStateChangeOn.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpPowerStateChangeOn.setStatus(
        "current"
    )

lgpEventRcpPowerStateChangeOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 22)
)
lgpEventRcpPowerStateChangeOff.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpPowerStateChangeOff.setStatus(
        "current"
    )

lgpEventRcpLoadAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 23)
)
lgpEventRcpLoadAdded.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpLoadAdded.setStatus(
        "current"
    )

lgpEventRcpLoadRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 24)
)
lgpEventRcpLoadRemoved.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRef"),
        ("LIEBERT-GP-MIB", "lgpEventParmTableRowRef"))
)
if mibBuilder.loadTexts:
    lgpEventRcpLoadRemoved.setStatus(
        "current"
    )

lgpSysNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 1)
)
lgpSysNotification.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpSysEventDescription"))
)
if mibBuilder.loadTexts:
    lgpSysNotification.setStatus(
        "current"
    )

lgpSysNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 2)
)
lgpSysNormal.setObjects(
      *(("SNMPv2-MIB", "sysUpTime"),
        ("LIEBERT-GP-MIB", "lgpAgentConnectedDeviceCount"))
)
if mibBuilder.loadTexts:
    lgpSysNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-GP-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertGlobalProducts": liebertGlobalProducts,
       "lgpModuleReg": lgpModuleReg,
       "liebertModuleReg": liebertModuleReg,
       "liebertGlobalProductsRegistrationModule": liebertGlobalProductsRegistrationModule,
       "liebertAgentModuleReg": liebertAgentModuleReg,
       "liebertAgentModule": liebertAgentModule,
       "liebertConditionsModuleReg": liebertConditionsModuleReg,
       "liebertGlobalProductsConditionsModule": liebertGlobalProductsConditionsModule,
       "liebertNotificationsModuleReg": liebertNotificationsModuleReg,
       "liebertGlobalProductsNotificationsModule": liebertGlobalProductsNotificationsModule,
       "liebertEnvironmentalModuleReg": liebertEnvironmentalModuleReg,
       "liebertGlobalProductsEnvironmentalModule": liebertGlobalProductsEnvironmentalModule,
       "liebertPowerModuleReg": liebertPowerModuleReg,
       "liebertGlobalProductsPowerModule": liebertGlobalProductsPowerModule,
       "liebertControllerModuleReg": liebertControllerModuleReg,
       "liebertControllerModule": liebertControllerModule,
       "liebertSystemModuleReg": liebertSystemModuleReg,
       "liebertSystemModule": liebertSystemModule,
       "liebertPduModuleReg": liebertPduModuleReg,
       "liebertGlobalProductsPduModule": liebertGlobalProductsPduModule,
       "liebertFlexibleModuleReg": liebertFlexibleModuleReg,
       "liebertGlobalProductsFlexibleModule": liebertGlobalProductsFlexibleModule,
       "liebertFlexibleConditionsModuleReg": liebertFlexibleConditionsModuleReg,
       "liebertGlobalProductsFlexibleConditionsModule": liebertGlobalProductsFlexibleConditionsModule,
       "lgpAgent": lgpAgent,
       "lgpAgentIdent": lgpAgentIdent,
       "lgpAgentIdentManufacturer": lgpAgentIdentManufacturer,
       "lgpAgentIdentModel": lgpAgentIdentModel,
       "lgpAgentIdentFirmwareVersion": lgpAgentIdentFirmwareVersion,
       "lgpAgentIdentSerialNumber": lgpAgentIdentSerialNumber,
       "lgpAgentIdentPartNumber": lgpAgentIdentPartNumber,
       "lgpAgentConnectedDeviceCount": lgpAgentConnectedDeviceCount,
       "lgpAgentNotifications": lgpAgentNotifications,
       "lgpAgentEventNotifications": lgpAgentEventNotifications,
       "lgpAgentDeviceCommunicationLost": lgpAgentDeviceCommunicationLost,
       "lgpAgentFirmwareUpdateSuccessful": lgpAgentFirmwareUpdateSuccessful,
       "lgpAgentFirmwareCorrupt": lgpAgentFirmwareCorrupt,
       "lgpAgentHeartbeat": lgpAgentHeartbeat,
       "lgpAgentDnsLookupFailure": lgpAgentDnsLookupFailure,
       "lgpAgentDevice": lgpAgentDevice,
       "lgpAgentManagedDeviceTable": lgpAgentManagedDeviceTable,
       "lgpAgentManagedDeviceEntry": lgpAgentManagedDeviceEntry,
       "lgpAgentDeviceIndex": lgpAgentDeviceIndex,
       "lgpAgentDeviceId": lgpAgentDeviceId,
       "lgpAgentDeviceManufacturer": lgpAgentDeviceManufacturer,
       "lgpAgentDeviceModel": lgpAgentDeviceModel,
       "lgpAgentDeviceFirmwareVersion": lgpAgentDeviceFirmwareVersion,
       "lgpAgentDeviceUnitNumber": lgpAgentDeviceUnitNumber,
       "lgpAgentDeviceSerialNumber": lgpAgentDeviceSerialNumber,
       "lgpAgentDeviceManufactureDate": lgpAgentDeviceManufactureDate,
       "lgpAgentDeviceServiceContact": lgpAgentDeviceServiceContact,
       "lgpAgentDeviceServicePhoneNumber": lgpAgentDeviceServicePhoneNumber,
       "lgpAgentDeviceServiceAddrLine1": lgpAgentDeviceServiceAddrLine1,
       "lgpAgentDeviceServiceAddrLine2": lgpAgentDeviceServiceAddrLine2,
       "lgpAgentDeviceServiceAddrLine3": lgpAgentDeviceServiceAddrLine3,
       "lgpAgentDeviceServiceAddrLine4": lgpAgentDeviceServiceAddrLine4,
       "lgpAgentDeviceUnitName": lgpAgentDeviceUnitName,
       "lgpAgentDeviceSiteIdentifier": lgpAgentDeviceSiteIdentifier,
       "lgpAgentDeviceTagNumber": lgpAgentDeviceTagNumber,
       "lgpAgentDeviceOrderLine1": lgpAgentDeviceOrderLine1,
       "lgpAgentDeviceOrderLine2": lgpAgentDeviceOrderLine2,
       "lgpAgentControl": lgpAgentControl,
       "lgpAgentReboot": lgpAgentReboot,
       "lgpFoundation": lgpFoundation,
       "lgpConditions": lgpConditions,
       "lgpConditionsWellKnown": lgpConditionsWellKnown,
       "lgpConditionHighTemperature": lgpConditionHighTemperature,
       "lgpConditionLowTemperature": lgpConditionLowTemperature,
       "lgpConditionHighHumidity": lgpConditionHighHumidity,
       "lgpConditionLowHumidity": lgpConditionLowHumidity,
       "lgpConditionLossOfAirflow": lgpConditionLossOfAirflow,
       "lgpConditionLossOfAirflow1": lgpConditionLossOfAirflow1,
       "lgpConditionLossOfAirflow2": lgpConditionLossOfAirflow2,
       "lgpConditionLossOfAirflowBlower1": lgpConditionLossOfAirflowBlower1,
       "lgpConditionLossOfAirflowAllBlowers": lgpConditionLossOfAirflowAllBlowers,
       "lgpConditionChangeFilter": lgpConditionChangeFilter,
       "lgpConditionCompressorHighHeadPressure": lgpConditionCompressorHighHeadPressure,
       "lgpConditionCompressor1HighHeadPressure": lgpConditionCompressor1HighHeadPressure,
       "lgpConditionCompressor1AHighHeadPressure": lgpConditionCompressor1AHighHeadPressure,
       "lgpConditionCompressor1BHighHeadPressure": lgpConditionCompressor1BHighHeadPressure,
       "lgpConditionCompressor2HighHeadPressure": lgpConditionCompressor2HighHeadPressure,
       "lgpConditionCompressor2AHighHeadPressure": lgpConditionCompressor2AHighHeadPressure,
       "lgpConditionCompressor2BHighHeadPressure": lgpConditionCompressor2BHighHeadPressure,
       "lgpConditionCompressor3HighHeadPressure": lgpConditionCompressor3HighHeadPressure,
       "lgpConditionCompressor4HighHeadPressure": lgpConditionCompressor4HighHeadPressure,
       "lgpConditionCompressorOverload": lgpConditionCompressorOverload,
       "lgpConditionCompressor1Overload": lgpConditionCompressor1Overload,
       "lgpConditionCompressor2Overload": lgpConditionCompressor2Overload,
       "lgpConditionCompressorShortCycle": lgpConditionCompressorShortCycle,
       "lgpConditionCompressor1ShortCycle": lgpConditionCompressor1ShortCycle,
       "lgpConditionCompressor1AShortCycle": lgpConditionCompressor1AShortCycle,
       "lgpConditionCompressor1BShortCycle": lgpConditionCompressor1BShortCycle,
       "lgpConditionCompressor2ShortCycle": lgpConditionCompressor2ShortCycle,
       "lgpConditionCompressor2AShortCycle": lgpConditionCompressor2AShortCycle,
       "lgpConditionCompressor2BShortCycle": lgpConditionCompressor2BShortCycle,
       "lgpConditionCompressorLowSuctionPressure": lgpConditionCompressorLowSuctionPressure,
       "lgpConditionCompressor1LowSuctionPressure": lgpConditionCompressor1LowSuctionPressure,
       "lgpConditionCompressor2LowSuctionPressure": lgpConditionCompressor2LowSuctionPressure,
       "lgpConditionMainFanOverLoad": lgpConditionMainFanOverLoad,
       "lgpConditionManualOverride": lgpConditionManualOverride,
       "lgpConditionStandbyGlycoolPumpOn": lgpConditionStandbyGlycoolPumpOn,
       "lgpConditionWaterUnderFloor": lgpConditionWaterUnderFloor,
       "lgpConditionHumidifierProblem": lgpConditionHumidifierProblem,
       "lgpConditionLowWaterInHumidifier": lgpConditionLowWaterInHumidifier,
       "lgpConditionSmokeDetected": lgpConditionSmokeDetected,
       "lgpConditionLowWaterFlow": lgpConditionLowWaterFlow,
       "lgpConditionLostPower": lgpConditionLostPower,
       "lgpGeneralFault": lgpGeneralFault,
       "lgpConditionLocalAlarm": lgpConditionLocalAlarm,
       "lgpConditionLocalAlarm1": lgpConditionLocalAlarm1,
       "lgpConditionLocalAlarm2": lgpConditionLocalAlarm2,
       "lgpConditionLocalAlarm3": lgpConditionLocalAlarm3,
       "lgpConditionLocalAlarm4": lgpConditionLocalAlarm4,
       "lgpConditionLocalAlarm5": lgpConditionLocalAlarm5,
       "lgpConditionLocalAlarm6": lgpConditionLocalAlarm6,
       "lgpConditionLocalAlarm7": lgpConditionLocalAlarm7,
       "lgpConditionLocalAlarm8": lgpConditionLocalAlarm8,
       "lgpConditionStandbyUnitOn": lgpConditionStandbyUnitOn,
       "lgpConditionCompressorLowPressure": lgpConditionCompressorLowPressure,
       "lgpConditionCompressor1LowPressure": lgpConditionCompressor1LowPressure,
       "lgpConditionTandemCompressorCircuit1LowPressure": lgpConditionTandemCompressorCircuit1LowPressure,
       "lgpConditionCompressor2LowPressure": lgpConditionCompressor2LowPressure,
       "lgpConditionTandemCompressorCircuit2LowPressure": lgpConditionTandemCompressorCircuit2LowPressure,
       "lgpConditionCompressor3LowPressure": lgpConditionCompressor3LowPressure,
       "lgpConditionCompressor4LowPressure": lgpConditionCompressor4LowPressure,
       "lgpConditionHighWaterInPan": lgpConditionHighWaterInPan,
       "lgpConditionFaultySensor": lgpConditionFaultySensor,
       "lgpConditionServiceCooling": lgpConditionServiceCooling,
       "lgpConditionServiceHumidifier": lgpConditionServiceHumidifier,
       "lgpConditionSystemControlBatteryLow": lgpConditionSystemControlBatteryLow,
       "lgpConditionGroundSystemFault": lgpConditionGroundSystemFault,
       "lgpConditionGroundFailure": lgpConditionGroundFailure,
       "lgpConditionSecurityBreach": lgpConditionSecurityBreach,
       "lgpConditionEmergencyShutdown": lgpConditionEmergencyShutdown,
       "lgpConditionOnBypass": lgpConditionOnBypass,
       "lgpConditionLoadOnBypass": lgpConditionLoadOnBypass,
       "lgpConditionLoadOnMaintenceBypass": lgpConditionLoadOnMaintenceBypass,
       "lgpConditionParallelSysLoadOnBypass": lgpConditionParallelSysLoadOnBypass,
       "lgpConditionLoadOnBypassByImpact": lgpConditionLoadOnBypassByImpact,
       "lgpConditionLoadTransferedToBypass": lgpConditionLoadTransferedToBypass,
       "lgpConditionEmergencyTransferToBypass": lgpConditionEmergencyTransferToBypass,
       "lgpConditionOutputToLoadVoltTHD": lgpConditionOutputToLoadVoltTHD,
       "lgpConditionLogicFailure": lgpConditionLogicFailure,
       "lgpConditionPowerSupplyFault": lgpConditionPowerSupplyFault,
       "lgpConditionPowerSupply1Fault": lgpConditionPowerSupply1Fault,
       "lgpConditionPowerSupply2Fault": lgpConditionPowerSupply2Fault,
       "lgpConditionPowerSupplyFailure": lgpConditionPowerSupplyFailure,
       "lgpConditionPowerSupply1Failure": lgpConditionPowerSupply1Failure,
       "lgpConditionPowerSupply2Failure": lgpConditionPowerSupply2Failure,
       "lgpConditionSource1PowerSupplyInputFailure": lgpConditionSource1PowerSupplyInputFailure,
       "lgpConditionSource2PowerSupplyInputFailure": lgpConditionSource2PowerSupplyInputFailure,
       "lgpConditionPowerSupplyLogicFailure": lgpConditionPowerSupplyLogicFailure,
       "lgpConditionCompressorPowerSupplyFailure": lgpConditionCompressorPowerSupplyFailure,
       "lgpConditionOverVoltage": lgpConditionOverVoltage,
       "lgpConditionSource1OverVoltage": lgpConditionSource1OverVoltage,
       "lgpConditionSource2OverVoltage": lgpConditionSource2OverVoltage,
       "lgpConditionOutputToLoadOverVoltage": lgpConditionOutputToLoadOverVoltage,
       "lgpConditionInputOverVoltage": lgpConditionInputOverVoltage,
       "lgpConditionBypassOverVoltage": lgpConditionBypassOverVoltage,
       "lgpConditionBypassOverVoltageFailure": lgpConditionBypassOverVoltageFailure,
       "lgpConditionBatteryOverVoltage": lgpConditionBatteryOverVoltage,
       "lgpConditionDcBusOverVoltage": lgpConditionDcBusOverVoltage,
       "lgpConditionDcBus1OverVoltage": lgpConditionDcBus1OverVoltage,
       "lgpConditionDcBus2OverVoltage": lgpConditionDcBus2OverVoltage,
       "lgpConditionDcBus1OverVoltageFailure": lgpConditionDcBus1OverVoltageFailure,
       "lgpConditionDcBus2OverVoltageFailure": lgpConditionDcBus2OverVoltageFailure,
       "lgpConditionUnderVoltage": lgpConditionUnderVoltage,
       "lgpConditionSource1UnderVoltage": lgpConditionSource1UnderVoltage,
       "lgpConditionSource2UnderVoltage": lgpConditionSource2UnderVoltage,
       "lgpConditionOutputToLoadUnderVoltage": lgpConditionOutputToLoadUnderVoltage,
       "lgpConditionSource1UnderVoltageRMS": lgpConditionSource1UnderVoltageRMS,
       "lgpConditionSource2UnderVoltageRMS": lgpConditionSource2UnderVoltageRMS,
       "lgpConditionInputUnderVoltage": lgpConditionInputUnderVoltage,
       "lgpConditionBypassUnderVoltage": lgpConditionBypassUnderVoltage,
       "lgpConditionBypassUnderVoltageFailure": lgpConditionBypassUnderVoltageFailure,
       "lgpConditionBatteryUnderVoltage": lgpConditionBatteryUnderVoltage,
       "lgpConditionDcBusUnderVoltage": lgpConditionDcBusUnderVoltage,
       "lgpConditionDcBus1UnderVoltage": lgpConditionDcBus1UnderVoltage,
       "lgpConditionDcBus2UnderVoltage": lgpConditionDcBus2UnderVoltage,
       "lgpConditionDcBus1UnderVoltageFailure": lgpConditionDcBus1UnderVoltageFailure,
       "lgpConditionDcBus2UnderVoltageFailure": lgpConditionDcBus2UnderVoltageFailure,
       "lgpConditionOverload": lgpConditionOverload,
       "lgpConditionSource1Overload": lgpConditionSource1Overload,
       "lgpConditionSystemOverload": lgpConditionSystemOverload,
       "lgpConditionSource1PeakCurrentOverLoad": lgpConditionSource1PeakCurrentOverLoad,
       "lgpConditionSource2PeakCurrentOverLoad": lgpConditionSource2PeakCurrentOverLoad,
       "lgpConditionOutputToLoadOverLimit": lgpConditionOutputToLoadOverLimit,
       "lgpConditionOutputToLoadOverload": lgpConditionOutputToLoadOverload,
       "lgpConditionParallelSysOverload": lgpConditionParallelSysOverload,
       "lgpConditionBypassCurrentOverload": lgpConditionBypassCurrentOverload,
       "lgpConditionBypassCurrentOverloadPhsA": lgpConditionBypassCurrentOverloadPhsA,
       "lgpConditionBypassCurrentOverloadPhsB": lgpConditionBypassCurrentOverloadPhsB,
       "lgpConditionBypassCurrentOverloadPhsC": lgpConditionBypassCurrentOverloadPhsC,
       "lgpConditionScrShort": lgpConditionScrShort,
       "lgpConditionSource1ScrShort": lgpConditionSource1ScrShort,
       "lgpConditionSource2ScrShort": lgpConditionSource2ScrShort,
       "lgpConditionBypassScrShort": lgpConditionBypassScrShort,
       "lgpConditionInvStaticSwScrShort": lgpConditionInvStaticSwScrShort,
       "lgpConditionSource1NeutralScrShort": lgpConditionSource1NeutralScrShort,
       "lgpConditionSource2NeutralScrShort": lgpConditionSource2NeutralScrShort,
       "lgpConditionScrOpen": lgpConditionScrOpen,
       "lgpConditionSource1ScrOpen": lgpConditionSource1ScrOpen,
       "lgpConditionSource2ScrOpen": lgpConditionSource2ScrOpen,
       "lgpConditionBypassScrOpen": lgpConditionBypassScrOpen,
       "lgpConditionSource1NeutralScrOpen": lgpConditionSource1NeutralScrOpen,
       "lgpConditionSource2NeutralScrOpen": lgpConditionSource2NeutralScrOpen,
       "lgpConditionFanFailure": lgpConditionFanFailure,
       "lgpConditionFan1Failure": lgpConditionFan1Failure,
       "lgpConditionRedundantFanFailure": lgpConditionRedundantFanFailure,
       "lgpConditionMultipleFanFailure": lgpConditionMultipleFanFailure,
       "lgpConditionBlowerFanFailure": lgpConditionBlowerFanFailure,
       "lgpConditionBottomBlowerFanFailure": lgpConditionBottomBlowerFanFailure,
       "lgpConditionTopBlowerFanFailure": lgpConditionTopBlowerFanFailure,
       "lgpConditionCondenserFanVFDFailure": lgpConditionCondenserFanVFDFailure,
       "lgpConditionFanPowerFailure": lgpConditionFanPowerFailure,
       "lgpConditionTransferInhibited": lgpConditionTransferInhibited,
       "lgpConditionAutoReTransferPrimed": lgpConditionAutoReTransferPrimed,
       "lgpConditionSourcesOutOfSync": lgpConditionSourcesOutOfSync,
       "lgpConditionSourceFailure": lgpConditionSourceFailure,
       "lgpConditionSource1Failure": lgpConditionSource1Failure,
       "lgpConditionSource2Failure": lgpConditionSource2Failure,
       "lgpConditionAutoReTransferInhibited": lgpConditionAutoReTransferInhibited,
       "lgpConditionAutoReTransferFailed": lgpConditionAutoReTransferFailed,
       "lgpConditionFuseOpen": lgpConditionFuseOpen,
       "lgpConditionControlFuse1Open": lgpConditionControlFuse1Open,
       "lgpConditionControlFuse2Open": lgpConditionControlFuse2Open,
       "lgpConditionRectifierFuseOpen": lgpConditionRectifierFuseOpen,
       "lgpConditionInverterFuseOpen": lgpConditionInverterFuseOpen,
       "lgpConditionOutputToLoadFuseOpen": lgpConditionOutputToLoadFuseOpen,
       "lgpConditionDcCapacitorFuseOpen": lgpConditionDcCapacitorFuseOpen,
       "lgpConditionDisconnect": lgpConditionDisconnect,
       "lgpConditionSource1DisconnectOpen": lgpConditionSource1DisconnectOpen,
       "lgpConditionSource2DisconnectOpen": lgpConditionSource2DisconnectOpen,
       "lgpConditionSource1PduDisconnectOpen": lgpConditionSource1PduDisconnectOpen,
       "lgpConditionSource2PduDisconnectOpen": lgpConditionSource2PduDisconnectOpen,
       "lgpConditionOutputToLoadDisconnect1Open": lgpConditionOutputToLoadDisconnect1Open,
       "lgpConditionOutputToLoadDisconnect2Open": lgpConditionOutputToLoadDisconnect2Open,
       "lgpConditionSource1BypassDisconnectClosed": lgpConditionSource1BypassDisconnectClosed,
       "lgpConditionSource2BypassDisconnectClosed": lgpConditionSource2BypassDisconnectClosed,
       "lgpConditionOutputToLoadNeutralDisconnectOpen": lgpConditionOutputToLoadNeutralDisconnectOpen,
       "lgpConditionBatteryDisconnectOpen": lgpConditionBatteryDisconnectOpen,
       "lgpConditionBatteryDiscOpenCab01": lgpConditionBatteryDiscOpenCab01,
       "lgpConditionBatteryDiscOpenCab02": lgpConditionBatteryDiscOpenCab02,
       "lgpConditionBatteryDiscOpenCab03": lgpConditionBatteryDiscOpenCab03,
       "lgpConditionBatteryDiscOpenCab04": lgpConditionBatteryDiscOpenCab04,
       "lgpConditionBatteryDiscOpenCab05": lgpConditionBatteryDiscOpenCab05,
       "lgpConditionBatteryDiscOpenCab06": lgpConditionBatteryDiscOpenCab06,
       "lgpConditionBatteryDiscOpenCab07": lgpConditionBatteryDiscOpenCab07,
       "lgpConditionBatteryDiscOpenCab08": lgpConditionBatteryDiscOpenCab08,
       "lgpConditionInputDisconnectOpen": lgpConditionInputDisconnectOpen,
       "lgpConditionOutputToLoadDisconnectOpen": lgpConditionOutputToLoadDisconnectOpen,
       "lgpConditionBypassDisconnectOpen": lgpConditionBypassDisconnectOpen,
       "lgpConditionStaticSwitchDisconnectOpen": lgpConditionStaticSwitchDisconnectOpen,
       "lgpConditionBreakerOpenFailure": lgpConditionBreakerOpenFailure,
       "lgpConditionBreakerCloseFailure": lgpConditionBreakerCloseFailure,
       "lgpConditionFrequencyDeviation": lgpConditionFrequencyDeviation,
       "lgpConditionSource1FrequencyDeviation": lgpConditionSource1FrequencyDeviation,
       "lgpConditionSource2FrequencyDeviation": lgpConditionSource2FrequencyDeviation,
       "lgpConditionInputFrequencyDeviation": lgpConditionInputFrequencyDeviation,
       "lgpConditionOutputToLoadFrequencyDeviation": lgpConditionOutputToLoadFrequencyDeviation,
       "lgpConditionBypassFrequencyDeviation": lgpConditionBypassFrequencyDeviation,
       "lgpConditionOverCurrent": lgpConditionOverCurrent,
       "lgpConditionSource1OverCurrent": lgpConditionSource1OverCurrent,
       "lgpConditionSource2OverCurrent": lgpConditionSource2OverCurrent,
       "lgpConditionOutputToLoadOverCurrent": lgpConditionOutputToLoadOverCurrent,
       "lgpConditionOutputToLoadOverCurrentPhsA": lgpConditionOutputToLoadOverCurrentPhsA,
       "lgpConditionOutputToLoadOverCurrentPhsB": lgpConditionOutputToLoadOverCurrentPhsB,
       "lgpConditionOutputToLoadOverCurrentPhsC": lgpConditionOutputToLoadOverCurrentPhsC,
       "lgpConditionGroundOverCurrent": lgpConditionGroundOverCurrent,
       "lgpConditionRectifierOverCurrent": lgpConditionRectifierOverCurrent,
       "lgpConditionInverterOverCurrent": lgpConditionInverterOverCurrent,
       "lgpConditionInverterOverCurrentPhsA": lgpConditionInverterOverCurrentPhsA,
       "lgpConditionInverterOverCurrentPhsB": lgpConditionInverterOverCurrentPhsB,
       "lgpConditionInverterOverCurrentPhsC": lgpConditionInverterOverCurrentPhsC,
       "lgpConditionBatteryConverterOverCurrent": lgpConditionBatteryConverterOverCurrent,
       "lgpConditionBatteryBalancerOverCurrent": lgpConditionBatteryBalancerOverCurrent,
       "lgpConditionHumidifierOverCurrent": lgpConditionHumidifierOverCurrent,
       "lgpConditionInputOverCurrent": lgpConditionInputOverCurrent,
       "lgpConditionSource1NeutralOverCurrent": lgpConditionSource1NeutralOverCurrent,
       "lgpConditionSource2NeutralOverCurrent": lgpConditionSource2NeutralOverCurrent,
       "lgpConditionSensorFailure": lgpConditionSensorFailure,
       "lgpConditionOutputToLoadVoltageSensorFailure": lgpConditionOutputToLoadVoltageSensorFailure,
       "lgpConditionSource1VoltageSensorFailure": lgpConditionSource1VoltageSensorFailure,
       "lgpConditionSource2VoltageSensorFailure": lgpConditionSource2VoltageSensorFailure,
       "lgpConditionSource1ScrSensorFailure": lgpConditionSource1ScrSensorFailure,
       "lgpConditionSource2ScrSensorFailure": lgpConditionSource2ScrSensorFailure,
       "lgpConditionSource1CurrentSensorFailure": lgpConditionSource1CurrentSensorFailure,
       "lgpConditionSource2CurrentSensorFailure": lgpConditionSource2CurrentSensorFailure,
       "lgpConditionRoomTempHumiditySensorFailure": lgpConditionRoomTempHumiditySensorFailure,
       "lgpConditionGlycolTempSensorFailure": lgpConditionGlycolTempSensorFailure,
       "lgpConditionLocal1SensorFailure": lgpConditionLocal1SensorFailure,
       "lgpConditionCompressor1SensorFailure": lgpConditionCompressor1SensorFailure,
       "lgpConditionCompressor2SensorFailure": lgpConditionCompressor2SensorFailure,
       "lgpConditionSupplySensorFailure": lgpConditionSupplySensorFailure,
       "lgpConditionCabinetTemperatureSensorFailure": lgpConditionCabinetTemperatureSensorFailure,
       "lgpConditionCabinetHumiditySensorFailure": lgpConditionCabinetHumiditySensorFailure,
       "lgpConditionRoomTempSensorFailure": lgpConditionRoomTempSensorFailure,
       "lgpConditionBatteryTempSensorFailure": lgpConditionBatteryTempSensorFailure,
       "lgpConditionAirSensorAFailure": lgpConditionAirSensorAFailure,
       "lgpConditionAirSensorBFailure": lgpConditionAirSensorBFailure,
       "lgpConditionChilledWaterSupplySensorFailure": lgpConditionChilledWaterSupplySensorFailure,
       "lgpConditionRefrigerantSupplySensorFailure": lgpConditionRefrigerantSupplySensorFailure,
       "lgpConditionFluidSupplySensorFailure": lgpConditionFluidSupplySensorFailure,
       "lgpConditionCompressorLowPressureSensorFailure": lgpConditionCompressorLowPressureSensorFailure,
       "lgpConditionCompressor1LowPressureSensorFailure": lgpConditionCompressor1LowPressureSensorFailure,
       "lgpConditionRemoteSensorFailure": lgpConditionRemoteSensorFailure,
       "lgpConditionAirSupplyTempSensorFailure": lgpConditionAirSupplyTempSensorFailure,
       "lgpConditionAirReturnTempSensorFailure": lgpConditionAirReturnTempSensorFailure,
       "lgpConditionCompressorHighPressureSensorFailure": lgpConditionCompressorHighPressureSensorFailure,
       "lgpConditionInternalCommunicationFailure": lgpConditionInternalCommunicationFailure,
       "lgpConditionExternalCommunicationFailure": lgpConditionExternalCommunicationFailure,
       "lgpConditionSourceGateDriveFailure": lgpConditionSourceGateDriveFailure,
       "lgpConditionSource1GateDriveFailure": lgpConditionSource1GateDriveFailure,
       "lgpConditionSource2GateDriveFailure": lgpConditionSource2GateDriveFailure,
       "lgpConditionDisconnectFailure": lgpConditionDisconnectFailure,
       "lgpConditionOutputToLoadNeutralDisconnectFailure": lgpConditionOutputToLoadNeutralDisconnectFailure,
       "lgpConditionSource1DisconnectShuntTripFailure": lgpConditionSource1DisconnectShuntTripFailure,
       "lgpConditionSource2DisconnectShuntTripFailure": lgpConditionSource2DisconnectShuntTripFailure,
       "lgpConditionInverterDisconnectFailure": lgpConditionInverterDisconnectFailure,
       "lgpConditionBatteryDisconnectFailure": lgpConditionBatteryDisconnectFailure,
       "lgpConditionRectifierDisconnectFailure": lgpConditionRectifierDisconnectFailure,
       "lgpConditionOverTemperature": lgpConditionOverTemperature,
       "lgpConditionHeatSink1OverTemperature": lgpConditionHeatSink1OverTemperature,
       "lgpConditionAmbient1OverTemperature": lgpConditionAmbient1OverTemperature,
       "lgpConditionSystemOverTemperature": lgpConditionSystemOverTemperature,
       "lgpConditionTransformerOverTemperature": lgpConditionTransformerOverTemperature,
       "lgpConditionBatteryOverTemperature": lgpConditionBatteryOverTemperature,
       "lgpConditionRectifierOverTemperature": lgpConditionRectifierOverTemperature,
       "lgpConditionInverterOverTemperature": lgpConditionInverterOverTemperature,
       "lgpConditionRectifierInductorOverTemperature": lgpConditionRectifierInductorOverTemperature,
       "lgpConditionInverterInductorOverTemperature": lgpConditionInverterInductorOverTemperature,
       "lgpConditionBatteryConverterOverTemperature": lgpConditionBatteryConverterOverTemperature,
       "lgpConditionBatteryBalancerInductorOverTemperature": lgpConditionBatteryBalancerInductorOverTemperature,
       "lgpConditionChilledWaterOverTemperature": lgpConditionChilledWaterOverTemperature,
       "lgpConditionElectricHeatersOverTemperature": lgpConditionElectricHeatersOverTemperature,
       "lgpConditionInletAirOverTemperature": lgpConditionInletAirOverTemperature,
       "lgpConditionSystemOverTempWarning": lgpConditionSystemOverTempWarning,
       "lgpConditionHighTemperatureBattString": lgpConditionHighTemperatureBattString,
       "lgpConditionLoadOnAlternateSource": lgpConditionLoadOnAlternateSource,
       "lgpConditionPhaseRotationError": lgpConditionPhaseRotationError,
       "lgpConditionSource1PhaseRotationError": lgpConditionSource1PhaseRotationError,
       "lgpConditionSource2PhaseRotationError": lgpConditionSource2PhaseRotationError,
       "lgpConditionBypassPhaseRotationError": lgpConditionBypassPhaseRotationError,
       "lgpConditionInputPhaseRotationError": lgpConditionInputPhaseRotationError,
       "lgpConditionControlModuleFailure": lgpConditionControlModuleFailure,
       "lgpConditionControlModule1Failure": lgpConditionControlModule1Failure,
       "lgpConditionHistoryLogFull": lgpConditionHistoryLogFull,
       "lgpConditionConfigurationModified": lgpConditionConfigurationModified,
       "lgpConditionPasswordModified": lgpConditionPasswordModified,
       "lgpConditionTimeModified": lgpConditionTimeModified,
       "lgpConditionDateModified": lgpConditionDateModified,
       "lgpConditionEventLogCleared": lgpConditionEventLogCleared,
       "lgpConditionHistoryLogCleared": lgpConditionHistoryLogCleared,
       "lgpConditionUtilityFailure": lgpConditionUtilityFailure,
       "lgpConditionBatteryTestInProgress": lgpConditionBatteryTestInProgress,
       "lgpConditionLoadOnBattery": lgpConditionLoadOnBattery,
       "lgpConditionReplaceBattery": lgpConditionReplaceBattery,
       "lgpConditionUpsShutdownPending": lgpConditionUpsShutdownPending,
       "lgpConditionBatteryChargerFailed": lgpConditionBatteryChargerFailed,
       "lgpConditionBypassVoltageUnqualified": lgpConditionBypassVoltageUnqualified,
       "lgpConditionCheckAirFilter": lgpConditionCheckAirFilter,
       "lgpConditionBrownOut": lgpConditionBrownOut,
       "lgpConditionMultipleTransferLockout": lgpConditionMultipleTransferLockout,
       "lgpConditionBypassPhaseLost": lgpConditionBypassPhaseLost,
       "lgpConditionMaintenceBypassInhibited": lgpConditionMaintenceBypassInhibited,
       "lgpConditionLoadLockedOnBypass": lgpConditionLoadLockedOnBypass,
       "lgpConditionOutputToLoadShort": lgpConditionOutputToLoadShort,
       "lgpConditionEmergencyTransferToInverter": lgpConditionEmergencyTransferToInverter,
       "lgpConditonEmergencyPowerOff": lgpConditonEmergencyPowerOff,
       "lgpConditionInverterBackFeed": lgpConditionInverterBackFeed,
       "lgpConditionDcGroundFault": lgpConditionDcGroundFault,
       "lgpConditionDcGroundFaultPos": lgpConditionDcGroundFaultPos,
       "lgpConditionDcGroundFaultNeg": lgpConditionDcGroundFaultNeg,
       "lgpConditionStaticTransferSwitchInhibited": lgpConditionStaticTransferSwitchInhibited,
       "lgpConditionBatteryLogFullWarning": lgpConditionBatteryLogFullWarning,
       "lgpConditionInputCurrentUnbalanced": lgpConditionInputCurrentUnbalanced,
       "lgpConditionSelfTestFailed": lgpConditionSelfTestFailed,
       "lgpConditionInverterOutOfSynchronization": lgpConditionInverterOutOfSynchronization,
       "lgpConditionModuleAlarm": lgpConditionModuleAlarm,
       "lgpConditioniModuleUnit1Alarm": lgpConditioniModuleUnit1Alarm,
       "lgpConditioniModuleUnit2Alarm": lgpConditioniModuleUnit2Alarm,
       "lgpConditioniModuleUnit3Alarm": lgpConditioniModuleUnit3Alarm,
       "lgpConditioniModuleUnit4Alarm": lgpConditioniModuleUnit4Alarm,
       "lgpConditioniModuleUnit5Alarm": lgpConditioniModuleUnit5Alarm,
       "lgpConditioniModuleUnit6Alarm": lgpConditioniModuleUnit6Alarm,
       "lgpConditioniModuleUnit7Alarm": lgpConditioniModuleUnit7Alarm,
       "lgpConditioniModuleUnit8Alarm": lgpConditioniModuleUnit8Alarm,
       "lgpConditionActiveModuleAlarm": lgpConditionActiveModuleAlarm,
       "lgpConditionControlFailure": lgpConditionControlFailure,
       "lgpConditionMainControlFailure": lgpConditionMainControlFailure,
       "lgpConditionRedundantControlFailure": lgpConditionRedundantControlFailure,
       "lgpConditionParallelSysControlFailure": lgpConditionParallelSysControlFailure,
       "lgpConditionMainControlCommFailure": lgpConditionMainControlCommFailure,
       "lgpConditionControlBoardFailure": lgpConditionControlBoardFailure,
       "lgpConditionHumidifierControlBdFailure": lgpConditionHumidifierControlBdFailure,
       "lgpConditionControlWarning": lgpConditionControlWarning,
       "lgpConditionMainControlWarning": lgpConditionMainControlWarning,
       "lgpConditionRedundantControlWarning": lgpConditionRedundantControlWarning,
       "lgpConditionUserInterfaceFailure": lgpConditionUserInterfaceFailure,
       "lgpConditionLostPowerRedundancy": lgpConditionLostPowerRedundancy,
       "lgpConditionPowerModuleFailure": lgpConditionPowerModuleFailure,
       "lgpConditionBatteryModuleFailure": lgpConditionBatteryModuleFailure,
       "lgpConditionOutputToLoadOff": lgpConditionOutputToLoadOff,
       "lgpConditionSystemOff": lgpConditionSystemOff,
       "lgpConditionRectifierStartupFailure": lgpConditionRectifierStartupFailure,
       "lgpConditionRectifierFault": lgpConditionRectifierFault,
       "lgpConditionInverterShutdownLowDc": lgpConditionInverterShutdownLowDc,
       "lgpConditionInverterFault": lgpConditionInverterFault,
       "lgpConditionInverterDcOffsetOverrun": lgpConditionInverterDcOffsetOverrun,
       "lgpConditionParallelSysLowBatteryWarning": lgpConditionParallelSysLowBatteryWarning,
       "lgpConditionParallelSysLoadShareFault": lgpConditionParallelSysLoadShareFault,
       "lgpConditionBatteryFault": lgpConditionBatteryFault,
       "lgpConditionBatteryConverterFailure": lgpConditionBatteryConverterFailure,
       "lgpConditionBatteryBalancerFault": lgpConditionBatteryBalancerFault,
       "lgpConditionpsUpsOperationFault": lgpConditionpsUpsOperationFault,
       "lgpConditionOutputToLoadOnJointMode": lgpConditionOutputToLoadOnJointMode,
       "lgpConditionInputNeutralLost": lgpConditionInputNeutralLost,
       "lgpConditionLowBatteryWarning": lgpConditionLowBatteryWarning,
       "lgpConditionInternalFault": lgpConditionInternalFault,
       "lgpConditionBatteryTestFailed": lgpConditionBatteryTestFailed,
       "lgpConditionPowerModuleWarning": lgpConditionPowerModuleWarning,
       "lgpConditionBatteryModuleWarning": lgpConditionBatteryModuleWarning,
       "lgpConditionControlModuleWarning": lgpConditionControlModuleWarning,
       "lgpConditionUpsOperationFault": lgpConditionUpsOperationFault,
       "lgpConditionActiveAlarm": lgpConditionActiveAlarm,
       "lgpConditionRectifierCommunicationFailure": lgpConditionRectifierCommunicationFailure,
       "lgpConditionInverterCommunicationFailure": lgpConditionInverterCommunicationFailure,
       "lgpConditionParallelSysConnectionFault": lgpConditionParallelSysConnectionFault,
       "lgpConditionParallelSysCommunicationFailure": lgpConditionParallelSysCommunicationFailure,
       "lgpConditionLostBatteryRedundancy": lgpConditionLostBatteryRedundancy,
       "lgpConditionCompPumpDownFailure": lgpConditionCompPumpDownFailure,
       "lgpConditionComp1PumpDownFailure": lgpConditionComp1PumpDownFailure,
       "lgpConditionComp2PumpDownFailure": lgpConditionComp2PumpDownFailure,
       "lgpConditionChilledWaterLowWaterFlow": lgpConditionChilledWaterLowWaterFlow,
       "lgpConditionAirFilterClogged": lgpConditionAirFilterClogged,
       "lgpConditionHumidifierFailure": lgpConditionHumidifierFailure,
       "lgpConditionRunHoursExceeded": lgpConditionRunHoursExceeded,
       "lgpConditionUnitRunHrsExceeded": lgpConditionUnitRunHrsExceeded,
       "lgpConditionComp1RunHrsExceeded": lgpConditionComp1RunHrsExceeded,
       "lgpConditionComp2RunHrsExceeded": lgpConditionComp2RunHrsExceeded,
       "lgpConditionFreeCoolRunHrsExceeded": lgpConditionFreeCoolRunHrsExceeded,
       "lgpConditionElectricalHeater1RunHrsExceeded": lgpConditionElectricalHeater1RunHrsExceeded,
       "lgpConditionElectricalHeater2RunHrsExceeded": lgpConditionElectricalHeater2RunHrsExceeded,
       "lgpConditionElectricalHeater3RunHrsExceeded": lgpConditionElectricalHeater3RunHrsExceeded,
       "lgpConditionHotWaterRunHrsExceeded": lgpConditionHotWaterRunHrsExceeded,
       "lgpConditionHotGasRunHrsExceeded": lgpConditionHotGasRunHrsExceeded,
       "lgpConditionHumidifierRunHrsExceeded": lgpConditionHumidifierRunHrsExceeded,
       "lgpConditionDehumidiferRunHrsExceeded": lgpConditionDehumidiferRunHrsExceeded,
       "lgpConditionFanRunHrsExceeded": lgpConditionFanRunHrsExceeded,
       "lgpConditionCommWarning": lgpConditionCommWarning,
       "lgpConditionCommWarningUnit1": lgpConditionCommWarningUnit1,
       "lgpConditionCommWarningUnit2": lgpConditionCommWarningUnit2,
       "lgpConditionCommWarningUnit3": lgpConditionCommWarningUnit3,
       "lgpConditionCommWarningUnit4": lgpConditionCommWarningUnit4,
       "lgpConditionCommWarningUnit5": lgpConditionCommWarningUnit5,
       "lgpConditionCommWarningUnit6": lgpConditionCommWarningUnit6,
       "lgpConditionCommWarningUnit7": lgpConditionCommWarningUnit7,
       "lgpConditionCommWarningUnit8": lgpConditionCommWarningUnit8,
       "lgpConditionCommWarningUnit9": lgpConditionCommWarningUnit9,
       "lgpConditionCommWarningUnit10": lgpConditionCommWarningUnit10,
       "lgpConditionCommWarningUnit11": lgpConditionCommWarningUnit11,
       "lgpConditionCommWarningUnit12": lgpConditionCommWarningUnit12,
       "lgpConditionCommWarningUnit13": lgpConditionCommWarningUnit13,
       "lgpConditionCommWarningUnit14": lgpConditionCommWarningUnit14,
       "lgpConditionCommWarningUnit15": lgpConditionCommWarningUnit15,
       "lgpConditionCommWarningUnit16": lgpConditionCommWarningUnit16,
       "lgpConditionUnitOn": lgpConditionUnitOn,
       "lgpConditionUnitOff": lgpConditionUnitOff,
       "lgpConditionSleepModeOff": lgpConditionSleepModeOff,
       "lgpConditionPowerOn": lgpConditionPowerOn,
       "lgpConditionSystemOnStanby": lgpConditionSystemOnStanby,
       "lgpConditionPowerOff": lgpConditionPowerOff,
       "lgpConditionHighTemperatureGroup": lgpConditionHighTemperatureGroup,
       "lgpConditionHighTemperatureSensor1": lgpConditionHighTemperatureSensor1,
       "lgpConditionHighTemperatureDigitalScroll1": lgpConditionHighTemperatureDigitalScroll1,
       "lgpConditionHighTemperatureDigitalScroll2": lgpConditionHighTemperatureDigitalScroll2,
       "lgpConditionHighTemperatureUser1": lgpConditionHighTemperatureUser1,
       "lgpConditionHighTemperatureInternal": lgpConditionHighTemperatureInternal,
       "lgpConditionHighTemperatureExternalAirSensorA": lgpConditionHighTemperatureExternalAirSensorA,
       "lgpConditionHighTemperatureExternalAirSensorB": lgpConditionHighTemperatureExternalAirSensorB,
       "lgpConditionHighTemperatureRefrigerantSupply": lgpConditionHighTemperatureRefrigerantSupply,
       "lgpConditionHighTemperatureFluidSupply": lgpConditionHighTemperatureFluidSupply,
       "lgpConditionHighTemperatureSupplyAir": lgpConditionHighTemperatureSupplyAir,
       "lgpConditionHighTemperatureReturnAir": lgpConditionHighTemperatureReturnAir,
       "lgpConditionLowTemperatureGroup": lgpConditionLowTemperatureGroup,
       "lgpConditionLowTemperatureSensor1": lgpConditionLowTemperatureSensor1,
       "lgpConditionLowTemperatureInternal": lgpConditionLowTemperatureInternal,
       "lgpConditionLowTemperatureExternalAirSensorA": lgpConditionLowTemperatureExternalAirSensorA,
       "lgpConditionLowTemperatureExternalAirSensorB": lgpConditionLowTemperatureExternalAirSensorB,
       "lgpConditionLowTemperatureRefrigerantSupply": lgpConditionLowTemperatureRefrigerantSupply,
       "lgpConditionLowTemperatureFluidSupply": lgpConditionLowTemperatureFluidSupply,
       "lgpConditionLowTemperatureSupplyAir": lgpConditionLowTemperatureSupplyAir,
       "lgpConditionHighHumidityGroup": lgpConditionHighHumidityGroup,
       "lgpConditionHighHumiditySensor1": lgpConditionHighHumiditySensor1,
       "lgpConditionHighHumidityReturnAir": lgpConditionHighHumidityReturnAir,
       "lgpConditionLowHumidityGroup": lgpConditionLowHumidityGroup,
       "lgpConditionLowHumiditySensor1": lgpConditionLowHumiditySensor1,
       "lgpConditionLowHumidityReturnAir": lgpConditionLowHumidityReturnAir,
       "lgpConditionPeerNetworkNoMaster": lgpConditionPeerNetworkNoMaster,
       "lgpConditionNoOnOffPermissions": lgpConditionNoOnOffPermissions,
       "lgpConditionPeerNetworkFailure": lgpConditionPeerNetworkFailure,
       "lgpConditionUnitDisabled": lgpConditionUnitDisabled,
       "lgpConditionUnitShutdown": lgpConditionUnitShutdown,
       "lgpConditionPeerNetworkDiscovered": lgpConditionPeerNetworkDiscovered,
       "lgpConditionLossOfWaterFlow": lgpConditionLossOfWaterFlow,
       "lgpConditionCondensatePumpHighWater": lgpConditionCondensatePumpHighWater,
       "lgpConditionGeneralAlarm": lgpConditionGeneralAlarm,
       "lgpConditionProductSpecific": lgpConditionProductSpecific,
       "lgpConditionReheatLockout": lgpConditionReheatLockout,
       "lgpConditionHumidifierLockout": lgpConditionHumidifierLockout,
       "lgpConditionCompressorsLockout": lgpConditionCompressorsLockout,
       "lgpConditionCallService": lgpConditionCallService,
       "lgpConditionLowMemoryGroup": lgpConditionLowMemoryGroup,
       "lgpConditionLowMemory1": lgpConditionLowMemory1,
       "lgpConditionMemoryFailureGroup": lgpConditionMemoryFailureGroup,
       "lgpConditionMemory1Failure": lgpConditionMemory1Failure,
       "lgpConditionMemory2Failure": lgpConditionMemory2Failure,
       "lgpConditionUnitCodeErrorGroup": lgpConditionUnitCodeErrorGroup,
       "lgpConditionUnitCodeNotConfigured": lgpConditionUnitCodeNotConfigured,
       "lgpConditionUnitCode01OutOfRange": lgpConditionUnitCode01OutOfRange,
       "lgpConditionUnitCode02OutOfRange": lgpConditionUnitCode02OutOfRange,
       "lgpConditionUnitCode03OutOfRange": lgpConditionUnitCode03OutOfRange,
       "lgpConditionUnitCode04OutOfRange": lgpConditionUnitCode04OutOfRange,
       "lgpConditionUnitCode05OutOfRange": lgpConditionUnitCode05OutOfRange,
       "lgpConditionUnitCode06OutOfRange": lgpConditionUnitCode06OutOfRange,
       "lgpConditionUnitCode07OutOfRange": lgpConditionUnitCode07OutOfRange,
       "lgpConditionUnitCode08OutOfRange": lgpConditionUnitCode08OutOfRange,
       "lgpConditionUnitCode09OutOfRange": lgpConditionUnitCode09OutOfRange,
       "lgpConditionUnitCode10OutOfRange": lgpConditionUnitCode10OutOfRange,
       "lgpConditionUnitCode11OutOfRange": lgpConditionUnitCode11OutOfRange,
       "lgpConditionUnitCode12OutOfRange": lgpConditionUnitCode12OutOfRange,
       "lgpConditionUnitCode13OutOfRange": lgpConditionUnitCode13OutOfRange,
       "lgpConditionUnitCode14OutOfRange": lgpConditionUnitCode14OutOfRange,
       "lgpConditionUnitCode15OutOfRange": lgpConditionUnitCode15OutOfRange,
       "lgpConditionUnitCode16OutOfRange": lgpConditionUnitCode16OutOfRange,
       "lgpConditionUnitCode17OutOfRange": lgpConditionUnitCode17OutOfRange,
       "lgpConditionUnitCode18OutOfRange": lgpConditionUnitCode18OutOfRange,
       "lgpConditionHighExternalDewPoint": lgpConditionHighExternalDewPoint,
       "lgpConditionHcbDisconnected": lgpConditionHcbDisconnected,
       "lgpConditionBmsResetTimerExpired": lgpConditionBmsResetTimerExpired,
       "lgpConditionAgentFirmwareCorrupt": lgpConditionAgentFirmwareCorrupt,
       "lgpConditionSystemAccessGroup": lgpConditionSystemAccessGroup,
       "lgpConditionFrontAccessOpen": lgpConditionFrontAccessOpen,
       "lgpConditionRearAccessOpen": lgpConditionRearAccessOpen,
       "lgpConditionsDamperFailure": lgpConditionsDamperFailure,
       "lgpConditionEmergencyDamperFailure": lgpConditionEmergencyDamperFailure,
       "lgpConditionRemoteShutdown": lgpConditionRemoteShutdown,
       "lgpConditionFireAlarm": lgpConditionFireAlarm,
       "lgpConditionHeatersOverheated": lgpConditionHeatersOverheated,
       "lgpConditionCondenserFailureGroup": lgpConditionCondenserFailureGroup,
       "lgpConditionCondenser1Failure": lgpConditionCondenser1Failure,
       "lgpConditionCondenser2Failure": lgpConditionCondenser2Failure,
       "lgpConditionCondenserTVSSFailure": lgpConditionCondenserTVSSFailure,
       "lgpConditionHumidifierCyclinderWorn": lgpConditionHumidifierCyclinderWorn,
       "lgpConditionUnderCurrent": lgpConditionUnderCurrent,
       "lgpConditionHumidifierUnderCurrent": lgpConditionHumidifierUnderCurrent,
       "lgpConditionInputUnderCurrent": lgpConditionInputUnderCurrent,
       "lgpConditionHeatRejectorGroup": lgpConditionHeatRejectorGroup,
       "lgpConditionHeatRejectorFanFailure": lgpConditionHeatRejectorFanFailure,
       "lgpConditionHeatRejectorVoltageSuppressionFailure": lgpConditionHeatRejectorVoltageSuppressionFailure,
       "lgpConditionFreeCoolLockout": lgpConditionFreeCoolLockout,
       "lgpConditionWaterLeakSensorFailure": lgpConditionWaterLeakSensorFailure,
       "lgpConditionNoLoadDetectedWarning": lgpConditionNoLoadDetectedWarning,
       "lgpConditionFirmwareGroup": lgpConditionFirmwareGroup,
       "lgpConditionFirmwareUpdateRequired": lgpConditionFirmwareUpdateRequired,
       "lgpConditionTestGroup": lgpConditionTestGroup,
       "lgpConditionTest01": lgpConditionTest01,
       "lgpConditionReceptacleBranchGroup": lgpConditionReceptacleBranchGroup,
       "lgpConditionRcpBranchFailure": lgpConditionRcpBranchFailure,
       "lgpConditionRcpBranchBreakerOpen": lgpConditionRcpBranchBreakerOpen,
       "lgpConditionInputUnqualified": lgpConditionInputUnqualified,
       "lgpConditionBypassUnavailable": lgpConditionBypassUnavailable,
       "lgpConditionAutoTransferFailed": lgpConditionAutoTransferFailed,
       "lgpConditionSBSUnavailable": lgpConditionSBSUnavailable,
       "lgpConditionSBSOverload": lgpConditionSBSOverload,
       "lgpConditionExcessPulseParallel": lgpConditionExcessPulseParallel,
       "lgpConditionRemoteBypassSwitchOffExt": lgpConditionRemoteBypassSwitchOffExt,
       "lgpConditionManTransferInhibited": lgpConditionManTransferInhibited,
       "lgpConditionManReTransferInhibited": lgpConditionManReTransferInhibited,
       "lgpConditionBatteryChargeError": lgpConditionBatteryChargeError,
       "lgpConditionBatteryAutoTestInhibited": lgpConditionBatteryAutoTestInhibited,
       "lgpConditionBatteryChargeReducedExt": lgpConditionBatteryChargeReducedExt,
       "lgpConditionBatteryCapacityLow": lgpConditionBatteryCapacityLow,
       "lgpConditionBatteryTempImbalance": lgpConditionBatteryTempImbalance,
       "lgpConditionBatteryEqualize": lgpConditionBatteryEqualize,
       "lgpConditionBatteryChargeInhibitedExt": lgpConditionBatteryChargeInhibitedExt,
       "lgpConditionServiceExtBatteryMonitorGroup": lgpConditionServiceExtBatteryMonitorGroup,
       "lgpConditionServiceExtBatteryMonitor1": lgpConditionServiceExtBatteryMonitor1,
       "lgpConditionServiceExtBatteryMonitor2": lgpConditionServiceExtBatteryMonitor2,
       "lgpConditionBatteryGroundFault": lgpConditionBatteryGroundFault,
       "lgpConditionBatteryLowShutdown": lgpConditionBatteryLowShutdown,
       "lgpConditionEmergencyPowerOffLocal": lgpConditionEmergencyPowerOffLocal,
       "lgpConditionOutputLowPFLagging": lgpConditionOutputLowPFLagging,
       "lgpConditionOutputLowPFLeading": lgpConditionOutputLowPFLeading,
       "lgpConditionOutputToLoadFault": lgpConditionOutputToLoadFault,
       "lgpConditionInvRestartInhibitedExt": lgpConditionInvRestartInhibitedExt,
       "lgpConditionInverterShutdownOverload": lgpConditionInverterShutdownOverload,
       "lgpConditionInverterOffExt": lgpConditionInverterOffExt,
       "lgpConditionInputContactGroup": lgpConditionInputContactGroup,
       "lgpConditionInputContact01": lgpConditionInputContact01,
       "lgpConditionInputContact02": lgpConditionInputContact02,
       "lgpConditionInputContact03": lgpConditionInputContact03,
       "lgpConditionInputContact04": lgpConditionInputContact04,
       "lgpConditionInputContact05": lgpConditionInputContact05,
       "lgpConditionInputContact06": lgpConditionInputContact06,
       "lgpConditionInputContact07": lgpConditionInputContact07,
       "lgpConditionInputContact08": lgpConditionInputContact08,
       "lgpConditionInputContact09": lgpConditionInputContact09,
       "lgpConditionInputContact10": lgpConditionInputContact10,
       "lgpConditionInputContact11": lgpConditionInputContact11,
       "lgpConditionInputContact12": lgpConditionInputContact12,
       "lgpConditionInputContact13": lgpConditionInputContact13,
       "lgpConditionInputContact14": lgpConditionInputContact14,
       "lgpConditionInputContact15": lgpConditionInputContact15,
       "lgpConditionInputContact16": lgpConditionInputContact16,
       "lgpConditionRectifierOperInhibited": lgpConditionRectifierOperInhibited,
       "lgpConditionBypassBackFeedBrkrOpen": lgpConditionBypassBackFeedBrkrOpen,
       "lgpConditionAutoRestartInProgress": lgpConditionAutoRestartInProgress,
       "lgpConditionAutoRestartInhibitedExt": lgpConditionAutoRestartInhibitedExt,
       "lgpConditionAutoRestartFailed": lgpConditionAutoRestartFailed,
       "lgpConditionInputOnGenerator": lgpConditionInputOnGenerator,
       "lgpConditionInputFilterCycleLock": lgpConditionInputFilterCycleLock,
       "lgpConditionServiceCodeActive": lgpConditionServiceCodeActive,
       "lgpConditionLoadBusSyncActive": lgpConditionLoadBusSyncActive,
       "lgpConditionLoadBusSyncInhibited": lgpConditionLoadBusSyncInhibited,
       "lgpConditionControlsResetRequired": lgpConditionControlsResetRequired,
       "lgpConditionEquipTempSensorFailed": lgpConditionEquipTempSensorFailed,
       "lgpConditionInputCurrentImbalance": lgpConditionInputCurrentImbalance,
       "lgpConditionPumpGroup": lgpConditionPumpGroup,
       "lgpConditionPumpFlowLoss": lgpConditionPumpFlowLoss,
       "lgpConditionPump1FlowLoss": lgpConditionPump1FlowLoss,
       "lgpConditionPump2FlowLoss": lgpConditionPump2FlowLoss,
       "lgpConditionPumpShortCycle": lgpConditionPumpShortCycle,
       "lgpConditionPumpInverterShortCycle": lgpConditionPumpInverterShortCycle,
       "lgpConditionPump1InverterShortCycle": lgpConditionPump1InverterShortCycle,
       "lgpConditionPump2InverterShortCycle": lgpConditionPump2InverterShortCycle,
       "lgpConditionValveGroup": lgpConditionValveGroup,
       "lgpConditionChilledWaterValvePosition": lgpConditionChilledWaterValvePosition,
       "lgpConditionCondensationDetected": lgpConditionCondensationDetected,
       "lgpConditionMaintenanceGroup": lgpConditionMaintenanceGroup,
       "lgpConditionMaintenanceDue": lgpConditionMaintenanceDue,
       "lgpConditionMaintenanceComplete": lgpConditionMaintenanceComplete,
       "lgpConditionExternalEventSignalGroup": lgpConditionExternalEventSignalGroup,
       "lgpConditionExternalFireDetect": lgpConditionExternalFireDetect,
       "lgpConditionExternalFlowLoss": lgpConditionExternalFlowLoss,
       "lgpConditionExternalReheatLockout": lgpConditionExternalReheatLockout,
       "lgpConditionExternalOverTemp": lgpConditionExternalOverTemp,
       "lgpConditionExternalCompLockout": lgpConditionExternalCompLockout,
       "lgpConditionExternalHumidifierLockout": lgpConditionExternalHumidifierLockout,
       "lgpConditionComponentShutdownGroup": lgpConditionComponentShutdownGroup,
       "lgpConditionComponentShutdownPartial": lgpConditionComponentShutdownPartial,
       "lgpConditionComponentShutdownHighPower": lgpConditionComponentShutdownHighPower,
       "lgpConditionCondenserProblemGroup": lgpConditionCondenserProblemGroup,
       "lgpConditionCondenser1Problem": lgpConditionCondenser1Problem,
       "lgpConditionHumidityOutOfPropBand": lgpConditionHumidityOutOfPropBand,
       "lgpConditionEnvRemoteSensorGroup": lgpConditionEnvRemoteSensorGroup,
       "lgpConditionEnvRemoteSensor1Issue": lgpConditionEnvRemoteSensor1Issue,
       "lgpConditionEnvRemoteSensor2Issue": lgpConditionEnvRemoteSensor2Issue,
       "lgpConditionEnvRemoteSensor3Issue": lgpConditionEnvRemoteSensor3Issue,
       "lgpConditionEnvRemoteSensor4Issue": lgpConditionEnvRemoteSensor4Issue,
       "lgpConditionEnvRemoteSensor5Issue": lgpConditionEnvRemoteSensor5Issue,
       "lgpConditionEnvRemoteSensor6Issue": lgpConditionEnvRemoteSensor6Issue,
       "lgpConditionEnvRemoteSensor7Issue": lgpConditionEnvRemoteSensor7Issue,
       "lgpConditionEnvRemoteSensor8Issue": lgpConditionEnvRemoteSensor8Issue,
       "lgpConditionEnvRemoteSensor9Issue": lgpConditionEnvRemoteSensor9Issue,
       "lgpConditionEnvRemoteSensor10Issue": lgpConditionEnvRemoteSensor10Issue,
       "lgpConditionNeutralSnubberBoardCommFailure": lgpConditionNeutralSnubberBoardCommFailure,
       "lgpConditionRedundantChargerFailure": lgpConditionRedundantChargerFailure,
       "lgpConditionBoardInputContactorPowerFailure": lgpConditionBoardInputContactorPowerFailure,
       "lgpConditionBoard1InputContactorPowerFailure": lgpConditionBoard1InputContactorPowerFailure,
       "lgpConditionBoard2InputContactorPowerFailure": lgpConditionBoard2InputContactorPowerFailure,
       "lgpConditionTooManySensors": lgpConditionTooManySensors,
       "lgpConditionDoorSwitchOpen": lgpConditionDoorSwitchOpen,
       "lgpConditionContactClosureOpen": lgpConditionContactClosureOpen,
       "lgpConditionContactClosureClosed": lgpConditionContactClosureClosed,
       "lgpConditionsPresent": lgpConditionsPresent,
       "lgpConditionsTable": lgpConditionsTable,
       "lgpConditionEntry": lgpConditionEntry,
       "lgpConditionId": lgpConditionId,
       "lgpConditionDescr": lgpConditionDescr,
       "lgpConditionTime": lgpConditionTime,
       "lgpConditionTableRef": lgpConditionTableRef,
       "lgpConditionTableRowRef": lgpConditionTableRowRef,
       "lgpConditionType": lgpConditionType,
       "lgpConditionCurrentState": lgpConditionCurrentState,
       "lgpConditionSeverity": lgpConditionSeverity,
       "lgpConditionAcknowledged": lgpConditionAcknowledged,
       "lgpConditionAckReq": lgpConditionAckReq,
       "lgpConditionControl": lgpConditionControl,
       "lgpConditionControlEventReset": lgpConditionControlEventReset,
       "lgpConditionControlEventAck": lgpConditionControlEventAck,
       "lgpConditionControlTable": lgpConditionControlTable,
       "lgpConditionControlEntry": lgpConditionControlEntry,
       "lgpConditionControlIndex": lgpConditionControlIndex,
       "lgpConditionControlDescr": lgpConditionControlDescr,
       "lgpConditionControlEnableStatus": lgpConditionControlEnableStatus,
       "lgpConditionControlType": lgpConditionControlType,
       "lgpConditionControlEnableCapability": lgpConditionControlEnableCapability,
       "lgpConditionDescription": lgpConditionDescription,
       "lgpNetworkName": lgpNetworkName,
       "lgpFlexConditions": lgpFlexConditions,
       "lgpFlexConditionsWellKnown": lgpFlexConditionsWellKnown,
       "lgpCondId4122SystemInputPowerProblem": lgpCondId4122SystemInputPowerProblem,
       "lgpCondId4132BypassOverloadPhaseA": lgpCondId4132BypassOverloadPhaseA,
       "lgpCondId4133BypassOverloadPhaseB": lgpCondId4133BypassOverloadPhaseB,
       "lgpCondId4134BypassOverloadPhaseC": lgpCondId4134BypassOverloadPhaseC,
       "lgpCondId4135BypassNotAvailable": lgpCondId4135BypassNotAvailable,
       "lgpCondId4137BypassAutoRetransferPrimed": lgpCondId4137BypassAutoRetransferPrimed,
       "lgpCondId4138BypassAutoRetransferFailed": lgpCondId4138BypassAutoRetransferFailed,
       "lgpCondId4139BypassExcessAutoRetransfers": lgpCondId4139BypassExcessAutoRetransfers,
       "lgpCondId4140BypassRestartInhibitExternal": lgpCondId4140BypassRestartInhibitExternal,
       "lgpCondId4141BypassBreakerClosed": lgpCondId4141BypassBreakerClosed,
       "lgpCondId4142BypassStaticSwitchOverload": lgpCondId4142BypassStaticSwitchOverload,
       "lgpCondId4143BypassStaticSwitchUnavailable": lgpCondId4143BypassStaticSwitchUnavailable,
       "lgpCondId4144BypassExcessivePulseParallel": lgpCondId4144BypassExcessivePulseParallel,
       "lgpCondId4145BypassAutoTransferFailed": lgpCondId4145BypassAutoTransferFailed,
       "lgpCondId4146SystemInputPhsRotationError": lgpCondId4146SystemInputPhsRotationError,
       "lgpCondId4147SystemInputCurrentLimit": lgpCondId4147SystemInputCurrentLimit,
       "lgpCondId4162BatteryLow": lgpCondId4162BatteryLow,
       "lgpCondId4163OutputOffEndofDischarge": lgpCondId4163OutputOffEndofDischarge,
       "lgpCondId4164BatteryChargingError": lgpCondId4164BatteryChargingError,
       "lgpCondId4165BatteryChargingReducedExtrnl": lgpCondId4165BatteryChargingReducedExtrnl,
       "lgpCondId4166BatteryCapacityLow": lgpCondId4166BatteryCapacityLow,
       "lgpCondId4167OutputOff": lgpCondId4167OutputOff,
       "lgpCondId4168BatteryDischarging": lgpCondId4168BatteryDischarging,
       "lgpCondId4169BatteryTemperatureImbalance": lgpCondId4169BatteryTemperatureImbalance,
       "lgpCondId4170BatteryEqualize": lgpCondId4170BatteryEqualize,
       "lgpCondId4171BatteryManualTestInProgress": lgpCondId4171BatteryManualTestInProgress,
       "lgpCondId4172BatteryAutoTestInProgress": lgpCondId4172BatteryAutoTestInProgress,
       "lgpCondId4173MainBatteryDisconnectOpen": lgpCondId4173MainBatteryDisconnectOpen,
       "lgpCondId4174BatteryTemperatureSensorFault": lgpCondId4174BatteryTemperatureSensorFault,
       "lgpCondId4175BypassFrequencyError": lgpCondId4175BypassFrequencyError,
       "lgpCondId4176BatteryCircuitBreaker1Open": lgpCondId4176BatteryCircuitBreaker1Open,
       "lgpCondId4177BatteryBreaker1OpenFailure": lgpCondId4177BatteryBreaker1OpenFailure,
       "lgpCondId4178BatteryBreaker1CloseFailure": lgpCondId4178BatteryBreaker1CloseFailure,
       "lgpCondId4179BatteryCircuitBreaker2Open": lgpCondId4179BatteryCircuitBreaker2Open,
       "lgpCondId4180BatteryBreaker2OpenFailure": lgpCondId4180BatteryBreaker2OpenFailure,
       "lgpCondId4181BatteryBreaker2CloseFailure": lgpCondId4181BatteryBreaker2CloseFailure,
       "lgpCondId4182BatteryCircuitBreaker3Open": lgpCondId4182BatteryCircuitBreaker3Open,
       "lgpCondId4183BatteryBreaker3OpenFailure": lgpCondId4183BatteryBreaker3OpenFailure,
       "lgpCondId4184BatteryBreaker3CloseFailure": lgpCondId4184BatteryBreaker3CloseFailure,
       "lgpCondId4185BatteryCircuitBreaker4Open": lgpCondId4185BatteryCircuitBreaker4Open,
       "lgpCondId4186BatteryBreaker4OpenFailure": lgpCondId4186BatteryBreaker4OpenFailure,
       "lgpCondId4187BatteryBreaker4CloseFailure": lgpCondId4187BatteryBreaker4CloseFailure,
       "lgpCondId4188BatteryCircuitBreaker5Open": lgpCondId4188BatteryCircuitBreaker5Open,
       "lgpCondId4189BatteryBreaker5OpenFailure": lgpCondId4189BatteryBreaker5OpenFailure,
       "lgpCondId4190BatteryBreaker5CloseFailure": lgpCondId4190BatteryBreaker5CloseFailure,
       "lgpCondId4191BatteryCircuitBreaker6Open": lgpCondId4191BatteryCircuitBreaker6Open,
       "lgpCondId4192BatteryBreaker6OpenFailure": lgpCondId4192BatteryBreaker6OpenFailure,
       "lgpCondId4193BatteryBreaker6CloseFailure": lgpCondId4193BatteryBreaker6CloseFailure,
       "lgpCondId4194BatteryCircuitBreaker7Open": lgpCondId4194BatteryCircuitBreaker7Open,
       "lgpCondId4195BatteryBreaker7OpenFailure": lgpCondId4195BatteryBreaker7OpenFailure,
       "lgpCondId4196BatteryBreaker7CloseFailure": lgpCondId4196BatteryBreaker7CloseFailure,
       "lgpCondId4197BatteryCircuitBreaker8Open": lgpCondId4197BatteryCircuitBreaker8Open,
       "lgpCondId4198BatteryBreaker8OpenFailure": lgpCondId4198BatteryBreaker8OpenFailure,
       "lgpCondId4199BatteryBreaker8CloseFailure": lgpCondId4199BatteryBreaker8CloseFailure,
       "lgpCondId4200BatteryChargingInhibited": lgpCondId4200BatteryChargingInhibited,
       "lgpCondId4213SystemShutdownEPO": lgpCondId4213SystemShutdownEPO,
       "lgpCondId4214SystemShutdownREPO": lgpCondId4214SystemShutdownREPO,
       "lgpCondId4215SystemOutputOff": lgpCondId4215SystemOutputOff,
       "lgpCondId4216BypassBackfeedDetected": lgpCondId4216BypassBackfeedDetected,
       "lgpCondId4217BypassManualXfrInhibited": lgpCondId4217BypassManualXfrInhibited,
       "lgpCondId4218BypassManualRexfrInhibited": lgpCondId4218BypassManualRexfrInhibited,
       "lgpCondId4219BatteryOverTemperature": lgpCondId4219BatteryOverTemperature,
       "lgpCondId4220BatteryExternalMonitor1": lgpCondId4220BatteryExternalMonitor1,
       "lgpCondId4221BatteryExternalMonitor2": lgpCondId4221BatteryExternalMonitor2,
       "lgpCondId4222BatteryGroundFault": lgpCondId4222BatteryGroundFault,
       "lgpCondId4229EmergencyPowerOffLatched": lgpCondId4229EmergencyPowerOffLatched,
       "lgpCondId4230SystemOutputLowPowerFactor": lgpCondId4230SystemOutputLowPowerFactor,
       "lgpCondId4231OutputCurrentExceedsThreshold": lgpCondId4231OutputCurrentExceedsThreshold,
       "lgpCondId4233InverterFailure": lgpCondId4233InverterFailure,
       "lgpCondId4234InverterOverloadPhaseA": lgpCondId4234InverterOverloadPhaseA,
       "lgpCondId4235InverterOverloadPhaseB": lgpCondId4235InverterOverloadPhaseB,
       "lgpCondId4236InverterOverloadPhaseC": lgpCondId4236InverterOverloadPhaseC,
       "lgpCondId4237InverterInhibitExternal": lgpCondId4237InverterInhibitExternal,
       "lgpCondId4238InverterOutBreakerOpenFail": lgpCondId4238InverterOutBreakerOpenFail,
       "lgpCondId4239InverterOutBreakerCloseFail": lgpCondId4239InverterOutBreakerCloseFail,
       "lgpCondId4270InputContact01": lgpCondId4270InputContact01,
       "lgpCondId4271InputContact02": lgpCondId4271InputContact02,
       "lgpCondId4272InputContact03": lgpCondId4272InputContact03,
       "lgpCondId4273InputContact04": lgpCondId4273InputContact04,
       "lgpCondId4274InputContact05": lgpCondId4274InputContact05,
       "lgpCondId4275InputContact06": lgpCondId4275InputContact06,
       "lgpCondId4276InputContact07": lgpCondId4276InputContact07,
       "lgpCondId4277InputContact08": lgpCondId4277InputContact08,
       "lgpCondId4278InputContact09": lgpCondId4278InputContact09,
       "lgpCondId4279InputContact10": lgpCondId4279InputContact10,
       "lgpCondId4280InputContact11": lgpCondId4280InputContact11,
       "lgpCondId4281InputContact12": lgpCondId4281InputContact12,
       "lgpCondId4282InputContact13": lgpCondId4282InputContact13,
       "lgpCondId4283InputContact14": lgpCondId4283InputContact14,
       "lgpCondId4284InputContact15": lgpCondId4284InputContact15,
       "lgpCondId4285InputContact16": lgpCondId4285InputContact16,
       "lgpCondId4286OutputAmpOverUserLimitPhsA": lgpCondId4286OutputAmpOverUserLimitPhsA,
       "lgpCondId4287OutputAmpOverUserLimitPhsB": lgpCondId4287OutputAmpOverUserLimitPhsB,
       "lgpCondId4288OutputAmpOverUserLimitPhsC": lgpCondId4288OutputAmpOverUserLimitPhsC,
       "lgpCondId4289InverterTransferInhibitExt": lgpCondId4289InverterTransferInhibitExt,
       "lgpCondId4290InverterShutdownOverload": lgpCondId4290InverterShutdownOverload,
       "lgpCondId4294InletAirOverTemperature": lgpCondId4294InletAirOverTemperature,
       "lgpCondId4295RectifierFailure": lgpCondId4295RectifierFailure,
       "lgpCondId4296RectifierOperationInhibitExt": lgpCondId4296RectifierOperationInhibitExt,
       "lgpCondId4297UPSOutputonInverter": lgpCondId4297UPSOutputonInverter,
       "lgpCondId4298UPSOutputonBypass": lgpCondId4298UPSOutputonBypass,
       "lgpCondId4299OutputLoadonMaintBypass": lgpCondId4299OutputLoadonMaintBypass,
       "lgpCondId4300InternalCommunicationsFailure": lgpCondId4300InternalCommunicationsFailure,
       "lgpCondId4308DCBusGroundFaultPositive": lgpCondId4308DCBusGroundFaultPositive,
       "lgpCondId4309DCBusGroundFaultNegative": lgpCondId4309DCBusGroundFaultNegative,
       "lgpCondId4310EquipmentOverTemperature": lgpCondId4310EquipmentOverTemperature,
       "lgpCondId4311SystemFanFailure": lgpCondId4311SystemFanFailure,
       "lgpCondId4313PasswordChanged": lgpCondId4313PasswordChanged,
       "lgpCondId4314PowerSupplyFailure": lgpCondId4314PowerSupplyFailure,
       "lgpCondId4315OnGenerator": lgpCondId4315OnGenerator,
       "lgpCondId4316AutoRestartInProgress": lgpCondId4316AutoRestartInProgress,
       "lgpCondId4317AutoRestartInhibitedExt": lgpCondId4317AutoRestartInhibitedExt,
       "lgpCondId4320InitiatedTransfertoBypass": lgpCondId4320InitiatedTransfertoBypass,
       "lgpCondId4321InitiatedTransfertoInverter": lgpCondId4321InitiatedTransfertoInverter,
       "lgpCondId4322BatteryTestPassed": lgpCondId4322BatteryTestPassed,
       "lgpCondId4323BatteryTestFailed": lgpCondId4323BatteryTestFailed,
       "lgpCondId4324BatteryTestManuallyStopped": lgpCondId4324BatteryTestManuallyStopped,
       "lgpCondId4325BackfeedBreakerOpen": lgpCondId4325BackfeedBreakerOpen,
       "lgpCondId4341VelocityAuthenticationFailure": lgpCondId4341VelocityAuthenticationFailure,
       "lgpCondId4360ReceptacleOverCurrent": lgpCondId4360ReceptacleOverCurrent,
       "lgpCondId4361ReceptacleUnderCurrent": lgpCondId4361ReceptacleUnderCurrent,
       "lgpCondId4382SystemInputCurrentImbalance": lgpCondId4382SystemInputCurrentImbalance,
       "lgpCondId4383BypassStaticSwitchOffExtrnl": lgpCondId4383BypassStaticSwitchOffExtrnl,
       "lgpCondId4384BatteryEoDDisconnect": lgpCondId4384BatteryEoDDisconnect,
       "lgpCondId4389SystemOutputFault": lgpCondId4389SystemOutputFault,
       "lgpCondId4390InverterOffExternal": lgpCondId4390InverterOffExternal,
       "lgpCondId4391InverterStaticSwitchSCRShort": lgpCondId4391InverterStaticSwitchSCRShort,
       "lgpCondId4392TemperatureSensorError": lgpCondId4392TemperatureSensorError,
       "lgpCondId4406BranchOverCurrent": lgpCondId4406BranchOverCurrent,
       "lgpCondId4407BranchUnderCurrent": lgpCondId4407BranchUnderCurrent,
       "lgpCondId4416BranchOverCurrent": lgpCondId4416BranchOverCurrent,
       "lgpCondId4417BranchUnderCurrent": lgpCondId4417BranchUnderCurrent,
       "lgpCondId4421BranchFailure": lgpCondId4421BranchFailure,
       "lgpCondId4436PDUOverCurrent": lgpCondId4436PDUOverCurrent,
       "lgpCondId4437PDUUnderCurrent": lgpCondId4437PDUUnderCurrent,
       "lgpCondId4438SystemInternalTemperatureRise": lgpCondId4438SystemInternalTemperatureRise,
       "lgpCondId4439AutomaticRestartFailed": lgpCondId4439AutomaticRestartFailed,
       "lgpCondId4440FuseFailure": lgpCondId4440FuseFailure,
       "lgpCondId4441SystemControllerError": lgpCondId4441SystemControllerError,
       "lgpCondId4442SystemBreakersOpenFailure": lgpCondId4442SystemBreakersOpenFailure,
       "lgpCondId4448PDUOverCurrent": lgpCondId4448PDUOverCurrent,
       "lgpCondId4449PDUUnderCurrent": lgpCondId4449PDUUnderCurrent,
       "lgpCondId4468PDUOverCurrentL1": lgpCondId4468PDUOverCurrentL1,
       "lgpCondId4469PDUOverCurrentL2": lgpCondId4469PDUOverCurrentL2,
       "lgpCondId4470PDUOverCurrentL3": lgpCondId4470PDUOverCurrentL3,
       "lgpCondId4471PDUUnderCurrentL1": lgpCondId4471PDUUnderCurrentL1,
       "lgpCondId4472PDUUnderCurrentL2": lgpCondId4472PDUUnderCurrentL2,
       "lgpCondId4473PDUUnderCurrentL3": lgpCondId4473PDUUnderCurrentL3,
       "lgpCondId4492ReceptaclePowerStateOn": lgpCondId4492ReceptaclePowerStateOn,
       "lgpCondId4493ReceptaclePowerStateOff": lgpCondId4493ReceptaclePowerStateOff,
       "lgpCondId4494BranchBreakerOpen": lgpCondId4494BranchBreakerOpen,
       "lgpCondId4495DeviceConfigurationChange": lgpCondId4495DeviceConfigurationChange,
       "lgpCondId4496BasicDisplayModuleRemoved": lgpCondId4496BasicDisplayModuleRemoved,
       "lgpCondId4497BasicDisplayModuleDiscovered": lgpCondId4497BasicDisplayModuleDiscovered,
       "lgpCondId4500PDUOverCurrent": lgpCondId4500PDUOverCurrent,
       "lgpCondId4501PDUUnderCurrent": lgpCondId4501PDUUnderCurrent,
       "lgpCondId4502PDUFailure": lgpCondId4502PDUFailure,
       "lgpCondId4503PDUCommunicationFail": lgpCondId4503PDUCommunicationFail,
       "lgpCondId4504BranchRemoved": lgpCondId4504BranchRemoved,
       "lgpCondId4505BranchDiscovered": lgpCondId4505BranchDiscovered,
       "lgpCondId4506BranchOverCurrent": lgpCondId4506BranchOverCurrent,
       "lgpCondId4507BranchCurrent": lgpCondId4507BranchCurrent,
       "lgpCondId4508ReceptacleLoadRemoved": lgpCondId4508ReceptacleLoadRemoved,
       "lgpCondId4509ReceptacleLoadAdded": lgpCondId4509ReceptacleLoadAdded,
       "lgpCondId4523ModuleRemoved": lgpCondId4523ModuleRemoved,
       "lgpCondId4524ModuleAdded": lgpCondId4524ModuleAdded,
       "lgpCondId4550FirmwareUpdateRequired": lgpCondId4550FirmwareUpdateRequired,
       "lgpCondId4551GenericTestEvent": lgpCondId4551GenericTestEvent,
       "lgpCondId4580OverTemperature": lgpCondId4580OverTemperature,
       "lgpCondId4581UnderTemperature": lgpCondId4581UnderTemperature,
       "lgpCondId4588OverRelativeHumidity": lgpCondId4588OverRelativeHumidity,
       "lgpCondId4589UnderRelativeHumidity": lgpCondId4589UnderRelativeHumidity,
       "lgpCondId4601ExternalAirSensorAOverTemperature": lgpCondId4601ExternalAirSensorAOverTemperature,
       "lgpCondId4604ExternalAirSensorBOverTemperature": lgpCondId4604ExternalAirSensorBOverTemperature,
       "lgpCondId4608ExtAirSensorAUnderTemperature": lgpCondId4608ExtAirSensorAUnderTemperature,
       "lgpCondId4611ExtAirSensorBUnderTemperature": lgpCondId4611ExtAirSensorBUnderTemperature,
       "lgpCondId4615ExtDewPointOverTemperature": lgpCondId4615ExtDewPointOverTemperature,
       "lgpCondId4618ExternalAirSensorAIssue": lgpCondId4618ExternalAirSensorAIssue,
       "lgpCondId4621ExternalAirSensorBIssue": lgpCondId4621ExternalAirSensorBIssue,
       "lgpCondId4626SupplyChilledWaterOverTemp": lgpCondId4626SupplyChilledWaterOverTemp,
       "lgpCondId4629SupplyChilledWaterTempSensorIssue": lgpCondId4629SupplyChilledWaterTempSensorIssue,
       "lgpCondId4634SupplyRefrigerantOverTemp": lgpCondId4634SupplyRefrigerantOverTemp,
       "lgpCondId4637SupplyRefrigerantUnderTemp": lgpCondId4637SupplyRefrigerantUnderTemp,
       "lgpCondId4640SupplyRefrigerantTempSensorIssue": lgpCondId4640SupplyRefrigerantTempSensorIssue,
       "lgpCondId4645SupplyFluidOverTemp": lgpCondId4645SupplyFluidOverTemp,
       "lgpCondId4648SupplyFluidUnderTemp": lgpCondId4648SupplyFluidUnderTemp,
       "lgpCondId4651SupplyFluidTempSensorIssue": lgpCondId4651SupplyFluidTempSensorIssue,
       "lgpCondId4656Pump1LossofFlow": lgpCondId4656Pump1LossofFlow,
       "lgpCondId4659Pump2LossofFlow": lgpCondId4659Pump2LossofFlow,
       "lgpCondId4662PumpShortCycle": lgpCondId4662PumpShortCycle,
       "lgpCondId4669Compressor1AHighHeadPressure": lgpCondId4669Compressor1AHighHeadPressure,
       "lgpCondId4672Compressor1BHighHeadPressure": lgpCondId4672Compressor1BHighHeadPressure,
       "lgpCondId4675Compressor2AHighHeadPressure": lgpCondId4675Compressor2AHighHeadPressure,
       "lgpCondId4678Compressor2BHighHeadPressure": lgpCondId4678Compressor2BHighHeadPressure,
       "lgpCondId4681Compressor1AShortCycle": lgpCondId4681Compressor1AShortCycle,
       "lgpCondId4684Compressor1BShortCycle": lgpCondId4684Compressor1BShortCycle,
       "lgpCondId4687Compressor2AShortCycle": lgpCondId4687Compressor2AShortCycle,
       "lgpCondId4690Compressor2BShortCycle": lgpCondId4690Compressor2BShortCycle,
       "lgpCondId4693Tandem1LowSuctionPressure": lgpCondId4693Tandem1LowSuctionPressure,
       "lgpCondId4696Tandem2LowSuctionPressure": lgpCondId4696Tandem2LowSuctionPressure,
       "lgpCondId4703ChilledWaterControlValvePosition": lgpCondId4703ChilledWaterControlValvePosition,
       "lgpCondId4711SystemCondensationDetected": lgpCondId4711SystemCondensationDetected,
       "lgpCondId4714ShutdownLossOfPower": lgpCondId4714ShutdownLossOfPower,
       "lgpCondId4720SmokeDetected": lgpCondId4720SmokeDetected,
       "lgpCondId4723WaterUnderFloor": lgpCondId4723WaterUnderFloor,
       "lgpCondId4726ServiceRequired": lgpCondId4726ServiceRequired,
       "lgpCondId4729FanIssue": lgpCondId4729FanIssue,
       "lgpCondId4732ReceptacleLoadDropped": lgpCondId4732ReceptacleLoadDropped,
       "lgpCondId4740BatteryAutomaticTestInhibited": lgpCondId4740BatteryAutomaticTestInhibited,
       "lgpCondId4741BatterySelfTest": lgpCondId4741BatterySelfTest,
       "lgpCondId4742BatteryLowShutdown": lgpCondId4742BatteryLowShutdown,
       "lgpCondId4747EquipmentTemperatureSensorFail": lgpCondId4747EquipmentTemperatureSensorFail,
       "lgpCondId4749SystemFanFailureRedundant": lgpCondId4749SystemFanFailureRedundant,
       "lgpCondId4750MultipleFanFailure": lgpCondId4750MultipleFanFailure,
       "lgpCondId4753MainControllerFault": lgpCondId4753MainControllerFault,
       "lgpCondId4754SystemBreakersCloseFailure": lgpCondId4754SystemBreakersCloseFailure,
       "lgpCondId4755InputFilterCycleLock": lgpCondId4755InputFilterCycleLock,
       "lgpCondId4756ServiceCodeActive": lgpCondId4756ServiceCodeActive,
       "lgpCondId4757LBSActive": lgpCondId4757LBSActive,
       "lgpCondId4758LBSInhibited": lgpCondId4758LBSInhibited,
       "lgpCondId4759LeadingPowerFactor": lgpCondId4759LeadingPowerFactor,
       "lgpCondId4760ControlsResetRequired": lgpCondId4760ControlsResetRequired,
       "lgpCondId4823ParallelCommWarning": lgpCondId4823ParallelCommWarning,
       "lgpCondId4824SystemCommFail": lgpCondId4824SystemCommFail,
       "lgpCondId4825LossofRedundancy": lgpCondId4825LossofRedundancy,
       "lgpCondId4826BPSSStartupInhibit": lgpCondId4826BPSSStartupInhibit,
       "lgpCondId4827MMSTransferInhibit": lgpCondId4827MMSTransferInhibit,
       "lgpCondId4828MMSRetransferInhibit": lgpCondId4828MMSRetransferInhibit,
       "lgpCondId4830MMSLossofSyncPulse": lgpCondId4830MMSLossofSyncPulse,
       "lgpCondId4831MMSOverload": lgpCondId4831MMSOverload,
       "lgpCondId4834MMSOnBattery": lgpCondId4834MMSOnBattery,
       "lgpCondId4835MMSLowBatteryWarning": lgpCondId4835MMSLowBatteryWarning,
       "lgpCondId4906LowAmbientTemperature": lgpCondId4906LowAmbientTemperature,
       "lgpCondId4907HighAmbientTemperature": lgpCondId4907HighAmbientTemperature,
       "lgpCondId4908LowOverallVoltage": lgpCondId4908LowOverallVoltage,
       "lgpCondId4909HighOverallVoltage": lgpCondId4909HighOverallVoltage,
       "lgpCondId4910HighBatteryStringCurrent": lgpCondId4910HighBatteryStringCurrent,
       "lgpCondId4911LowBatteryStringFloatCurrent": lgpCondId4911LowBatteryStringFloatCurrent,
       "lgpCondId4912HighBatteryStringFloatCurrent": lgpCondId4912HighBatteryStringFloatCurrent,
       "lgpCondId4913HighBatteryStringRippleCurrent": lgpCondId4913HighBatteryStringRippleCurrent,
       "lgpCondId4914BatteryStringDischargeDetected": lgpCondId4914BatteryStringDischargeDetected,
       "lgpCondId4915MaximumDischargeTimeExceeded": lgpCondId4915MaximumDischargeTimeExceeded,
       "lgpCondId4916DischargeLowOverallVoltage": lgpCondId4916DischargeLowOverallVoltage,
       "lgpCondId4917DischargeLowCellVoltage": lgpCondId4917DischargeLowCellVoltage,
       "lgpCondId4918DischargeHighBatteryStringCurrent": lgpCondId4918DischargeHighBatteryStringCurrent,
       "lgpCondId4919ExcessiveCelltoCellTemperatureDeviation": lgpCondId4919ExcessiveCelltoCellTemperatureDeviation,
       "lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation": lgpCondId4920ExcessiveCelltoAmbientTemperatureDeviation,
       "lgpCondId4964LowCellVoltage": lgpCondId4964LowCellVoltage,
       "lgpCondId4965HighCellVoltage": lgpCondId4965HighCellVoltage,
       "lgpCondId4966LowCellTemperature": lgpCondId4966LowCellTemperature,
       "lgpCondId4967HighCellTemperature": lgpCondId4967HighCellTemperature,
       "lgpCondId4968LowInternalResistance": lgpCondId4968LowInternalResistance,
       "lgpCondId4969HighInternalResistance": lgpCondId4969HighInternalResistance,
       "lgpCondId4970HighIntercellResistance": lgpCondId4970HighIntercellResistance,
       "lgpCondId4978IntertierResistanceHigh": lgpCondId4978IntertierResistanceHigh,
       "lgpCondId4980SupplyChilledWaterLossofFlow": lgpCondId4980SupplyChilledWaterLossofFlow,
       "lgpCondId4983SupplyRefrigOverTempBand1": lgpCondId4983SupplyRefrigOverTempBand1,
       "lgpCondId4986SupplyRefrigUnderTempBand1": lgpCondId4986SupplyRefrigUnderTempBand1,
       "lgpCondId4990SupplyRefrigOverTempBand2": lgpCondId4990SupplyRefrigOverTempBand2,
       "lgpCondId4993SupplyRefrigUnderTempBand2": lgpCondId4993SupplyRefrigUnderTempBand2,
       "lgpCondId4996Inverter1ShortCycle": lgpCondId4996Inverter1ShortCycle,
       "lgpCondId4999Inverter2ShortCycle": lgpCondId4999Inverter2ShortCycle,
       "lgpCondId5015SupplyAirOverTemperature": lgpCondId5015SupplyAirOverTemperature,
       "lgpCondId5019SupplyAirUnderTemperature": lgpCondId5019SupplyAirUnderTemperature,
       "lgpCondId5023ReturnAirOverTemperature": lgpCondId5023ReturnAirOverTemperature,
       "lgpCondId5026SupplyAirSensorIssue": lgpCondId5026SupplyAirSensorIssue,
       "lgpCondId5034HighReturnHumidity": lgpCondId5034HighReturnHumidity,
       "lgpCondId5036LowReturnHumidity": lgpCondId5036LowReturnHumidity,
       "lgpCondId5037HumidifierHoursExceeded": lgpCondId5037HumidifierHoursExceeded,
       "lgpCondId5038DehumidifierHoursExceeded": lgpCondId5038DehumidifierHoursExceeded,
       "lgpCondId5039HumidifierUnderCurrent": lgpCondId5039HumidifierUnderCurrent,
       "lgpCondId5040HumidifierOverCurrent": lgpCondId5040HumidifierOverCurrent,
       "lgpCondId5041HumidifierLowWater": lgpCondId5041HumidifierLowWater,
       "lgpCondId5042HumidifierCylinderWorn": lgpCondId5042HumidifierCylinderWorn,
       "lgpCondId5043HumidifierIssue": lgpCondId5043HumidifierIssue,
       "lgpCondId5044ExtHumidifierLockout": lgpCondId5044ExtHumidifierLockout,
       "lgpCondId5045HumidifierControlBoardNotDetected": lgpCondId5045HumidifierControlBoardNotDetected,
       "lgpCondId5046ReturnHumidityOutOfProportionalBand": lgpCondId5046ReturnHumidityOutOfProportionalBand,
       "lgpCondId5053LossofAirFlow": lgpCondId5053LossofAirFlow,
       "lgpCondId5054FanHoursExceeded": lgpCondId5054FanHoursExceeded,
       "lgpCondId5055TopFanIssue": lgpCondId5055TopFanIssue,
       "lgpCondId5056BottomFanIssue": lgpCondId5056BottomFanIssue,
       "lgpCondId5060RemoteSensorIssue": lgpCondId5060RemoteSensorIssue,
       "lgpCondId5062Compressor1LowSuctionPressure": lgpCondId5062Compressor1LowSuctionPressure,
       "lgpCondId5063Compressor1HoursExceeded": lgpCondId5063Compressor1HoursExceeded,
       "lgpCondId5064DigScrollComp1TempSensorIssue": lgpCondId5064DigScrollComp1TempSensorIssue,
       "lgpCondId5065DigScrollComp1OverTemp": lgpCondId5065DigScrollComp1OverTemp,
       "lgpCondId5066Compressor1LowPressureTransducerIssue": lgpCondId5066Compressor1LowPressureTransducerIssue,
       "lgpCondId5067ExtCompressorLockout": lgpCondId5067ExtCompressorLockout,
       "lgpCondId5068ReheaterOverTemperature": lgpCondId5068ReheaterOverTemperature,
       "lgpCondId5069ElectricReheater1HoursExceeded": lgpCondId5069ElectricReheater1HoursExceeded,
       "lgpCondId5070ExtReheatLockout": lgpCondId5070ExtReheatLockout,
       "lgpCondId5071Condenser1Issue": lgpCondId5071Condenser1Issue,
       "lgpCondId5072CondenserVFDIssue": lgpCondId5072CondenserVFDIssue,
       "lgpCondId5073CondenserTVSSIssue": lgpCondId5073CondenserTVSSIssue,
       "lgpCondId5104ExtOverTemperature": lgpCondId5104ExtOverTemperature,
       "lgpCondId5105ExtLossofFlow": lgpCondId5105ExtLossofFlow,
       "lgpCondId5106ExtCondenserPumpHighWater": lgpCondId5106ExtCondenserPumpHighWater,
       "lgpCondId5107ExtStandbyGlycolPumpOn": lgpCondId5107ExtStandbyGlycolPumpOn,
       "lgpCondId5108ExternalFireDetected": lgpCondId5108ExternalFireDetected,
       "lgpCondId5109UnitOn": lgpCondId5109UnitOn,
       "lgpCondId5110UnitOff": lgpCondId5110UnitOff,
       "lgpCondId5111UnitStandby": lgpCondId5111UnitStandby,
       "lgpCondId5112UnitPartialShutdown": lgpCondId5112UnitPartialShutdown,
       "lgpCondId5113UnitShutdown": lgpCondId5113UnitShutdown,
       "lgpCondId5114WaterLeakageDetectorSensorIssue": lgpCondId5114WaterLeakageDetectorSensorIssue,
       "lgpCondId5115BMSCommunicationsTimeout": lgpCondId5115BMSCommunicationsTimeout,
       "lgpCondId5116MaintenanceDue": lgpCondId5116MaintenanceDue,
       "lgpCondId5117MaintenanceCompleted": lgpCondId5117MaintenanceCompleted,
       "lgpCondId5118CloggedAirFilter": lgpCondId5118CloggedAirFilter,
       "lgpCondId5119RAMBatteryIssue": lgpCondId5119RAMBatteryIssue,
       "lgpCondId5120MasterUnitCommunicationLost": lgpCondId5120MasterUnitCommunicationLost,
       "lgpCondId5121HighPowerShutdown": lgpCondId5121HighPowerShutdown,
       "lgpCondId5126DigScrollComp2OverTemp": lgpCondId5126DigScrollComp2OverTemp,
       "lgpCondId5144OutputOfUf": lgpCondId5144OutputOfUf,
       "lgpCondId5145MMSModuleAlarmActive": lgpCondId5145MMSModuleAlarmActive,
       "lgpCondId5146CompressorPumpDownIssue": lgpCondId5146CompressorPumpDownIssue,
       "lgpCondId5147ReturnAirSensorIssue": lgpCondId5147ReturnAirSensorIssue,
       "lgpCondId5148CompressorHighPressureTransducerIssue": lgpCondId5148CompressorHighPressureTransducerIssue,
       "lgpCondId5149BatteryNotQualified": lgpCondId5149BatteryNotQualified,
       "lgpCondId5150BatteryTerminalsReversed": lgpCondId5150BatteryTerminalsReversed,
       "lgpCondId5151BatteryConverterFailure": lgpCondId5151BatteryConverterFailure,
       "lgpCondId5152InverterSCROpen": lgpCondId5152InverterSCROpen,
       "lgpCondId5153LoadSharingFault": lgpCondId5153LoadSharingFault,
       "lgpCondId5154DCBusAbnormal": lgpCondId5154DCBusAbnormal,
       "lgpCondId5155MainsInputNeutralLost": lgpCondId5155MainsInputNeutralLost,
       "lgpCondId5156LoadImpactTransfer": lgpCondId5156LoadImpactTransfer,
       "lgpCondId5157UserOperationInvalid": lgpCondId5157UserOperationInvalid,
       "lgpCondId5158PowerSubModuleFault": lgpCondId5158PowerSubModuleFault,
       "lgpCondId5178OutputOvervoltage": lgpCondId5178OutputOvervoltage,
       "lgpCondId5179OutputUndervoltage": lgpCondId5179OutputUndervoltage,
       "lgpCondId5180OutputOvercurrent": lgpCondId5180OutputOvercurrent,
       "lgpCondId5181NeutralOvercurrent": lgpCondId5181NeutralOvercurrent,
       "lgpCondId5182GroundOvercurrent": lgpCondId5182GroundOvercurrent,
       "lgpCondId5183OutputVoltageTHD": lgpCondId5183OutputVoltageTHD,
       "lgpCondId5184OutputFrequencyError": lgpCondId5184OutputFrequencyError,
       "lgpCondId5185TransformerOvertemperature": lgpCondId5185TransformerOvertemperature,
       "lgpCondId5212PanelSummaryStatus": lgpCondId5212PanelSummaryStatus,
       "lgpCondId5213PanelOvervoltage": lgpCondId5213PanelOvervoltage,
       "lgpCondId5214PanelUndervoltage": lgpCondId5214PanelUndervoltage,
       "lgpCondId5215PanelOvercurrent": lgpCondId5215PanelOvercurrent,
       "lgpCondId5216PanelNeutralOvercurrent": lgpCondId5216PanelNeutralOvercurrent,
       "lgpCondId5217PanelGroundOvercurrent": lgpCondId5217PanelGroundOvercurrent,
       "lgpCondId5226BranchOvercurrent": lgpCondId5226BranchOvercurrent,
       "lgpCondId5227BranchUndercurrent": lgpCondId5227BranchUndercurrent,
       "lgpCondId5245SubfeedPhaseOvercurrent": lgpCondId5245SubfeedPhaseOvercurrent,
       "lgpCondId5246SubfeedNeutralOvercurrent": lgpCondId5246SubfeedNeutralOvercurrent,
       "lgpCondId5247SubfeedGroundOvercurrent": lgpCondId5247SubfeedGroundOvercurrent,
       "lgpCondId5249EventState": lgpCondId5249EventState,
       "lgpCondId5263CompressorNotStopping": lgpCondId5263CompressorNotStopping,
       "lgpCondId5269CompressorHoursExceeded": lgpCondId5269CompressorHoursExceeded,
       "lgpCondId5270CompressorHighHeadPressure": lgpCondId5270CompressorHighHeadPressure,
       "lgpCondId5271CompressorLowSuctionPressure": lgpCondId5271CompressorLowSuctionPressure,
       "lgpCondId5272CompressorThermalOverload": lgpCondId5272CompressorThermalOverload,
       "lgpCondId5273CompressorLowOilPressure": lgpCondId5273CompressorLowOilPressure,
       "lgpCondId5274CompressorHeadPressureOverThreshold": lgpCondId5274CompressorHeadPressureOverThreshold,
       "lgpCondId5275CompressorLossofDifferentialPressure": lgpCondId5275CompressorLossofDifferentialPressure,
       "lgpCondId5277CondenserFanIssue": lgpCondId5277CondenserFanIssue,
       "lgpCondId5278LowCondenserRefrigerantPressure": lgpCondId5278LowCondenserRefrigerantPressure,
       "lgpCondId5280LowFluidPressure": lgpCondId5280LowFluidPressure,
       "lgpCondId5293ReturnFluidOverTemp": lgpCondId5293ReturnFluidOverTemp,
       "lgpCondId5294ReturnFluidUnderTemp": lgpCondId5294ReturnFluidUnderTemp,
       "lgpCondId5295ReturnFluidTempSensorIssue": lgpCondId5295ReturnFluidTempSensorIssue,
       "lgpCondId5296TeamworkReturnFluidTempSensorIssue": lgpCondId5296TeamworkReturnFluidTempSensorIssue,
       "lgpCondId5297AllPumpsLossofFlow": lgpCondId5297AllPumpsLossofFlow,
       "lgpCondId5300PumpHoursExceeded": lgpCondId5300PumpHoursExceeded,
       "lgpCondId5306FreeCoolingValveHoursExceeded": lgpCondId5306FreeCoolingValveHoursExceeded,
       "lgpCondId5308EvaporatorInletTempSensorIssue": lgpCondId5308EvaporatorInletTempSensorIssue,
       "lgpCondId5309TeamworkEvaporatorInletTempSensorIssue": lgpCondId5309TeamworkEvaporatorInletTempSensorIssue,
       "lgpCondId5310EvaporatorFluidFreezeAutoReset": lgpCondId5310EvaporatorFluidFreezeAutoReset,
       "lgpCondId5311EvaporatorFluidFreezeManualResetRequired": lgpCondId5311EvaporatorFluidFreezeManualResetRequired,
       "lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss": lgpCondId5315SubgroupEventOccurredDuringCommunicationLoss,
       "lgpCondId5335ReturnAirUnderTemperature": lgpCondId5335ReturnAirUnderTemperature,
       "lgpCondId5349ExtAirSensorAHighHumidity": lgpCondId5349ExtAirSensorAHighHumidity,
       "lgpCondId5351ExtAirSensorALowHumidity": lgpCondId5351ExtAirSensorALowHumidity,
       "lgpCondId5352CompressorShortCycle": lgpCondId5352CompressorShortCycle,
       "lgpCondId5354DigScrollCompDischargeTempSensorIssue": lgpCondId5354DigScrollCompDischargeTempSensorIssue,
       "lgpCondId5355DigScrollCompOverTemp": lgpCondId5355DigScrollCompOverTemp,
       "lgpCondId5361ExtFreeCoolingLockout": lgpCondId5361ExtFreeCoolingLockout,
       "lgpCondId5362FreeCoolingTempSensorIssue": lgpCondId5362FreeCoolingTempSensorIssue,
       "lgpCondId5365HotWaterHotGasValveHoursExceeded": lgpCondId5365HotWaterHotGasValveHoursExceeded,
       "lgpCondId5368ElectricReheaterHoursExceeded": lgpCondId5368ElectricReheaterHoursExceeded,
       "lgpCondId5376MainFanOverload": lgpCondId5376MainFanOverload,
       "lgpCondId5377Condenser": lgpCondId5377Condenser,
       "lgpCondId5415ExtLossofAirBlower": lgpCondId5415ExtLossofAirBlower,
       "lgpCondId5416ExtStandbyUnitOn": lgpCondId5416ExtStandbyUnitOn,
       "lgpCondId5417DigitalOutputBoardNotDetected": lgpCondId5417DigitalOutputBoardNotDetected,
       "lgpCondId5418UnitCodeMissing": lgpCondId5418UnitCodeMissing,
       "lgpCondId5419UnitCommunicationLost": lgpCondId5419UnitCommunicationLost,
       "lgpCondId5422OvertemperaturePowerOff": lgpCondId5422OvertemperaturePowerOff,
       "lgpCondId5423TooManySensors": lgpCondId5423TooManySensors,
       "lgpCondId5432TransformerOvertemperaturePowerOff": lgpCondId5432TransformerOvertemperaturePowerOff,
       "lgpCondId5433TransformerOvertemperature": lgpCondId5433TransformerOvertemperature,
       "lgpCondId5434TransformerTemperatureSensorFail": lgpCondId5434TransformerTemperatureSensorFail,
       "lgpCondId5436LowAmbientTemperatureProbeTwo": lgpCondId5436LowAmbientTemperatureProbeTwo,
       "lgpCondId5437HighAmbientTemperatureProbeTwo": lgpCondId5437HighAmbientTemperatureProbeTwo,
       "lgpCondId5438ThermalRunawayDetected": lgpCondId5438ThermalRunawayDetected,
       "lgpCondId5439BatteryStringEqualize": lgpCondId5439BatteryStringEqualize,
       "lgpCondId5440BatteryStringOffline": lgpCondId5440BatteryStringOffline,
       "lgpCondId5442DischargeLowCellVoltage": lgpCondId5442DischargeLowCellVoltage,
       "lgpCondId5447MMSPowerSharing": lgpCondId5447MMSPowerSharing,
       "lgpCondId5453ModuleInStandbyIntelligentParalleling": lgpCondId5453ModuleInStandbyIntelligentParalleling,
       "lgpCondId5456ECOModeActive": lgpCondId5456ECOModeActive,
       "lgpCondId5457ECOModeSuspended": lgpCondId5457ECOModeSuspended,
       "lgpCondId5458ExcessECOSuspends": lgpCondId5458ExcessECOSuspends,
       "lgpCondId5471DoorOpen": lgpCondId5471DoorOpen,
       "lgpCondId5472DoorSensorDisconnected": lgpCondId5472DoorSensorDisconnected,
       "lgpCondId5479ContactClosureOpen": lgpCondId5479ContactClosureOpen,
       "lgpCondId5480ContactClosureClosed": lgpCondId5480ContactClosureClosed,
       "lgpCondId5492ExtSystemCondensationDetected": lgpCondId5492ExtSystemCondensationDetected,
       "lgpCondId5495ExtFanIssue": lgpCondId5495ExtFanIssue,
       "lgpCondId5500ExtRemoteShutdown": lgpCondId5500ExtRemoteShutdown,
       "lgpCondId5505HotAisleTempOutofRange": lgpCondId5505HotAisleTempOutofRange,
       "lgpCondId5508ColdAisleTempOutofRange": lgpCondId5508ColdAisleTempOutofRange,
       "lgpCondId5512RemoteShutdown": lgpCondId5512RemoteShutdown,
       "lgpCondId5513CompressorCapacityReduced": lgpCondId5513CompressorCapacityReduced,
       "lgpCondId5514CompressorLowPressureTransducerIssue": lgpCondId5514CompressorLowPressureTransducerIssue,
       "lgpCondId5524PDUNeutralOverCurrent": lgpCondId5524PDUNeutralOverCurrent,
       "lgpCondId5531CondenserCommunicationLost": lgpCondId5531CondenserCommunicationLost,
       "lgpCondId5535CondenserOutsideAirTempSensorIssue": lgpCondId5535CondenserOutsideAirTempSensorIssue,
       "lgpCondId5536CondenserOutsideAirTempOutofOperatingRange": lgpCondId5536CondenserOutsideAirTempOutofOperatingRange,
       "lgpCondId5537CondenserControlBoardIssue": lgpCondId5537CondenserControlBoardIssue,
       "lgpCondId5539CondenserRefrigerantPressureOverThreshold": lgpCondId5539CondenserRefrigerantPressureOverThreshold,
       "lgpCondId5540CondenserRefrigerantPressureUnderThreshold": lgpCondId5540CondenserRefrigerantPressureUnderThreshold,
       "lgpCondId5541CondenserRefrigerantPressureSensorIssue": lgpCondId5541CondenserRefrigerantPressureSensorIssue,
       "lgpCondId5542CondenserSupplyRefrigerantOverTemp": lgpCondId5542CondenserSupplyRefrigerantOverTemp,
       "lgpCondId5543CondenserSupplyRefrigerantUnderTemp": lgpCondId5543CondenserSupplyRefrigerantUnderTemp,
       "lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue": lgpCondId5544CondenserSupplyRefrigerantTempSensorIssue,
       "lgpCondId5545CondenserMaxFanSpeedOverride": lgpCondId5545CondenserMaxFanSpeedOverride,
       "lgpCondId5559EvaporatorReturnFluidOverTemp": lgpCondId5559EvaporatorReturnFluidOverTemp,
       "lgpCondId5560EvaporatorReturnFluidUnderTemp": lgpCondId5560EvaporatorReturnFluidUnderTemp,
       "lgpCondId5561LBSActiveMaster": lgpCondId5561LBSActiveMaster,
       "lgpCondId5562LBSActiveSlave": lgpCondId5562LBSActiveSlave,
       "lgpCondId5563DCBusLowFault": lgpCondId5563DCBusLowFault,
       "lgpCondId5564FanContactorOpen": lgpCondId5564FanContactorOpen,
       "lgpCondId5565FanContactorOpenFail": lgpCondId5565FanContactorOpenFail,
       "lgpCondId5566FanContactorCloseFail": lgpCondId5566FanContactorCloseFail,
       "lgpCondId5567IPInhibit": lgpCondId5567IPInhibit,
       "lgpCondId5568InputUndervoltage": lgpCondId5568InputUndervoltage,
       "lgpCondId5569InputOvervoltage": lgpCondId5569InputOvervoltage,
       "lgpCondId5573AmbientAirSensorIssue": lgpCondId5573AmbientAirSensorIssue,
       "lgpCondId5577ExtDewPointUnderTemperature": lgpCondId5577ExtDewPointUnderTemperature,
       "lgpCondId5578DewPointOverTemperature": lgpCondId5578DewPointOverTemperature,
       "lgpCondId5579DewPointUnderTemperature": lgpCondId5579DewPointUnderTemperature,
       "lgpCondId5588UnspecifiedGeneralEvent": lgpCondId5588UnspecifiedGeneralEvent,
       "lgpCondId5593RemoteSensorAverageOverTemperature": lgpCondId5593RemoteSensorAverageOverTemperature,
       "lgpCondId5594RemoteSensorAverageUnderTemperature": lgpCondId5594RemoteSensorAverageUnderTemperature,
       "lgpCondId5595RemoteSensorSystemAverageOverTemperature": lgpCondId5595RemoteSensorSystemAverageOverTemperature,
       "lgpCondId5596RemoteSensorSystemAverageUnderTemperature": lgpCondId5596RemoteSensorSystemAverageUnderTemperature,
       "lgpCondId5597RemoteSensorOverTemperature": lgpCondId5597RemoteSensorOverTemperature,
       "lgpCondId5598RemoteSensorUnderTemperature": lgpCondId5598RemoteSensorUnderTemperature,
       "lgpCondId5600AirEconomizerEmergencyOverride": lgpCondId5600AirEconomizerEmergencyOverride,
       "lgpCondId5601AirEconomizerReducedAirflow": lgpCondId5601AirEconomizerReducedAirflow,
       "lgpCondId5604CompressorSuperheatOverThreshold": lgpCondId5604CompressorSuperheatOverThreshold,
       "lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent": lgpCondId5609ThermalRunawayCelltoAmbientTemperatureEvent,
       "lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent": lgpCondId5610ThermalRunawayCelltoCellTemperatureEvent,
       "lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent": lgpCondId5611ThermalRunawayChargerCurrentLevelOneEvent,
       "lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent": lgpCondId5612ThermalRunawayChargerCurrentLevelTwoEvent,
       "lgpCondId5617TemperatureControlSensorIssue": lgpCondId5617TemperatureControlSensorIssue,
       "lgpNotifications": lgpNotifications,
       "lgpEventNotifications": lgpEventNotifications,
       "lgpEventConditionEntryAdded": lgpEventConditionEntryAdded,
       "lgpEventConditionEntryRemoved": lgpEventConditionEntryRemoved,
       "lgpEventLowBatteryWarning": lgpEventLowBatteryWarning,
       "lgpEventLoadTransferedToBypass": lgpEventLoadTransferedToBypass,
       "lgpEventInternalFault": lgpEventInternalFault,
       "lgpEventBatteryTestFailed": lgpEventBatteryTestFailed,
       "lgpEventOutputOverload": lgpEventOutputOverload,
       "lgpEventEstablishedPowerRedundancy": lgpEventEstablishedPowerRedundancy,
       "lgpEventLostPowerRedundancy": lgpEventLostPowerRedundancy,
       "lgpEventPowerModuleFailure": lgpEventPowerModuleFailure,
       "lgpEventBatteryModuleFailure": lgpEventBatteryModuleFailure,
       "lgpEventControlModuleFailure": lgpEventControlModuleFailure,
       "lgpEventPowerModuleWarning": lgpEventPowerModuleWarning,
       "lgpEventBatteryModuleWarning": lgpEventBatteryModuleWarning,
       "lgpEventControlModuleWarning": lgpEventControlModuleWarning,
       "lgpEventAgentFirmwareUpdateSuccessful": lgpEventAgentFirmwareUpdateSuccessful,
       "lgpEventAgentFirmwareCorrupt": lgpEventAgentFirmwareCorrupt,
       "lgpEventConfigModified": lgpEventConfigModified,
       "lgpEventModuleAdded": lgpEventModuleAdded,
       "lgpEventModuleRemoved": lgpEventModuleRemoved,
       "lgpEventRcpPowerStateChangeOn": lgpEventRcpPowerStateChangeOn,
       "lgpEventRcpPowerStateChangeOff": lgpEventRcpPowerStateChangeOff,
       "lgpEventRcpLoadAdded": lgpEventRcpLoadAdded,
       "lgpEventRcpLoadRemoved": lgpEventRcpLoadRemoved,
       "lgpEventParameters": lgpEventParameters,
       "lgpEventParmTableRef": lgpEventParmTableRef,
       "lgpEventParmTableRowRef": lgpEventParmTableRowRef,
       "lgpEnvironmental": lgpEnvironmental,
       "lgpEnvTemperature": lgpEnvTemperature,
       "lgpEnvTemperatureWellKnown": lgpEnvTemperatureWellKnown,
       "lgpEnvControlTemperature": lgpEnvControlTemperature,
       "lgpEnvReturnAirTemperature": lgpEnvReturnAirTemperature,
       "lgpEnvSupplyAirTemperature": lgpEnvSupplyAirTemperature,
       "lgpAmbientTemperature": lgpAmbientTemperature,
       "lgpInverterTemperature": lgpInverterTemperature,
       "lgpBatteryTempterature": lgpBatteryTempterature,
       "lgpAcDcConverterTemperature": lgpAcDcConverterTemperature,
       "lgpPfcTemperature": lgpPfcTemperature,
       "lgpTransformerTemperature": lgpTransformerTemperature,
       "lgpLocalTemperature": lgpLocalTemperature,
       "lgpLocal1Temperature": lgpLocal1Temperature,
       "lgpLocal2Temperature": lgpLocal2Temperature,
       "lgpLocal3Temperature": lgpLocal3Temperature,
       "lgpDigitalScrollCompressorTemperature": lgpDigitalScrollCompressorTemperature,
       "lgpDigitalScrollCompressor1Temperature": lgpDigitalScrollCompressor1Temperature,
       "lgpDigitalScrollCompressor2Temperature": lgpDigitalScrollCompressor2Temperature,
       "lgpChillWaterTemperature": lgpChillWaterTemperature,
       "lgpCoolantTemperature": lgpCoolantTemperature,
       "lgpEnvEnclosureTemperatureSensors": lgpEnvEnclosureTemperatureSensors,
       "lgpEnvEnclosureTemperatureSensor1": lgpEnvEnclosureTemperatureSensor1,
       "lgpEnvEnclosureTemperatureSensor2": lgpEnvEnclosureTemperatureSensor2,
       "lgpEnvEnclosureTemperatureSensor3": lgpEnvEnclosureTemperatureSensor3,
       "lgpEnvEnclosureTemperatureSensor4": lgpEnvEnclosureTemperatureSensor4,
       "lgpEnvValueAmbientRoomTemperature": lgpEnvValueAmbientRoomTemperature,
       "lgpEnvDewPointTemperature": lgpEnvDewPointTemperature,
       "lgpEnvEnclosureTemperature": lgpEnvEnclosureTemperature,
       "lgpEnvAdjustedTemperature": lgpEnvAdjustedTemperature,
       "lgpEnvExternalSensors": lgpEnvExternalSensors,
       "lgpEnvExternalAirSensorA": lgpEnvExternalAirSensorA,
       "lgpEnvExternalAirSensorADewPoint": lgpEnvExternalAirSensorADewPoint,
       "lgpEnvExternalAirSensorB": lgpEnvExternalAirSensorB,
       "lgpEnvExternalAirSensorBDewPoint": lgpEnvExternalAirSensorBDewPoint,
       "lgpEnvSupplyFluidTemperature": lgpEnvSupplyFluidTemperature,
       "lgpEnvSupplyRefrigerantTemperature": lgpEnvSupplyRefrigerantTemperature,
       "lgpEnvMinDesiredRoomAirTemperature": lgpEnvMinDesiredRoomAirTemperature,
       "lgpEnvDewPointTemperatures": lgpEnvDewPointTemperatures,
       "lgpEnvInletDewPointTemperature": lgpEnvInletDewPointTemperature,
       "lgpEnvTemperatureFahrenheit": lgpEnvTemperatureFahrenheit,
       "lgpEnvTemperatureSettingDegF": lgpEnvTemperatureSettingDegF,
       "lgpEnvTemperatureToleranceDegF": lgpEnvTemperatureToleranceDegF,
       "lgpEnvTemperatureTableDegF": lgpEnvTemperatureTableDegF,
       "lgpEnvTemperatureEntryDegF": lgpEnvTemperatureEntryDegF,
       "lgpEnvTemperatureIdDegF": lgpEnvTemperatureIdDegF,
       "lgpEnvTemperatureDescrDegF": lgpEnvTemperatureDescrDegF,
       "lgpEnvTemperatureMeasurementDegF": lgpEnvTemperatureMeasurementDegF,
       "lgpEnvTemperatureHighThresholdDegF": lgpEnvTemperatureHighThresholdDegF,
       "lgpEnvTemperatureLowThresholdDegF": lgpEnvTemperatureLowThresholdDegF,
       "lgpEnvTemperatureSetPointDegF": lgpEnvTemperatureSetPointDegF,
       "lgpEnvTemperatureDailyHighDegF": lgpEnvTemperatureDailyHighDegF,
       "lgpEnvTemperatureDailyLowDegF": lgpEnvTemperatureDailyLowDegF,
       "lgpEnvTempDailyHighTimeHourDegF": lgpEnvTempDailyHighTimeHourDegF,
       "lgpEnvTempDailyHighTimeMinuteDegF": lgpEnvTempDailyHighTimeMinuteDegF,
       "lgpEnvTempDailyHighTimeSecondDegF": lgpEnvTempDailyHighTimeSecondDegF,
       "lgpEnvTempDailyLowTimeHourDegF": lgpEnvTempDailyLowTimeHourDegF,
       "lgpEnvTempDailyLowTimeMinuteDegF": lgpEnvTempDailyLowTimeMinuteDegF,
       "lgpEnvTempDailyLowTimeSecondDegF": lgpEnvTempDailyLowTimeSecondDegF,
       "lgpEnvTemperatureMeasurementTenthsDegF": lgpEnvTemperatureMeasurementTenthsDegF,
       "lgpEnvTemperatureHighThresholdTenthsDegF": lgpEnvTemperatureHighThresholdTenthsDegF,
       "lgpEnvTemperatureLowThresholdTenthsDegF": lgpEnvTemperatureLowThresholdTenthsDegF,
       "lgpEnvTemperatureSetPointTenthsDegF": lgpEnvTemperatureSetPointTenthsDegF,
       "lgpEnvTemperatureDeadBandTenthsDegF": lgpEnvTemperatureDeadBandTenthsDegF,
       "lgpEnvTempHeatingPropBandTenthsDegF": lgpEnvTempHeatingPropBandTenthsDegF,
       "lgpEnvTempCoolingPropBandTenthsDegF": lgpEnvTempCoolingPropBandTenthsDegF,
       "lgpEnvTemperatureDeadbandRangeDegF": lgpEnvTemperatureDeadbandRangeDegF,
       "lgpEnvTemperatureCelsius": lgpEnvTemperatureCelsius,
       "lgpEnvTemperatureSettingDegC": lgpEnvTemperatureSettingDegC,
       "lgpEnvTemperatureToleranceDegC": lgpEnvTemperatureToleranceDegC,
       "lgpEnvTemperatureTableDegC": lgpEnvTemperatureTableDegC,
       "lgpEnvTemperatureEntryDegC": lgpEnvTemperatureEntryDegC,
       "lgpEnvTemperatureIdDegC": lgpEnvTemperatureIdDegC,
       "lgpEnvTemperatureDescrDegC": lgpEnvTemperatureDescrDegC,
       "lgpEnvTemperatureMeasurementDegC": lgpEnvTemperatureMeasurementDegC,
       "lgpEnvTemperatureHighThresholdDegC": lgpEnvTemperatureHighThresholdDegC,
       "lgpEnvTemperatureLowThresholdDegC": lgpEnvTemperatureLowThresholdDegC,
       "lgpEnvTemperatureSetPointDegC": lgpEnvTemperatureSetPointDegC,
       "lgpEnvTemperatureDailyHighDegC": lgpEnvTemperatureDailyHighDegC,
       "lgpEnvTemperatureDailyLowDegC": lgpEnvTemperatureDailyLowDegC,
       "lgpEnvTempDailyHighTimeHourDegC": lgpEnvTempDailyHighTimeHourDegC,
       "lgpEnvTempDailyHighTimeMinuteDegC": lgpEnvTempDailyHighTimeMinuteDegC,
       "lgpEnvTempDailyHighTimeSecondDegC": lgpEnvTempDailyHighTimeSecondDegC,
       "lgpEnvTempDailyLowTimeHourDegC": lgpEnvTempDailyLowTimeHourDegC,
       "lgpEnvTempDailyLowTimeMinuteDegC": lgpEnvTempDailyLowTimeMinuteDegC,
       "lgpEnvTempDailyLowTimeSecondDegC": lgpEnvTempDailyLowTimeSecondDegC,
       "lgpEnvTemperatureMeasurementTenthsDegC": lgpEnvTemperatureMeasurementTenthsDegC,
       "lgpEnvTemperatureHighThresholdTenthsDegC": lgpEnvTemperatureHighThresholdTenthsDegC,
       "lgpEnvTemperatureLowThresholdTenthsDegC": lgpEnvTemperatureLowThresholdTenthsDegC,
       "lgpEnvTemperatureSetPointTenthsDegC": lgpEnvTemperatureSetPointTenthsDegC,
       "lgpEnvTemperatureDeadBandTenthsDegC": lgpEnvTemperatureDeadBandTenthsDegC,
       "lgpEnvTempHeatingPropBandTenthsDegC": lgpEnvTempHeatingPropBandTenthsDegC,
       "lgpEnvTempCoolingPropBandTenthsDegC": lgpEnvTempCoolingPropBandTenthsDegC,
       "lgpEnvTemperatureDeadbandRangeDegC": lgpEnvTemperatureDeadbandRangeDegC,
       "lgpEnvTemperatureControlMode": lgpEnvTemperatureControlMode,
       "lgpEnvHumidity": lgpEnvHumidity,
       "lgpEnvHumidityWellKnown": lgpEnvHumidityWellKnown,
       "lgpEnvControlHumidity": lgpEnvControlHumidity,
       "lgpEnvReturnAirHumidity": lgpEnvReturnAirHumidity,
       "lgpEnvSupplyAirHumidity": lgpEnvSupplyAirHumidity,
       "lgpEnvValueAmbientHumidity": lgpEnvValueAmbientHumidity,
       "lgpEnvHumidityRelative": lgpEnvHumidityRelative,
       "lgpEnvHumiditySettingRel": lgpEnvHumiditySettingRel,
       "lgpEnvHumidityToleranceRel": lgpEnvHumidityToleranceRel,
       "lgpEnvHumidityTableRel": lgpEnvHumidityTableRel,
       "lgpEnvHumidityEntryRel": lgpEnvHumidityEntryRel,
       "lgpEnvHumidityIdRel": lgpEnvHumidityIdRel,
       "lgpEnvHumidityDescrRel": lgpEnvHumidityDescrRel,
       "lgpEnvHumidityMeasurementRel": lgpEnvHumidityMeasurementRel,
       "lgpEnvHumidityHighThresholdRel": lgpEnvHumidityHighThresholdRel,
       "lgpEnvHumidityLowThresholdRel": lgpEnvHumidityLowThresholdRel,
       "lgpEnvHumiditySetPoint": lgpEnvHumiditySetPoint,
       "lgpEnvHumidityDailyHigh": lgpEnvHumidityDailyHigh,
       "lgpEnvHumidityDailyLow": lgpEnvHumidityDailyLow,
       "lgpEnvHumidityDailyHighTimeHour": lgpEnvHumidityDailyHighTimeHour,
       "lgpEnvHumidityDailyHighTimeMinute": lgpEnvHumidityDailyHighTimeMinute,
       "lgpEnvHumidityDailyHighTimeSecond": lgpEnvHumidityDailyHighTimeSecond,
       "lgpEnvHumidityDailyLowTimeHour": lgpEnvHumidityDailyLowTimeHour,
       "lgpEnvHumidityDailyLowTimeMinute": lgpEnvHumidityDailyLowTimeMinute,
       "lgpEnvHumidityDailyLowTimeSecond": lgpEnvHumidityDailyLowTimeSecond,
       "lgpEnvHumidityDeadBand": lgpEnvHumidityDeadBand,
       "lgpEnvHumidifyPropBand": lgpEnvHumidifyPropBand,
       "lgpEnvDehumidifyPropBand": lgpEnvDehumidifyPropBand,
       "lgpEnvHumidityMeasurementRelTenths": lgpEnvHumidityMeasurementRelTenths,
       "lgpEnvHumidityHighThresholdRelTenths": lgpEnvHumidityHighThresholdRelTenths,
       "lgpEnvHumidityLowThresholdRelTenths": lgpEnvHumidityLowThresholdRelTenths,
       "lgpEnvHumidityDeadbandRange": lgpEnvHumidityDeadbandRange,
       "lgpEnvState": lgpEnvState,
       "lgpEnvStateSystem": lgpEnvStateSystem,
       "lgpEnvStateCooling": lgpEnvStateCooling,
       "lgpEnvStateHeating": lgpEnvStateHeating,
       "lgpEnvStateHumidifying": lgpEnvStateHumidifying,
       "lgpEnvStateDehumidifying": lgpEnvStateDehumidifying,
       "lgpEnvStateEconoCycle": lgpEnvStateEconoCycle,
       "lgpEnvStateFan": lgpEnvStateFan,
       "lgpEnvStateGeneralAlarmOutput": lgpEnvStateGeneralAlarmOutput,
       "lgpEnvStateCoolingCapacity": lgpEnvStateCoolingCapacity,
       "lgpEnvStateHeatingCapacity": lgpEnvStateHeatingCapacity,
       "lgpEnvStateAudibleAlarm": lgpEnvStateAudibleAlarm,
       "lgpEnvStateCoolingUnits": lgpEnvStateCoolingUnits,
       "lgpEnvStateCoolingUnit1": lgpEnvStateCoolingUnit1,
       "lgpEnvStateCoolingUnit2": lgpEnvStateCoolingUnit2,
       "lgpEnvStateCoolingUnit3": lgpEnvStateCoolingUnit3,
       "lgpEnvStateCoolingUnit4": lgpEnvStateCoolingUnit4,
       "lgpEnvStateHeatingUnits": lgpEnvStateHeatingUnits,
       "lgpEnvStateHeatingUnit1": lgpEnvStateHeatingUnit1,
       "lgpEnvStateHeatingUnit2": lgpEnvStateHeatingUnit2,
       "lgpEnvStateHeatingUnit3": lgpEnvStateHeatingUnit3,
       "lgpEnvStateHeatingUnit4": lgpEnvStateHeatingUnit4,
       "lgpEnvStateOperatingReason": lgpEnvStateOperatingReason,
       "lgpEnvStateOperatingMode": lgpEnvStateOperatingMode,
       "lgpEnvStateFanCapacity": lgpEnvStateFanCapacity,
       "lgpEnvStateFreeCoolingCapacity": lgpEnvStateFreeCoolingCapacity,
       "lgpEnvStateDehumidifyingCapacity": lgpEnvStateDehumidifyingCapacity,
       "lgpEnvStateHumidifyingCapacity": lgpEnvStateHumidifyingCapacity,
       "lgpEnvStateFreeCooling": lgpEnvStateFreeCooling,
       "lgpEnvStateElectricHeater": lgpEnvStateElectricHeater,
       "lgpEnvStateHotWater": lgpEnvStateHotWater,
       "lgpEnvStateOperatingEfficiency": lgpEnvStateOperatingEfficiency,
       "lgpEnvComponentStateTable": lgpEnvComponentStateTable,
       "lgpEnvComponentStateEntry": lgpEnvComponentStateEntry,
       "lgpEnvComponentStateIndex": lgpEnvComponentStateIndex,
       "lgpEnvComponentStateDescr": lgpEnvComponentStateDescr,
       "lgpEnvComponentState": lgpEnvComponentState,
       "lgpEnvValveTable": lgpEnvValveTable,
       "lgpEnvValveEntry": lgpEnvValveEntry,
       "lgpEnvValveIndex": lgpEnvValveIndex,
       "lgpEnvValveDescr": lgpEnvValveDescr,
       "lgpEnvValveState": lgpEnvValveState,
       "lgpEnvValvePositionTenths": lgpEnvValvePositionTenths,
       "lgpEnvConfig": lgpEnvConfig,
       "lgpEnvConfigReheatLockout": lgpEnvConfigReheatLockout,
       "lgpEnvConfigHumLockout": lgpEnvConfigHumLockout,
       "lgpEnvConfigRestartDelay": lgpEnvConfigRestartDelay,
       "lgpEnvConfigRemoteShutdown": lgpEnvConfigRemoteShutdown,
       "lgpEnvConfigCoolingServiceInterval": lgpEnvConfigCoolingServiceInterval,
       "lgpEnvConfigHumidifierServiceInterval": lgpEnvConfigHumidifierServiceInterval,
       "lgpEnvConfigFilterServiceInterval": lgpEnvConfigFilterServiceInterval,
       "lgpEnvConfigSleepModeDeadbandRangeDegC": lgpEnvConfigSleepModeDeadbandRangeDegC,
       "lgpEnvConfigSleepModeDeadbandRangeDegF": lgpEnvConfigSleepModeDeadbandRangeDegF,
       "lgpEnvConfigSupplyTempLowLimitDegF": lgpEnvConfigSupplyTempLowLimitDegF,
       "lgpEnvConfigSupplyTempLowLimitDegC": lgpEnvConfigSupplyTempLowLimitDegC,
       "lgpEnvConfigTemperatureIntegTime": lgpEnvConfigTemperatureIntegTime,
       "lgpEnvConfigLocalTemperatureUnit": lgpEnvConfigLocalTemperatureUnit,
       "lgpEnvConfigSleepMode": lgpEnvConfigSleepMode,
       "lgpEnvConfigHumidityIntegTime": lgpEnvConfigHumidityIntegTime,
       "lgpEnvConfigFreecoolingDeltaDegF": lgpEnvConfigFreecoolingDeltaDegF,
       "lgpEnvConfigFreecoolingDeltaDegC": lgpEnvConfigFreecoolingDeltaDegC,
       "lgpEnvConfigSupplyTempLowLimit": lgpEnvConfigSupplyTempLowLimit,
       "lgpEnvConfigSensorEventsStandard": lgpEnvConfigSensorEventsStandard,
       "lgpEnvConfigSensorEvents1": lgpEnvConfigSensorEvents1,
       "lgpEnvConfigSleepModeDeadbandRange": lgpEnvConfigSleepModeDeadbandRange,
       "lgpEnvConfigAutoConfiguration": lgpEnvConfigAutoConfiguration,
       "lgpEnvConfigDeltaGlycolType": lgpEnvConfigDeltaGlycolType,
       "lgpEnvConfigChillWaterControl": lgpEnvConfigChillWaterControl,
       "lgpEnvConfigInfaredFlushRate": lgpEnvConfigInfaredFlushRate,
       "lgpEnvConfigHumidityControl": lgpEnvConfigHumidityControl,
       "lgpEnvConfigCompressorLockout": lgpEnvConfigCompressorLockout,
       "lgpEnvConfigReheatAndHumidifierLockout": lgpEnvConfigReheatAndHumidifierLockout,
       "lgpEnvOperationalTimeTable": lgpEnvOperationalTimeTable,
       "lgpEnvOperationalTimeEntry": lgpEnvOperationalTimeEntry,
       "lgpEnvOperationTimeIndex": lgpEnvOperationTimeIndex,
       "lgpEnvOperationTimePoint": lgpEnvOperationTimePoint,
       "lgpEnvOperationTimeSubID": lgpEnvOperationTimeSubID,
       "lgpEnvOperationTimeUnit": lgpEnvOperationTimeUnit,
       "lgpEnvOperationTimeValue": lgpEnvOperationTimeValue,
       "lgpEnvOperationTimeHighWarning": lgpEnvOperationTimeHighWarning,
       "lgpEnvConfigTempControlAlgorithm": lgpEnvConfigTempControlAlgorithm,
       "lgpEnvConfigFanSpeedMode": lgpEnvConfigFanSpeedMode,
       "lgpEnvConfigFanSpeedCapacity": lgpEnvConfigFanSpeedCapacity,
       "lgpEnvConfigBmsResetTimer": lgpEnvConfigBmsResetTimer,
       "lgpEnvConfigDisableSensorOffsetDegC": lgpEnvConfigDisableSensorOffsetDegC,
       "lgpEnvConfigDisableSensorOffsetDegF": lgpEnvConfigDisableSensorOffsetDegF,
       "lgpEnvConfigCabinetSensorAlarms": lgpEnvConfigCabinetSensorAlarms,
       "lgpEnvConfigAirTemperatureControlSensor": lgpEnvConfigAirTemperatureControlSensor,
       "lgpEnvConfigFanSpeedControlSensor": lgpEnvConfigFanSpeedControlSensor,
       "lgpEnvConfigMinFanSpeed": lgpEnvConfigMinFanSpeed,
       "lgpEnvConfigMaxFanSpeed": lgpEnvConfigMaxFanSpeed,
       "lgpEnvConfigFanSpeedPropBandDegC": lgpEnvConfigFanSpeedPropBandDegC,
       "lgpEnvConfigFanSpeedPropBandDegF": lgpEnvConfigFanSpeedPropBandDegF,
       "lgpEnvControl": lgpEnvControl,
       "lgpEnvControlShutdownAfterDelay": lgpEnvControlShutdownAfterDelay,
       "lgpEnvControlStartupAfterDelay": lgpEnvControlStartupAfterDelay,
       "lgpEnvSleepIntervalTimeTable": lgpEnvSleepIntervalTimeTable,
       "lgpEnvSleepIntervalTimeEntry": lgpEnvSleepIntervalTimeEntry,
       "lgpEnvSleepTimeIndex": lgpEnvSleepTimeIndex,
       "lgpEnvSleepTimeSubID": lgpEnvSleepTimeSubID,
       "lgpEnvSleepTimeStartHour": lgpEnvSleepTimeStartHour,
       "lgpEnvSleepTimeStartMinute": lgpEnvSleepTimeStartMinute,
       "lgpEnvSleepTimeStopHour": lgpEnvSleepTimeStopHour,
       "lgpEnvSleepTimeStopMinute": lgpEnvSleepTimeStopMinute,
       "lgpEnvSleepDayTable": lgpEnvSleepDayTable,
       "lgpEnvSleepDayEntry": lgpEnvSleepDayEntry,
       "lgpEnvSleepDayIndex": lgpEnvSleepDayIndex,
       "lgpEnvSleepDay": lgpEnvSleepDay,
       "lgpEnvSleepAllDayEnabled": lgpEnvSleepAllDayEnabled,
       "lgpEnvStatistics": lgpEnvStatistics,
       "lgpEnvStatisticsComp1RunHr": lgpEnvStatisticsComp1RunHr,
       "lgpEnvStatisticsComp2RunHr": lgpEnvStatisticsComp2RunHr,
       "lgpEnvStatisticsFanRunHr": lgpEnvStatisticsFanRunHr,
       "lgpEnvStatisticsHumRunHr": lgpEnvStatisticsHumRunHr,
       "lgpEnvStatisticsReheat1RunHr": lgpEnvStatisticsReheat1RunHr,
       "lgpEnvStatisticsReheat2RunHr": lgpEnvStatisticsReheat2RunHr,
       "lgpEnvStatisticsReheat3RunHr": lgpEnvStatisticsReheat3RunHr,
       "lgpEnvStatisticsCoolingModeHrs": lgpEnvStatisticsCoolingModeHrs,
       "lgpEnvStatisticsHeatingModeHrs": lgpEnvStatisticsHeatingModeHrs,
       "lgpEnvStatisticsHumidifyModeHrs": lgpEnvStatisticsHumidifyModeHrs,
       "lgpEnvStatisticsDehumidifyModeHrs": lgpEnvStatisticsDehumidifyModeHrs,
       "lgpEnvStatisticsHotGasRunHr": lgpEnvStatisticsHotGasRunHr,
       "lgpEnvStatisticsHotWaterRunHr": lgpEnvStatisticsHotWaterRunHr,
       "lgpEnvStatisticsFreeCoolRunHr": lgpEnvStatisticsFreeCoolRunHr,
       "lgpEnvStatisticsComp3RunHr": lgpEnvStatisticsComp3RunHr,
       "lgpEnvStatisticsComp4RunHr": lgpEnvStatisticsComp4RunHr,
       "lgpEnvPoints": lgpEnvPoints,
       "lgpEnvWellKnownPoints": lgpEnvWellKnownPoints,
       "lgpEnvFanPoint": lgpEnvFanPoint,
       "lgpEnvCompressorPoint": lgpEnvCompressorPoint,
       "lgpEnvElectricHeaterPoint": lgpEnvElectricHeaterPoint,
       "lgpEnvChilledWaterPoint": lgpEnvChilledWaterPoint,
       "lgpEnvHumidifierPoint": lgpEnvHumidifierPoint,
       "lgpEnvDehumidifierPoint": lgpEnvDehumidifierPoint,
       "lgpEnvFreeCoolingPoint": lgpEnvFreeCoolingPoint,
       "lgpEnvHotWaterPoint": lgpEnvHotWaterPoint,
       "lgpEnvHotGasPoint": lgpEnvHotGasPoint,
       "lgpEnvBatteryCabinetPoint": lgpEnvBatteryCabinetPoint,
       "lgpEnvPumpPoints": lgpEnvPumpPoints,
       "lgpEnvPump1Point": lgpEnvPump1Point,
       "lgpEnvPump2Point": lgpEnvPump2Point,
       "lgpEnvCompressorPoints": lgpEnvCompressorPoints,
       "lgpEnvCompressor1Point": lgpEnvCompressor1Point,
       "lgpEnvCompressor1APoint": lgpEnvCompressor1APoint,
       "lgpEnvCompressor1BPoint": lgpEnvCompressor1BPoint,
       "lgpEnvCompressor2Point": lgpEnvCompressor2Point,
       "lgpEnvCompressor2APoint": lgpEnvCompressor2APoint,
       "lgpEnvCompressor2BPoint": lgpEnvCompressor2BPoint,
       "lgpEnvValvePoints": lgpEnvValvePoints,
       "lgpEnvHotGasValve1Point": lgpEnvHotGasValve1Point,
       "lgpEnvHotGasValve2Point": lgpEnvHotGasValve2Point,
       "lgpEnvRemoteSensorStatisticPoints": lgpEnvRemoteSensorStatisticPoints,
       "lgpEnvRemoteSensorMinimumPoint": lgpEnvRemoteSensorMinimumPoint,
       "lgpEnvRemoteSensorMaximumPoint": lgpEnvRemoteSensorMaximumPoint,
       "lgpEnvRemoteSensorAveragePoint": lgpEnvRemoteSensorAveragePoint,
       "lgpEnvUnits": lgpEnvUnits,
       "lgpEnvWellKnownUnits": lgpEnvWellKnownUnits,
       "lgpEnvHours": lgpEnvHours,
       "lgpEnvRemoteSensors": lgpEnvRemoteSensors,
       "lgpEnvRemoteSensorCalc": lgpEnvRemoteSensorCalc,
       "lgpEnvRemoteSensorTable": lgpEnvRemoteSensorTable,
       "lgpEnvRemoteSensorEntry": lgpEnvRemoteSensorEntry,
       "lgpEnvRemoteSensorIndex": lgpEnvRemoteSensorIndex,
       "lgpEnvRemoteSensorId": lgpEnvRemoteSensorId,
       "lgpEnvRemoteSensorMode": lgpEnvRemoteSensorMode,
       "lgpEnvRemoteSensorUsrLabel": lgpEnvRemoteSensorUsrLabel,
       "lgpEnvRemoteSensorTempMeasurementDegF": lgpEnvRemoteSensorTempMeasurementDegF,
       "lgpEnvRemoteSensorTempMeasurementDegC": lgpEnvRemoteSensorTempMeasurementDegC,
       "lgpPower": lgpPower,
       "lgpPwrBattery": lgpPwrBattery,
       "lgpPwrNumberInstalledBatteryModules": lgpPwrNumberInstalledBatteryModules,
       "lgpPwrNumberFailedBatteryModules": lgpPwrNumberFailedBatteryModules,
       "lgpPwrNumberRedundantBatteryModules": lgpPwrNumberRedundantBatteryModules,
       "lgpPwrNumberActiveBatteryModules": lgpPwrNumberActiveBatteryModules,
       "lgpPwrConfigLowBatteryWarningTime": lgpPwrConfigLowBatteryWarningTime,
       "lgpPwrNumberBatteryModuleWarnings": lgpPwrNumberBatteryModuleWarnings,
       "lgpPwrBatteryCount": lgpPwrBatteryCount,
       "lgpPwrBatteryTestResult": lgpPwrBatteryTestResult,
       "lgpPwrNominalBatteryCapacity": lgpPwrNominalBatteryCapacity,
       "lgpPwrBatteryFloatVoltage": lgpPwrBatteryFloatVoltage,
       "lgpPwrBatteryEndOfDischargeVoltage": lgpPwrBatteryEndOfDischargeVoltage,
       "lgpPwrAutomaticBatteryTestInterval": lgpPwrAutomaticBatteryTestInterval,
       "lgpPwrAutomaticBatteryTestCountdown": lgpPwrAutomaticBatteryTestCountdown,
       "lgpPwrBatteryChargeStatus": lgpPwrBatteryChargeStatus,
       "lgpPwrBatteryLifeEnhancer": lgpPwrBatteryLifeEnhancer,
       "lgpPwrBatteryCharger": lgpPwrBatteryCharger,
       "lgpPwrBatteryChargeMode": lgpPwrBatteryChargeMode,
       "lgpPwrBatteryTimeRemaining": lgpPwrBatteryTimeRemaining,
       "lgpPwrBatteryCapacity": lgpPwrBatteryCapacity,
       "lgpPwrBatteryCabinet": lgpPwrBatteryCabinet,
       "lgpPwrBatteryCabinetCount": lgpPwrBatteryCabinetCount,
       "lgpPwrBatteryCabinetType": lgpPwrBatteryCabinetType,
       "lgpPwrBatteryCabinetRatedCapacity": lgpPwrBatteryCabinetRatedCapacity,
       "lgpPwrBatteryLeadAcidCellCount": lgpPwrBatteryLeadAcidCellCount,
       "lgpPwrBatteryNiCadCellCount": lgpPwrBatteryNiCadCellCount,
       "lgpPwrBatteryAmpHoursConsumed": lgpPwrBatteryAmpHoursConsumed,
       "lgpPwrBatteryAmpHoursDischargeConsumed": lgpPwrBatteryAmpHoursDischargeConsumed,
       "lgpPwrBatteryLastDischargeTime": lgpPwrBatteryLastDischargeTime,
       "lgpPwrBatteryLastCommissionTime": lgpPwrBatteryLastCommissionTime,
       "lgpPwrBatteryPresentDischargeTime": lgpPwrBatteryPresentDischargeTime,
       "lgpPwrBatteryCapacityStatus": lgpPwrBatteryCapacityStatus,
       "lgpPwrBatteryCircuitBreakerState": lgpPwrBatteryCircuitBreakerState,
       "lgpPwrMeasurements": lgpPwrMeasurements,
       "lgpPwrWellKnownMeasurementPoints": lgpPwrWellKnownMeasurementPoints,
       "lgpPwrSource1Input": lgpPwrSource1Input,
       "lgpPwrSource2Input": lgpPwrSource2Input,
       "lgpPwrSourcePdu1Input": lgpPwrSourcePdu1Input,
       "lgpPwrSourcePdu2Input": lgpPwrSourcePdu2Input,
       "lgpPwrOutputToLoad": lgpPwrOutputToLoad,
       "lgpPwrMeasBattery": lgpPwrMeasBattery,
       "lgpPwrMeasBypass": lgpPwrMeasBypass,
       "lgpPwrMeasDcBus": lgpPwrMeasDcBus,
       "lgpPwrMeasSystemOutput": lgpPwrMeasSystemOutput,
       "lgpPwrMeasBatteryCabinet": lgpPwrMeasBatteryCabinet,
       "lgpPwrMeasurementPointTable": lgpPwrMeasurementPointTable,
       "lgpPwrMeasurementPointEntry": lgpPwrMeasurementPointEntry,
       "lgpPwrMeasurementPointIndex": lgpPwrMeasurementPointIndex,
       "lgpPwrMeasurementPointId": lgpPwrMeasurementPointId,
       "lgpPwrMeasurementPointNumLines": lgpPwrMeasurementPointNumLines,
       "lgpPwrMeasurementPointNomVolts": lgpPwrMeasurementPointNomVolts,
       "lgpPwrMeasurementPointNomFrequency": lgpPwrMeasurementPointNomFrequency,
       "lgpPwrMeasurementPointFrequency": lgpPwrMeasurementPointFrequency,
       "lgpPwrMeasurementPointApparentPower": lgpPwrMeasurementPointApparentPower,
       "lgpPwrMeasurementPointTruePower": lgpPwrMeasurementPointTruePower,
       "lgpPwrMeasurementPointPowerFactor": lgpPwrMeasurementPointPowerFactor,
       "lgpPwrMeasurementPointWattHours": lgpPwrMeasurementPointWattHours,
       "lgpPwrMeasurementPointVAPercent": lgpPwrMeasurementPointVAPercent,
       "lgpPwrMeasurementPointNeutralCurrent": lgpPwrMeasurementPointNeutralCurrent,
       "lgpPwrMeasurementPointGroundCurrent": lgpPwrMeasurementPointGroundCurrent,
       "lgpPwrMeasurementPointNomCurrent": lgpPwrMeasurementPointNomCurrent,
       "lgpPwrMeasurementPointNomPowerFactor": lgpPwrMeasurementPointNomPowerFactor,
       "lgpPwrMeasurementPointNomVA": lgpPwrMeasurementPointNomVA,
       "lgpPwrMeasurementPointNomW": lgpPwrMeasurementPointNomW,
       "lgpPwrMeasurementPointPowerFactorTag": lgpPwrMeasurementPointPowerFactorTag,
       "lgpPwrLineMeasurementTable": lgpPwrLineMeasurementTable,
       "lgpPwrLineMeasurementEntry": lgpPwrLineMeasurementEntry,
       "lgpPwrMeasurementPtIndex": lgpPwrMeasurementPtIndex,
       "lgpPwrLineMeasurementIndex": lgpPwrLineMeasurementIndex,
       "lgpPwrMeasurementPoint": lgpPwrMeasurementPoint,
       "lgpPwrLineMeasurementVoltsLL": lgpPwrLineMeasurementVoltsLL,
       "lgpPwrLineMeasurementVoltsLN": lgpPwrLineMeasurementVoltsLN,
       "lgpPwrLineMeasurementCurrent": lgpPwrLineMeasurementCurrent,
       "lgpPwrLineMeasurementCapacity": lgpPwrLineMeasurementCapacity,
       "lgpPwrLineMeasurementVA": lgpPwrLineMeasurementVA,
       "lgpPwrLineMeasurementTruePower": lgpPwrLineMeasurementTruePower,
       "lgpPwrLineMeasurementVoltageTHD": lgpPwrLineMeasurementVoltageTHD,
       "lgpPwrLineMeasurementCurrentTHD": lgpPwrLineMeasurementCurrentTHD,
       "lgpPwrLineMeasurementKFactorCurrent": lgpPwrLineMeasurementKFactorCurrent,
       "lgpPwrLineMeasurementCrestFactorCurrent": lgpPwrLineMeasurementCrestFactorCurrent,
       "lgpPwrLineMeasurementPowerFactor": lgpPwrLineMeasurementPowerFactor,
       "lgpPwrLineMeasurementPowerFactorTag": lgpPwrLineMeasurementPowerFactorTag,
       "lgpPwrLineMeasurementMaxVolts": lgpPwrLineMeasurementMaxVolts,
       "lgpPwrLineMeasurementMinVolts": lgpPwrLineMeasurementMinVolts,
       "lgpPwrLineMeasurementVAR": lgpPwrLineMeasurementVAR,
       "lgpPwrLineMeasurementPercentLoad": lgpPwrLineMeasurementPercentLoad,
       "lgpPwrLineMeasurementVolts": lgpPwrLineMeasurementVolts,
       "lgpPwrLineMeasurementVACapacity": lgpPwrLineMeasurementVACapacity,
       "lgpPwrDcMeasurementPointTable": lgpPwrDcMeasurementPointTable,
       "lgpPwrDcMeasurementPointEntry": lgpPwrDcMeasurementPointEntry,
       "lgpPwrDcMeasurementPointIndex": lgpPwrDcMeasurementPointIndex,
       "lgpPwrDcMeasurementPointId": lgpPwrDcMeasurementPointId,
       "lgpPwrDcMeasurementPointSubID": lgpPwrDcMeasurementPointSubID,
       "lgpPwrDcMeasurementPointVolts": lgpPwrDcMeasurementPointVolts,
       "lgpPwrDcMeasurementPointCurrent": lgpPwrDcMeasurementPointCurrent,
       "lgpPwrDcMeasurementPointNomVolts": lgpPwrDcMeasurementPointNomVolts,
       "lgpPwrDcMeasurementPointTruePower": lgpPwrDcMeasurementPointTruePower,
       "lgpPwrWellKnownMeasurementTypes": lgpPwrWellKnownMeasurementTypes,
       "lgpPwrVoltsAc": lgpPwrVoltsAc,
       "lgpPwrVoltsDc": lgpPwrVoltsDc,
       "lgpPwrAmpsNeutral": lgpPwrAmpsNeutral,
       "lgpPwrStatus": lgpPwrStatus,
       "lgpPwrTransferCount": lgpPwrTransferCount,
       "lgpPwrAutoTransferTimer": lgpPwrAutoTransferTimer,
       "lgpPwrAutoReTransferEnabled": lgpPwrAutoReTransferEnabled,
       "lgpPwrSyncPhaseAngle": lgpPwrSyncPhaseAngle,
       "lgpPwrParallelSystemOutputToLoadSource": lgpPwrParallelSystemOutputToLoadSource,
       "lgpPwrDcToDcConverter": lgpPwrDcToDcConverter,
       "lgpPwrOutputToLoadOnInverter": lgpPwrOutputToLoadOnInverter,
       "lgpPwrBatteryChargeCompensating": lgpPwrBatteryChargeCompensating,
       "lgpPwrInverterReady": lgpPwrInverterReady,
       "lgpPwrOutputToLoadOnBypass": lgpPwrOutputToLoadOnBypass,
       "lgpPwrBoost": lgpPwrBoost,
       "lgpPwrBuck": lgpPwrBuck,
       "lgpPwrShutdownOverTemperature": lgpPwrShutdownOverTemperature,
       "lgpPwrShutdownOverload": lgpPwrShutdownOverload,
       "lgpPwrShutdownDcBusOverload": lgpPwrShutdownDcBusOverload,
       "lgpPwrShutdownOutputShort": lgpPwrShutdownOutputShort,
       "lgpPwrShutdownLineSwap": lgpPwrShutdownLineSwap,
       "lgpPwrShutdownLowBattery": lgpPwrShutdownLowBattery,
       "lgpPwrShutdownRemote": lgpPwrShutdownRemote,
       "lgpPwrShutdownInputUnderVoltage": lgpPwrShutdownInputUnderVoltage,
       "lgpPwrShutdownPowerFactorCorrectionFailure": lgpPwrShutdownPowerFactorCorrectionFailure,
       "lgpPwrShutdownHardware": lgpPwrShutdownHardware,
       "lgpPwrRedundantSubModule": lgpPwrRedundantSubModule,
       "lgpPwrBypassReady": lgpPwrBypassReady,
       "lgpPwrGeneratorStatus": lgpPwrGeneratorStatus,
       "lgpPwrRotaryBreakerStatus": lgpPwrRotaryBreakerStatus,
       "lgpPwrPowerFactorCorrection": lgpPwrPowerFactorCorrection,
       "lgpPwrBypassSyncDiff": lgpPwrBypassSyncDiff,
       "lgpPwrBypassOverloadShutdownTime": lgpPwrBypassOverloadShutdownTime,
       "lgpPwrInverterOverloadShutdownTime": lgpPwrInverterOverloadShutdownTime,
       "lgpPwrStateOutputSource": lgpPwrStateOutputSource,
       "lgpPwrStateInputSource": lgpPwrStateInputSource,
       "lgpPwrStateInputQualification": lgpPwrStateInputQualification,
       "lgpPwrStateBypassStaticSwitchState": lgpPwrStateBypassStaticSwitchState,
       "lgpPwrStateBypassQualification": lgpPwrStateBypassQualification,
       "lgpPwrStateDCBusQualification": lgpPwrStateDCBusQualification,
       "lgpPwrStateOutQualification": lgpPwrStateOutQualification,
       "lgpPwrStateInverterQualification": lgpPwrStateInverterQualification,
       "lgpPwrStateInverterState": lgpPwrStateInverterState,
       "lgpPwrStateRectifierState": lgpPwrStateRectifierState,
       "lgpPwrStateModuleGroup": lgpPwrStateModuleGroup,
       "lgpPwrStateUpsModuleCount": lgpPwrStateUpsModuleCount,
       "lgpPwrStateUpsModuleRedundantCount": lgpPwrStateUpsModuleRedundantCount,
       "lgpPwrStateBackfeedBrkrState": lgpPwrStateBackfeedBrkrState,
       "lgpPwrStateLoadDisconnectState": lgpPwrStateLoadDisconnectState,
       "lgpPwrStateInputBrkrState": lgpPwrStateInputBrkrState,
       "lgpPwrStateTrapFilterBrkrState": lgpPwrStateTrapFilterBrkrState,
       "lgpPwrStateInvOutputBrkrState": lgpPwrStateInvOutputBrkrState,
       "lgpPwrStateIntBypassBrkrState": lgpPwrStateIntBypassBrkrState,
       "lgpPwrStateBypassIsolBrkrState": lgpPwrStateBypassIsolBrkrState,
       "lgpPwrStateRectifierIsolBrkrState": lgpPwrStateRectifierIsolBrkrState,
       "lgpPwrStateMaintBypassBrkrState": lgpPwrStateMaintBypassBrkrState,
       "lgpPwrStateMaintIsolBrkrState": lgpPwrStateMaintIsolBrkrState,
       "lgpPwrStateOutStaticSwState": lgpPwrStateOutStaticSwState,
       "lgpPwrStateModuleOutBrkrState": lgpPwrStateModuleOutBrkrState,
       "lgpPwrBypassReXfrRemainTime": lgpPwrBypassReXfrRemainTime,
       "lgpPwrStateUpsOutputSource": lgpPwrStateUpsOutputSource,
       "lgpPwrStateLoadBusSynchronization": lgpPwrStateLoadBusSynchronization,
       "lgpPwrSettings": lgpPwrSettings,
       "lgpPwrPreferredSource": lgpPwrPreferredSource,
       "lgpPwrLoadOnSource": lgpPwrLoadOnSource,
       "lgpPwrNominalVoltageDeviation": lgpPwrNominalVoltageDeviation,
       "lgpPwrNominalVoltageDeviationPercent": lgpPwrNominalVoltageDeviationPercent,
       "lgpPwrPhaseDifferenceLimit": lgpPwrPhaseDifferenceLimit,
       "lgpPwrFrequencyDeviationLimit": lgpPwrFrequencyDeviationLimit,
       "lgpPwrThresholdTable": lgpPwrThresholdTable,
       "lgpPwrThresholdEntry": lgpPwrThresholdEntry,
       "lgpPwrThresholdIndex": lgpPwrThresholdIndex,
       "lgpPwrThresholdPoint": lgpPwrThresholdPoint,
       "lgpPwrThresholdSubID": lgpPwrThresholdSubID,
       "lgpPwrThresholdType": lgpPwrThresholdType,
       "lgpPwrThresholdHighWarning": lgpPwrThresholdHighWarning,
       "lgpPwrThresholdHighFailure": lgpPwrThresholdHighFailure,
       "lgpPwrThresholdLowWarning": lgpPwrThresholdLowWarning,
       "lgpPwrThresholdLowFailure": lgpPwrThresholdLowFailure,
       "lgpPwrUpsAutoRestart": lgpPwrUpsAutoRestart,
       "lgpPwrUpsAutoRestartDelay": lgpPwrUpsAutoRestartDelay,
       "lgpPwrAutoRestartBatteryChargeThreshold": lgpPwrAutoRestartBatteryChargeThreshold,
       "lgpPwrParallelModuleCount": lgpPwrParallelModuleCount,
       "lgpPwrParallelRedundancyCount": lgpPwrParallelRedundancyCount,
       "lgpPwrLoadBusSyncMode": lgpPwrLoadBusSyncMode,
       "lgpPwrEconomicOperationMode": lgpPwrEconomicOperationMode,
       "lgpPwrAutomaticBatteryTest": lgpPwrAutomaticBatteryTest,
       "lgpPwrMinimumRedundantPowerModule": lgpPwrMinimumRedundantPowerModule,
       "lgpPwrMinimumRedundantBatteryModule": lgpPwrMinimumRedundantBatteryModule,
       "lgpPwrOutputToLoadUserOverloadLimit": lgpPwrOutputToLoadUserOverloadLimit,
       "lgpPwrNoLoadWarningLimit": lgpPwrNoLoadWarningLimit,
       "lgpPwrNoLoadWarningDelay": lgpPwrNoLoadWarningDelay,
       "lgpPwrConversion": lgpPwrConversion,
       "lgpPwrNumberInstalledPowerModules": lgpPwrNumberInstalledPowerModules,
       "lgpPwrNumberFailedPowerModules": lgpPwrNumberFailedPowerModules,
       "lgpPwrNumberRedundantPowerModules": lgpPwrNumberRedundantPowerModules,
       "lgpPwrNumberActivePowerModules": lgpPwrNumberActivePowerModules,
       "lgpPwrNumberPowerModuleWarnings": lgpPwrNumberPowerModuleWarnings,
       "lgpPwrUpsInverterStandby": lgpPwrUpsInverterStandby,
       "lgpPwrControl": lgpPwrControl,
       "lgpPwrWellKnownControlPoints": lgpPwrWellKnownControlPoints,
       "lgpPwrLoadCircuit": lgpPwrLoadCircuit,
       "lgpPwrLoadCircuitTable": lgpPwrLoadCircuitTable,
       "lgpPwrLoadCircuitEntry": lgpPwrLoadCircuitEntry,
       "lgpPwrLoadCircuitIndex": lgpPwrLoadCircuitIndex,
       "lgpPwrLoadCircuitId": lgpPwrLoadCircuitId,
       "lgpPwrLoadCircuitSubID": lgpPwrLoadCircuitSubID,
       "lgpPwrLoadCircuitState": lgpPwrLoadCircuitState,
       "lgpPwrAlarmSilence": lgpPwrAlarmSilence,
       "lgpPwrBatteryTest": lgpPwrBatteryTest,
       "lgpPwrUpsAbortCommand": lgpPwrUpsAbortCommand,
       "lgpPwrTransferToBypass": lgpPwrTransferToBypass,
       "lgpPwrTransferToInverter": lgpPwrTransferToInverter,
       "lgpPwrOutputOnDelay": lgpPwrOutputOnDelay,
       "lgpPwrOutputOffDelayWithRestart": lgpPwrOutputOffDelayWithRestart,
       "lgpPwrOutputOffDelayWithoutRestart": lgpPwrOutputOffDelayWithoutRestart,
       "lgpPwrTopology": lgpPwrTopology,
       "lgpPwrUpsTopOffline": lgpPwrUpsTopOffline,
       "lgpPwrUpsTopLineInteractive": lgpPwrUpsTopLineInteractive,
       "lgpPwrUPSTopDualInput": lgpPwrUPSTopDualInput,
       "lgpPwrTopFrequencyConverter": lgpPwrTopFrequencyConverter,
       "lgpPwrTopVoltageConverter": lgpPwrTopVoltageConverter,
       "lgpPwrTopMaximumFrameCapacity": lgpPwrTopMaximumFrameCapacity,
       "lgpPwrTopRedundantControlModules": lgpPwrTopRedundantControlModules,
       "lgpPwrInputIsolationTransformerInstalled": lgpPwrInputIsolationTransformerInstalled,
       "lgpPwrStateStaticSwitchType": lgpPwrStateStaticSwitchType,
       "lgpPwrStateModuleType": lgpPwrStateModuleType,
       "lgpPwrStateBypassInputConfig": lgpPwrStateBypassInputConfig,
       "lgpPwrStateOutputConfig": lgpPwrStateOutputConfig,
       "lgpPwrRectifierPassiveFilterInstalled": lgpPwrRectifierPassiveFilterInstalled,
       "lgpPwrRectifierTrapInstalled": lgpPwrRectifierTrapInstalled,
       "lgpPwrRectifierActiveFilterInstalled": lgpPwrRectifierActiveFilterInstalled,
       "lgpPwrStatistic": lgpPwrStatistic,
       "lgpPwrBrownOutCount": lgpPwrBrownOutCount,
       "lgpPwrBlackOutCount": lgpPwrBlackOutCount,
       "lgpPwrTransientCount": lgpPwrTransientCount,
       "lgpPwrBatteryDischargeCount": lgpPwrBatteryDischargeCount,
       "lgpPwrBatteryDischargeTime": lgpPwrBatteryDischargeTime,
       "lgpPwrBatteryAmpHours": lgpPwrBatteryAmpHours,
       "lgpPwrBatteryWattHours": lgpPwrBatteryWattHours,
       "lgpPwrBatteryStatisticsReset": lgpPwrBatteryStatisticsReset,
       "lgpPwrStatisticsReset": lgpPwrStatisticsReset,
       "lgpPwrConfig": lgpPwrConfig,
       "lgpPwrSysCapacity": lgpPwrSysCapacity,
       "lgpPwrUPSModuleMode": lgpPwrUPSModuleMode,
       "lgpPwrMaxRatedCurrent": lgpPwrMaxRatedCurrent,
       "lgpPwrRectifierPulseCount": lgpPwrRectifierPulseCount,
       "lgpController": lgpController,
       "lgpCtrlNumberInstalledControlModules": lgpCtrlNumberInstalledControlModules,
       "lgpCtrlNumberFailedControlModules": lgpCtrlNumberFailedControlModules,
       "lgpCtrlNumberRedundantControlModules": lgpCtrlNumberRedundantControlModules,
       "lgpCtrlNumberControlModuleWarnings": lgpCtrlNumberControlModuleWarnings,
       "lgpCtrlBoardBatteryVoltage": lgpCtrlBoardBatteryVoltage,
       "lgpSystem": lgpSystem,
       "lgpSysStatistics": lgpSysStatistics,
       "lgpSysStatisticsRunHrs": lgpSysStatisticsRunHrs,
       "lgpSysStatus": lgpSysStatus,
       "lgpSysSelfTestResult": lgpSysSelfTestResult,
       "lgpSysState": lgpSysState,
       "lgpSysSettings": lgpSysSettings,
       "lgpSysAudibleAlarm": lgpSysAudibleAlarm,
       "lgpSysControl": lgpSysControl,
       "lgpSysSelfTest": lgpSysSelfTest,
       "lgpSysControlOperationOnOff": lgpSysControlOperationOnOff,
       "lgpSysTime": lgpSysTime,
       "lgpSysTimeEpoch": lgpSysTimeEpoch,
       "lgpSysMaintenance": lgpSysMaintenance,
       "lgpSysMaintenanceCapacity": lgpSysMaintenanceCapacity,
       "lgpSysMaintenanceYear": lgpSysMaintenanceYear,
       "lgpSysMaintenanceMonth": lgpSysMaintenanceMonth,
       "lgpSysEventDescription": lgpSysEventDescription,
       "lgpSysEventNotifications": lgpSysEventNotifications,
       "lgpSysNotification": lgpSysNotification,
       "lgpSysNormal": lgpSysNormal,
       "lgpSysDeviceComponentGroup": lgpSysDeviceComponentGroup,
       "lgpSysDeviceComponentTable": lgpSysDeviceComponentTable,
       "lgpSysDeviceComponentEntry": lgpSysDeviceComponentEntry,
       "lgpSysDeviceComponentIndex": lgpSysDeviceComponentIndex,
       "lgpSysDeviceComponentDescr": lgpSysDeviceComponentDescr,
       "lgpSysDeviceComponentSerialNum": lgpSysDeviceComponentSerialNum,
       "lgpSysDeviceComponentModelNum": lgpSysDeviceComponentModelNum,
       "lgpSysDeviceComponentWellknown": lgpSysDeviceComponentWellknown,
       "lgpSysDeviceBatCabinet": lgpSysDeviceBatCabinet,
       "lgpSysDeviceParallelCabinet": lgpSysDeviceParallelCabinet,
       "lgpSysDeviceMaintBypass": lgpSysDeviceMaintBypass,
       "lgpPdu": lgpPdu,
       "lgpPduCluster": lgpPduCluster,
       "lgpPduGrpSysStatus": lgpPduGrpSysStatus,
       "lgpPduTableCount": lgpPduTableCount,
       "lgpPduTable": lgpPduTable,
       "lgpPduEntry": lgpPduEntry,
       "lgpPduEntryIndex": lgpPduEntryIndex,
       "lgpPduEntryId": lgpPduEntryId,
       "lgpPduEntryUsrLabel": lgpPduEntryUsrLabel,
       "lgpPduEntrySysAssignLabel": lgpPduEntrySysAssignLabel,
       "lgpPduEntryPositionRelative": lgpPduEntryPositionRelative,
       "lgpPduEntrySysStatus": lgpPduEntrySysStatus,
       "lgpPduEntryUsrTag1": lgpPduEntryUsrTag1,
       "lgpPduEntryUsrTag2": lgpPduEntryUsrTag2,
       "lgpPduEntrySerialNumber": lgpPduEntrySerialNumber,
       "lgpPduEntryRbCount": lgpPduEntryRbCount,
       "lgpPduPowerSource": lgpPduPowerSource,
       "lgpPduPsTableCount": lgpPduPsTableCount,
       "lgpPduPsTable": lgpPduPsTable,
       "lgpPduPsEntry": lgpPduPsEntry,
       "lgpPduPsEntryIndex": lgpPduPsEntryIndex,
       "lgpPduPsEntryId": lgpPduPsEntryId,
       "lgpPduPsEntrySysAssignLabel": lgpPduPsEntrySysAssignLabel,
       "lgpPduPsEntryModel": lgpPduPsEntryModel,
       "lgpPduPsEntryWiringType": lgpPduPsEntryWiringType,
       "lgpPduPsEntryEpInputRated": lgpPduPsEntryEpInputRated,
       "lgpPduPsEntryEcInputRated": lgpPduPsEntryEcInputRated,
       "lgpPduPsEntryFreqRated": lgpPduPsEntryFreqRated,
       "lgpPduPsEntryEnergyAccum": lgpPduPsEntryEnergyAccum,
       "lgpPduPsEntrySerialNum": lgpPduPsEntrySerialNum,
       "lgpPduPsEntryFirmwareVersion": lgpPduPsEntryFirmwareVersion,
       "lgpPduPsEntryPwrTotal": lgpPduPsEntryPwrTotal,
       "lgpPduPsEntryEcNeutral": lgpPduPsEntryEcNeutral,
       "lgpPduPsEntryEcNeutralThrshldOvrWarn": lgpPduPsEntryEcNeutralThrshldOvrWarn,
       "lgpPduPsEntryEcNeutralThrshldOvrAlarm": lgpPduPsEntryEcNeutralThrshldOvrAlarm,
       "lgpPduPsLineTable": lgpPduPsLineTable,
       "lgpPduPsLineEntry": lgpPduPsLineEntry,
       "lgpPduPsLineEntryIndex": lgpPduPsLineEntryIndex,
       "lgpPduPsLineEntryId": lgpPduPsLineEntryId,
       "lgpPduPsLineEntryLine": lgpPduPsLineEntryLine,
       "lgpPduPsLineEntryEpLNTenths": lgpPduPsLineEntryEpLNTenths,
       "lgpPduPsLineEntryEpLN": lgpPduPsLineEntryEpLN,
       "lgpPduPsLineEntryEc": lgpPduPsLineEntryEc,
       "lgpPduPsLineEntryEcHundredths": lgpPduPsLineEntryEcHundredths,
       "lgpPduPsLineEntryEcThrshldUndrAlarm": lgpPduPsLineEntryEcThrshldUndrAlarm,
       "lgpPduPsLineEntryEcThrshldOvrWarn": lgpPduPsLineEntryEcThrshldOvrWarn,
       "lgpPduPsLineEntryEcThrshldOvrAlarm": lgpPduPsLineEntryEcThrshldOvrAlarm,
       "lgpPduPsLineEntryEcAvailBeforeAlarm": lgpPduPsLineEntryEcAvailBeforeAlarm,
       "lgpPduPsLineEntryEcUsedBeforeAlarm": lgpPduPsLineEntryEcUsedBeforeAlarm,
       "lgpPduPsLineEntryEpLL": lgpPduPsLineEntryEpLL,
       "lgpPduPsLineEntryEpLLTenths": lgpPduPsLineEntryEpLLTenths,
       "lgpPduPsLineEntryEcAvailBeforeAlarmHundredths": lgpPduPsLineEntryEcAvailBeforeAlarmHundredths,
       "lgpPduReceptacleBranch": lgpPduReceptacleBranch,
       "lgpPduRbTableCount": lgpPduRbTableCount,
       "lgpPduRbTable": lgpPduRbTable,
       "lgpPduRbEntry": lgpPduRbEntry,
       "lgpPduRbEntryIndex": lgpPduRbEntryIndex,
       "lgpPduRbEntryId": lgpPduRbEntryId,
       "lgpPduRbEntryUsrLabel": lgpPduRbEntryUsrLabel,
       "lgpPduRbEntrySysAssignLabel": lgpPduRbEntrySysAssignLabel,
       "lgpPduRbEntryPositionRelative": lgpPduRbEntryPositionRelative,
       "lgpPduRbEntrySerialNum": lgpPduRbEntrySerialNum,
       "lgpPduRbEntryModel": lgpPduRbEntryModel,
       "lgpPduRbEntryFirmwareVersion": lgpPduRbEntryFirmwareVersion,
       "lgpPduRbEntryUsrTag1": lgpPduRbEntryUsrTag1,
       "lgpPduRbEntryUsrTag2": lgpPduRbEntryUsrTag2,
       "lgpPduRbEntryReceptacleType": lgpPduRbEntryReceptacleType,
       "lgpPduRbEntryCapabilities": lgpPduRbEntryCapabilities,
       "lgpPduRbEntryLineSource": lgpPduRbEntryLineSource,
       "lgpPduRbEntryRcpCount": lgpPduRbEntryRcpCount,
       "lgpPduRbEntryEpRated": lgpPduRbEntryEpRated,
       "lgpPduRbEntryEcRated": lgpPduRbEntryEcRated,
       "lgpPduRbEntryFreqRated": lgpPduRbEntryFreqRated,
       "lgpPduRbEntryEnergyAccum": lgpPduRbEntryEnergyAccum,
       "lgpPduRbEntryEpLNTenths": lgpPduRbEntryEpLNTenths,
       "lgpPduRbEntryPwr": lgpPduRbEntryPwr,
       "lgpPduRbEntryAp": lgpPduRbEntryAp,
       "lgpPduRbEntryPf": lgpPduRbEntryPf,
       "lgpPduRbEntryEcHundredths": lgpPduRbEntryEcHundredths,
       "lgpPduRbEntryEcThrshldUndrAlm": lgpPduRbEntryEcThrshldUndrAlm,
       "lgpPduRbEntryEcThrshldOvrWarn": lgpPduRbEntryEcThrshldOvrWarn,
       "lgpPduRbEntryEcThrshldOvrAlm": lgpPduRbEntryEcThrshldOvrAlm,
       "lgpPduRbEntryEcAvailBeforeAlarmHundredths": lgpPduRbEntryEcAvailBeforeAlarmHundredths,
       "lgpPduRbEntryEcUsedBeforeAlarm": lgpPduRbEntryEcUsedBeforeAlarm,
       "lgpPduRbEntryEpLLTenths": lgpPduRbEntryEpLLTenths,
       "lgpPduRbLineTable": lgpPduRbLineTable,
       "lgpPduRbLineEntry": lgpPduRbLineEntry,
       "lgpPduRbLineEntryIndex": lgpPduRbLineEntryIndex,
       "lgpPduRbLineEntryId": lgpPduRbLineEntryId,
       "lgpPduRbLineEntryLine": lgpPduRbLineEntryLine,
       "lgpPduRbLineEntryEpLNTenths": lgpPduRbLineEntryEpLNTenths,
       "lgpPduRbLineEntryEpLN": lgpPduRbLineEntryEpLN,
       "lgpPduRbLineEntryEc": lgpPduRbLineEntryEc,
       "lgpPduRbLineEntryPwr": lgpPduRbLineEntryPwr,
       "lgpPduRbLineEntryAp": lgpPduRbLineEntryAp,
       "lgpPduRbLineEntryPf": lgpPduRbLineEntryPf,
       "lgpPduRbLineEntryEcHundredths": lgpPduRbLineEntryEcHundredths,
       "lgpPduRbLineEntryEcThrshldUndrAlm": lgpPduRbLineEntryEcThrshldUndrAlm,
       "lgpPduRbLineEntryEcThrshldOvrWarn": lgpPduRbLineEntryEcThrshldOvrWarn,
       "lgpPduRbLineEntryEcThrshldOvrAlm": lgpPduRbLineEntryEcThrshldOvrAlm,
       "lgpPduRbLineEntryEcAvailBeforeAlarmHundredths": lgpPduRbLineEntryEcAvailBeforeAlarmHundredths,
       "lgpPduRbLineEntryEcAvailBeforeAlarm": lgpPduRbLineEntryEcAvailBeforeAlarm,
       "lgpPduRbLineEntryEcUsedBeforeAlarm": lgpPduRbLineEntryEcUsedBeforeAlarm,
       "lgpPduRbLineEntryEpLL": lgpPduRbLineEntryEpLL,
       "lgpPduRbLineEntryEpLLTenths": lgpPduRbLineEntryEpLLTenths,
       "lgpPduReceptacle": lgpPduReceptacle,
       "lgpPduRcpTableCount": lgpPduRcpTableCount,
       "lgpPduRcpTable": lgpPduRcpTable,
       "lgpPduRcpEntry": lgpPduRcpEntry,
       "lgpPduRcpEntryIndex": lgpPduRcpEntryIndex,
       "lgpPduRcpEntryId": lgpPduRcpEntryId,
       "lgpPduRcpEntryUsrLabel": lgpPduRcpEntryUsrLabel,
       "lgpPduRcpEntryUsrTag1": lgpPduRcpEntryUsrTag1,
       "lgpPduRcpEntryUsrTag2": lgpPduRcpEntryUsrTag2,
       "lgpPduRcpEntrySysAssignLabel": lgpPduRcpEntrySysAssignLabel,
       "lgpPduRcpEntryPosition": lgpPduRcpEntryPosition,
       "lgpPduRcpEntryType": lgpPduRcpEntryType,
       "lgpPduRcpEntryLineSource": lgpPduRcpEntryLineSource,
       "lgpPduRcpEntryCapabilities": lgpPduRcpEntryCapabilities,
       "lgpPduRcpEntryEp": lgpPduRcpEntryEp,
       "lgpPduRcpEntryEpTenths": lgpPduRcpEntryEpTenths,
       "lgpPduRcpEntryEc": lgpPduRcpEntryEc,
       "lgpPduRcpEntryEcHundredths": lgpPduRcpEntryEcHundredths,
       "lgpPduRcpEntryPwrOut": lgpPduRcpEntryPwrOut,
       "lgpPduRcpEntryApOut": lgpPduRcpEntryApOut,
       "lgpPduRcpEntryPf": lgpPduRcpEntryPf,
       "lgpPduRcpEntryFreq": lgpPduRcpEntryFreq,
       "lgpPduRcpEntryEnergyAccum": lgpPduRcpEntryEnergyAccum,
       "lgpPduRcpEntryPwrOnDelay": lgpPduRcpEntryPwrOnDelay,
       "lgpPduRcpEntryPwrState": lgpPduRcpEntryPwrState,
       "lgpPduRcpEntryControl": lgpPduRcpEntryControl,
       "lgpPduRcpEntryControlLock": lgpPduRcpEntryControlLock,
       "lgpPduRcpEntryEcThrshldUnderAlarm": lgpPduRcpEntryEcThrshldUnderAlarm,
       "lgpPduRcpEntryEcThrshldOverWarn": lgpPduRcpEntryEcThrshldOverWarn,
       "lgpPduRcpEntryEcThrshldOverAlarm": lgpPduRcpEntryEcThrshldOverAlarm,
       "lgpPduRcpEntryEcAvailBeforeAlarmHundredths": lgpPduRcpEntryEcAvailBeforeAlarmHundredths,
       "lgpPduRcpEntryEcAvailBeforeAlarm": lgpPduRcpEntryEcAvailBeforeAlarm,
       "lgpPduRcpEntryEcUsedBeforeAlarm": lgpPduRcpEntryEcUsedBeforeAlarm,
       "lgpPduRcpEntryEcCrestFactor": lgpPduRcpEntryEcCrestFactor,
       "lgpPduRcpEntryBlinkLED": lgpPduRcpEntryBlinkLED,
       "lgpPduAuxiliarySensors": lgpPduAuxiliarySensors,
       "lgpPduAuxSensorCount": lgpPduAuxSensorCount,
       "lgpPduAuxSensorTable": lgpPduAuxSensorTable,
       "lgpPduAuxSensorEntry": lgpPduAuxSensorEntry,
       "lgpPduAuxSensorIndex": lgpPduAuxSensorIndex,
       "lgpPduAuxSensorMeasType": lgpPduAuxSensorMeasType,
       "lgpPduAuxSensorId": lgpPduAuxSensorId,
       "lgpPduAuxSensorSysAssignLabel": lgpPduAuxSensorSysAssignLabel,
       "lgpPduAuxSensorPositionRelative": lgpPduAuxSensorPositionRelative,
       "lgpPduAuxSensorUsrLabel": lgpPduAuxSensorUsrLabel,
       "lgpPduAuxSensorUsrTag1": lgpPduAuxSensorUsrTag1,
       "lgpPduAuxSensorUsrTag2": lgpPduAuxSensorUsrTag2,
       "lgpPduAuxSensorTempSerialNum": lgpPduAuxSensorTempSerialNum,
       "lgpPduAuxSensorHumSerialNum": lgpPduAuxSensorHumSerialNum,
       "lgpPduAuxSensorTempMeasurementDegF": lgpPduAuxSensorTempMeasurementDegF,
       "lgpPduAuxSensorTempThrshldUndrAlmDegF": lgpPduAuxSensorTempThrshldUndrAlmDegF,
       "lgpPduAuxSensorTempThrshldOvrAlmDegF": lgpPduAuxSensorTempThrshldOvrAlmDegF,
       "lgpPduAuxSensorTempThrshldUndrWarnDegF": lgpPduAuxSensorTempThrshldUndrWarnDegF,
       "lgpPduAuxSensorTempThrshldOvrWarnDegF": lgpPduAuxSensorTempThrshldOvrWarnDegF,
       "lgpPduAuxSensorTempMeasurementDegC": lgpPduAuxSensorTempMeasurementDegC,
       "lgpPduAuxSensorTempThrshldUndrAlmDegC": lgpPduAuxSensorTempThrshldUndrAlmDegC,
       "lgpPduAuxSensorTempThrshldOvrAlmDegC": lgpPduAuxSensorTempThrshldOvrAlmDegC,
       "lgpPduAuxSensorTempThrshldUndrWarnDegC": lgpPduAuxSensorTempThrshldUndrWarnDegC,
       "lgpPduAuxSensorTempThrshldOvrWarnDegC": lgpPduAuxSensorTempThrshldOvrWarnDegC,
       "lgpPduAuxSensorHumMeasurement": lgpPduAuxSensorHumMeasurement,
       "lgpPduAuxSensorHumThrshldUndrAlm": lgpPduAuxSensorHumThrshldUndrAlm,
       "lgpPduAuxSensorHumThrshldOvrAlm": lgpPduAuxSensorHumThrshldOvrAlm,
       "lgpPduAuxSensorHumThrshldUndrWarn": lgpPduAuxSensorHumThrshldUndrWarn,
       "lgpPduAuxSensorHumThrshldOvrWarn": lgpPduAuxSensorHumThrshldOvrWarn,
       "lgpPduAuxMeasTable": lgpPduAuxMeasTable,
       "lgpPduAuxMeasEntry": lgpPduAuxMeasEntry,
       "lgpPduAuxMeasSensorIndex": lgpPduAuxMeasSensorIndex,
       "lgpPduAuxMeasSensorMeasurementIndex": lgpPduAuxMeasSensorMeasurementIndex,
       "lgpPduAuxMeasType": lgpPduAuxMeasType,
       "lgpPduAuxMeasSensorSysAssignLabel": lgpPduAuxMeasSensorSysAssignLabel,
       "lgpPduAuxMeasUsrLabel": lgpPduAuxMeasUsrLabel,
       "lgpPduAuxMeasUsrTag1": lgpPduAuxMeasUsrTag1,
       "lgpPduAuxMeasUsrTag2": lgpPduAuxMeasUsrTag2,
       "lgpPduAuxMeasSensorSerialNum": lgpPduAuxMeasSensorSerialNum,
       "lgpPduAuxMeasTempDegF": lgpPduAuxMeasTempDegF,
       "lgpPduAuxMeasTempThrshldUndrAlmDegF": lgpPduAuxMeasTempThrshldUndrAlmDegF,
       "lgpPduAuxMeasTempThrshldOvrAlmDegF": lgpPduAuxMeasTempThrshldOvrAlmDegF,
       "lgpPduAuxMeasTempThrshldUndrWarnDegF": lgpPduAuxMeasTempThrshldUndrWarnDegF,
       "lgpPduAuxMeasTempThrshldOvrWarnDegF": lgpPduAuxMeasTempThrshldOvrWarnDegF,
       "lgpPduAuxMeasTempDegC": lgpPduAuxMeasTempDegC,
       "lgpPduAuxMeasTempThrshldUndrAlmDegC": lgpPduAuxMeasTempThrshldUndrAlmDegC,
       "lgpPduAuxMeasTempThrshldOvrAlmDegC": lgpPduAuxMeasTempThrshldOvrAlmDegC,
       "lgpPduAuxMeasTempThrshldUndrWarnDegC": lgpPduAuxMeasTempThrshldUndrWarnDegC,
       "lgpPduAuxMeasTempThrshldOvrWarnDegC": lgpPduAuxMeasTempThrshldOvrWarnDegC,
       "lgpPduAuxMeasHum": lgpPduAuxMeasHum,
       "lgpPduAuxMeasHumThrshldUndrAlm": lgpPduAuxMeasHumThrshldUndrAlm,
       "lgpPduAuxMeasHumThrshldOvrAlm": lgpPduAuxMeasHumThrshldOvrAlm,
       "lgpPduAuxMeasHumThrshldUndrWarn": lgpPduAuxMeasHumThrshldUndrWarn,
       "lgpPduAuxMeasHumThrshldOvrWarn": lgpPduAuxMeasHumThrshldOvrWarn,
       "lgpPduAuxMeasDrClosureState": lgpPduAuxMeasDrClosureState,
       "lgpPduAuxMeasDrClosureConfig": lgpPduAuxMeasDrClosureConfig,
       "lgpPduAuxMeasCntctClosureState": lgpPduAuxMeasCntctClosureState,
       "lgpPduAuxMeasCntctClosureConfig": lgpPduAuxMeasCntctClosureConfig,
       "lgpFlexible": lgpFlexible,
       "lgpFlexibleTableCount": lgpFlexibleTableCount,
       "lgpFlexibleBasicTable": lgpFlexibleBasicTable,
       "lgpFlexibleBasicEntry": lgpFlexibleBasicEntry,
       "lgpFlexibleEntryIndex": lgpFlexibleEntryIndex,
       "lgpFlexibleEntryDataLabel": lgpFlexibleEntryDataLabel,
       "lgpFlexibleEntryValue": lgpFlexibleEntryValue,
       "lgpFlexibleEntryUnitsOfMeasure": lgpFlexibleEntryUnitsOfMeasure,
       "lgpFlexibleExtendedTable": lgpFlexibleExtendedTable,
       "lgpFlexibleExtendedEntry": lgpFlexibleExtendedEntry,
       "lgpFlexibleEntryIntegerValue": lgpFlexibleEntryIntegerValue,
       "lgpFlexibleEntryUnsignedIntegerValue": lgpFlexibleEntryUnsignedIntegerValue,
       "lgpFlexibleEntryDecimalPosition": lgpFlexibleEntryDecimalPosition,
       "lgpFlexibleEntryDataType": lgpFlexibleEntryDataType,
       "lgpFlexibleEntryAccessibility": lgpFlexibleEntryAccessibility,
       "lgpFlexibleEntryUnitsOfMeasureEnum": lgpFlexibleEntryUnitsOfMeasureEnum,
       "lgpFlexibleEntryDataDescription": lgpFlexibleEntryDataDescription,
       "lgpProductSpecific": lgpProductSpecific,
       "lgpUpsProducts": lgpUpsProducts,
       "lgpSeries7200": lgpSeries7200,
       "lgpUPStationGXT": lgpUPStationGXT,
       "lgpPowerSureInteractive": lgpPowerSureInteractive,
       "lgpNfinity": lgpNfinity,
       "lgpNpower": lgpNpower,
       "lgpGXT2Dual": lgpGXT2Dual,
       "lgpPowerSureInteractive2": lgpPowerSureInteractive2,
       "lgpNX": lgpNX,
       "lgpHiNet": lgpHiNet,
       "lgpNXL": lgpNXL,
       "lgpSuper400": lgpSuper400,
       "lgpSeries600or610": lgpSeries600or610,
       "lgpSeries300": lgpSeries300,
       "lgpSeries610SMS": lgpSeries610SMS,
       "lgpSeries610MMU": lgpSeries610MMU,
       "lgpSeries610SCC": lgpSeries610SCC,
       "lgpNXr": lgpNXr,
       "lgpAcProducts": lgpAcProducts,
       "lgpAdvancedMicroprocessor": lgpAdvancedMicroprocessor,
       "lgpStandardMicroprocessor": lgpStandardMicroprocessor,
       "lgpMiniMate2": lgpMiniMate2,
       "lgpHimod": lgpHimod,
       "lgpCEMS100orLECS15": lgpCEMS100orLECS15,
       "lgpIcom": lgpIcom,
       "lgpIcomPA": lgpIcomPA,
       "lgpIcomPAtypeDS": lgpIcomPAtypeDS,
       "lgpIcomPAtypeHPM": lgpIcomPAtypeHPM,
       "lgpIcomPAtypeChallenger": lgpIcomPAtypeChallenger,
       "lgpIcomPAtypePeX": lgpIcomPAtypePeX,
       "lgpIcomPAtypeDeluxeSys3": lgpIcomPAtypeDeluxeSys3,
       "lgpIcomPAtypeJumboCW": lgpIcomPAtypeJumboCW,
       "lgpIcomXD": lgpIcomXD,
       "lgpIcomXDtypeXDF": lgpIcomXDtypeXDF,
       "lgpIcomXDtypeXDFN": lgpIcomXDtypeXDFN,
       "lgpIcomXP": lgpIcomXP,
       "lgpIcomXPtypeXDP": lgpIcomXPtypeXDP,
       "lgpIcomXPtypeXDPCray": lgpIcomXPtypeXDPCray,
       "lgpIcomXPtypeXDC": lgpIcomXPtypeXDC,
       "lgpIcomXPtypeXDPW": lgpIcomXPtypeXDPW,
       "lgpIcomSC": lgpIcomSC,
       "lgpIcomSCtypeHPC": lgpIcomSCtypeHPC,
       "lgpIcomSCtypeHPCSSmall": lgpIcomSCtypeHPCSSmall,
       "lgpIcomSCtypeHPCSLarge": lgpIcomSCtypeHPCSLarge,
       "lgpIcomSCtypeHPCR": lgpIcomSCtypeHPCR,
       "lgpIcomSCtypeHPCM": lgpIcomSCtypeHPCM,
       "lgpIcomSCtypeHPCL": lgpIcomSCtypeHPCL,
       "lgpIcomSCtypeHPCW": lgpIcomSCtypeHPCW,
       "lgpIcomCR": lgpIcomCR,
       "lgpIcomCRtypeCRV": lgpIcomCRtypeCRV,
       "lgpPowerConditioningProducts": lgpPowerConditioningProducts,
       "lgpPMP": lgpPMP,
       "lgpEPMP": lgpEPMP,
       "lgpTransferSwitchProducts": lgpTransferSwitchProducts,
       "lgpStaticTransferSwitchEDS": lgpStaticTransferSwitchEDS,
       "lgpStaticTransferSwitch1": lgpStaticTransferSwitch1,
       "lgpStaticTransferSwitch2": lgpStaticTransferSwitch2,
       "lgpStaticTransferSwitch2FourPole": lgpStaticTransferSwitch2FourPole,
       "lgpMultiLinkProducts": lgpMultiLinkProducts,
       "lgpMultiLinkBasicNotification": lgpMultiLinkBasicNotification,
       "lgpPowerDistributionProducts": lgpPowerDistributionProducts,
       "lgpRackPDU": lgpRackPDU,
       "lgpMPX": lgpMPX,
       "lgpMPH": lgpMPH}
)
