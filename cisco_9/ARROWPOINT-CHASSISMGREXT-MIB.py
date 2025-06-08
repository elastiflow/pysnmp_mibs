# SNMP MIB module (ARROWPOINT-CHASSISMGREXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ARROWPOINT-CHASSISMGREXT-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 19:35:05 2025
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

(chassisMgrExt,) = mibBuilder.importSymbols(
    "CISCO-APENT-MIB",
    "chassisMgrExt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

_ChassisMgrExtMib_ObjectIdentity = ObjectIdentity
chassisMgrExtMib = _ChassisMgrExtMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1)
)
_ChassisMgrExtMibNotifs_ObjectIdentity = ObjectIdentity
chassisMgrExtMibNotifs = _ChassisMgrExtMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 0)
)
_ChassisMgrExtMibObjects_ObjectIdentity = ObjectIdentity
chassisMgrExtMibObjects = _ChassisMgrExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 1)
)
_ChassisMgrExtMibConform_ObjectIdentity = ObjectIdentity
chassisMgrExtMibConform = _ChassisMgrExtMibConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 2)
)
_ChassisMgrExtMibCompliances_ObjectIdentity = ObjectIdentity
chassisMgrExtMibCompliances = _ChassisMgrExtMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 2, 1)
)
_ChassisMgrExtMibCompliance_ObjectIdentity = ObjectIdentity
chassisMgrExtMibCompliance = _ChassisMgrExtMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 2, 1, 1)
)
_ChassisMgrExtMibGroups_ObjectIdentity = ObjectIdentity
chassisMgrExtMibGroups = _ChassisMgrExtMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 2, 2)
)
_ChassisMgrExtMibGroup_ObjectIdentity = ObjectIdentity
chassisMgrExtMibGroup = _ChassisMgrExtMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 2, 2, 1)
)
_ChassisMgrExtMibNotif_ObjectIdentity = ObjectIdentity
chassisMgrExtMibNotif = _ChassisMgrExtMibNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 2, 2, 2)
)


class _ApChassisMgrExtChassisType_Type(Integer32):
    """Custom type apChassisMgrExtChassisType based on Integer32"""
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
        *(("ws100", 0),
          ("ws800", 1),
          ("ws150", 2),
          ("ws50", 3),
          ("unknown", 4),
          ("css11503", 5),
          ("css11506", 6),
          ("css11501", 7))
    )


_ApChassisMgrExtChassisType_Type.__name__ = "Integer32"
_ApChassisMgrExtChassisType_Object = MibScalar
apChassisMgrExtChassisType = _ApChassisMgrExtChassisType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 2),
    _ApChassisMgrExtChassisType_Type()
)
apChassisMgrExtChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtChassisType.setStatus("mandatory")


class _ApChassisMgrExtChassisName_Type(SnmpAdminString):
    """Custom type apChassisMgrExtChassisName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApChassisMgrExtChassisName_Type.__name__ = "SnmpAdminString"
_ApChassisMgrExtChassisName_Object = MibScalar
apChassisMgrExtChassisName = _ApChassisMgrExtChassisName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 3),
    _ApChassisMgrExtChassisName_Type()
)
apChassisMgrExtChassisName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtChassisName.setStatus("mandatory")
_ApChassisMgrExtChassisSerialNumber_Type = SnmpAdminString
_ApChassisMgrExtChassisSerialNumber_Object = MibScalar
apChassisMgrExtChassisSerialNumber = _ApChassisMgrExtChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 4),
    _ApChassisMgrExtChassisSerialNumber_Type()
)
apChassisMgrExtChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtChassisSerialNumber.setStatus("mandatory")


class _ApChassisMgrExtNumberSlots_Type(Integer32):
    """Custom type apChassisMgrExtNumberSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ApChassisMgrExtNumberSlots_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberSlots_Object = MibScalar
apChassisMgrExtNumberSlots = _ApChassisMgrExtNumberSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 5),
    _ApChassisMgrExtNumberSlots_Type()
)
apChassisMgrExtNumberSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberSlots.setStatus("mandatory")


class _ApChassisMgrExtNumberModules_Type(Integer32):
    """Custom type apChassisMgrExtNumberModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_ApChassisMgrExtNumberModules_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberModules_Object = MibScalar
apChassisMgrExtNumberModules = _ApChassisMgrExtNumberModules_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 6),
    _ApChassisMgrExtNumberModules_Type()
)
apChassisMgrExtNumberModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberModules.setStatus("mandatory")


class _ApChassisMgrExtNumberPowerSupplies_Type(Integer32):
    """Custom type apChassisMgrExtNumberPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ApChassisMgrExtNumberPowerSupplies_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberPowerSupplies_Object = MibScalar
apChassisMgrExtNumberPowerSupplies = _ApChassisMgrExtNumberPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 7),
    _ApChassisMgrExtNumberPowerSupplies_Type()
)
apChassisMgrExtNumberPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberPowerSupplies.setStatus("mandatory")


