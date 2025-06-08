# SNMP MIB module (OSA-TWAMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/adva_2544/OSA-TWAMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 00:07:58 2025
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

(advaMIB,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "advaMIB")

(VlanId,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

osaTwamp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 8)
)
if mibBuilder.loadTexts:
    osaTwamp.setRevisions(
        ("2021-08-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsaTwampNotifications_ObjectIdentity = ObjectIdentity
osaTwampNotifications = _OsaTwampNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 8, 0)
)
_OsaTwampGlobals_ObjectIdentity = ObjectIdentity
osaTwampGlobals = _OsaTwampGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 8, 1)
)


class _OsaTwampResponderIgnoreEs_Type(Integer32):
    """Custom type osaTwampResponderIgnoreEs based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("notIgnore", 2))
    )


_OsaTwampResponderIgnoreEs_Type.__name__ = "Integer32"
_OsaTwampResponderIgnoreEs_Object = MibScalar
osaTwampResponderIgnoreEs = _OsaTwampResponderIgnoreEs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 1, 1),
    _OsaTwampResponderIgnoreEs_Type()
)
osaTwampResponderIgnoreEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osaTwampResponderIgnoreEs.setStatus("current")
_OsaTwampResponderTable_Object = MibTable
osaTwampResponderTable = _OsaTwampResponderTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2)
)
if mibBuilder.loadTexts:
    osaTwampResponderTable.setStatus("current")
_OsaTwampResponderEntry_Object = MibTableRow
osaTwampResponderEntry = _OsaTwampResponderEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1)
)
osaTwampResponderEntry.setIndexNames(
    (0, "OSA-TWAMP-MIB", "osaTwampResponderIndex"),
)
if mibBuilder.loadTexts:
    osaTwampResponderEntry.setStatus("current")


class _OsaTwampResponderIndex_Type(Integer32):
    """Custom type osaTwampResponderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsaTwampResponderIndex_Type.__name__ = "Integer32"
_OsaTwampResponderIndex_Object = MibTableColumn
osaTwampResponderIndex = _OsaTwampResponderIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 1),
    _OsaTwampResponderIndex_Type()
)
osaTwampResponderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osaTwampResponderIndex.setStatus("current")


class _OsaTwampResponderAlias_Type(DisplayString):
    """Custom type osaTwampResponderAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_OsaTwampResponderAlias_Type.__name__ = "DisplayString"
_OsaTwampResponderAlias_Object = MibTableColumn
osaTwampResponderAlias = _OsaTwampResponderAlias_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 2),
    _OsaTwampResponderAlias_Type()
)
osaTwampResponderAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderAlias.setStatus("current")


class _OsaTwampResponderControlMode_Type(Integer32):
    """Custom type osaTwampResponderControlMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlDisabled", 1),
          ("controlEnabled", 2))
    )


_OsaTwampResponderControlMode_Type.__name__ = "Integer32"
_OsaTwampResponderControlMode_Object = MibTableColumn
osaTwampResponderControlMode = _OsaTwampResponderControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 3),
    _OsaTwampResponderControlMode_Type()
)
osaTwampResponderControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderControlMode.setStatus("current")


class _OsaTwampResponderIdleTimeout_Type(Unsigned32):
    """Custom type osaTwampResponderIdleTimeout based on Unsigned32"""
    defaultValue = 5


_OsaTwampResponderIdleTimeout_Type.__name__ = "Unsigned32"
_OsaTwampResponderIdleTimeout_Object = MibTableColumn
osaTwampResponderIdleTimeout = _OsaTwampResponderIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 4),
    _OsaTwampResponderIdleTimeout_Type()
)
osaTwampResponderIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderIdleTimeout.setStatus("current")


class _OsaTwampResponderAgingTimeout_Type(Unsigned32):
    """Custom type osaTwampResponderAgingTimeout based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_OsaTwampResponderAgingTimeout_Type.__name__ = "Unsigned32"
_OsaTwampResponderAgingTimeout_Object = MibTableColumn
osaTwampResponderAgingTimeout = _OsaTwampResponderAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 5),
    _OsaTwampResponderAgingTimeout_Type()
)
osaTwampResponderAgingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderAgingTimeout.setStatus("current")
_OsaTwampResponderVlanTag_Type = VlanId
_OsaTwampResponderVlanTag_Object = MibTableColumn
osaTwampResponderVlanTag = _OsaTwampResponderVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 6),
    _OsaTwampResponderVlanTag_Type()
)
osaTwampResponderVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderVlanTag.setStatus("current")


class _OsaTwampResponderSourceIpAddress_Type(DisplayString):
    """Custom type osaTwampResponderSourceIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 48),
    )


