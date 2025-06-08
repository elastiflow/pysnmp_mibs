# SNMP MIB module (RUIJIE-PIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-PIM-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:07 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ipMRouteGroup,
 ipMRouteNextHopAddress,
 ipMRouteNextHopGroup,
 ipMRouteNextHopIfIndex,
 ipMRouteNextHopSource,
 ipMRouteNextHopSourceMask,
 ipMRouteSource,
 ipMRouteSourceMask) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteGroup",
    "ipMRouteNextHopAddress",
    "ipMRouteNextHopGroup",
    "ipMRouteNextHopIfIndex",
    "ipMRouteNextHopSource",
    "ipMRouteNextHopSourceMask",
    "ipMRouteSource",
    "ipMRouteSourceMask")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ruijieMgmt,) = mibBuilder.importSymbols(
    "RUIJIE-SMI",
    "ruijieMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruijiePimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27)
)
if mibBuilder.loadTexts:
    ruijiePimMIB.setRevisions(
        ("2003-01-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijiePimMIBObjects_ObjectIdentity = ObjectIdentity
ruijiePimMIBObjects = _RuijiePimMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1)
)
_RuijiePim_ObjectIdentity = ObjectIdentity
ruijiePim = _RuijiePim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1)
)


class _RuijiePimJoinPruneInterval_Type(Integer32):
    """Custom type ruijiePimJoinPruneInterval based on Integer32"""
    defaultValue = 60


_RuijiePimJoinPruneInterval_Type.__name__ = "Integer32"
_RuijiePimJoinPruneInterval_Object = MibScalar
ruijiePimJoinPruneInterval = _RuijiePimJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 1),
    _RuijiePimJoinPruneInterval_Type()
)
ruijiePimJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimJoinPruneInterval.setUnits("seconds")
_RuijiePimInterfaceTable_Object = MibTable
ruijiePimInterfaceTable = _RuijiePimInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruijiePimInterfaceTable.setStatus("current")
_RuijiePimInterfaceEntry_Object = MibTableRow
ruijiePimInterfaceEntry = _RuijiePimInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1)
)
ruijiePimInterfaceEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ruijiePimInterfaceEntry.setStatus("current")
_RuijiePimInterfaceIfIndex_Type = InterfaceIndex
_RuijiePimInterfaceIfIndex_Object = MibTableColumn
ruijiePimInterfaceIfIndex = _RuijiePimInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 1),
    _RuijiePimInterfaceIfIndex_Type()
)
ruijiePimInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimInterfaceIfIndex.setStatus("current")
_RuijiePimInterfaceAddress_Type = IpAddress
_RuijiePimInterfaceAddress_Object = MibTableColumn
ruijiePimInterfaceAddress = _RuijiePimInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 2),
    _RuijiePimInterfaceAddress_Type()
)
ruijiePimInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceAddress.setStatus("current")
_RuijiePimInterfaceNetMask_Type = IpAddress
_RuijiePimInterfaceNetMask_Object = MibTableColumn
ruijiePimInterfaceNetMask = _RuijiePimInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 3),
    _RuijiePimInterfaceNetMask_Type()
)
ruijiePimInterfaceNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceNetMask.setStatus("current")


class _RuijiePimInterfaceMode_Type(Integer32):
    """Custom type ruijiePimInterfaceMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2),
          ("sparseDense", 3))
    )


_RuijiePimInterfaceMode_Type.__name__ = "Integer32"
_RuijiePimInterfaceMode_Object = MibTableColumn
ruijiePimInterfaceMode = _RuijiePimInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 4),
    _RuijiePimInterfaceMode_Type()
)
ruijiePimInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceMode.setStatus("current")
_RuijiePimInterfaceDR_Type = IpAddress
_RuijiePimInterfaceDR_Object = MibTableColumn
ruijiePimInterfaceDR = _RuijiePimInterfaceDR_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 5),
    _RuijiePimInterfaceDR_Type()
)
ruijiePimInterfaceDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceDR.setStatus("current")


class _RuijiePimInterfaceHelloInterval_Type(Integer32):
    """Custom type ruijiePimInterfaceHelloInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijiePimInterfaceHelloInterval_Type.__name__ = "Integer32"
_RuijiePimInterfaceHelloInterval_Object = MibTableColumn
ruijiePimInterfaceHelloInterval = _RuijiePimInterfaceHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 6),
    _RuijiePimInterfaceHelloInterval_Type()
)
ruijiePimInterfaceHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfaceHelloInterval.setUnits("seconds")
_RuijiePimInterfaceJoinPruneInterval_Type = Integer32
_RuijiePimInterfaceJoinPruneInterval_Object = MibTableColumn
ruijiePimInterfaceJoinPruneInterval = _RuijiePimInterfaceJoinPruneInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 7),
    _RuijiePimInterfaceJoinPruneInterval_Type()
)
ruijiePimInterfaceJoinPruneInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceJoinPruneInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfaceJoinPruneInterval.setUnits("seconds")


class _RuijiePimInterfaceCBSRPreference_Type(Integer32):
    """Custom type ruijiePimInterfaceCBSRPreference based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_RuijiePimInterfaceCBSRPreference_Type.__name__ = "Integer32"
_RuijiePimInterfaceCBSRPreference_Object = MibTableColumn
ruijiePimInterfaceCBSRPreference = _RuijiePimInterfaceCBSRPreference_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 8),
    _RuijiePimInterfaceCBSRPreference_Type()
)
ruijiePimInterfaceCBSRPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceCBSRPreference.setStatus("current")


class _RuijiePimInterfaceTrigHelloInterval_Type(Integer32):
    """Custom type ruijiePimInterfaceTrigHelloInterval based on Integer32"""
    defaultValue = 5


_RuijiePimInterfaceTrigHelloInterval_Type.__name__ = "Integer32"
_RuijiePimInterfaceTrigHelloInterval_Object = MibTableColumn
ruijiePimInterfaceTrigHelloInterval = _RuijiePimInterfaceTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 9),
    _RuijiePimInterfaceTrigHelloInterval_Type()
)
ruijiePimInterfaceTrigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfaceTrigHelloInterval.setUnits("seconds")


class _RuijiePimInterfaceHelloHoldtime_Type(Integer32):
    """Custom type ruijiePimInterfaceHelloHoldtime based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijiePimInterfaceHelloHoldtime_Type.__name__ = "Integer32"
_RuijiePimInterfaceHelloHoldtime_Object = MibTableColumn
ruijiePimInterfaceHelloHoldtime = _RuijiePimInterfaceHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 10),
    _RuijiePimInterfaceHelloHoldtime_Type()
)
ruijiePimInterfaceHelloHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfaceHelloHoldtime.setUnits("seconds")


class _RuijiePimInterfaceLanPruneDelay_Type(Integer32):
    """Custom type ruijiePimInterfaceLanPruneDelay based on Integer32"""
    defaultValue = 2

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


_RuijiePimInterfaceLanPruneDelay_Type.__name__ = "Integer32"
_RuijiePimInterfaceLanPruneDelay_Object = MibTableColumn
ruijiePimInterfaceLanPruneDelay = _RuijiePimInterfaceLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 11),
    _RuijiePimInterfaceLanPruneDelay_Type()
)
ruijiePimInterfaceLanPruneDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceLanPruneDelay.setStatus("current")


class _RuijiePimInterfacePropagationDelay_Type(Integer32):
    """Custom type ruijiePimInterfacePropagationDelay based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_RuijiePimInterfacePropagationDelay_Type.__name__ = "Integer32"
_RuijiePimInterfacePropagationDelay_Object = MibTableColumn
ruijiePimInterfacePropagationDelay = _RuijiePimInterfacePropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 12),
    _RuijiePimInterfacePropagationDelay_Type()
)
ruijiePimInterfacePropagationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfacePropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfacePropagationDelay.setUnits("milliseconds")


class _RuijiePimInterfaceOverrideInterval_Type(Integer32):
    """Custom type ruijiePimInterfaceOverrideInterval based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijiePimInterfaceOverrideInterval_Type.__name__ = "Integer32"