class _ApChassisMgrExtNumberFans_Type(Integer32):
    """Custom type apChassisMgrExtNumberFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ApChassisMgrExtNumberFans_Type.__name__ = "Integer32"
_ApChassisMgrExtNumberFans_Object = MibScalar
apChassisMgrExtNumberFans = _ApChassisMgrExtNumberFans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 8),
    _ApChassisMgrExtNumberFans_Type()
)
apChassisMgrExtNumberFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtNumberFans.setStatus("mandatory")


class _ApChassisMgrExtSoftwareVersionNumber_Type(SnmpAdminString):
    """Custom type apChassisMgrExtSoftwareVersionNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApChassisMgrExtSoftwareVersionNumber_Type.__name__ = "SnmpAdminString"
_ApChassisMgrExtSoftwareVersionNumber_Object = MibScalar
apChassisMgrExtSoftwareVersionNumber = _ApChassisMgrExtSoftwareVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 9),
    _ApChassisMgrExtSoftwareVersionNumber_Type()
)
apChassisMgrExtSoftwareVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSoftwareVersionNumber.setStatus("mandatory")


class _ApChassisMgrExtBootpState_Type(Integer32):
    """Custom type apChassisMgrExtBootpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bootp-disabled", 0),
          ("bootp-enabled", 1))
    )


_ApChassisMgrExtBootpState_Type.__name__ = "Integer32"
_ApChassisMgrExtBootpState_Object = MibScalar
apChassisMgrExtBootpState = _ApChassisMgrExtBootpState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 10),
    _ApChassisMgrExtBootpState_Type()
)
apChassisMgrExtBootpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtBootpState.setStatus("mandatory")
_ApChassisMgrExtMgmtPortIpAddress_Type = IpAddress
_ApChassisMgrExtMgmtPortIpAddress_Object = MibScalar
apChassisMgrExtMgmtPortIpAddress = _ApChassisMgrExtMgmtPortIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 11),
    _ApChassisMgrExtMgmtPortIpAddress_Type()
)
apChassisMgrExtMgmtPortIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtMgmtPortIpAddress.setStatus("mandatory")


class _ApChassisMgrExtBaseEthernetAddress_Type(SnmpAdminString):
    """Custom type apChassisMgrExtBaseEthernetAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_ApChassisMgrExtBaseEthernetAddress_Type.__name__ = "SnmpAdminString"
_ApChassisMgrExtBaseEthernetAddress_Object = MibScalar
apChassisMgrExtBaseEthernetAddress = _ApChassisMgrExtBaseEthernetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 12),
    _ApChassisMgrExtBaseEthernetAddress_Type()
)
apChassisMgrExtBaseEthernetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtBaseEthernetAddress.setStatus("mandatory")
_ApChassisMgrExtMajorHwVersion_Type = SnmpAdminString
_ApChassisMgrExtMajorHwVersion_Object = MibScalar
apChassisMgrExtMajorHwVersion = _ApChassisMgrExtMajorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 14),
    _ApChassisMgrExtMajorHwVersion_Type()
)
apChassisMgrExtMajorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtMajorHwVersion.setStatus("mandatory")
_ApChassisMgrExtMinorHwVersion_Type = SnmpAdminString
_ApChassisMgrExtMinorHwVersion_Object = MibScalar
apChassisMgrExtMinorHwVersion = _ApChassisMgrExtMinorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 15),
    _ApChassisMgrExtMinorHwVersion_Type()
)
apChassisMgrExtMinorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtMinorHwVersion.setStatus("mandatory")
_ApChassisMgrExtModuleTable_Object = MibTable
apChassisMgrExtModuleTable = _ApChassisMgrExtModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16)
)
if mibBuilder.loadTexts:
    apChassisMgrExtModuleTable.setStatus("mandatory")
_ApChassisMgrExtModuleEntry_Object = MibTableRow
apChassisMgrExtModuleEntry = _ApChassisMgrExtModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1)
)
apChassisMgrExtModuleEntry.setIndexNames(
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtModuleSlotNumber"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtModuleEntry.setStatus("mandatory")


class _ApChassisMgrExtModuleSlotNumber_Type(Integer32):
    """Custom type apChassisMgrExtModuleSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtModuleSlotNumber_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleSlotNumber_Object = MibTableColumn
apChassisMgrExtModuleSlotNumber = _ApChassisMgrExtModuleSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 2),
    _ApChassisMgrExtModuleSlotNumber_Type()
)
apChassisMgrExtModuleSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleSlotNumber.setStatus("mandatory")


class _ApChassisMgrExtModuleType_Type(Integer32):
    """Custom type apChassisMgrExtModuleType based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("scm-1g", 0),
          ("sfm", 1),
          ("scfm", 2),
          ("fem-t1", 3),
          ("dual-hssi", 4),
          ("fem", 5),
          ("fenic", 6),
          ("genic", 7),
          ("gem", 8),
          ("hdfem", 9),
          ("unknown", 10),
          ("iom", 11),
          ("scm", 12),
          ("fc", 13),
          ("ssl", 14))
    )


