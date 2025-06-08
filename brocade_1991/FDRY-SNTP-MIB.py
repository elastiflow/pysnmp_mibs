# SNMP MIB module (FDRY-SNTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/FDRY-SNTP-MIB.mib
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

(fdrySntp,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "fdrySntp")

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

fdrySntpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fdrySntpMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-02-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdrySntpServer_ObjectIdentity = ObjectIdentity
fdrySntpServer = _FdrySntpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1)
)
_FdrySntpServerTable_Object = MibTable
fdrySntpServerTable = _FdrySntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fdrySntpServerTable.setStatus("current")
_FdrySntpServerEntry_Object = MibTableRow
fdrySntpServerEntry = _FdrySntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1)
)
fdrySntpServerEntry.setIndexNames(
    (0, "FDRY-SNTP-MIB", "fdrySntpServerIndex"),
)
if mibBuilder.loadTexts:
    fdrySntpServerEntry.setStatus("current")
_FdrySntpServerIndex_Type = Unsigned32
_FdrySntpServerIndex_Object = MibTableColumn
fdrySntpServerIndex = _FdrySntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 1),
    _FdrySntpServerIndex_Type()
)
fdrySntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdrySntpServerIndex.setStatus("current")


class _FdrySntpServerAddrType_Type(InetAddressType):
    """Custom type fdrySntpServerAddrType based on InetAddressType"""
    defaultValue = 1


_FdrySntpServerAddrType_Type.__name__ = "InetAddressType"
_FdrySntpServerAddrType_Object = MibTableColumn
fdrySntpServerAddrType = _FdrySntpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 2),
    _FdrySntpServerAddrType_Type()
)
fdrySntpServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerAddrType.setStatus("current")
_FdrySntpServerAddr_Type = InetAddress
_FdrySntpServerAddr_Object = MibTableColumn
fdrySntpServerAddr = _FdrySntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 3),
    _FdrySntpServerAddr_Type()
)
fdrySntpServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerAddr.setStatus("current")


class _FdrySntpServerVersion_Type(Integer32):
    """Custom type fdrySntpServerVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FdrySntpServerVersion_Type.__name__ = "Integer32"
_FdrySntpServerVersion_Object = MibTableColumn
fdrySntpServerVersion = _FdrySntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 4),
    _FdrySntpServerVersion_Type()
)
fdrySntpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerVersion.setStatus("current")
_FdrySntpServerRowStatus_Type = RowStatus
_FdrySntpServerRowStatus_Object = MibTableColumn
fdrySntpServerRowStatus = _FdrySntpServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 7, 1, 1, 1, 1, 5),
    _FdrySntpServerRowStatus_Type()
)
fdrySntpServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdrySntpServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-SNTP-MIB",
    **{"fdrySntpMIB": fdrySntpMIB,
       "fdrySntpServer": fdrySntpServer,
       "fdrySntpServerTable": fdrySntpServerTable,
       "fdrySntpServerEntry": fdrySntpServerEntry,
       "fdrySntpServerIndex": fdrySntpServerIndex,
       "fdrySntpServerAddrType": fdrySntpServerAddrType,
       "fdrySntpServerAddr": fdrySntpServerAddr,
       "fdrySntpServerVersion": fdrySntpServerVersion,
       "fdrySntpServerRowStatus": fdrySntpServerRowStatus}
)