_RuijiePimInterfaceOverrideInterval_Object = MibTableColumn
ruijiePimInterfaceOverrideInterval = _RuijiePimInterfaceOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 13),
    _RuijiePimInterfaceOverrideInterval_Type()
)
ruijiePimInterfaceOverrideInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceOverrideInterval.setStatus("current")


class _RuijiePimInterfaceGenerationID_Type(Integer32):
    """Custom type ruijiePimInterfaceGenerationID based on Integer32"""
    defaultValue = 2

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


_RuijiePimInterfaceGenerationID_Type.__name__ = "Integer32"
_RuijiePimInterfaceGenerationID_Object = MibTableColumn
ruijiePimInterfaceGenerationID = _RuijiePimInterfaceGenerationID_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 14),
    _RuijiePimInterfaceGenerationID_Type()
)
ruijiePimInterfaceGenerationID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceGenerationID.setStatus("current")


class _RuijiePimInterfaceJoinPruneHoldtime_Type(Integer32):
    """Custom type ruijiePimInterfaceJoinPruneHoldtime based on Integer32"""
    defaultValue = 210

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RuijiePimInterfaceJoinPruneHoldtime_Type.__name__ = "Integer32"
_RuijiePimInterfaceJoinPruneHoldtime_Object = MibTableColumn
ruijiePimInterfaceJoinPruneHoldtime = _RuijiePimInterfaceJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 15),
    _RuijiePimInterfaceJoinPruneHoldtime_Type()
)
ruijiePimInterfaceJoinPruneHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfaceJoinPruneHoldtime.setUnits("seconds")


class _RuijiePimInterfaceGraftRetryInterval_Type(Integer32):
    """Custom type ruijiePimInterfaceGraftRetryInterval based on Integer32"""
    defaultValue = 3


_RuijiePimInterfaceGraftRetryInterval_Type.__name__ = "Integer32"
_RuijiePimInterfaceGraftRetryInterval_Object = MibTableColumn
ruijiePimInterfaceGraftRetryInterval = _RuijiePimInterfaceGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 16),
    _RuijiePimInterfaceGraftRetryInterval_Type()
)
ruijiePimInterfaceGraftRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimInterfaceGraftRetryInterval.setUnits("seconds")


class _RuijiePimInterfaceMaxGraftRetries_Type(Integer32):
    """Custom type ruijiePimInterfaceMaxGraftRetries based on Integer32"""
    defaultValue = 2


_RuijiePimInterfaceMaxGraftRetries_Type.__name__ = "Integer32"
_RuijiePimInterfaceMaxGraftRetries_Object = MibTableColumn
ruijiePimInterfaceMaxGraftRetries = _RuijiePimInterfaceMaxGraftRetries_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 17),
    _RuijiePimInterfaceMaxGraftRetries_Type()
)
ruijiePimInterfaceMaxGraftRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceMaxGraftRetries.setStatus("current")


class _RuijiePimInterfaceSRTTLThreshold_Type(Integer32):
    """Custom type ruijiePimInterfaceSRTTLThreshold based on Integer32"""
    defaultValue = 0


_RuijiePimInterfaceSRTTLThreshold_Type.__name__ = "Integer32"
_RuijiePimInterfaceSRTTLThreshold_Object = MibTableColumn
ruijiePimInterfaceSRTTLThreshold = _RuijiePimInterfaceSRTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 18),
    _RuijiePimInterfaceSRTTLThreshold_Type()
)
ruijiePimInterfaceSRTTLThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceSRTTLThreshold.setStatus("current")
_RuijiePimInterfaceLanDelayEnabled_Type = TruthValue
_RuijiePimInterfaceLanDelayEnabled_Object = MibTableColumn
ruijiePimInterfaceLanDelayEnabled = _RuijiePimInterfaceLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 19),
    _RuijiePimInterfaceLanDelayEnabled_Type()
)
ruijiePimInterfaceLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceLanDelayEnabled.setStatus("current")
_RuijiePimInterfaceSRCapable_Type = TruthValue
_RuijiePimInterfaceSRCapable_Object = MibTableColumn
ruijiePimInterfaceSRCapable = _RuijiePimInterfaceSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 20),
    _RuijiePimInterfaceSRCapable_Type()
)
ruijiePimInterfaceSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceSRCapable.setStatus("current")


class _RuijiePimInterfaceDRPriority_Type(Integer32):
    """Custom type ruijiePimInterfaceDRPriority based on Integer32"""
    defaultValue = 1


_RuijiePimInterfaceDRPriority_Type.__name__ = "Integer32"
_RuijiePimInterfaceDRPriority_Object = MibTableColumn
ruijiePimInterfaceDRPriority = _RuijiePimInterfaceDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 21),
    _RuijiePimInterfaceDRPriority_Type()
)
ruijiePimInterfaceDRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceDRPriority.setStatus("current")
_RuijiePimInterfaceNbrCounter_Type = Integer32
_RuijiePimInterfaceNbrCounter_Object = MibTableColumn
ruijiePimInterfaceNbrCounter = _RuijiePimInterfaceNbrCounter_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 22),
    _RuijiePimInterfaceNbrCounter_Type()
)
ruijiePimInterfaceNbrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceNbrCounter.setStatus("current")


class _RuijiePimInterfaceBsrBorderEnabled_Type(EnabledStatus):
    """Custom type ruijiePimInterfaceBsrBorderEnabled based on EnabledStatus"""
    defaultValue = 2


_RuijiePimInterfaceBsrBorderEnabled_Type.__name__ = "EnabledStatus"
_RuijiePimInterfaceBsrBorderEnabled_Object = MibTableColumn
ruijiePimInterfaceBsrBorderEnabled = _RuijiePimInterfaceBsrBorderEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 23),
    _RuijiePimInterfaceBsrBorderEnabled_Type()
)
ruijiePimInterfaceBsrBorderEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceBsrBorderEnabled.setStatus("current")
_RuijiePimInterfaceCountIn_Type = Integer32
_RuijiePimInterfaceCountIn_Object = MibTableColumn
ruijiePimInterfaceCountIn = _RuijiePimInterfaceCountIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 24),
    _RuijiePimInterfaceCountIn_Type()
)
ruijiePimInterfaceCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceCountIn.setStatus("current")
_RuijiePimInterfaceCountOut_Type = Integer32
_RuijiePimInterfaceCountOut_Object = MibTableColumn
ruijiePimInterfaceCountOut = _RuijiePimInterfaceCountOut_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 25),
    _RuijiePimInterfaceCountOut_Type()
)
ruijiePimInterfaceCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimInterfaceCountOut.setStatus("current")


class _RuijiePimInterfaceEnabled_Type(EnabledStatus):
    """Custom type ruijiePimInterfaceEnabled based on EnabledStatus"""
    defaultValue = 2


_RuijiePimInterfaceEnabled_Type.__name__ = "EnabledStatus"
_RuijiePimInterfaceEnabled_Object = MibTableColumn
ruijiePimInterfaceEnabled = _RuijiePimInterfaceEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 26),
    _RuijiePimInterfaceEnabled_Type()
)
ruijiePimInterfaceEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimInterfaceEnabled.setStatus("current")


class _RuijiePimNeighborFilterAcl_Type(DisplayString):
    """Custom type ruijiePimNeighborFilterAcl based on DisplayString"""
    defaultValue = OctetString("")