_ApChassisMgrExtModuleType_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleType_Object = MibTableColumn
apChassisMgrExtModuleType = _ApChassisMgrExtModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 3),
    _ApChassisMgrExtModuleType_Type()
)
apChassisMgrExtModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleType.setStatus("mandatory")
_ApChassisMgrExtModuleName_Type = SnmpAdminString
_ApChassisMgrExtModuleName_Object = MibTableColumn
apChassisMgrExtModuleName = _ApChassisMgrExtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 4),
    _ApChassisMgrExtModuleName_Type()
)
apChassisMgrExtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleName.setStatus("mandatory")
_ApChassisMgrExtModuleSerialNumber_Type = SnmpAdminString
_ApChassisMgrExtModuleSerialNumber_Object = MibTableColumn
apChassisMgrExtModuleSerialNumber = _ApChassisMgrExtModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 5),
    _ApChassisMgrExtModuleSerialNumber_Type()
)
apChassisMgrExtModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleSerialNumber.setStatus("mandatory")


class _ApChassisMgrExtModuleOpStatus_Type(Integer32):
    """Custom type apChassisMgrExtModuleOpStatus based on Integer32"""
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
        *(("powered-off", 0),
          ("powered-on", 1),
          ("primary", 2),
          ("backup", 3),
          ("bad", 4),
          ("unknown", 5))
    )


_ApChassisMgrExtModuleOpStatus_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleOpStatus_Object = MibTableColumn
apChassisMgrExtModuleOpStatus = _ApChassisMgrExtModuleOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 6),
    _ApChassisMgrExtModuleOpStatus_Type()
)
apChassisMgrExtModuleOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleOpStatus.setStatus("mandatory")


class _ApChassisMgrExtModuleNumSubModules_Type(Integer32):
    """Custom type apChassisMgrExtModuleNumSubModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ApChassisMgrExtModuleNumSubModules_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleNumSubModules_Object = MibTableColumn
apChassisMgrExtModuleNumSubModules = _ApChassisMgrExtModuleNumSubModules_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 7),
    _ApChassisMgrExtModuleNumSubModules_Type()
)
apChassisMgrExtModuleNumSubModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleNumSubModules.setStatus("mandatory")
_ApChassisMgrExtModuleMajorHwVersion_Type = SnmpAdminString
_ApChassisMgrExtModuleMajorHwVersion_Object = MibTableColumn
apChassisMgrExtModuleMajorHwVersion = _ApChassisMgrExtModuleMajorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 8),
    _ApChassisMgrExtModuleMajorHwVersion_Type()
)
apChassisMgrExtModuleMajorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleMajorHwVersion.setStatus("mandatory")
_ApChassisMgrExtModuleMinorHwVersion_Type = SnmpAdminString
_ApChassisMgrExtModuleMinorHwVersion_Object = MibTableColumn
apChassisMgrExtModuleMinorHwVersion = _ApChassisMgrExtModuleMinorHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 9),
    _ApChassisMgrExtModuleMinorHwVersion_Type()
)
apChassisMgrExtModuleMinorHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleMinorHwVersion.setStatus("mandatory")


class _ApChassisMgrExtModuleSubType_Type(Integer32):
    """Custom type apChassisMgrExtModuleSubType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("fem-tx", 0),
          ("fem-fx", 1),
          ("sfm", 2),
          ("sfm2", 3),
          ("scfm", 4),
          ("scfm-plus", 5),
          ("fenic-tx", 6),
          ("fenic-fx", 7),
          ("genic", 8),
          ("gem", 9),
          ("hdfem", 10),
          ("scm-1g", 11),
          ("hssi", 12),
          ("fem-t1", 13),
          ("unknown", 14),
          ("iom-16port", 15),
          ("iom-session", 16),
          ("iom-8port", 17),
          ("scm", 18),
          ("scm-session", 19),
          ("scm-2gig-iom", 20),
          ("prc", 21),
          ("ssl", 22),
          ("scm-fe-ge", 23))
    )


_ApChassisMgrExtModuleSubType_Type.__name__ = "Integer32"
_ApChassisMgrExtModuleSubType_Object = MibTableColumn
apChassisMgrExtModuleSubType = _ApChassisMgrExtModuleSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 16, 1, 10),
    _ApChassisMgrExtModuleSubType_Type()
)
apChassisMgrExtModuleSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtModuleSubType.setStatus("mandatory")
_ApChassisMgrExtSubModuleTable_Object = MibTable
apChassisMgrExtSubModuleTable = _ApChassisMgrExtSubModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17)
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleTable.setStatus("mandatory")
_ApChassisMgrExtSubModuleEntry_Object = MibTableRow
apChassisMgrExtSubModuleEntry = _ApChassisMgrExtSubModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1)
)
apChassisMgrExtSubModuleEntry.setIndexNames(
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleSlot"),
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleSubSlot"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleEntry.setStatus("mandatory")


class _ApChassisMgrExtSubModuleSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtSubModuleSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSlot_Object = MibTableColumn
apChassisMgrExtSubModuleSlot = _ApChassisMgrExtSubModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 1),
    _ApChassisMgrExtSubModuleSlot_Type()
)
apChassisMgrExtSubModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSlot.setStatus("mandatory")


class _ApChassisMgrExtSubModuleSubSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ApChassisMgrExtSubModuleSubSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSubSlot_Object = MibTableColumn
apChassisMgrExtSubModuleSubSlot = _ApChassisMgrExtSubModuleSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 2),
    _ApChassisMgrExtSubModuleSubSlot_Type()
)
apChassisMgrExtSubModuleSubSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSubSlot.setStatus("mandatory")


