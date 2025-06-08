# SNMP MIB module (CONTELEC-DUMMYLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/continental_48307/CONTELEC-DUMMYLOAD-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:57:19 2025
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

(contelec,) = mibBuilder.importSymbols(
    "CONTELEC-COMMON-MIB",
    "contelec")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

contelecDummyLoad = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1)
)
if mibBuilder.loadTexts:
    contelecDummyLoad.setRevisions(
        ("2017-09-06 14:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CecDLConformance_ObjectIdentity = ObjectIdentity
cecDLConformance = _CecDLConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2)
)
_CecDLCompliances_ObjectIdentity = ObjectIdentity
cecDLCompliances = _CecDLCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 1)
)
_CecDLGroups_ObjectIdentity = ObjectIdentity
cecDLGroups = _CecDLGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2)
)
_CecDLobject_ObjectIdentity = ObjectIdentity
cecDLobject = _CecDLobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3)
)
_CecDLTraps_ObjectIdentity = ObjectIdentity
cecDLTraps = _CecDLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0)
)
_CecDLSpecs_ObjectIdentity = ObjectIdentity
cecDLSpecs = _CecDLSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1)
)


class _CecDLready_Type(Integer32):
    """Custom type cecDLready based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CecDLready_Type.__name__ = "Integer32"
_CecDLready_Object = MibScalar
cecDLready = _CecDLready_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 1),
    _CecDLready_Type()
)
cecDLready.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLready.setStatus("current")


class _CecDLwaterTemperIN_Type(Integer32):
    """Custom type cecDLwaterTemperIN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CecDLwaterTemperIN_Type.__name__ = "Integer32"
_CecDLwaterTemperIN_Object = MibScalar
cecDLwaterTemperIN = _CecDLwaterTemperIN_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 2),
    _CecDLwaterTemperIN_Type()
)
cecDLwaterTemperIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLwaterTemperIN.setStatus("current")


class _CecDLwaterTemperOUT_Type(Integer32):
    """Custom type cecDLwaterTemperOUT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CecDLwaterTemperOUT_Type.__name__ = "Integer32"
_CecDLwaterTemperOUT_Object = MibScalar
cecDLwaterTemperOUT = _CecDLwaterTemperOUT_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 3),
    _CecDLwaterTemperOUT_Type()
)
cecDLwaterTemperOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLwaterTemperOUT.setStatus("current")


class _CecDLwaterFlow_Type(Integer32):
    """Custom type cecDLwaterFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6300),
    )


_CecDLwaterFlow_Type.__name__ = "Integer32"
_CecDLwaterFlow_Object = MibScalar
cecDLwaterFlow = _CecDLwaterFlow_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 4),
    _CecDLwaterFlow_Type()
)
cecDLwaterFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLwaterFlow.setStatus("current")


class _CecDLohms_Type(Integer32):
    """Custom type cecDLohms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 50),
    )


_CecDLohms_Type.__name__ = "Integer32"
_CecDLohms_Object = MibScalar
cecDLohms = _CecDLohms_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 5),
    _CecDLohms_Type()
)
cecDLohms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cecDLohms.setStatus("current")
_CecDLhours_Type = Integer32
_CecDLhours_Object = MibScalar
cecDLhours = _CecDLhours_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 6),
    _CecDLhours_Type()
)
cecDLhours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLhours.setStatus("current")
_CecDLhwConfig_Type = OctetString
_CecDLhwConfig_Object = MibScalar
cecDLhwConfig = _CecDLhwConfig_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 7),
    _CecDLhwConfig_Type()
)
cecDLhwConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLhwConfig.setStatus("current")
_CecDLswConfig_Type = OctetString
_CecDLswConfig_Object = MibScalar
cecDLswConfig = _CecDLswConfig_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 8),
    _CecDLswConfig_Type()
)
cecDLswConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLswConfig.setStatus("current")
_CecDLpower_Type = Integer32
_CecDLpower_Object = MibScalar
cecDLpower = _CecDLpower_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 9),
    _CecDLpower_Type()
)
cecDLpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLpower.setStatus("current")
_CecDLpowerCal_Type = Integer32
_CecDLpowerCal_Object = MibScalar
cecDLpowerCal = _CecDLpowerCal_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 10),
    _CecDLpowerCal_Type()
)
cecDLpowerCal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cecDLpowerCal.setStatus("current")


class _CecDLremote_Type(Integer32):
    """Custom type cecDLremote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CecDLremote_Type.__name__ = "Integer32"
_CecDLremote_Object = MibScalar
cecDLremote = _CecDLremote_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 11),
    _CecDLremote_Type()
)
cecDLremote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLremote.setStatus("current")


class _CecDLpumpTempStatus_Type(Integer32):
    """Custom type cecDLpumpTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CecDLpumpTempStatus_Type.__name__ = "Integer32"
_CecDLpumpTempStatus_Object = MibScalar
cecDLpumpTempStatus = _CecDLpumpTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 12),
    _CecDLpumpTempStatus_Type()
)
cecDLpumpTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLpumpTempStatus.setStatus("current")


class _CecDLpumpFaultStatus_Type(Integer32):
    """Custom type cecDLpumpFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CecDLpumpFaultStatus_Type.__name__ = "Integer32"
