# SNMP MIB module (CEM-SYS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ciena_6352/CEM-SYS.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:49:21 2025
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

(catena,) = mibBuilder.importSymbols(
    "CEM-SMI",
    "catena")

(entPhysicalClass,
 entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalClass",
    "entPhysicalDescr",
    "entPhysicalIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysObjectID,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysObjectID")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cnSystemGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 2)
)
if mibBuilder.loadTexts:
    cnSystemGroup.setRevisions(
        ("2001-10-04 13:48",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CnSnmpFeatureIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("cnSnmpFeatureAlarm", 1),
          ("cnSnmpFeatureAps", 2),
          ("cnSnmpFeatureAtm", 3),
          ("cnSnmpFeatureCard", 4),
          ("cnSnmpFeatureDs1", 5),
          ("cnSnmpFeatureDs3", 6),
          ("cnSnmpFeatureDsl", 7),
          ("cnSnmpFeatureIpnet", 8),
          ("cnSnmpFeatureLooptest", 9),
          ("cnSnmpFeatureMaintenance", 10),
          ("cnSnmpFeatureShelf", 11),
          ("cnSnmpFeatureSnmp", 12),
          ("cnSnmpFeatureSonet", 13),
          ("cnSnmpFeatureSparing", 14),
          ("cnSnmpFeatureSpecials", 15),
          ("cnSnmpFeatureSystem", 16),
          ("cnSnmpFeatureTiming", 17),
          ("cnSnmpFeatureVoiceServices", 18),
          ("cnSnmpFeatureVoiceInfrastructure", 19),
          ("cnSnmpFeatureUser", 20),
          ("cnSnmpFeatureMulticast", 21),
          ("cnSnmpFeatureRings", 22))
    )



# MIB Managed Objects in the order of their OIDs

_CnSystemMIB_ObjectIdentity = ObjectIdentity
cnSystemMIB = _CnSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1)
)
_CnSysLocalDateAndTime_Type = DateAndTime
_CnSysLocalDateAndTime_Object = MibScalar
cnSysLocalDateAndTime = _CnSysLocalDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 1),
    _CnSysLocalDateAndTime_Type()
)
cnSysLocalDateAndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysLocalDateAndTime.setStatus("current")


class _CnSysEnableConfigurationTraps_Type(Integer32):
    """Custom type cnSysEnableConfigurationTraps based on Integer32"""
    defaultValue = 1

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


_CnSysEnableConfigurationTraps_Type.__name__ = "Integer32"
_CnSysEnableConfigurationTraps_Object = MibScalar
cnSysEnableConfigurationTraps = _CnSysEnableConfigurationTraps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 2),
    _CnSysEnableConfigurationTraps_Type()
)
cnSysEnableConfigurationTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysEnableConfigurationTraps.setStatus("current")


class _CnAdslProfileEditableWhenInUse_Type(Integer32):
    """Custom type cnAdslProfileEditableWhenInUse based on Integer32"""
    defaultValue = 0

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


_CnAdslProfileEditableWhenInUse_Type.__name__ = "Integer32"
_CnAdslProfileEditableWhenInUse_Object = MibScalar
cnAdslProfileEditableWhenInUse = _CnAdslProfileEditableWhenInUse_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 3),
    _CnAdslProfileEditableWhenInUse_Type()
)
cnAdslProfileEditableWhenInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnAdslProfileEditableWhenInUse.setStatus("current")


class _CnConfigChangeInfo_Type(OctetString):
    """Custom type cnConfigChangeInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CnConfigChangeInfo_Type.__name__ = "OctetString"
_CnConfigChangeInfo_Object = MibScalar
cnConfigChangeInfo = _CnConfigChangeInfo_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 4),
    _CnConfigChangeInfo_Type()
)
cnConfigChangeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnConfigChangeInfo.setStatus("current")


class _CnSysShutdownTime_Type(Integer32):
    """Custom type cnSysShutdownTime based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 480),
    )


_CnSysShutdownTime_Type.__name__ = "Integer32"
_CnSysShutdownTime_Object = MibScalar
cnSysShutdownTime = _CnSysShutdownTime_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 5),
    _CnSysShutdownTime_Type()
)
cnSysShutdownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysShutdownTime.setStatus("current")