class _ApChassisMgrExtSubModuleType_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("scm-submodule", 0),
          ("sfm-submodule", 1),
          ("scfm-submodule", 2),
          ("t1-submodule", 3),
          ("hssi-submodule", 4),
          ("epif-submodule", 5),
          ("v35-submodule", 6),
          ("xpif-submodule", 7),
          ("sfm2-submodule", 8),
          ("scfm2-submodule", 9),
          ("genic-2port-submodule", 10),
          ("genic-1port-submodule", 11),
          ("hdfem-submodule", 12),
          ("unknown-submodule", 13),
          ("mallomar-submodule", 14),
          ("spritz-submodule", 15),
          ("fc-submodule", 16),
          ("fortune-submodule", 17),
          ("g2iom-submodule", 18),
          ("session-submodule", 19),
          ("nilla-submodule", 20))
    )


_ApChassisMgrExtSubModuleType_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleType_Object = MibTableColumn
apChassisMgrExtSubModuleType = _ApChassisMgrExtSubModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 3),
    _ApChassisMgrExtSubModuleType_Type()
)
apChassisMgrExtSubModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleType.setStatus("mandatory")


class _ApChassisMgrExtSubModuleName_Type(SnmpAdminString):
    """Custom type apChassisMgrExtSubModuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ApChassisMgrExtSubModuleName_Type.__name__ = "SnmpAdminString"
_ApChassisMgrExtSubModuleName_Object = MibTableColumn
apChassisMgrExtSubModuleName = _ApChassisMgrExtSubModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 4),
    _ApChassisMgrExtSubModuleName_Type()
)
apChassisMgrExtSubModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleName.setStatus("mandatory")


class _ApChassisMgrExtSubModuleOpStatus_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleOpStatus based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("offline-ok", 0),
          ("offline-bad", 1),
          ("online", 2),
          ("bad", 3),
          ("going-online", 4),
          ("going-offline", 5),
          ("inserted", 6),
          ("post", 7),
          ("post-ok", 8),
          ("post-fail", 9),
          ("post-bad-comm", 10),
          ("flash-upgrade", 11),
          ("flash-upgrade-cmplt", 12),
          ("any", 13),
          ("unknown-state", 14))
    )


_ApChassisMgrExtSubModuleOpStatus_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleOpStatus_Object = MibTableColumn
apChassisMgrExtSubModuleOpStatus = _ApChassisMgrExtSubModuleOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 5),
    _ApChassisMgrExtSubModuleOpStatus_Type()
)
apChassisMgrExtSubModuleOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleOpStatus.setStatus("mandatory")


class _ApChassisMgrExtSubModuleSystemHeapFree_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSystemHeapFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleSystemHeapFree_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSystemHeapFree_Object = MibTableColumn
apChassisMgrExtSubModuleSystemHeapFree = _ApChassisMgrExtSubModuleSystemHeapFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 10),
    _ApChassisMgrExtSubModuleSystemHeapFree_Type()
)
apChassisMgrExtSubModuleSystemHeapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSystemHeapFree.setStatus("mandatory")


class _ApChassisMgrExtSubModuleSystemHeapChainDepth_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSystemHeapChainDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleSystemHeapChainDepth_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSystemHeapChainDepth_Object = MibTableColumn
apChassisMgrExtSubModuleSystemHeapChainDepth = _ApChassisMgrExtSubModuleSystemHeapChainDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 11),
    _ApChassisMgrExtSubModuleSystemHeapChainDepth_Type()
)
apChassisMgrExtSubModuleSystemHeapChainDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSystemHeapChainDepth.setStatus("mandatory")


class _ApChassisMgrExtSubModuleInstalledMemory_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleInstalledMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleInstalledMemory_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleInstalledMemory_Object = MibTableColumn
apChassisMgrExtSubModuleInstalledMemory = _ApChassisMgrExtSubModuleInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 12),
    _ApChassisMgrExtSubModuleInstalledMemory_Type()
)
apChassisMgrExtSubModuleInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleInstalledMemory.setStatus("mandatory")


class _ApChassisMgrExtSubModuleCPUInstantaneous_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleCPUInstantaneous based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApChassisMgrExtSubModuleCPUInstantaneous_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleCPUInstantaneous_Object = MibTableColumn
apChassisMgrExtSubModuleCPUInstantaneous = _ApChassisMgrExtSubModuleCPUInstantaneous_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 13),
    _ApChassisMgrExtSubModuleCPUInstantaneous_Type()
)
apChassisMgrExtSubModuleCPUInstantaneous.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleCPUInstantaneous.setStatus("mandatory")


class _ApChassisMgrExtSubModuleCPUAverage_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleCPUAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApChassisMgrExtSubModuleCPUAverage_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleCPUAverage_Object = MibTableColumn
apChassisMgrExtSubModuleCPUAverage = _ApChassisMgrExtSubModuleCPUAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 14),
    _ApChassisMgrExtSubModuleCPUAverage_Type()
)
apChassisMgrExtSubModuleCPUAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleCPUAverage.setStatus("mandatory")


class _ApChassisMgrExtSubModuleCurSpWeight_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleCurSpWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleCurSpWeight_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleCurSpWeight_Object = MibTableColumn
apChassisMgrExtSubModuleCurSpWeight = _ApChassisMgrExtSubModuleCurSpWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 15),
    _ApChassisMgrExtSubModuleCurSpWeight_Type()
)
apChassisMgrExtSubModuleCurSpWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleCurSpWeight.setStatus("mandatory")


class _ApChassisMgrExtSubModuleCurSpPower_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleCurSpPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApChassisMgrExtSubModuleCurSpPower_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleCurSpPower_Object = MibTableColumn
apChassisMgrExtSubModuleCurSpPower = _ApChassisMgrExtSubModuleCurSpPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 17, 1, 16),
    _ApChassisMgrExtSubModuleCurSpPower_Type()
)
apChassisMgrExtSubModuleCurSpPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleCurSpPower.setStatus("mandatory")
_ApChassisMgrExtSubModuleBufferTable_Object = MibTable
apChassisMgrExtSubModuleBufferTable = _ApChassisMgrExtSubModuleBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18)
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferTable.setStatus("mandatory")
_ApChassisMgrExtSubModuleBufferEntry_Object = MibTableRow
apChassisMgrExtSubModuleBufferEntry = _ApChassisMgrExtSubModuleBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1)
)
apChassisMgrExtSubModuleBufferEntry.setIndexNames(
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleBufferPool"),
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleBufferSlot"),
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleBufferSubSlot"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferEntry.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferPool_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferPool based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_ApChassisMgrExtSubModuleBufferPool_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferPool_Object = MibTableColumn
apChassisMgrExtSubModuleBufferPool = _ApChassisMgrExtSubModuleBufferPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 1),
    _ApChassisMgrExtSubModuleBufferPool_Type()
)
apChassisMgrExtSubModuleBufferPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferPool.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtSubModuleBufferSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferSlot_Object = MibTableColumn
apChassisMgrExtSubModuleBufferSlot = _ApChassisMgrExtSubModuleBufferSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 2),
    _ApChassisMgrExtSubModuleBufferSlot_Type()
)
apChassisMgrExtSubModuleBufferSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferSlot.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferSubSlot_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferSubSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ApChassisMgrExtSubModuleBufferSubSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferSubSlot_Object = MibTableColumn
apChassisMgrExtSubModuleBufferSubSlot = _ApChassisMgrExtSubModuleBufferSubSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 3),
    _ApChassisMgrExtSubModuleBufferSubSlot_Type()
)
apChassisMgrExtSubModuleBufferSubSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferSubSlot.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferSize_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleBufferSize_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferSize_Object = MibTableColumn
apChassisMgrExtSubModuleBufferSize = _ApChassisMgrExtSubModuleBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 4),
    _ApChassisMgrExtSubModuleBufferSize_Type()
)
apChassisMgrExtSubModuleBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferSize.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferCount_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleBufferCount_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferCount_Object = MibTableColumn
apChassisMgrExtSubModuleBufferCount = _ApChassisMgrExtSubModuleBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 5),
    _ApChassisMgrExtSubModuleBufferCount_Type()
)
apChassisMgrExtSubModuleBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferCount.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferAvailable_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleBufferAvailable_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferAvailable_Object = MibTableColumn
apChassisMgrExtSubModuleBufferAvailable = _ApChassisMgrExtSubModuleBufferAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 6),
    _ApChassisMgrExtSubModuleBufferAvailable_Type()
)
apChassisMgrExtSubModuleBufferAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferAvailable.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferFailures_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleBufferFailures_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferFailures_Object = MibTableColumn
apChassisMgrExtSubModuleBufferFailures = _ApChassisMgrExtSubModuleBufferFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 7),
    _ApChassisMgrExtSubModuleBufferFailures_Type()
)
apChassisMgrExtSubModuleBufferFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferFailures.setStatus("mandatory")


class _ApChassisMgrExtSubModuleBufferLowBufferCount_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleBufferLowBufferCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ApChassisMgrExtSubModuleBufferLowBufferCount_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleBufferLowBufferCount_Object = MibTableColumn
apChassisMgrExtSubModuleBufferLowBufferCount = _ApChassisMgrExtSubModuleBufferLowBufferCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 18, 1, 8),
    _ApChassisMgrExtSubModuleBufferLowBufferCount_Type()
)
apChassisMgrExtSubModuleBufferLowBufferCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleBufferLowBufferCount.setStatus("mandatory")
_ApChassisMgrExtSlotPortTable_Object = MibTable
apChassisMgrExtSlotPortTable = _ApChassisMgrExtSlotPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19)
)
if mibBuilder.loadTexts:
    apChassisMgrExtSlotPortTable.setStatus("mandatory")
_ApChassisMgrExtSlotPortEntry_Object = MibTableRow
apChassisMgrExtSlotPortEntry = _ApChassisMgrExtSlotPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19, 1)
)
apChassisMgrExtSlotPortEntry.setIndexNames(
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSlot"),
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtPort"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtSlotPortEntry.setStatus("mandatory")


class _ApChassisMgrExtSlot_Type(Integer32):
    """Custom type apChassisMgrExtSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_ApChassisMgrExtSlot_Type.__name__ = "Integer32"