_OsaTwampResponderSourceIpAddress_Type.__name__ = "DisplayString"
_OsaTwampResponderSourceIpAddress_Object = MibTableColumn
osaTwampResponderSourceIpAddress = _OsaTwampResponderSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 7),
    _OsaTwampResponderSourceIpAddress_Type()
)
osaTwampResponderSourceIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderSourceIpAddress.setStatus("current")


class _OsaTwampResponderRemoteClientIpAddress_Type(DisplayString):
    """Custom type osaTwampResponderRemoteClientIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 48),
    )


_OsaTwampResponderRemoteClientIpAddress_Type.__name__ = "DisplayString"
_OsaTwampResponderRemoteClientIpAddress_Object = MibTableColumn
osaTwampResponderRemoteClientIpAddress = _OsaTwampResponderRemoteClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 8),
    _OsaTwampResponderRemoteClientIpAddress_Type()
)
osaTwampResponderRemoteClientIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderRemoteClientIpAddress.setStatus("current")


class _OsaTwampResponderSourceUdpPort_Type(Unsigned32):
    """Custom type osaTwampResponderSourceUdpPort based on Unsigned32"""
    defaultValue = 862

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsaTwampResponderSourceUdpPort_Type.__name__ = "Unsigned32"
_OsaTwampResponderSourceUdpPort_Object = MibTableColumn
osaTwampResponderSourceUdpPort = _OsaTwampResponderSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 9),
    _OsaTwampResponderSourceUdpPort_Type()
)
osaTwampResponderSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderSourceUdpPort.setStatus("current")


class _OsaTwampResponderRemoteClientUdpPort_Type(Unsigned32):
    """Custom type osaTwampResponderRemoteClientUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsaTwampResponderRemoteClientUdpPort_Type.__name__ = "Unsigned32"
_OsaTwampResponderRemoteClientUdpPort_Object = MibTableColumn
osaTwampResponderRemoteClientUdpPort = _OsaTwampResponderRemoteClientUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 10),
    _OsaTwampResponderRemoteClientUdpPort_Type()
)
osaTwampResponderRemoteClientUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderRemoteClientUdpPort.setStatus("current")


class _OsaTwampResponderSequenceAction_Type(Integer32):
    """Custom type osaTwampResponderSequenceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearSequenceNumber", 2))
    )


_OsaTwampResponderSequenceAction_Type.__name__ = "Integer32"
_OsaTwampResponderSequenceAction_Object = MibTableColumn
osaTwampResponderSequenceAction = _OsaTwampResponderSequenceAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 11),
    _OsaTwampResponderSequenceAction_Type()
)
osaTwampResponderSequenceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderSequenceAction.setStatus("current")


class _OsaTwampResponderState_Type(Integer32):
    """Custom type osaTwampResponderState based on Integer32"""
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
        *(("init", 1),
          ("testReady", 2),
          ("waitingForTransitTimeout", 3),
          ("end", 4))
    )


_OsaTwampResponderState_Type.__name__ = "Integer32"
_OsaTwampResponderState_Object = MibTableColumn
osaTwampResponderState = _OsaTwampResponderState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 12),
    _OsaTwampResponderState_Type()
)
osaTwampResponderState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderState.setStatus("current")
_OsaTwampResponderRowStatus_Type = RowStatus
_OsaTwampResponderRowStatus_Object = MibTableColumn
osaTwampResponderRowStatus = _OsaTwampResponderRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 2, 1, 13),
    _OsaTwampResponderRowStatus_Type()
)
osaTwampResponderRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    osaTwampResponderRowStatus.setStatus("current")
_OsaTwampResponderSessionTable_Object = MibTable
osaTwampResponderSessionTable = _OsaTwampResponderSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3)
)
if mibBuilder.loadTexts:
    osaTwampResponderSessionTable.setStatus("current")
_OsaTwampResponderSessionEntry_Object = MibTableRow
osaTwampResponderSessionEntry = _OsaTwampResponderSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1)
)
osaTwampResponderSessionEntry.setIndexNames(
    (0, "OSA-TWAMP-MIB", "osaTwampResponderServerIndex"),
    (0, "OSA-TWAMP-MIB", "osaTwampResponderSessionIndex"),
)
if mibBuilder.loadTexts:
    osaTwampResponderSessionEntry.setStatus("current")


class _OsaTwampResponderServerIndex_Type(Integer32):
    """Custom type osaTwampResponderServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_OsaTwampResponderServerIndex_Type.__name__ = "Integer32"
