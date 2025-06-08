# SNMP MIB module (CISCO-DLEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/CISCO-DLEP-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 23:02:46 2025
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoNetworkAddress,
 CiscoNetworkProtocol) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoNetworkAddress",
    "CiscoNetworkProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoDlepMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060)
)
if mibBuilder.loadTexts:
    ciscoDlepMIB.setRevisions(
        ("2023-10-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDlepMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDlepMIBNotifs = _CiscoDlepMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 0)
)
_DlepMIBNotifications_ObjectIdentity = ObjectIdentity
dlepMIBNotifications = _DlepMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 0, 0)
)
_CiscoDlepMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDlepMIBObjects = _CiscoDlepMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1)
)
_DlepGlobals_ObjectIdentity = ObjectIdentity
dlepGlobals = _DlepGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 1)
)


class _DlepEnableIndividualNotifications_Type(Bits):
    """Custom type dlepEnableIndividualNotifications based on Bits"""
    namedValues = NamedValues(
        *(("neighborSessionChange", 0),
          ("clientSessionChange", 1))
    )

_DlepEnableIndividualNotifications_Type.__name__ = "Bits"
_DlepEnableIndividualNotifications_Object = MibScalar
dlepEnableIndividualNotifications = _DlepEnableIndividualNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 1, 1),
    _DlepEnableIndividualNotifications_Type()
)
dlepEnableIndividualNotifications.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlepEnableIndividualNotifications.setStatus("current")
_DlepInterface_ObjectIdentity = ObjectIdentity
dlepInterface = _DlepInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 2)
)
_DlepInterfaceTable_Object = MibTable
dlepInterfaceTable = _DlepInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dlepInterfaceTable.setStatus("current")
_DlepInterfaceEntry_Object = MibTableRow
dlepInterfaceEntry = _DlepInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 2, 1, 1)
)
dlepInterfaceEntry.setIndexNames(
    (0, "CISCO-DLEP-MIB", "dlepInterfaceIndex"),
    (0, "CISCO-DLEP-MIB", "dlepInterfaceNbrSessionId"),
)
if mibBuilder.loadTexts:
    dlepInterfaceEntry.setStatus("current")
_DlepInterfaceIndex_Type = InterfaceIndex
_DlepInterfaceIndex_Object = MibTableColumn
dlepInterfaceIndex = _DlepInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 2, 1, 1, 1),
    _DlepInterfaceIndex_Type()
)
dlepInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepInterfaceIndex.setStatus("current")
_DlepInterfaceNbrSessionId_Type = Integer32
_DlepInterfaceNbrSessionId_Object = MibTableColumn
dlepInterfaceNbrSessionId = _DlepInterfaceNbrSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 2, 1, 1, 2),
    _DlepInterfaceNbrSessionId_Type()
)
dlepInterfaceNbrSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepInterfaceNbrSessionId.setStatus("current")


class _DlepInterfaceName_Type(DisplayString):
    """Custom type dlepInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_DlepInterfaceName_Type.__name__ = "DisplayString"
_DlepInterfaceName_Object = MibTableColumn
dlepInterfaceName = _DlepInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 2, 1, 1, 3),
    _DlepInterfaceName_Type()
)
dlepInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepInterfaceName.setStatus("current")
_DlepNeighbor_ObjectIdentity = ObjectIdentity
dlepNeighbor = _DlepNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3)
)
_DlepNeighborTable_Object = MibTable
dlepNeighborTable = _DlepNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dlepNeighborTable.setStatus("current")
_DlepNeighborEntry_Object = MibTableRow
dlepNeighborEntry = _DlepNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1)
)
dlepNeighborEntry.setIndexNames(
    (0, "CISCO-DLEP-MIB", "dlepNeighborSessionId"),
)
if mibBuilder.loadTexts:
    dlepNeighborEntry.setStatus("current")


class _DlepNeighborSessionId_Type(Integer32):
    """Custom type dlepNeighborSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborSessionId_Type.__name__ = "Integer32"
_DlepNeighborSessionId_Object = MibTableColumn
dlepNeighborSessionId = _DlepNeighborSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 1),
    _DlepNeighborSessionId_Type()
)
dlepNeighborSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborSessionId.setStatus("current")
_DlepNeighborInterfaceIndex_Type = InterfaceIndex
_DlepNeighborInterfaceIndex_Object = MibTableColumn
dlepNeighborInterfaceIndex = _DlepNeighborInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 2),
    _DlepNeighborInterfaceIndex_Type()
)
dlepNeighborInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborInterfaceIndex.setStatus("current")


class _DlepNeighborInterfaceName_Type(DisplayString):
    """Custom type dlepNeighborInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DlepNeighborInterfaceName_Type.__name__ = "DisplayString"
_DlepNeighborInterfaceName_Object = MibTableColumn
dlepNeighborInterfaceName = _DlepNeighborInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 3),
    _DlepNeighborInterfaceName_Type()
)
dlepNeighborInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborInterfaceName.setStatus("current")
_DlepNeighborAddress_Type = CiscoNetworkAddress
_DlepNeighborAddress_Object = MibTableColumn
dlepNeighborAddress = _DlepNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 4),
    _DlepNeighborAddress_Type()
)
dlepNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborAddress.setStatus("current")
_DlepNeighborAddressV6LL_Type = CiscoNetworkAddress
_DlepNeighborAddressV6LL_Object = MibTableColumn
dlepNeighborAddressV6LL = _DlepNeighborAddressV6LL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 5),
    _DlepNeighborAddressV6LL_Type()
)
dlepNeighborAddressV6LL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborAddressV6LL.setStatus("current")
_DlepNeighborAddressV6GBL_Type = CiscoNetworkAddress
_DlepNeighborAddressV6GBL_Object = MibTableColumn
dlepNeighborAddressV6GBL = _DlepNeighborAddressV6GBL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 6),
    _DlepNeighborAddressV6GBL_Type()
)
dlepNeighborAddressV6GBL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborAddressV6GBL.setStatus("current")
_DlepNeighborIpUpTime_Type = TimeTicks
_DlepNeighborIpUpTime_Object = MibTableColumn
dlepNeighborIpUpTime = _DlepNeighborIpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 7),
    _DlepNeighborIpUpTime_Type()
)
dlepNeighborIpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborIpUpTime.setStatus("current")


class _DlepNeighborMetricsMTU_Type(Integer32):
    """Custom type dlepNeighborMetricsMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsMTU_Type.__name__ = "Integer32"
_DlepNeighborMetricsMTU_Object = MibTableColumn
dlepNeighborMetricsMTU = _DlepNeighborMetricsMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 8),
    _DlepNeighborMetricsMTU_Type()
)
dlepNeighborMetricsMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsMTU.setStatus("current")


class _DlepNeighborMetricsCdrRx_Type(Integer32):
    """Custom type dlepNeighborMetricsCdrRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsCdrRx_Type.__name__ = "Integer32"
_DlepNeighborMetricsCdrRx_Object = MibTableColumn
dlepNeighborMetricsCdrRx = _DlepNeighborMetricsCdrRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 9),
    _DlepNeighborMetricsCdrRx_Type()
)
dlepNeighborMetricsCdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsCdrRx.setStatus("current")


class _DlepNeighborMetricsCdrTx_Type(Integer32):
    """Custom type dlepNeighborMetricsCdrTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsCdrTx_Type.__name__ = "Integer32"
_DlepNeighborMetricsCdrTx_Object = MibTableColumn
dlepNeighborMetricsCdrTx = _DlepNeighborMetricsCdrTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 10),
    _DlepNeighborMetricsCdrTx_Type()
)
dlepNeighborMetricsCdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsCdrTx.setStatus("current")


