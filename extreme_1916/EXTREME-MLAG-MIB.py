# SNMP MIB module (EXTREME-MLAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/extreme_1916/EXTREME-MLAG-MIB.mib
# Produced by pysmi-1.6.1 at Tue Jun  3 16:23:18 2025
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

extremeMlag = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41)
)
if mibBuilder.loadTexts:
    extremeMlag.setRevisions(
        ("2018-05-17 14:05",
         "2018-04-04 05:00",
         "2017-01-05 00:00",
         "2013-08-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeMlagObjects_ObjectIdentity = ObjectIdentity
extremeMlagObjects = _ExtremeMlagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1)
)
_ExtremeMlagPeerTable_Object = MibTable
extremeMlagPeerTable = _ExtremeMlagPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1)
)
if mibBuilder.loadTexts:
    extremeMlagPeerTable.setStatus("current")
_ExtremeMlagPeerEntry_Object = MibTableRow
extremeMlagPeerEntry = _ExtremeMlagPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1)
)
extremeMlagPeerEntry.setIndexNames(
    (0, "EXTREME-MLAG-MIB", "extremeMlagPeerName"),
)
if mibBuilder.loadTexts:
    extremeMlagPeerEntry.setStatus("current")


class _ExtremeMlagPeerName_Type(DisplayString):
    """Custom type extremeMlagPeerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerName_Type.__name__ = "DisplayString"
_ExtremeMlagPeerName_Object = MibTableColumn
extremeMlagPeerName = _ExtremeMlagPeerName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 1),
    _ExtremeMlagPeerName_Type()
)
extremeMlagPeerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerName.setStatus("current")


class _ExtremeMlagPeerVlan_Type(DisplayString):
    """Custom type extremeMlagPeerVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerVlan_Type.__name__ = "DisplayString"
_ExtremeMlagPeerVlan_Object = MibTableColumn
extremeMlagPeerVlan = _ExtremeMlagPeerVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 2),
    _ExtremeMlagPeerVlan_Type()
)
extremeMlagPeerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerVlan.setStatus("current")


class _ExtremeMlagPeerVR_Type(DisplayString):
    """Custom type extremeMlagPeerVR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerVR_Type.__name__ = "DisplayString"
_ExtremeMlagPeerVR_Object = MibTableColumn
extremeMlagPeerVR = _ExtremeMlagPeerVR_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 3),
    _ExtremeMlagPeerVR_Type()
)
extremeMlagPeerVR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerVR.setStatus("current")
_ExtremeMlagLocalAddrType_Type = InetAddressType
_ExtremeMlagLocalAddrType_Object = MibTableColumn
extremeMlagLocalAddrType = _ExtremeMlagLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 4),
    _ExtremeMlagLocalAddrType_Type()
)
extremeMlagLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagLocalAddrType.setStatus("current")
_ExtremeMlagLocalIP_Type = InetAddress
_ExtremeMlagLocalIP_Object = MibTableColumn
extremeMlagLocalIP = _ExtremeMlagLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 5),
    _ExtremeMlagLocalIP_Type()
)
extremeMlagLocalIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagLocalIP.setStatus("current")


class _ExtremeMlagPeerAddrType_Type(InetAddressType):
    """Custom type extremeMlagPeerAddrType based on InetAddressType"""
    defaultValue = 1


_ExtremeMlagPeerAddrType_Type.__name__ = "InetAddressType"
_ExtremeMlagPeerAddrType_Object = MibTableColumn
extremeMlagPeerAddrType = _ExtremeMlagPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 6),
    _ExtremeMlagPeerAddrType_Type()
)
extremeMlagPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerAddrType.setStatus("current")
_ExtremeMlagPeerIP_Type = InetAddress
_ExtremeMlagPeerIP_Object = MibTableColumn
extremeMlagPeerIP = _ExtremeMlagPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 7),
    _ExtremeMlagPeerIP_Type()
)
extremeMlagPeerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerIP.setStatus("current")
_ExtremeMlagPeerPortCount_Type = Integer32
_ExtremeMlagPeerPortCount_Object = MibTableColumn
extremeMlagPeerPortCount = _ExtremeMlagPeerPortCount_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 8),
    _ExtremeMlagPeerPortCount_Type()
)
extremeMlagPeerPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerPortCount.setStatus("current")


class _ExtremeMlagPeerCheckPointStatus_Type(Integer32):
    """Custom type extremeMlagPeerCheckPointStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ExtremeMlagPeerCheckPointStatus_Type.__name__ = "Integer32"