_RuijiePimNeighborFilterAcl_Type.__name__ = "DisplayString"
_RuijiePimNeighborFilterAcl_Object = MibTableColumn
ruijiePimNeighborFilterAcl = _RuijiePimNeighborFilterAcl_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 27),
    _RuijiePimNeighborFilterAcl_Type()
)
ruijiePimNeighborFilterAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimNeighborFilterAcl.setStatus("current")


class _RuijiePimDrSupportAddressBound_Type(DisplayString):
    """Custom type ruijiePimDrSupportAddressBound based on DisplayString"""
    defaultValue = OctetString("")


_RuijiePimDrSupportAddressBound_Type.__name__ = "DisplayString"
_RuijiePimDrSupportAddressBound_Object = MibTableColumn
ruijiePimDrSupportAddressBound = _RuijiePimDrSupportAddressBound_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 2, 1, 28),
    _RuijiePimDrSupportAddressBound_Type()
)
ruijiePimDrSupportAddressBound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimDrSupportAddressBound.setStatus("current")
_RuijiePimNeighborTable_Object = MibTable
ruijiePimNeighborTable = _RuijiePimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruijiePimNeighborTable.setStatus("current")
_RuijiePimNeighborEntry_Object = MibTableRow
ruijiePimNeighborEntry = _RuijiePimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1)
)
ruijiePimNeighborEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimNeighborAddress"),
)
if mibBuilder.loadTexts:
    ruijiePimNeighborEntry.setStatus("current")
_RuijiePimNeighborAddress_Type = IpAddress
_RuijiePimNeighborAddress_Object = MibTableColumn
ruijiePimNeighborAddress = _RuijiePimNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 1),
    _RuijiePimNeighborAddress_Type()
)
ruijiePimNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimNeighborAddress.setStatus("current")
_RuijiePimNeighborIfIndex_Type = InterfaceIndex
_RuijiePimNeighborIfIndex_Object = MibTableColumn
ruijiePimNeighborIfIndex = _RuijiePimNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 2),
    _RuijiePimNeighborIfIndex_Type()
)
ruijiePimNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborIfIndex.setStatus("current")
_RuijiePimNeighborUpTime_Type = TimeTicks
_RuijiePimNeighborUpTime_Object = MibTableColumn
ruijiePimNeighborUpTime = _RuijiePimNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 3),
    _RuijiePimNeighborUpTime_Type()
)
ruijiePimNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborUpTime.setStatus("current")
_RuijiePimNeighborExpiryTime_Type = TimeTicks
_RuijiePimNeighborExpiryTime_Object = MibTableColumn
ruijiePimNeighborExpiryTime = _RuijiePimNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 4),
    _RuijiePimNeighborExpiryTime_Type()
)
ruijiePimNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborExpiryTime.setStatus("current")


class _RuijiePimNeighborMode_Type(Integer32):
    """Custom type ruijiePimNeighborMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dense", 1),
          ("sparse", 2))
    )


_RuijiePimNeighborMode_Type.__name__ = "Integer32"
_RuijiePimNeighborMode_Object = MibTableColumn
ruijiePimNeighborMode = _RuijiePimNeighborMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 5),
    _RuijiePimNeighborMode_Type()
)
ruijiePimNeighborMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborMode.setStatus("deprecated")
_RuijiePimNeighborLanPruneDelay_Type = Integer32
_RuijiePimNeighborLanPruneDelay_Object = MibTableColumn
ruijiePimNeighborLanPruneDelay = _RuijiePimNeighborLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 6),
    _RuijiePimNeighborLanPruneDelay_Type()
)
ruijiePimNeighborLanPruneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborLanPruneDelay.setStatus("current")
_RuijiePimNeighborOverrideInterval_Type = Integer32
_RuijiePimNeighborOverrideInterval_Object = MibTableColumn
ruijiePimNeighborOverrideInterval = _RuijiePimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 7),
    _RuijiePimNeighborOverrideInterval_Type()
)
ruijiePimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborOverrideInterval.setStatus("current")
_RuijiePimNeighborTBit_Type = Integer32
_RuijiePimNeighborTBit_Object = MibTableColumn
ruijiePimNeighborTBit = _RuijiePimNeighborTBit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 8),
    _RuijiePimNeighborTBit_Type()
)
ruijiePimNeighborTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborTBit.setStatus("current")
_RuijiePimNeighborSRCapable_Type = TruthValue
_RuijiePimNeighborSRCapable_Object = MibTableColumn
ruijiePimNeighborSRCapable = _RuijiePimNeighborSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 9),
    _RuijiePimNeighborSRCapable_Type()
)
ruijiePimNeighborSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborSRCapable.setStatus("current")
_RuijiePimNeighborDRPresent_Type = TruthValue
_RuijiePimNeighborDRPresent_Object = MibTableColumn
ruijiePimNeighborDRPresent = _RuijiePimNeighborDRPresent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 3, 1, 10),
    _RuijiePimNeighborDRPresent_Type()
)
ruijiePimNeighborDRPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimNeighborDRPresent.setStatus("current")
_RuijiePimIpMRouteTable_Object = MibTable
ruijiePimIpMRouteTable = _RuijiePimIpMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruijiePimIpMRouteTable.setStatus("current")
_RuijiePimIpMRouteEntry_Object = MibTableRow
ruijiePimIpMRouteEntry = _RuijiePimIpMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1)
)
ruijiePimIpMRouteEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteSourceMask"),
)
if mibBuilder.loadTexts:
    ruijiePimIpMRouteEntry.setStatus("current")
_RuijiePimIpMRouteUpstreamAssertTimer_Type = TimeTicks
_RuijiePimIpMRouteUpstreamAssertTimer_Object = MibTableColumn
ruijiePimIpMRouteUpstreamAssertTimer = _RuijiePimIpMRouteUpstreamAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 1),
    _RuijiePimIpMRouteUpstreamAssertTimer_Type()
)
ruijiePimIpMRouteUpstreamAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteUpstreamAssertTimer.setStatus("current")
_RuijiePimIpMRouteAssertMetric_Type = Integer32
_RuijiePimIpMRouteAssertMetric_Object = MibTableColumn
ruijiePimIpMRouteAssertMetric = _RuijiePimIpMRouteAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 2),
    _RuijiePimIpMRouteAssertMetric_Type()
)
ruijiePimIpMRouteAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteAssertMetric.setStatus("current")
_RuijiePimIpMRouteAssertMetricPref_Type = Integer32
_RuijiePimIpMRouteAssertMetricPref_Object = MibTableColumn
ruijiePimIpMRouteAssertMetricPref = _RuijiePimIpMRouteAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 3),
    _RuijiePimIpMRouteAssertMetricPref_Type()
)
ruijiePimIpMRouteAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteAssertMetricPref.setStatus("current")
_RuijiePimIpMRouteAssertRPTBit_Type = TruthValue
_RuijiePimIpMRouteAssertRPTBit_Object = MibTableColumn
ruijiePimIpMRouteAssertRPTBit = _RuijiePimIpMRouteAssertRPTBit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 4),
    _RuijiePimIpMRouteAssertRPTBit_Type()
)
ruijiePimIpMRouteAssertRPTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteAssertRPTBit.setStatus("current")


class _RuijiePimIpMRouteFlags_Type(Integer32):
    """Custom type ruijiePimIpMRouteFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rpt", 0),
          ("spt", 1))
    )


