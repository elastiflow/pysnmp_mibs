# SNMP MIB module (ME1200-RMIRROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/cisco_9/ME1200-RMIRROR-MIB.mib
# Produced by pysmi-1.5.11 at Sat May 24 09:05:31 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200InterfaceIndex,
 ME1200Unsigned16) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200InterfaceIndex",
    "ME1200Unsigned16")

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

me1200RmirrorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120)
)
if mibBuilder.loadTexts:
    me1200RmirrorMib.setRevisions(
        ("2014-05-08 00:00",
         "2014-05-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200RmirrorSwitchType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mirror", 0),
          ("source", 1),
          ("intermediate", 2),
          ("destination", 3))
    )



class ME1200RmirrorMirrorType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tx", 1),
          ("rx", 2),
          ("both", 3))
    )



class ME1200RmirrorPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("intermediate", 1),
          ("destination", 2),
          ("reflector", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200RmirrorMibObjects_ObjectIdentity = ObjectIdentity
me1200RmirrorMibObjects = _Me1200RmirrorMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1)
)
_Me1200RmirrorCapabilities_ObjectIdentity = ObjectIdentity
me1200RmirrorCapabilities = _Me1200RmirrorCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 1)
)
_Me1200RmirrorCapabilitiesReflectorPortSupport_Type = TruthValue
_Me1200RmirrorCapabilitiesReflectorPortSupport_Object = MibScalar
me1200RmirrorCapabilitiesReflectorPortSupport = _Me1200RmirrorCapabilitiesReflectorPortSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 1, 1),
    _Me1200RmirrorCapabilitiesReflectorPortSupport_Type()
)
me1200RmirrorCapabilitiesReflectorPortSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200RmirrorCapabilitiesReflectorPortSupport.setStatus("current")
_Me1200RmirrorCapabilitiesCpuMirrorSupport_Type = TruthValue
_Me1200RmirrorCapabilitiesCpuMirrorSupport_Object = MibScalar
me1200RmirrorCapabilitiesCpuMirrorSupport = _Me1200RmirrorCapabilitiesCpuMirrorSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 1, 2),
    _Me1200RmirrorCapabilitiesCpuMirrorSupport_Type()
)
me1200RmirrorCapabilitiesCpuMirrorSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200RmirrorCapabilitiesCpuMirrorSupport.setStatus("current")
_Me1200RmirrorConfig_ObjectIdentity = ObjectIdentity
me1200RmirrorConfig = _Me1200RmirrorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2)
)
_Me1200RmirrorConfigSessionTable_Object = MibTable
me1200RmirrorConfigSessionTable = _Me1200RmirrorConfigSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1)
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionTable.setStatus("current")
_Me1200RmirrorConfigSessionEntry_Object = MibTableRow
me1200RmirrorConfigSessionEntry = _Me1200RmirrorConfigSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1)
)
me1200RmirrorConfigSessionEntry.setIndexNames(
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSessionId"),
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionEntry.setStatus("current")


class _Me1200RmirrorConfigSessionSessionId_Type(Integer32):
    """Custom type me1200RmirrorConfigSessionSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Me1200RmirrorConfigSessionSessionId_Type.__name__ = "Integer32"
_Me1200RmirrorConfigSessionSessionId_Object = MibTableColumn
me1200RmirrorConfigSessionSessionId = _Me1200RmirrorConfigSessionSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 1),
    _Me1200RmirrorConfigSessionSessionId_Type()
)
me1200RmirrorConfigSessionSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSessionId.setStatus("current")
_Me1200RmirrorConfigSessionMode_Type = TruthValue
_Me1200RmirrorConfigSessionMode_Object = MibTableColumn
me1200RmirrorConfigSessionMode = _Me1200RmirrorConfigSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 2),
    _Me1200RmirrorConfigSessionMode_Type()
)
me1200RmirrorConfigSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionMode.setStatus("current")
_Me1200RmirrorConfigSessionSwitchType_Type = ME1200RmirrorSwitchType
_Me1200RmirrorConfigSessionSwitchType_Object = MibTableColumn
me1200RmirrorConfigSessionSwitchType = _Me1200RmirrorConfigSessionSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 3),
    _Me1200RmirrorConfigSessionSwitchType_Type()
)
me1200RmirrorConfigSessionSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSwitchType.setStatus("current")


class _Me1200RmirrorConfigSessionVid_Type(ME1200Unsigned16):
    """Custom type me1200RmirrorConfigSessionVid based on ME1200Unsigned16"""
    subtypeSpec = ME1200Unsigned16.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Me1200RmirrorConfigSessionVid_Type.__name__ = "ME1200Unsigned16"
_Me1200RmirrorConfigSessionVid_Object = MibTableColumn
me1200RmirrorConfigSessionVid = _Me1200RmirrorConfigSessionVid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 1, 1, 4),
    _Me1200RmirrorConfigSessionVid_Type()
)
me1200RmirrorConfigSessionVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionVid.setStatus("current")
_Me1200RmirrorConfigSessionSourceCpuTable_Object = MibTable
me1200RmirrorConfigSessionSourceCpuTable = _Me1200RmirrorConfigSessionSourceCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2)
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceCpuTable.setStatus("current")
_Me1200RmirrorConfigSessionSourceCpuEntry_Object = MibTableRow
me1200RmirrorConfigSessionSourceCpuEntry = _Me1200RmirrorConfigSessionSourceCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1)
)
me1200RmirrorConfigSessionSourceCpuEntry.setIndexNames(
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuSessionId"),
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuSwitchId"),
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceCpuEntry.setStatus("current")


class _Me1200RmirrorConfigSessionSourceCpuSessionId_Type(Integer32):
    """Custom type me1200RmirrorConfigSessionSourceCpuSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Me1200RmirrorConfigSessionSourceCpuSessionId_Type.__name__ = "Integer32"
_Me1200RmirrorConfigSessionSourceCpuSessionId_Object = MibTableColumn
me1200RmirrorConfigSessionSourceCpuSessionId = _Me1200RmirrorConfigSessionSourceCpuSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1, 1),
    _Me1200RmirrorConfigSessionSourceCpuSessionId_Type()
)
me1200RmirrorConfigSessionSourceCpuSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceCpuSessionId.setStatus("current")