_ExtremeMlagPeerCheckPointStatus_Object = MibTableColumn
extremeMlagPeerCheckPointStatus = _ExtremeMlagPeerCheckPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 9),
    _ExtremeMlagPeerCheckPointStatus_Type()
)
extremeMlagPeerCheckPointStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerCheckPointStatus.setStatus("current")
_ExtremeMlagPeerRxHellos_Type = Counter32
_ExtremeMlagPeerRxHellos_Object = MibTableColumn
extremeMlagPeerRxHellos = _ExtremeMlagPeerRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 10),
    _ExtremeMlagPeerRxHellos_Type()
)
extremeMlagPeerRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerRxHellos.setStatus("current")
_ExtremeMlagPeerRxCheckpointMsgs_Type = Counter32
_ExtremeMlagPeerRxCheckpointMsgs_Object = MibTableColumn
extremeMlagPeerRxCheckpointMsgs = _ExtremeMlagPeerRxCheckpointMsgs_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 11),
    _ExtremeMlagPeerRxCheckpointMsgs_Type()
)
extremeMlagPeerRxCheckpointMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerRxCheckpointMsgs.setStatus("current")
_ExtremeMlagPeerHelloErrors_Type = Counter32
_ExtremeMlagPeerHelloErrors_Object = MibTableColumn
extremeMlagPeerHelloErrors = _ExtremeMlagPeerHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 12),
    _ExtremeMlagPeerHelloErrors_Type()
)
extremeMlagPeerHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerHelloErrors.setStatus("current")
_ExtremeMlagPeerHelloTimeouts_Type = Counter32
_ExtremeMlagPeerHelloTimeouts_Object = MibTableColumn
extremeMlagPeerHelloTimeouts = _ExtremeMlagPeerHelloTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 13),
    _ExtremeMlagPeerHelloTimeouts_Type()
)
extremeMlagPeerHelloTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerHelloTimeouts.setStatus("current")
_ExtremeMlagPeerUptime_Type = TimeStamp
_ExtremeMlagPeerUptime_Object = MibTableColumn
extremeMlagPeerUptime = _ExtremeMlagPeerUptime_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 14),
    _ExtremeMlagPeerUptime_Type()
)
extremeMlagPeerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerUptime.setStatus("current")


class _ExtremeMlagPeerLocalTxInterval_Type(Integer32):
    """Custom type extremeMlagPeerLocalTxInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_ExtremeMlagPeerLocalTxInterval_Type.__name__ = "Integer32"
_ExtremeMlagPeerLocalTxInterval_Object = MibTableColumn
extremeMlagPeerLocalTxInterval = _ExtremeMlagPeerLocalTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 15),
    _ExtremeMlagPeerLocalTxInterval_Type()
)
extremeMlagPeerLocalTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerLocalTxInterval.setStatus("current")


class _ExtremeMlagPeerRemoteTxInterval_Type(Integer32):
    """Custom type extremeMlagPeerRemoteTxInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_ExtremeMlagPeerRemoteTxInterval_Type.__name__ = "Integer32"
