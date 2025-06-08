# SNMP MIB module (METEL-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/metel_38616/METEL-TRAPS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:24:38 2025
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

(device,) = mibBuilder.importSymbols(
    "METEL-MIB",
    "device")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100)
)
if mibBuilder.loadTexts:
    traps.setRevisions(
        ("2018-03-14 00:00",
         "2015-11-04 00:00",
         "2012-07-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TrapsDstIpNumber_Type = Integer32
_TrapsDstIpNumber_Object = MibScalar
trapsDstIpNumber = _TrapsDstIpNumber_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 100),
    _TrapsDstIpNumber_Type()
)
trapsDstIpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsDstIpNumber.setStatus("current")
_TrapsDstIpTable_Object = MibTable
trapsDstIpTable = _TrapsDstIpTable_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101)
)
if mibBuilder.loadTexts:
    trapsDstIpTable.setStatus("current")
_TrapsDstIpEntry_Object = MibTableRow
trapsDstIpEntry = _TrapsDstIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101, 1)
)
trapsDstIpEntry.setIndexNames(
    (0, "METEL-TRAPS-MIB", "trapsDstIpIndex"),
)
if mibBuilder.loadTexts:
    trapsDstIpEntry.setStatus("current")


class _TrapsDstIpIndex_Type(Integer32):
    """Custom type trapsDstIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TrapsDstIpIndex_Type.__name__ = "Integer32"
_TrapsDstIpIndex_Object = MibTableColumn
trapsDstIpIndex = _TrapsDstIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101, 1, 1),
    _TrapsDstIpIndex_Type()
)
trapsDstIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapsDstIpIndex.setStatus("current")


class _TrapsDstIpEnable_Type(Integer32):
    """Custom type trapsDstIpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_TrapsDstIpEnable_Type.__name__ = "Integer32"
_TrapsDstIpEnable_Object = MibTableColumn
trapsDstIpEnable = _TrapsDstIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101, 1, 2),
    _TrapsDstIpEnable_Type()
)
trapsDstIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsDstIpEnable.setStatus("current")
_TrapsDstIpAddr_Type = IpAddress
_TrapsDstIpAddr_Object = MibTableColumn
trapsDstIpAddr = _TrapsDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101, 1, 3),
    _TrapsDstIpAddr_Type()
)
trapsDstIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsDstIpAddr.setStatus("current")
_TrapsDstPort_Type = Integer32
_TrapsDstPort_Object = MibTableColumn
trapsDstPort = _TrapsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101, 1, 4),
    _TrapsDstPort_Type()
)
trapsDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsDstPort.setStatus("current")


class _TrapsDstUsrName_Type(OctetString):
    """Custom type trapsDstUsrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_TrapsDstUsrName_Type.__name__ = "OctetString"
_TrapsDstUsrName_Object = MibTableColumn
trapsDstUsrName = _TrapsDstUsrName_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 101, 1, 5),
    _TrapsDstUsrName_Type()
)
trapsDstUsrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsDstUsrName.setStatus("current")
_TrapsTotalCnt_Type = Integer32
_TrapsTotalCnt_Object = MibScalar
trapsTotalCnt = _TrapsTotalCnt_Object(
    (1, 3, 6, 1, 4, 1, 38616, 1, 100, 102),
    _TrapsTotalCnt_Type()
)
trapsTotalCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapsTotalCnt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "METEL-TRAPS-MIB",
    **{"traps": traps,
       "trapsDstIpNumber": trapsDstIpNumber,
       "trapsDstIpTable": trapsDstIpTable,
       "trapsDstIpEntry": trapsDstIpEntry,
       "trapsDstIpIndex": trapsDstIpIndex,
       "trapsDstIpEnable": trapsDstIpEnable,
       "trapsDstIpAddr": trapsDstIpAddr,
       "trapsDstPort": trapsDstPort,
       "trapsDstUsrName": trapsDstUsrName,
       "trapsTotalCnt": trapsTotalCnt}
)
