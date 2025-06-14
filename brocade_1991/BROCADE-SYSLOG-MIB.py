# SNMP MIB module (BROCADE-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/brocade_1991/BROCADE-SYSLOG-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 10:20:39 2025
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

(brcdSysLog,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "brcdSysLog")

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

brocadeSysLogMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    brocadeSysLogMIB.setRevisions(
        ("2011-11-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BrcdSysLogGroup_ObjectIdentity = ObjectIdentity
brcdSysLogGroup = _BrcdSysLogGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1)
)
_BrcdSysLogServerTable_Object = MibTable
brcdSysLogServerTable = _BrcdSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    brcdSysLogServerTable.setStatus("current")
_BrcdSysLogServerEntry_Object = MibTableRow
brcdSysLogServerEntry = _BrcdSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1)
)
brcdSysLogServerEntry.setIndexNames(
    (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerAddrType"),
    (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerAddr"),
    (0, "BROCADE-SYSLOG-MIB", "brcdSysLogServerUDPPort"),
)
if mibBuilder.loadTexts:
    brcdSysLogServerEntry.setStatus("current")
_BrcdSysLogServerAddrType_Type = InetAddressType
_BrcdSysLogServerAddrType_Object = MibTableColumn
brcdSysLogServerAddrType = _BrcdSysLogServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 1),
    _BrcdSysLogServerAddrType_Type()
)
brcdSysLogServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSysLogServerAddrType.setStatus("current")
_BrcdSysLogServerAddr_Type = InetAddress
_BrcdSysLogServerAddr_Object = MibTableColumn
brcdSysLogServerAddr = _BrcdSysLogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 2),
    _BrcdSysLogServerAddr_Type()
)
brcdSysLogServerAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSysLogServerAddr.setStatus("current")


class _BrcdSysLogServerUDPPort_Type(Unsigned32):
    """Custom type brcdSysLogServerUDPPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BrcdSysLogServerUDPPort_Type.__name__ = "Unsigned32"
_BrcdSysLogServerUDPPort_Object = MibTableColumn
brcdSysLogServerUDPPort = _BrcdSysLogServerUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 3),
    _BrcdSysLogServerUDPPort_Type()
)
brcdSysLogServerUDPPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    brcdSysLogServerUDPPort.setStatus("current")
_BrcdSysLogServerOutPkts_Type = Counter32
_BrcdSysLogServerOutPkts_Object = MibTableColumn
brcdSysLogServerOutPkts = _BrcdSysLogServerOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 4),
    _BrcdSysLogServerOutPkts_Type()
)
brcdSysLogServerOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brcdSysLogServerOutPkts.setStatus("current")
_BrcdSysLogServerRowStatus_Type = RowStatus
_BrcdSysLogServerRowStatus_Object = MibTableColumn
brcdSysLogServerRowStatus = _BrcdSysLogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 11, 1, 1, 1, 1, 5),
    _BrcdSysLogServerRowStatus_Type()
)
brcdSysLogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    brcdSysLogServerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BROCADE-SYSLOG-MIB",
    **{"brocadeSysLogMIB": brocadeSysLogMIB,
       "brcdSysLogGroup": brcdSysLogGroup,
       "brcdSysLogServerTable": brcdSysLogServerTable,
       "brcdSysLogServerEntry": brcdSysLogServerEntry,
       "brcdSysLogServerAddrType": brcdSysLogServerAddrType,
       "brcdSysLogServerAddr": brcdSysLogServerAddr,
       "brcdSysLogServerUDPPort": brcdSysLogServerUDPPort,
       "brcdSysLogServerOutPkts": brcdSysLogServerOutPkts,
       "brcdSysLogServerRowStatus": brcdSysLogServerRowStatus}
)