class _CnSysCountDownRemaining_Type(Integer32):
    """Custom type cnSysCountDownRemaining based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 480),
    )


_CnSysCountDownRemaining_Type.__name__ = "Integer32"
_CnSysCountDownRemaining_Object = MibScalar
cnSysCountDownRemaining = _CnSysCountDownRemaining_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 6),
    _CnSysCountDownRemaining_Type()
)
cnSysCountDownRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnSysCountDownRemaining.setStatus("current")


class _CnFlashRestoreStatus_Type(Integer32):
    """Custom type cnFlashRestoreStatus based on Integer32"""
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
        *(("restoreInProgress", 1),
          ("restoreSuccess", 2),
          ("restoreFailureUnknown", 3),
          ("restoreFailureInUse", 4))
    )


_CnFlashRestoreStatus_Type.__name__ = "Integer32"
_CnFlashRestoreStatus_Object = MibScalar
cnFlashRestoreStatus = _CnFlashRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 13),
    _CnFlashRestoreStatus_Type()
)
cnFlashRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnFlashRestoreStatus.setStatus("current")


class _CnSysEnableDslLineStatusTraps_Type(Integer32):
    """Custom type cnSysEnableDslLineStatusTraps based on Integer32"""
    defaultValue = 0

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


_CnSysEnableDslLineStatusTraps_Type.__name__ = "Integer32"
_CnSysEnableDslLineStatusTraps_Object = MibScalar
cnSysEnableDslLineStatusTraps = _CnSysEnableDslLineStatusTraps_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 19),
    _CnSysEnableDslLineStatusTraps_Type()
)
cnSysEnableDslLineStatusTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysEnableDslLineStatusTraps.setStatus("current")


class _CnSysUbrReserve_Type(Integer32):
    """Custom type cnSysUbrReserve based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CnSysUbrReserve_Type.__name__ = "Integer32"
_CnSysUbrReserve_Object = MibScalar
cnSysUbrReserve = _CnSysUbrReserve_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 20),
    _CnSysUbrReserve_Type()
)
cnSysUbrReserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysUbrReserve.setStatus("current")


class _CnSysTL1TcpPort_Type(Integer32):
    """Custom type cnSysTL1TcpPort based on Integer32"""
    defaultValue = 9050

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 9999),
    )


_CnSysTL1TcpPort_Type.__name__ = "Integer32"
_CnSysTL1TcpPort_Object = MibScalar
cnSysTL1TcpPort = _CnSysTL1TcpPort_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 21),
    _CnSysTL1TcpPort_Type()
)
cnSysTL1TcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysTL1TcpPort.setStatus("current")