_ApChassisMgrExtSlot_Object = MibTableColumn
apChassisMgrExtSlot = _ApChassisMgrExtSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19, 1, 1),
    _ApChassisMgrExtSlot_Type()
)
apChassisMgrExtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSlot.setStatus("mandatory")


class _ApChassisMgrExtPort_Type(Integer32):
    """Custom type apChassisMgrExtPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_ApChassisMgrExtPort_Type.__name__ = "Integer32"
_ApChassisMgrExtPort_Object = MibTableColumn
apChassisMgrExtPort = _ApChassisMgrExtPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19, 1, 2),
    _ApChassisMgrExtPort_Type()
)
apChassisMgrExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtPort.setStatus("mandatory")


class _ApChassisMgrExtIfIndex_Type(Integer32):
    """Custom type apChassisMgrExtIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_ApChassisMgrExtIfIndex_Type.__name__ = "Integer32"
_ApChassisMgrExtIfIndex_Object = MibTableColumn
apChassisMgrExtIfIndex = _ApChassisMgrExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19, 1, 3),
    _ApChassisMgrExtIfIndex_Type()
)
apChassisMgrExtIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtIfIndex.setStatus("mandatory")
_ApChassisMgrExtPortName_Type = SnmpAdminString
_ApChassisMgrExtPortName_Object = MibTableColumn
apChassisMgrExtPortName = _ApChassisMgrExtPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19, 1, 4),
    _ApChassisMgrExtPortName_Type()
)
apChassisMgrExtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtPortName.setStatus("mandatory")


