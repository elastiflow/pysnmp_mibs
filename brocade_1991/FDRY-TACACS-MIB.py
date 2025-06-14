# SNMP MIB module (FDRY-TACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FDRY-TACACS-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:18:53 2025
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

(ServerUsage,) = mibBuilder.importSymbols(
    "FDRY-RADIUS-MIB",
    "ServerUsage")

(fdryTacacs,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdryTacacs")

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
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fdryTacacsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    fdryTacacsMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryTacacsServer_ObjectIdentity = ObjectIdentity
fdryTacacsServer = _FdryTacacsServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1)
)
_FdryTacacsServerTable_Object = MibTable
fdryTacacsServerTable = _FdryTacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdryTacacsServerTable.setStatus("current")
_FdryTacacsServerEntry_Object = MibTableRow
fdryTacacsServerEntry = _FdryTacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1)
)
fdryTacacsServerEntry.setIndexNames(
    (0, "FDRY-TACACS-MIB", "fdryTacacsServerIndex"),
)
if mibBuilder.loadTexts:
    fdryTacacsServerEntry.setStatus("current")
_FdryTacacsServerIndex_Type = Unsigned32
_FdryTacacsServerIndex_Object = MibTableColumn
fdryTacacsServerIndex = _FdryTacacsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 1),
    _FdryTacacsServerIndex_Type()
)
fdryTacacsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryTacacsServerIndex.setStatus("current")


class _FdryTacacsServerAddrType_Type(InetAddressType):
    """Custom type fdryTacacsServerAddrType based on InetAddressType"""
    defaultValue = 1


_FdryTacacsServerAddrType_Type.__name__ = "InetAddressType"
_FdryTacacsServerAddrType_Object = MibTableColumn
fdryTacacsServerAddrType = _FdryTacacsServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 2),
    _FdryTacacsServerAddrType_Type()
)
fdryTacacsServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTacacsServerAddrType.setStatus("current")
_FdryTacacsServerAddr_Type = InetAddress
_FdryTacacsServerAddr_Object = MibTableColumn
fdryTacacsServerAddr = _FdryTacacsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 3),
    _FdryTacacsServerAddr_Type()
)
fdryTacacsServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTacacsServerAddr.setStatus("current")


class _FdryTacacsServerAuthPort_Type(Unsigned32):
    """Custom type fdryTacacsServerAuthPort based on Unsigned32"""
    defaultValue = 49


_FdryTacacsServerAuthPort_Type.__name__ = "Unsigned32"
_FdryTacacsServerAuthPort_Object = MibTableColumn
fdryTacacsServerAuthPort = _FdryTacacsServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 4),
    _FdryTacacsServerAuthPort_Type()
)
fdryTacacsServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTacacsServerAuthPort.setStatus("current")
_FdryTacacsServerRowKey_Type = DisplayString
_FdryTacacsServerRowKey_Object = MibTableColumn
fdryTacacsServerRowKey = _FdryTacacsServerRowKey_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 5),
    _FdryTacacsServerRowKey_Type()
)
fdryTacacsServerRowKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTacacsServerRowKey.setStatus("current")


class _FdryTacacsServerUsage_Type(ServerUsage):
    """Custom type fdryTacacsServerUsage based on ServerUsage"""
    defaultValue = 1


_FdryTacacsServerUsage_Type.__name__ = "ServerUsage"
_FdryTacacsServerUsage_Object = MibTableColumn
fdryTacacsServerUsage = _FdryTacacsServerUsage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 6),
    _FdryTacacsServerUsage_Type()
)
fdryTacacsServerUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTacacsServerUsage.setStatus("current")
_FdryTacacsServerRowStatus_Type = RowStatus
_FdryTacacsServerRowStatus_Object = MibTableColumn
fdryTacacsServerRowStatus = _FdryTacacsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 9, 1, 1, 1, 1, 7),
    _FdryTacacsServerRowStatus_Type()
)
fdryTacacsServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryTacacsServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-TACACS-MIB",
    **{"fdryTacacsMIB": fdryTacacsMIB,
       "fdryTacacsServer": fdryTacacsServer,
       "fdryTacacsServerTable": fdryTacacsServerTable,
       "fdryTacacsServerEntry": fdryTacacsServerEntry,
       "fdryTacacsServerIndex": fdryTacacsServerIndex,
       "fdryTacacsServerAddrType": fdryTacacsServerAddrType,
       "fdryTacacsServerAddr": fdryTacacsServerAddr,
       "fdryTacacsServerAuthPort": fdryTacacsServerAuthPort,
       "fdryTacacsServerRowKey": fdryTacacsServerRowKey,
       "fdryTacacsServerUsage": fdryTacacsServerUsage,
       "fdryTacacsServerRowStatus": fdryTacacsServerRowStatus}
)