class _DlepNeighborMetricsMdrRx_Type(Integer32):
    """Custom type dlepNeighborMetricsMdrRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsMdrRx_Type.__name__ = "Integer32"
_DlepNeighborMetricsMdrRx_Object = MibTableColumn
dlepNeighborMetricsMdrRx = _DlepNeighborMetricsMdrRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 11),
    _DlepNeighborMetricsMdrRx_Type()
)
dlepNeighborMetricsMdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsMdrRx.setStatus("current")


class _DlepNeighborMetricsMdrTx_Type(Integer32):
    """Custom type dlepNeighborMetricsMdrTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsMdrTx_Type.__name__ = "Integer32"
_DlepNeighborMetricsMdrTx_Object = MibTableColumn
dlepNeighborMetricsMdrTx = _DlepNeighborMetricsMdrTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 12),
    _DlepNeighborMetricsMdrTx_Type()
)
dlepNeighborMetricsMdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsMdrTx.setStatus("current")


class _DlepNeighborMetricsRlqRx_Type(Integer32):
    """Custom type dlepNeighborMetricsRlqRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsRlqRx_Type.__name__ = "Integer32"
_DlepNeighborMetricsRlqRx_Object = MibTableColumn
dlepNeighborMetricsRlqRx = _DlepNeighborMetricsRlqRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 13),
    _DlepNeighborMetricsRlqRx_Type()
)
dlepNeighborMetricsRlqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsRlqRx.setStatus("current")


class _DlepNeighborMetricsRlqTx_Type(Integer32):
    """Custom type dlepNeighborMetricsRlqTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsRlqTx_Type.__name__ = "Integer32"
_DlepNeighborMetricsRlqTx_Object = MibTableColumn
dlepNeighborMetricsRlqTx = _DlepNeighborMetricsRlqTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 14),
    _DlepNeighborMetricsRlqTx_Type()
)
dlepNeighborMetricsRlqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsRlqTx.setStatus("current")


class _DlepNeighborMetricsLatency_Type(Integer32):
    """Custom type dlepNeighborMetricsLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsLatency_Type.__name__ = "Integer32"
_DlepNeighborMetricsLatency_Object = MibTableColumn
dlepNeighborMetricsLatency = _DlepNeighborMetricsLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 15),
    _DlepNeighborMetricsLatency_Type()
)
dlepNeighborMetricsLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsLatency.setStatus("current")


class _DlepNeighborMetricsResources_Type(Integer32):
    """Custom type dlepNeighborMetricsResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborMetricsResources_Type.__name__ = "Integer32"
_DlepNeighborMetricsResources_Object = MibTableColumn
dlepNeighborMetricsResources = _DlepNeighborMetricsResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 16),
    _DlepNeighborMetricsResources_Type()
)
dlepNeighborMetricsResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsResources.setStatus("current")


class _DlepNeighborMetricsVac_Type(DisplayString):
    """Custom type dlepNeighborMetricsVac based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_DlepNeighborMetricsVac_Type.__name__ = "DisplayString"
_DlepNeighborMetricsVac_Object = MibTableColumn
dlepNeighborMetricsVac = _DlepNeighborMetricsVac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 17),
    _DlepNeighborMetricsVac_Type()
)
dlepNeighborMetricsVac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsVac.setStatus("current")
_DlepNeighborMetricsMacAddress_Type = CiscoNetworkAddress
_DlepNeighborMetricsMacAddress_Object = MibTableColumn
dlepNeighborMetricsMacAddress = _DlepNeighborMetricsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 18),
    _DlepNeighborMetricsMacAddress_Type()
)
dlepNeighborMetricsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborMetricsMacAddress.setStatus("current")


class _DlepNeighborSessionOperStatus_Type(Integer32):
    """Custom type dlepNeighborSessionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("forcedDown", 3))
    )


_DlepNeighborSessionOperStatus_Type.__name__ = "Integer32"
_DlepNeighborSessionOperStatus_Object = MibTableColumn
dlepNeighborSessionOperStatus = _DlepNeighborSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 3, 1, 1, 19),
    _DlepNeighborSessionOperStatus_Type()
)
dlepNeighborSessionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborSessionOperStatus.setStatus("current")
_DlepClient_ObjectIdentity = ObjectIdentity
dlepClient = _DlepClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4)
)
_DlepClientTable_Object = MibTable
dlepClientTable = _DlepClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dlepClientTable.setStatus("current")
_DlepClientEntry_Object = MibTableRow
dlepClientEntry = _DlepClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1)
)
dlepClientEntry.setIndexNames(
    (0, "CISCO-DLEP-MIB", "dlepClientInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dlepClientEntry.setStatus("current")
_DlepClientInterfaceIndex_Type = InterfaceIndex
_DlepClientInterfaceIndex_Object = MibTableColumn
dlepClientInterfaceIndex = _DlepClientInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 1),
    _DlepClientInterfaceIndex_Type()
)
dlepClientInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientInterfaceIndex.setStatus("current")


class _DlepClientInterfaceName_Type(DisplayString):
    """Custom type dlepClientInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlepClientInterfaceName_Type.__name__ = "DisplayString"
_DlepClientInterfaceName_Object = MibTableColumn
dlepClientInterfaceName = _DlepClientInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 2),
    _DlepClientInterfaceName_Type()
)
dlepClientInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientInterfaceName.setStatus("current")


class _DlepClientPeerId_Type(Integer32):
    """Custom type dlepClientPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientPeerId_Type.__name__ = "Integer32"
_DlepClientPeerId_Object = MibTableColumn
dlepClientPeerId = _DlepClientPeerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 3),
    _DlepClientPeerId_Type()
)
dlepClientPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientPeerId.setStatus("current")


class _DlepNeighborCount_Type(Integer32):
    """Custom type dlepNeighborCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepNeighborCount_Type.__name__ = "Integer32"
_DlepNeighborCount_Object = MibTableColumn
dlepNeighborCount = _DlepNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 4),
    _DlepNeighborCount_Type()
)
dlepNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepNeighborCount.setStatus("current")


class _DlepClientDescription_Type(DisplayString):
    """Custom type dlepClientDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlepClientDescription_Type.__name__ = "DisplayString"
_DlepClientDescription_Object = MibTableColumn
dlepClientDescription = _DlepClientDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 5),
    _DlepClientDescription_Type()
)
dlepClientDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientDescription.setStatus("current")
_DlepClientAddressType_Type = CiscoNetworkProtocol
_DlepClientAddressType_Object = MibTableColumn
dlepClientAddressType = _DlepClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 6),
    _DlepClientAddressType_Type()
)
dlepClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientAddressType.setStatus("current")
_DlepClientLocalAddress_Type = CiscoNetworkAddress
_DlepClientLocalAddress_Object = MibTableColumn
dlepClientLocalAddress = _DlepClientLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 7),
    _DlepClientLocalAddress_Type()
)
dlepClientLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientLocalAddress.setStatus("current")
_DlepClientLocalRadioAddress_Type = CiscoNetworkAddress
_DlepClientLocalRadioAddress_Object = MibTableColumn
dlepClientLocalRadioAddress = _DlepClientLocalRadioAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 8),
    _DlepClientLocalRadioAddress_Type()
)
dlepClientLocalRadioAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientLocalRadioAddress.setStatus("current")
_DlepClientUpTime_Type = TimeTicks
_DlepClientUpTime_Object = MibTableColumn
dlepClientUpTime = _DlepClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 9),
    _DlepClientUpTime_Type()
)
dlepClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientUpTime.setStatus("current")


class _DlepClientMetricsCdrRx_Type(Integer32):
    """Custom type dlepClientMetricsCdrRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsCdrRx_Type.__name__ = "Integer32"
_DlepClientMetricsCdrRx_Object = MibTableColumn
dlepClientMetricsCdrRx = _DlepClientMetricsCdrRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 10),
    _DlepClientMetricsCdrRx_Type()
)
dlepClientMetricsCdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsCdrRx.setStatus("current")


class _DlepClientMetricsCdrTx_Type(Integer32):
    """Custom type dlepClientMetricsCdrTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsCdrTx_Type.__name__ = "Integer32"