_RuijiePimIpMRouteFlags_Type.__name__ = "Integer32"
_RuijiePimIpMRouteFlags_Object = MibTableColumn
ruijiePimIpMRouteFlags = _RuijiePimIpMRouteFlags_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 5),
    _RuijiePimIpMRouteFlags_Type()
)
ruijiePimIpMRouteFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteFlags.setStatus("current")
_RuijiePimIpMRouteRPFNeighbor_Type = IpAddress
_RuijiePimIpMRouteRPFNeighbor_Object = MibTableColumn
ruijiePimIpMRouteRPFNeighbor = _RuijiePimIpMRouteRPFNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 6),
    _RuijiePimIpMRouteRPFNeighbor_Type()
)
ruijiePimIpMRouteRPFNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteRPFNeighbor.setStatus("current")
_RuijiePimIpMRouteSourceTimer_Type = TimeTicks
_RuijiePimIpMRouteSourceTimer_Object = MibTableColumn
ruijiePimIpMRouteSourceTimer = _RuijiePimIpMRouteSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 7),
    _RuijiePimIpMRouteSourceTimer_Type()
)
ruijiePimIpMRouteSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteSourceTimer.setStatus("current")
_RuijiePimIpMRouteOriginatorSRTTL_Type = Integer32
_RuijiePimIpMRouteOriginatorSRTTL_Object = MibTableColumn
ruijiePimIpMRouteOriginatorSRTTL = _RuijiePimIpMRouteOriginatorSRTTL_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 4, 1, 8),
    _RuijiePimIpMRouteOriginatorSRTTL_Type()
)
ruijiePimIpMRouteOriginatorSRTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteOriginatorSRTTL.setStatus("current")
_RuijiePimIpMRouteNextHopTable_Object = MibTable
ruijiePimIpMRouteNextHopTable = _RuijiePimIpMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopTable.setStatus("current")
_RuijiePimIpMRouteNextHopEntry_Object = MibTableRow
ruijiePimIpMRouteNextHopEntry = _RuijiePimIpMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1)
)
ruijiePimIpMRouteNextHopEntry.setIndexNames(
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopGroup"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSource"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopSourceMask"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopIfIndex"),
    (0, "IPMROUTE-STD-MIB", "ipMRouteNextHopAddress"),
)
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopEntry.setStatus("current")


class _RuijiePimIpMRouteNextHopPruneReason_Type(Integer32):
    """Custom type ruijiePimIpMRouteNextHopPruneReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("prune", 2),
          ("assert", 3))
    )


_RuijiePimIpMRouteNextHopPruneReason_Type.__name__ = "Integer32"
_RuijiePimIpMRouteNextHopPruneReason_Object = MibTableColumn
ruijiePimIpMRouteNextHopPruneReason = _RuijiePimIpMRouteNextHopPruneReason_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1, 1),
    _RuijiePimIpMRouteNextHopPruneReason_Type()
)
ruijiePimIpMRouteNextHopPruneReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopPruneReason.setStatus("current")
_RuijiePimIpMRouteNextHopAssertWinner_Type = IpAddress
_RuijiePimIpMRouteNextHopAssertWinner_Object = MibTableColumn
ruijiePimIpMRouteNextHopAssertWinner = _RuijiePimIpMRouteNextHopAssertWinner_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1, 2),
    _RuijiePimIpMRouteNextHopAssertWinner_Type()
)
ruijiePimIpMRouteNextHopAssertWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopAssertWinner.setStatus("current")
_RuijiePimIpMRouteNextHopAssertTimer_Type = TimeTicks
_RuijiePimIpMRouteNextHopAssertTimer_Object = MibTableColumn
ruijiePimIpMRouteNextHopAssertTimer = _RuijiePimIpMRouteNextHopAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1, 3),
    _RuijiePimIpMRouteNextHopAssertTimer_Type()
)
ruijiePimIpMRouteNextHopAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopAssertTimer.setStatus("current")
_RuijiePimIpMRouteNextHopAssertMetric_Type = Integer32
_RuijiePimIpMRouteNextHopAssertMetric_Object = MibTableColumn
ruijiePimIpMRouteNextHopAssertMetric = _RuijiePimIpMRouteNextHopAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1, 4),
    _RuijiePimIpMRouteNextHopAssertMetric_Type()
)
ruijiePimIpMRouteNextHopAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopAssertMetric.setStatus("current")
_RuijiePimIpMRouteNextHopAssertMetricPref_Type = Integer32
_RuijiePimIpMRouteNextHopAssertMetricPref_Object = MibTableColumn
ruijiePimIpMRouteNextHopAssertMetricPref = _RuijiePimIpMRouteNextHopAssertMetricPref_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1, 5),
    _RuijiePimIpMRouteNextHopAssertMetricPref_Type()
)
ruijiePimIpMRouteNextHopAssertMetricPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopAssertMetricPref.setStatus("current")
_RuijiePimIpMRouteNextHopJoinPruneTimer_Type = TimeTicks
_RuijiePimIpMRouteNextHopJoinPruneTimer_Object = MibTableColumn
ruijiePimIpMRouteNextHopJoinPruneTimer = _RuijiePimIpMRouteNextHopJoinPruneTimer_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 5, 1, 6),
    _RuijiePimIpMRouteNextHopJoinPruneTimer_Type()
)
ruijiePimIpMRouteNextHopJoinPruneTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimIpMRouteNextHopJoinPruneTimer.setStatus("current")
_RuijiePimRPSetTable_Object = MibTable
ruijiePimRPSetTable = _RuijiePimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ruijiePimRPSetTable.setStatus("current")
_RuijiePimRPSetEntry_Object = MibTableRow
ruijiePimRPSetEntry = _RuijiePimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1)
)
ruijiePimRPSetEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimRPSetComponent"),
    (0, "RUIJIE-PIM-MIB", "ruijiePimRPSetGroupAddress"),
    (0, "RUIJIE-PIM-MIB", "ruijiePimRPSetGroupMask"),
    (0, "RUIJIE-PIM-MIB", "ruijiePimRPSetAddress"),
)
if mibBuilder.loadTexts:
    ruijiePimRPSetEntry.setStatus("current")
_RuijiePimRPSetGroupAddress_Type = IpAddress
_RuijiePimRPSetGroupAddress_Object = MibTableColumn
ruijiePimRPSetGroupAddress = _RuijiePimRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 1),
    _RuijiePimRPSetGroupAddress_Type()
)
ruijiePimRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimRPSetGroupAddress.setStatus("current")
_RuijiePimRPSetGroupMask_Type = IpAddress
_RuijiePimRPSetGroupMask_Object = MibTableColumn
ruijiePimRPSetGroupMask = _RuijiePimRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 2),
    _RuijiePimRPSetGroupMask_Type()
)
ruijiePimRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimRPSetGroupMask.setStatus("current")
_RuijiePimRPSetAddress_Type = IpAddress
_RuijiePimRPSetAddress_Object = MibTableColumn
ruijiePimRPSetAddress = _RuijiePimRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 3),
    _RuijiePimRPSetAddress_Type()
)
ruijiePimRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimRPSetAddress.setStatus("current")


class _RuijiePimRPSetHoldTime_Type(Integer32):
    """Custom type ruijiePimRPSetHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijiePimRPSetHoldTime_Type.__name__ = "Integer32"
_RuijiePimRPSetHoldTime_Object = MibTableColumn
ruijiePimRPSetHoldTime = _RuijiePimRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 4),
    _RuijiePimRPSetHoldTime_Type()
)
ruijiePimRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimRPSetHoldTime.setUnits("seconds")
_RuijiePimRPSetExpiryTime_Type = TimeTicks
_RuijiePimRPSetExpiryTime_Object = MibTableColumn
ruijiePimRPSetExpiryTime = _RuijiePimRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 5),
    _RuijiePimRPSetExpiryTime_Type()
)
ruijiePimRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimRPSetExpiryTime.setStatus("current")


