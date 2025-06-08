# SNMP MIB module (ARISTA-XCVR-DWDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/arista_30065/ARISTA-XCVR-DWDM-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 30 16:46:36 2025
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

aristaXcvrDwdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19)
)
if mibBuilder.loadTexts:
    aristaXcvrDwdmMIB.setRevisions(
        ("2018-08-27 00:00",
         "2018-05-16 00:00",
         "2016-03-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AristaDwdmGridSpacing(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(6250, 6250),
        ValueRangeConstraint(12500, 12500),
        ValueRangeConstraint(25000, 25000),
        ValueRangeConstraint(50000, 50000),
        ValueRangeConstraint(100000, 100000),
    )



class AristaModulationFormat(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 0),
          ("none", 1),
          ("qpsk", 2),
          ("eightQam", 3),
          ("sixteenQam", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AristaXcvrDwdmTable_Object = MibTable
aristaXcvrDwdmTable = _AristaXcvrDwdmTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1)
)
if mibBuilder.loadTexts:
    aristaXcvrDwdmTable.setStatus("current")
_AristaXcvrDwdmEntry_Object = MibTableRow
aristaXcvrDwdmEntry = _AristaXcvrDwdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1)
)
aristaXcvrDwdmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaXcvrDwdmEntry.setStatus("current")
_AristaXcvrDwdmOperChannel_Type = Unsigned32
_AristaXcvrDwdmOperChannel_Object = MibTableColumn
aristaXcvrDwdmOperChannel = _AristaXcvrDwdmOperChannel_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 1),
    _AristaXcvrDwdmOperChannel_Type()
)
aristaXcvrDwdmOperChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXcvrDwdmOperChannel.setStatus("current")
_AristaXcvrDwdmOperGrid_Type = AristaDwdmGridSpacing
_AristaXcvrDwdmOperGrid_Object = MibTableColumn
aristaXcvrDwdmOperGrid = _AristaXcvrDwdmOperGrid_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 2),
    _AristaXcvrDwdmOperGrid_Type()
)
aristaXcvrDwdmOperGrid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXcvrDwdmOperGrid.setStatus("current")
_AristaXcvrDwdmOperFrequency_Type = Unsigned32
_AristaXcvrDwdmOperFrequency_Object = MibTableColumn
aristaXcvrDwdmOperFrequency = _AristaXcvrDwdmOperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 3),
    _AristaXcvrDwdmOperFrequency_Type()
)
aristaXcvrDwdmOperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXcvrDwdmOperFrequency.setStatus("current")


