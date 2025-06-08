# SNMP MIB module (RUIJIE-INTERFACE-STATIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/ruijie_4881/RUIJIE-INTERFACE-STATIS-MIB.mib
# Produced by pysmi-1.6.1 at Sun Jun  8 11:04:17 2025
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

(ruijieInterfaceMIB,) = mibBuilder.importSymbols(
    "RUIJIE-INTERFACE-MIB",
    "ruijieInterfaceMIB")

(IfIndex,) = mibBuilder.importSymbols(
    "RUIJIE-TC",
    "IfIndex")

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

ruijieInterfaceStatisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4)
)
if mibBuilder.loadTexts:
    ruijieInterfaceStatisMIB.setRevisions(
        ("2010-02-01 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuijieIfErrStatisTable_Object = MibTable
ruijieIfErrStatisTable = _RuijieIfErrStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1)
)
if mibBuilder.loadTexts:
    ruijieIfErrStatisTable.setStatus("current")
_RuijieIfErrStatisEntry_Object = MibTableRow
ruijieIfErrStatisEntry = _RuijieIfErrStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1)
)
ruijieIfErrStatisEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-STATIS-MIB", "ruijieIfErrStatisIndex"),
)
if mibBuilder.loadTexts:
    ruijieIfErrStatisEntry.setStatus("current")
_RuijieIfErrStatisIndex_Type = IfIndex
_RuijieIfErrStatisIndex_Object = MibTableColumn
ruijieIfErrStatisIndex = _RuijieIfErrStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 1),
    _RuijieIfErrStatisIndex_Type()
)
ruijieIfErrStatisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfErrStatisIndex.setStatus("current")
_RuijieIfUnderSize_Type = Counter64
_RuijieIfUnderSize_Object = MibTableColumn
ruijieIfUnderSize = _RuijieIfUnderSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 2),
    _RuijieIfUnderSize_Type()
)
ruijieIfUnderSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfUnderSize.setStatus("current")
_RuijieIfOverSize_Type = Counter64
_RuijieIfOverSize_Object = MibTableColumn
ruijieIfOverSize = _RuijieIfOverSize_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 3),
    _RuijieIfOverSize_Type()
)
ruijieIfOverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfOverSize.setStatus("current")
_RuijieIfCollisions_Type = Counter64
_RuijieIfCollisions_Object = MibTableColumn
ruijieIfCollisions = _RuijieIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 4),
    _RuijieIfCollisions_Type()
)
ruijieIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfCollisions.setStatus("current")
_RuijieIfFragments_Type = Counter64
_RuijieIfFragments_Object = MibTableColumn
ruijieIfFragments = _RuijieIfFragments_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 5),
    _RuijieIfFragments_Type()
)
ruijieIfFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFragments.setStatus("current")
_RuijieIfJabbers_Type = Counter64
_RuijieIfJabbers_Object = MibTableColumn
ruijieIfJabbers = _RuijieIfJabbers_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 6),
    _RuijieIfJabbers_Type()
)
ruijieIfJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfJabbers.setStatus("current")
_RuijieIfCRCerror_Type = Counter64
_RuijieIfCRCerror_Object = MibTableColumn
ruijieIfCRCerror = _RuijieIfCRCerror_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 7),
    _RuijieIfCRCerror_Type()
)
ruijieIfCRCerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfCRCerror.setStatus("current")
_RuijieIfAlignerror_Type = Counter64
_RuijieIfAlignerror_Object = MibTableColumn
ruijieIfAlignerror = _RuijieIfAlignerror_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 8),
    _RuijieIfAlignerror_Type()
)
ruijieIfAlignerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfAlignerror.setStatus("current")
_RuijieIfFECerror_Type = Counter64
_RuijieIfFECerror_Object = MibTableColumn
ruijieIfFECerror = _RuijieIfFECerror_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 1, 1, 9),
    _RuijieIfFECerror_Type()
)
ruijieIfFECerror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfFECerror.setStatus("current")
_RuijieIfIpStatisTable_Object = MibTable
ruijieIfIpStatisTable = _RuijieIfIpStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2)
)
if mibBuilder.loadTexts:
    ruijieIfIpStatisTable.setStatus("current")
_RuijieIfIpStatisEntry_Object = MibTableRow
ruijieIfIpStatisEntry = _RuijieIfIpStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1)
)
ruijieIfIpStatisEntry.setIndexNames(
    (0, "RUIJIE-INTERFACE-STATIS-MIB", "ruijieIfIpStatisIndex"),
    (0, "RUIJIE-INTERFACE-STATIS-MIB", "ruijieIfIpstatisIPVersion"),
)
if mibBuilder.loadTexts:
    ruijieIfIpStatisEntry.setStatus("current")
_RuijieIfIpStatisIndex_Type = IfIndex
_RuijieIfIpStatisIndex_Object = MibTableColumn
ruijieIfIpStatisIndex = _RuijieIfIpStatisIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 1),
    _RuijieIfIpStatisIndex_Type()
)
ruijieIfIpStatisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpStatisIndex.setStatus("current")