_CecDLpumpFaultStatus_Object = MibScalar
cecDLpumpFaultStatus = _CecDLpumpFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 13),
    _CecDLpumpFaultStatus_Type()
)
cecDLpumpFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLpumpFaultStatus.setStatus("current")


class _CecDLpumpOnStatus_Type(Integer32):
    """Custom type cecDLpumpOnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CecDLpumpOnStatus_Type.__name__ = "Integer32"
_CecDLpumpOnStatus_Object = MibScalar
cecDLpumpOnStatus = _CecDLpumpOnStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 14),
    _CecDLpumpOnStatus_Type()
)
cecDLpumpOnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLpumpOnStatus.setStatus("current")


class _CecDLintlkStatus_Type(Integer32):
    """Custom type cecDLintlkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CecDLintlkStatus_Type.__name__ = "Integer32"
_CecDLintlkStatus_Object = MibScalar
cecDLintlkStatus = _CecDLintlkStatus_Object(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 1, 15),
    _CecDLintlkStatus_Type()
)
cecDLintlkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cecDLintlkStatus.setStatus("current")

# Managed Objects groups

cecDLGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 1)
)
cecDLGroup.setObjects(
      *(("CONTELEC-DUMMYLOAD-MIB", "cecDLready"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLwaterTemperIN"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLwaterTemperOUT"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLwaterFlow"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLohms"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLhours"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLhwConfig"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLswConfig"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpower"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpowerCal"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLremote"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpumpTempStatus"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpumpFaultStatus"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpumpOnStatus"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLintlkStatus"))
)
if mibBuilder.loadTexts:
    cecDLGroup.setStatus("current")


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        "current"
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 2)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        "current"
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 3)
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        "current"
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 4)
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        "current"
    )

cecDLfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 5)
)
if mibBuilder.loadTexts:
    cecDLfault.setStatus(
        "current"
    )

cecDLpumpFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 6)
)
if mibBuilder.loadTexts:
    cecDLpumpFault.setStatus(
        "current"
    )

cecDLpumpOvertemp = NotificationType(
    (1, 3, 6, 1, 4, 1, 48307, 1, 3, 0, 7)
)
if mibBuilder.loadTexts:
    cecDLpumpOvertemp.setStatus(
        "current"
    )


# Notifications groups

cecDLNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 2, 2)
)
cecDLNotificationGroup.setObjects(
      *(("CONTELEC-DUMMYLOAD-MIB", "coldStart"),
        ("CONTELEC-DUMMYLOAD-MIB", "warmStart"),
        ("CONTELEC-DUMMYLOAD-MIB", "linkDown"),
        ("CONTELEC-DUMMYLOAD-MIB", "linkUp"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLfault"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpumpFault"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLpumpOvertemp"))
)
if mibBuilder.loadTexts:
    cecDLNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cecDLCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 48307, 1, 2, 1, 1)
)
cecDLCompliance.setObjects(
      *(("CONTELEC-DUMMYLOAD-MIB", "cecDLGroup"),
        ("CONTELEC-DUMMYLOAD-MIB", "cecDLNotificationGroup"))
)
if mibBuilder.loadTexts:
    cecDLCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTELEC-DUMMYLOAD-MIB",
    **{"contelecDummyLoad": contelecDummyLoad,
       "cecDLConformance": cecDLConformance,
       "cecDLCompliances": cecDLCompliances,
       "cecDLCompliance": cecDLCompliance,
       "cecDLGroups": cecDLGroups,
       "cecDLGroup": cecDLGroup,
       "cecDLNotificationGroup": cecDLNotificationGroup,
       "cecDLobject": cecDLobject,
       "cecDLTraps": cecDLTraps,
       "coldStart": coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "cecDLfault": cecDLfault,
       "cecDLpumpFault": cecDLpumpFault,
       "cecDLpumpOvertemp": cecDLpumpOvertemp,
       "cecDLSpecs": cecDLSpecs,
       "cecDLready": cecDLready,
       "cecDLwaterTemperIN": cecDLwaterTemperIN,
       "cecDLwaterTemperOUT": cecDLwaterTemperOUT,
       "cecDLwaterFlow": cecDLwaterFlow,
       "cecDLohms": cecDLohms,
       "cecDLhours": cecDLhours,
       "cecDLhwConfig": cecDLhwConfig,
       "cecDLswConfig": cecDLswConfig,
       "cecDLpower": cecDLpower,
       "cecDLpowerCal": cecDLpowerCal,
       "cecDLremote": cecDLremote,
       "cecDLpumpTempStatus": cecDLpumpTempStatus,
       "cecDLpumpFaultStatus": cecDLpumpFaultStatus,
       "cecDLpumpOnStatus": cecDLpumpOnStatus,
       "cecDLintlkStatus": cecDLintlkStatus}
)