class _RuijiePimRPSetComponent_Type(Integer32):
    """Custom type ruijiePimRPSetComponent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijiePimRPSetComponent_Type.__name__ = "Integer32"
_RuijiePimRPSetComponent_Object = MibTableColumn
ruijiePimRPSetComponent = _RuijiePimRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 6),
    _RuijiePimRPSetComponent_Type()
)
ruijiePimRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimRPSetComponent.setStatus("current")
_RuijiePimRPSetUpTime_Type = TimeTicks
_RuijiePimRPSetUpTime_Object = MibTableColumn
ruijiePimRPSetUpTime = _RuijiePimRPSetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 6, 1, 7),
    _RuijiePimRPSetUpTime_Type()
)
ruijiePimRPSetUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimRPSetUpTime.setStatus("current")
_RuijiePimComponentTable_Object = MibTable
ruijiePimComponentTable = _RuijiePimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7)
)
if mibBuilder.loadTexts:
    ruijiePimComponentTable.setStatus("current")
_RuijiePimComponentEntry_Object = MibTableRow
ruijiePimComponentEntry = _RuijiePimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1)
)
ruijiePimComponentEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimComponentIndex"),
)
if mibBuilder.loadTexts:
    ruijiePimComponentEntry.setStatus("current")


class _RuijiePimComponentIndex_Type(Integer32):
    """Custom type ruijiePimComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijiePimComponentIndex_Type.__name__ = "Integer32"
_RuijiePimComponentIndex_Object = MibTableColumn
ruijiePimComponentIndex = _RuijiePimComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 1),
    _RuijiePimComponentIndex_Type()
)
ruijiePimComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimComponentIndex.setStatus("current")
_RuijiePimComponentBSRAddress_Type = IpAddress
_RuijiePimComponentBSRAddress_Object = MibTableColumn
ruijiePimComponentBSRAddress = _RuijiePimComponentBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 2),
    _RuijiePimComponentBSRAddress_Type()
)
ruijiePimComponentBSRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentBSRAddress.setStatus("current")
_RuijiePimComponentBSRExpiryTime_Type = TimeTicks
_RuijiePimComponentBSRExpiryTime_Object = MibTableColumn
ruijiePimComponentBSRExpiryTime = _RuijiePimComponentBSRExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 3),
    _RuijiePimComponentBSRExpiryTime_Type()
)
ruijiePimComponentBSRExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentBSRExpiryTime.setStatus("current")


class _RuijiePimComponentCRPHoldTime_Type(Integer32):
    """Custom type ruijiePimComponentCRPHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijiePimComponentCRPHoldTime_Type.__name__ = "Integer32"
_RuijiePimComponentCRPHoldTime_Object = MibTableColumn
ruijiePimComponentCRPHoldTime = _RuijiePimComponentCRPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 4),
    _RuijiePimComponentCRPHoldTime_Type()
)
ruijiePimComponentCRPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePimComponentCRPHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimComponentCRPHoldTime.setUnits("seconds")
_RuijiePimComponentBSRUptime_Type = TimeTicks
_RuijiePimComponentBSRUptime_Object = MibTableColumn
ruijiePimComponentBSRUptime = _RuijiePimComponentBSRUptime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 5),
    _RuijiePimComponentBSRUptime_Type()
)
ruijiePimComponentBSRUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentBSRUptime.setStatus("current")
_RuijiePimComponentBSRPriority_Type = Integer32
_RuijiePimComponentBSRPriority_Object = MibTableColumn
ruijiePimComponentBSRPriority = _RuijiePimComponentBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 6),
    _RuijiePimComponentBSRPriority_Type()
)
ruijiePimComponentBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentBSRPriority.setStatus("current")
_RuijiePimComponentBSRHashMaskLength_Type = Integer32
_RuijiePimComponentBSRHashMaskLength_Object = MibTableColumn
ruijiePimComponentBSRHashMaskLength = _RuijiePimComponentBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 7),
    _RuijiePimComponentBSRHashMaskLength_Type()
)
ruijiePimComponentBSRHashMaskLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentBSRHashMaskLength.setStatus("current")
_RuijiePimComponentBSRNextBsrMessage_Type = TimeTicks
_RuijiePimComponentBSRNextBsrMessage_Object = MibTableColumn
ruijiePimComponentBSRNextBsrMessage = _RuijiePimComponentBSRNextBsrMessage_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 8),
    _RuijiePimComponentBSRNextBsrMessage_Type()
)
ruijiePimComponentBSRNextBsrMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentBSRNextBsrMessage.setStatus("current")
_RuijiePimComponentNextCandRPAdv_Type = TimeTicks
_RuijiePimComponentNextCandRPAdv_Object = MibTableColumn
ruijiePimComponentNextCandRPAdv = _RuijiePimComponentNextCandRPAdv_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 7, 1, 9),
    _RuijiePimComponentNextCandRPAdv_Type()
)
ruijiePimComponentNextCandRPAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimComponentNextCandRPAdv.setStatus("current")


class _RuijiePimSourceLifetime_Type(Integer32):
    """Custom type ruijiePimSourceLifetime based on Integer32"""
    defaultValue = 2100


_RuijiePimSourceLifetime_Type.__name__ = "Integer32"
_RuijiePimSourceLifetime_Object = MibScalar
ruijiePimSourceLifetime = _RuijiePimSourceLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 8),
    _RuijiePimSourceLifetime_Type()
)
ruijiePimSourceLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimSourceLifetime.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimSourceLifetime.setUnits("seconds")


class _RuijiePimStateRefreshInterval_Type(Integer32):
    """Custom type ruijiePimStateRefreshInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuijiePimStateRefreshInterval_Type.__name__ = "Integer32"
_RuijiePimStateRefreshInterval_Object = MibScalar
ruijiePimStateRefreshInterval = _RuijiePimStateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 9),
    _RuijiePimStateRefreshInterval_Type()
)
ruijiePimStateRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimStateRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    ruijiePimStateRefreshInterval.setUnits("seconds")


class _RuijiePimStateRefreshLimitInterval_Type(Integer32):
    """Custom type ruijiePimStateRefreshLimitInterval based on Integer32"""
    defaultValue = 0


_RuijiePimStateRefreshLimitInterval_Type.__name__ = "Integer32"
_RuijiePimStateRefreshLimitInterval_Object = MibScalar
ruijiePimStateRefreshLimitInterval = _RuijiePimStateRefreshLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 10),
    _RuijiePimStateRefreshLimitInterval_Type()
)
ruijiePimStateRefreshLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimStateRefreshLimitInterval.setStatus("current")


class _RuijiePimStateRefreshTimeToLive_Type(Integer32):
    """Custom type ruijiePimStateRefreshTimeToLive based on Integer32"""
    defaultValue = 16


_RuijiePimStateRefreshTimeToLive_Type.__name__ = "Integer32"
_RuijiePimStateRefreshTimeToLive_Object = MibScalar
ruijiePimStateRefreshTimeToLive = _RuijiePimStateRefreshTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 11),
    _RuijiePimStateRefreshTimeToLive_Type()
)
ruijiePimStateRefreshTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimStateRefreshTimeToLive.setStatus("current")
_RuijiePimBsrCandidateGroup_ObjectIdentity = ObjectIdentity
ruijiePimBsrCandidateGroup = _RuijiePimBsrCandidateGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 12)
)
_RuijiePimBsrCandidateIfindex_Type = Integer32
_RuijiePimBsrCandidateIfindex_Object = MibScalar
ruijiePimBsrCandidateIfindex = _RuijiePimBsrCandidateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 12, 1),
    _RuijiePimBsrCandidateIfindex_Type()
)
ruijiePimBsrCandidateIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimBsrCandidateIfindex.setStatus("current")