class _ApChassisMgrExtPortOpStatus_Type(Integer32):
    """Custom type apChassisMgrExtPortOpStatus based on Integer32"""
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
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("offline-ok", 0),
          ("offline-bad", 1),
          ("online", 2),
          ("bad", 3),
          ("going-online", 4),
          ("going-offline", 5),
          ("inserted", 6),
          ("post", 7),
          ("post-ok", 8),
          ("post-fail", 9),
          ("post-bad-comm", 10),
          ("flash-upgrade", 11),
          ("flash-upgrade-cmplt", 12),
          ("any", 13),
          ("unknown-state", 14))
    )


_ApChassisMgrExtPortOpStatus_Type.__name__ = "Integer32"
_ApChassisMgrExtPortOpStatus_Object = MibTableColumn
apChassisMgrExtPortOpStatus = _ApChassisMgrExtPortOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 19, 1, 5),
    _ApChassisMgrExtPortOpStatus_Type()
)
apChassisMgrExtPortOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtPortOpStatus.setStatus("mandatory")
_ApChassisMgrExtSubModuleSpWeightTable_Object = MibTable
apChassisMgrExtSubModuleSpWeightTable = _ApChassisMgrExtSubModuleSpWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 20)
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSpWeightTable.setStatus("mandatory")
_ApChassisMgrExtSubModuleSpWeightEntry_Object = MibTableRow
apChassisMgrExtSubModuleSpWeightEntry = _ApChassisMgrExtSubModuleSpWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 20, 1)
)
apChassisMgrExtSubModuleSpWeightEntry.setIndexNames(
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleSlot"),
    (0, "ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtSubModuleSubSlot"),
)
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSpWeightEntry.setStatus("mandatory")


class _ApChassisMgrExtSubModuleSpWeight_Type(Integer32):
    """Custom type apChassisMgrExtSubModuleSpWeight based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_ApChassisMgrExtSubModuleSpWeight_Type.__name__ = "Integer32"
_ApChassisMgrExtSubModuleSpWeight_Object = MibTableColumn
apChassisMgrExtSubModuleSpWeight = _ApChassisMgrExtSubModuleSpWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 20, 1, 1),
    _ApChassisMgrExtSubModuleSpWeight_Type()
)
apChassisMgrExtSubModuleSpWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apChassisMgrExtSubModuleSpWeight.setStatus("mandatory")


class _ApChassisMgrExtSpTotalWeight_Type(Integer32):
    """Custom type apChassisMgrExtSpTotalWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApChassisMgrExtSpTotalWeight_Type.__name__ = "Integer32"
_ApChassisMgrExtSpTotalWeight_Object = MibScalar
apChassisMgrExtSpTotalWeight = _ApChassisMgrExtSpTotalWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 21),
    _ApChassisMgrExtSpTotalWeight_Type()
)
apChassisMgrExtSpTotalWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSpTotalWeight.setStatus("mandatory")


class _ApChassisMgrExtSpTotalCount_Type(Integer32):
    """Custom type apChassisMgrExtSpTotalCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApChassisMgrExtSpTotalCount_Type.__name__ = "Integer32"
_ApChassisMgrExtSpTotalCount_Object = MibScalar
apChassisMgrExtSpTotalCount = _ApChassisMgrExtSpTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 22),
    _ApChassisMgrExtSpTotalCount_Type()
)
apChassisMgrExtSpTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSpTotalCount.setStatus("mandatory")


class _ApChassisMgrExtSpActiveCount_Type(Integer32):
    """Custom type apChassisMgrExtSpActiveCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApChassisMgrExtSpActiveCount_Type.__name__ = "Integer32"