_DlepClientMetricsCdrTx_Object = MibTableColumn
dlepClientMetricsCdrTx = _DlepClientMetricsCdrTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 11),
    _DlepClientMetricsCdrTx_Type()
)
dlepClientMetricsCdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsCdrTx.setStatus("current")


class _DlepClientMetricsMdrRx_Type(Integer32):
    """Custom type dlepClientMetricsMdrRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsMdrRx_Type.__name__ = "Integer32"
_DlepClientMetricsMdrRx_Object = MibTableColumn
dlepClientMetricsMdrRx = _DlepClientMetricsMdrRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 12),
    _DlepClientMetricsMdrRx_Type()
)
dlepClientMetricsMdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsMdrRx.setStatus("current")


class _DlepClientMetricsMdrTx_Type(Integer32):
    """Custom type dlepClientMetricsMdrTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsMdrTx_Type.__name__ = "Integer32"
_DlepClientMetricsMdrTx_Object = MibTableColumn
dlepClientMetricsMdrTx = _DlepClientMetricsMdrTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 13),
    _DlepClientMetricsMdrTx_Type()
)
dlepClientMetricsMdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsMdrTx.setStatus("current")


class _DlepClientMetricsRlqRx_Type(Integer32):
    """Custom type dlepClientMetricsRlqRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsRlqRx_Type.__name__ = "Integer32"
_DlepClientMetricsRlqRx_Object = MibTableColumn
dlepClientMetricsRlqRx = _DlepClientMetricsRlqRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 14),
    _DlepClientMetricsRlqRx_Type()
)
dlepClientMetricsRlqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsRlqRx.setStatus("current")


class _DlepClientMetricsRlqTx_Type(Integer32):
    """Custom type dlepClientMetricsRlqTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsRlqTx_Type.__name__ = "Integer32"
_DlepClientMetricsRlqTx_Object = MibTableColumn
dlepClientMetricsRlqTx = _DlepClientMetricsRlqTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 15),
    _DlepClientMetricsRlqTx_Type()
)
dlepClientMetricsRlqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsRlqTx.setStatus("current")


class _DlepClientMetricsLatency_Type(Integer32):
    """Custom type dlepClientMetricsLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsLatency_Type.__name__ = "Integer32"
_DlepClientMetricsLatency_Object = MibTableColumn
dlepClientMetricsLatency = _DlepClientMetricsLatency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 16),
    _DlepClientMetricsLatency_Type()
)
dlepClientMetricsLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsLatency.setStatus("current")


class _DlepClientMetricsResources_Type(Integer32):
    """Custom type dlepClientMetricsResources based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsResources_Type.__name__ = "Integer32"
_DlepClientMetricsResources_Object = MibTableColumn
dlepClientMetricsResources = _DlepClientMetricsResources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 17),
    _DlepClientMetricsResources_Type()
)
dlepClientMetricsResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsResources.setStatus("current")


class _DlepClientMetricsMTU_Type(Integer32):
    """Custom type dlepClientMetricsMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientMetricsMTU_Type.__name__ = "Integer32"
_DlepClientMetricsMTU_Object = MibTableColumn
dlepClientMetricsMTU = _DlepClientMetricsMTU_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 18),
    _DlepClientMetricsMTU_Type()
)
dlepClientMetricsMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsMTU.setStatus("current")


class _DlepClientPort_Type(Integer32):
    """Custom type dlepClientPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientPort_Type.__name__ = "Integer32"
_DlepClientPort_Object = MibTableColumn
dlepClientPort = _DlepClientPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 19),
    _DlepClientPort_Type()
)
dlepClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientPort.setStatus("current")


class _DlepClientConfigVT_Type(Integer32):
    """Custom type dlepClientConfigVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientConfigVT_Type.__name__ = "Integer32"
_DlepClientConfigVT_Object = MibTableColumn
dlepClientConfigVT = _DlepClientConfigVT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 20),
    _DlepClientConfigVT_Type()
)
dlepClientConfigVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientConfigVT.setStatus("current")


class _DlepClientConfigHeartBeat_Type(Integer32):
    """Custom type dlepClientConfigHeartBeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientConfigHeartBeat_Type.__name__ = "Integer32"
_DlepClientConfigHeartBeat_Object = MibTableColumn
dlepClientConfigHeartBeat = _DlepClientConfigHeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 21),
    _DlepClientConfigHeartBeat_Type()
)
dlepClientConfigHeartBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientConfigHeartBeat.setStatus("current")


class _DlepClientConfigDeadInterval_Type(Integer32):
    """Custom type dlepClientConfigDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientConfigDeadInterval_Type.__name__ = "Integer32"
_DlepClientConfigDeadInterval_Object = MibTableColumn
dlepClientConfigDeadInterval = _DlepClientConfigDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 22),
    _DlepClientConfigDeadInterval_Type()
)
dlepClientConfigDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientConfigDeadInterval.setStatus("current")


class _DlepClientConfigTerminate_Type(Integer32):
    """Custom type dlepClientConfigTerminate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepClientConfigTerminate_Type.__name__ = "Integer32"
_DlepClientConfigTerminate_Object = MibTableColumn
dlepClientConfigTerminate = _DlepClientConfigTerminate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 23),
    _DlepClientConfigTerminate_Type()
)
dlepClientConfigTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientConfigTerminate.setStatus("current")


class _DlepConfigNeighborDown_Type(Integer32):
    """Custom type dlepConfigNeighborDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigNeighborDown_Type.__name__ = "Integer32"
_DlepConfigNeighborDown_Object = MibTableColumn
dlepConfigNeighborDown = _DlepConfigNeighborDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 24),
    _DlepConfigNeighborDown_Type()
)
dlepConfigNeighborDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigNeighborDown.setStatus("current")


class _DlepClientSessionOperStatus_Type(Integer32):
    """Custom type dlepClientSessionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("forcedDown", 3))
    )


_DlepClientSessionOperStatus_Type.__name__ = "Integer32"
_DlepClientSessionOperStatus_Object = MibTableColumn
dlepClientSessionOperStatus = _DlepClientSessionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 25),
    _DlepClientSessionOperStatus_Type()
)
dlepClientSessionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientSessionOperStatus.setStatus("current")


class _DlepClientMetricsSummary_Type(DisplayString):
    """Custom type dlepClientMetricsSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepClientMetricsSummary_Type.__name__ = "DisplayString"
_DlepClientMetricsSummary_Object = MibTableColumn
dlepClientMetricsSummary = _DlepClientMetricsSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 26),
    _DlepClientMetricsSummary_Type()
)
dlepClientMetricsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientMetricsSummary.setStatus("current")


class _DlepClientConfigSummary_Type(DisplayString):
    """Custom type dlepClientConfigSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepClientConfigSummary_Type.__name__ = "DisplayString"
_DlepClientConfigSummary_Object = MibTableColumn
dlepClientConfigSummary = _DlepClientConfigSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 4, 1, 1, 27),
    _DlepClientConfigSummary_Type()
)
dlepClientConfigSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepClientConfigSummary.setStatus("current")
_DlepConfig_ObjectIdentity = ObjectIdentity
dlepConfig = _DlepConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5)
)
_DlepConfigTable_Object = MibTable
dlepConfigTable = _DlepConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dlepConfigTable.setStatus("current")
_DlepConfigEntry_Object = MibTableRow
dlepConfigEntry = _DlepConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1)
)
dlepConfigEntry.setIndexNames(
    (0, "CISCO-DLEP-MIB", "dlepConfigInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dlepConfigEntry.setStatus("current")
_DlepConfigInterfaceIndex_Type = InterfaceIndex
_DlepConfigInterfaceIndex_Object = MibTableColumn
dlepConfigInterfaceIndex = _DlepConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 1),
    _DlepConfigInterfaceIndex_Type()
)
dlepConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigInterfaceIndex.setStatus("current")