_OsaTwampResponderServerIndex_Object = MibTableColumn
osaTwampResponderServerIndex = _OsaTwampResponderServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 1),
    _OsaTwampResponderServerIndex_Type()
)
osaTwampResponderServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osaTwampResponderServerIndex.setStatus("current")


class _OsaTwampResponderSessionIndex_Type(Integer32):
    """Custom type osaTwampResponderSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_OsaTwampResponderSessionIndex_Type.__name__ = "Integer32"
_OsaTwampResponderSessionIndex_Object = MibTableColumn
osaTwampResponderSessionIndex = _OsaTwampResponderSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 2),
    _OsaTwampResponderSessionIndex_Type()
)
osaTwampResponderSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osaTwampResponderSessionIndex.setStatus("current")


class _OsaTwampResponderSessionIdleTimeout_Type(Unsigned32):
    """Custom type osaTwampResponderSessionIdleTimeout based on Unsigned32"""
    defaultValue = 5


_OsaTwampResponderSessionIdleTimeout_Type.__name__ = "Unsigned32"
_OsaTwampResponderSessionIdleTimeout_Object = MibTableColumn
osaTwampResponderSessionIdleTimeout = _OsaTwampResponderSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 3),
    _OsaTwampResponderSessionIdleTimeout_Type()
)
osaTwampResponderSessionIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionIdleTimeout.setStatus("current")


class _OsaTwampResponderSessionAgingTimeout_Type(Unsigned32):
    """Custom type osaTwampResponderSessionAgingTimeout based on Unsigned32"""
    defaultValue = 900


_OsaTwampResponderSessionAgingTimeout_Type.__name__ = "Unsigned32"
_OsaTwampResponderSessionAgingTimeout_Object = MibTableColumn
osaTwampResponderSessionAgingTimeout = _OsaTwampResponderSessionAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 4),
    _OsaTwampResponderSessionAgingTimeout_Type()
)
osaTwampResponderSessionAgingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionAgingTimeout.setStatus("current")
_OsaTwampResponderSessionVlanTag_Type = VlanId
_OsaTwampResponderSessionVlanTag_Object = MibTableColumn
osaTwampResponderSessionVlanTag = _OsaTwampResponderSessionVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 5),
    _OsaTwampResponderSessionVlanTag_Type()
)
osaTwampResponderSessionVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionVlanTag.setStatus("current")


class _OsaTwampResponderSessionSourceIpAddress_Type(DisplayString):
    """Custom type osaTwampResponderSessionSourceIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 48),
    )


_OsaTwampResponderSessionSourceIpAddress_Type.__name__ = "DisplayString"
_OsaTwampResponderSessionSourceIpAddress_Object = MibTableColumn
osaTwampResponderSessionSourceIpAddress = _OsaTwampResponderSessionSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 6),
    _OsaTwampResponderSessionSourceIpAddress_Type()
)
osaTwampResponderSessionSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionSourceIpAddress.setStatus("current")


