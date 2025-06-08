# SNMP MIB module (FIREBRICK-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/firebrick_24693/FIREBRICK-CPU-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 23:00:30 2025
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

(firebrickNewStyle,) = mibBuilder.importSymbols(
    "FIREBRICK-MIB",
    "firebrickNewStyle")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fbCpuMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2)
)
if mibBuilder.loadTexts:
    fbCpuMib.setRevisions(
        ("2022-07-15 00:00",
         "2020-06-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FbCpuUsageTable_Object = MibTable
fbCpuUsageTable = _FbCpuUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1)
)
if mibBuilder.loadTexts:
    fbCpuUsageTable.setStatus("current")
_FbCpuUsageEntry_Object = MibTableRow
fbCpuUsageEntry = _FbCpuUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1)
)
fbCpuUsageEntry.setIndexNames(
    (0, "FIREBRICK-CPU-MIB", "fbCpuPeriod"),
    (0, "FIREBRICK-CPU-MIB", "fbCpuCore"),
)
if mibBuilder.loadTexts:
    fbCpuUsageEntry.setStatus("current")
_FbCpuIRQ_Type = Gauge32
_FbCpuIRQ_Object = MibTableColumn
fbCpuIRQ = _FbCpuIRQ_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1, 1),
    _FbCpuIRQ_Type()
)
fbCpuIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbCpuIRQ.setStatus("current")
_FbCpuAll_Type = Gauge32
_FbCpuAll_Object = MibTableColumn
fbCpuAll = _FbCpuAll_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1, 2),
    _FbCpuAll_Type()
)
fbCpuAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbCpuAll.setStatus("current")
_FbCpuIRQPeak_Type = Gauge32
_FbCpuIRQPeak_Object = MibTableColumn
fbCpuIRQPeak = _FbCpuIRQPeak_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1, 3),
    _FbCpuIRQPeak_Type()
)
fbCpuIRQPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbCpuIRQPeak.setStatus("current")
_FbCpuAllPeak_Type = Gauge32
_FbCpuAllPeak_Object = MibTableColumn
fbCpuAllPeak = _FbCpuAllPeak_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1, 4),
    _FbCpuAllPeak_Type()
)
fbCpuAllPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fbCpuAllPeak.setStatus("current")
_FbCpuPeriod_Type = Integer32
_FbCpuPeriod_Object = MibTableColumn
fbCpuPeriod = _FbCpuPeriod_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1, 5),
    _FbCpuPeriod_Type()
)
fbCpuPeriod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbCpuPeriod.setStatus("current")
_FbCpuCore_Type = Integer32
_FbCpuCore_Object = MibTableColumn
fbCpuCore = _FbCpuCore_Object(
    (1, 3, 6, 1, 4, 1, 24693, 100, 2, 1, 1, 6),
    _FbCpuCore_Type()
)
fbCpuCore.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fbCpuCore.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREBRICK-CPU-MIB",
    **{"fbCpuMib": fbCpuMib,
       "fbCpuUsageTable": fbCpuUsageTable,
       "fbCpuUsageEntry": fbCpuUsageEntry,
       "fbCpuIRQ": fbCpuIRQ,
       "fbCpuAll": fbCpuAll,
       "fbCpuIRQPeak": fbCpuIRQPeak,
       "fbCpuAllPeak": fbCpuAllPeak,
       "fbCpuPeriod": fbCpuPeriod,
       "fbCpuCore": fbCpuCore}
)