class _DlepConfigInterfaceName_Type(DisplayString):
    """Custom type dlepConfigInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlepConfigInterfaceName_Type.__name__ = "DisplayString"
_DlepConfigInterfaceName_Object = MibTableColumn
dlepConfigInterfaceName = _DlepConfigInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 2),
    _DlepConfigInterfaceName_Type()
)
dlepConfigInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigInterfaceName.setStatus("current")


class _DlepConfigPeerInterfaceDescription_Type(DisplayString):
    """Custom type dlepConfigPeerInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlepConfigPeerInterfaceDescription_Type.__name__ = "DisplayString"
_DlepConfigPeerInterfaceDescription_Object = MibTableColumn
dlepConfigPeerInterfaceDescription = _DlepConfigPeerInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 3),
    _DlepConfigPeerInterfaceDescription_Type()
)
dlepConfigPeerInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigPeerInterfaceDescription.setStatus("current")
_DlepConfigLocalAddressType_Type = CiscoNetworkProtocol
_DlepConfigLocalAddressType_Object = MibTableColumn
dlepConfigLocalAddressType = _DlepConfigLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 4),
    _DlepConfigLocalAddressType_Type()
)
dlepConfigLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigLocalAddressType.setStatus("current")
_DlepConfigLocalAddress_Type = CiscoNetworkAddress
_DlepConfigLocalAddress_Object = MibTableColumn
dlepConfigLocalAddress = _DlepConfigLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 5),
    _DlepConfigLocalAddress_Type()
)
dlepConfigLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigLocalAddress.setStatus("current")


class _DlepConfigLocalTCPPort_Type(Integer32):
    """Custom type dlepConfigLocalTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigLocalTCPPort_Type.__name__ = "Integer32"
_DlepConfigLocalTCPPort_Object = MibTableColumn
dlepConfigLocalTCPPort = _DlepConfigLocalTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 6),
    _DlepConfigLocalTCPPort_Type()
)
dlepConfigLocalTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigLocalTCPPort.setStatus("current")


class _DlepConfigLocalUDPPort_Type(Integer32):
    """Custom type dlepConfigLocalUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigLocalUDPPort_Type.__name__ = "Integer32"
_DlepConfigLocalUDPPort_Object = MibTableColumn
dlepConfigLocalUDPPort = _DlepConfigLocalUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 7),
    _DlepConfigLocalUDPPort_Type()
)
dlepConfigLocalUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigLocalUDPPort.setStatus("current")
_DlepConfigRemoteAddressType_Type = CiscoNetworkProtocol
_DlepConfigRemoteAddressType_Object = MibTableColumn
dlepConfigRemoteAddressType = _DlepConfigRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 8),
    _DlepConfigRemoteAddressType_Type()
)
dlepConfigRemoteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigRemoteAddressType.setStatus("current")
_DlepConfigRemoteAddress_Type = CiscoNetworkAddress
_DlepConfigRemoteAddress_Object = MibTableColumn
dlepConfigRemoteAddress = _DlepConfigRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 9),
    _DlepConfigRemoteAddress_Type()
)
dlepConfigRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigRemoteAddress.setStatus("current")


class _DlepConfigRemoteTCPPort_Type(Integer32):
    """Custom type dlepConfigRemoteTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigRemoteTCPPort_Type.__name__ = "Integer32"
_DlepConfigRemoteTCPPort_Object = MibTableColumn
dlepConfigRemoteTCPPort = _DlepConfigRemoteTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 10),
    _DlepConfigRemoteTCPPort_Type()
)
dlepConfigRemoteTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigRemoteTCPPort.setStatus("current")


class _DlepConfigRemoteUDPPort_Type(Integer32):
    """Custom type dlepConfigRemoteUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigRemoteUDPPort_Type.__name__ = "Integer32"
_DlepConfigRemoteUDPPort_Object = MibTableColumn
dlepConfigRemoteUDPPort = _DlepConfigRemoteUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 11),
    _DlepConfigRemoteUDPPort_Type()
)
dlepConfigRemoteUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigRemoteUDPPort.setStatus("current")


class _DlepConfigSessionMode_Type(Integer32):
    """Custom type dlepConfigSessionMode based on Integer32"""
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
        *(("manual-v4", 1),
          ("manual-v6", 2),
          ("auto-v4", 3),
          ("auto-v6", 4))
    )


_DlepConfigSessionMode_Type.__name__ = "Integer32"
_DlepConfigSessionMode_Object = MibTableColumn
dlepConfigSessionMode = _DlepConfigSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 12),
    _DlepConfigSessionMode_Type()
)
dlepConfigSessionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigSessionMode.setStatus("current")


class _DlepConfigVirtualTemplate_Type(Integer32):
    """Custom type dlepConfigVirtualTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigVirtualTemplate_Type.__name__ = "Integer32"
_DlepConfigVirtualTemplate_Object = MibTableColumn
dlepConfigVirtualTemplate = _DlepConfigVirtualTemplate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 13),
    _DlepConfigVirtualTemplate_Type()
)
dlepConfigVirtualTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigVirtualTemplate.setStatus("current")


class _DlepConfigMissedHeartbeatThreshold_Type(Integer32):
    """Custom type dlepConfigMissedHeartbeatThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigMissedHeartbeatThreshold_Type.__name__ = "Integer32"
_DlepConfigMissedHeartbeatThreshold_Object = MibTableColumn
dlepConfigMissedHeartbeatThreshold = _DlepConfigMissedHeartbeatThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 14),
    _DlepConfigMissedHeartbeatThreshold_Type()
)
dlepConfigMissedHeartbeatThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigMissedHeartbeatThreshold.setStatus("current")


class _DlepConfigHeartbeatInterval_Type(Integer32):
    """Custom type dlepConfigHeartbeatInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigHeartbeatInterval_Type.__name__ = "Integer32"
_DlepConfigHeartbeatInterval_Object = MibTableColumn
dlepConfigHeartbeatInterval = _DlepConfigHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 15),
    _DlepConfigHeartbeatInterval_Type()
)
dlepConfigHeartbeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigHeartbeatInterval.setStatus("current")


class _DlepConfigDiscoveryInterval_Type(Integer32):
    """Custom type dlepConfigDiscoveryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigDiscoveryInterval_Type.__name__ = "Integer32"
_DlepConfigDiscoveryInterval_Object = MibTableColumn
dlepConfigDiscoveryInterval = _DlepConfigDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 16),
    _DlepConfigDiscoveryInterval_Type()
)
dlepConfigDiscoveryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigDiscoveryInterval.setStatus("current")


class _DlepConfigSessionAckTimeout_Type(Integer32):
    """Custom type dlepConfigSessionAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigSessionAckTimeout_Type.__name__ = "Integer32"
_DlepConfigSessionAckTimeout_Object = MibTableColumn
dlepConfigSessionAckTimeout = _DlepConfigSessionAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 17),
    _DlepConfigSessionAckTimeout_Type()
)
dlepConfigSessionAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigSessionAckTimeout.setStatus("current")


class _DlepConfigPeerTerminateAckTimeout_Type(Integer32):
    """Custom type dlepConfigPeerTerminateAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigPeerTerminateAckTimeout_Type.__name__ = "Integer32"
_DlepConfigPeerTerminateAckTimeout_Object = MibTableColumn
dlepConfigPeerTerminateAckTimeout = _DlepConfigPeerTerminateAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 18),
    _DlepConfigPeerTerminateAckTimeout_Type()
)
dlepConfigPeerTerminateAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigPeerTerminateAckTimeout.setStatus("current")


class _DlepConfigNeighborDownAckTimeout_Type(Integer32):
    """Custom type dlepConfigNeighborDownAckTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepConfigNeighborDownAckTimeout_Type.__name__ = "Integer32"
_DlepConfigNeighborDownAckTimeout_Object = MibTableColumn
dlepConfigNeighborDownAckTimeout = _DlepConfigNeighborDownAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 19),
    _DlepConfigNeighborDownAckTimeout_Type()
)
dlepConfigNeighborDownAckTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigNeighborDownAckTimeout.setStatus("current")


class _DlepConfigSummary_Type(DisplayString):
    """Custom type dlepConfigSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepConfigSummary_Type.__name__ = "DisplayString"