_ApChassisMgrExtSpActiveCount_Object = MibScalar
apChassisMgrExtSpActiveCount = _ApChassisMgrExtSpActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 23),
    _ApChassisMgrExtSpActiveCount_Type()
)
apChassisMgrExtSpActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtSpActiveCount.setStatus("mandatory")
_ApChassisMgrExtTrapPsEventText_Type = SnmpAdminString
_ApChassisMgrExtTrapPsEventText_Object = MibScalar
apChassisMgrExtTrapPsEventText = _ApChassisMgrExtTrapPsEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 24),
    _ApChassisMgrExtTrapPsEventText_Type()
)
apChassisMgrExtTrapPsEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtTrapPsEventText.setStatus("mandatory")
_ApChassisMgrExtTrapModuleEventText_Type = SnmpAdminString
_ApChassisMgrExtTrapModuleEventText_Object = MibScalar
apChassisMgrExtTrapModuleEventText = _ApChassisMgrExtTrapModuleEventText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 25),
    _ApChassisMgrExtTrapModuleEventText_Type()
)
apChassisMgrExtTrapModuleEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtTrapModuleEventText.setStatus("mandatory")
_ApChassisMgrExtFreeSpaceDisk0_Type = Integer32
_ApChassisMgrExtFreeSpaceDisk0_Object = MibScalar
apChassisMgrExtFreeSpaceDisk0 = _ApChassisMgrExtFreeSpaceDisk0_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 26),
    _ApChassisMgrExtFreeSpaceDisk0_Type()
)
apChassisMgrExtFreeSpaceDisk0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtFreeSpaceDisk0.setStatus("mandatory")
_ApChassisMgrExtFreeSpaceDisk1_Type = Integer32
_ApChassisMgrExtFreeSpaceDisk1_Object = MibScalar
apChassisMgrExtFreeSpaceDisk1 = _ApChassisMgrExtFreeSpaceDisk1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 27),
    _ApChassisMgrExtFreeSpaceDisk1_Type()
)
apChassisMgrExtFreeSpaceDisk1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apChassisMgrExtFreeSpaceDisk1.setStatus("mandatory")

# Managed Objects groups


# Notification objects

apChassisMgrExtPsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 0, 1)
)
apChassisMgrExtPsTrap.setObjects(
    ("ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtTrapPsEventText")
)
if mibBuilder.loadTexts:
    apChassisMgrExtPsTrap.setStatus(
        ""
    )

apChassisMgrExtModuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 368, 1, 34, 1, 0, 2)
)
apChassisMgrExtModuleTrap.setObjects(
    ("ARROWPOINT-CHASSISMGREXT-MIB", "apChassisMgrExtTrapModuleEventText")
)
if mibBuilder.loadTexts:
    apChassisMgrExtModuleTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARROWPOINT-CHASSISMGREXT-MIB",
    **{"chassisMgrExtMib": chassisMgrExtMib,
       "chassisMgrExtMibNotifs": chassisMgrExtMibNotifs,
       "apChassisMgrExtPsTrap": apChassisMgrExtPsTrap,
       "apChassisMgrExtModuleTrap": apChassisMgrExtModuleTrap,
       "chassisMgrExtMibObjects": chassisMgrExtMibObjects,
       "chassisMgrExtMibConform": chassisMgrExtMibConform,
       "chassisMgrExtMibCompliances": chassisMgrExtMibCompliances,
       "chassisMgrExtMibCompliance": chassisMgrExtMibCompliance,
       "chassisMgrExtMibGroups": chassisMgrExtMibGroups,
       "chassisMgrExtMibGroup": chassisMgrExtMibGroup,
       "chassisMgrExtMibNotif": chassisMgrExtMibNotif,
       "apChassisMgrExtChassisType": apChassisMgrExtChassisType,
       "apChassisMgrExtChassisName": apChassisMgrExtChassisName,
       "apChassisMgrExtChassisSerialNumber": apChassisMgrExtChassisSerialNumber,
       "apChassisMgrExtNumberSlots": apChassisMgrExtNumberSlots,
       "apChassisMgrExtNumberModules": apChassisMgrExtNumberModules,
       "apChassisMgrExtNumberPowerSupplies": apChassisMgrExtNumberPowerSupplies,
       "apChassisMgrExtNumberFans": apChassisMgrExtNumberFans,
       "apChassisMgrExtSoftwareVersionNumber": apChassisMgrExtSoftwareVersionNumber,
       "apChassisMgrExtBootpState": apChassisMgrExtBootpState,
       "apChassisMgrExtMgmtPortIpAddress": apChassisMgrExtMgmtPortIpAddress,
       "apChassisMgrExtBaseEthernetAddress": apChassisMgrExtBaseEthernetAddress,
       "apChassisMgrExtMajorHwVersion": apChassisMgrExtMajorHwVersion,
       "apChassisMgrExtMinorHwVersion": apChassisMgrExtMinorHwVersion,
       "apChassisMgrExtModuleTable": apChassisMgrExtModuleTable,
       "apChassisMgrExtModuleEntry": apChassisMgrExtModuleEntry,
       "apChassisMgrExtModuleSlotNumber": apChassisMgrExtModuleSlotNumber,
       "apChassisMgrExtModuleType": apChassisMgrExtModuleType,
       "apChassisMgrExtModuleName": apChassisMgrExtModuleName,
       "apChassisMgrExtModuleSerialNumber": apChassisMgrExtModuleSerialNumber,
       "apChassisMgrExtModuleOpStatus": apChassisMgrExtModuleOpStatus,
       "apChassisMgrExtModuleNumSubModules": apChassisMgrExtModuleNumSubModules,
       "apChassisMgrExtModuleMajorHwVersion": apChassisMgrExtModuleMajorHwVersion,
       "apChassisMgrExtModuleMinorHwVersion": apChassisMgrExtModuleMinorHwVersion,
       "apChassisMgrExtModuleSubType": apChassisMgrExtModuleSubType,
       "apChassisMgrExtSubModuleTable": apChassisMgrExtSubModuleTable,
       "apChassisMgrExtSubModuleEntry": apChassisMgrExtSubModuleEntry,
       "apChassisMgrExtSubModuleSlot": apChassisMgrExtSubModuleSlot,
       "apChassisMgrExtSubModuleSubSlot": apChassisMgrExtSubModuleSubSlot,
       "apChassisMgrExtSubModuleType": apChassisMgrExtSubModuleType,
       "apChassisMgrExtSubModuleName": apChassisMgrExtSubModuleName,
       "apChassisMgrExtSubModuleOpStatus": apChassisMgrExtSubModuleOpStatus,
       "apChassisMgrExtSubModuleSystemHeapFree": apChassisMgrExtSubModuleSystemHeapFree,
       "apChassisMgrExtSubModuleSystemHeapChainDepth": apChassisMgrExtSubModuleSystemHeapChainDepth,
       "apChassisMgrExtSubModuleInstalledMemory": apChassisMgrExtSubModuleInstalledMemory,
       "apChassisMgrExtSubModuleCPUInstantaneous": apChassisMgrExtSubModuleCPUInstantaneous,
       "apChassisMgrExtSubModuleCPUAverage": apChassisMgrExtSubModuleCPUAverage,
       "apChassisMgrExtSubModuleCurSpWeight": apChassisMgrExtSubModuleCurSpWeight,
       "apChassisMgrExtSubModuleCurSpPower": apChassisMgrExtSubModuleCurSpPower,
       "apChassisMgrExtSubModuleBufferTable": apChassisMgrExtSubModuleBufferTable,
       "apChassisMgrExtSubModuleBufferEntry": apChassisMgrExtSubModuleBufferEntry,
       "apChassisMgrExtSubModuleBufferPool": apChassisMgrExtSubModuleBufferPool,
       "apChassisMgrExtSubModuleBufferSlot": apChassisMgrExtSubModuleBufferSlot,
       "apChassisMgrExtSubModuleBufferSubSlot": apChassisMgrExtSubModuleBufferSubSlot,
       "apChassisMgrExtSubModuleBufferSize": apChassisMgrExtSubModuleBufferSize,
       "apChassisMgrExtSubModuleBufferCount": apChassisMgrExtSubModuleBufferCount,
       "apChassisMgrExtSubModuleBufferAvailable": apChassisMgrExtSubModuleBufferAvailable,
       "apChassisMgrExtSubModuleBufferFailures": apChassisMgrExtSubModuleBufferFailures,
       "apChassisMgrExtSubModuleBufferLowBufferCount": apChassisMgrExtSubModuleBufferLowBufferCount,
       "apChassisMgrExtSlotPortTable": apChassisMgrExtSlotPortTable,
       "apChassisMgrExtSlotPortEntry": apChassisMgrExtSlotPortEntry,
       "apChassisMgrExtSlot": apChassisMgrExtSlot,
       "apChassisMgrExtPort": apChassisMgrExtPort,
       "apChassisMgrExtIfIndex": apChassisMgrExtIfIndex,
       "apChassisMgrExtPortName": apChassisMgrExtPortName,
       "apChassisMgrExtPortOpStatus": apChassisMgrExtPortOpStatus,
       "apChassisMgrExtSubModuleSpWeightTable": apChassisMgrExtSubModuleSpWeightTable,
       "apChassisMgrExtSubModuleSpWeightEntry": apChassisMgrExtSubModuleSpWeightEntry,
       "apChassisMgrExtSubModuleSpWeight": apChassisMgrExtSubModuleSpWeight,
       "apChassisMgrExtSpTotalWeight": apChassisMgrExtSpTotalWeight,
       "apChassisMgrExtSpTotalCount": apChassisMgrExtSpTotalCount,
       "apChassisMgrExtSpActiveCount": apChassisMgrExtSpActiveCount,
       "apChassisMgrExtTrapPsEventText": apChassisMgrExtTrapPsEventText,
       "apChassisMgrExtTrapModuleEventText": apChassisMgrExtTrapModuleEventText,
       "apChassisMgrExtFreeSpaceDisk0": apChassisMgrExtFreeSpaceDisk0,
       "apChassisMgrExtFreeSpaceDisk1": apChassisMgrExtFreeSpaceDisk1}
)