_ExtremeMlagPeerRemoteTxInterval_Object = MibTableColumn
extremeMlagPeerRemoteTxInterval = _ExtremeMlagPeerRemoteTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 16),
    _ExtremeMlagPeerRemoteTxInterval_Type()
)
extremeMlagPeerRemoteTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerRemoteTxInterval.setStatus("current")
_ExtremeMlagPeerTxHellos_Type = Counter32
_ExtremeMlagPeerTxHellos_Object = MibTableColumn
extremeMlagPeerTxHellos = _ExtremeMlagPeerTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 17),
    _ExtremeMlagPeerTxHellos_Type()
)
extremeMlagPeerTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerTxHellos.setStatus("current")
_ExtremeMlagPeerTxCheckpoints_Type = Counter32
_ExtremeMlagPeerTxCheckpoints_Object = MibTableColumn
extremeMlagPeerTxCheckpoints = _ExtremeMlagPeerTxCheckpoints_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 18),
    _ExtremeMlagPeerTxCheckpoints_Type()
)
extremeMlagPeerTxCheckpoints.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerTxCheckpoints.setStatus("current")
_ExtremeMlagPeerCheckpointErrors_Type = Counter32
_ExtremeMlagPeerCheckpointErrors_Object = MibTableColumn
extremeMlagPeerCheckpointErrors = _ExtremeMlagPeerCheckpointErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 19),
    _ExtremeMlagPeerCheckpointErrors_Type()
)
extremeMlagPeerCheckpointErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerCheckpointErrors.setStatus("current")
_ExtremeMlagPeerConnnectErrors_Type = Counter32
_ExtremeMlagPeerConnnectErrors_Object = MibTableColumn
extremeMlagPeerConnnectErrors = _ExtremeMlagPeerConnnectErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 20),
    _ExtremeMlagPeerConnnectErrors_Type()
)
extremeMlagPeerConnnectErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerConnnectErrors.setStatus("current")
_ExtremeMlagPeerRowStatus_Type = RowStatus
_ExtremeMlagPeerRowStatus_Object = MibTableColumn
extremeMlagPeerRowStatus = _ExtremeMlagPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 21),
    _ExtremeMlagPeerRowStatus_Type()
)
extremeMlagPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerRowStatus.setStatus("current")
_ExtremeMlagPeerCfgLacpMac_Type = MacAddress
_ExtremeMlagPeerCfgLacpMac_Object = MibTableColumn
extremeMlagPeerCfgLacpMac = _ExtremeMlagPeerCfgLacpMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 22),
    _ExtremeMlagPeerCfgLacpMac_Type()
)
extremeMlagPeerCfgLacpMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerCfgLacpMac.setStatus("current")
_ExtremeMlagPeerOperLacpMac_Type = MacAddress
_ExtremeMlagPeerOperLacpMac_Object = MibTableColumn
extremeMlagPeerOperLacpMac = _ExtremeMlagPeerOperLacpMac_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 23),
    _ExtremeMlagPeerOperLacpMac_Type()
)
extremeMlagPeerOperLacpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerOperLacpMac.setStatus("current")


class _ExtremeMlagPeerAlternateVlan_Type(DisplayString):
    """Custom type extremeMlagPeerAlternateVlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerAlternateVlan_Type.__name__ = "DisplayString"
_ExtremeMlagPeerAlternateVlan_Object = MibTableColumn
extremeMlagPeerAlternateVlan = _ExtremeMlagPeerAlternateVlan_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 24),
    _ExtremeMlagPeerAlternateVlan_Type()
)
extremeMlagPeerAlternateVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerAlternateVlan.setStatus("current")


class _ExtremeMlagPeerAlternateVR_Type(DisplayString):
    """Custom type extremeMlagPeerAlternateVR based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ExtremeMlagPeerAlternateVR_Type.__name__ = "DisplayString"
_ExtremeMlagPeerAlternateVR_Object = MibTableColumn
extremeMlagPeerAlternateVR = _ExtremeMlagPeerAlternateVR_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 25),
    _ExtremeMlagPeerAlternateVR_Type()
)
extremeMlagPeerAlternateVR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerAlternateVR.setStatus("current")
_ExtremeMlagAlternateLocalAddrType_Type = InetAddressType
_ExtremeMlagAlternateLocalAddrType_Object = MibTableColumn
extremeMlagAlternateLocalAddrType = _ExtremeMlagAlternateLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 26),
    _ExtremeMlagAlternateLocalAddrType_Type()
)
extremeMlagAlternateLocalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagAlternateLocalAddrType.setStatus("current")
_ExtremeMlagAlternateLocalIP_Type = InetAddress
_ExtremeMlagAlternateLocalIP_Object = MibTableColumn
extremeMlagAlternateLocalIP = _ExtremeMlagAlternateLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 27),
    _ExtremeMlagAlternateLocalIP_Type()
)
extremeMlagAlternateLocalIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagAlternateLocalIP.setStatus("current")


class _ExtremeMlagAlternatePeerAddrType_Type(InetAddressType):
    """Custom type extremeMlagAlternatePeerAddrType based on InetAddressType"""
    defaultValue = 1