class _RuijiePimBsrCandidateHashMaskLength_Type(Integer32):
    """Custom type ruijiePimBsrCandidateHashMaskLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuijiePimBsrCandidateHashMaskLength_Type.__name__ = "Integer32"
_RuijiePimBsrCandidateHashMaskLength_Object = MibScalar
ruijiePimBsrCandidateHashMaskLength = _RuijiePimBsrCandidateHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 12, 2),
    _RuijiePimBsrCandidateHashMaskLength_Type()
)
ruijiePimBsrCandidateHashMaskLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimBsrCandidateHashMaskLength.setStatus("current")


class _RuijiePimBsrCandidatePriority_Type(Integer32):
    """Custom type ruijiePimBsrCandidatePriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RuijiePimBsrCandidatePriority_Type.__name__ = "Integer32"
_RuijiePimBsrCandidatePriority_Object = MibScalar
ruijiePimBsrCandidatePriority = _RuijiePimBsrCandidatePriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 12, 3),
    _RuijiePimBsrCandidatePriority_Type()
)
ruijiePimBsrCandidatePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruijiePimBsrCandidatePriority.setStatus("current")
_RuijiePimRPTable_Object = MibTable
ruijiePimRPTable = _RuijiePimRPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 13)
)
if mibBuilder.loadTexts:
    ruijiePimRPTable.setStatus("current")
_RuijiePimRPEntry_Object = MibTableRow
ruijiePimRPEntry = _RuijiePimRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 13, 1)
)
ruijiePimRPEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimRPGroupAddress"),
)
if mibBuilder.loadTexts:
    ruijiePimRPEntry.setStatus("current")
_RuijiePimRPGroupAddress_Type = IpAddress
_RuijiePimRPGroupAddress_Object = MibTableColumn
ruijiePimRPGroupAddress = _RuijiePimRPGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 13, 1, 1),
    _RuijiePimRPGroupAddress_Type()
)
ruijiePimRPGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimRPGroupAddress.setStatus("current")
_RuijiePimRPAddress_Type = IpAddress
_RuijiePimRPAddress_Object = MibTableColumn
ruijiePimRPAddress = _RuijiePimRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 13, 1, 2),
    _RuijiePimRPAddress_Type()
)
ruijiePimRPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimRPAddress.setStatus("current")
_RuijiePimRPExpiryTime_Type = TimeTicks
_RuijiePimRPExpiryTime_Object = MibTableColumn
ruijiePimRPExpiryTime = _RuijiePimRPExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 13, 1, 3),
    _RuijiePimRPExpiryTime_Type()
)
ruijiePimRPExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimRPExpiryTime.setStatus("current")
_RuijiePimRPNextRPReachableIn_Type = TimeTicks
_RuijiePimRPNextRPReachableIn_Object = MibTableColumn
ruijiePimRPNextRPReachableIn = _RuijiePimRPNextRPReachableIn_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 13, 1, 4),
    _RuijiePimRPNextRPReachableIn_Type()
)
ruijiePimRPNextRPReachableIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijiePimRPNextRPReachableIn.setStatus("current")
_RuijiePimStaticRPTable_Object = MibTable
ruijiePimStaticRPTable = _RuijiePimStaticRPTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 14)
)
if mibBuilder.loadTexts:
    ruijiePimStaticRPTable.setStatus("current")
_RuijiePimStaticRPEntry_Object = MibTableRow
ruijiePimStaticRPEntry = _RuijiePimStaticRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 14, 1)
)
ruijiePimStaticRPEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimStaticRPAddress"),
)
if mibBuilder.loadTexts:
    ruijiePimStaticRPEntry.setStatus("current")
_RuijiePimStaticRPAddress_Type = IpAddress
_RuijiePimStaticRPAddress_Object = MibTableColumn
ruijiePimStaticRPAddress = _RuijiePimStaticRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 14, 1, 1),
    _RuijiePimStaticRPAddress_Type()
)
ruijiePimStaticRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimStaticRPAddress.setStatus("current")


class _RuijiePimStaticRPAddressIsOverride_Type(EnabledStatus):
    """Custom type ruijiePimStaticRPAddressIsOverride based on EnabledStatus"""
    defaultValue = 2


_RuijiePimStaticRPAddressIsOverride_Type.__name__ = "EnabledStatus"
_RuijiePimStaticRPAddressIsOverride_Object = MibTableColumn
ruijiePimStaticRPAddressIsOverride = _RuijiePimStaticRPAddressIsOverride_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 14, 1, 2),
    _RuijiePimStaticRPAddressIsOverride_Type()
)
ruijiePimStaticRPAddressIsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePimStaticRPAddressIsOverride.setStatus("current")


class _RuijiePimStaticRPAclName_Type(DisplayString):
    """Custom type ruijiePimStaticRPAclName based on DisplayString"""
    defaultValue = OctetString("")


_RuijiePimStaticRPAclName_Type.__name__ = "DisplayString"
_RuijiePimStaticRPAclName_Object = MibTableColumn
ruijiePimStaticRPAclName = _RuijiePimStaticRPAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 14, 1, 3),
    _RuijiePimStaticRPAclName_Type()
)
ruijiePimStaticRPAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePimStaticRPAclName.setStatus("current")
_RuijiePimStaticRPStatus_Type = RowStatus
_RuijiePimStaticRPStatus_Object = MibTableColumn
ruijiePimStaticRPStatus = _RuijiePimStaticRPStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 14, 1, 4),
    _RuijiePimStaticRPStatus_Type()
)
ruijiePimStaticRPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePimStaticRPStatus.setStatus("current")
_RuijiePimRpCandidateTable_Object = MibTable
ruijiePimRpCandidateTable = _RuijiePimRpCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 15)
)
if mibBuilder.loadTexts:
    ruijiePimRpCandidateTable.setStatus("current")
_RuijiePimRpCandidateEntry_Object = MibTableRow
ruijiePimRpCandidateEntry = _RuijiePimRpCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 15, 1)
)
ruijiePimRpCandidateEntry.setIndexNames(
    (0, "RUIJIE-PIM-MIB", "ruijiePimRpCandidateIfindex"),
)
if mibBuilder.loadTexts:
    ruijiePimRpCandidateEntry.setStatus("current")
_RuijiePimRpCandidateIfindex_Type = InterfaceIndex
_RuijiePimRpCandidateIfindex_Object = MibTableColumn
ruijiePimRpCandidateIfindex = _RuijiePimRpCandidateIfindex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 15, 1, 1),
    _RuijiePimRpCandidateIfindex_Type()
)
ruijiePimRpCandidateIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruijiePimRpCandidateIfindex.setStatus("current")


class _RuijiePimRpCandidateAclName_Type(DisplayString):
    """Custom type ruijiePimRpCandidateAclName based on DisplayString"""
    defaultValue = OctetString("")


_RuijiePimRpCandidateAclName_Type.__name__ = "DisplayString"
_RuijiePimRpCandidateAclName_Object = MibTableColumn
ruijiePimRpCandidateAclName = _RuijiePimRpCandidateAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 15, 1, 2),
    _RuijiePimRpCandidateAclName_Type()
)
ruijiePimRpCandidateAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePimRpCandidateAclName.setStatus("current")
_RuijiePimRpCandidateStatus_Type = RowStatus
_RuijiePimRpCandidateStatus_Object = MibTableColumn
ruijiePimRpCandidateStatus = _RuijiePimRpCandidateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 1, 15, 1, 3),
    _RuijiePimRpCandidateStatus_Type()
)
ruijiePimRpCandidateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruijiePimRpCandidateStatus.setStatus("current")
_RuijiePimTraps_ObjectIdentity = ObjectIdentity
ruijiePimTraps = _RuijiePimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 2)
)
_RuijiePimMIBConformance_ObjectIdentity = ObjectIdentity
ruijiePimMIBConformance = _RuijiePimMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 2)
)
_RuijiePimMIBCompliances_ObjectIdentity = ObjectIdentity
ruijiePimMIBCompliances = _RuijiePimMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 2, 1)
)
_RuijiePimMIBGroups_ObjectIdentity = ObjectIdentity
ruijiePimMIBGroups = _RuijiePimMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 2, 2)
)