class _AristaXcvrDwdmAdminChannel_Type(Unsigned32):
    """Custom type aristaXcvrDwdmAdminChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
    )


_AristaXcvrDwdmAdminChannel_Type.__name__ = "Unsigned32"
_AristaXcvrDwdmAdminChannel_Object = MibTableColumn
aristaXcvrDwdmAdminChannel = _AristaXcvrDwdmAdminChannel_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 6),
    _AristaXcvrDwdmAdminChannel_Type()
)
aristaXcvrDwdmAdminChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aristaXcvrDwdmAdminChannel.setStatus("current")
_AristaXcvrDwdmAdminGrid_Type = AristaDwdmGridSpacing
_AristaXcvrDwdmAdminGrid_Object = MibTableColumn
aristaXcvrDwdmAdminGrid = _AristaXcvrDwdmAdminGrid_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 7),
    _AristaXcvrDwdmAdminGrid_Type()
)
aristaXcvrDwdmAdminGrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aristaXcvrDwdmAdminGrid.setStatus("current")
_AristaXcvrDwdmTunable_Type = TruthValue
_AristaXcvrDwdmTunable_Object = MibTableColumn
aristaXcvrDwdmTunable = _AristaXcvrDwdmTunable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 8),
    _AristaXcvrDwdmTunable_Type()
)
aristaXcvrDwdmTunable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXcvrDwdmTunable.setStatus("current")
_AristaXcvrDwdmModulationFormat_Type = AristaModulationFormat
_AristaXcvrDwdmModulationFormat_Object = MibTableColumn
aristaXcvrDwdmModulationFormat = _AristaXcvrDwdmModulationFormat_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 9),
    _AristaXcvrDwdmModulationFormat_Type()
)
aristaXcvrDwdmModulationFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXcvrDwdmModulationFormat.setStatus("current")
_AristaXcvrDwdmAdminFrequency_Type = Unsigned32
_AristaXcvrDwdmAdminFrequency_Object = MibTableColumn
aristaXcvrDwdmAdminFrequency = _AristaXcvrDwdmAdminFrequency_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 10),
    _AristaXcvrDwdmAdminFrequency_Type()
)
aristaXcvrDwdmAdminFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aristaXcvrDwdmAdminFrequency.setStatus("current")
_AristaXcvrDwdmUncorrectedCodewords_Type = Counter64
_AristaXcvrDwdmUncorrectedCodewords_Object = MibTableColumn
aristaXcvrDwdmUncorrectedCodewords = _AristaXcvrDwdmUncorrectedCodewords_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 1, 1, 11),
    _AristaXcvrDwdmUncorrectedCodewords_Type()
)
aristaXcvrDwdmUncorrectedCodewords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaXcvrDwdmUncorrectedCodewords.setStatus("current")
_AristaXcvrDwdmMibConformance_ObjectIdentity = ObjectIdentity
aristaXcvrDwdmMibConformance = _AristaXcvrDwdmMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 2)
)
_AristaXcvrDwdmMibCompliances_ObjectIdentity = ObjectIdentity
aristaXcvrDwdmMibCompliances = _AristaXcvrDwdmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 1)
)
_AristaXcvrDwdmMibGroups_ObjectIdentity = ObjectIdentity
aristaXcvrDwdmMibGroups = _AristaXcvrDwdmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 2)
)

# Managed Objects groups

aristaXcvrDwdmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 2, 1)
)
aristaXcvrDwdmGroup.setObjects(
      *(("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmOperChannel"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmOperGrid"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmOperFrequency"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmAdminChannel"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmAdminGrid"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmTunable"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmModulationFormat"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmAdminFrequency"),
        ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmUncorrectedCodewords"))
)
if mibBuilder.loadTexts:
    aristaXcvrDwdmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaXcvrDwdmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 19, 2, 1, 1)
)
aristaXcvrDwdmMibCompliance.setObjects(
    ("ARISTA-XCVR-DWDM-MIB", "aristaXcvrDwdmGroup")
)
if mibBuilder.loadTexts:
    aristaXcvrDwdmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-XCVR-DWDM-MIB",
    **{"AristaDwdmGridSpacing": AristaDwdmGridSpacing,
       "AristaModulationFormat": AristaModulationFormat,
       "aristaXcvrDwdmMIB": aristaXcvrDwdmMIB,
       "aristaXcvrDwdmTable": aristaXcvrDwdmTable,
       "aristaXcvrDwdmEntry": aristaXcvrDwdmEntry,
       "aristaXcvrDwdmOperChannel": aristaXcvrDwdmOperChannel,
       "aristaXcvrDwdmOperGrid": aristaXcvrDwdmOperGrid,
       "aristaXcvrDwdmOperFrequency": aristaXcvrDwdmOperFrequency,
       "aristaXcvrDwdmAdminChannel": aristaXcvrDwdmAdminChannel,
       "aristaXcvrDwdmAdminGrid": aristaXcvrDwdmAdminGrid,
       "aristaXcvrDwdmTunable": aristaXcvrDwdmTunable,
       "aristaXcvrDwdmModulationFormat": aristaXcvrDwdmModulationFormat,
       "aristaXcvrDwdmAdminFrequency": aristaXcvrDwdmAdminFrequency,
       "aristaXcvrDwdmUncorrectedCodewords": aristaXcvrDwdmUncorrectedCodewords,
       "aristaXcvrDwdmMibConformance": aristaXcvrDwdmMibConformance,
       "aristaXcvrDwdmMibCompliances": aristaXcvrDwdmMibCompliances,
       "aristaXcvrDwdmMibCompliance": aristaXcvrDwdmMibCompliance,
       "aristaXcvrDwdmMibGroups": aristaXcvrDwdmMibGroups,
       "aristaXcvrDwdmGroup": aristaXcvrDwdmGroup}
)