class _CnSysRegionProfile_Type(Integer32):
    """Custom type cnSysRegionProfile based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("region1", 0),
          ("region2", 1),
          ("region3", 2))
    )


_CnSysRegionProfile_Type.__name__ = "Integer32"
_CnSysRegionProfile_Object = MibScalar
cnSysRegionProfile = _CnSysRegionProfile_Object(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 22),
    _CnSysRegionProfile_Type()
)
cnSysRegionProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnSysRegionProfile.setStatus("current")

# Managed Objects groups


# Notification objects

cnCLIConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 7)
)
cnCLIConfigChangeTrap.setObjects(
    ("CEM-SYS", "cnConfigChangeInfo")
)
if mibBuilder.loadTexts:
    cnCLIConfigChangeTrap.setStatus(
        "current"
    )

cnSysPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 8)
)
cnSysPowerFailure.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    cnSysPowerFailure.setStatus(
        "current"
    )

cnSysPowerRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 9)
)
cnSysPowerRestore.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    cnSysPowerRestore.setStatus(
        "current"
    )

cnSysShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 10)
)
cnSysShutdown.setObjects(
    ("SNMPv2-MIB", "sysObjectID")
)
if mibBuilder.loadTexts:
    cnSysShutdown.setStatus(
        "current"
    )

cnCardAppearance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 11)
)
cnCardAppearance.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    cnCardAppearance.setStatus(
        "deprecated"
    )

cnCardDisappearance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 12)
)
cnCardDisappearance.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    cnCardDisappearance.setStatus(
        "deprecated"
    )

cnFlashRestoreCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 14)
)
cnFlashRestoreCompletion.setObjects(
    ("CEM-SYS", "cnFlashRestoreStatus")
)
if mibBuilder.loadTexts:
    cnFlashRestoreCompletion.setStatus(
        "current"
    )

cnSysBootFromStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 15)
)
if mibBuilder.loadTexts:
    cnSysBootFromStandby.setStatus(
        "current"
    )

cnEcuBootFromStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 16)
)
cnEcuBootFromStandby.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    cnEcuBootFromStandby.setStatus(
        "current"
    )

cnV2CardAppearance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 17)
)
cnV2CardAppearance.setObjects(
    ("ENTITY-MIB", "entPhysicalClass")
)
if mibBuilder.loadTexts:
    cnV2CardAppearance.setStatus(
        "current"
    )

cnV2CardDisappearance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6352, 2, 1, 18)
)
cnV2CardDisappearance.setObjects(
    ("ENTITY-MIB", "entPhysicalClass")
)
if mibBuilder.loadTexts:
    cnV2CardDisappearance.setStatus(
        "current"
    )


# Notifications groups

cnTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 2, 3)
)
cnTrapGroup.setObjects(
      *(("CEM-SYS", "cnCLIConfigChangeTrap"),
        ("CEM-SYS", "cnSysPowerFailure"),
        ("CEM-SYS", "cnSysPowerRestore"),
        ("CEM-SYS", "cnSysShutdown"),
        ("CEM-SYS", "cnCardAppearance"),
        ("CEM-SYS", "cnCardDisappearance"),
        ("CEM-SYS", "cnFlashRestoreCompletion"),
        ("CEM-SYS", "cnSysBootFromStandby"))
)
if mibBuilder.loadTexts:
    cnTrapGroup.setStatus(
        "deprecated"
    )

cnV2TrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6352, 2, 4)
)
cnV2TrapGroup.setObjects(
      *(("CEM-SYS", "cnCLIConfigChangeTrap"),
        ("CEM-SYS", "cnSysPowerFailure"),
        ("CEM-SYS", "cnSysPowerRestore"),
        ("CEM-SYS", "cnSysShutdown"),
        ("CEM-SYS", "cnFlashRestoreCompletion"),
        ("CEM-SYS", "cnSysBootFromStandby"),
        ("CEM-SYS", "cnEcuBootFromStandby"),
        ("CEM-SYS", "cnV2CardAppearance"),
        ("CEM-SYS", "cnV2CardDisappearance"))
)
if mibBuilder.loadTexts:
    cnV2TrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CEM-SYS",
    **{"CnSnmpFeatureIndex": CnSnmpFeatureIndex,
       "cnSystemGroup": cnSystemGroup,
       "cnSystemMIB": cnSystemMIB,
       "cnSysLocalDateAndTime": cnSysLocalDateAndTime,
       "cnSysEnableConfigurationTraps": cnSysEnableConfigurationTraps,
       "cnAdslProfileEditableWhenInUse": cnAdslProfileEditableWhenInUse,
       "cnConfigChangeInfo": cnConfigChangeInfo,
       "cnSysShutdownTime": cnSysShutdownTime,
       "cnSysCountDownRemaining": cnSysCountDownRemaining,
       "cnCLIConfigChangeTrap": cnCLIConfigChangeTrap,
       "cnSysPowerFailure": cnSysPowerFailure,
       "cnSysPowerRestore": cnSysPowerRestore,
       "cnSysShutdown": cnSysShutdown,
       "cnCardAppearance": cnCardAppearance,
       "cnCardDisappearance": cnCardDisappearance,
       "cnFlashRestoreStatus": cnFlashRestoreStatus,
       "cnFlashRestoreCompletion": cnFlashRestoreCompletion,
       "cnSysBootFromStandby": cnSysBootFromStandby,
       "cnEcuBootFromStandby": cnEcuBootFromStandby,
       "cnV2CardAppearance": cnV2CardAppearance,
       "cnV2CardDisappearance": cnV2CardDisappearance,
       "cnSysEnableDslLineStatusTraps": cnSysEnableDslLineStatusTraps,
       "cnSysUbrReserve": cnSysUbrReserve,
       "cnSysTL1TcpPort": cnSysTL1TcpPort,
       "cnSysRegionProfile": cnSysRegionProfile,
       "cnTrapGroup": cnTrapGroup,
       "cnV2TrapGroup": cnV2TrapGroup}
)