# Managed Objects groups

ruijiePimMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 2, 2, 1)
)
ruijiePimMIBGroup.setObjects(
      *(("RUIJIE-PIM-MIB", "ruijiePimJoinPruneInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceAddress"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceNetMask"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceMode"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceDR"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceHelloInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceJoinPruneInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceCBSRPreference"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceTrigHelloInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceHelloHoldtime"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceLanPruneDelay"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfacePropagationDelay"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceOverrideInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceGenerationID"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceJoinPruneHoldtime"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceGraftRetryInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceMaxGraftRetries"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceSRTTLThreshold"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceLanDelayEnabled"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceSRCapable"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceDRPriority"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceNbrCounter"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceBsrBorderEnabled"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceCountIn"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceCountOut"),
        ("RUIJIE-PIM-MIB", "ruijiePimInterfaceEnabled"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborFilterAcl"),
        ("RUIJIE-PIM-MIB", "ruijiePimDrSupportAddressBound"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborIfIndex"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborUpTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborExpiryTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborMode"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborLanPruneDelay"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborOverrideInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborTBit"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborSRCapable"),
        ("RUIJIE-PIM-MIB", "ruijiePimNeighborDRPresent"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteUpstreamAssertTimer"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteAssertMetric"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteAssertMetricPref"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteAssertRPTBit"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteFlags"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteRPFNeighbor"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteSourceTimer"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteOriginatorSRTTL"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteNextHopPruneReason"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteNextHopAssertWinner"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteNextHopAssertTimer"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteNextHopAssertMetric"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteNextHopAssertMetricPref"),
        ("RUIJIE-PIM-MIB", "ruijiePimIpMRouteNextHopJoinPruneTimer"),
        ("RUIJIE-PIM-MIB", "ruijiePimRPSetHoldTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimRPSetExpiryTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimRPSetUpTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentBSRAddress"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentBSRExpiryTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentCRPHoldTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentBSRUptime"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentBSRPriority"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentBSRHashMaskLength"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentBSRNextBsrMessage"),
        ("RUIJIE-PIM-MIB", "ruijiePimComponentNextCandRPAdv"),
        ("RUIJIE-PIM-MIB", "ruijiePimSourceLifetime"),
        ("RUIJIE-PIM-MIB", "ruijiePimStateRefreshInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimStateRefreshLimitInterval"),
        ("RUIJIE-PIM-MIB", "ruijiePimStateRefreshTimeToLive"),
        ("RUIJIE-PIM-MIB", "ruijiePimBsrCandidateIfindex"),
        ("RUIJIE-PIM-MIB", "ruijiePimBsrCandidateHashMaskLength"),
        ("RUIJIE-PIM-MIB", "ruijiePimBsrCandidatePriority"),
        ("RUIJIE-PIM-MIB", "ruijiePimRPAddress"),
        ("RUIJIE-PIM-MIB", "ruijiePimRPExpiryTime"),
        ("RUIJIE-PIM-MIB", "ruijiePimRPNextRPReachableIn"),
        ("RUIJIE-PIM-MIB", "ruijiePimStaticRPAddressIsOverride"),
        ("RUIJIE-PIM-MIB", "ruijiePimStaticRPAclName"),
        ("RUIJIE-PIM-MIB", "ruijiePimStaticRPStatus"),
        ("RUIJIE-PIM-MIB", "ruijiePimRpCandidateAclName"),
        ("RUIJIE-PIM-MIB", "ruijiePimRpCandidateStatus"))
)
if mibBuilder.loadTexts:
    ruijiePimMIBGroup.setStatus("current")


# Notification objects

ruijiePimNeighborLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 1, 2, 1)
)
ruijiePimNeighborLoss.setObjects(
    ("RUIJIE-PIM-MIB", "ruijiePimNeighborIfIndex")
)
if mibBuilder.loadTexts:
    ruijiePimNeighborLoss.setStatus(
        "current"
    )


# Notifications groups

ruijiePimNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 2, 2, 2)
)
ruijiePimNotifyGroup.setObjects(
    ("RUIJIE-PIM-MIB", "ruijiePimNeighborLoss")
)
if mibBuilder.loadTexts:
    ruijiePimNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ruijiePimMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 27, 2, 1, 1)
)
ruijiePimMIBCompliance.setObjects(
    ("RUIJIE-PIM-MIB", "ruijiePimMIBGroup")
)
if mibBuilder.loadTexts:
    ruijiePimMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-PIM-MIB",
    **{"ruijiePimMIB": ruijiePimMIB,
       "ruijiePimMIBObjects": ruijiePimMIBObjects,
       "ruijiePim": ruijiePim,
       "ruijiePimJoinPruneInterval": ruijiePimJoinPruneInterval,
       "ruijiePimInterfaceTable": ruijiePimInterfaceTable,
       "ruijiePimInterfaceEntry": ruijiePimInterfaceEntry,
       "ruijiePimInterfaceIfIndex": ruijiePimInterfaceIfIndex,
       "ruijiePimInterfaceAddress": ruijiePimInterfaceAddress,
       "ruijiePimInterfaceNetMask": ruijiePimInterfaceNetMask,
       "ruijiePimInterfaceMode": ruijiePimInterfaceMode,
       "ruijiePimInterfaceDR": ruijiePimInterfaceDR,
       "ruijiePimInterfaceHelloInterval": ruijiePimInterfaceHelloInterval,
       "ruijiePimInterfaceJoinPruneInterval": ruijiePimInterfaceJoinPruneInterval,
       "ruijiePimInterfaceCBSRPreference": ruijiePimInterfaceCBSRPreference,
       "ruijiePimInterfaceTrigHelloInterval": ruijiePimInterfaceTrigHelloInterval,
       "ruijiePimInterfaceHelloHoldtime": ruijiePimInterfaceHelloHoldtime,
       "ruijiePimInterfaceLanPruneDelay": ruijiePimInterfaceLanPruneDelay,
       "ruijiePimInterfacePropagationDelay": ruijiePimInterfacePropagationDelay,
       "ruijiePimInterfaceOverrideInterval": ruijiePimInterfaceOverrideInterval,
       "ruijiePimInterfaceGenerationID": ruijiePimInterfaceGenerationID,
       "ruijiePimInterfaceJoinPruneHoldtime": ruijiePimInterfaceJoinPruneHoldtime,
       "ruijiePimInterfaceGraftRetryInterval": ruijiePimInterfaceGraftRetryInterval,
       "ruijiePimInterfaceMaxGraftRetries": ruijiePimInterfaceMaxGraftRetries,
       "ruijiePimInterfaceSRTTLThreshold": ruijiePimInterfaceSRTTLThreshold,
       "ruijiePimInterfaceLanDelayEnabled": ruijiePimInterfaceLanDelayEnabled,
       "ruijiePimInterfaceSRCapable": ruijiePimInterfaceSRCapable,
       "ruijiePimInterfaceDRPriority": ruijiePimInterfaceDRPriority,
       "ruijiePimInterfaceNbrCounter": ruijiePimInterfaceNbrCounter,
       "ruijiePimInterfaceBsrBorderEnabled": ruijiePimInterfaceBsrBorderEnabled,
       "ruijiePimInterfaceCountIn": ruijiePimInterfaceCountIn,
       "ruijiePimInterfaceCountOut": ruijiePimInterfaceCountOut,
       "ruijiePimInterfaceEnabled": ruijiePimInterfaceEnabled,
       "ruijiePimNeighborFilterAcl": ruijiePimNeighborFilterAcl,
       "ruijiePimDrSupportAddressBound": ruijiePimDrSupportAddressBound,
       "ruijiePimNeighborTable": ruijiePimNeighborTable,
       "ruijiePimNeighborEntry": ruijiePimNeighborEntry,
       "ruijiePimNeighborAddress": ruijiePimNeighborAddress,
       "ruijiePimNeighborIfIndex": ruijiePimNeighborIfIndex,
       "ruijiePimNeighborUpTime": ruijiePimNeighborUpTime,
       "ruijiePimNeighborExpiryTime": ruijiePimNeighborExpiryTime,
       "ruijiePimNeighborMode": ruijiePimNeighborMode,
       "ruijiePimNeighborLanPruneDelay": ruijiePimNeighborLanPruneDelay,
       "ruijiePimNeighborOverrideInterval": ruijiePimNeighborOverrideInterval,
       "ruijiePimNeighborTBit": ruijiePimNeighborTBit,
       "ruijiePimNeighborSRCapable": ruijiePimNeighborSRCapable,
       "ruijiePimNeighborDRPresent": ruijiePimNeighborDRPresent,
       "ruijiePimIpMRouteTable": ruijiePimIpMRouteTable,
       "ruijiePimIpMRouteEntry": ruijiePimIpMRouteEntry,
       "ruijiePimIpMRouteUpstreamAssertTimer": ruijiePimIpMRouteUpstreamAssertTimer,
       "ruijiePimIpMRouteAssertMetric": ruijiePimIpMRouteAssertMetric,
       "ruijiePimIpMRouteAssertMetricPref": ruijiePimIpMRouteAssertMetricPref,
       "ruijiePimIpMRouteAssertRPTBit": ruijiePimIpMRouteAssertRPTBit,
       "ruijiePimIpMRouteFlags": ruijiePimIpMRouteFlags,
       "ruijiePimIpMRouteRPFNeighbor": ruijiePimIpMRouteRPFNeighbor,
       "ruijiePimIpMRouteSourceTimer": ruijiePimIpMRouteSourceTimer,
       "ruijiePimIpMRouteOriginatorSRTTL": ruijiePimIpMRouteOriginatorSRTTL,
       "ruijiePimIpMRouteNextHopTable": ruijiePimIpMRouteNextHopTable,
       "ruijiePimIpMRouteNextHopEntry": ruijiePimIpMRouteNextHopEntry,
       "ruijiePimIpMRouteNextHopPruneReason": ruijiePimIpMRouteNextHopPruneReason,
       "ruijiePimIpMRouteNextHopAssertWinner": ruijiePimIpMRouteNextHopAssertWinner,
       "ruijiePimIpMRouteNextHopAssertTimer": ruijiePimIpMRouteNextHopAssertTimer,
       "ruijiePimIpMRouteNextHopAssertMetric": ruijiePimIpMRouteNextHopAssertMetric,
       "ruijiePimIpMRouteNextHopAssertMetricPref": ruijiePimIpMRouteNextHopAssertMetricPref,
       "ruijiePimIpMRouteNextHopJoinPruneTimer": ruijiePimIpMRouteNextHopJoinPruneTimer,
       "ruijiePimRPSetTable": ruijiePimRPSetTable,
       "ruijiePimRPSetEntry": ruijiePimRPSetEntry,
       "ruijiePimRPSetGroupAddress": ruijiePimRPSetGroupAddress,
       "ruijiePimRPSetGroupMask": ruijiePimRPSetGroupMask,
       "ruijiePimRPSetAddress": ruijiePimRPSetAddress,
       "ruijiePimRPSetHoldTime": ruijiePimRPSetHoldTime,
       "ruijiePimRPSetExpiryTime": ruijiePimRPSetExpiryTime,
       "ruijiePimRPSetComponent": ruijiePimRPSetComponent,
       "ruijiePimRPSetUpTime": ruijiePimRPSetUpTime,
       "ruijiePimComponentTable": ruijiePimComponentTable,
       "ruijiePimComponentEntry": ruijiePimComponentEntry,
       "ruijiePimComponentIndex": ruijiePimComponentIndex,
       "ruijiePimComponentBSRAddress": ruijiePimComponentBSRAddress,
       "ruijiePimComponentBSRExpiryTime": ruijiePimComponentBSRExpiryTime,
       "ruijiePimComponentCRPHoldTime": ruijiePimComponentCRPHoldTime,
       "ruijiePimComponentBSRUptime": ruijiePimComponentBSRUptime,
       "ruijiePimComponentBSRPriority": ruijiePimComponentBSRPriority,
       "ruijiePimComponentBSRHashMaskLength": ruijiePimComponentBSRHashMaskLength,
       "ruijiePimComponentBSRNextBsrMessage": ruijiePimComponentBSRNextBsrMessage,
       "ruijiePimComponentNextCandRPAdv": ruijiePimComponentNextCandRPAdv,
       "ruijiePimSourceLifetime": ruijiePimSourceLifetime,
       "ruijiePimStateRefreshInterval": ruijiePimStateRefreshInterval,
       "ruijiePimStateRefreshLimitInterval": ruijiePimStateRefreshLimitInterval,
       "ruijiePimStateRefreshTimeToLive": ruijiePimStateRefreshTimeToLive,
       "ruijiePimBsrCandidateGroup": ruijiePimBsrCandidateGroup,
       "ruijiePimBsrCandidateIfindex": ruijiePimBsrCandidateIfindex,
       "ruijiePimBsrCandidateHashMaskLength": ruijiePimBsrCandidateHashMaskLength,
       "ruijiePimBsrCandidatePriority": ruijiePimBsrCandidatePriority,
       "ruijiePimRPTable": ruijiePimRPTable,
       "ruijiePimRPEntry": ruijiePimRPEntry,
       "ruijiePimRPGroupAddress": ruijiePimRPGroupAddress,
       "ruijiePimRPAddress": ruijiePimRPAddress,
       "ruijiePimRPExpiryTime": ruijiePimRPExpiryTime,
       "ruijiePimRPNextRPReachableIn": ruijiePimRPNextRPReachableIn,
       "ruijiePimStaticRPTable": ruijiePimStaticRPTable,
       "ruijiePimStaticRPEntry": ruijiePimStaticRPEntry,
       "ruijiePimStaticRPAddress": ruijiePimStaticRPAddress,
       "ruijiePimStaticRPAddressIsOverride": ruijiePimStaticRPAddressIsOverride,
       "ruijiePimStaticRPAclName": ruijiePimStaticRPAclName,
       "ruijiePimStaticRPStatus": ruijiePimStaticRPStatus,
       "ruijiePimRpCandidateTable": ruijiePimRpCandidateTable,
       "ruijiePimRpCandidateEntry": ruijiePimRpCandidateEntry,
       "ruijiePimRpCandidateIfindex": ruijiePimRpCandidateIfindex,
       "ruijiePimRpCandidateAclName": ruijiePimRpCandidateAclName,
       "ruijiePimRpCandidateStatus": ruijiePimRpCandidateStatus,
       "ruijiePimTraps": ruijiePimTraps,
       "ruijiePimNeighborLoss": ruijiePimNeighborLoss,
       "ruijiePimMIBConformance": ruijiePimMIBConformance,
       "ruijiePimMIBCompliances": ruijiePimMIBCompliances,
       "ruijiePimMIBCompliance": ruijiePimMIBCompliance,
       "ruijiePimMIBGroups": ruijiePimMIBGroups,
       "ruijiePimMIBGroup": ruijiePimMIBGroup,
       "ruijiePimNotifyGroup": ruijiePimNotifyGroup}
)