_DlepConfigSummary_Object = MibTableColumn
dlepConfigSummary = _DlepConfigSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 5, 1, 1, 20),
    _DlepConfigSummary_Type()
)
dlepConfigSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepConfigSummary.setStatus("current")
_DlepCounters_ObjectIdentity = ObjectIdentity
dlepCounters = _DlepCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6)
)
_DlepCountersTable_Object = MibTable
dlepCountersTable = _DlepCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dlepCountersTable.setStatus("current")
_DlepCountersEntry_Object = MibTableRow
dlepCountersEntry = _DlepCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1)
)
dlepCountersEntry.setIndexNames(
    (0, "CISCO-DLEP-MIB", "dlepCounterInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dlepCountersEntry.setStatus("current")
_DlepCounterInterfaceIndex_Type = InterfaceIndex
_DlepCounterInterfaceIndex_Object = MibTableColumn
dlepCounterInterfaceIndex = _DlepCounterInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 1),
    _DlepCounterInterfaceIndex_Type()
)
dlepCounterInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterInterfaceIndex.setStatus("current")


class _DlepCounterInterfaceName_Type(DisplayString):
    """Custom type dlepCounterInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlepCounterInterfaceName_Type.__name__ = "DisplayString"
_DlepCounterInterfaceName_Object = MibTableColumn
dlepCounterInterfaceName = _DlepCounterInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 2),
    _DlepCounterInterfaceName_Type()
)
dlepCounterInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterInterfaceName.setStatus("current")


class _DlepCounterLastClearTime_Type(DisplayString):
    """Custom type dlepCounterLastClearTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DlepCounterLastClearTime_Type.__name__ = "DisplayString"
_DlepCounterLastClearTime_Object = MibTableColumn
dlepCounterLastClearTime = _DlepCounterLastClearTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 3),
    _DlepCounterLastClearTime_Type()
)
dlepCounterLastClearTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterLastClearTime.setStatus("current")
_DlepCounterLocalIpType_Type = CiscoNetworkProtocol
_DlepCounterLocalIpType_Object = MibTableColumn
dlepCounterLocalIpType = _DlepCounterLocalIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 4),
    _DlepCounterLocalIpType_Type()
)
dlepCounterLocalIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterLocalIpType.setStatus("current")
_DlepCounterLocalIp_Type = CiscoNetworkAddress
_DlepCounterLocalIp_Object = MibTableColumn
dlepCounterLocalIp = _DlepCounterLocalIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 5),
    _DlepCounterLocalIp_Type()
)
dlepCounterLocalIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterLocalIp.setStatus("current")


class _DlepCounterLocalTCPPort_Type(Integer32):
    """Custom type dlepCounterLocalTCPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterLocalTCPPort_Type.__name__ = "Integer32"
_DlepCounterLocalTCPPort_Object = MibTableColumn
dlepCounterLocalTCPPort = _DlepCounterLocalTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 6),
    _DlepCounterLocalTCPPort_Type()
)
dlepCounterLocalTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterLocalTCPPort.setStatus("current")


class _DlepCounterLocalUDPPort_Type(Integer32):
    """Custom type dlepCounterLocalUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterLocalUDPPort_Type.__name__ = "Integer32"
_DlepCounterLocalUDPPort_Object = MibTableColumn
dlepCounterLocalUDPPort = _DlepCounterLocalUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 7),
    _DlepCounterLocalUDPPort_Type()
)
dlepCounterLocalUDPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterLocalUDPPort.setStatus("current")


class _DlepCounterRXPeerDiscovery_Type(Integer32):
    """Custom type dlepCounterRXPeerDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXPeerDiscovery_Type.__name__ = "Integer32"
_DlepCounterRXPeerDiscovery_Object = MibTableColumn
dlepCounterRXPeerDiscovery = _DlepCounterRXPeerDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 8),
    _DlepCounterRXPeerDiscovery_Type()
)
dlepCounterRXPeerDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXPeerDiscovery.setStatus("current")


class _DlepCounterRXPeerOffer_Type(Integer32):
    """Custom type dlepCounterRXPeerOffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXPeerOffer_Type.__name__ = "Integer32"
_DlepCounterRXPeerOffer_Object = MibTableColumn
dlepCounterRXPeerOffer = _DlepCounterRXPeerOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 9),
    _DlepCounterRXPeerOffer_Type()
)
dlepCounterRXPeerOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXPeerOffer.setStatus("current")


class _DlepCounterRXPeerInit_Type(Integer32):
    """Custom type dlepCounterRXPeerInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXPeerInit_Type.__name__ = "Integer32"
_DlepCounterRXPeerInit_Object = MibTableColumn
dlepCounterRXPeerInit = _DlepCounterRXPeerInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 10),
    _DlepCounterRXPeerInit_Type()
)
dlepCounterRXPeerInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXPeerInit.setStatus("current")


class _DlepCounterRXPeerInitAck_Type(Integer32):
    """Custom type dlepCounterRXPeerInitAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXPeerInitAck_Type.__name__ = "Integer32"
_DlepCounterRXPeerInitAck_Object = MibTableColumn
dlepCounterRXPeerInitAck = _DlepCounterRXPeerInitAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 11),
    _DlepCounterRXPeerInitAck_Type()
)
dlepCounterRXPeerInitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXPeerInitAck.setStatus("current")


class _DlepCounterRXHeartbeat_Type(Integer32):
    """Custom type dlepCounterRXHeartbeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXHeartbeat_Type.__name__ = "Integer32"
_DlepCounterRXHeartbeat_Object = MibTableColumn
dlepCounterRXHeartbeat = _DlepCounterRXHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 12),
    _DlepCounterRXHeartbeat_Type()
)
dlepCounterRXHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXHeartbeat.setStatus("current")


class _DlepCounterRXPeerTerminate_Type(Integer32):
    """Custom type dlepCounterRXPeerTerminate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXPeerTerminate_Type.__name__ = "Integer32"
_DlepCounterRXPeerTerminate_Object = MibTableColumn
dlepCounterRXPeerTerminate = _DlepCounterRXPeerTerminate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 13),
    _DlepCounterRXPeerTerminate_Type()
)
dlepCounterRXPeerTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXPeerTerminate.setStatus("current")


class _DlepCounterRXPeerTerminateAck_Type(Integer32):
    """Custom type dlepCounterRXPeerTerminateAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXPeerTerminateAck_Type.__name__ = "Integer32"
_DlepCounterRXPeerTerminateAck_Object = MibTableColumn
dlepCounterRXPeerTerminateAck = _DlepCounterRXPeerTerminateAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 14),
    _DlepCounterRXPeerTerminateAck_Type()
)
dlepCounterRXPeerTerminateAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXPeerTerminateAck.setStatus("current")


class _DlepCounterTXPeerOffer_Type(Integer32):
    """Custom type dlepCounterTXPeerOffer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXPeerOffer_Type.__name__ = "Integer32"
_DlepCounterTXPeerOffer_Object = MibTableColumn
dlepCounterTXPeerOffer = _DlepCounterTXPeerOffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 15),
    _DlepCounterTXPeerOffer_Type()
)
dlepCounterTXPeerOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXPeerOffer.setStatus("current")


class _DlepCounterTXPeerDiscovery_Type(Integer32):
    """Custom type dlepCounterTXPeerDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXPeerDiscovery_Type.__name__ = "Integer32"
_DlepCounterTXPeerDiscovery_Object = MibTableColumn
dlepCounterTXPeerDiscovery = _DlepCounterTXPeerDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 16),
    _DlepCounterTXPeerDiscovery_Type()
)
dlepCounterTXPeerDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXPeerDiscovery.setStatus("current")


class _DlepCounterTXPeerInitAck_Type(Integer32):
    """Custom type dlepCounterTXPeerInitAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXPeerInitAck_Type.__name__ = "Integer32"