class _Me1200RmirrorConfigSessionSourceCpuSwitchId_Type(Integer32):
    """Custom type me1200RmirrorConfigSessionSourceCpuSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200RmirrorConfigSessionSourceCpuSwitchId_Type.__name__ = "Integer32"
_Me1200RmirrorConfigSessionSourceCpuSwitchId_Object = MibTableColumn
me1200RmirrorConfigSessionSourceCpuSwitchId = _Me1200RmirrorConfigSessionSourceCpuSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1, 2),
    _Me1200RmirrorConfigSessionSourceCpuSwitchId_Type()
)
me1200RmirrorConfigSessionSourceCpuSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceCpuSwitchId.setStatus("current")
_Me1200RmirrorConfigSessionSourceCpuMirrorType_Type = ME1200RmirrorMirrorType
_Me1200RmirrorConfigSessionSourceCpuMirrorType_Object = MibTableColumn
me1200RmirrorConfigSessionSourceCpuMirrorType = _Me1200RmirrorConfigSessionSourceCpuMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 2, 1, 3),
    _Me1200RmirrorConfigSessionSourceCpuMirrorType_Type()
)
me1200RmirrorConfigSessionSourceCpuMirrorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceCpuMirrorType.setStatus("current")
_Me1200RmirrorConfigSessionSourceVlanTable_Object = MibTable
me1200RmirrorConfigSessionSourceVlanTable = _Me1200RmirrorConfigSessionSourceVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3)
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceVlanTable.setStatus("current")
_Me1200RmirrorConfigSessionSourceVlanEntry_Object = MibTableRow
me1200RmirrorConfigSessionSourceVlanEntry = _Me1200RmirrorConfigSessionSourceVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1)
)
me1200RmirrorConfigSessionSourceVlanEntry.setIndexNames(
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanSessionId"),
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanIfIndex"),
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceVlanEntry.setStatus("current")


class _Me1200RmirrorConfigSessionSourceVlanSessionId_Type(Integer32):
    """Custom type me1200RmirrorConfigSessionSourceVlanSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Me1200RmirrorConfigSessionSourceVlanSessionId_Type.__name__ = "Integer32"