class _OsaTwampResponderSessionRemoteClientIpAddress_Type(DisplayString):
    """Custom type osaTwampResponderSessionRemoteClientIpAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 48),
    )


_OsaTwampResponderSessionRemoteClientIpAddress_Type.__name__ = "DisplayString"
_OsaTwampResponderSessionRemoteClientIpAddress_Object = MibTableColumn
osaTwampResponderSessionRemoteClientIpAddress = _OsaTwampResponderSessionRemoteClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 7),
    _OsaTwampResponderSessionRemoteClientIpAddress_Type()
)
osaTwampResponderSessionRemoteClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionRemoteClientIpAddress.setStatus("current")


class _OsaTwampResponderSessionSourceUdpPort_Type(Unsigned32):
    """Custom type osaTwampResponderSessionSourceUdpPort based on Unsigned32"""
    defaultValue = 862

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsaTwampResponderSessionSourceUdpPort_Type.__name__ = "Unsigned32"
_OsaTwampResponderSessionSourceUdpPort_Object = MibTableColumn
osaTwampResponderSessionSourceUdpPort = _OsaTwampResponderSessionSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 8),
    _OsaTwampResponderSessionSourceUdpPort_Type()
)
osaTwampResponderSessionSourceUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionSourceUdpPort.setStatus("current")


class _OsaTwampResponderSessionRemoteClientUdpPort_Type(Unsigned32):
    """Custom type osaTwampResponderSessionRemoteClientUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OsaTwampResponderSessionRemoteClientUdpPort_Type.__name__ = "Unsigned32"
_OsaTwampResponderSessionRemoteClientUdpPort_Object = MibTableColumn
osaTwampResponderSessionRemoteClientUdpPort = _OsaTwampResponderSessionRemoteClientUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 9),
    _OsaTwampResponderSessionRemoteClientUdpPort_Type()
)
osaTwampResponderSessionRemoteClientUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionRemoteClientUdpPort.setStatus("current")
_OsaTwampResponderSessionSequenceNumber_Type = Unsigned32
_OsaTwampResponderSessionSequenceNumber_Object = MibTableColumn
osaTwampResponderSessionSequenceNumber = _OsaTwampResponderSessionSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 10),
    _OsaTwampResponderSessionSequenceNumber_Type()
)
osaTwampResponderSessionSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionSequenceNumber.setStatus("current")