_DlepCounterTXPeerInitAck_Object = MibTableColumn
dlepCounterTXPeerInitAck = _DlepCounterTXPeerInitAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 17),
    _DlepCounterTXPeerInitAck_Type()
)
dlepCounterTXPeerInitAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXPeerInitAck.setStatus("current")


class _DlepCounterTXPeerInit_Type(Integer32):
    """Custom type dlepCounterTXPeerInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXPeerInit_Type.__name__ = "Integer32"
_DlepCounterTXPeerInit_Object = MibTableColumn
dlepCounterTXPeerInit = _DlepCounterTXPeerInit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 18),
    _DlepCounterTXPeerInit_Type()
)
dlepCounterTXPeerInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXPeerInit.setStatus("current")


class _DlepCounterTXHeartbeat_Type(Integer32):
    """Custom type dlepCounterTXHeartbeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXHeartbeat_Type.__name__ = "Integer32"
_DlepCounterTXHeartbeat_Object = MibTableColumn
dlepCounterTXHeartbeat = _DlepCounterTXHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 19),
    _DlepCounterTXHeartbeat_Type()
)
dlepCounterTXHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXHeartbeat.setStatus("current")


class _DlepCounterTXPeerTerminateAck_Type(Integer32):
    """Custom type dlepCounterTXPeerTerminateAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXPeerTerminateAck_Type.__name__ = "Integer32"
_DlepCounterTXPeerTerminateAck_Object = MibTableColumn
dlepCounterTXPeerTerminateAck = _DlepCounterTXPeerTerminateAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 20),
    _DlepCounterTXPeerTerminateAck_Type()
)
dlepCounterTXPeerTerminateAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXPeerTerminateAck.setStatus("current")


class _DlepCounterTXPeerTerminate_Type(Integer32):
    """Custom type dlepCounterTXPeerTerminate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXPeerTerminate_Type.__name__ = "Integer32"
_DlepCounterTXPeerTerminate_Object = MibTableColumn
dlepCounterTXPeerTerminate = _DlepCounterTXPeerTerminate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 21),
    _DlepCounterTXPeerTerminate_Type()
)
dlepCounterTXPeerTerminate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXPeerTerminate.setStatus("current")


class _DlepCounterRXNeighborUp_Type(Integer32):
    """Custom type dlepCounterRXNeighborUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXNeighborUp_Type.__name__ = "Integer32"
_DlepCounterRXNeighborUp_Object = MibTableColumn
dlepCounterRXNeighborUp = _DlepCounterRXNeighborUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 22),
    _DlepCounterRXNeighborUp_Type()
)
dlepCounterRXNeighborUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXNeighborUp.setStatus("current")


class _DlepCounterRXMetric_Type(Integer32):
    """Custom type dlepCounterRXMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXMetric_Type.__name__ = "Integer32"
_DlepCounterRXMetric_Object = MibTableColumn
dlepCounterRXMetric = _DlepCounterRXMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 23),
    _DlepCounterRXMetric_Type()
)
dlepCounterRXMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXMetric.setStatus("current")


class _DlepCounterRXNeighborDown_Type(Integer32):
    """Custom type dlepCounterRXNeighborDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXNeighborDown_Type.__name__ = "Integer32"
_DlepCounterRXNeighborDown_Object = MibTableColumn
dlepCounterRXNeighborDown = _DlepCounterRXNeighborDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 24),
    _DlepCounterRXNeighborDown_Type()
)
dlepCounterRXNeighborDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXNeighborDown.setStatus("current")


class _DlepCounterRXNeighborDownAck_Type(Integer32):
    """Custom type dlepCounterRXNeighborDownAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXNeighborDownAck_Type.__name__ = "Integer32"
_DlepCounterRXNeighborDownAck_Object = MibTableColumn
dlepCounterRXNeighborDownAck = _DlepCounterRXNeighborDownAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 25),
    _DlepCounterRXNeighborDownAck_Type()
)
dlepCounterRXNeighborDownAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXNeighborDownAck.setStatus("current")


class _DlepCounterTXNeighborUpAck_Type(Integer32):
    """Custom type dlepCounterTXNeighborUpAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXNeighborUpAck_Type.__name__ = "Integer32"
_DlepCounterTXNeighborUpAck_Object = MibTableColumn
dlepCounterTXNeighborUpAck = _DlepCounterTXNeighborUpAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 26),
    _DlepCounterTXNeighborUpAck_Type()
)
dlepCounterTXNeighborUpAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXNeighborUpAck.setStatus("current")


class _DlepCounterTXNeighborDownAck_Type(Integer32):
    """Custom type dlepCounterTXNeighborDownAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXNeighborDownAck_Type.__name__ = "Integer32"
_DlepCounterTXNeighborDownAck_Object = MibTableColumn
dlepCounterTXNeighborDownAck = _DlepCounterTXNeighborDownAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 27),
    _DlepCounterTXNeighborDownAck_Type()
)
dlepCounterTXNeighborDownAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXNeighborDownAck.setStatus("current")


class _DlepCounterTXNeighborDown_Type(Integer32):
    """Custom type dlepCounterTXNeighborDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterTXNeighborDown_Type.__name__ = "Integer32"
_DlepCounterTXNeighborDown_Object = MibTableColumn
dlepCounterTXNeighborDown = _DlepCounterTXNeighborDown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 28),
    _DlepCounterTXNeighborDown_Type()
)
dlepCounterTXNeighborDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterTXNeighborDown.setStatus("current")


class _DlepCounterRXInvalidMessage_Type(Integer32):
    """Custom type dlepCounterRXInvalidMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXInvalidMessage_Type.__name__ = "Integer32"
_DlepCounterRXInvalidMessage_Object = MibTableColumn
dlepCounterRXInvalidMessage = _DlepCounterRXInvalidMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 29),
    _DlepCounterRXInvalidMessage_Type()
)
dlepCounterRXInvalidMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXInvalidMessage.setStatus("current")


class _DlepCounterPreExistingNeighbor_Type(Integer32):
    """Custom type dlepCounterPreExistingNeighbor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterPreExistingNeighbor_Type.__name__ = "Integer32"
_DlepCounterPreExistingNeighbor_Object = MibTableColumn
dlepCounterPreExistingNeighbor = _DlepCounterPreExistingNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 30),
    _DlepCounterPreExistingNeighbor_Type()
)
dlepCounterPreExistingNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterPreExistingNeighbor.setStatus("current")


class _DlepCounterNeighborNotFound_Type(Integer32):
    """Custom type dlepCounterNeighborNotFound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterNeighborNotFound_Type.__name__ = "Integer32"
_DlepCounterNeighborNotFound_Object = MibTableColumn
dlepCounterNeighborNotFound = _DlepCounterNeighborNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 31),
    _DlepCounterNeighborNotFound_Type()
)
dlepCounterNeighborNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterNeighborNotFound.setStatus("current")


class _DlepCounterRXUnknownMessage_Type(Integer32):
    """Custom type dlepCounterRXUnknownMessage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRXUnknownMessage_Type.__name__ = "Integer32"
_DlepCounterRXUnknownMessage_Object = MibTableColumn
dlepCounterRXUnknownMessage = _DlepCounterRXUnknownMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 32),
    _DlepCounterRXUnknownMessage_Type()
)
dlepCounterRXUnknownMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRXUnknownMessage.setStatus("current")


class _DlepCounterNeighborResourceError_Type(Integer32):
    """Custom type dlepCounterNeighborResourceError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterNeighborResourceError_Type.__name__ = "Integer32"
_DlepCounterNeighborResourceError_Object = MibTableColumn
dlepCounterNeighborResourceError = _DlepCounterNeighborResourceError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 33),
    _DlepCounterNeighborResourceError_Type()
)
dlepCounterNeighborResourceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterNeighborResourceError.setStatus("current")