_ExtremeMlagAlternatePeerAddrType_Type.__name__ = "InetAddressType"
_ExtremeMlagAlternatePeerAddrType_Object = MibTableColumn
extremeMlagAlternatePeerAddrType = _ExtremeMlagAlternatePeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 28),
    _ExtremeMlagAlternatePeerAddrType_Type()
)
extremeMlagAlternatePeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagAlternatePeerAddrType.setStatus("current")
_ExtremeMlagAlternatePeerIP_Type = InetAddress
_ExtremeMlagAlternatePeerIP_Object = MibTableColumn
extremeMlagAlternatePeerIP = _ExtremeMlagAlternatePeerIP_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 29),
    _ExtremeMlagAlternatePeerIP_Type()
)
extremeMlagAlternatePeerIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagAlternatePeerIP.setStatus("current")
_ExtremeMlagPeerAlternateRxHellos_Type = Counter32
_ExtremeMlagPeerAlternateRxHellos_Object = MibTableColumn
extremeMlagPeerAlternateRxHellos = _ExtremeMlagPeerAlternateRxHellos_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 30),
    _ExtremeMlagPeerAlternateRxHellos_Type()
)
extremeMlagPeerAlternateRxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerAlternateRxHellos.setStatus("current")
_ExtremeMlagPeerAlternateHelloErrors_Type = Counter32
_ExtremeMlagPeerAlternateHelloErrors_Object = MibTableColumn
extremeMlagPeerAlternateHelloErrors = _ExtremeMlagPeerAlternateHelloErrors_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 31),
    _ExtremeMlagPeerAlternateHelloErrors_Type()
)
extremeMlagPeerAlternateHelloErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerAlternateHelloErrors.setStatus("current")
_ExtremeMlagPeerAlternateHelloTimeouts_Type = Counter32
_ExtremeMlagPeerAlternateHelloTimeouts_Object = MibTableColumn
extremeMlagPeerAlternateHelloTimeouts = _ExtremeMlagPeerAlternateHelloTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 32),
    _ExtremeMlagPeerAlternateHelloTimeouts_Type()
)
extremeMlagPeerAlternateHelloTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerAlternateHelloTimeouts.setStatus("current")
_ExtremeMlagPeerAlternateTxHellos_Type = Counter32
_ExtremeMlagPeerAlternateTxHellos_Object = MibTableColumn
extremeMlagPeerAlternateTxHellos = _ExtremeMlagPeerAlternateTxHellos_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 33),
    _ExtremeMlagPeerAlternateTxHellos_Type()
)
extremeMlagPeerAlternateTxHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPeerAlternateTxHellos.setStatus("current")


class _ExtremeMlagPeerCheckPointAuthType_Type(Integer32):
    """Custom type extremeMlagPeerCheckPointAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("md5", 2))
    )


_ExtremeMlagPeerCheckPointAuthType_Type.__name__ = "Integer32"
_ExtremeMlagPeerCheckPointAuthType_Object = MibTableColumn
extremeMlagPeerCheckPointAuthType = _ExtremeMlagPeerCheckPointAuthType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 34),
    _ExtremeMlagPeerCheckPointAuthType_Type()
)
extremeMlagPeerCheckPointAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerCheckPointAuthType.setStatus("current")


class _ExtremeMlagPeerCheckpointAuthKey_Type(DisplayString):
    """Custom type extremeMlagPeerCheckpointAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_ExtremeMlagPeerCheckpointAuthKey_Type.__name__ = "DisplayString"
_ExtremeMlagPeerCheckpointAuthKey_Object = MibTableColumn
extremeMlagPeerCheckpointAuthKey = _ExtremeMlagPeerCheckpointAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 1, 1, 35),
    _ExtremeMlagPeerCheckpointAuthKey_Type()
)
extremeMlagPeerCheckpointAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPeerCheckpointAuthKey.setStatus("current")
_ExtremeMlagPortTable_Object = MibTable
extremeMlagPortTable = _ExtremeMlagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2)
)
if mibBuilder.loadTexts:
    extremeMlagPortTable.setStatus("current")
_ExtremeMlagPortEntry_Object = MibTableRow
extremeMlagPortEntry = _ExtremeMlagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1)
)
extremeMlagPortEntry.setIndexNames(
    (0, "EXTREME-MLAG-MIB", "extremeMlagPortLocalPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeMlagPortEntry.setStatus("current")
_ExtremeMlagPortLocalPortIfIndex_Type = Unsigned32
_ExtremeMlagPortLocalPortIfIndex_Object = MibTableColumn
extremeMlagPortLocalPortIfIndex = _ExtremeMlagPortLocalPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 1),
    _ExtremeMlagPortLocalPortIfIndex_Type()
)
extremeMlagPortLocalPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPortLocalPortIfIndex.setStatus("current")