_Me1200RmirrorConfigSessionSourceVlanSessionId_Object = MibTableColumn
me1200RmirrorConfigSessionSourceVlanSessionId = _Me1200RmirrorConfigSessionSourceVlanSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1, 1),
    _Me1200RmirrorConfigSessionSourceVlanSessionId_Type()
)
me1200RmirrorConfigSessionSourceVlanSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceVlanSessionId.setStatus("current")
_Me1200RmirrorConfigSessionSourceVlanIfIndex_Type = ME1200InterfaceIndex
_Me1200RmirrorConfigSessionSourceVlanIfIndex_Object = MibTableColumn
me1200RmirrorConfigSessionSourceVlanIfIndex = _Me1200RmirrorConfigSessionSourceVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1, 2),
    _Me1200RmirrorConfigSessionSourceVlanIfIndex_Type()
)
me1200RmirrorConfigSessionSourceVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceVlanIfIndex.setStatus("current")
_Me1200RmirrorConfigSessionSourceVlanMode_Type = TruthValue
_Me1200RmirrorConfigSessionSourceVlanMode_Object = MibTableColumn
me1200RmirrorConfigSessionSourceVlanMode = _Me1200RmirrorConfigSessionSourceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 3, 1, 3),
    _Me1200RmirrorConfigSessionSourceVlanMode_Type()
)
me1200RmirrorConfigSessionSourceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceVlanMode.setStatus("current")
_Me1200RmirrorConfigSessionSourcePortTable_Object = MibTable
me1200RmirrorConfigSessionSourcePortTable = _Me1200RmirrorConfigSessionSourcePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4)
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourcePortTable.setStatus("current")
_Me1200RmirrorConfigSessionSourcePortEntry_Object = MibTableRow
me1200RmirrorConfigSessionSourcePortEntry = _Me1200RmirrorConfigSessionSourcePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1)
)
me1200RmirrorConfigSessionSourcePortEntry.setIndexNames(
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortSessionId"),
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortIfIndex"),
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourcePortEntry.setStatus("current")


class _Me1200RmirrorConfigSessionSourcePortSessionId_Type(Integer32):
    """Custom type me1200RmirrorConfigSessionSourcePortSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Me1200RmirrorConfigSessionSourcePortSessionId_Type.__name__ = "Integer32"
_Me1200RmirrorConfigSessionSourcePortSessionId_Object = MibTableColumn
me1200RmirrorConfigSessionSourcePortSessionId = _Me1200RmirrorConfigSessionSourcePortSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1, 1),
    _Me1200RmirrorConfigSessionSourcePortSessionId_Type()
)
me1200RmirrorConfigSessionSourcePortSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourcePortSessionId.setStatus("current")
_Me1200RmirrorConfigSessionSourcePortIfIndex_Type = ME1200InterfaceIndex
_Me1200RmirrorConfigSessionSourcePortIfIndex_Object = MibTableColumn
me1200RmirrorConfigSessionSourcePortIfIndex = _Me1200RmirrorConfigSessionSourcePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1, 2),
    _Me1200RmirrorConfigSessionSourcePortIfIndex_Type()
)
me1200RmirrorConfigSessionSourcePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourcePortIfIndex.setStatus("current")
_Me1200RmirrorConfigSessionSourcePortMirrorType_Type = ME1200RmirrorMirrorType
_Me1200RmirrorConfigSessionSourcePortMirrorType_Object = MibTableColumn
me1200RmirrorConfigSessionSourcePortMirrorType = _Me1200RmirrorConfigSessionSourcePortMirrorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 4, 1, 3),
    _Me1200RmirrorConfigSessionSourcePortMirrorType_Type()
)
me1200RmirrorConfigSessionSourcePortMirrorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourcePortMirrorType.setStatus("current")
_Me1200RmirrorConfigSessionPortTable_Object = MibTable
me1200RmirrorConfigSessionPortTable = _Me1200RmirrorConfigSessionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5)
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionPortTable.setStatus("current")
_Me1200RmirrorConfigSessionPortEntry_Object = MibTableRow
me1200RmirrorConfigSessionPortEntry = _Me1200RmirrorConfigSessionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1)
)
me1200RmirrorConfigSessionPortEntry.setIndexNames(
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortSessionId"),
    (0, "ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortIfIndex"),
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionPortEntry.setStatus("current")


class _Me1200RmirrorConfigSessionPortSessionId_Type(Integer32):
    """Custom type me1200RmirrorConfigSessionPortSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Me1200RmirrorConfigSessionPortSessionId_Type.__name__ = "Integer32"
_Me1200RmirrorConfigSessionPortSessionId_Object = MibTableColumn
me1200RmirrorConfigSessionPortSessionId = _Me1200RmirrorConfigSessionPortSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1, 1),
    _Me1200RmirrorConfigSessionPortSessionId_Type()
)
me1200RmirrorConfigSessionPortSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionPortSessionId.setStatus("current")
_Me1200RmirrorConfigSessionPortIfIndex_Type = ME1200InterfaceIndex
_Me1200RmirrorConfigSessionPortIfIndex_Object = MibTableColumn
me1200RmirrorConfigSessionPortIfIndex = _Me1200RmirrorConfigSessionPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1, 2),
    _Me1200RmirrorConfigSessionPortIfIndex_Type()
)
me1200RmirrorConfigSessionPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionPortIfIndex.setStatus("current")
_Me1200RmirrorConfigSessionPortType_Type = ME1200RmirrorPortType
_Me1200RmirrorConfigSessionPortType_Object = MibTableColumn
me1200RmirrorConfigSessionPortType = _Me1200RmirrorConfigSessionPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 1, 2, 5, 1, 3),
    _Me1200RmirrorConfigSessionPortType_Type()
)
me1200RmirrorConfigSessionPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionPortType.setStatus("current")
_Me1200RmirrorMibConformance_ObjectIdentity = ObjectIdentity
me1200RmirrorMibConformance = _Me1200RmirrorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2)
)
_Me1200RmirrorMibCompliances_ObjectIdentity = ObjectIdentity
me1200RmirrorMibCompliances = _Me1200RmirrorMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 1)
)
_Me1200RmirrorMibGroups_ObjectIdentity = ObjectIdentity
me1200RmirrorMibGroups = _Me1200RmirrorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2)
)