class _DlepCounterNeighborMsgPeerNotUp_Type(Integer32):
    """Custom type dlepCounterNeighborMsgPeerNotUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterNeighborMsgPeerNotUp_Type.__name__ = "Integer32"
_DlepCounterNeighborMsgPeerNotUp_Object = MibTableColumn
dlepCounterNeighborMsgPeerNotUp = _DlepCounterNeighborMsgPeerNotUp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 34),
    _DlepCounterNeighborMsgPeerNotUp_Type()
)
dlepCounterNeighborMsgPeerNotUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterNeighborMsgPeerNotUp.setStatus("current")


class _DlepCounterPeerHeartbeatTimer_Type(Integer32):
    """Custom type dlepCounterPeerHeartbeatTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterPeerHeartbeatTimer_Type.__name__ = "Integer32"
_DlepCounterPeerHeartbeatTimer_Object = MibTableColumn
dlepCounterPeerHeartbeatTimer = _DlepCounterPeerHeartbeatTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 35),
    _DlepCounterPeerHeartbeatTimer_Type()
)
dlepCounterPeerHeartbeatTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterPeerHeartbeatTimer.setStatus("current")


class _DlepCounterPeerTerminateAckTimer_Type(Integer32):
    """Custom type dlepCounterPeerTerminateAckTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterPeerTerminateAckTimer_Type.__name__ = "Integer32"
_DlepCounterPeerTerminateAckTimer_Object = MibTableColumn
dlepCounterPeerTerminateAckTimer = _DlepCounterPeerTerminateAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 36),
    _DlepCounterPeerTerminateAckTimer_Type()
)
dlepCounterPeerTerminateAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterPeerTerminateAckTimer.setStatus("current")


class _DlepCounterNeighborTerminateAckTimer_Type(Integer32):
    """Custom type dlepCounterNeighborTerminateAckTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterNeighborTerminateAckTimer_Type.__name__ = "Integer32"
_DlepCounterNeighborTerminateAckTimer_Object = MibTableColumn
dlepCounterNeighborTerminateAckTimer = _DlepCounterNeighborTerminateAckTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 37),
    _DlepCounterNeighborTerminateAckTimer_Type()
)
dlepCounterNeighborTerminateAckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterNeighborTerminateAckTimer.setStatus("current")


class _DlepCounterRadioConnectTimer_Type(Integer32):
    """Custom type dlepCounterRadioConnectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlepCounterRadioConnectTimer_Type.__name__ = "Integer32"
_DlepCounterRadioConnectTimer_Object = MibTableColumn
dlepCounterRadioConnectTimer = _DlepCounterRadioConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 38),
    _DlepCounterRadioConnectTimer_Type()
)
dlepCounterRadioConnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCounterRadioConnectTimer.setStatus("current")


class _DlepCountersPeersSummary_Type(DisplayString):
    """Custom type dlepCountersPeersSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepCountersPeersSummary_Type.__name__ = "DisplayString"
_DlepCountersPeersSummary_Object = MibTableColumn
dlepCountersPeersSummary = _DlepCountersPeersSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 39),
    _DlepCountersPeersSummary_Type()
)
dlepCountersPeersSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCountersPeersSummary.setStatus("current")


class _DlepCountersNeighborsSummary_Type(DisplayString):
    """Custom type dlepCountersNeighborsSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepCountersNeighborsSummary_Type.__name__ = "DisplayString"
_DlepCountersNeighborsSummary_Object = MibTableColumn
dlepCountersNeighborsSummary = _DlepCountersNeighborsSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 40),
    _DlepCountersNeighborsSummary_Type()
)
dlepCountersNeighborsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCountersNeighborsSummary.setStatus("current")


class _DlepCountersExceptionsSummary_Type(DisplayString):
    """Custom type dlepCountersExceptionsSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepCountersExceptionsSummary_Type.__name__ = "DisplayString"
_DlepCountersExceptionsSummary_Object = MibTableColumn
dlepCountersExceptionsSummary = _DlepCountersExceptionsSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 41),
    _DlepCountersExceptionsSummary_Type()
)
dlepCountersExceptionsSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCountersExceptionsSummary.setStatus("current")


class _DlepCountersTimersSummary_Type(DisplayString):
    """Custom type dlepCountersTimersSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepCountersTimersSummary_Type.__name__ = "DisplayString"
_DlepCountersTimersSummary_Object = MibTableColumn
dlepCountersTimersSummary = _DlepCountersTimersSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 42),
    _DlepCountersTimersSummary_Type()
)
dlepCountersTimersSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepCountersTimersSummary.setStatus("current")


class _DlepLocalCountersSummary_Type(DisplayString):
    """Custom type dlepLocalCountersSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_DlepLocalCountersSummary_Type.__name__ = "DisplayString"
_DlepLocalCountersSummary_Object = MibTableColumn
dlepLocalCountersSummary = _DlepLocalCountersSummary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 1, 6, 1, 1, 43),
    _DlepLocalCountersSummary_Type()
)
dlepLocalCountersSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlepLocalCountersSummary.setStatus("current")

# Managed Objects groups


# Notification objects

dlepNeighborSessionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 0, 0, 0)
)
dlepNeighborSessionChange.setObjects(
      *(("CISCO-DLEP-MIB", "dlepNeighborInterfaceIndex"),
        ("CISCO-DLEP-MIB", "dlepNeighborSessionOperStatus"))
)
if mibBuilder.loadTexts:
    dlepNeighborSessionChange.setStatus(
        "current"
    )

dlepClientSessionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 1060, 0, 0, 1)
)
dlepClientSessionChange.setObjects(
      *(("CISCO-DLEP-MIB", "dlepClientInterfaceIndex"),
        ("CISCO-DLEP-MIB", "dlepClientSessionOperStatus"))
)
if mibBuilder.loadTexts:
    dlepClientSessionChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DLEP-MIB",
    **{"ciscoDlepMIB": ciscoDlepMIB,
       "ciscoDlepMIBNotifs": ciscoDlepMIBNotifs,
       "dlepMIBNotifications": dlepMIBNotifications,
       "dlepNeighborSessionChange": dlepNeighborSessionChange,
       "dlepClientSessionChange": dlepClientSessionChange,
       "ciscoDlepMIBObjects": ciscoDlepMIBObjects,
       "dlepGlobals": dlepGlobals,
       "dlepEnableIndividualNotifications": dlepEnableIndividualNotifications,
       "dlepInterface": dlepInterface,
       "dlepInterfaceTable": dlepInterfaceTable,
       "dlepInterfaceEntry": dlepInterfaceEntry,
       "dlepInterfaceIndex": dlepInterfaceIndex,
       "dlepInterfaceNbrSessionId": dlepInterfaceNbrSessionId,
       "dlepInterfaceName": dlepInterfaceName,
       "dlepNeighbor": dlepNeighbor,
       "dlepNeighborTable": dlepNeighborTable,
       "dlepNeighborEntry": dlepNeighborEntry,
       "dlepNeighborSessionId": dlepNeighborSessionId,
       "dlepNeighborInterfaceIndex": dlepNeighborInterfaceIndex,
       "dlepNeighborInterfaceName": dlepNeighborInterfaceName,
       "dlepNeighborAddress": dlepNeighborAddress,
       "dlepNeighborAddressV6LL": dlepNeighborAddressV6LL,
       "dlepNeighborAddressV6GBL": dlepNeighborAddressV6GBL,
       "dlepNeighborIpUpTime": dlepNeighborIpUpTime,
       "dlepNeighborMetricsMTU": dlepNeighborMetricsMTU,
       "dlepNeighborMetricsCdrRx": dlepNeighborMetricsCdrRx,
       "dlepNeighborMetricsCdrTx": dlepNeighborMetricsCdrTx,
       "dlepNeighborMetricsMdrRx": dlepNeighborMetricsMdrRx,
       "dlepNeighborMetricsMdrTx": dlepNeighborMetricsMdrTx,
       "dlepNeighborMetricsRlqRx": dlepNeighborMetricsRlqRx,
       "dlepNeighborMetricsRlqTx": dlepNeighborMetricsRlqTx,
       "dlepNeighborMetricsLatency": dlepNeighborMetricsLatency,
       "dlepNeighborMetricsResources": dlepNeighborMetricsResources,
       "dlepNeighborMetricsVac": dlepNeighborMetricsVac,
       "dlepNeighborMetricsMacAddress": dlepNeighborMetricsMacAddress,
       "dlepNeighborSessionOperStatus": dlepNeighborSessionOperStatus,
       "dlepClient": dlepClient,
       "dlepClientTable": dlepClientTable,
       "dlepClientEntry": dlepClientEntry,
       "dlepClientInterfaceIndex": dlepClientInterfaceIndex,
       "dlepClientInterfaceName": dlepClientInterfaceName,
       "dlepClientPeerId": dlepClientPeerId,
       "dlepNeighborCount": dlepNeighborCount,
       "dlepClientDescription": dlepClientDescription,
       "dlepClientAddressType": dlepClientAddressType,
       "dlepClientLocalAddress": dlepClientLocalAddress,
       "dlepClientLocalRadioAddress": dlepClientLocalRadioAddress,
       "dlepClientUpTime": dlepClientUpTime,
       "dlepClientMetricsCdrRx": dlepClientMetricsCdrRx,
       "dlepClientMetricsCdrTx": dlepClientMetricsCdrTx,
       "dlepClientMetricsMdrRx": dlepClientMetricsMdrRx,
       "dlepClientMetricsMdrTx": dlepClientMetricsMdrTx,
       "dlepClientMetricsRlqRx": dlepClientMetricsRlqRx,
       "dlepClientMetricsRlqTx": dlepClientMetricsRlqTx,
       "dlepClientMetricsLatency": dlepClientMetricsLatency,
       "dlepClientMetricsResources": dlepClientMetricsResources,
       "dlepClientMetricsMTU": dlepClientMetricsMTU,
       "dlepClientPort": dlepClientPort,
       "dlepClientConfigVT": dlepClientConfigVT,
       "dlepClientConfigHeartBeat": dlepClientConfigHeartBeat,
       "dlepClientConfigDeadInterval": dlepClientConfigDeadInterval,
       "dlepClientConfigTerminate": dlepClientConfigTerminate,
       "dlepConfigNeighborDown": dlepConfigNeighborDown,
       "dlepClientSessionOperStatus": dlepClientSessionOperStatus,
       "dlepClientMetricsSummary": dlepClientMetricsSummary,
       "dlepClientConfigSummary": dlepClientConfigSummary,
       "dlepConfig": dlepConfig,
       "dlepConfigTable": dlepConfigTable,
       "dlepConfigEntry": dlepConfigEntry,
       "dlepConfigInterfaceIndex": dlepConfigInterfaceIndex,
       "dlepConfigInterfaceName": dlepConfigInterfaceName,
       "dlepConfigPeerInterfaceDescription": dlepConfigPeerInterfaceDescription,
       "dlepConfigLocalAddressType": dlepConfigLocalAddressType,
       "dlepConfigLocalAddress": dlepConfigLocalAddress,
       "dlepConfigLocalTCPPort": dlepConfigLocalTCPPort,
       "dlepConfigLocalUDPPort": dlepConfigLocalUDPPort,
       "dlepConfigRemoteAddressType": dlepConfigRemoteAddressType,
       "dlepConfigRemoteAddress": dlepConfigRemoteAddress,
       "dlepConfigRemoteTCPPort": dlepConfigRemoteTCPPort,
       "dlepConfigRemoteUDPPort": dlepConfigRemoteUDPPort,
       "dlepConfigSessionMode": dlepConfigSessionMode,
       "dlepConfigVirtualTemplate": dlepConfigVirtualTemplate,
       "dlepConfigMissedHeartbeatThreshold": dlepConfigMissedHeartbeatThreshold,
       "dlepConfigHeartbeatInterval": dlepConfigHeartbeatInterval,
       "dlepConfigDiscoveryInterval": dlepConfigDiscoveryInterval,
       "dlepConfigSessionAckTimeout": dlepConfigSessionAckTimeout,
       "dlepConfigPeerTerminateAckTimeout": dlepConfigPeerTerminateAckTimeout,
       "dlepConfigNeighborDownAckTimeout": dlepConfigNeighborDownAckTimeout,
       "dlepConfigSummary": dlepConfigSummary,
       "dlepCounters": dlepCounters,
       "dlepCountersTable": dlepCountersTable,
       "dlepCountersEntry": dlepCountersEntry,
       "dlepCounterInterfaceIndex": dlepCounterInterfaceIndex,
       "dlepCounterInterfaceName": dlepCounterInterfaceName,
       "dlepCounterLastClearTime": dlepCounterLastClearTime,
       "dlepCounterLocalIpType": dlepCounterLocalIpType,
       "dlepCounterLocalIp": dlepCounterLocalIp,
       "dlepCounterLocalTCPPort": dlepCounterLocalTCPPort,
       "dlepCounterLocalUDPPort": dlepCounterLocalUDPPort,
       "dlepCounterRXPeerDiscovery": dlepCounterRXPeerDiscovery,
       "dlepCounterRXPeerOffer": dlepCounterRXPeerOffer,
       "dlepCounterRXPeerInit": dlepCounterRXPeerInit,
       "dlepCounterRXPeerInitAck": dlepCounterRXPeerInitAck,
       "dlepCounterRXHeartbeat": dlepCounterRXHeartbeat,
       "dlepCounterRXPeerTerminate": dlepCounterRXPeerTerminate,
       "dlepCounterRXPeerTerminateAck": dlepCounterRXPeerTerminateAck,
       "dlepCounterTXPeerOffer": dlepCounterTXPeerOffer,
       "dlepCounterTXPeerDiscovery": dlepCounterTXPeerDiscovery,
       "dlepCounterTXPeerInitAck": dlepCounterTXPeerInitAck,
       "dlepCounterTXPeerInit": dlepCounterTXPeerInit,
       "dlepCounterTXHeartbeat": dlepCounterTXHeartbeat,
       "dlepCounterTXPeerTerminateAck": dlepCounterTXPeerTerminateAck,
       "dlepCounterTXPeerTerminate": dlepCounterTXPeerTerminate,
       "dlepCounterRXNeighborUp": dlepCounterRXNeighborUp,
       "dlepCounterRXMetric": dlepCounterRXMetric,
       "dlepCounterRXNeighborDown": dlepCounterRXNeighborDown,
       "dlepCounterRXNeighborDownAck": dlepCounterRXNeighborDownAck,
       "dlepCounterTXNeighborUpAck": dlepCounterTXNeighborUpAck,
       "dlepCounterTXNeighborDownAck": dlepCounterTXNeighborDownAck,
       "dlepCounterTXNeighborDown": dlepCounterTXNeighborDown,
       "dlepCounterRXInvalidMessage": dlepCounterRXInvalidMessage,
       "dlepCounterPreExistingNeighbor": dlepCounterPreExistingNeighbor,
       "dlepCounterNeighborNotFound": dlepCounterNeighborNotFound,
       "dlepCounterRXUnknownMessage": dlepCounterRXUnknownMessage,
       "dlepCounterNeighborResourceError": dlepCounterNeighborResourceError,
       "dlepCounterNeighborMsgPeerNotUp": dlepCounterNeighborMsgPeerNotUp,
       "dlepCounterPeerHeartbeatTimer": dlepCounterPeerHeartbeatTimer,
       "dlepCounterPeerTerminateAckTimer": dlepCounterPeerTerminateAckTimer,
       "dlepCounterNeighborTerminateAckTimer": dlepCounterNeighborTerminateAckTimer,
       "dlepCounterRadioConnectTimer": dlepCounterRadioConnectTimer,
       "dlepCountersPeersSummary": dlepCountersPeersSummary,
       "dlepCountersNeighborsSummary": dlepCountersNeighborsSummary,
       "dlepCountersExceptionsSummary": dlepCountersExceptionsSummary,
       "dlepCountersTimersSummary": dlepCountersTimersSummary,
       "dlepLocalCountersSummary": dlepLocalCountersSummary}
)