class _RuijieIfIpstatisIPVersion_Type(Integer32):
    """Custom type ruijieIfIpstatisIPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ipv4", 1),
          ("ipv6", 2))
    )


_RuijieIfIpstatisIPVersion_Type.__name__ = "Integer32"
_RuijieIfIpstatisIPVersion_Object = MibTableColumn
ruijieIfIpstatisIPVersion = _RuijieIfIpstatisIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 2),
    _RuijieIfIpstatisIPVersion_Type()
)
ruijieIfIpstatisIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpstatisIPVersion.setStatus("current")
_RuijieIfIpInBitsRate_Type = Counter64
_RuijieIfIpInBitsRate_Object = MibTableColumn
ruijieIfIpInBitsRate = _RuijieIfIpInBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 3),
    _RuijieIfIpInBitsRate_Type()
)
ruijieIfIpInBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpInBitsRate.setStatus("current")
_RuijieIfIpInPktRate_Type = Counter64
_RuijieIfIpInPktRate_Object = MibTableColumn
ruijieIfIpInPktRate = _RuijieIfIpInPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 4),
    _RuijieIfIpInPktRate_Type()
)
ruijieIfIpInPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpInPktRate.setStatus("current")
_RuijieIfIpOutBitsRate_Type = Counter64
_RuijieIfIpOutBitsRate_Object = MibTableColumn
ruijieIfIpOutBitsRate = _RuijieIfIpOutBitsRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 5),
    _RuijieIfIpOutBitsRate_Type()
)
ruijieIfIpOutBitsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpOutBitsRate.setStatus("current")
_RuijieIfIpOutPktRate_Type = Counter64
_RuijieIfIpOutPktRate_Object = MibTableColumn
ruijieIfIpOutPktRate = _RuijieIfIpOutPktRate_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 6),
    _RuijieIfIpOutPktRate_Type()
)
ruijieIfIpOutPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpOutPktRate.setStatus("current")
_RuijieIfIpInOctets_Type = Counter64
_RuijieIfIpInOctets_Object = MibTableColumn
ruijieIfIpInOctets = _RuijieIfIpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 7),
    _RuijieIfIpInOctets_Type()
)
ruijieIfIpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpInOctets.setStatus("current")
_RuijieIfIpInPkts_Type = Counter64
_RuijieIfIpInPkts_Object = MibTableColumn
ruijieIfIpInPkts = _RuijieIfIpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 8),
    _RuijieIfIpInPkts_Type()
)
ruijieIfIpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpInPkts.setStatus("current")
_RuijieIfIpOutOctets_Type = Counter64
_RuijieIfIpOutOctets_Object = MibTableColumn
ruijieIfIpOutOctets = _RuijieIfIpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 9),
    _RuijieIfIpOutOctets_Type()
)
ruijieIfIpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpOutOctets.setStatus("current")
_RuijieIfIpOutPkts_Type = Counter64
_RuijieIfIpOutPkts_Object = MibTableColumn
ruijieIfIpOutPkts = _RuijieIfIpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 10, 4, 2, 1, 10),
    _RuijieIfIpOutPkts_Type()
)
ruijieIfIpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruijieIfIpOutPkts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUIJIE-INTERFACE-STATIS-MIB",
    **{"ruijieInterfaceStatisMIB": ruijieInterfaceStatisMIB,
       "ruijieIfErrStatisTable": ruijieIfErrStatisTable,
       "ruijieIfErrStatisEntry": ruijieIfErrStatisEntry,
       "ruijieIfErrStatisIndex": ruijieIfErrStatisIndex,
       "ruijieIfUnderSize": ruijieIfUnderSize,
       "ruijieIfOverSize": ruijieIfOverSize,
       "ruijieIfCollisions": ruijieIfCollisions,
       "ruijieIfFragments": ruijieIfFragments,
       "ruijieIfJabbers": ruijieIfJabbers,
       "ruijieIfCRCerror": ruijieIfCRCerror,
       "ruijieIfAlignerror": ruijieIfAlignerror,
       "ruijieIfFECerror": ruijieIfFECerror,
       "ruijieIfIpStatisTable": ruijieIfIpStatisTable,
       "ruijieIfIpStatisEntry": ruijieIfIpStatisEntry,
       "ruijieIfIpStatisIndex": ruijieIfIpStatisIndex,
       "ruijieIfIpstatisIPVersion": ruijieIfIpstatisIPVersion,
       "ruijieIfIpInBitsRate": ruijieIfIpInBitsRate,
       "ruijieIfIpInPktRate": ruijieIfIpInPktRate,
       "ruijieIfIpOutBitsRate": ruijieIfIpOutBitsRate,
       "ruijieIfIpOutPktRate": ruijieIfIpOutPktRate,
       "ruijieIfIpInOctets": ruijieIfIpInOctets,
       "ruijieIfIpInPkts": ruijieIfIpInPkts,
       "ruijieIfIpOutOctets": ruijieIfIpOutOctets,
       "ruijieIfIpOutPkts": ruijieIfIpOutPkts}
)