# Managed Objects groups

me1200RmirrorCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 1)
)
me1200RmirrorCapabilitiesInfoGroup.setObjects(
      *(("ME1200-RMIRROR-MIB", "me1200RmirrorCapabilitiesReflectorPortSupport"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorCapabilitiesCpuMirrorSupport"))
)
if mibBuilder.loadTexts:
    me1200RmirrorCapabilitiesInfoGroup.setStatus("current")

me1200RmirrorConfigSessionTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 2)
)
me1200RmirrorConfigSessionTableInfoGroup.setObjects(
      *(("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionMode"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSwitchType"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionVid"))
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionTableInfoGroup.setStatus("current")

me1200RmirrorConfigSessionSourceCpuTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 3)
)
me1200RmirrorConfigSessionSourceCpuTableInfoGroup.setObjects(
    ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuMirrorType")
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceCpuTableInfoGroup.setStatus("current")

me1200RmirrorConfigSessionSourceVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 4)
)
me1200RmirrorConfigSessionSourceVlanTableInfoGroup.setObjects(
    ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanMode")
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourceVlanTableInfoGroup.setStatus("current")

me1200RmirrorConfigSessionSourcePortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 5)
)
me1200RmirrorConfigSessionSourcePortTableInfoGroup.setObjects(
    ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortMirrorType")
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionSourcePortTableInfoGroup.setStatus("current")

me1200RmirrorConfigSessionPortTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 2, 6)
)
me1200RmirrorConfigSessionPortTableInfoGroup.setObjects(
    ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortType")
)
if mibBuilder.loadTexts:
    me1200RmirrorConfigSessionPortTableInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