class _ExtremeMlagPortId_Type(Integer32):
    """Custom type extremeMlagPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_ExtremeMlagPortId_Type.__name__ = "Integer32"
_ExtremeMlagPortId_Object = MibTableColumn
extremeMlagPortId = _ExtremeMlagPortId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 2),
    _ExtremeMlagPortId_Type()
)
extremeMlagPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPortId.setStatus("current")
_ExtremeMlagPortPeer_Type = DisplayString
_ExtremeMlagPortPeer_Object = MibTableColumn
extremeMlagPortPeer = _ExtremeMlagPortPeer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 3),
    _ExtremeMlagPortPeer_Type()
)
extremeMlagPortPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPortPeer.setStatus("current")


class _ExtremeMlagPortLocalLinkStatus_Type(Integer32):
    """Custom type extremeMlagPortLocalLinkStatus based on Integer32"""
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
        *(("active", 1),
          ("disabled", 2),
          ("ready", 3),
          ("portNotPresent", 4))
    )


_ExtremeMlagPortLocalLinkStatus_Type.__name__ = "Integer32"
_ExtremeMlagPortLocalLinkStatus_Object = MibTableColumn
extremeMlagPortLocalLinkStatus = _ExtremeMlagPortLocalLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 4),
    _ExtremeMlagPortLocalLinkStatus_Type()
)
extremeMlagPortLocalLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortLocalLinkStatus.setStatus("current")


class _ExtremeMlagPortRemoteLinkStatus_Type(Integer32):
    """Custom type extremeMlagPortRemoteLinkStatus based on Integer32"""
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
          ("notAvailable", 3))
    )


_ExtremeMlagPortRemoteLinkStatus_Type.__name__ = "Integer32"
_ExtremeMlagPortRemoteLinkStatus_Object = MibTableColumn
extremeMlagPortRemoteLinkStatus = _ExtremeMlagPortRemoteLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 5),
    _ExtremeMlagPortRemoteLinkStatus_Type()
)
extremeMlagPortRemoteLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortRemoteLinkStatus.setStatus("current")


class _ExtremeMlagPortPeerState_Type(Integer32):
    """Custom type extremeMlagPortPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_ExtremeMlagPortPeerState_Type.__name__ = "Integer32"
_ExtremeMlagPortPeerState_Object = MibTableColumn
extremeMlagPortPeerState = _ExtremeMlagPortPeerState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 6),
    _ExtremeMlagPortPeerState_Type()
)
extremeMlagPortPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortPeerState.setStatus("current")
_ExtremeMlagPortLocalFailures_Type = Counter32
_ExtremeMlagPortLocalFailures_Object = MibTableColumn
extremeMlagPortLocalFailures = _ExtremeMlagPortLocalFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 7),
    _ExtremeMlagPortLocalFailures_Type()
)
extremeMlagPortLocalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortLocalFailures.setStatus("current")
_ExtremeMlagPortRemoteFailures_Type = Counter32
_ExtremeMlagPortRemoteFailures_Object = MibTableColumn
extremeMlagPortRemoteFailures = _ExtremeMlagPortRemoteFailures_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 8),
    _ExtremeMlagPortRemoteFailures_Type()
)
extremeMlagPortRemoteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeMlagPortRemoteFailures.setStatus("current")
_ExtremeMlagPortRowStatus_Type = RowStatus
_ExtremeMlagPortRowStatus_Object = MibTableColumn
extremeMlagPortRowStatus = _ExtremeMlagPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 2, 1, 9),
    _ExtremeMlagPortRowStatus_Type()
)
extremeMlagPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeMlagPortRowStatus.setStatus("current")


class _ExtremeMlagConvergenceControl_Type(Integer32):
    """Custom type extremeMlagConvergenceControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastConvergence", 1),
          ("conserveAccessLists", 2))
    )


_ExtremeMlagConvergenceControl_Type.__name__ = "Integer32"
_ExtremeMlagConvergenceControl_Object = MibScalar
extremeMlagConvergenceControl = _ExtremeMlagConvergenceControl_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 3),
    _ExtremeMlagConvergenceControl_Type()
)
extremeMlagConvergenceControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagConvergenceControl.setStatus("current")


class _ExtremeMlagReloadDelayInterval_Type(Integer32):
    """Custom type extremeMlagReloadDelayInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1200),
    )