class _OsaTwampResponderSessionState_Type(Integer32):
    """Custom type osaTwampResponderSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("testInProgress", 2),
          ("idle", 3))
    )


_OsaTwampResponderSessionState_Type.__name__ = "Integer32"
_OsaTwampResponderSessionState_Object = MibTableColumn
osaTwampResponderSessionState = _OsaTwampResponderSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 8, 3, 1, 11),
    _OsaTwampResponderSessionState_Type()
)
osaTwampResponderSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaTwampResponderSessionState.setStatus("current")
_OsaTwampConformance_ObjectIdentity = ObjectIdentity
osaTwampConformance = _OsaTwampConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 8, 100)
)
_OsaTwampMIBCompliances_ObjectIdentity = ObjectIdentity
osaTwampMIBCompliances = _OsaTwampMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 8, 100, 1)
)
_OsaTwampMIBGroups_ObjectIdentity = ObjectIdentity
osaTwampMIBGroups = _OsaTwampMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 8, 100, 2)
)

# Managed Objects groups

osaTwampMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 8, 100, 2, 1)
)
osaTwampMandatoryGroup.setObjects(
      *(("OSA-TWAMP-MIB", "osaTwampResponderIgnoreEs"),
        ("OSA-TWAMP-MIB", "osaTwampResponderAlias"),
        ("OSA-TWAMP-MIB", "osaTwampResponderControlMode"),
        ("OSA-TWAMP-MIB", "osaTwampResponderIdleTimeout"),
        ("OSA-TWAMP-MIB", "osaTwampResponderAgingTimeout"),
        ("OSA-TWAMP-MIB", "osaTwampResponderVlanTag"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSourceIpAddress"),
        ("OSA-TWAMP-MIB", "osaTwampResponderRemoteClientIpAddress"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSourceUdpPort"),
        ("OSA-TWAMP-MIB", "osaTwampResponderRemoteClientUdpPort"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSequenceAction"),
        ("OSA-TWAMP-MIB", "osaTwampResponderState"),
        ("OSA-TWAMP-MIB", "osaTwampResponderRowStatus"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionIdleTimeout"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionAgingTimeout"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionVlanTag"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionSourceIpAddress"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionRemoteClientIpAddress"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionSourceUdpPort"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionRemoteClientUdpPort"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionSequenceNumber"),
        ("OSA-TWAMP-MIB", "osaTwampResponderSessionState"))
)
if mibBuilder.loadTexts:
    osaTwampMandatoryGroup.setStatus("current")


# Notification objects

osaTwampMaxSessionsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2544, 8, 0, 1)
)
if mibBuilder.loadTexts:
    osaTwampMaxSessionsExceeded.setStatus(
        "current"
    )


# Notifications groups

osaTwampNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2544, 8, 100, 2, 2)
)
osaTwampNotificationGroup.setObjects(
    ("OSA-TWAMP-MIB", "osaTwampMaxSessionsExceeded")
)
if mibBuilder.loadTexts:
    osaTwampNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

osaTwampMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 8, 100, 1, 1)
)
osaTwampMIBCompliance.setObjects(
      *(("OSA-TWAMP-MIB", "osaTwampMandatoryGroup"),
        ("OSA-TWAMP-MIB", "osaTwampNotificationGroup"))
)
if mibBuilder.loadTexts:
    osaTwampMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OSA-TWAMP-MIB",
    **{"osaTwamp": osaTwamp,
       "osaTwampNotifications": osaTwampNotifications,
       "osaTwampMaxSessionsExceeded": osaTwampMaxSessionsExceeded,
       "osaTwampGlobals": osaTwampGlobals,
       "osaTwampResponderIgnoreEs": osaTwampResponderIgnoreEs,
       "osaTwampResponderTable": osaTwampResponderTable,
       "osaTwampResponderEntry": osaTwampResponderEntry,
       "osaTwampResponderIndex": osaTwampResponderIndex,
       "osaTwampResponderAlias": osaTwampResponderAlias,
       "osaTwampResponderControlMode": osaTwampResponderControlMode,
       "osaTwampResponderIdleTimeout": osaTwampResponderIdleTimeout,
       "osaTwampResponderAgingTimeout": osaTwampResponderAgingTimeout,
       "osaTwampResponderVlanTag": osaTwampResponderVlanTag,
       "osaTwampResponderSourceIpAddress": osaTwampResponderSourceIpAddress,
       "osaTwampResponderRemoteClientIpAddress": osaTwampResponderRemoteClientIpAddress,
       "osaTwampResponderSourceUdpPort": osaTwampResponderSourceUdpPort,
       "osaTwampResponderRemoteClientUdpPort": osaTwampResponderRemoteClientUdpPort,
       "osaTwampResponderSequenceAction": osaTwampResponderSequenceAction,
       "osaTwampResponderState": osaTwampResponderState,
       "osaTwampResponderRowStatus": osaTwampResponderRowStatus,
       "osaTwampResponderSessionTable": osaTwampResponderSessionTable,
       "osaTwampResponderSessionEntry": osaTwampResponderSessionEntry,
       "osaTwampResponderServerIndex": osaTwampResponderServerIndex,
       "osaTwampResponderSessionIndex": osaTwampResponderSessionIndex,
       "osaTwampResponderSessionIdleTimeout": osaTwampResponderSessionIdleTimeout,
       "osaTwampResponderSessionAgingTimeout": osaTwampResponderSessionAgingTimeout,
       "osaTwampResponderSessionVlanTag": osaTwampResponderSessionVlanTag,
       "osaTwampResponderSessionSourceIpAddress": osaTwampResponderSessionSourceIpAddress,
       "osaTwampResponderSessionRemoteClientIpAddress": osaTwampResponderSessionRemoteClientIpAddress,
       "osaTwampResponderSessionSourceUdpPort": osaTwampResponderSessionSourceUdpPort,
       "osaTwampResponderSessionRemoteClientUdpPort": osaTwampResponderSessionRemoteClientUdpPort,
       "osaTwampResponderSessionSequenceNumber": osaTwampResponderSessionSequenceNumber,
       "osaTwampResponderSessionState": osaTwampResponderSessionState,
       "osaTwampConformance": osaTwampConformance,
       "osaTwampMIBCompliances": osaTwampMIBCompliances,
       "osaTwampMIBCompliance": osaTwampMIBCompliance,
       "osaTwampMIBGroups": osaTwampMIBGroups,
       "osaTwampMandatoryGroup": osaTwampMandatoryGroup,
       "osaTwampNotificationGroup": osaTwampNotificationGroup}
)