me1200RmirrorMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 120, 2, 1, 1)
)
me1200RmirrorMibCompliance.setObjects(
      *(("ME1200-RMIRROR-MIB", "me1200RmirrorCapabilitiesInfoGroup"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionTableInfoGroup"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceCpuTableInfoGroup"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourceVlanTableInfoGroup"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionSourcePortTableInfoGroup"),
        ("ME1200-RMIRROR-MIB", "me1200RmirrorConfigSessionPortTableInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200RmirrorMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-RMIRROR-MIB",
    **{"ME1200RmirrorSwitchType": ME1200RmirrorSwitchType,
       "ME1200RmirrorMirrorType": ME1200RmirrorMirrorType,
       "ME1200RmirrorPortType": ME1200RmirrorPortType,
       "me1200RmirrorMib": me1200RmirrorMib,
       "me1200RmirrorMibObjects": me1200RmirrorMibObjects,
       "me1200RmirrorCapabilities": me1200RmirrorCapabilities,
       "me1200RmirrorCapabilitiesReflectorPortSupport": me1200RmirrorCapabilitiesReflectorPortSupport,
       "me1200RmirrorCapabilitiesCpuMirrorSupport": me1200RmirrorCapabilitiesCpuMirrorSupport,
       "me1200RmirrorConfig": me1200RmirrorConfig,
       "me1200RmirrorConfigSessionTable": me1200RmirrorConfigSessionTable,
       "me1200RmirrorConfigSessionEntry": me1200RmirrorConfigSessionEntry,
       "me1200RmirrorConfigSessionSessionId": me1200RmirrorConfigSessionSessionId,
       "me1200RmirrorConfigSessionMode": me1200RmirrorConfigSessionMode,
       "me1200RmirrorConfigSessionSwitchType": me1200RmirrorConfigSessionSwitchType,
       "me1200RmirrorConfigSessionVid": me1200RmirrorConfigSessionVid,
       "me1200RmirrorConfigSessionSourceCpuTable": me1200RmirrorConfigSessionSourceCpuTable,
       "me1200RmirrorConfigSessionSourceCpuEntry": me1200RmirrorConfigSessionSourceCpuEntry,
       "me1200RmirrorConfigSessionSourceCpuSessionId": me1200RmirrorConfigSessionSourceCpuSessionId,
       "me1200RmirrorConfigSessionSourceCpuSwitchId": me1200RmirrorConfigSessionSourceCpuSwitchId,
       "me1200RmirrorConfigSessionSourceCpuMirrorType": me1200RmirrorConfigSessionSourceCpuMirrorType,
       "me1200RmirrorConfigSessionSourceVlanTable": me1200RmirrorConfigSessionSourceVlanTable,
       "me1200RmirrorConfigSessionSourceVlanEntry": me1200RmirrorConfigSessionSourceVlanEntry,
       "me1200RmirrorConfigSessionSourceVlanSessionId": me1200RmirrorConfigSessionSourceVlanSessionId,
       "me1200RmirrorConfigSessionSourceVlanIfIndex": me1200RmirrorConfigSessionSourceVlanIfIndex,
       "me1200RmirrorConfigSessionSourceVlanMode": me1200RmirrorConfigSessionSourceVlanMode,
       "me1200RmirrorConfigSessionSourcePortTable": me1200RmirrorConfigSessionSourcePortTable,
       "me1200RmirrorConfigSessionSourcePortEntry": me1200RmirrorConfigSessionSourcePortEntry,
       "me1200RmirrorConfigSessionSourcePortSessionId": me1200RmirrorConfigSessionSourcePortSessionId,
       "me1200RmirrorConfigSessionSourcePortIfIndex": me1200RmirrorConfigSessionSourcePortIfIndex,
       "me1200RmirrorConfigSessionSourcePortMirrorType": me1200RmirrorConfigSessionSourcePortMirrorType,
       "me1200RmirrorConfigSessionPortTable": me1200RmirrorConfigSessionPortTable,
       "me1200RmirrorConfigSessionPortEntry": me1200RmirrorConfigSessionPortEntry,
       "me1200RmirrorConfigSessionPortSessionId": me1200RmirrorConfigSessionPortSessionId,
       "me1200RmirrorConfigSessionPortIfIndex": me1200RmirrorConfigSessionPortIfIndex,
       "me1200RmirrorConfigSessionPortType": me1200RmirrorConfigSessionPortType,
       "me1200RmirrorMibConformance": me1200RmirrorMibConformance,
       "me1200RmirrorMibCompliances": me1200RmirrorMibCompliances,
       "me1200RmirrorMibCompliance": me1200RmirrorMibCompliance,
       "me1200RmirrorMibGroups": me1200RmirrorMibGroups,
       "me1200RmirrorCapabilitiesInfoGroup": me1200RmirrorCapabilitiesInfoGroup,
       "me1200RmirrorConfigSessionTableInfoGroup": me1200RmirrorConfigSessionTableInfoGroup,
       "me1200RmirrorConfigSessionSourceCpuTableInfoGroup": me1200RmirrorConfigSessionSourceCpuTableInfoGroup,
       "me1200RmirrorConfigSessionSourceVlanTableInfoGroup": me1200RmirrorConfigSessionSourceVlanTableInfoGroup,
       "me1200RmirrorConfigSessionSourcePortTableInfoGroup": me1200RmirrorConfigSessionSourcePortTableInfoGroup,
       "me1200RmirrorConfigSessionPortTableInfoGroup": me1200RmirrorConfigSessionPortTableInfoGroup}
)