_ExtremeMlagReloadDelayInterval_Type.__name__ = "Integer32"
_ExtremeMlagReloadDelayInterval_Object = MibScalar
extremeMlagReloadDelayInterval = _ExtremeMlagReloadDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 4),
    _ExtremeMlagReloadDelayInterval_Type()
)
extremeMlagReloadDelayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagReloadDelayInterval.setStatus("current")


class _ExtremeMlagReloadDelayEnable_Type(TruthValue):
    """Custom type extremeMlagReloadDelayEnable based on TruthValue"""
    defaultValue = 2


_ExtremeMlagReloadDelayEnable_Type.__name__ = "TruthValue"
_ExtremeMlagReloadDelayEnable_Object = MibScalar
extremeMlagReloadDelayEnable = _ExtremeMlagReloadDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 5),
    _ExtremeMlagReloadDelayEnable_Type()
)
extremeMlagReloadDelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagReloadDelayEnable.setStatus("current")


class _ExtremeMlagLinkupIsolationEnable_Type(TruthValue):
    """Custom type extremeMlagLinkupIsolationEnable based on TruthValue"""
    defaultValue = 2


_ExtremeMlagLinkupIsolationEnable_Type.__name__ = "TruthValue"
_ExtremeMlagLinkupIsolationEnable_Object = MibScalar
extremeMlagLinkupIsolationEnable = _ExtremeMlagLinkupIsolationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 1, 6),
    _ExtremeMlagLinkupIsolationEnable_Type()
)
extremeMlagLinkupIsolationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeMlagLinkupIsolationEnable.setStatus("current")
_ExtremeMlagNotificationObjects_ObjectIdentity = ObjectIdentity
extremeMlagNotificationObjects = _ExtremeMlagNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 2)
)
_ExtremeMlagNotifications_ObjectIdentity = ObjectIdentity
extremeMlagNotifications = _ExtremeMlagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3)
)
_ExtremeMlagNotificationsPrefix_ObjectIdentity = ObjectIdentity
extremeMlagNotificationsPrefix = _ExtremeMlagNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0)
)

# Managed Objects groups


# Notification objects

extremeMlagPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0, 1)
)
extremeMlagPeerUp.setObjects(
    ("EXTREME-MLAG-MIB", "extremeMlagPeerName")
)
if mibBuilder.loadTexts:
    extremeMlagPeerUp.setStatus(
        "current"
    )

extremeMlagPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0, 2)
)
extremeMlagPeerDown.setObjects(
    ("EXTREME-MLAG-MIB", "extremeMlagPeerName")
)
if mibBuilder.loadTexts:
    extremeMlagPeerDown.setStatus(
        "current"
    )

extremeMlagAltPathUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0, 3)
)
extremeMlagAltPathUp.setObjects(
      *(("EXTREME-MLAG-MIB", "extremeMlagAlternatePeerAddrType"),
        ("EXTREME-MLAG-MIB", "extremeMlagAlternatePeerIP"))
)
if mibBuilder.loadTexts:
    extremeMlagAltPathUp.setStatus(
        "current"
    )

extremeMlagAltPathDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 41, 3, 0, 4)
)
extremeMlagAltPathDown.setObjects(
      *(("EXTREME-MLAG-MIB", "extremeMlagAlternatePeerAddrType"),
        ("EXTREME-MLAG-MIB", "extremeMlagAlternatePeerIP"))
)
if mibBuilder.loadTexts:
    extremeMlagAltPathDown.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-MLAG-MIB",
    **{"extremeMlag": extremeMlag,
       "extremeMlagObjects": extremeMlagObjects,
       "extremeMlagPeerTable": extremeMlagPeerTable,
       "extremeMlagPeerEntry": extremeMlagPeerEntry,
       "extremeMlagPeerName": extremeMlagPeerName,
       "extremeMlagPeerVlan": extremeMlagPeerVlan,
       "extremeMlagPeerVR": extremeMlagPeerVR,
       "extremeMlagLocalAddrType": extremeMlagLocalAddrType,
       "extremeMlagLocalIP": extremeMlagLocalIP,
       "extremeMlagPeerAddrType": extremeMlagPeerAddrType,
       "extremeMlagPeerIP": extremeMlagPeerIP,
       "extremeMlagPeerPortCount": extremeMlagPeerPortCount,
       "extremeMlagPeerCheckPointStatus": extremeMlagPeerCheckPointStatus,
       "extremeMlagPeerRxHellos": extremeMlagPeerRxHellos,
       "extremeMlagPeerRxCheckpointMsgs": extremeMlagPeerRxCheckpointMsgs,
       "extremeMlagPeerHelloErrors": extremeMlagPeerHelloErrors,
       "extremeMlagPeerHelloTimeouts": extremeMlagPeerHelloTimeouts,
       "extremeMlagPeerUptime": extremeMlagPeerUptime,
       "extremeMlagPeerLocalTxInterval": extremeMlagPeerLocalTxInterval,
       "extremeMlagPeerRemoteTxInterval": extremeMlagPeerRemoteTxInterval,
       "extremeMlagPeerTxHellos": extremeMlagPeerTxHellos,
       "extremeMlagPeerTxCheckpoints": extremeMlagPeerTxCheckpoints,
       "extremeMlagPeerCheckpointErrors": extremeMlagPeerCheckpointErrors,
       "extremeMlagPeerConnnectErrors": extremeMlagPeerConnnectErrors,
       "extremeMlagPeerRowStatus": extremeMlagPeerRowStatus,
       "extremeMlagPeerCfgLacpMac": extremeMlagPeerCfgLacpMac,
       "extremeMlagPeerOperLacpMac": extremeMlagPeerOperLacpMac,
       "extremeMlagPeerAlternateVlan": extremeMlagPeerAlternateVlan,
       "extremeMlagPeerAlternateVR": extremeMlagPeerAlternateVR,
       "extremeMlagAlternateLocalAddrType": extremeMlagAlternateLocalAddrType,
       "extremeMlagAlternateLocalIP": extremeMlagAlternateLocalIP,
       "extremeMlagAlternatePeerAddrType": extremeMlagAlternatePeerAddrType,
       "extremeMlagAlternatePeerIP": extremeMlagAlternatePeerIP,
       "extremeMlagPeerAlternateRxHellos": extremeMlagPeerAlternateRxHellos,
       "extremeMlagPeerAlternateHelloErrors": extremeMlagPeerAlternateHelloErrors,
       "extremeMlagPeerAlternateHelloTimeouts": extremeMlagPeerAlternateHelloTimeouts,
       "extremeMlagPeerAlternateTxHellos": extremeMlagPeerAlternateTxHellos,
       "extremeMlagPeerCheckPointAuthType": extremeMlagPeerCheckPointAuthType,
       "extremeMlagPeerCheckpointAuthKey": extremeMlagPeerCheckpointAuthKey,
       "extremeMlagPortTable": extremeMlagPortTable,
       "extremeMlagPortEntry": extremeMlagPortEntry,
       "extremeMlagPortLocalPortIfIndex": extremeMlagPortLocalPortIfIndex,
       "extremeMlagPortId": extremeMlagPortId,
       "extremeMlagPortPeer": extremeMlagPortPeer,
       "extremeMlagPortLocalLinkStatus": extremeMlagPortLocalLinkStatus,
       "extremeMlagPortRemoteLinkStatus": extremeMlagPortRemoteLinkStatus,
       "extremeMlagPortPeerState": extremeMlagPortPeerState,
       "extremeMlagPortLocalFailures": extremeMlagPortLocalFailures,
       "extremeMlagPortRemoteFailures": extremeMlagPortRemoteFailures,
       "extremeMlagPortRowStatus": extremeMlagPortRowStatus,
       "extremeMlagConvergenceControl": extremeMlagConvergenceControl,
       "extremeMlagReloadDelayInterval": extremeMlagReloadDelayInterval,
       "extremeMlagReloadDelayEnable": extremeMlagReloadDelayEnable,
       "extremeMlagLinkupIsolationEnable": extremeMlagLinkupIsolationEnable,
       "extremeMlagNotificationObjects": extremeMlagNotificationObjects,
       "extremeMlagNotifications": extremeMlagNotifications,
       "extremeMlagNotificationsPrefix": extremeMlagNotificationsPrefix,
       "extremeMlagPeerUp": extremeMlagPeerUp,
       "extremeMlagPeerDown": extremeMlagPeerDown,
       "extremeMlagAltPathUp": extremeMlagAltPathUp,
       "extremeMlagAltPathDown": extremeMlagAltPathDown}
)
